from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 获取从第j篇开始的最多10篇posts的abstract
    url(r'^post/abstract/$', 'blog.views.get_abstract_10', name='abstract_10'),
    # 获取分类c_id的从第j篇开始的最多10篇posts的abstract
    url(r'^post/abstract/(\d+)/$', 'blog.views.get_abstract_c_10', name='abstract_c_10'),
    # 获取id为post_id的post全文
    url(r'^post/(\d+)/$', 'blog.views.get_a_post', name='a_post'),
)
