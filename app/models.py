from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.CharField(max_length=200,null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    def get_all_categories(self):
        return Categories.objects.filter(status=1).order_by('created_on')
    
class Author(models.Model):
   name = models.CharField(max_length=100, null=True)
   slug = models.SlugField(max_length=100, unique=True)
   author_profile = models.ImageField(upload_to="Media/author")
   about_author = models.TextField()
   created_on = models.DateTimeField(default=timezone.now)
   updated_on = models.DateTimeField(auto_now=True)
   status = models.IntegerField(choices=STATUS, default=0)

   def __str__(self):
       return self.name 
   
class Level(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
       return self.name 


class Language(models.Model):
    language = models.CharField(max_length=100)
    
    def __str__(self):
       return self.language      
   
class Course(models.Model):
    certificate_choice = (
        ('No', 'No'),
        ('Yes', 'Yes'),
    )
    title = models.CharField(max_length=500)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    featured_image = models.ImageField(upload_to="Media/featured_img",null=True)
    featured_video = models.CharField(max_length=300,null=True)
    description = models.TextField()
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    level = models.ForeignKey(Level,on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    language = models.ForeignKey(Language,on_delete=models.CASCADE,null=True)
    deadline = models.CharField(max_length=100,null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    certificate = models.CharField(choices=certificate_choice, default='No', max_length=100)
    
    
    def get_url(self):
         return reverse('course_detail', args=[self.slug])

    def __str__(self):
        return self.title
    
    
class What_you_learn(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points 
       
class Requirements(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    
    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'
    
    def __str__(self):
        return self.points 
    
class Lession(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return self.name + ".... " + self.course.title 
    
class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to="Media/Yt_Thumbnail",null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    lession = models.ForeignKey(Lession,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    youtube_id = models.CharField(max_length=300,null=True)
    time_duration = models.FloatField(null=True)
    preview = models.BooleanField(default=False)

   
    def __str__(self):
        return self.title 
    
    
class UserCourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    paid = models.BooleanField(default=0)
    date = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.user.first_name + ".... " + self.course.title 
    
class Payment(models.Model):
    
    order_id = models.CharField(max_length=100,null=True, blank=True)
    payment_id = models.CharField(max_length=100,null=True, blank=True)
    user_course = models.ForeignKey(UserCourse,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

   
    def __str__(self):
        
        # return self.user
        return self.user.first_name + ".... " + self.course.title                              
    
    