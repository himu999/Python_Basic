p1 = input("Rock paper or scissors? : ")
p2 = input("Rock paper or scissors? : ")


def game(a, b):
    if a == b:
        return "It's a tie!"
    elif a == 'rock':
        if b == 'scissors':
            return "Rock beats scissors!"
        else:
            return "Paper beats rock"
    elif a == "scissors":
        if b == 'paper':
            return "Scissors beats paper!"
        else:
            return "Rock beats scissors"

    elif a == "paper":
        if b == 'rock':
            return 'Paper beats rock!'
        else:
            return "Scissors beat paper!"

    else:
        return "You have not entered rock, paper or scissors. "


aa = game(p1, p2)
print(aa)
