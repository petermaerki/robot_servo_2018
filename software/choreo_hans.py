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
  s('C', -0.5, 5000)
  s('A,B', -0.5, 100)
  s.move(waitforservos='A,B')
  s('A', 0.4)
  s('B', 0.5j)
  s.move(ms=2000)
  s('A,B', 0.5, duration=300)
  s.move(waitforservos='A,B')

  def knick(fWinkel):
    print('  knick %0.2f' % fWinkel)
    s('A', pos=fWinkel, duration=300)
    s('B', pos=fWinkel, duration=500, move='L')
    s.move(ms=500)

  knick(0.0)
  knick(-0.5)
  knick(-0.8)
  s.move()

def initialize(s):
  s.addServo(7, 'A')
  s.addServo(8, 'B')
  s.addServo(9, 'C')

if __name__ == '__main__':
  s = lib_servo.Servos()
  initialize(s)
  run(s)
