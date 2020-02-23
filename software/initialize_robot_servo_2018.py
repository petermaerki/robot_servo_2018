

def initialize_serial1(s):
  s.addServo(9, 'Z', iMin_us= 1100, iMax_us=1600, fPositionMin=1.0, fPositionMax=0.0) # Zange, zu 0.0 offen 1.0
  s.addServo(8, 'K') # Kopf, links -1.0 rechts 1.0
  s.addServo(7, 'A')
  offset_B = 60
  s.addServo(6, 'B', iMin_us= 600+offset_B, iMax_us=2400+offset_B, fPositionMin=-1.0, fPositionMax=1.0)
  offset_C = 40
  s.addServo(5, 'C', iMin_us= 600+offset_C, iMax_us=2400+offset_C, fPositionMin=-1.0, fPositionMax=1.0)
  offset_D = 50
  s.addServo(4, 'D', iMin_us= 600+offset_D, iMax_us=2400+offset_D, fPositionMin=-1.0, fPositionMax=1.0)
  offset_E = 50
  s.addServo(3, 'E', iMin_us= 600+offset_E, iMax_us=2400+offset_E, fPositionMin=-1.0, fPositionMax=1.0)
  offset_F = 40
  s.addServo(2, 'F', iMin_us= 600+offset_F, iMax_us=2400+offset_F, fPositionMin=-1.0, fPositionMax=1.0)
  offset_G = 30
  s.addServo(1, 'G', iMin_us= 600+offset_G, iMax_us=2400+offset_G, fPositionMin=-1.0, fPositionMax=1.0)
  s.addServo(0, 'T', iMin_us= 600, iMax_us=2400, fPositionMin=1.0, fPositionMax=-1.0) # Tail 1: oben, 0 flach, -1 unten

