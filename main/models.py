from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

class AboutMe(models.Model):
    fi = models.CharField(max_length=255)
    about = RichTextField()
    phone = models.CharField(max_length=13)
    birthday = models.DateField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    work = models.CharField(max_length=255)
    photo = models.ImageField(null=True, upload_to='about')

    def __str__(self):
        return self.fi

class Skills(models.Model):
    name = models.CharField(max_length=50)
    percent = models.IntegerField()
    def __str__(self):
        return self.name


class Socials(models.Model):
    sts = (
        ("sc_facebook", "sc_facebook"),
        ("sc_twitter", "sc_twitter"),
        ("sc_google", "sc_google"),
        ("sc_youtube", "sc_youtube"),
        ("sc_instagram", "sc_instagram"),
    )
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    cls = models.CharField(choices=sts, max_length=30, default='sc_facebook')
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CategoryOfPortfolio(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Portfolios(models.Model):
    category = models.ForeignKey(CategoryOfPortfolio, on_delete=models.CASCADE, related_name='portfolio')
    project_name = models.CharField(max_length=50)
    text = RichTextField()
    client_name = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)
    domen = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name

class PhotosForPortfolio(models.Model):
    portfolio = models.ForeignKey(Portfolios, on_delete=models.CASCADE, related_name='photo')
    photo = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.portfolio.project_name


class CategoryOfBlog(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(CategoryOfBlog, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=100)
    text = RichTextField()
    photo = models.ImageField(upload_to='blog')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Messages(models.Model):
    fi = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.fi


class Icon(models.Model):
    icon = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    difficult = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Icons(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=30)
    count = models.CharField(max_length=100)


class Resume(models.Model):
    staff = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.company


class Logo(models.Model):
    photo = models.ImageField(upload_to='logo')

