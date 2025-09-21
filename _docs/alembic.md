# Database Migration Commands for Flask

## Initializing Flask-Migration

### Initialize Flask-Migration

`flask db init`

### Generate an initial migration or generate migration on model change

`flask db migrate -m "initial migration"`

### Generate a migration

`flask db revision -m "migration message"`

### Apply migrations

`flask db upgrade`
