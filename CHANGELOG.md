# Changelog

## 0.5.0 (2023-08-21)

### Feat

- **apps/users**: add the initial users view

## 0.4.0 (2023-08-06)

### Feat

- **apps/authentication**: create initial authentication app

### Fix

- **server/settings**: add the Heroku domain to the allowed hosts

## 0.3.0 (2023-08-04)

### Feat

- add a settings file for production
- set a custom view for 404 page
- **core/middlewares**: delete many headers until we need them
- **server**: add a custom middleware to remove useless headers

### Fix

- **server**: enable all CORS origins on development
- **server**: set the default renderer class
- disable collect static configuration on heroku app
- add database url to the heroku app schema
- add config vars to the heroku app schema

## 0.2.0 (2023-07-23)

### Feat

- **apps/users**: Add support to users tokens
- **users**: initial users feature development

### Fix

- **apps/users**: Cast user token to string
- **users**: Remove checks when creating a new user

## 0.1.0 (2023-07-01)

### Feat

- add integration with postgresql
- add pre-commit hooks
- initial app development

### Fix

- add shebang to `manage.py` file
- **docker**: fix docker compose config file
