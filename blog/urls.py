from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 通过ajax获取第k页的post abstract
    url(r'^ajax_abstract$', 'blog.views.ajax_get_abstract', name='ajax_abstract'),
    # 获取从第k页的post abstract全页面
    url(r'^abstract/(\d+)$', 'blog.views.get_abstract', name='abstract'),

    # 通过ajax获取分类i的第k页post abstract
    url(r'^ajax_abstract_c$', 'blog.views.ajax_get_abstract_c', name='ajax_abstract_c'),
    # 获取分类i的第k页post abstract全页面
    url(r'^abstract_c/(\d+)/(\d+)/$', 'blog.views.get_abstract_c', name='abstract_c'),

    # 通过ajax获取id为post_id的post全文
    url(r'^ajax_a_post$', 'blog.views.ajax_get_a_post', name='ajax_a_post'),
    # 获取页面/post/id
    url(r'^post/(\d+)$', 'blog.views.get_post_page', name='post_page'),
)
