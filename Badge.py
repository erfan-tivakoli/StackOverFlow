__author__ = 'Rfun'
from enum import Enum

class Badge():
    def __init__(self, user, time, title):
        self.owner = user
        self.time = time
        self.title = title


class BadgeTitle(Enum):
    Curious = 1
    Inquisitive = 2
    Socratic = 3
    Explainer = 4
    Refiner = 5
    Illuminator = 6

def get_enum_from_string(input):
    if input == 'Curious':
        return BadgeTitle.Curious
    elif input == 'Inquisitive':
        return BadgeTitle.Inquisitive
    elif input == 'Socratic':
        return BadgeTitle.Socratic
    elif input == 'Explainer':
        return BadgeTitle.Explainer
    elif input == 'Refiner':
        return BadgeTitle.Refiner
    elif input == 'Illuminator':
        return BadgeTitle.Illuminator
