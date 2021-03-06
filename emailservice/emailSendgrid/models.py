from django.db import models


class EmailModel(models.Model):

    sender = models.EmailField(max_length=30)
    sent_at = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=200)
    attachment = models.FileField()
    subject = models.TextField(max_length=100)
    status = models.BooleanField(default=True)


class EmailReceiverTo(models.Model):

    email = models.ForeignKey(EmailModel, on_delete=models.CASCADE)
    receivers = models.EmailField(max_length=30)


class EmailReceiverCC(models.Model):

    email = models.ForeignKey(EmailModel, on_delete=models.CASCADE)
    cc  = models.EmailField(max_length=30)


class EmailReceiverBCC(models.Model):

    email = models.ForeignKey(EmailModel, on_delete=models.CASCADE)
    bcc = models.EmailField(max_length=30)


