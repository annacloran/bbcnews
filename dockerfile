FROM python
RUN mkdir /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY bbc_news_scrape.py /code/
CMD ["python","/code/bbc_news_scrape.py"]