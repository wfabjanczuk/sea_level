from django.db import models
from django.utils import timezone
import jsonfield

STATUS_MAX_LENGTH = 16
MSG_MAX_LENGTH = 512
DATA_SET_MAX_LENGTH = 128
ATTRIBUTES_MAX_LENGTH = 256


class Task(models.Model):
    task_date = models.DateTimeField(default=timezone.now)
    json_content = jsonfield.JSONField()
    status = models.CharField(max_length=STATUS_MAX_LENGTH, default="pending")
    data_set = models.TextField(max_length=DATA_SET_MAX_LENGTH, default="???")
    msg = models.CharField(max_length=MSG_MAX_LENGTH)


class DataSets(models.Model):
    data_set = models.CharField(max_length=DATA_SET_MAX_LENGTH, unique=True)
    attributes = models.CharField(max_length=ATTRIBUTES_MAX_LENGTH)

# DataSets Foreign Key TBA
# DownloadedFile Foreign Key TBA
# DownloadedFile TBA


# class DownloadedFile(models.Model):
#     date = models.DateTimeField(default=timezone.now)
#     path = models.CharField(max_length=255)
#     size = models.CharField(max_length=31)
#     fk = models.ForeignKey(Task, on_delete=models.CASCADE)

#     def set_path(self, category):
#         self.path = "./files/" + category + "/file_id_" + self.fk
