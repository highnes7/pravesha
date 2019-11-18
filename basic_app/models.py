from django.db import models
from django.contrib.auth.models import User
from django import forms


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    mob_no = models.CharField(max_length=10,blank=False,default=None)
    college = models.CharField(max_length=120,blank=False,default=None)
    dept = models.CharField(max_length=120,blank=False,default=None)
    Year = models.IntegerField(default=0,max_length=1)
    college_reg_id = models.CharField(max_length=50,blank=False,default=None)
    food_pref = models.CharField(max_length=10,blank=True,default='ND')
    #Events------------------------------
    pp = models.BooleanField(default=False)
    bat= models.BooleanField(default=False)
    tq = models.BooleanField(default=False)
    ar = models.BooleanField(default=False)
    aio = models.BooleanField(default=False)
    ty = models.BooleanField(default=False)
    syt = models.BooleanField(default=False)
    mod = models.BooleanField(default=False)
    th = models.BooleanField(default=False)
    pubg = models.BooleanField(default=False)
#-----------------------Payment Status-------------------------------------
    payment_stats = models.BooleanField(default=False)

#-----------------------Coodinator Status-------------------------------------
    cs = models.BooleanField(default=False)
    cs_reg_status = models.BooleanField(default=False)
    cs_cert_status = models.BooleanField(default=False)
    cs_report_status = models.BooleanField(default=False)
    cs_pp_status = models.BooleanField(default=False)
    cs_bat_status = models.BooleanField(default=False)
    cs_tq_status = models.BooleanField(default=False)
    cs_ar_status = models.BooleanField(default=False)
    cs_aio_status = models.BooleanField(default=False)
    cs_ty_status = models.BooleanField(default=False)
    cs_syt_status = models.BooleanField(default=False)
    cs_mod_status = models.BooleanField(default=False)
    cs_th_status = models.BooleanField(default=False)
    cs_pubg_status = models.BooleanField(default=False)




#-----------------------Participation Status-------------------------------------
    status_pp = models.CharField(max_length=4,blank=False,default=0)
    status_bat = models.CharField(max_length=4,blank=False,default=0)
    status_tq = models.CharField(max_length=4,blank=False,default=0)
    status_ar = models.CharField(max_length=4,blank=False,default=0)
    status_aio = models.CharField(max_length=4,blank=False,default=0)
    status_ty = models.CharField(max_length=4,blank=False,default=0)
    status_syt = models.CharField(max_length=4,blank=False,default=0)
    status_mod = models.CharField(max_length=4,blank=False,default=0)
    status_th = models.CharField(max_length=4,blank=False,default=0)
    status_pubg = models.CharField(max_length=4,blank=False,default=0)


    def __str__(self):
        return self.user.username


class Log(models.Model):
    refuser = models.CharField(max_length=10,blank=False,default=None)
    mob_no_log = models.CharField(max_length=10,blank=False,default=None)
    email_log = models.CharField(max_length=50,blank=False,default=None)
