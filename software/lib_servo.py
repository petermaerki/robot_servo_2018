# https://github.com/adafruit/micropython-adafruit-pca9685/blob/master/pca9685.py
# https://micropython-pca9685.readthedocs.io/en/latest/
# https://www.adafruit.com/product/815
# https://cdn-learn.adafruit.com/downloads/pdf/16-channel-pwm-servo-driver.pdf 
import math
import utime
import time
import ustruct
import machine

from pyb import I2C

class PCA9685:
  def __init__(self, i2c= I2C(2) , address=0x40):
    self.i2c = i2c
    #print(self.i2c)
    self.address = address
    self.reset()

  def _write(self, address, value):
    self.i2c.writeto_mem(self.address, address, bytearray([value]))

  def _read(self, address):
    return self.i2c.readfrom_mem(self.address, address, 1)[0]

  def setTimeOn_us(self, iI2cIndex, fTimeOn_us):
    iTime = int(fTimeOn_us * 4096 * self.__freq / 1000000)
    self.pwm(iI2cIndex, on=0, off=iTime)

  def reset(self):
    self._write(0x00, 0x00) # Mode1

  def freq(self, freq=None):
    if freq is None:
      return int(25000000.0 / 4096 / (self._read(0xfe) - 0.5))
    self.__freq = freq
    prescale = int(25000000.0 / 4096.0 / freq + 0.5)
    old_mode = self._read(0x00) # Mode 1
    self._write(0x00, (old_mode & 0x7F) | 0x10) # Mode 1, sleep
    self._write(0xfe, prescale) # Prescale
    self._write(0x00, old_mode) # Mode 1
    time.sleep_us(5)
    self._write(0x00, old_mode | 0xa1) # Mode 1, autoincrement on

  def pwm(self, index, on=None, off=None):
    if on is None or off is None:
      data = self.i2c.readfrom_mem(self.address, 0x06 + 4 * index, 4)
      return ustruct.unpack('<HH', data)
    data = ustruct.pack('<HH', on, off)
    self.i2c.writeto_mem(self.address, 0x06 + 4 * index,  data)

class Servo:
  def __init__(self, pca9685, iI2cIndex, strName, iMin_us=600, iMax_us=2400, fPositionMin=-1.0, fPositionMax=1.0):
    self.__pca9685 = pca9685
    self.__iI2cIndex = iI2cIndex
    self.__strName = strName
    self.__iMin_us = iMin_us
    self.__iMax_us = iMax_us
    self.__fPositionMin = fPositionMin
    self.__fPositionMax = fPositionMax
    self.__objMove = None
    self.__fPosition = 0.0

  @property
  def strName(self):
    return self.__strName

  def setPosition(self, fPosition):
    fTime_us = self.__iMin_us + (fPosition - self.__fPositionMin) * (self.__iMax_us - self.__iMin_us) / (self.__fPositionMax - self.__fPositionMin) 
    fTime_us = min(fTime_us, self.__iMax_us)
    fTime_us = max(fTime_us, self.__iMin_us)
    self.__pca9685.setTimeOn_us(self.__iI2cIndex, fTime_us)

  def setMove(self, iTimeNowFromStart_ms, objMove):
    objMove.setStartPosition(self.__fPosition)
    self.__objMove = objMove
    print('  %5dms %-8s: %4.1f -> %4.1f %dms' % (iTimeNowFromStart_ms, self.__strName, objMove._fStartPos, objMove._fEndPos, objMove._iTimeDuration_ms))

  def updateMove(self, iTimeNow_ms):
    if self.__objMove == None:
      return
    self.__fPosition = self.__objMove.getPosition(iTimeNow_ms)
    self.setPosition(self.__fPosition)

