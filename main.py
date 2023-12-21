from get_comb import get_comb
from get_answer import get_what2remove
import numpy as np
import random
import argparse

def game(table,seed = 0,step = 1):
  #table 생성
  np.random.seed(seed)
  comb = get_comb(table)
  score = 0
  while len(comb) > 0:
    comb = get_comb(table)
    remove = get_what2remove(comb,table,step)
    
    # print(len(comb))
    
    if remove[0][0] != -1:
      score += np.count_nonzero(table[remove[0,0]:remove[0,1],remove[1,0]:remove[1,1]])
      table[remove[0,0]:remove[0,1],remove[1,0]:remove[1,1]] = 0
    
    print(table)
    print("score: ",score)

  return (table,score)
  

parser = argparse.ArgumentParser()

parser.add_argument('--seed',          type=int,   default=0)
parser.add_argument('--min_apple',     type=int,   default=1)
parser.add_argument('--max_apple',     type=int, default=9)
parser.add_argument('--width',     type=int, default=17)
parser.add_argument('--height',     type=int, default=10)
parser.add_argument('--step',     type=int, default=1)
args = parser.parse_args()

np.random.seed(args.seed)

table = np.random.randint(args.min_apple,args.max_apple+1,size = (args.height,args.width))
score_sum = 0
result_table,result_score = game(table,seed = args.seed , step = args.step)


