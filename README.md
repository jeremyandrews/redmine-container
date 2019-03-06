# A simple Redmine container

A simple starting point for hosting Redmine in a container.

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

> Redmine is a flexible project management web application. Written using the Ruby on Rails framework, it is cross-platform and cross-database.
>
> Redmine is open source and released under the terms of the GNU General Public License v2 (GPL).

## Customizations

The starting place is two official containers:
 - https://hub.docker.com/_/redmine/
 - https://hub.docker.com/_/postgres/

### Listening port (default: 8088)

The Ruby on Rails server listens on port 3000, however it's been exposed on ports
8088 in `docker-compose.yml`. To change which port the container responds to,
edit `docker-compose.yml` changing:
```
   ports:
    - "8088:3000"
```
from `8088` to your desired port.
