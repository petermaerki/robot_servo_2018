import lib_servo

def run(s):
  # Examples:
  #   s('A,B', pos=1.0, duration=3000, move='L')
  #   s('A,B', 1.0, 3000, 'L')
  #   s('A,B', 0.1j)  # The increment is defined as a complex number
  #
  # Named parameters are: s(strNames, pos, duration=1000, move='S')
  #
  # pos or inc has to be defined
  # move is 'S' for Sinus, 'L' for Linear, 'I' for Instant
  # Default duration=1000
  # Default move='S'
  # s('A,B', -0.5, 100)
  # s.wait_ms(1000)
  # s('A', 0.4)
  # s('B', 0.5j)
  # s.wait_ms(2000)
  # s('A,B', 0.5, duration=300)
  # s.wait_ms(1500)

  # def knick(fWinkel):
  #   print('  knick %0.2f' % fWinkel)
  #   s('A', pos=fWinkel, duration=300)
  #   s('B', pos=fWinkel, duration=500, move='L')
  #   s.wait_ms(500)

  # knick(0.0)
  # knick(-0.5)
  # knick(-0.8)

  # def handorgel(winkel):
  #   s('B,D,F', winkel, 3000, move='S')
  #   s('C,E', -winkel, 3000, move='S')
  #   s('G', -winkel/2.0-winkel/3.0, 3000, move='S')
  #   s.wait_ms(3000)

  # handorgel(0.2)
  # s('T', 0.4, 500)
  # s.wait_ms(1000)
  # s('T', 0.6, 500)
  # s.wait_ms(1000)


def handorgel(winkel= 0.8): 
  s('A', 0.6, 1000, move='L')
  s('B,D,F', winkel, 3000, move='L')
  s('C,E', -winkel, 3000, move='L')
  s('G', -winkel/2.0-winkel/5.0, 3000, move='L')
  s.wait_ms(3000)

def bogen(winkel= -0.2): 
  s('B,C,D,E,F', winkel, 1000, move='L')
  s('A,G', 1, 1000, move='L')
  s.wait_ms(1000)

def bogenbogen(n=3): 
  s('A', 1, 1000, move='L')
  s('G', 1, 1000, move='L')
  for i in range(n):
    s('B,C,D,E,F', -0.1, 2000, move='L')
    s.wait_ms(2000)
    s('B,C,D,E,F', -0.2, 2000, move='L')
    s.wait_ms(2000)

def init_flach(): 
  pause = 300
  s('A', 0.5, pause, move='L')
  s.wait_ms(pause)
  s('B', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('C', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('D', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('E', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('F', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('G', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('T', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('K', 0.0, pause, move='L')
  s.wait_ms(pause)
  s('Z', 0.0, pause, move='L')
  s.wait_ms(pause)

def aufrichten(): 
  pause = 300
  s('A', 0.8, pause, move='L')
  s.wait_ms(pause)
  s('C', 0.7, pause, move='L')
  s.wait_ms(pause)
  s('A', 0.3, 2000, move='L')
  s('C', 0.0, 2000, move='L')
  s('D', 0.7, 2000, move='L')
  s.wait_ms(2000)
  s('D', 0.0, 2000, move='L')
  s('E', 0.7, 2000, move='L')
  s.wait_ms(2000)

  # s('E', winkel, pause, move='L')
  # s.wait_ms(pause)
  # s('F', winkel, pause, move='L')
  # s.wait_ms(pause)
  # s('G', winkel, pause, move='L')
  # s.wait_ms(pause)
  # s('T', winkel, pause, move='L')
  # s.wait_ms(pause)
  # s('K', winkel, pause, move='L')
  # s.wait_ms(pause)
  # s('Z', winkel, pause, move='L')
  # s.wait_ms(pause)

#handorgel(0.3)
#bogen(-0.3)
#bogenbogen()
init_flach()
aufrichten()