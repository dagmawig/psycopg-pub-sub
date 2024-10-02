import pytest
import asyncio
import sys
import os

rootpath = os.path.join(os.getcwd(), 'pg-queue')
sys.path.append(rootpath)
from fetch import fetch
from publish import publish

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@pytest.mark.asyncio
async def test_async_fetch():
    result = await fetch(connection_str=os.environ.get('CONNECTION_URL'), channel='news', start_date='2024-09-23', end_date='2024-09-24', name='DAG')
    subset = {'channel': 'news', 'data': {'name':'DAG'}}
    assert subset.items() <= result[0].items()

@pytest.mark.asyncio
async def test_async_publish():
    result = await publish(connection_str=os.environ.get('CONNECTION_URL'), channel='news', data={'topic': 'business'})
    subset = {'channel': 'news', 'data': {'topic': 'business'}}
    assert subset.items() <= result.items()