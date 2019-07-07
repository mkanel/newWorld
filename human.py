#!/usr/bin/python3

import random

class Human( object ):

        def __init__( self, name, age, money ):
                self.name = name
                self.age = age
                self.money = money
                self.isDead = False
                #print( "[{:10s}]:\tI was born!".format( self.name ) )

        def __del__( self ):
                #print( "[{:10s}]:\tI died!".format( self.name ) )
                pass

        def update( self ):
                if self.money < 0:
                        self.die()
                        #print( "[{:10s}]: I am poor!".format( self.name ) )
                        #if self.isAlive():
                        #        self.speak()
                        #        self.pay( random.randint( 1, 1000000 ) )

        #-----------------------------------------------------------------------

        def speak( self ):
                print( "[{:10s}]:\tI am {:3} years old and have {:8} money!".format( self.name, self.age, self.money ) )

        def pay( self, human, money ):
                self.money -= money
                human.money += money

        def die( self ):
                self.isDead = True

        def isAlive( self ):
                return not self.isDead
