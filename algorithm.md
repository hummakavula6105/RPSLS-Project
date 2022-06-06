
# Outline

- write entry statement
- ask how many players / AI involvement
- show rules
- begin game statement
- input(user selection) * 3 (if chosen)
- AI selection
- creat loops for rounds
- declare winner


# Algorithm Steps & Such

- need parent class for players
- run the game, these need to be in it:
- entry statement
- game rules
- run the game
    - loops rounds (best out of 3)
    - prints round winner / tied rounds
- declare winner


# What the player(s) will see

- Welcome statement: Welcome to a sassy game of Rock, Paper, Scissors, Lizard, Spark! A virtual way to beat your opponents and have a chuckle!

- Will you be playing with the computer? Y/N:
    - If no, continues to ask how many human players (2 or 3)
 
- Players generate their user name. 
    - If computer is playing, player can name the computer.

- Rules: Here are the rules to the game, there are 3 rounds, best 2 out of 3. Here is the list of who beats who:
            1. Rock - crushes Scissors
            2. Paper - covers Rock
            3. Scissors - cuts Paper
            4. Lizard - poisons Spock
            5. Spock - smashes Scissors
            6. Scissors - decapitates Lizard
            7. Lizard - eats Paper
            Input the number for your selection when asked and watch as the game ensue! Good luck, and may the odds ever be in your favor!

            Which action do you wish to take against your opponent?:   

- Run game: 
    - Player *** has chosen ***!
    - Player/AI *** has chosen ***!

    - Player *** wins this round!
    - If players made the same choice, this round is a tie
        - With 3 players:
            - Whomever has the choice that beats out the other two opponents
                - Mini rounds played with 3 human players
                    - Player 0 vs 1 first, then player 1 vs 2
                    - This was done to keep the game moving faster rather than potential of X number of rounds
            - Declare winner of this round

    - 2 / 3 rounds played - best of 3 wins
        - If tie rounds encountered (except 3 players), statement prints "Tie, let's go again"
        - Loop back to another round, no points awarded for this round

    - Congratulation ***, you have outwitted your foes!

