FROM python:3.8-slim

WORKDIR /home/app

COPY ./dist/main /home/app

EXPOSE 80

CMD ["/home/app/main"]
