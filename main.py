import pygame
from pygame.display import *
import time
import random
import pygame_widgets

from PIL import  Image
from PIL import  ImageDraw
from pygame_widgets.slider import Slider
from pygame_widgets.toggle import Toggle
from pygame_widgets.button import Button
import matplotlib.pyplot
from copy import *

import pygame, os

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialisation de Pygame
pygame.init()
pygame.font.init()
time_last_gen=time.time()

# définition des structures par des tableaux
planeur =[[1,0,1],
          [0,1,1],
          [0,1,0]]

canon=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
       [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
grand_vaisseau_nord_est=[[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]]

grand_vaisseau=[[grand_vaisseau_nord_est[j][i] for i in range(len(grand_vaisseau_nord_est[j])-1,-1,-1)]for j in range(len(grand_vaisseau_nord_est)-1,-1,-1)]
canon_bis=[[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1],
[0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1],
[0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1],
[0,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,1],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,1],
[1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1],
[0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1]]

puffer=[[0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0],
        [1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0],
        [0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0],]


puffer_2=[[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,0],
[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1],
[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0],
[0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0]]


grand_canon=[[1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,1,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0]]



taille_simulation = 100 # taille de la simulation au debut
font = pygame.font.Font(None, 24) # police par défaut
screen_recup_info = pygame.display.set_mode()       # récupération des dimension de l'ecran
width=int(min(screen_recup_info .get_size()[1],screen_recup_info .get_size()[0])*0.9)
height=width
calque=[]           # création du calque vide et de la liste d'image pour les images animés
image_list = []

pygame.display.quit()
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((int(width*1.4),height),pygame.RESIZABLE)

historique_nb_cellules=[]

die=[0,1,4,5,6,7,8,9]   # parametres par défaut du jeu de la vie
life = [3]

simulation = [[1 if 0 == random.randint(0,5) else 0 for i in range(taille_simulation)] for j in range(taille_simulation)]
case_a_verifier = set([(i, j) for i in range(len(simulation)) for j in (range(len(simulation)))])

fig, ax = matplotlib.pyplot.subplots()

ax.plot([])
matplotlib.pyplot.close()


def nb_voisins(i,j):
    """
    nb_voisins(i:int,j:int)->int
    prend en paramètre les coordonés d'une case dans la simulation et renvoie son nombre de voisins vivants parmis les 8 cases autour
    """

    if i == 0:
        if j == 0:
            return simulation[i+1][j]+simulation[i][j+1]+simulation[i+1][j+1]
        elif j+1 == len(simulation[0]):
            return simulation[i+1][j]+simulation[i][j-1]+simulation[i+1][j-1]
        else:
            return simulation[i][j-1]+simulation[i][j+1]+ simulation[i + 1][j - 1] + simulation[i + 1][j] + simulation[i + 1][j + 1]
    elif i+1 == len(simulation):
        if j == 0:
            return simulation[i-1][j]+simulation[i-1][j+1]+simulation[i][j+1]
        elif j+1 == len(simulation[0]):
            return simulation[i-1][j-1]+simulation[i-1][j]+simulation[i][j-1]
        else:
           return simulation[i][j-1]+simulation[i-1][j-1]+simulation[i-1][j]+simulation[i-1][j+1]+simulation[i][j+1]
    elif j+1 == len(simulation[0]):
        return simulation[i-1][j]+simulation[i-1][j-1]+simulation[i][j-1]+simulation[i+1][j-1]+simulation[i+1][j]
    elif j == 0 :
        return simulation[i-1][j]+simulation[i+1][j]+simulation[i-1][j+1]+simulation[i][j+1]+simulation[i+1][j+1]

    else:
        return simulation[i - 1][j - 1] + simulation[i - 1][j] + simulation[i - 1][j + 1] + simulation[i][j - 1] + simulation[i][j + 1] + simulation[i + 1][j - 1] + simulation[i + 1][j] + simulation[i + 1][j + 1]


