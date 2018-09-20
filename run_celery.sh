#!/bin/sh
celery -A Pogomite worker -l info --autoscale=10,1 -B