from django.forms import ModelForm

from blog.models import ModelBlog


class CreateMessageForm(ModelForm):
    class Meta:
        model = ModelBlog
        fields = ['title', 'content']