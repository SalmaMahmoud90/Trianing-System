from django.db import models

# Create your models here.

class MainUser(models.Model):
    USER_TYPE_CHOICES = [
        ('trainee', 'Trainee'),
        ('trainer', 'Trainer'),
    ]
    name = models.CharField(max_length=15, null= True)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, null=True, blank=True)
    is_completed= models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name if self.name else "User"



class Trainer(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits= 5, decimal_places= 2)

    def __str__(self):
        return f"Trainer : {self.user.name if self.user else ''}"

class Course(models.Model) :
    COURSE_CATEGORY_CHOICES= [
        ('fit', 'Fit') ,
        ('weight_gain','Weight_Gain'),
        ('weight_loss', 'Weight_Loss'),
        ('muscle_building', 'Muscle_Building'),
        ('phisical_therapy', 'Phisical_Therapy') 
    ]
    title= models.CharField(max_length= 50)
    price= models.DecimalField(max_digits= 5, decimal_places= 2)
    category=  models.CharField(max_length=50, choices=COURSE_CATEGORY_CHOICES, null=True, blank=True)  

    def __str__(self):
        return self.title

    
class Trainee(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    fitness_level= models.IntegerField( null=True, blank=True)
    courses = models.ManyToManyField(Course, through='Enrollment')

    def __str__(self):
        return f"Trainee : {self.user.name if self.user else ''}"

class Enrollment(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    def __str__(self):
        return f"{self.trainee.user.name} enrolled in {self.course.title} on {self.date_enrolled}"
    