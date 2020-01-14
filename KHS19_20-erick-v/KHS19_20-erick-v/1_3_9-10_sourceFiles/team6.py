####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '><><>Eric>><' # Only 10 chars displayed.
strategy_name = 'on off on off'
strategy_description = 'it decides based on what the last move of the opponent was, then uses history at the third round onward.'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    else:
        return 'c'
    if their_history=='ccc':
        return 'b'
    else:
        return 'c'
    if my_score < their_score:
        return 'b'
    else:
        return 'c'