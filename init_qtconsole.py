import os
import django

os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
django.setup()