from django.db import models
from django.core.urlresolvers import reverse
import django.utils.timezone as timezone

# Create your models here.

class ArticleType(models.Model):
    type_id = models.IntegerField(unique=True) #类型ID
    name = models.CharField(max_length=50,blank=False) #类型名称
    
    def __unicode__(self) :
        return self.name


class Article(models.Model) :
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, default="onion")
    likes = models.IntegerField(default=0)
    reads = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    picture = models.CharField(max_length=200, blank=True, default="blog_default.png")
    category = models.CharField(max_length=50, blank=True)  #博客标签
    #category = models.ForeignKey(ArticleType, on_delete=models.CASCADE)  #博客标签
    date_time = models.DateTimeField(auto_now_add=True)  #博客日期
    modify_time = models.DateTimeField(default=timezone.now)
    content = models.TextField(blank=True, null=True)  #博客文章正文

    #博客置顶
    TOP_CHOICES=(
        ('t',u'置顶'),
        ('g',u'一般'),
    )
    top = models.CharField(verbose_name=u'置顶', max_length=1,choices=TOP_CHOICES, default='g')
    
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://139.199.227.244:8080%s" % path

    def __unicode__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-top','-modify_time']


