FROM python

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py
COPY numericals.csv numericals.csv

ENTRYPOINT [ "python", "pipeline.py" ]
