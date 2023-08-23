from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    job_id = models.CharField(max_length=20, unique=True)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    posting_date = models.DateField()
    job_description_url = models.URLField()
    salary = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title

    class Meta:
        db_table = 'jobs'  # Set the MongoDB collection name
