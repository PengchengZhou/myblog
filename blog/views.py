from django.shortcuts import render

# Create your views here.

def home(req):
    '''
    主页
    '''
    return render(req, 'home.html')


def get_classification_list(req):
    '''
    获取分类列表
    '''
    pass


def get_rank_10(req):
    '''
    获取访问量排行前10的posts
    '''
    pass


def get_abstract_10(req, j):
    '''
    获取从第j篇开始的最多10篇posts的abstract
    '''
    pass


def get_abstract_c_10(req, c_id, j):
    '''
    获取分类c_id的从第j篇开始的最多10篇posts的abstract
    '''
    pass

def get_a_post(req, post_id):
    '''
    获取id为post_id的post全文
    '''
    pass
