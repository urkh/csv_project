from django.contrib import admin
from modules.test_app.models import Project, Variable, Respondent, Data


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'data_file', 'variable_file']
    list_filter = ['title', 'description', 'date']
    search_fields = ['title', 'description', 'date']
    date_hierarchy = 'date'

    def save_model(self, request, obj, form, change):
        #import ipdb; ipdb.set_trace()

        data_file = request.FILES['data_file'].readlines()
        variable_file = request.FILES['variable_file'].readlines()

        rownum = 0
        obj.save()

        for row in variable_file:
            if rownum == 0:
                pass
            else:
                nvf = row.split(",")
                variable = Variable.objects.create(
                    project = obj,
                    name = nvf[0],
                    label = nvf[1],
                    tags = nvf[2]
                )
                variable.save()

                respondent = Respondent.objects.create(
                    notes = data_file[rownum].split(",")[1]
                )
                respondent.save()

                data = Data.objects.create(
                    variable = variable,
                    respondent = respondent,
                    value = data_file[rownum].split(",")[2]
                )
                data.save()

            rownum += 1
admin.site.register(Project, ProjectAdmin)


class VariableAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'label', 'tags', 'question']
    list_filter = ['project', 'name', 'label']
    search_fields = ['project', 'name', 'label', 'tags', 'question']
admin.site.register(Variable, VariableAdmin)


class RespondentAdmin(admin.ModelAdmin):
    list_display = ['notes',]
    search_fields = ['notes',]
admin.site.register(Respondent, RespondentAdmin)


class DataAdmin(admin.ModelAdmin):
    list_display = ['variable', 'respondent', 'value']
    search_fields = ['variable', 'respondent', 'value']
admin.site.register(Data, DataAdmin)
