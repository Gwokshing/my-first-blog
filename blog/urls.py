from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # (?P<pk>[0-9]+)表示Django会把所有你放到这里的东西转变成一个称作pk的变量并传递给视图。 [0-9]也告诉我们它只能由数字，
    # 而不是字母（所以是取值范围是介于0和9之间）。 + 意味着需要一个或更多的数字。pk 是 primary key（主键）的缩写.
]