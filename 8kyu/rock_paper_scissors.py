def rps(p1, p2):
    #your code here
    if p1 == p2:
        return "Draw!"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "Player 1 won!" if wins.get(p1) == p2 else "Player 2 won!"


rps('rock', 'scissors')
rps('scissors', 'rock')


#Other solutions
def rps(p1, p2):
    return "Draw!" if p1 == p2 else "Player 1 won!" if (p1, p2) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')] else "Player 2 won!"