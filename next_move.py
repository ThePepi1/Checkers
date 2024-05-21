RED = (255, 0, 0)
BLUE = (0, 0, 255)
def Outside(x, y):
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return True
    return False
class Que:
    def __init__(self):
        self.queue = []
    def append(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def VariableDeepth(reds,blues):
    lenght = 0
    for key in reds.keys():
        if reds[key].movment == "KING":
            lenght += 10
        else:
            lenght += 2
    for key in blues.keys():
        if blues[key].movment == "KING":
            lenght += 10
        else:
            lenght += 2
    if lenght < 30:
        return 6
    else:
        return 5






def predict_next_move(state):
    reds, blues = generate_reds(state)
    best_move = None
    best_score = -100000
    depth = VariableDeepth(reds,blues)
    for moves in generate_next_move(reds,state):
        score = predict_next_move_tree(state, VariableDeepth(reds,blues), moves, reds, blues,False, best_score, 100000)
        if score > best_score:
            best_score = score
            best_move = moves
    #print("Best move", best_move)
    #print("_________________________")
    return best_move

        
def predict_next_move_tree(state, depth, last_move, played, playing,minmax, alpha, beta):

    played[last_move[0][0]] = played[last_move[1]]
    del played[last_move[1]]
    state[last_move[0][0]] = state[last_move[1]]

    del state[last_move[1]]
    state[last_move[0][0]].row = last_move[0][0][0]
    state[last_move[0][0]].col = last_move[0][0][1]
    if state[last_move[0][0]].row == 0 and state[last_move[0][0]].movment == "Dawn" or state[last_move[0][0]].row == 7 and state[last_move[0][0]].movment == "UP":
        state[last_move[0][0]].movment = "KING"
        promoted = True
    else:
        promoted = False
    figures_removed = []
    if last_move[0][1]:
        for figures in last_move[0][1]:
            figures_removed.append((figures, state[figures]))
            del state[figures]
            del playing[figures]
    if depth == 0:
        score =  evaluate(played,playing)
        for cordinates , figures in figures_removed:
            state[cordinates] = figures
            playing[cordinates] = state[cordinates]
        played[last_move[1]] = played[last_move[0][0]]
        del played[last_move[0][0]]
        state[last_move[1]] = state[last_move[0][0]]
        del state[last_move[0][0]]
        if promoted:
            state[last_move[1]].Demote()
        state[last_move[1]].row = last_move[1][0]
        state[last_move[1]].col = last_move[1][1]
        return score
    ending = game_ended(played, playing,minmax)
    if  ending != 0:
        for cordinates , figures in figures_removed:
            state[cordinates] = figures
            playing[cordinates] = state[cordinates]
        played[last_move[1]] = played[last_move[0][0]]
        del played[last_move[0][0]]
        state[last_move[1]] = state[last_move[0][0]]
        del state[last_move[0][0]]
        if promoted:
            state[last_move[1]].Demote()
        state[last_move[1]].row = last_move[1][0]
        state[last_move[1]].col = last_move[1][1]
        return ending
    
    best_move = None
    best_score = -100000
    if not minmax:
        best_score = 100000

    for move in generate_next_move(playing, state):
        if minmax:
            score = predict_next_move_tree(state, depth - 1, move, playing,played, not minmax, alpha , beta)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        else:
            score = predict_next_move_tree(state, depth - 1, move, playing,played, not minmax, alpha , beta)   
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break

    for cordinates , figures in figures_removed:
        state[cordinates] = figures
        playing[cordinates] = state[cordinates]
    played[last_move[1]] = played[last_move[0][0]]
    del played[last_move[0][0]]
    state[last_move[1]] = state[last_move[0][0]]
    del state[last_move[0][0]]
    if promoted:
        state[last_move[1]].Demote()
    state[last_move[1]].row = last_move[1][0]
    state[last_move[1]].col = last_move[1][1]
    if abs(best_score) == 100000:
        return 0
    return best_score
    



def evaluate(reds,blues):
    
    red_score = 0
    blue_score = 0
    check_key = 0;
    for key in reds:
        check_key = key
        red_score += 1
        if reds[key].movment == "KING":
            red_score += 0.5
            if reds[key].col == 0 or reds[key].col == 7:
                red_score += 0.1
        else:
            if reds[key].col == 0 or reds[key].col == 7:
                red_score += 0.05


    for key in blues:
        blue_score += 1
        if blues[key].movment == "KING":
            blue_score += 0.5
            if blues[key].col == 0 or blues[key].col == 7:
                blue_score += 0.1
        else:
            if blues[key].col == 0 or blues[key].col == 7:
                blue_score += 0.05    
    
    
    if(reds[check_key].color == RED):
        return red_score - blue_score
    else:
        return blue_score - red_score

def generate_reds(state):
    reds = {}
    blues = {}
    for key in state:
        if state[key].color == RED:
            reds[key] = state[key]
        elif state[key].color == BLUE:
            blues[key] = state[key]
    return reds, blues
def generate_next_move(red,state):
    red_figures = red.copy()
    for figure in red_figures:
        moves = all_posible_moves(red_figures[figure], state)
        for move in moves:   
            yield move , figure
def all_posible_moves(selected_checker, checkers):
    moves = []
    if selected_checker:
        color, row, col = selected_checker.color, selected_checker.row, selected_checker.col
        movment = selected_checker.movment
        if movment == "UP":       # Check if the move is diagonal and forward
            if (row - 1, col - 1) not in checkers:
                if not Outside(row - 1, col - 1):
                    moves.append(((row - 1, col - 1),None))
            if (row - 1, col + 1) not in checkers:
                if not Outside(row - 1, col + 1):
                    moves.append(((row - 1, col + 1),None))
            # Check for possible captures
            que= Que()
            que.append(((row, col),[]))
            while(not que.is_empty()):
                cord, eaten = que.dequeue()
                start_row, start_col = cord      
                if (start_row - 2, start_col - 2) not in checkers and (start_row - 1, start_col - 1) in checkers and checkers[(start_row - 1, start_col - 1)].color != color:
                    if not Outside(start_row - 2, start_col - 2):
                        moves.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                        que.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                if (start_row - 2, start_col + 2) not in checkers and (start_row - 1, start_col + 1) in checkers and checkers[(start_row - 1, start_col + 1)].color != color:
                    if not Outside(start_row - 2, start_col + 2):
                        moves.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
                        que.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
                # Check if the move is diagonal and forward
        elif movment == "Dawn":
                # Check if the move is diagonal and forward
            if (row + 1, col - 1) not in checkers:
                if not Outside(row + 1, col - 1):
                    moves.append(((row + 1, col - 1),None))
            if (row + 1, col + 1) not in checkers:
                if not Outside(row + 1, col + 1):
                    moves.append(((row + 1, col + 1),None))
            # Check for possible captures
            que= Que()
            que.append(((row, col),[]))
            while(not que.is_empty()):
                cord, eaten = que.dequeue()
                start_row, start_col = cord
                if (start_row + 2, start_col - 2) not in checkers and (start_row + 1, start_col - 1) in checkers and checkers[(start_row + 1, start_col - 1)].color == BLUE:
                    if not Outside(start_row + 2, start_col - 2):
                        moves.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                        que.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                if (start_row + 2, start_col + 2) not in checkers and (start_row + 1, start_col + 1) in checkers and checkers[(start_row + 1, start_col + 1)].color == BLUE:
                    if not Outside(start_row + 2, start_col + 2):
                        moves.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
                        que.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
        elif movment == "KING":
            if (row - 1, col - 1) not in checkers:
                if not Outside(row - 1, col - 1):
                    moves.append(((row - 1, col - 1),None))
            if (row - 1, col + 1) not in checkers:
                if not Outside(row - 1, col + 1): 
                    moves.append(((row - 1, col + 1),None))
            if (row + 1, col - 1) not in checkers:
                if not Outside(row + 1, col - 1):
                    moves.append(((row + 1, col - 1),None))
            if (row + 1, col + 1) not in checkers:
                if not Outside(row + 1, col + 1):
                    moves.append(((row + 1, col + 1),None))
            
            # Check for possible captures
            been_to = {}
            que= Que()
            que.append(((row, col),[]))
            while(not que.is_empty()):
                cord, eaten = que.dequeue()
                start_row, start_col = cord                     
                been_to[(start_row, start_col)] = True
                if (start_row - 2, start_col - 2) not in checkers and (start_row - 1, start_col - 1) in checkers and checkers[(start_row - 1, start_col - 1)].color != color:
                    if not been_to.get((start_row - 2, start_col - 2)):
                        if not Outside(start_row - 2, start_col - 2):
                            moves.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                            que.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                if (start_row - 2, start_col + 2) not in checkers and (start_row - 1, start_col + 1) in checkers and checkers[(start_row - 1, start_col + 1)].color != color:
                    if not been_to.get((start_row - 2, start_col + 2)):
                        if not Outside(start_row - 2, start_col + 2):
                            moves.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
                            que.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
                if (start_row + 2, start_col - 2) not in checkers and (start_row + 1, start_col - 1) in checkers and checkers[(start_row + 1, start_col - 1)].color != color:
                    if not been_to.get((start_row + 2, start_col - 2)):
                        if not Outside(start_row + 2, start_col - 2):
                            moves.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                            que.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                if (start_row + 2, start_col + 2) not in checkers and (start_row + 1, start_col + 1) in checkers and checkers[(start_row + 1, start_col + 1)].color != color:
                    if not been_to.get((start_row + 2, start_col + 2)):    
                        if not Outside(start_row + 2, start_col + 2):
                            moves.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
                            que.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
    return moves

def game_ended(reds , blues,first):
    score = 0
    if reds == {}:
        score = 1000
    if blues == {}:
        score = 1000 
    
    if(not first):
        return score
    else:
        return -1 * score
    