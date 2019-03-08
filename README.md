# A simple Redmine container

A simple starting point for testing Redmine in a container, using a MariaDB
(MySQL) database in another container.

## Installation

Clone this repository, cd into the redmine-container directory, and then run
the following commands:
```
	docker-compose build && docker-compose up
```

Then visit the following URL to configure the wiki:
	http://localhost:8088/

To ssh into the container, use the following command:
```
	docker exec -it redmine bash
```

To log in as the site administrator, log in as `admin`/`admin` as documented
here:
https://www.redmine.org/projects/redmine/wiki/RedmineInstall#Step-10-Logging-into-the-application

## Redmine

For full details, visit http://www.redmine.org/

> Redmine is a flexible project management web application. Written using the
> Ruby on Rails framework, it is cross-platform and cross-database.
>
> Redmine is open source and released under the terms of the GNU General Public
> License v2 (GPL).

## Customizations

The starting place is two official containers:
 - https://hub.docker.com/_/redmine/
 - https://hub.docker.com/_/mariadb/

### Listening port (default: 3000)

The Ruby on Rails server listens on port 3000. To change which port the
container responds to, edit `docker-compose.yml` changing the _first_ occurence
of 3000:
```
   ports:
    - "3000:3000"
```
from `3000` to your desired port. For example, to change to port 80, you'd edit
it to be as follows:
```
   ports:
    - "80:3000"
```
