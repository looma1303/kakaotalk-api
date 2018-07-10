from django.conf.urls import urls


urlpatterns = [
    url(r'^keyboard/', 'kakao.views.keyboard'),
    url(r'^message', 'kakao.views.answer'),
    
]
