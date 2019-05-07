from django.db import models

class timetable(models.Model):
    time = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    teacher = models.CharField(max_length=300)
    
    def sub(self):
    	return self.subject
    	
    def __str__(self):
        return self.time
    