def actualisation():
    """
    actualisation()->list[list[int]]
    Renvoie la génération suivante de la simulation
    :return:
    """
    nouvelle_simulation = [[0 for i in range(len(simulation))] for j in range(len(simulation))]
    nb_cell=0
    global case_a_verifier
    case_a_verifier_actuelle=case_a_verifier.copy()
    case_a_verifier=set([ ])
    nb=0
    if 0 not in life:
        for curr in case_a_verifier_actuelle:
            voisins = nb_voisins(curr[0],curr[1])
            if voisins in life:
                nb_cell+=1
                nouvelle_simulation[curr[0]][curr[1]] = 1
                nb+=1
                ajouter_case_a_verifier(curr[0],curr[1])

            elif voisins in die:
                nouvelle_simulation[curr[0]][curr[1]] = 0
            else:
                nouvelle_simulation[curr[0]][curr[1]] = simulation[curr[0]][curr[1]]
                nb_cell += simulation[curr[0]][curr[1]]
                if(simulation[curr[0]][curr[1]]==1):
                    nb+=1
                    ajouter_case_a_verifier(curr[0],curr[1])
    else:
        for i in range(len(simulation)):
            for j in range(len(simulation[i])):
                voisins = nb_voisins(i, j)
                if voisins in life:
                    nb_cell += 1
                    nouvelle_simulation[i][j] = 1
                    nb += 1
                    ajouter_case_a_verifier(i, j)

                elif voisins in die:
                    nouvelle_simulation[i][j] = 0
                else:
                    nouvelle_simulation[i][j] = simulation[i][i]
                    nb_cell += simulation[i][j]
                    if (simulation[i][j] == 1):
                        nb += 1
                        ajouter_case_a_verifier(i, j)
    return copy(nouvelle_simulation),nb_cell
def ajouter_case_a_verifier(x,y):
    """
    ajouter_case_a_verifier(x:int,y:int)->Null
    Prend en parametre des coordonés d'une case dans la simulation et rajoute tous ses voisins immédiats dans la liste des cases a vérifier
    """
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if x + i < len(simulation)  and y + j < len(simulation)  and x + i >= 0 and y + j >= 0:
                case_a_verifier.add((x + i, y + j))
def redimensionner_jeu(x,y):
    """
    redimensionner_jeu(x:int,y:int)->Null
    prend en parametre les dimensions souhaité pour la simulation et la redimensionne
    """
    global simulation
    if(x<len(simulation)):
        copie_simulation=simulation.copy()
        simulation=[[copie_simulation[j][i]for i in range (x)]for j in range (x) ]

    else:
        for i in range(len(simulation)):
            for j in range(x-len(simulation)):
                simulation[i].append(0)
        for j in range(x - len(simulation)):
            simulation.append([0 for k in range(x)])

def afficher_historique():
    """
    afficher_historique->Null
    Affiche le graphique montrant l'évolution du nombre de cellules par génération
    """
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot([i for i in range(len(historique_nb_cellules))],historique_nb_cellules)
    matplotlib.pyplot.yscale("log")
    matplotlib.pyplot.show()

def appliquer_calque(calque_a_coller):
    """
    appliquer_calque(calque_a_coller:list[list[int]])->Null
    donne a calque la valeur passé en parametre
    """
    global calque
    calque = calque_a_coller.copy()

