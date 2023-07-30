from django.shortcuts import render

# Create your views here.
from .models import Student, Marks, Subject, Teacher

def input_marks(request):
    if request.method == 'POST':
        student_req = request.POST.get('student')
        roll_no = request.POST.get('RollNo')
        subject_req = request.POST.get('subject')
        teacher_req = request.POST.get('teacher')
        marks_obtained = request.POST.get('marks')

        if(Student.objects.filter(roll_number=roll_no).exists()):
            student = Student.objects.get(roll_number=roll_no)
        else:
            Student.objects.create(name=student_req,roll_number=roll_no)
            student = Student.objects.get(roll_number=roll_no)

        if(Subject.objects.filter(sub_name=subject_req).exists()):
            subject = Subject.objects.get(sub_name=subject_req)       
        else:
            Subject.objects.create(sub_name=subject_req)
            subject = Subject.objects.get(sub_name=subject_req)

        if(Teacher.objects.filter(name=teacher_req).exists()):
            teacher = Teacher.objects.get(name=teacher_req)       
        else:
            Teacher.objects.create(name=teacher_req)
            teacher = Teacher.objects.get(name=teacher_req)
            teacher.subjects.add(subject)
        

        Marks.objects.create(
            student=student,
            subject=subject,
            teacher=teacher,
            marks_obtained=marks_obtained
        )

    return render(request, 'input_marks.html')

def view_marks(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        student = Student.objects.get(roll_number = student_id)
        marks = Marks.objects.filter(student=student)

        return render(request, 'view_marks.html', {'student': student, 'marks': marks})

    students = Student.objects.all()
    return render(request, 'select_student.html', {'students': students})
