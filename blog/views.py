from django.shortcuts import render
from .models import Classification, Post
from django.http import HttpResponse
import json

# Create your views here.

def home(req):
    '''
    主页
    '''
    # 分类列表
    c_list = Classification.objects.all()
    # 访问量前5的post abstract
    rank_5_abstract = Post.objects.order_by('-visit_count').values('id', 'title', 'visit_count')[:5]
    # 最近的8篇post abstract
    latest_8_abstract = Post.objects.order_by('-pub_date').values('id', 'title', 'visit_count', 'pub_date', 'abstract')[:8]

    return render(req, 'home.html', {
        'c_list': c_list,
        'rank_5_abstract': rank_5_abstract,
        'latest_8_abstract': latest_8_abstract,
    })


def ajax_get_abstract(req):
    '''
    通过ajax获取第page_num页的post abstract
    '''
    page_num = int(req.POST['page_num'])
    start = (page_num-1)*8
    end = page_num*8
    posts = Post.objects.order_by('-pub_date')
    abstracts = []
    if len(posts)>start:
        for post in posts[start:end]:
            abstracts.append(post.get_json_abstract())
    response_data = {}
    response_data['page_num'] = page_num
    response_data['abstracts'] = abstracts

    return HttpResponse(json.dumps(response_data), content_type='application/json')


def get_abstract(req, page_num):
    '''
    获取第page_num页的post abstract 全页面
    '''
    # 分类列表
    c_list = Classification.objects.all()
    # 访问量前5的post abstract
    rank_5_abstract = Post.objects.order_by('-visit_count').values('id', 'title', 'visit_count')[:5]
    return render(req, 'abstract_page.html', {
        'c_list': c_list,
        'rank_5_abstract': rank_5_abstract,
        'page_num': page_num,
    })


def ajax_get_abstract_c(req):
    '''
    通过ajax获取分类id为c_id，第page_num页的post abstract
    '''
    c_id = int(req.POST['c_id'])
    page_num = int(req.POST['page_num'])
    classification = Classification.objects.get(id=c_id)
    posts = classification.post_set.order_by('-pub_date')
    start = (page_num-1)*8
    end = page_num*8
    abstracts = []
    if len(posts)>start:
        for post in posts[start:end]:
            abstracts.append(post.get_json_abstract())
    response_data = {}
    response_data['c_id'] = c_id
    response_data['page_num'] = page_num
    response_data['abstracts'] = abstracts

    return HttpResponse(json.dumps(response_data), content_type='application/json')


def get_abstract_c(req, c_id, page_num):
    '''
    获取分类id为c_id，第page_num页的post abstract全页面
    '''
    # 分类列表
    c_list = Classification.objects.all()
    # 访问量前5的post abstract
    rank_5_abstract = Post.objects.order_by('-visit_count').values('id', 'title', 'visit_count')[:5]
    return render(req, 'abstract_c_page.html', {
        'c_list': c_list,
        'rank_5_abstract': rank_5_abstract,
        'c_id': c_id,
        'page_num': page_num,
    })


def ajax_get_a_post(req):
    '''
    通过ajax获取id为id的post全文
    '''
    post_id = int(req.POST['id'])
    a_post = Post.objects.get(id=post_id)
    a_post.visit_count += 1
    a_post.save()
    response_data = a_post.get_json_content()

    return HttpResponse(response_data, content_type='application/json')


def get_post_page(req, post_id):
    '''
    获取显示id为post_id的整个页面
    '''
    # 分类列表
    c_list = Classification.objects.all()
    # 访问量前5的post abstract
    rank_5_abstract = Post.objects.order_by('-visit_count').values('id', 'title', 'visit_count')[:5]
    return render(req, 'post_page.html', {
        'c_list': c_list,
        'rank_5_abstract': rank_5_abstract,
        'post_id': post_id,
    })

