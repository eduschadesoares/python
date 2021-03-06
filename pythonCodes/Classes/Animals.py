#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal:
    
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return "{} {}".format(self.name, self.genre)


class Dog(Animal):
    def __init__(self, name, genre, breed):
        self.breed = breed
        super().__init__(name, genre)

    def __str__(self):
        return super().__str__() + ", " + self.breed


class LittleDog(Dog):
    def __init__(self, name, genre, breed):
        super().__init__(name, genre, breed)
        self.size = "Puppy"

    def __str__(self):
        return super().__str__() + ", " + self.size


a = LittleDog("rodolfo", "masculino", "Vira-Lata")

print(a.size)
