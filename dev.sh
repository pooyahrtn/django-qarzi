#!/bin/bash
pip freeze > ./api/requirements.txt
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up