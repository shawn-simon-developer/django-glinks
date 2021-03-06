# About Django-Glinks

Django-Glinks is a simple internal ad manager for django sites. A glink is a "Graphical Link" which when slammed together in pure creative bliss you get glink!

**NOTE: Do NOT use the word ad, advertisement, advertise, or anything that would make an ad blocker think your glink is an advertisement!**

What glink provides is a way to host your own ads on your site as a simple image so that ad-blocker will not block your add.This image, when clicked, will lead to the link of your choice while also counting the impressions and the clicks interally by redirecting back to your site backend then to the link for the ad. These properties are READ ONLY and should stay that way for integrity of your impression and click counts. Don't be sketchy...

Each glink also comes with a weight from 0 to 9. Glinks with a rating of 0 will never be shown and glinks from 1-9 have a greater and greater chance of being shown (9 being most likely). Each glink has an associated "blueprint" to outline its type. The blueprint has properties such as a name, height, and width. This is because ads are often associated as "medium-rectangle" or "header" with respective sizes known more so by the developers or admin. Therefore each glink must be associated to a blueprint and therefore you can have an ad of your desired size show up where you want by simply using the template tag shown below.

Understanding that ads are really annoying to a lot of people, please use responsibly. 

# Quick Start/Installation

You can install django-glinks either from source at https://pypi.python.org/pypi/django-glinks or by simply using pip install.

```python
pip install django-glinks
```
Once installed, you must include the app in your settings.py.

```python

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'glinks',
)
```

Next, we need to add a url to allow django to redirect to our glink link. In your urls.py file you must add the glink url.

```python
from glinks.views import glink_counter

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ...

    url(r'^glink/([0-9]+)/$', glink_counter, name="glink_counter")
)
```

In order to gave our impression and click location tracking we need to add these context prossesors.

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    )
```

From there you can head into your admin pannel and add some glinks with blueprints of your choice. On this github I have included some with some horrible images that don't even match the resolution of the blueprint. To include a glink in your template you simple load glinks and then place a glink with the blueprint you desire.

```python
{% load glink %}

{% glink with blueprint='header' %}
```

