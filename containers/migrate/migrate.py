from redminelib import Redmine
import mysql.connector

import settings


# This sample script is the basis for migrating data from a MySQL source
# database. But it does nothing more than demonstrate how you establish a
# connection fomr your source database, and to the destination redmine instance.
# If your source data is actually stored in another type of backend, update
# requires.txt, adding the necessary Python library to speak to the backend,
# and import it above instead of mysql.connector.

# Connect to the source database.
mysql_db = mysql.connector.connect(
    host=settings.source_hostname, user=settings.source_username,
    password=settings.source_password, database=settings.source_database,
)

# In order to migrate data via the Redmine API, it must be enabled. Log in to
# Redmine as an administrator, and visit Administration, Settings, API and
# check 'Enable REST web service'. Then, click "My account" and show your
# API access key, updating it in settings.py.

# Connect to the destintation redmine API.
redmine = Redmine(settings.destination_url,
    key=settings.destination_api_key,
)

# Now SELECT items from your source, and create() them in your destination.
# https://python-redmine.com/introduction.html
