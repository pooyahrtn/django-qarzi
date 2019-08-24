export DJANGO_DEBUG=False
export DJANGO_CONFIGURATION=Production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build