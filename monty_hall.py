"""
Monty Carlo process with Monty Hall theory

Functions: main()
"""
import random
import time

def main():
    """
    Docsting for the sake of docstring
    """
    sims = 1000000
    door_no_three = 0
    same_door = 0

    doors = ['one', 'two', 'three']
    start_time = time.time()
    for i in range(sims):
        winner = random.choice(doors)
        choose = random.choice(doors)

        #open a random door that isn't my choice or the winner
        opened = random.choice(doors)
        while (opened == winner) or (opened == choose):
            opened = random.choice(doors)

        if winner != choose:
            door_no_three += 1

        elif winner == choose:
            same_door += 1

        else:
            print("Your code is broken ")

    print("For loop took: ", time.time()-start_time)
    print("Out of {0} simulations, your choice won: {1}, switching won: {2}".format(
        sims, same_door, door_no_three))
    print("The odd on your door are: {0}%, the odds on door #3 are: {1}%".format(
        int((same_door/sims)*100), int((door_no_three/sims)*100)))

if __name__ == "__main__":
    main()
