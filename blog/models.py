from django.db import models
import json

# Create your models here.

class Classification(models.Model):
    '''
    文章分类
    '''
    # 分类名
    name = models.TextField(default='')
    # 该分类的文章数
    post_num = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' (' + str(self.post_num) + ')'


class Post(models.Model):
    '''
    文章
    '''
    # 外键约束，文章分类
    classification = models.ForeignKey(Classification)
    # 文章标题
    title = models.TextField(default='')
    # 访问量
    visit_count = models.IntegerField(default=0)
    # 发布时间
    pub_date = models.DateField(auto_now=True, auto_now_add=True)
    # 文章摘要
    abstract = models.TextField(default='')
    # 文章全文
    content = models.TextField(default='')

    def __str__(self):
        return self.title

    def get_json_abstract(self):
        data = {}
        data['id'] = int(self.id);
        data['title'] = str(self.title)
        data['visit_count'] = int(self.visit_count)
        data['pub_date'] = str(self.pub_date)
        data['abstract'] = str(self.abstract)
        return json.dumps(data)

    def get_json_content(self):
        data = {}
        data['id'] = int(self.id)
        data['title'] = str(self.title)
        data['visit_count'] = int(self.visit_count)
        data['pub_date'] = str(self.pub_date)
        data['content'] = str(self.content)
        return json.dumps(data)

    def _do_insert(self, *args, **kwargs):
        '''
        覆盖_do_insert方法,以便在新添加post的时候自动增加相应文章分类的计数
        '''
        self.classification.post_num += 1
        self.classification.save()
        super(Post, self)._do_insert(*args, **kwargs)


    def delete(self, *args, **kwargs):
        '''
        覆盖delete方法,以便在删除post的时候自动减小相应文章分类的计数
        '''
        self.classification.post_num -= 1
        self.classification.save()
        super(Post, self).delete(*args, **kwargs)
