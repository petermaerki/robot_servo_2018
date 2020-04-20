axes = 'BCDEFG'
for index in range(len(axes)-1):
    print(axes[index])
    print(axes[index+1])


def kopf_guemi(movetime_ms = 1000):
    s('T', 0.2, 100, move='S')
    s.move()
    s('K', -0.2, 100, move='S')
    s('A', -0.3, movetime_ms, move='S')
    s.move()

  def schwanz_guemi(movetime_ms = 1000):
    s('A', 0.2, 100, move='S')
    s.move()
    s('T', -0.2, movetime_ms, move='S')
    s.move()

  winkel = -0.25
  movetime_ms = 2000



  s('A', -0.5, 2000, move='S')  # Schwanz abe
  s.move()
  s('T', 0.2, movetime_ms, move='S')
  s.move()

  s.move(ms=1000) # etwas warten

  s('A', -0.1, 2000, move='S')
  s('B,C,D,E,F', winkel, movetime_ms, move='S') # buggeli
  s('G', -0.1, movetime_ms, move='S')
  s.move()

  # s('T', 0.2, 100, move='S')  # Schwanz ufe
  # s.move()
  # s('K', -0.2, 100, move='S') # Kopf abe
  # s('A', -0.3, movetime_ms, move='S')
  # s.move()
  s.move(ms=1000) # etwas warten
  s('T', -0.2, movetime_ms, move='S')
  s('B,C,D,E,F,G', 0, movetime_ms, move='S') # flach
  s.move()