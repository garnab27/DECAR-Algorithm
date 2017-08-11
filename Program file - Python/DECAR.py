#DECAR Algorithm implementation

import numpy as np
import matplotlib.pyplot as plt

#this function calculates distance b/w two points
def dist(x1,y1,x2,y2):
	return float(np.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))

#this function updates radius of coverage of the sensors
def updaterc(dsink,dmax,dmin,e,rc):
	return float((1-e*(dmax-dsink)/(dmax-dmin))*rc)

nodes=200 	#no. of nodes

e=0.8		#factor e

neighb=np.array([0 for x in range(0,nodes)])		#array to store no. of neighbours of a sensor i

neighb1=np.array([[0 for x in range(0,nodes)] for y in range(0,nodes)])		#array to store the neighbours of sensor i

res=np.array([np.random.rand()*100 for x in range(0,nodes)])		#array to store randomly generated residual energy

distance=np.array([[0.0 for x in range(0,nodes)] for y in range(0,nodes)])		#array to store distance b/w two nodes

nd=np.array([[np.random.rand()*1000 for x in range(0,2)] for y in range(0,nodes)])		#array to store position of sensor i

rang=100.0		#radius of coverage of the sensor 

cr=np.array([rang for x in range(0,nodes)])		#array to store updated radius of coverage

wht=np.array([0.0 for x in range(0,nodes)])		#array to store factor Weigth of sensors

isch=np.array([0 for x in range(0,nodes)])		#array to store whether is cluster head or not

ch=np.array([0 for x in range(0,nodes+1)])		#array to store cluster heads

dmax=0.0										#max distance between sensor and sink

dmin=500.0										#min distance between sensor and sink

#NOTE :: Sink(Base Station) is assumed to be present at the center i.e. (500.0,500.0)

for x in range(0,nodes):						#loop to calculate dmax and dmin
	d=dist(500.0,500.0,nd[x][0],nd[x][1])
	if dmax<d:
		dmax=d
	if dmin>d:
		dmin=d

#print(dmax+" "+dmin)
plt.plot(500.0,500.0,'o')						#plotting sink with a circle

plt.axis([0,1000,0,1000])

for x in range(0,nodes):						#loop to update radius of coverage and print the sensors
	cr[x]=updaterc(dist(500.0,500.0,nd[x][0],nd[x][1]),dmax,dmin,e,rang)
	plt.plot(nd[x][0],nd[x][1],'^')
	plt.axis([1,1000,1,1000])

for i in range(0,nodes):						#loop to calculate distance between the nodes
	for j in range(0,nodes):
		distance[i][j]=dist(nd[i][0],nd[i][1],nd[j][0],nd[j][1])

for i in range(0,nodes):						#loop to calculate neighbours and their quantity
	for j in range(0,nodes):
		if distance[i][j]<=cr[i]:
			neighb[i]=neighb[i]+1
			neighb1[i][j]=1

for i in range(0,nodes):						#loop to calculate factor Weigth
	wht[i]=(res[i]*res[i])/neighb[i]
#print(wht)

p=0

for i in range(0,nodes):						#loop to calculate cluster heads
	flag=1
	for j in range(0,nodes):
		if neighb1[i][j]==1 and flag==1:
			if wht[j]>wht[i] and i!=j:
				flag=0
				break
	#print(flag)
	if flag==1:
		isch[i]=1
		ch[p]=i
		p=p+1

color=np.random.rand()							#color decides the color of area of the cluster head

for x in range(0,p):							#loop to print the cluster heads and their area of coverage
	a=np.pi*(cr[ch[x]])**1.8
	plt.scatter(nd[ch[x]][0],nd[ch[x]][1],s=a,c=color,alpha=0.5)
	plt.axis([0,1000,0,1000])
	
for x in range(0,p):							#loop to print the radius of the cluster heads
	print(cr[ch[x]])

plt.show()
