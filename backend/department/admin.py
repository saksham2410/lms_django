from django.contrib import admin
from department.models import Department, Course, CourseOffering, FileModel

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(FileModel)