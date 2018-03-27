# **WAD2 Project:** YAPS

### Developed by:
> Andrew
Jim
Sean
Z`hengren

#### Project URLs

#### IMPORTANT INFORMATION

1. Requirements file is included. Create a new virtual environment with mkvirtualenv, then install requirements from the given file with

```sh
$ pip install -r requirements.txt
```
2. **Google Maps Javascript API key**

Before running the app, you require an API key to generate a map for the fives/\<game> and fives/about_us pages.
In the fives directory, nested inside the main wad2_project directory, is the file context_processors.py. Within this file is one method: api_key_processor. This passes the api key to the context for every template - line 6 assigns the api key to the variable api_key. There is a comment notifying you where you are required to paste the key (this should be of type string). To obtain an api key, follow the link below:
https://developers.google.com/maps/documentation/javascript/get-api-key

3. **Unit Tests**

The unit tests have been split into separate files, located in wad_project/fives/tests. To run coverage, use the following command:
```sh
$ coverage run manage.py test fives.tests
```

---
#### Description

---
#### External Sources
* Django (1.11.7):
* https://docs.djangoproject.com/en/2.0/releases/1.11.7/
* JQuery (& Plugins):
* https://jquery.com/
* https://mottie.github.io/tablesorter/docs/
* https://jqueryvalidation.org/
* Bootstrap:
* https://getbootstrap.com/
* Geopy (1.11.0):
* https://geopy.readthedocs.io/en/1.11.0/
* Coverage (4.5.1):
* https://coverage.readthedocs.io/en/coverage-4.5.1/
* Google Maps Javascript API:
* https://developers.google.com/maps/documentation/javascript/tutorial


