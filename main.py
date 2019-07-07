#!/usr/bin/python3

from utils import generate_word
from human import Human

import time
import random

def main():

        howManyHumans = 1000
        humans = []
        for i in range( howManyHumans ):
                name = generate_word( random.randint( 3, 8 ) )
                age =  random.randint( 1, 100 )
                money =  random.randint( 0, 10000000 )
                human = Human( name, age, money )
                humans.append( human )

        year = 0
        while( True ):
                print( "\nThis is year {}".format( year ) )
                year += 1
                time.sleep( 1 )

                for human in humans:
                        human.update()

                        if human.isAlive():
                                human.speak()
                                human.pay( humans[99], random.randint( 1, 1000000 ) )

main()
