from PIL import Image
from django.db import models
from django.urls import reverse

# Create your models here.

LEVEL_CHOICES = (
    ('Pre-School', 'Pre-School'),
    ('Primary', 'Primary'),
    ('Junior High', 'Junior High'),
)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name


TUITION_INTERVAL_CHOICES = (
    ('Day', 'Day'),
    ('Month', 'Month'),
    ('Term', 'Term'),
    ('Year', 'Year'),
)


class Class(models.Model):
    picture = models.ImageField(upload_to='class', default='class-1.jpg')
    video = models.FileField(upload_to='class', null=True, blank=True)
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    name = models.CharField(max_length=15, unique=True)
    slug = models.SlugField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    tuition_interval = models.CharField(max_length=15, choices=TUITION_INTERVAL_CHOICES)
    total_seats = models.IntegerField()
    start_time = models.TimeField(max_length=15)
    close_time = models.TimeField(max_length=15)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


GALLERY_CATEGORY = (
    ('Academics', 'Academics'),
    ('Sports', 'Sports'),
    ('I.T', 'I.T'),
    ('Science', 'Science'),
)


class GalleryCategory(models.Model):
    category = models.CharField(max_length=50, choices=GALLERY_CATEGORY)

    def __str__(self):
        return self.category


class Gallery(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery', null=True, blank=True)
    detail = models.CharField(max_length=255)

    def __str__(self):
        return self.detail

    def save(self, *args, **kwargs):
        super(Gallery, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 700:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


GAMES_CATEGORY = (
    ('Football', 'Football'),
    ('Volley', 'Volley'),
    ('Tag', 'Tag'),
)


class GamesCategory(models.Model):
    category = models.CharField(max_length=50, choices=GAMES_CATEGORY)

    def __str__(self):
        return self.category


class Games(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='games', null=True, blank=True)
    detail = models.CharField(max_length=255)

    def __str__(self):
        return self.detail

    def save(self, *args, **kwargs):
        super(Games, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 700:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Transportation(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registered_number = models.CharField(max_length=15)
    driver_name = models.CharField(max_length=100)
    driver_contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to='transport', null=True, blank=True)
    driver_picture = models.ImageField(null=True, default="default.jpg")

    def __str__(self):
        return self.make


class Route(models.Model):
    bus = models.ForeignKey(Transportation, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    pickup_time = models.TimeField()
    drop_time = models.TimeField()

    def __str__(self):
        return self.destination


class OurCareer(models.Model):
    position = models.CharField(max_length=255)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    job_description = models.CharField(max_length=255)
    picture = models.ImageField(default='career.png', upload_to='careers', null=True, blank=True)
    employer_email = models.EmailField()

    def get_absolute_url(self):
        return reverse('career', args=[str(self.id)])

    def __str__(self):
        return str(self.position)


class Testimony(models.Model):
    full_name = models.CharField(max_length=55, unique=True)
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    testimony = models.TextField()

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super(Testimony, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 700:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ArticlesCategories(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.category}"

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])


class Articles(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticlesCategories, on_delete=models.CASCADE)
    picture_1 = models.ImageField(default='', upload_to='blog')
    blockquote = models.CharField(max_length=255, null=True, blank=True)
    picture_2 = models.ImageField(upload_to='blog', null=True, blank=True)
    picture_3 = models.ImageField(upload_to='blog', null=True, blank=True)
    detail_1 = models.TextField(null=True, blank=True)
    detail_2 = models.TextField(null=True, blank=True)
    topic_3 = models.CharField(max_length=255, null=True, blank=True)
    detail_3 = models.TextField(null=True, blank=True)
    topic_4 = models.CharField(max_length=255, null=True, blank=True)
    detail_4 = models.TextField(null=True, blank=True)
    detail_5 = models.TextField(null=True, blank=True)
    detail_6 = models.TextField(null=True, blank=True)
    banner = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=155)
    author_pic = models.ImageField(upload_to='blog', default="default.jpg", null=True, blank=True)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Journal(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticlesCategories, on_delete=models.CASCADE)
    picture_1 = models.ImageField(default='', upload_to='blog')
    blockquote = models.CharField(max_length=255, null=True, blank=True)
    picture_2 = models.ImageField(upload_to='blog', null=True, blank=True)
    picture_3 = models.ImageField(upload_to='blog', null=True, blank=True)
    detail_1 = models.TextField(null=True, blank=True)
    detail_2 = models.TextField(null=True, blank=True)
    topic_3 = models.CharField(max_length=255, null=True, blank=True)
    detail_3 = models.TextField(null=True, blank=True)
    topic_4 = models.CharField(max_length=255, null=True, blank=True)
    detail_4 = models.TextField(null=True, blank=True)
    detail_5 = models.TextField(null=True, blank=True)
    detail_6 = models.TextField(null=True, blank=True)
    banner = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=155)
    author_pic = models.ImageField(upload_to='blog', default="default.jpg", null=True, blank=True)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class AdmissionForm(models.Model):
    form_file = models.FileField(upload_to='admission_form')


class OnlineApplication(models.Model):
    full_name = models.CharField(max_length=125)
    birth_date = models.DateField()
    expected_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    current_academic_report = models.FileField()

    def __str__(self):
        return f"{self.full_name}"


class Calendar(models.Model):
    date = models.DateField()
    activity = models.CharField(max_length=255)

    def __str__(self):
        return self.activity


class Announcement(models.Model):
    event = models.TextField()

    def __str__(self):
        return self.event


class OtherFee(models.Model):
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    admission = models.IntegerField()
    canteen = models.IntegerField()
    uniform = models.IntegerField()
    others = models.IntegerField()

    def __str__(self):
        return self.level


BOOKS_CHOICES = (
    ('Text Book', 'Text Book'),
    ('Novel', 'Novel'),
    ('Biography', 'Biography'),
    ('Others', 'Others'),
)


class Library(models.Model):
    type = models.CharField(max_length=255, choices=BOOKS_CHOICES)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    file = models.FileField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class ScheduleVisit(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=125)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    question = models.FileField()
    deadline = models.DateTimeField()
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.clas.name
