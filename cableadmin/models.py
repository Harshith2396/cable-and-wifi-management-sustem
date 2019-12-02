from django.db import models
class cable_properties(models.Model):
    cable_id=models.CharField(max_length=5,primary_key=True,)
    cable_plane_name=models.CharField(max_length=30)
    cable_price=models.CharField(max_length=30)
    bandwidth=models.CharField(max_length=30)
class wifi_properties(models.Model):
    wifi_id=models.CharField(max_length=5,primary_key=True)
    wifi_plan_name=models.CharField(max_length=30)
    wifi_price=models.CharField(max_length=10)
    speed_provided=models.CharField(max_length=10)
class area(models.Model):
    area_id=models.CharField(max_length=5,primary_key=True)
    name_of_place=models.CharField(max_length=30)
class collectors(models.Model):
    collector_id=models.CharField(max_length=5,primary_key=True)
    collector_name=models.CharField(max_length=5)
    area_id=models.CharField(max_length=5)
class Manager(models.Model):
    manager_id=models.CharField(max_length=5,primary_key=True)
    manager_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20,default='123')
class Servers(models.Model):
    server_id=models.CharField(max_length=5,primary_key=True)
    area_id=models.CharField(max_length=5)
    manager_id=models.CharField(max_length=5)
class customers(models.Model):
    customer_id=models.CharField(max_length=5,primary_key=True)
    customer_name=models.CharField(max_length=30)
    area_id=models.CharField(max_length=5)
    server_id=models.CharField(max_length=5)
    wifi_plans=models.CharField(max_length=5)
    cable_plans=models.CharField(max_length=5)
    subscription_cable=models.CharField(max_length=20,default='1 MONTH')
    subscription_wifi=models.CharField(max_length=20,default='1 MONTH')
    collector_id=models.CharField(max_length=5,default='21')
    password=models.CharField(max_length=20,default='abc')