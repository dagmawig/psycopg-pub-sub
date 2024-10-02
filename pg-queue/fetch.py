import psycopg
import asyncio
from psycopg.rows import dict_row
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# this function fetches messages from the message table
async def fetch(connection_str: str, channel: str, start_date: str, end_date=datetime.today().strftime('%Y-%m-%d'), **kwargs):
    
    con = await psycopg.AsyncConnection.connect(connection_str)
    cur = con.cursor(row_factory=dict_row)

    # build the filter sql string
    # this filter looks through the data column to find rows that fit the key-value pairs
    filter_sql = ''
    for key, value in kwargs.items():
        filter_sql += f' and m."data" @> \'{{"{key}":"{value}"}}\''
    print(filter_sql)    

    # this builds the total sql string that fetches the messages
    sql = f"SELECT * FROM queue.message m WHERE m.channel = '{channel}' and m.created_at >= '{start_date}' and m.created_at < '{end_date}'{filter_sql}"
    await cur.execute(sql)

    rows = await cur.fetchall()

    await cur.close()
    return rows
    
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(fetch(connection_str=os.environ.get('CONNECTION_URL'), channel='news', start_date='2024-09-23', name='DAG'))