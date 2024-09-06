# Owned by Yash Jangid 
# github_id = im-yash21
# leetcode_id = im-yash21
# linkeldn_id = im-yash21
from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_priority = models.CharField(max_length=10)
    task_duedate = models.CharField(max_length=10)