def test_toggle():
    """
    test_toggle()->Null
    Teste chacun des toggle(les boutons avec 2 valeurs), modifie les valeurs dans les listes indiquant le nombre de
    voisins nécessaire pour vivre ou mourrire et change la valeur de son homologue si les deux sont allumés
    """
    if (toggle0l.getValue()) != (0 in life):
        if(toggle0l.getValue()):
            if toggle0d.getValue():
                die.remove(0)
                toggle0d.toggle()
            life.append(0)
        else:
            life.remove(0)
    if (toggle0d.getValue()) != (0 in die):
        if (toggle0d.getValue()):
            if toggle0l.getValue():
                life.remove(0)
                toggle0l.toggle()
            die.append(0)
        else:
            die.remove(0)
    if (toggle1l.getValue()) != (1 in life):
        if(toggle1l.getValue()):
            if toggle1d.getValue():
                die.remove(1)
                toggle1d.toggle()
            life.append(1)
        else:
            life.remove(1)
    if (toggle1d.getValue()) != (1 in die):
        if (toggle1d.getValue()):
            if toggle1l.getValue():
                life.remove(1)
                toggle1l.toggle()
            die.append(1)
        else:
            die.remove(1)
    if (toggle2l.getValue()) != (2 in life):
        if(toggle2l.getValue()):
            if toggle2d.getValue():
                die.remove(2)
                toggle2d.toggle()
            life.append(2)
        else:
            life.remove(2)
    if (toggle2d.getValue()) != (2 in die):
        if (toggle2d.getValue()):
            if toggle2l.getValue():
                life.remove(2)
                toggle2l.toggle()
            die.append(2)
        else:
            die.remove(2)
    if (toggle3l.getValue()) != (3 in life):
        if(toggle3l.getValue()):
            if toggle3d.getValue():
                die.remove(3)
                toggle3d.toggle()
            life.append(3)
        else:
            life.remove(3)
    if (toggle3d.getValue()) != (3 in die):
        if (toggle3d.getValue()):
            if toggle3l.getValue():
                life.remove(3)
                toggle3l.toggle()
            die.append(3)
        else:
            die.remove(3)
    if (toggle4l.getValue()) != (4 in life):
        if(toggle4l.getValue()):
            if toggle4d.getValue():
                die.remove(4)
                toggle4d.toggle()
            life.append(4)
        else:
            life.remove(4)
    if (toggle4d.getValue()) != (4 in die):
        if (toggle4d.getValue()):
            if toggle4l.getValue():
                life.remove(4)
                toggle4l.toggle()
            die.append(4)
        else:
            die.remove(4)
    if (toggle5l.getValue()) != (5 in life):
        if(toggle5l.getValue()):
            if toggle5d.getValue():
                die.remove(5)
                toggle5d.toggle()
            life.append(5)
        else:
            life.remove(5)
    if (toggle5d.getValue()) != (5 in die):
        if (toggle5d.getValue()):
            if toggle5l.getValue():
                life.remove(5)
                toggle5l.toggle()
            die.append(5)
        else:
            die.remove(5)
    if (toggle6l.getValue()) != (6 in life):
        if(toggle6l.getValue()):
            if toggle6d.getValue():
                die.remove(6)
                toggle6d.toggle()
            life.append(6)
        else:
            life.remove(6)
    if (toggle6d.getValue()) != (6 in die):
        if (toggle6d.getValue()):
            if toggle6l.getValue():
                life.remove(6)
                toggle6l.toggle()
            die.append(6)
        else:
            die.remove(6)
    if (toggle7l.getValue()) != (7 in life):
        if(toggle7l.getValue()):
            if toggle7d.getValue():
                die.remove(7)
                toggle7d.toggle()
            life.append(7)
        else:
            life.remove(7)
    if (toggle7d.getValue()) != (7 in die):
        if (toggle7d.getValue()):
            if toggle7l.getValue():
                life.remove(7)
                toggle7l.toggle()
            die.append(7)
        else:
            die.remove(7)
    if (toggle8l.getValue()) != (8 in life):
        if(toggle8l.getValue()):
            if toggle8d.getValue():
                die.remove(8)
                toggle8d.toggle()
            life.append(8)
        else:
            life.remove(8)
    if (toggle8d.getValue()) != (8 in die):
        if (toggle8d.getValue()):
            if toggle8l.getValue():
                life.remove(8)
                toggle8l.toggle()
            die.append(8)
        else:
            die.remove(8)


