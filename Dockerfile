FROM python:3.8
WORKDIR /app
COPY run /usr/local/bin
COPY app /app
RUN chmod +x /usr/local/bin/run && \
    pip install tools && \
    pip install wget && \
    chmod -R +x .

CMD ["/usr/local/bin/run"]