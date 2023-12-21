# from get_comb import get_comb
# import random
# import numpy as np

# def get_what2remove(comb,table,step = 1):
#   best_choice_indexs = [0]  
#   best_next_comb_num = 0 #best comb_num of next table
#   for i,choice in enumerate(comb):
#     table_next = table.copy()
#     table_next[choice[0,0]:choice[0,1],choice[1,0]:choice[1,1]] = 0
#     next_comb = get_comb(table_next)
#     next_comb_num =len(next_comb)

      
#     #재귀 호출
#     if (step >= 2) and (next_comb_num > 0):
#       next_choice = get_what2remove(next_comb,table_next,step-1)
#       if next_choice.any() != -1:
#         table_next[next_choice[0,0]:next_choice[0,1],next_choice[1,0]:next_choice[1,1]] = 0
#         next_comb = get_comb(table_next)
#         next_comb_num =len(next_comb)
#     # print(f"if we choose{choice}, then next comb_num is {next_comb_num}")
#     if next_comb_num > best_next_comb_num:
#       best_choice_indexs = [i]
#       best_next_comb_num = next_comb_num
#     elif next_comb_num == best_next_comb_num:
#       #만약 다음 테이블에서 조합의 개수가 같다면, 더 많이 지우는 것을 선택
#       if (len(comb[i]) > len(comb[best_choice_indexs[0]])):
#         best_choice_indexs = [i]
#         best_next_comb_num = next_comb_num
#       elif (len(comb[i]) == len(comb[best_choice_indexs[0]])):
#         #만약 다음 테이블에서 조합의 개수가 같고, 지우는 것도 같다면 랜덤하게 선택하기 위해 저장해둔다.
#         best_choice_indexs.append(i)
#   # print(f"The best choice is {comb[best_choice_index]} and it have {best_next_comb_num} comb in next table")
#   #index 들 중 랜덤하게 하나 선택해서 반환
#   if (len(best_choice_indexs) == 0) or(len(comb) == 0):
#     print("Reach The End")
#     return -1
#   return(comb[random.choice(best_choice_indexs)])


from get_comb import get_comb
import random
import numpy as np

def get_what2remove(comb, table, step=1, cache=None):
    if cache is None:
        cache = {}

    best_choice_indexes = []
    best_next_comb_num = 0

    for i, choice in enumerate(comb):
        table_next = table.copy()
        table_next[choice[0, 0]:choice[0, 1], choice[1, 0]:choice[1, 1]] = 0
        table_next_key = tuple(map(tuple, table_next))

        if table_next_key in cache:
            next_comb, next_comb_num = cache[table_next_key]
        else:
            next_comb = get_comb(table_next)
            next_comb_num = len(next_comb)
            cache[table_next_key] = (next_comb, next_comb_num)

        if step >= 2 and next_comb_num > 0:
            next_choice = get_what2remove(next_comb, table_next, step-1, cache)
            if next_choice[0][0] != -1:
                table_next[next_choice[0, 0]:next_choice[0, 1], next_choice[1, 0]:next_choice[1, 1]] = 0
                next_comb = get_comb(table_next)
                next_comb_num = len(next_comb)

        if next_comb_num > best_next_comb_num:
            best_choice_indexes = [i]
            best_next_comb_num = next_comb_num
        elif next_comb_num == best_next_comb_num:
            best_choice_indexes.append(i)

    if not best_choice_indexes:
        print("Reach The End")
        return np.array([[-1]])
    return comb[random.choice(best_choice_indexes)]

# Example usage
# table = np.array(...)  # Define your table
# comb = get_comb(table)
# choice = get_what2remove(comb, table)