def faire_gif():
    """
    faire_gif()->Null
    Créé un gif et le sauvegarde dans image avec pour nom generation{numero_generation_depart}-{numero_generation_fin)
    a partir de la liste d'image
    """
    global image_list

    frame_one = image_list[0]
    frame_one.save(f"image/generation{generation-len(image_list)}-{generation}.gif", format="GIF", append_images=image_list,
                   save_all=True, duration=150, loop=0)

def enregistrement():
    """
    enregistrement()->Null
    Demarre ou termine l'enregistrement, met capture en cours a vrai si l'enregistrement démarre sinon a faux  et fin_capture a vrai
    """
    global capture_en_cours
    global fin_capture
    if(capture_en_cours):
        capture_en_cours=0
        fin_capture=1
    else:
        capture_en_cours=1

def remplissage():
    """
    remplissage()
    donne a toute les cases de la simulation une valeur aléatoire avec une densité de 1/6 en moyenne
    :return:
    """
    global  simulation
    global case_a_verifier
    simulation = [[1 if 0 == random.randint(0, 5) else 0 for i in range(taille_simulation)] for j in range(taille_simulation)]
    case_a_verifier = set([(i, j) for i in range(len(simulation)) for j in (range(len(simulation)))])

def afficher_et_repositionner_texte_et_bouton():
    """
    afficher_et_repositionner_texte_et_bouton()
    affiche et repositionne le texte lorsque la fenetre a été redimensionné
    """
    slide_taille_simulation.setX(pos_boutons)
    slide_taille_simulation.draw()

    global text_taille_simulation
    text_taille_simulation = font.render("Nombre de cellules par coté: " + str(taille_simulation), 1, (255, 255, 255))
    toggle0l.setX(pos_boutons)
    toggle0l.draw()
    toggle0d.setX(pos_boutons+150)
    toggle0d.draw()

    toggle1l.setX(pos_boutons)
    toggle1l.draw()
    toggle1d.setX(pos_boutons+150)
    toggle1d.draw()

    toggle2l.setX(pos_boutons)
    toggle2l.draw()
    toggle2d.setX(pos_boutons+150)
    toggle2d.draw()

    toggle3l.setX(pos_boutons)
    toggle3l.draw()
    toggle3d.setX(pos_boutons+150)
    toggle3d.draw()

    toggle4l.setX(pos_boutons)
    toggle4l.draw()
    toggle4d.setX(pos_boutons+150)
    toggle4d.draw()

    toggle5l.setX(pos_boutons)
    toggle5l.draw()
    toggle5d.setX(pos_boutons+150)
    toggle5d.draw()

    toggle6l.setX(pos_boutons)
    toggle6l.draw()
    toggle6d.setX(pos_boutons+150)
    toggle6d.draw()

    toggle7l.setX(pos_boutons)
    toggle7l.draw()
    toggle7d.setX(pos_boutons+150)
    toggle7d.draw()

    toggle8l.setX(pos_boutons)
    toggle8l.draw()
    toggle8d.setX(pos_boutons+150)
    toggle8d.draw()

    Bouton_planeur.setX(pos_boutons)
    Bouton_planeur.draw()

    Bouton_canon.setX(pos_boutons)
    Bouton_canon.draw()

    Bouton_locomotive.setX(pos_boutons)
    Bouton_locomotive.draw()

    Bouton_vaisseau.setX(pos_boutons + 120)
    Bouton_vaisseau.draw()

    Bouton_grand_canon.setX(pos_boutons + 120)
    Bouton_grand_canon.draw()

    Bouton_puffer_2.setX(pos_boutons + 120)
    Bouton_puffer_2.draw()

    Bouton_enregistrement.setX(pos_boutons)
    Bouton_enregistrement.draw()

    Bouton_remplissage.setX(pos_boutons + 120)
    Bouton_remplissage.draw()
    Bouton_historique_nombre_cellule.setX(pos_boutons)
    Bouton_historique_nombre_cellule.draw()

    screen.blit(text0, (pos_boutons + 100, 125))
    screen.blit(text1, (pos_boutons + 100, 175))
    screen.blit(text2, (pos_boutons + 100, 225))
    screen.blit(text3, (pos_boutons + 100, 275))
    screen.blit(text4, (pos_boutons + 100, 325))
    screen.blit(text5, (pos_boutons + 100, 375))
    screen.blit(text6, (pos_boutons + 100, 425))
    screen.blit(text7, (pos_boutons + 100, 475))
    screen.blit(text8, (pos_boutons + 100, 525))
    screen.blit(text_changement_regle, (pos_boutons + 20, 70))
    screen.blit(text_mort, (pos_boutons + 155, 100))
    screen.blit(text_vie, (pos_boutons + 10, 100))
    screen.blit(text_nb_voisins, (pos_boutons + 60, 95))


