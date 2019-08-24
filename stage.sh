#!/bin/bash
# pip freeze > ./api/requirements.txt
export DJANGO_CONFIGURATION=Local
docker-compose -f docker-compose.yml -f docker-compose.stage.yml up "$@"