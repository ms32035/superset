FROM amancevice/superset
USER root
RUN pip install -U redis
USER superset
ADD superset_config.py /etc/superset/superset_config.py