class Servos:
  def __init__(self):
    self.__objI2c = machine.I2C(2) # Peter von 1 auf 2 geaendert
    self.__objPca9685 = PCA9685(self.__objI2c)
    self.__objPca9685.freq(50.0)
    self.__dictServos = {}
    self.resetTime()

  def resetTime(self):
    self.__iTimeStart_ms = utime.ticks_ms()
    self.__iTimeNow_ms = self.__iTimeStart_ms

  def __addServo(self, objServo):
    self.__dictServos[objServo.strName] = objServo

  def addServo(self, iI2cIndex, strName, iMin_us=600, iMax_us=2400, fPositionMin=-1.0, fPositionMax=1.0):
    objServo = Servo(self.__objPca9685, iI2cIndex, strName, iMin_us, iMax_us, fPositionMin, fPositionMax)
    self.__addServo(objServo)

  def setPosition(self, strName, fPosition):
    objServo = self.__dictServos[strName]
    objServo.setPosition(fPosition)

  def wait_ms(self, iTimeToWait_ms):
    print('  wait_ms %dms' % iTimeToWait_ms)
    self.__iTimeNow_ms = self.__iTimeNow_ms + iTimeToWait_ms
    while True:
      iTimeNow_ms = utime.ticks_ms()
      self.updateMove(iTimeNow_ms)
      if iTimeNow_ms > self.__iTimeNow_ms:
        return
      utime.sleep_ms(10)

  def __call__(self, strNames, pos, duration=1000, move='S'):
    '''
      strNames: 'A,B'

      s('A,B', pos=1.0, duration=3000, move='L')
      s('A,B', inc=0.2j, duration=3000, move='L')

      if pos is imag, then it is an increment.
    '''
    iTimeNowFromStart_ms = self.__iTimeNow_ms - self.__iTimeStart_ms
    listNames = strNames.split(',')
    for strName in listNames:
      objMove = Move(iTimeStart_ms=self.__iTimeNow_ms, iTimeDuration_ms=duration, fEndPos=pos, strMoveType=move)
      self.setMove(iTimeNowFromStart_ms, strName, objMove)

  def setMove(self, iTimeNow_ms, strName, objMove):
    '''
      strName: 'A'
    '''
    objServo = self.__dictServos[strName]
    objServo.setMove(iTimeNow_ms, objMove)

  def updateMove(self, iTimeNow_ms):
    for objServo in self.__dictServos.values():
      objServo.updateMove(iTimeNow_ms)

  def getNamen(self):
    listNamen = list(self.__dictServos.keys())
    listNamen.sort()
    return ', '.join(listNamen)

class Move:
  def __init__(self, iTimeStart_ms, iTimeDuration_ms, fEndPos, strMoveType):
    self._fStartPos = None
    self._iTimeStart_ms = iTimeStart_ms
    self._iTimeDuration_ms = iTimeDuration_ms
    self._fEndPos = fEndPos
    self._strMoveType = strMoveType

  def setStartPosition(self, fStartPos):
    assert fStartPos != None
    self._fStartPos = fStartPos
    if type(self._fEndPos).__name__ == 'complex':
      # _fEndPos is a complex number and therefore is the increment
      self._fEndPos = fStartPos + self._fEndPos.imag

  def getPosition(self, iTimeNow_ms):
    assert self._fStartPos != None, 'setStartPosition() wurde nicht aufgerufen!'
    iTime_ms = utime.ticks_diff(iTimeNow_ms, self._iTimeStart_ms)
    fAnteil = iTime_ms/self._iTimeDuration_ms
    if fAnteil > 1.0:
      fAnteil = 1.0
    return self.getPositionAnteil(fAnteil)

  def getPositionAnteil(self, fAnteil):
    if self._strMoveType == 'S':
      fPosition = ((math.sin(math.pi*(fAnteil+0.5))-1.0)/-2.0)*(self._fEndPos - self._fStartPos) + self._fStartPos
      return fPosition
    if self._strMoveType == 'L':
      fPosition = fAnteil*(self._fEndPos - self._fStartPos) + self._fStartPos
      return fPosition
    if self._strMoveType == 'I':
      fPosition = 1.0
      return fPosition
    assert False, 'Expected "S", "L" or "I"!'