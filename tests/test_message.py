import pytest
import asyncio
import sys
import os

rootpath = os.path.join(os.getcwd(), 'pg-queue')
sys.path.append(rootpath)
from fetch import fetch

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@pytest.mark.asyncio
async def test_async_fetch():
    result = await fetch(connection_str=os.environ.get('CONNECTION_URL'), channel='news', start_date='2024-09-23', name='DAG')
    subset = {'channel': 'news', 'data': {'name':'DAG'}}
    assert subset.items() <= result[0].items()
   