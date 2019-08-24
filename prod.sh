#!/bin/bash
export DJANGO_DEBUG=False
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build