def creer_bouton_et_texte():
    """
    creer_bouton_et_texte
    créé et initialise les bouton et le texte
    """
    global slide_taille_simulation
    slide_taille_simulation = Slider(screen, pos_boutons, 50, 200, 15, min=4, max=800, step=1, initial=100)

    global text0
    global toggle0l
    global toggle0d

    global text0
    global toggle0l
    global toggle0d

    global text1
    global toggle1l
    global toggle1d

    global text2
    global toggle2l
    global toggle2d

    global text3
    global toggle3l
    global toggle3d

    global text4
    global toggle4l
    global toggle4d

    global text5
    global toggle5l
    global toggle5d

    global text6
    global toggle6l
    global toggle6d

    global text7
    global toggle7l
    global toggle7d

    global text8
    global toggle8l
    global toggle8d

    global text_changement_regle
    global text_vie
    global text_nb_voisins
    global text_mort

    global Bouton_historique_nombre_cellule
    global Bouton_enregistrement
    global Bouton_remplissage
    global Bouton_planeur
    global Bouton_canon
    global Bouton_locomotive
    global Bouton_vaisseau
    global Bouton_grand_canon
    global Bouton_puffer_2

    slide_taille_simulation = Slider(screen, pos_boutons, 50, 200, 15, min=4, max=800, step=1, initial=100)

    text0 = font.render("0", 1, (255, 255, 255))
    toggle0l = Toggle(screen, pos_boutons, 125, 50, 20)
    toggle0d = Toggle(screen, 150 + pos_boutons, 125, 50, 20, startOn=1)

    text1 = font.render("1", 1, (255, 255, 255))
    toggle1l = Toggle(screen, pos_boutons, 175, 50, 20)
    toggle1d = Toggle(screen, 150 + pos_boutons, 175, 50, 20, startOn=1)

    text2 = font.render("2", 1, (255, 255, 255))
    toggle2l = Toggle(screen, pos_boutons, 225, 50, 20)
    toggle2d = Toggle(screen, 150 + pos_boutons, 225, 50, 20)

    text3 = font.render("3", 1, (255, 255, 255))
    toggle3l = Toggle(screen, pos_boutons, 275, 50, 20, startOn=1)
    toggle3d = Toggle(screen, 150 + pos_boutons, 275, 50, 20)

    text4 = font.render("4", 1, (255, 255, 255))
    toggle4l = Toggle(screen, pos_boutons, 325, 50, 20)
    toggle4d = Toggle(screen, 150 + pos_boutons, 325, 50, 20, startOn=1)

    text5 = font.render("5", 1, (255, 255, 255))
    toggle5l = Toggle(screen, pos_boutons, 375, 50, 20)
    toggle5d = Toggle(screen, 150 + pos_boutons, 375, 50, 20, startOn=1)

    text6 = font.render("6", 1, (255, 255, 255))
    toggle6l = Toggle(screen, pos_boutons, 425, 50, 20)
    toggle6d = Toggle(screen, 150 + pos_boutons, 425, 50, 20, startOn=1)

    text7 = font.render("7", 1, (255, 255, 255))
    toggle7l = Toggle(screen, pos_boutons, 475, 50, 20)
    toggle7d = Toggle(screen, 150 + pos_boutons, 475, 50, 20, startOn=1)

    text8 = font.render("8", 1, (255, 255, 255))
    toggle8l = Toggle(screen, pos_boutons, 525, 50, 20)
    toggle8d = Toggle(screen, 150 + pos_boutons, 525, 50, 20, startOn=1)

    text_changement_regle = font.render("Modifier les règles : ", 1, (255, 255, 255))
    text_vie = font.render("Nait", 1, (255, 255, 255))
    text_nb_voisins = font.render("Nb voisins", 1, (255, 255, 255))
    text_mort = font.render("Meurt", 1, (255, 255, 255))

    Bouton_historique_nombre_cellule = Button(screen, pos_boutons, 565, 150, 30, onClick=lambda: afficher_historique(),
                                              radius=80, text="Evolution Nb Cellule")

    Bouton_enregistrement = Button(screen, pos_boutons, 615, 105, 30, onClick=lambda: enregistrement(), radius=80,
                                   text="Enregistrement")
    Bouton_remplissage = Button(screen, pos_boutons + 100, 615, 105, 30, onClick=lambda: remplissage(), radius=80,
                                text="Remplir la grille")

    Bouton_planeur = Button(screen, pos_boutons, 655, 105, 30, onClick=lambda: appliquer_calque(planeur), radius=80,
                            text="planeur")
    Bouton_canon = Button(screen, pos_boutons, 695, 105, 30, onClick=lambda: appliquer_calque(canon), radius=80,
                          text="Canon")
    Bouton_locomotive = Button(screen, pos_boutons, 735, 105, 30, onClick=lambda: appliquer_calque(puffer), radius=80,
                               text="Puffer")

    Bouton_vaisseau = Button(screen, pos_boutons + 100, 655, 105, 30, onClick=lambda: appliquer_calque(grand_vaisseau),
                             radius=80, text="Vaisseau(grand)")
    Bouton_grand_canon = Button(screen, pos_boutons + 100, 695, 105, 30, onClick=lambda: appliquer_calque(grand_canon),
                                radius=80, text="Canon(grand)")
    Bouton_puffer_2 = Button(screen, pos_boutons + 100, 735, 105, 30, onClick=lambda: appliquer_calque(puffer_2),
                             radius=80, text="Locomotive")


