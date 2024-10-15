import psycopg

# subscribe client to a channel
async def subscribe(connection_str: str, channel: str):
    
    try:
        con = psycopg.connect(connection_str, autocommit=True)
        con.execute(f'LISTEN {channel}')
        gen = con.notifies()
    except:
        print('subscribe error!')
    return gen
