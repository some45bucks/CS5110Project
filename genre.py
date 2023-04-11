from enum import Enum
import random

class Genre(Enum):
    DEFAULT = 0
    FPS = 1
    ADVENTURE = 2
    ROGUELITE = 3
    PUZZLE = 4
    OTHER = 5

def random_genre():
        return random.choice(list(Genre))
    
def get_random_genre_preferences():
    preferences = {}
    
    for g in Genre:
        preferences[g] =  random.uniform(0,1)
        
    return preferences