import os


def django_initialize():
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curso_python.settings")
        from django.core.wsgi import get_wsgi_application

        get_wsgi_application()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    django_initialize()
