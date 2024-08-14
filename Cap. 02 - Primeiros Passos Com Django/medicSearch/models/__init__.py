from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

from .Profile import Profile
from .Speciality import Speciality
from .DayWeek import DayWeek
from .State import State
from .City import City
from .Neighborhood import Neighborhood