from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # 默认情况下， ``QuerySet`` 返回的结果是根据模型 ``Meta`` 中的 ``ordering`` 选项给出的排序元组排序
        ordering = ('-pub_date',)
        def __str__(self):#回傳必須是字串
            return self.title

#默认情况下，QuerySet 根据模型 Meta 类的 ordering 选项排序。要使用特定的排序方法时可以用 order_by()：

#例如，要按 pub_date 字段升序排列，使用以下方法：

#ordering = ['pub_date']
#要按 pub_date 降序排列，请使用：

#ordering = ['-pub_date']
#要按 pub_date 降序，然后按 author 升序，请使用：