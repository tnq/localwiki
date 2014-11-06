from django.conf.urls import *
from django.views.generic import TemplateView 

urlpatterns = patterns('',
#    url(r'^register/$', RegistrationView.as_view,
#        {'backend': 'users.registration_backend.SaplingBackend'},
#        name='registration_register'),
    url(r'^register/closed/$', TemplateView.as_view(
            template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
    (r'', include('registration.auth_urls')),
)
