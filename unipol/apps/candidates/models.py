from django.db import models
from django.utils import timezone


class Candidate(models.Model):

    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    
    curp = models.CharField(max_length=19, help_text="Entry CURP", unique=True)
    rfc = models.CharField(max_length=13, help_text="Entry RFC", unique=True)
    
    name = models.CharField(max_length=50,help_text="Entry name")
    last_name = models.CharField(max_length=50, help_text="Entry last name")
    mothers_last_name = models.CharField(max_length=50, help_text="Entry mothers last name")

    gender = models.CharField(max_length=1, choices=GENDER, help_text="Entry gender")

    age = models.IntegerField(help_text="Entry age")
    height = models.IntegerField(help_text="Entry height")
    belongs_other_corporation = models.BooleanField(default=False)

    date_create = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Candidate'
    def __str__(self):
        return f'{self.curp}'



class Documents(models.Model):

    candidate = models.OneToOneField(
        Candidate,
        primary_key=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )


    file_birth_certificate = models.FileField(upload_to='documents', max_length=100)
    file_curp = models.FileField(upload_to='documents', max_length=100)
    file_rfc = models.FileField(upload_to='documents', max_length=100)
    file_ine = models.FileField(upload_to='documents', max_length=100)
    file_proof_address = models.FileField(upload_to='documents', max_length=100)
    file_proof_studies = models.FileField(upload_to=f'documents', max_length=100)
    file_proof_courses = models.FileField(upload_to=f'documents', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Document'

    def __str__(self):
        return f'{self.candidate.curp}'


class Contact(models.Model):

    candidate = models.OneToOneField(
        Candidate,
        primary_key=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    telephone = models.IntegerField(help_text="Entry Telephone")
    mobile_telephone = models.IntegerField(null=True, blank=True, help_text="Entry Mobile Telephone")
    email = models.EmailField(help_text="Entry Email", unique=True)

    def __str__(self):
        return f'{self.candidate.curp}'


class Direction(models.Model):
    
    candidate = models.OneToOneField(
        Candidate,
        primary_key=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    place_of_residence = models.CharField(max_length=35)
    delegation = models.CharField(max_length=50)
    suburb = models.CharField(max_length=70)
    postal_code = models.IntegerField()
    street = models.CharField(max_length=50)
    num_outdoor = models.IntegerField()
    num_inside = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Direction'

    def __str__(self):
        return f'{self.candidate.curp}'


class CallInfo(models.Model):
    candidate = models.OneToOneField(
        Candidate,
        primary_key=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    medium = models.TextField()
    attraction = models.TextField()
    
    class Meta:
        verbose_name = 'Call_Info'

    def __str__(self):
        return f'{self.candidate.curp}'


class Studies(models.Model):

    candidate = models.OneToOneField(
        Candidate,
        primary_key=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    level_of_studies = models.CharField(max_length=15, help_text="Entry level study")
    details = models.CharField(max_length=60, help_text="Entry details level study", null=True)

    class Meta:
        verbose_name = 'Studie'

    def __str__(self):
        return f'{self.candidate.curp}'



