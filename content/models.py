from django.db import models
from django.db.models.fields import related
from taggit.managers import TaggableManager
from datetime import datetime  
from django.core.exceptions import ValidationError
class Movie(models.Model):
    title = models.CharField(max_length=512, blank=True, null=True, verbose_name='Name of the movie: ')
    moviefile = models.FileField(verbose_name='Upload the movie: ', blank=True)
    movielink = models.CharField(max_length=512,blank=True, null=True, verbose_name='OR | Enter the upload location url', help_text="If a URL is mentioned even when a file is uploaded, then the uploaded file will be shown instead of the file on the URL.")
    subtitle_file = models.FileField(verbose_name='Upload the subtitles file: ')
    trailer_file = models.FileField(blank=True, null=True, verbose_name='Upload the trailer file: ')
    poster_file = models.FileField(upload_to='posters', max_length=512, verbose_name='Upload a poster file: ')
    releasedate = models.DateField(verbose_name='Select the date of release: ', default=datetime.now)
    content_rating = models.CharField(max_length=16, verbose_name='Rating: ')
    genre_tags = models.CharField(max_length=512)
    description = models.TextField(blank=True, verbose_name='Movie description: ')
    displayornot = models.BooleanField(default=True, verbose_name='Disable this checkbox to hide this movie from the website: ')
    actors = models.CharField(max_length=512, verbose_name='Actors (seperate by comma): ')
    views = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}"
    def __unicode__(self):
        return self.title

class TvShow(models.Model):
    title = models.CharField(max_length=512, blank=True, null=True, verbose_name='Name of the show: ')
    start_date = models.DateField(null=False, verbose_name='Airing start date: ', default=datetime.now)
    end_date = models.DateField(blank=True, null=True, verbose_name='Airing end date (leave empty if running): ')
    trailer_file = models.FileField(blank=True, null=True, verbose_name='Upload the trailer file: ')
    poster_file = models.FileField(upload_to='posters', max_length=512, verbose_name='Upload a poster file: ')
    releasedate = models.DateField(verbose_name='Select the date of release: ', default=datetime.now)
    content_rating = models.CharField(max_length=16, verbose_name='Rating: ')
    genre_tags = models.CharField(max_length=512)
    description = models.TextField(blank=True, verbose_name='Show description: ')
    displayornot = models.BooleanField(default=True, verbose_name='Disable this checkbox to hide this show from the website: ')
    actors = models.CharField(max_length=512, verbose_name='Actors (seperate by comma): ')
    views = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}"
    def __unicode__(self):
        return self.title
    
class Episode(models.Model):
    tv_show = models.ForeignKey(TvShow, related_name='episodes', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=512)
    air_date = models.DateField(null=False, verbose_name='Airing date: ', default=datetime.now)
    episode_num = models.SmallIntegerField()
    season_num = models.SmallIntegerField()
    description = models.TextField(blank=True, verbose_name='Episode description: ')
    movie_file = models.FileField(verbose_name='Upload the episode: ')
    subtitle_file = models.FileField(verbose_name='Upload the subtitles file: ')
    displayornot = models.BooleanField(default=True, verbose_name='Disable this checkbox to hide this episode from the website: ')
    views = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}"
    def __unicode__(self):
        return self.title
    
class termsconditionlisting(models.Model):
    about = models.TextField()
    terms = models.TextField()
    privacypolicy = models.TextField()
    faq = models.TextField()
    pricing = models.TextField()
    contact = models.TextField()
    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'About, Terms and Privacy Policy'
        verbose_name_plural = 'About, Terms and Privacy Policy'
        
class Ebook(models.Model):    
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    file = models.FileField()
    displayornot = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}"
    def __unicode__(self):
        return self.title
    
class UploadFileModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField()
    file2 = models.FileField()

    def __str__(self):
        return f"{self.title}"
    def __unicode__(self):
        return self.title
