FROM python:3.12


RUN pip install celery django_celery_beat

COPY . .


# CMD ["celery","-A","masterjet","--app=celeryconf.app","worker","-l","info","--scheduler","django_celery_beat.schedulers:DatabaseScheduler"]
CMD ["celery","-A","masterjet","beat","-l","info","--scheduler","django_celery_beat.schedulers:DatabaseScheduler"]
