import serial, sys

class ardser():
  def open_s(self,port,bps):
    ser=serial.Serial(port,bps)
    print("connected to: " + ser.portstr)
    return(ser)
  def read_s(self,ser):
    num=range(0,10)
    line=ser.readline()
    nums=line.split()
    print(nums)
    if len(nums)!=11:
      num=[]
      num.insert(0,nums[0].strip().decode('utf-8'))
    return(num)
  def close_s(self,ser):
    ser.close()
    return
  
  
# how to use
ard=ardser()
ser=ard.open_s(sys.argv[1],sys.argv[2])  # port name, bps
while True:
  try:
    num=ard.read_s(ser)
    print(num)
  except KeyboardInterrupt:
    print("exiting")
    break
ard.close_s(ser)
