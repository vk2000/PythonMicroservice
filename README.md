
## Synopsis

An example of Dockerized Microservice using Python Flask framework

## Code Example


## Motivation

This project starts with a simple micro service using Flask framework and will eventually show dow to deploy it in AWS ECS (Elastic Container service)

## Installation

Using Dockerfile to create image:

docker build -t <image_name> .

Deploy Docker image using 

docker run -p 5001:5000 -d <image_name> 

Using docker-compose:
docker-compose build
docker-compose up


## API Reference

## Tests

You can test the app using curl command  or POSTMAN plugin for Chrome

## Contributors


## License

All code provided is AS IS. It can be used completely FREE.




