def print_hello():
	print("hello world")

import random
class Test:
  def __init__(self):
    self.score=0
  
  def addTest(self):
    a=random.randint(0, 10)
    b=random.randint(0, 10)
    c=a+b
    print(a, "+", b, "=", end="")
    ans=int(input())
    if ans==c:
      self.score=self.score+1
    
  def subTest(self):
    a=random.randint(0, 10)
    b=random.randint(0, 10)
    c=a-b 
    print(a, "-", b, "=", end="")
    ans=int(input())
    if ans==c:
      self.score=self.score+1

#score=0
test=Test()

while(True):
  print("-----")
  print("[1] addTest")
  print("[2] subTest")
  print("[q] exit")
  print("-----")
  m=input("select menu:")
  if m=="q":
    break
  elif m=="1":
    test.addTest()
  elif m=="2":
    test.subTest()
print("Your score is", test.score)

if __name__ == '__main__':
	print_hello()