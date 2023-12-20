from PIL import Image
from django.db import models
from django.urls import reverse

from authy.models import User

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
    teacher = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    captain = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='class_captain')

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


class Driver(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    photo = models.ImageField(default="default.jpg", blank=True, null=True)
    license_copy = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Transportation(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registered_number = models.CharField(max_length=15)
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='transport', null=True, blank=True)

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


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ArticlesCategories, on_delete=models.CASCADE)
    image_1 = models.ImageField()
    image_2 = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    quote_1 = models.CharField(max_length=255)
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField()
    paragraph_3 = models.TextField(blank=True, null=True)
    paragraph_4 = models.TextField(blank=True, null=True)
    paragraph_5 = models.TextField(blank=True, null=True)
    paragraph_6 = models.TextField(blank=True, null=True)
    paragraph_7 = models.TextField(blank=True, null=True)
    paragraph_8 = models.TextField(blank=True, null=True)
    paragraph_9 = models.TextField(blank=True, null=True)
    quote_2 = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class ArticleComment(models.Model):
    name = models.CharField(max_length=124)
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Journal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ArticlesCategories, on_delete=models.CASCADE)
    image_1 = models.ImageField()
    image_2 = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    quote_1 = models.CharField(max_length=255)
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField()
    paragraph_3 = models.TextField(blank=True, null=True)
    paragraph_4 = models.TextField(blank=True, null=True)
    paragraph_5 = models.TextField(blank=True, null=True)
    paragraph_6 = models.TextField(blank=True, null=True)
    paragraph_7 = models.TextField(blank=True, null=True)
    paragraph_8 = models.TextField(blank=True, null=True)
    paragraph_9 = models.TextField(blank=True, null=True)
    quote_2 = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('journal_details', args=[str(self.id)])


class JournalComment(models.Model):
    name = models.CharField(max_length=124)
    comment = models.TextField()
    article = models.ForeignKey(Journal, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AdmissionForm(models.Model):
    form_file = models.FileField(upload_to='admission_form')
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Admission Form"


class OnlineApplication(models.Model):
    full_name = models.CharField(max_length=125)
    email = models.EmailField()
    contact = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    birth_date = models.DateField()
    expected_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    current_academic_report = models.FileField(blank=True, null=True)

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
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clas.name


class SubmitAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assignment_id = models.CharField(max_length=125)
    answer_file = models.FileField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assignment_id


class VirtualClass(models.Model):
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    title = models.CharField(max_length=255)
    link = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clas.name


class Management(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    photo = models.ImageField(default="default.jpg", blank=True, null=True)

    def __str__(self):
        return self.name


class Counselor(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    photo = models.ImageField(blank=True, null=True, default="default.jpg")

    def __str__(self):
        return self.name


class Award(models.Model):
    activity = models.CharField(max_length=255)
    photo = models.ImageField()
    received_date = models.DateField()

    def __str__(self):
        return self.activity


class Query(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name