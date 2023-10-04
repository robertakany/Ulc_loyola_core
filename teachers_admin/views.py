from django.shortcuts import render, redirect

from main.models import Auditoire
from teachers_admin.models import Teacher
from university_admin.models import Course


"""def add_course(request):
    error = "Il y a une erreur dans ces champs"
    # Obtenir les auditoires disponibles depuis la base de données
    auditoires = Course.objects.all()
    
    # Créer une instance de votre formulaire PdfCourse en passant les auditoires disponibles
    form = CourseForm(auditoires=auditoires)

    teacher = Teacher.objects.get(user=request.user)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, auditoires=auditoires)
        if form.is_valid():
            # Utilisez form.cleaned_data pour accéder aux données du formulaire
            cleaned_data = form.cleaned_data
            try:
                courses = Course.objects.create(
                    teacher=teacher,
                    auditoire=cleaned_data['auditoire'],
                    title=cleaned_data['title'],
                    warnings=cleaned_data['warnings'],
                    pdf_files=cleaned_data["pdf_files"]
                )
                courses.save()
                return redirect('courses')
            except Exception as e:
                print('error in courses ')
                return error"""




def teacher_admin(request, teacher_slug):
    user= request.user
    teacher = Teacher.objects.get(user=user, slug=teacher_slug)
    print(teacher.user )
    return render(request, "teachers_admin/teacher_admin_home.html", locals())


def add_course(request):
    error = "Il y a une erreur dans ces champs"
    teacher = Teacher.objects.filter(user=request.user).first()
    print(teacher.user.username)
    if request.method == 'POST':
        print(request.POST)
        image = request.FILES.get('image')
        pdf_files = request.FILES.get('pdf_files')
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        notes = request.POST.get('notes', '')
        try:
            course = Course.objects.create(
                teacher=teacher,
                # auditoire=data.getlist("auditoire"),
                title=title,
                image=image,
                notes=notes,
                pdf_files=pdf_files,
                description=description
            )
            course.save()
            print("voici le course: ", course)
            # for auditoire_id in auditoires:
            #    course.auditoire.add(auditoire_id)
            return redirect("courses_list")
        except Exception as e:
            print('error in course', e)
            return error
    else:
        auditoires = Auditoire.objects.all()
    return render(request, "teachers_admin/add_course.html", locals())

 



def courses_list(request):
    user = request.user
    teacher = Teacher.objects.filter(user=user).first()
    courses = Course.objects.filter(teacher=teacher)
    return render(request, "teachers_admin/courses.html", locals())

# Create your views here.
