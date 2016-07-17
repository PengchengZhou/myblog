from django.shortcuts import render
from .models import Classification, Post
from django.http import HttpResponse

# Create your views here.

def home(req):
    '''
    主页
    '''
    # 分类列表
    c_list = Classification.objects.all()
    # 访问量前10的post abstract
    rank_10_abstract = Post.objects.order_by('-visit_count').values('id', 'title', 'visit_count')[:10]
    # 最近的10篇post abstract
    latest_10_abstract = Post.objects.order_by('-pub_date').values('id', 'title', 'visit_count', 'pub_date', 'abstract')[:10]

    print(rank_10_abstract)

    response = render(req, 'home.html', {
        'c_list': c_list,
        'rank_10_abstract': rank_10_abstract,
        'latest_10_abstract': latest_10_abstract,
    })

    for c in c_list:
        response.set_cookie('c_start_' + str(c.id), 1)
    response.set_cookie('latest_now', len(latest_10_abstract))

    return response


def get_abstract_10(req):
    '''
    获取从第j篇开始的最多10篇posts的abstract
    '''
    return HttpResponse('hello')


def get_abstract_c_10(req, c_id):
    '''
    获取分类c_id的从第j篇开始的最多10篇posts的abstract
    '''
    return HttpResponse('hello')


def get_a_post(req, post_id):
    '''
    获取id为post_id的post全文
    '''
    return HttpResponse('hello')
