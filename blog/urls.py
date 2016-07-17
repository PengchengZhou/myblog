from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 获取分类列表
    url(r'^classification_list$', 'blog.views.get_classification_list', name='classification_list'),
    # 获取访问量排行前10的posts
    url(r'^rank_10$', 'blog.views.get_rank_10', name='rank_10'),
    # 获取从第j篇开始的最多10篇posts的abstract
    url(r'^post/abstract/(\d+)$', 'blog.views.get_abstract_10', 'abstract_10'),
    # 获取分类c_id的从第j篇开始的最多10篇posts的abstract
    url(r'^post/abstract/(\d+)/(\d+)$', 'blog.views.get_abstract_c_10', 'abstract_c_10'),
    # 获取id为post_id的post全文
    url(r'^post/(\d+)$', 'blog.views.get_a_post', name='a_post'),
)
