import numpy as np
def get_comb(table):
  comb = np.array([[[0,0],[0,0]]])
  #선택 가능한 조합 저장할 array 생성

  M = table.shape[0] #M=4
  N = table.shape[1]
  for x in range(M):
    for y in range(N):
      if (table[x,y] != 0):
        max_square_size = min(M - x , N - y)
        #만들 수 있는 제일 큰 square 의 한 변의 길이 구함 예를 들어 현재 좌표가 2,2고 table 이 4x4 라면 3x3이 가장 큰 정사각형
        s_s = 1 #정사각형의 크기
        while np.sum(table[x:x+s_s, y:y+s_s]) < 10 and (s_s <= max_square_size):
          #정사각형에 해당하는 원소들의 합이 10보다 작다면 반복문 계속 수행한다.
          width = 2
          height = 2
          while np.sum(table[x:x+width, y:y+s_s]) < 10 and (x+width <= M):
            #해당하는 직사각형에 대한 크기가 10 이하일 때 까지 직사각형 크기 오른쪽으로 넓힘, 만약 벽에 도달하면 멈춤
            width += 1
            #높이 고정, 너비만 변화 시킨다.
          if np.sum(table[x:x+width, y:y+s_s]) == 10:
            comb = np.append(comb,[[(x,x+width),(y,y+s_s)]],axis = 0)
            # print(f"Find {(x,y),(x+width-1,y+s_s-1)}!!")
            
          while np.sum(table[x:x+s_s, y:y+height]) < 10 and (y+height <= N):
            #해당하는 직사각형에 대한 크기가 10 이하일 때 까지 직사각형 크기 아래로 넓힘, 만약 벽에 도달하면 멈춤
            height += 1
            #너비 고정, 높이만 변화 시킨다.
          if np.sum(table[x:x+s_s, y:y+height]) == 10:
            comb = np.append(comb,[[(x,x+s_s),(y,y+height)]],axis = 0)
            # print(f"Find {(x,y),(x+s_s-1,y+height-1)}!!")

            
          
          s_s +=1 # 정사각형의 크기를 늘려서 다시 수행
        
  comb = np.delete(comb, 0, axis=0)
  return comb