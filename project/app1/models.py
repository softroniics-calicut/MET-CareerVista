from django.db import models

# Create your models here.


class userreg(models.Model):
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    name=models.CharField(max_length=200)
    email=models.CharField(unique=True,max_length=200)
    contact=models.CharField(unique=True,max_length=200)
    file=models.FileField()
    username=models.CharField(unique=True,max_length=200)
    password=models.CharField(max_length=200)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)
    def __str__(self):
        return self.name
    

class companyreg(models.Model):
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    companyname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(unique=True,max_length=200)
    contact=models.CharField(unique=True,max_length=200)
    username=models.CharField(unique=True,max_length=200)
    password=models.CharField(max_length=200)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)
    def __str__(self):
        return self.companyname
 

class job(models.Model):
    company_id = models.ForeignKey(companyreg, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    def __str__(self):
        return (self.job_name)


class application(models.Model):
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    user_id = models.ForeignKey(userreg, on_delete=models.CASCADE)
    job = models.ForeignKey(job,on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True, null=True)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)
    def __str__(self):
        return (self.user_id.name)


class notification(models.Model):
    notification = models.CharField(max_length=200)