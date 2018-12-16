FROM debian

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install Flask
RUN pip3 install twitter

CMD ["mkdir","/flask"]
ADD ./server/ /flask/

ENTRYPOINT ["python3","/flask/main.py"]
EXPOSE 80 443 8080 8081
