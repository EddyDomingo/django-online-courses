from django.db import models

# Create your models here.
class StudentCourses(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Email = models.EmailField()
    Technology_Entrepreneurship = 'Technology Entrepreneurship'
    Intro_to_Aerospace_Structures = 'Intro to Aerospace Structures'
    Connected_Strategy = 'Connected Strategy'
    Exercising_Leadership = 'Exercising Leadership'
    Intro_to_Project_Management = 'Intro to Project Management'
    Science_of_Happiness_at_Work = 'Science of Happiness at Work'
    courseChoice = [
        (Technology_Entrepreneurship, 'Technology Entrepreneurship'),
        (Intro_to_Aerospace_Structures,  'Intro to Aerospace Structures'),
        (Connected_Strategy,  'Connected Strategy'),
        (Exercising_Leadership,  'Exercising Leadership'),
        (Intro_to_Project_Management,  'Intro to Project Management'),
        (Science_of_Happiness_at_Work,  'Science of Happiness at Work'),
    ]
    courseWork = models.CharField(
        max_length=50,
        choices=courseChoice,
        default=Technology_Entrepreneurship,
    )

    def __str__(self):
        return  '{} {} {} {} {}'.format(self.Fname, ",", self.Lname, ",", self.Email)


