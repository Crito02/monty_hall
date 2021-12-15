
import random

def main():   
    sims = 1000000
    doorNoThree = 0
    sameDoor = 0

    doors = ['one', 'two', 'three']

    for i in range(sims):
        winner = random.choice(doors)
        choose = random.choice(doors)
        
        #open a random door that isn't my choice or the winner
        opened = random.choice(doors)
        while (opened == winner) or (opened == choose):
            opened = random.choice(doors)

        if winner != choose:
            doorNoThree +=1

        elif winner == choose:
            sameDoor +=1

        else:
            print("Your code is broken ")

    print("Out of {0} simulations, your choice won: {1}, switching won: {2}".format(sims,sameDoor,doorNoThree))
    print("The odd on your door are: {0}%, the odds on door #3 are: {1}%".format(int((sameDoor/sims)*100), int((doorNoThree/sims)*100)))

if __name__ == "__main__":
    main()
