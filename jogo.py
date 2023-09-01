import random
import os
from time import sleep

def GetLine(position):
   global pa, pb, pc
   position *= 2

   # below, we have a sequence of "magic numbers" which, in reality, in a rather obscure way,
   # form the vertical, horizontal and diagonal lines of the board. For example:
   # 591, 132, 258, and so on...
   # I could do it another way, but my aim with this is to pay homage to 'THE GUY' who created
   # the little program for the CP-200 / TK-85 and whose name is unfortunately not disclosed

   # NOTE: the numbers have been subtracted by 1 to match the positions of the string which
   # in PYTHON starts at 0
   #z = '59132587963756471'
   z =  '48021476852645360' 

   pa = int(z[position + 0])
   pb = int(z[position + 1])
   pc = int(z[position + 2])
   return board[pa] + board[pb] + board[pc]


def pc_play():

   for x in (2, 18):
      for n in range(8):
         if GetLine(n) == x:
            if   board[pa] == empty: pos = pa
            elif board[pb] == empty: pos = pb
            else:                    pos = pc
            
            board[pos] = 1
            print('%s%s%i%s' % (BLUE, 'Pc position: ', (pos+1), RST))
            sleep(2)
            return

   while True:
      pos = random.randint(0, 8)
      if board[pos] == empty:
         board[pos] = 1
         break

   print('%s%s%i%s' % (BLUE, 'Pc position: ', (pos+1), RST))
   sleep(2)
   return


def user_play():
   while True:
      x = input('%s%s%s' % (GREEN, 'User position: ', RST))

      if x in ('q', 'Q', '0'):
         print('Aborted game...')
         exit(0)

      try:
         pos = int(x) - 1
         
         if board[pos] != empty:
            print('Position already held')

         else :
            board[pos] = 9
            break
      except:
         pass


def display():
   global draw, micro, user
   os.system('cls')
   mk = []
   for i, v in enumerate(board):
      if   v == 0: mk.append('%s%s%s' % (YELLOW, str(i+1), RST))
      elif v == 1: mk.append('%s%s%s' % (BLUE  , 'O'     , RST))
      else:        mk.append('%s%s%s' % (GREEN , 'X'     , RST))

   print('%s%s%i%s' % (WHITE, 'Draw  = ', draw, RST))
   print('%s%s%i%s' % (BLUE , 'IA   = ', micro , RST))
   print('%s%s%i%s' % (GREEN, 'User = ', user  , RST))
   print()
   print(' %s | %s | %s' % tuple(mk[6:9]))
   print('---+---+---')
   print(' %s | %s | %s' % tuple(mk[3:6]))
   print('---+---+---')
   print(' %s | %s | %s' % tuple(mk[0:3]))
   print()


def verif():
   global draw, micro, user

   for n in range(8):
      if   GetLine(n) == 3:
          print('%s%s%s' % (BLUE, 'The Computer Wins', RST))
          micro += 1
          sleep(2)
          return True

      elif GetLine(n) == 27:
          print('%s%s%s' % (GREEN, 'The User Wins', RST))
          user += 1
          sleep(2)
          return True

   if not empty in board:
      print('Tied...')
      draw += 1
      sleep(2)
      return True

   return False


if __name__ == '__main__':

   # Defines variables used to display colors in the terminal
   RST     = '\033[00m'
   GRAY    = '\033[30m'
   RED     = '\033[31m'
   GREEN   = '\033[32m'
   YELLOW  = '\033[33m'
   BLUE    = '\033[34m'
   VIOLET  = '\033[35m'
   VERDAO  = '\033[36m'
   WHITE   = '\033[37m'

   draw = 0
   micro  = 0
   user   = 0
   empty  = 0

   while True:

      board = [empty] * 9

      Flag = random.choice([True, False])

      display()

      while True:

         Flag = not Flag

         if Flag: pc_play()

         else:    user_play()

         display()

         if verif(): break

      display()
      key = input('Want to play again? (Y/N)')

      if key not in ('Y', 'y'):
         break

   print('\nGame over')