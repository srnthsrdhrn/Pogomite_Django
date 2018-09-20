from __future__ import absolute_import, unicode_literals

import json
import os
from datetime import datetime

from celery import Celery, shared_task

# set the default Django settings module for the 'celery' program.
from Pogomite import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pogomite.settings')

app = Celery('Pogomite')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Broker CONNACK response
import django
import paho.mqtt.client as mqtt

django.setup()
flag = False
client = None


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    global client
    client = mqtt.Client(client_id='srinath1234mqtt')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.hivemq.com", 1883, 60)
    sender.add_periodic_task(10.0, periodic_checking.s('hello'), name='periodic_checking')


@shared_task
def periodic_checking(args):
    from service.models import Order
    date = datetime.now()
    orders = Order.objects.filter(startDateTime__lte=date, worker_notified=False)
    for order in orders:
        user_token = order.worker.mqtt_token
        topic = settings.MQTT_ROOT_TOPIC + user_token + "/" + settings.MQTT_PASSIVE_TOPIC_STRING
        customer = order.customer
        print("topic: {}".format(topic))
        data = {"code": settings.MQTT_USER_REGISTER_TOPIC, "username": customer.username, "lat": customer.lat,
                "lng": customer.lng, "time": order.startDateTime.strftime("%d/%m/%Y %H:%M:%S")}
        client.publish(topic, json.dumps(data))
        customer_topic = settings.MQTT_ROOT_TOPIC + order.customer.mqtt_token + "/" + settings.MQTT_PASSIVE_TOPIC_STRING
        worker_topic = settings.MQTT_ROOT_TOPIC + order.worker.mqtt_token + "/" + settings.MQTT_LOCATION_TOPIC_STRING
        customer_data = {"code": settings.MQTT_CUSTOMER_UPDATE_TOPIC_STRING, "worker_topic": worker_topic}
        client.publish(customer_topic, json.dumps(customer_data))
        order.worker_notified = True
        order.save()


def on_connect(client, userdata, flags, rc):
    # Subscribing to topic and reconnect for
    global flag
    flag = True


# Receive message

def on_message(client, userdata, msg):
    pass
    # client.publish(("data/server/gpsdata/{}".format(bus_data['Busno'])), str(publish_data))
