from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    data_file = models.FileField(upload_to='data_files/%Y/%m/%d')
    variable_file = models.FileField(upload_to='variable_files/%Y/%m/%d')

    class Meta:
        verbose_name_plural = 'Project'

    def __unicode__(self):
        return self.title


class Variable(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    question = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Variable'

    def __unicode__(self):
        return u'%s - %s' % (self.project.title, self.name)

class Respondent(models.Model):
    notes = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Respondent'

    def __unicode__(self):
        return self.notes

class Data(models.Model):
    variable = models.ForeignKey(Variable)
    respondent = models.ForeignKey(Respondent)
    value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Data'

    def __unicode__(self):
        return u'%s - %s - %s' % (self.variable, self.respondent, self.value)

