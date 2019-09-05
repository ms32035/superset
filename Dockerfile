FROM amancevice/superset
USER root
RUN pip install -U redis flower
USER superset
ADD superset_config.py /etc/superset/superset_config.py