from django.db import models



class Project (models.Model):
    name = models.CharField (max_length = 200)
    def _str_(self):
        return self.name
    
class Task (models.Model):
    title = models.CharField (max_length = 200)
    description = models.TextField()
    project = models.ForeignKey (Project, on_delete = models.CASCADE)
    def _str_(self):
        return self.title + '-' + self.description
    
