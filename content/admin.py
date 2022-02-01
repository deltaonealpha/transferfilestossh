from django.contrib import admin
from django import forms
# Register your models here.
from .models import Movie, TvShow, Episode, termsconditionlisting, UploadFileModel, Ebook, Moviecategory, TVcategory
admin.site.register(termsconditionlisting)
admin.site.site_header = "Cipherflix"
admin.site.register(Ebook)
class UploadMovie(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = []
class UploadMovieModelAdmin(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'        
    form = UploadMovie

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)
admin.site.register(Movie, UploadMovieModelAdmin)

class UploadTvShow(forms.ModelForm):
    class Meta:
        model = TvShow
        exclude = []
class UploadTvShowModelAdmin(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'        
    form = UploadTvShow

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)
admin.site.register(TvShow, UploadTvShowModelAdmin)

class UploadEpisode(forms.ModelForm):
    class Meta:
        model = Episode
        exclude = []
class UploadEpisodeModelAdmin(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'        
    form = UploadEpisode

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)
admin.site.register(Episode, UploadEpisodeModelAdmin)

admin.site.register(TVcategory)
admin.site.register(Moviecategory)

'''
from mce_filebrowser.admin import MCEFilebrowserAdmin
class PostVideoAdmin(MCEFilebrowserAdmin):
    pass
admin.site.register(Video, PostVideoAdmin)'''

