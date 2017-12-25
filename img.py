import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


maze = mpimg.imread('../dog.png')


print("------------------------------")
x=0
y=10
rgb=0.0000
c=0
#print the the pixels of the image in ndarray
print(maze)
#iterate to plot image
for row in maze:
   for row1 in row:
    for row2 in row1:
     rgb=rgb+row2 
    
    rgb=rgb/3 #calculate the average RGB
    if (rgb!=0.0000000): #check the necessary RGB to distinguish points. Apply yours to perform the task
          plt.plot(x,y,'ro')
          c+=1
    else:
          plt.plot(x,y,'bo')
          c+=1     
    print (rgb,c)#print RGB and counter to keep track
    x+=.5
    rgb=0.000
   
   y-=1; x=0; 


plt.axis([-5,200,-200,15]) #ploting in graph
plt.show()
   
   



     







