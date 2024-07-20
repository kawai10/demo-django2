#!/bin/bash
FOLDER="/home/ec2-user/django_web"

if [ -d ${FOLDER} ]
then
  sudo rm -rf ${FOLDER}
else
  cd ${FOLDER}
  docker-compose down
fi