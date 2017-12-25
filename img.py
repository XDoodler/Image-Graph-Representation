import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


maze = mpimg.imread('../py/dog.png')


print("------------------------------")
x=0
y=10
rgb=0.0000
c=0

print(maze)

for row in maze:
   for row1 in row:
    for row2 in row1:
     rgb=rgb+row2 
    
    rgb=rgb/3
    if (rgb!=0.0000000):
          plt.plot(x,y,'ro')
          c+=1
    else:
          plt.plot(x,y,'bo')
          c+=1     
    print (rgb,c)
    x+=.5
    rgb=0.000
   
   y-=1; x=0; 


plt.axis([-5,200,-200,15])
plt.show()
   
   



     







