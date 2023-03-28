from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class Item(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True



class Video(Item):
    video_source = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def type(self):
        return 'video'



class Article(Item):
    content = models.TextField()

    def __str__(self):
        return self.title

    @property
    def type(self):
        return 'article'



class Section(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    cours = models.ForeignKey('Cours', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    @property
    def items(self):
        items = []
        items += self.video_set.all()
        items += self.article_set.all()
        items.sort(key=lambda x: x.create_at, reverse=True)
        return items
        


class Cours(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='cours-thumbnails/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Cours"

    @property
    def sections(self):
        return self.section_set.all().order_by('-create_at')
    
    @property
    def items(self):
        sections = self.section_set.all()
        items = []
        for section in sections:
            items += section.video_set.all()
            items += section.article_set.all()

        return items
    
    @property
    def items_count(self):
        return len(self.items)
    
    @property
    def videos(self):
        sections = self.section_set.all()
        videos = []
        for section in sections:
            videos += section.video_set.all()

        return videos

    @property
    def videos_count(self):
        return len(self.videos)

    @property
    def articles(self):
        sections = self.section_set.all()
        articles = []
        for section in sections:
            articles += section.article_set.all()

        return articles

    @property
    def articles_count(self):
        return len(self.articles)