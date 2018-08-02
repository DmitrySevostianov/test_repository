
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework_project.settings')

application = get_wsgi_application()
'''

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework_project.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
'''