#Determine the resultant of the coplanar parallel forces shown and locate it w.r.t to centre O of radius r
import math
r=float(input("ENTER THE RADIUS OF CIRCLE "))
print("EVERY VALUE OF FORCE ENTERED FOLLOWS THE BASIC SIGN CONVENTION THAT IS +VE SIGN IS +VE X AXIS AND -VE SIGN IS -VE Y AXIS SAME FOR FORCE ALONG Y DIRECTION")
print("EVERY VALUE OF THETA ENTERED +VE IS ABOVE THE X AXIS AND ENTERED -VE IS BELOW THE X AXIS ALL ANGLES ARE ACUTE")
f1=float(input("ENTER THE VALUE OF FIRST  FORCE "))
f2=float(input("ENTER THE VALUE OF SECOND FORCE "))
f3=float(input("ENTER THE VALUE OF THIRD FORCE "))
f4=float(input("ENTER THE VALUE OF FOURTH FORCE "))
t1=float(input("enter the angle at centre to the force 1 "))
t2=float(input("enter the angle at centre to the force 2 "))
t3=float(input("enter the angle at centre to the force 3 "))
t4=float(input("enter the angle at centre to the force 4 "))
#finding the resultant

fr= f1 + f2 + f3 + f4 

print("RESULTANT OF THE FORCES IS =",round(fr))

#finding the position using verignon's theorm
if f1>0:
  if t1>0:
    v1 = (-1)*f1*r*math.sin(t1)
  elif t1 == 0:
    v1 = 0  
  else:
    v1 = f1*r*math.sin(t1)
elif f1 == 0 :
  v1 = 0
else:
  if t1>0:
    v1 = f1*r*math.sin(t1)
  elif t1 == 0:
    v1 = 0  
  else:
    v1 = (-1)*f1*r*math.sin(t1)

if f2>0:
  if t2>0:
    v2 = (-1)*f2*r*math.sin(t2)
  elif t2 == 0:
    v2 = 0  
  else:
    v2 = f2*r*math.sin(t2)
elif f2 == 0 :
  v2 = 0
else:
  if t2>0:
    v2 = f2*r*math.sin(t2)
  elif t2 == 0:
    v2 = 0  
  else:
    v2 = (-1)*f2*r*math.sin(t2)

if f3>0:
  if t3>0:
    v3 = (-1)*f3*r*math.sin(t3)
  elif t3 == 0:
    v3 = 0  
  else:
    v3 = f3*r*math.sin(t3)
elif f3 == 0 :
  v3 = 0
else:
  if t3>0:
    v3 = f3*r*math.sin(t3)
  elif t3 == 0:
    v3 = 0  
  else:
    v3 = (-1)*f3*r*math.sin(t3)

if f4>0:
  if t4>0:
    v4 = (-1)*f4*r*math.sin(t4)
  elif t4 == 0:
    v4 = 0  
  else:
    v4 = f4*r*math.sin(t4)
elif f4 == 0 :
  v4 = 0
else:
  if t4>0:
    v4 = f4*r*math.sin(t4)
  elif t4 == 0:
    v4 = 0  
  else:
    v4 = (-1)*f4*r*math.sin(t4)
vr=v1 + v2 + v3 + v4
d=((vr/fr))/(-1)
if d > 0:
  print("POSITION OF THE RESULTANT WITH RESPECT TO CENTRE IS " + str(round(d)) + " ABOVE THE CENTRE")
else:
  print("POSITION OF THE RESULTANT WITH RESPECT TO CENTRE IS " + str(round(d)) + " BELOW THE CENTRE") 