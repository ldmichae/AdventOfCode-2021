# %%
draw_order = []
with open('day4-draw-order.txt') as file:
    lines = file.readlines();    
    lines_lst = (lines[0].split(','))
    lines_lst[-1] = lines_lst[-1].split('\n')[0] 
    draw_order = [int(x) for x in lines_lst]

with open('day4-boards.txt') as file:
     lines = file.readlines();    
     groups = [[]]
     for line in lines:
        if line != '\n':
            boardRow = line.split('\n')[0]
            groups[-1].append([int(i) for i in boardRow.split(' ') if i != ''])
        else:
            groups.append([])
            
def transpose_board(board):
    cols = []
    for slot in range(len(board[0])):
        coldata = []
        for row in range(len(board)):
            coldata.append(board[row][slot])
        cols.append(coldata)
    return cols
       
def calculate_score(board, current_pile):
    data = rows[board]
    flat_list = [item for sublist in data for item in sublist]
    remaining_vals = [i for i in flat_list if i not in current_pile]
    return(sum(remaining_vals))
     
rows = {}
columns = {}
counter = 1
for group in groups:
    rows[counter] = group
    columns[counter] = transpose_board(group)
    counter += 1
    
# %%
currently_drawn = draw_order[0:5]
solution_found = False
for value in draw_order[5:]:
    if not solution_found:
        currently_drawn.append(value)
        winner = {'board_num':'','row_or_col': 'row', 'list_idx':0,'data':''}
        for board in rows:
            for i, row in enumerate(rows[board]):
                if all(elem in currently_drawn for elem in row):
                    print('found in row')
                    winner = {'board_num': board, 'row_or_col': 'row', 'list_idx': i, 'data': row}
                    solution_found = True
                else:
                    pass
            for i, col in enumerate(columns[board]):
                if all(elem in currently_drawn for elem in col):
                    print('found in column')
                    winner = {'board_num': board, 'row_or_col':'col', 'list_idx': i, 'data': col}
                    solution_found = True
                else:
                    pass
remaining_points = calculate_score(winner['board_num'], currently_drawn)
winning_num = currently_drawn[-1]

total_score = remaining_points * winning_num
print(total_score)
# %%
