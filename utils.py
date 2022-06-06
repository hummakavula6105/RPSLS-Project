def validate_int_input(prompt):
    try:
        choice = int(input(prompt))
        if choice < 6 and choice > 0:
            return choice
        else:
            choice = validate_int_input(prompt + ' You must choose a number between 1 and 5! ')
            return choice
    except:
        validate_int_input(prompt)
        

def check_results(players, ai_player):
    rock_wins = ['Scissors', 'Lizard']
    rock_loses = ['Paper', 'Spock']
    paper_wins = ['Rock', 'Spock']
    paper_loses = ['Scissors', 'Lizard']
    scissors_wins = ['Paper', 'Lizard']
    scissors_loses = ['Rock', 'Spock']
    lizard_wins = ['Spock', 'Paper']
    lizard_loses = ['Rock', 'Scissors']
    spock_wins = ['Scissors', 'Rock']
    spock_loses = ['Paper', 'Lizard']
    
    round_winner = ''
    
    while round_winner == '':
        if not ai_player and len(players) < 4:  
            if players[1].choice == 'Rock':
                if players[2].choice in rock_wins: round_winner = players[1].name
                if players[2].choice in rock_loses: round_winner = players[2].name
            if players[1].choice == 'Paper':
                if players[2].choice in paper_wins: round_winner = players[1].name
                if players[2].choice in paper_loses: round_winner = players[2].name
            if players[1].choice == 'Scissors':
                if players[2].choice in scissors_wins: round_winner = players[1].name
                if players[2].choice in scissors_loses: round_winner = players[2].name
            if players[1].choice == 'Lizard':
                if players[2].choice in lizard_wins: round_winner = players[1].name
                if players[2].choice in lizard_loses: round_winner = players[2].name
            if players[1].choice == 'Spock':
                if players[2].choice in spock_wins: round_winner = players[1].name
                if players[2].choice in spock_loses: round_winner = players[2].name      
            if round_winner == '': 
                return 'Tie'
            else:
                return round_winner

        if players[0].choice == 'Rock':               
            if players[1].choice in rock_wins: round_winner = players[0].name
            if players[1].choice in rock_loses: round_winner = players[1].name
        if players[0].choice == 'Paper':
            if players[1].choice in paper_wins: round_winner = players[0].name
            if players[1].choice in paper_loses: round_winner = players[1].name
        if players[0].choice == 'Scissors':
            if players[1].choice in scissors_wins: round_winner = players[0].name
            if players[1].choice in scissors_loses: round_winner = players[1].name
        if players[0].choice == 'Lizard':
            if players[1].choice in lizard_wins: round_winner = players[0].name
            if players[1].choice in lizard_loses: round_winner = players[1].name
        if players[0].choice == 'Spock':
            if players[1].choice in spock_wins: round_winner = players[0].name
            if players[1].choice in spock_loses: round_winner = players[1].name       
        if round_winner == '': round_winner = 'Tie' 
            
        if len(players) < 3:
            return round_winner
        #else:
        elif ai_player:
            if round_winner == 'Tie':
                if players[0].choice == 'Rock':               
                    if players[2].choice in rock_wins: round_winner = 'Tie'
                    if players[2].choice in rock_loses: round_winner = players[2].name
                if players[0].choice == 'Paper':
                    if players[2].choice in paper_wins: round_winner = 'Tie'
                    if players[2].choice in paper_loses: round_winner = players[2].name
                if players[0].choice == 'Scissors':
                    if players[2].choice in scissors_wins: round_winner = 'Tie'
                    if players[2].choice in scissors_loses: round_winner = players[2].name
                if players[0].choice == 'Lizard':
                    if players[2].choice in lizard_wins: round_winner = 'Tie'
                    if players[2].choice in lizard_loses: round_winner = players[2].name
                if players[0].choice == 'Spock':
                    if players[2].choice in spock_wins: round_winner = 'Tie'
                    if players[2].choice in spock_loses: round_winner = players[2].name       
            else:
                index = 0 if round_winner == players[0].name else 1
                if players[index].choice == 'Rock':               
                    if players[2].choice in rock_wins: 
                        round_winner = players[index].name
                    elif players[2].choice in rock_loses: 
                        round_winner = players[2].name
                    else: 
                        round_winner = 'Tie'
                if players[index].choice == 'Paper':    
                    if players[2].choice in paper_wins: 
                        round_winner = players[index].name
                    elif players[2].choice in paper_loses: 
                        round_winner = players[2].name
                    else: 
                        round_winner = 'Tie'
                if players[index].choice == 'Scissors':        
                    if players[2].choice in scissors_wins: 
                        round_winner = players[index].name
                    elif players[2].choice in scissors_loses: 
                        round_winner = players[2].name
                    else: 
                        round_winner = 'Tie'     
                if players[index].choice == 'Lizard':
                    if players[2].choice in lizard_wins: 
                        round_winner = players[index].name
                    elif players[2].choice in lizard_loses: 
                        round_winner = players[2].name
                    else: 
                        round_winner = 'Tie' 
                if players[index].choice == 'Spock':
                    if players[2].choice in spock_wins: 
                        round_winner = players[index].name
                    elif players[2].choice in spock_loses: 
                        round_winner = players[2].name
                    else: 
                        round_winner = 'Tie' 
        else:
            if round_winner == 'Tie':
                if players[1].choice == 'Rock':               
                    if players[3].choice in rock_wins: round_winner = 'Tie'
                    if players[3].choice in rock_loses: round_winner = players[3].name
                if players[1].choice == 'Paper':
                    if players[3].choice in paper_wins: round_winner = 'Tie'
                    if players[3].choice in paper_loses: round_winner = players[3].name
                if players[1].choice == 'Scissors':
                    if players[3].choice in scissors_wins: round_winner = 'Tie'
                    if players[3].choice in scissors_loses: round_winner = players[3].name
                if players[1].choice == 'Lizard':
                    if players[3].choice in lizard_wins: round_winner = 'Tie'
                    if players[3].choice in lizard_loses: round_winner = players[3].name
                if players[1].choice == 'Spock':
                    if players[3].choice in spock_wins: round_winner = 'Tie'
                    if players[3].choice in spock_loses: round_winner = players[3].name       
            else:
                index = 1 if round_winner == players[1].name else 2
                if players[index].choice == 'Rock':               
                    if players[3].choice in rock_wins: 
                        round_winner = players[index].name
                    elif players[3].choice in rock_loses: 
                        round_winner = players[3].name
                    else: 
                        round_winner = 'Tie'
                if players[index].choice == 'Paper':    
                    if players[3].choice in paper_wins: 
                        round_winner = players[index].name
                    elif players[3].choice in paper_loses: 
                        round_winner = players[3].name
                    else: 
                        round_winner = 'Tie'
                if players[index].choice == 'Scissors':        
                    if players[3].choice in scissors_wins: 
                        round_winner = players[index].name
                    elif players[3].choice in scissors_loses: 
                        round_winner = players[3].name
                    else: 
                        round_winner = 'Tie'     
                if players[index].choice == 'Lizard':
                    if players[3].choice in lizard_wins: 
                        round_winner = players[index].name
                    elif players[3].choice in lizard_loses: 
                        round_winner = players[3].name
                    else: 
                        round_winner = 'Tie' 
                if players[index].choice == 'Spock':
                    if players[3].choice in spock_wins: 
                        round_winner = players[index].name
                    elif players[3].choice in spock_loses: 
                        round_winner = players[3].name
                    else: 
                        round_winner = 'Tie' 
            
        return round_winner