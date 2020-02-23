import lib_servo

import initialize_robot_servo_2018

def initialize(s):
  initialize_robot_servo_2018.initialize_serial1(s)

def run(s):
  def handorgel(winkel= 0.8): 
    s('A', 0.6, 1000, move='L')
    s('B,D,F', winkel, 3000, move='L')
    s('C,E', -winkel, 3000, move='L')
    s('G', -winkel/2.0-winkel/5.0, 3000, move='L')
    s.move()

  def bogen(winkel= -0.2): 
    s('B,C,D,E,F', winkel, 1000, move='L')
    s('A,G', 1, 1000, move='L')
    s.move()

  def bogenbogen(n=3): 
    s('A', 1, 1000, move='L')
    s('G', 1, 1000, move='L')
    for i in range(n):
      s('B,C,D,E,F', -0.1, 2000, move='L')
      s.move()
      s('B,C,D,E,F', -0.2, 2000, move='L')
      s.move()

  def init_flach(): 
    pause = 300
    s('A', 0.5, pause, move='L')
    s.move()
    s('B', 0.0, pause, move='L')
    s.move()
    s('C', 0.0, pause, move='L')
    s.move()
    s('D', 0.0, pause, move='L')
    s.move()
    s('E', 0.0, pause, move='L')
    s.move()
    s('F', 0.0, pause, move='L')
    s.move()
    s('G', 0.0, pause, move='L')
    s.move()
    s('T', 0.0, pause, move='L')
    s.move()
    s('K', 0.0, pause, move='L')
    s.move()
    s('Z', 0.0, pause, move='L')
    s.move()

  def aufrichten(): 
    pause = 300
    s('A', 0.8, pause, move='L')
    s.move()
    s('C', 0.7, pause, move='L')
    s.move()
    s('A', 0.3, 2000, move='L')
    s('C', 0.0, 2000, move='L')
    s('D', 0.7, 2000, move='L')
    s.move()
    s('D', 0.0, 2000, move='L')
    s('E', 0.7, 2000, move='L')
    s.move()

    # s('E', winkel, pause, move='L')
    # s.move()
    # s('F', winkel, pause, move='L')
    # s.move()
    # s('G', winkel, pause, move='L')
    # s.move()
    # s('T', winkel, pause, move='L')
    # s.move()
    # s('K', winkel, pause, move='L')
    # s.move()
    # s('Z', winkel, pause, move='L')
    # s.move()

  #handorgel(0.3)
  #bogen(-0.3)
  #bogenbogen()

  init_flach()
  aufrichten()

if __name__ == '__main__':
  s = lib_servo.Servos()
  initialize(s)
  run(s)
