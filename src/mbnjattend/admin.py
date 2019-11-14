from django.contrib import admin
from mbnjattend.models import (Course, Faculty, Grade, Information,
                                Performance, Roster, Student, Transaction)

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('transdate',)


admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Grade)
admin.site.register(Information)
admin.site.register(Performance)
admin.site.register(Roster)
admin.site.register(Student)
admin.site.register(Transaction, TransactionAdmin)
