import django
# just returns current installed django version for the footer
def django_version(request):
    return {'django_current_version': django.__version__}
