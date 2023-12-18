from datetime import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import OnlineApplicationForm
from .models import Class, GalleryCategory, Gallery, GamesCategory, Games, Transportation, Route, OurCareer, Testimony, \
    Articles, Subject, AdmissionForm, OnlineApplication, Journal, Calendar, Announcement, OtherFee, Library, FAQ, \
    ScheduleVisit, Newsletter, Assignment

today = datetime.today()


def home_page(request):
    activities = Calendar.objects.all()
    announcements = Announcement.objects.all().order_by('-id')[:10]
    popular_class = Class.objects.all()[:3]
    testimonies = Testimony.objects.all()
    tuition_fees = Class.objects.all()
    articles = Articles.objects.all().order_by('-date_posted')
    faqs = FAQ.objects.all()
    context = {
        'popular_class': popular_class,
        'testimonies': testimonies,
        'announcements': announcements,
        'articles': articles,
        'tuition_fees': tuition_fees,
        'activities': activities,
        'faqs': faqs
    }
    return render(request, 'core/home.html', context)


def about_us(request):
    context = {

    }
    return render(request, 'core/about_us.html', context)


class CreateTestimonyView(CreateView):
    model = Testimony
    fields = "__all__"
    template_name = 'core/create_testimony.html'
    success_url = reverse_lazy('home')


def history(request):
    context = {

    }
    return render(request, 'core/history.html', context)


def management(request):
    context = {

    }
    return render(request, 'core/management.html', context)


def teachers(request):
    context = {

    }
    return render(request, 'core/teachers.html', context)


def classes(request):
    classes = Class.objects.all()
    context = {
        'classes': classes
    }
    return render(request, 'core/classes.html', context)


def class_detail(request, slug):
    name = Class.objects.get(slug=slug)
    context = {
        'name': name
    }
    return render(request, 'core/class_detail.html', context)


def contact(request):
    context = {

    }
    return render(request, 'core/contact.html', context)


def academics(request):
    pre_school_subjects = Subject.objects.filter(level='Pre-School')
    primary_subjects = Subject.objects.filter(level='Primary')
    jhs_subjects = Subject.objects.filter(level='Junior High')
    context = {
        'pre_school_subjects': pre_school_subjects,
        'primary_subjects': primary_subjects,
        'jhs_subjects': jhs_subjects,
    }
    return render(request, 'core/academics.html', context)


def placement_test(request):
    context = {

    }
    return render(request, 'core/placement_test.html', context)


def games(request):
    games_cat = GamesCategory.objects.all()
    games = Games.objects.all()
    context = {
        'games_cat': games_cat,
        'games': games
    }
    return render(request, 'core/games.html', context)


def gallery(request):
    gallery_cat = GalleryCategory.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'galleries': galleries,
        'gallery_cat': gallery_cat
    }
    return render(request, 'core/gallery.html', context)


def articles(request):
    articles = Articles.objects.all().order_by('-date_posted')
    context = {
        'articles': articles,
    }
    return render(request, 'core/articles.html', context)


def article_details(request, id):
    article = get_object_or_404(Articles, id=id)
    recent_article = Articles.objects.all().order_by('-date_posted')[:5]
    context = {
        'article': article,
        'recent_article': recent_article,
    }
    return render(request, 'core/article_details.html', context)


def journal(request):
    context = {

    }
    return render(request, 'core/journal.html', context)


def careers(request):
    careers = OurCareer.objects.all()
    context = {
        'careers': careers,
    }
    return render(request, 'core/careers.html', context)


def career_detail(request, career_id):
    career = OurCareer.objects.get(id=career_id)

    context = {
        'career': career,
    }
    return render(request, 'core/career_detail.html', context)


def store(request):
    context = {

    }
    return render(request, 'core/store.html', context)


def transportation(request):
    transportation = Transportation.objects.all()
    context = {
        'transportation': transportation,
    }
    return render(request, 'core/transportation.html', context)


def transportation_details(request, id):
    bus = Transportation.objects.get(id=id)
    routes = Route.objects.filter(bus=bus)
    context = {
        'bus': bus,
        'routes': routes
    }
    return render(request, 'core/transportation_details.html', context)


def remote(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'core/remote.html', context)


def library(request):
    books = Library.objects.all().order_by('title')
    context = {
        'books': books,
    }
    return render(request, 'core/library.html', context)


def fees(request):
    tuition_fees = Class.objects.all()
    other_fees = OtherFee.objects.all()
    context = {
        'tuition_fees': tuition_fees,
        'other_fees': other_fees
    }
    return render(request, 'core/fees.html', context)


def awards(request):
    context = {
    }
    return render(request, 'core/awards.html', context)


def counselors(request):
    context = {
    }
    return render(request, 'core/counselors.html', context)


def calendar(request):
    activities = Calendar.objects.all()
    context = {
        'activities': activities,
    }
    return render(request, 'core/calendar.html', context)


def admission(request):
    form_file = AdmissionForm.objects.all().first()
    form = OnlineApplicationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OnlineApplicationForm(request.POST)
    context = {
        'form_file': form_file,
        'form': form,
    }
    return render(request, 'core/admission.html', context)


class CreateAdmissionView(CreateView):
    model = OnlineApplication
    form_class = OnlineApplicationForm
    template_name = 'core/admission.html'
    success_url = reverse_lazy('home')


class JournalListView(ListView):
    model = Journal
    template_name = 'core/journal.html'
    context_object_name = 'articles'


class JournalDetailView(DetailView):
    model = Journal
    template_name = 'core/journal_details.html'
    context_object_name = 'article'


def schedule_visit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        date = request.POST['date']
        time = request.POST['time']
        if ScheduleVisit.objects.filter(phone_number=phone_number).exists():
            messages.success(request, f'Scheduled Already')
        elif ScheduleVisit.objects.filter(email=email).exists():
            messages.success(request, f'Scheduled Already')
        else:
            visit = ScheduleVisit.objects.create(name=name, email=email, phone_number=phone_number,
                                         date=date, time=time)
            visit.save()
            messages.success(request, f'Visit Scheduled Successfully')
    else:
        return redirect("home")
    return redirect("home")


def newsletter(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        if Newsletter.objects.filter(email=email).exists():
            messages.success(request, f'Already Subscribed')
        else:
            visit = Newsletter.objects.create(name=name, email=email)
            visit.save()
            messages.success(request, f'Subscribed Successfully')
    else:
        return redirect("home")
    return redirect("home")