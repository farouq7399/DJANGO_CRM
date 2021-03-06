from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', landing_page),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('', include('leads.urls')),
    path('', include('agents.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
