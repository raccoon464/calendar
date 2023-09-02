import base64

from django.conf import settings
from django.db import models


def get_upload_path(instance, filename):
    return f"{type(instance)()}/{instance.id}/{filename}"


class BaseModel(models.Model):
    created_datetime = models.DateTimeField("Created At", auto_now_add=True)

    class Meta:
        abstract = True


class BaseNoteModel(BaseModel):
    comment = models.TextField("Note")

    def __str__(self):
        return self.comment

    class Meta:
        abstract = True


class BaseFileModel(BaseModel):
    file = models.FileField("File")
    order = models.PositiveIntegerField("Order", null=True, blank=True)

    def __str__(self):
        return self.file.name

    def get_file_as_b64(self) -> str:
        if self.file:
            name, extension = self.file.name.split(".")
            return f"data:image/{extension};base64,{base64.b64encode(self.file.read()).decode('ascii')}"
        else:
            return ""

    class Meta:
        abstract = True
        ordering = ["order"]


class BaseStatusModel(BaseModel):
    comment = models.TextField("Comment", null=True, blank=True)
    from_dttm = models.DateTimeField("From date-time")
    till_dttm = models.DateTimeField("Till date-time", null=True, blank=True)

    def __str__(self):
        return f"{self.status} ({self.from_dttm} - {self.till_dttm})"

    class Meta:
        abstract = True
        get_latest_by = "-from_dttm"
