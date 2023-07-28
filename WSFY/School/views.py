from django.shortcuts import render

# Create your views here.
from .models import Student, Marks, Subject, Teacher

def input_marks(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        teacher_id = request.POST.get('teacher')
        marks_obtained = request.POST.get('marks')

        student = Student.objects.get(pk=student_id)
        subject = Subject.objects.get(pk=subject_id)
        teacher = Teacher.objects.get(pk=teacher_id)

        Marks.objects.create(
            student=student,
            subject=subject,
            teacher=teacher,
            marks_obtained=marks_obtained
        )

    students = Student.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()

    return render(request, 'input_marks.html', {'students': students, 'subjects': subjects, 'teachers': teachers})

def view_marks(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        student = Student.objects.get(pk=student_id)
        marks = Marks.objects.filter(student=student)

        return render(request, 'view_marks.html', {'student': student, 'marks': marks})

    students = Student.objects.all()
    return render(request, 'select_student.html', {'students': students})
