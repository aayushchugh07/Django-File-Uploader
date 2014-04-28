from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                (r'polls/','polls.views.index'),
                (r'doregister/','fileapp.views.doregister'),
                (r'dosignin/','fileapp.views.dosignin'),
                (r'dosignout/','fileapp.views.dosignout'),
                (r'register/','fileapp.views.register'),
                (r'signin/','fileapp.views.signin'),
                (r'home/','fileapp.views.home'),
                (r'upload/','fileapp.views.upload'),
                (r'download/','fileapp.views.download'),
                (r'error/','fileapp.views.error'),
                (r'.*/','fileapp.views.home'),
                
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
