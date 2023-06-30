#!/bin/bash

cp config/.env.example config/.env

SECRET_KEY=$(openssl rand -hex 32)

sed -i "s/SECRET_KEY=.*/SECRET_KEY=$SECRET_KEY/g" config/.env
