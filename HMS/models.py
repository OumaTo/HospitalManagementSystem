from django.db import models

class Patient(models.Model):
    status = [('Served','Served'),
                 ('Not Served','Not Served'),
                 ]
    Name = models.CharField(max_length=200, null=True)
    Age = models.IntegerField( null=True)
    Illness = models.CharField(max_length=200, null=True)
    Date = models.DateField( null=True)
    Status = models.CharField(max_length=40, default='Not Served', choices=status)

    def __str__(self):
        return (f'{self.Name}')

class Appointment(models.Model):
    level = [('Very Critical','Very Critical'),
                 ('Moderately Critical','Moderately Critical'),
                 ('Not Critical','Not Critical'),
                 ]
    status = [('Served','Served'),
                 ('Not Served','Not Served'),
                 ]
    FirstName = models.CharField(max_length=200, null=True)
    LastName = models.CharField(max_length=200, null=True)
    Age = models.IntegerField( null=True)
    Category = models.CharField(max_length=200, null=True)
    Phone = models.CharField(max_length=14)
    Situation = models.CharField(max_length=40, null=True, choices=level)
    Date = models.DateField( null=True)
    Description = models.TextField(null =True)
    Status = models.CharField(max_length=40, default='Not Served', choices=status)

    
    def __str__(self):
        return (f'{self.FirstName} {self.Date}')
        

class Statistic(models.Model):
    Drugs = models.IntegerField(null = True)
    Admitted = models.IntegerField(null = True)
    Emergency = models.IntegerField(null = True)
    Doctors = models.IntegerField(null = True)
    Nurses = models.IntegerField(null = True)
    Services = models.IntegerField(null = True)
    Patients = models.IntegerField(null = True)

    def __str__(self):
        return 'statistics'
