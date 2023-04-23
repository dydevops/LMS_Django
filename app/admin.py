from django.contrib import admin
from .models import *
# Register your models here.   
    
class What_you_learn_TabularInline(admin.TabularInline):
    model = What_you_learn
    extra = 0
    
class Requirements_TabularInline(admin.TabularInline):
    model = Requirements
    extra = 0  
    
class Video_TabularInline(admin.TabularInline):
    model = Video
    extra = 0      
    
# class course_admin(admin.ModelAdmin):
#     inlines = (What_you_learnTabularInline,RequirementsTabularInline)  
# class What_you_learnAdmin(admin.ModelAdmin):
#     list_display = ['points','course']
#     list_display_links = ('points',)  
    
# class RequirementsAdmin(admin.ModelAdmin):
#     list_display = ['points','course','status']
#     list_display_links = ('points',)     
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','category','author','status','created_on']
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (What_you_learn_TabularInline,Requirements_TabularInline,Video_TabularInline)


# admin.site.register(Course,course_admin,)
admin.site.register(Course,CourseAdmin,)
# admin.site.register(What_you_learn,What_you_learnAdmin)
# admin.site.register(Requirements,RequirementsAdmin)
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(Lession) 
admin.site.register(Language)
admin.site.register(Payment)
admin.site.register(UserCourse)
admin.site.register(Video)