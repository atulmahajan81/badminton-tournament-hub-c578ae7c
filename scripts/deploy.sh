#!/bin/bash

set -e

ssh $DEPLOY_USER@$DEPLOY_HOST << 'ENDSSH'
cd /path/to/your/app

git pull origin main
docker-compose -f docker-compose.yml -f docker-compose.prod.yml pull

docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

./scripts/migrate.sh
ENDSSH