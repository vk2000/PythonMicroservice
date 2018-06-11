FROM python:3.6.5

# set working directory
RUN mkdir -p /app
WORKDIR /app

# add requirements
COPY ./requirements.txt .

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /app


# run server
WORKDIR ./bin
CMD ./start_infinity_service.sh

