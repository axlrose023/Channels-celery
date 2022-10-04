import requests
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


@shared_task()
def get_joke():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url).json()
    fact = response['fact']
    async_to_sync(channel_layer.group_send)('jokes', {'type': 'send_jokes', 'text': fact})

#####Run celery, redis
# celery -A channelsproj beat -l INFO
# celery -A channelsproj worker --pool=solo  -l INFO
