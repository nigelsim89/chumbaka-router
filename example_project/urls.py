from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from portal import urls as portal_urls

from game import urls as game_urls
from game import python_den_urls

admin.autodiscover()

urlpatterns = [
    # Send homepage directly to Rapid Router
    path(
        "",
        RedirectView.as_view(
            url="/rapidrouter/",
            permanent=False
        ),
        name="home",
    ),

    path("administration/", admin.site.urls),
    re_path(r"^rapidrouter/", include(game_urls)),
    re_path(r"^pythonden/", include(python_den_urls)),

    # Keep portal URLs available for anything Rapid Router still depends on
    re_path(r"^", include(portal_urls)),
]
