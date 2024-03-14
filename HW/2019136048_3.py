class Time:
   
   def __init__ (self,h=0, m=0,s=0):
      self.h=h
      self.m=m
      self.s=s

   def set(self,h,m,s):
      self.h=h
      self.m=m
      self.s=s
 
   def hour(self) : return self.h
   
   def minute(self) : return self.m
   
   def second(self) : return self.s

   def isAM(self): return self.h <12

   def isSame(self,t):
      return self.h==t.h and self.m==t.m and self.s==t.s
   
   def difference(self, t2):
    diff_seconds = self.s - t2.s
    diff_minutes = self.m - t2.m
    diff_hours = self.h - t2.h

    if diff_seconds < 0:
        diff_seconds += 60
        diff_minutes -= 1
    if diff_minutes < 0:
        diff_minutes += 60
        diff_hours -= 1
    if diff_hours < 0:
        diff_hours += 12

    return Time(diff_hours, diff_minutes, diff_seconds)

       
  
   def trim(self):
        if self.s >= 60:
            self.m += self.s //60
            self.s %= 60
        if self.m >= 60:
            self.h +=self.m //60
            self.m %= 60
        if self.h >= 12:
            self.h -= 12

        if self.s < 0:
           self.s += 60
           self.m -= 1
        if self.m < 0:
           self.m += 60
           self.h -= 1
        if self.h < 0:
           self.h += 12
   

        
      
   def display(self):
      print("time:%02d:%02d:%02d"%(self.h,self.m,self.s))

t1 = Time(10, 61, 33)
t2 = Time(5, 30, 45)
result =t1.isSame(t2)

diff = t1.difference(t2)
t1.display()
t2.display()
t1.trim()
t1.display()
print(t1.isAM())
if result:
   print("True")
else: 
   print("False")
diff.display()


    
