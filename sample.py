from random import sample
all_games = []

def get_num_games():
    while True:
        try:
            games = int(input('how many games do you want for the Mega-Sena lottery: ').strip())
            if games <= 0:
                print('enter a valid option')
                continue
            else:
                return games
        except ValueError:
            print('enter a valid number')

def get_game(games):
    for g in range(games):
        num_game = sorted(sample(range(1 , 61), 6))
        all_games.append(num_game)
        
#start program

games = get_num_games()
get_game(games)
    
for g in all_games:
    print(f'game: {g}')