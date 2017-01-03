# https://www.codewars.com/kata/street-fighter-2-character-selection/train/python

fighters = [
    ["Ryu","E.Honda","Blanka","Guile","Balrog","Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

fighters = []
initial_position = (0,0)


# moves = ['up', 'left', 'right', 'left', 'left']
# moves =['down', 'right', 'up', 'down', 'down', 'up', 'up']
# moves = ['right'] * 8
moves =  ["up"]+["left"]*6+["down"]+["right"]*6
# print(moves)
# print(moves.count('left'))

print(len(fighters))
# print(fighters[0][-6])


def street_fighter_selection(fighters, initial_position, moves):
    my_move_dict = {'up': -1, 'down': 1, 'right': 1, 'left': -1}
    my_output = []
    my_current_position = [0,0]
    my_row_count = len(fighters) - 1
    if(len(fighters) == 0):
        return my_output
    for eachMove in moves:
        if(eachMove == 'up' or eachMove == 'down'):
            if((my_current_position[0] >= my_row_count and eachMove == 'down')
            or (my_current_position[0] == 0 and eachMove == 'up')):
                my_current_position = [my_current_position[0], my_current_position[1]]
                my_output.append(fighters[my_current_position[0]][my_current_position[1]])
            else:
                my_current_position = [my_current_position[0] + my_move_dict[eachMove], my_current_position[1]]
                my_output.append(fighters[my_current_position[0]][my_current_position[1]])
        elif(eachMove=='left' or eachMove == 'right'):
            if(my_current_position[1] == 0 and moves.count('left') == len(moves)):
                my_current_position = [my_current_position[0], my_current_position[1] + 6]
            elif(my_current_position[1] == 0 and moves.count('right') == len(moves)):
                my_current_position = [my_current_position[0], my_current_position[1] - 6]
            my_current_position = [my_current_position[0], my_current_position[1] + my_move_dict[eachMove]]
            my_output.append(fighters[my_current_position[0]][my_current_position[1]])
    return my_output



print(street_fighter_selection(fighters, initial_position, moves))
