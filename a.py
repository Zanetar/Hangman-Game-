from random import *
import random
class Game:
    def __int__(self,name,level):
        self.name=name
        self.level=level

class Hangman(Game):
    def __int__(self, name,level):
        super().__init__(name,level)

    def __repr__(self):
        return('Gra polega na odgadnięciu ukrytego wyrazu.')

    def print_1(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_2(self):
        print('------')
        print('|   |')
        print('|   0')
        print('|---+---')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_3(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_4(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|   |')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_5(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|   |')
        print('|  |')
        print('|  |')
        print('|')
        print('----------')

    def print_6(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|   |')
        print('|  | |')
        print('|  | |')
        print('|')
        print('----------')

    def rules(self):
        print('Witaj w grze Wisielec')
        self.print_6()
        print('Twoim zadaniem jest odgadnięcie hasła, ukrytego przez komputer.')
        print('Wpisuj propozycję liter, które twoim zdaniem występują w ukrytym wyrazie')
        print('W przypadku, kiedy podasz błędną literę, komputer dorysuje kolejne części szubienicy')
        print('Gdy komputer skończy swój rysunek- przegrywasz')
        print('Masz tylko 6 żyć!')

    def difficulty_level(self):
        print('Wybierz poziom trudności')
        print('1-łatwy')
        print('2-średni')
        print('3-zaawansowany')
        level = int(input())
        return level

    def words(self,document):
        with open(document) as file:
            file = file.readlines()
            file = [i.rstrip('\n') for i in file]
            word = random.choice(file)
            return word

    def exit(self):
        self.print_6()
        exit = int(input('Czy chcesz zagrać w grę? 1-T,0-N'))
        return exit

    def game(self,word):
        wrong_anwsers = 6
        word = list(word)
        letters = list(word)
        print('TWOJE HASŁO')
        print(len(letters) * ' _ ')
        for i in range(len(letters)):
            letters[i] = '_'
        used_letters = []
        while True:
            proposed_letter = str(input('Wpisz swoją propozycję litery'))

            if proposed_letter in word:
                for i in range(len(word)):
                    if word[i] == proposed_letter:
                        letters[i] = proposed_letter
                        print(f'dobrze!{letters}')
                if letters == word:
                    a = (' '.join(word))
                    print(f'Wygrałeś grę.Szukane słowo to:   {a} .   GRATULACJE!')
                    break

            else:
                used_letters.append(1)
                print('Źle!')
                print(f'Wykorzystałeś już {sum(used_letters)}. Pozostało Ci{wrong_anwsers - sum(used_letters)}')
                print(letters)
                if sum(used_letters) == 1:
                   self.print_1()
                elif sum(used_letters) == 2:
                    self.print_2()
                elif sum(used_letters) == 3:
                    self.print_3()
                elif sum(used_letters) == 4:
                    self.print_4()
                elif sum(used_letters) == 5:
                    self.print_5()
                elif sum(used_letters) == 6:
                    self.print_6()
                    print(f'Przegrałeś grę! Szukane słowo to:     {word}')
                    break

    def exit(self):
        print('Dziękujemy za grę.')
        exit = int(input('Czy chcesz zagrać jeszcze raz? 1=T/0=N'))
        return exit

def menu_hang(object):
    try:
        while True:
            object.rules()
            difficult = object.difficulty_level()
            if difficult == 1:
                word = object.words('words.txt')
                object.game(word)
            elif difficult == 2:
                word = object.words('words2.txt')
                object.game(word)
            elif difficult == 3:
                word = object.words('words3.txt')
                object.game(word)
            x = object.exit()
            if x == 0:
                break
            elif x == 1:
                pass
            else:
                print('Podałeś zły znak. Uruchom grę ponownie')
                break
    except: print('Wybrano zły znak!')

third_game=Hangman()
menu_hang(third_game) #wywołanie programu