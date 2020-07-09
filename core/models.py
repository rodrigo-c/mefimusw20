from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Platform(models.Model):
    title = models.CharField(max_length=200)

    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Group(models.Model):
    title = models.CharField(max_length=200)
    comments = GenericRelation('Comment')
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group', args=[str(self.id)])

    def mix_set(self):
        return {'all': [i.mix for i in self.myuser_set.all()]}

    class Meta:
        ordering = ['title']

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class MyUser(AbstractUser):
    mefi_handle = models.CharField(max_length=200, null=True)
    the_group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, blank=True, null=True)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING, blank=True, null=True)

    objects = CustomUserManager()

    # def __str__(self):
    #     try:
    #         return self.mefi_handle
    #     except:
    #         return self.username

    @classmethod
    def get_email_field_name(cls):
        return 'username'

    def get_absolute_url(self):
        if hasattr(self, 'mix'):
            return self.mix.get_absolute_url()


class Mix(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    text = models.TextField(blank=True)
    # link = models.TextField()
    cover_image = models.ImageField(upload_to='covers', blank=True)
    back_image = models.ImageField(upload_to='covers', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    bg_color = models.CharField(max_length=200, default='#9cc754')
    tx_color = models.CharField(max_length=200, default='#000000')
    comments = GenericRelation('Comment')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mix', args=[str(self.id)])


class Tag(models.Model):
    title = models.CharField(max_length=1000)

    comments = GenericRelation('Comment')

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']

    def __str__(self):
        try:
            return self.title
        except:
            return 'tag'

    def get_absolute_url(self):
        return reverse('tag', args=[self.id])


class Event(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=200)

    class Meta:
        ordering = ['-datetime']


class Comment(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['datetime']

    def get_absolute_url(self):
        return self.content_object.get_absolute_url() + f"#comment-{self.id}"
