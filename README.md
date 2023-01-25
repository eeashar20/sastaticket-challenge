# Storefront

# Project Setup
Following are the commands to setup the project

```shell
pipenv install
```

```shell
python manage.py runserver
```

# Docker Setup
The docker containers runs the backend code for the storefront web application. The application is built with 
Python3.9 and runs on python docker image ```python:3.10.9```. 

## Getting Started

In order to run the docker containers you must download this code on your machine and have the required
dependencies install. 

### Prerequisities

In order to run the containers you'll need docker installed, for which platform specific instructions can be found by 
clicking any of the below mentioned links

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Build Image for the Container

To build the image use the following command

```shell
docker build -t storefront:dev .
```

#### Running the container

```shell
docker run -d -p 8080:8000 --restart always --name storefront-dev storefront:dev

```

## Built With

- Python python:3.10.9

## Find Us

- [GitHub](https://github.com/OptimumGrading/backend)

## Authors

- **Ashar Haroon**