run = True
temp_entre_generation = 0.1
generation = 0
nb_cell=0
pos_boutons=width+int(((width*0.4-200)/2))

clock = pygame.time.Clock()

fin_capture=False       # initialisation variables
capture_en_cours=False
hide_text=False


creer_bouton_et_texte()
arret= False
while not arret:# tant que l'arret n'as pas été demandé
    width = (min(screen.get_size()[1],int( screen.get_size()[0]/1.4)) ) # réadapte les dimensions si l'écran change de taille
    height = width
    pos_boutons = width + int(((width * 0.4 - 200) / 2))

    if slide_taille_simulation.getValue() != taille_simulation: # si le slider a été bougé, adapter le jeu en conséquence
        taille_simulation = slide_taille_simulation.getValue()
        redimensionner_jeu(taille_simulation,taille_simulation)
        case_a_verifier = set([(i, j) for i in range(len(simulation)) for j in (range(len(simulation)))])

    test_toggle()
    screen.fill((0,100,100))    # met le fond en bleu
    fond_blanc=pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0 ,0,width ,height))# affiche un carré blancc pour la simulation en fond

    events=pygame.event.get() # récupère est stocke les évènepents

    for event in events:    # pour chaque évènement detecté
        if event.type == pygame.VIDEORESIZE:    # recadrer la fenetre sans aller en dessous de (1100,800)
            screen = pygame.display.set_mode((max(1100,event.w), max(800,event.h)),pygame.RESIZABLE)
        if event.type == pygame.QUIT:   # quitter si l'utilisateur le demande
            arret = True
            pygame.quit()
        if(event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_h): # cacher le texte si la touche h est pressé
                if hide_text:
                    hide_text=False
                else:
                    hide_text=True
            if(event.key==pygame.K_p):# mettre en pauche si la touche P est pressé
                if run:
                    run=False
                else:
                    run=True
            if (event.key == pygame.K_UP): # si la touche flèche haut est pressé augmenter le délai
                temp_entre_generation+=0.1
            if (event.key== pygame.K_DOWN): # si la touche flèche bas est pressé et que le délais est  supérieur a 0.1, enlever 0.1 sinon le mettre a 0
                if temp_entre_generation>=0.1:
                    temp_entre_generation-=0.1
                else:
                    temp_entre_generation =0
            if(event.key== pygame.K_r): # si la touche R est pressé: remplir aléatoirement la grille avec densité 1/6
                simulation = [[1 if 0 == random.randint(0, 2) else 0 for i in range(taille_simulation)] for j in range(taille_simulation)]
                case_a_verifier = set( [(i, j) for i in range (len(simulation)) for j in (range(len(simulation)))] )
        if(event.type == pygame.MOUSEBUTTONDOWN) :
            if(event.button==1):    # si un clique gauche est détecté
                pos=pygame.mouse.get_pos()
                if(pos[0]<width and pos[1]<height): # si la souris est sur le quadrillage
                    if calque==[]:  # si le calque est vide
                        if(simulation[int(pos[0]/(width/taille_simulation))][int(pos[1]/(height/taille_simulation))]):    # si la cellule cliqué et vivante alors elle devient morte
                            simulation[int(pos[0] / (width/taille_simulation))][int(pos[1] / (height/taille_simulation))]=0
                        else:                                                                       # sinon elle devient vivante
                            simulation[int(pos[0] / (width/taille_simulation))][int(pos[1] / (height/taille_simulation))] = 1
                            ajouter_case_a_verifier(int(pos[0] / (width/taille_simulation)),int(pos[1] / (height/taille_simulation)))

                    else:   # si le calque est plein
                        pos = pygame.mouse.get_pos()
                        x_souris = int(pos[0] / (width / taille_simulation))
                        y_souris = int(pos[1] / (height / taille_simulation))   # recupere la case survolé par la souris
                        for i in range(len(calque)):
                            for j in range(len(calque[0])):
                                if (i + x_souris < len(simulation) and j + y_souris < len(simulation)) :    # recopie chaque case du calque
                                    simulation[i+x_souris][j+y_souris]=calque[i][j]
                                    ajouter_case_a_verifier(i+x_souris,j+y_souris)

                        calque=[]
            if(event.button==4 and taille_simulation>=9): # molette +, rétréci le quadrillage si il n'est pas déja trop petit
                taille_simulation-=5
                redimensionner_jeu(taille_simulation,taille_simulation)
                slide_taille_simulation.setValue(taille_simulation)
                case_a_verifier_copie=case_a_verifier.copy()
                case_a_verifier = set([curr if (curr[0]<len(simulation) and curr[1]<len(simulation)) else (0,0) for curr in case_a_verifier_copie])
            if (event.button == 5 and taille_simulation<=795):  # molette +, aggrandi le quadrillage si il n'est pas déja trop grand
                taille_simulation += 5
                redimensionner_jeu(taille_simulation, taille_simulation)
                slide_taille_simulation.setValue(taille_simulation)

    pygame_widgets.update(events)   # donne les évènements a pygames_widget

    espace_entre_cellules=min(100/(taille_simulation),1)

    if (espace_entre_cellules >= 1):   # dessinne le quadrillage si il fait plus d'un pixel
        for i in range (len(simulation)):
            for j in range(len(simulation[0])):
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i * (width / taille_simulation) - espace_entre_cellules,j * (height / taille_simulation) - espace_entre_cellules,espace_entre_cellules , (height / taille_simulation)+1))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i * (width / taille_simulation) - espace_entre_cellules,j * (height / taille_simulation) - espace_entre_cellules,(height / taille_simulation)+1, espace_entre_cellules))
    for curr in case_a_verifier:    # affiche un carré noir pour chaque cellule vivante
        if(simulation[curr[0]][curr[1]]):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(curr[0] * (width / taille_simulation), curr[1] * (height / taille_simulation),
                                                            (width / taille_simulation) - espace_entre_cellules + 1,
                                                            (height / taille_simulation) - espace_entre_cellules + 1))

    if(calque!=None):       # si le calque n'est pas vide
        pos = pygame.mouse.get_pos()
        x_souris = int(pos[0] / (width / taille_simulation))    # convertis les coordonés de la souris pour connaire la cellule survolé
        y_souris = int(pos[1] / (height / taille_simulation))
        for i in range(len(calque)):
            for j in range(len(calque[0])):
                if(calque[i][j]):       # dessinne la figure dans le calque en vert
                    pygame.draw.rect(screen, (50,200,50), pygame.Rect((i+x_souris)*(width/taille_simulation), (j+y_souris)*(height/taille_simulation), (width/taille_simulation)-espace_entre_cellules+1, (height/taille_simulation)-espace_entre_cellules+1))


    pygame.draw.rect(screen, (0, 100, 100), pygame.Rect(width,0, 4000, width)) # affiche un fond bleu en fond a droite



    if not hide_text:       # créé les textes informatifes en haut a gauche
        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 0, 375, 80))
        text = font.render("Generation: "+str(generation), 1, (0, 0, 0))
        text_cell = font.render("Nb cellules: "+str(nb_cell), 1, (0, 0, 0))
        text_fps = font.render("FPS: " + str(clock.get_fps()), 1, (0, 0, 0))
        text_temp_entre_generation= font.render("Temp souhaité entre chaque génération : " + str(round(temp_entre_generation*10)/10), 1, (0, 0, 0))

    afficher_et_repositionner_texte_et_bouton()     # affiche tous les textes/boutons/slider ormis ceux en haut a gauche



    if not hide_text:                       # afficher les textes informatifes
      screen.blit(text, (0, 0))
      screen.blit(text_cell, (0, 20))
      screen.blit(text_fps,(0,40))
      screen.blit(text_temp_entre_generation,(0,60))




    screen.blit(text_taille_simulation,(width+int(((width*0.4-250)/2)),25)) # afficher le texte indiquant les dimension de la grille



    pygame.display.update()
    clock.tick(60)
    if(run and time.time()-time_last_gen>=temp_entre_generation):           # Si le programme n'est pas en pause et que le délais demandé est atteint
        time_last_gen=time.time()
        if capture_en_cours:                                # Créer et rajouter l'image actuelle a la liste
            h,w=800,800
            img = Image.new("RGB", (h, w),"#FFFFFF")
            img1 = ImageDraw.Draw(img)
            if (espace_entre_cellules >= 1):                   # faire le quadrillage
                for i in range(len(simulation)):
                    for j in range(len(simulation[0])):
                        rectangle = [(i * (h / len(simulation)), j * (w / len(simulation))),
                                     ((i + 1) * (h / len(simulation)), (j + 1) * (w / len(simulation)))]
                        img1.rectangle(rectangle, fill="#FFFFFF", outline="#000000")

            for curr in case_a_verifier:                    # faire les cellules
                if (simulation[curr[0]][curr[1]]):
                    rectangle = [(curr[0] * (h/ len(simulation)), curr[1] * (w/len(simulation))),
                                 ((curr[0] + 1) * ( h/len(simulation)), (curr[1] + 1) * (w/len(simulation)))]
                    img1.rectangle(rectangle, fill="#000000")
            image_list.append(img)


        if fin_capture or len(image_list)>500:              # Si la fin de la capture a été demandé ou si il y a plus de 500 images
            faire_gif()
            image_list=[]
            fin_capture=0
            capture_en_cours=0

        generation += 1
        act = actualisation()                               # recuperation de la nouvelle grille et du nombre de cellule
        simulation = act[0]
        nb_cell= act[1]
        historique_nb_cellules.append(nb_cell)              # Rajout a l'historique
