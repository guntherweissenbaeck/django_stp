# The STP (Stadttaubenprojekt)

## Add Test Data

To add testdata, use the loaddata functionality of django:

```bash
docker exec -ti django_stp_web_1 python3 manage.py loaddata fixtures/defaultUser.json
```

## Test Account

The test account you can use:

- user: admin
- password: abcdef

## Deployment

This is a little reminder what you will need to deploy the app.

### Secret Key

Generate Secret Key:
```bash
openssl rand -base64 36
```

## How to use this project?

### Development

Build the images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Test it out:

1. [http://stp.localhost:8008/](http://stp.localhost:8008/)

### Production

Update the domain in *docker-compose.prod.yml*, and add your email to *traefik.prod.toml*.

Build the images and run the containers:

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
```

