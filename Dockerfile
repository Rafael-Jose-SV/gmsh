FROM ubuntu:22.04

COPY . /app

WORKDIR /app

ARG PORT
ENV PORT=$PORT

RUN apt-get update && apt-get upgrade -y
RUN apt-get install gmsh -y
RUN apt-get install pip -y
RUN pip install --upgrade pip
RUN pip install gmsh
RUN pip install fastapi
RUN pip install "uvicorn[standard]"

EXPOSE $PORT

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "${PORT}"]