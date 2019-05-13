### Before moving on, install some additional libraries that you will use later:

Requests-OAuthlib: OAuth for Humans for handling sign-in and OAuth token flows, and for making calls to Microsoft Graph.
PyYAML for loading configuration from a YAML file.
python-dateutil for parsing ISO 8601 date strings returned from Microsoft Graph

pipenv install requests_oauthlib 
pipenv install pyyaml 
pipenv install python-dateutil

cd 66_MicrosoftGraph_Django/graph_tutorial
cd DannyJRa.github.io/66_MicrosoftGraph_Django/graph_tutorial/

python manage.py runserver

### test