
# 创建一个漂亮的方式来增加和编辑博客文章。 Django的管理是很酷，但是它很难去自定义，变得更漂亮。 通过forms，我们可以拥有对我们界面绝对的权利—我们能够做几乎我们能想象到的所有事情！
#
# Django表单的一个好处就是我们既可以从零开始自定义，也可以创建ModelForm，它将表单的结果保存到模型里。
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
