import torch
import numpy as np
import random
from collections import deque
from game import SnakeGameAI , Direction , Point

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self) -> None:
        pass
    
    #were at 44:30 of : "https://www.youtube.com/watch?v=L8ypSXwyBds"