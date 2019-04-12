
st_p=input()
end_p=input()
fstops=open("stops.txt","r")
s_id=[]
l=fstops.readlines()
def searchstop_id(l,s_id):
    #k=0
    flg=0
    flg1=0
    for i in range(len(l)):
        #k=k+1
        a=l[i].split(',')
        if(a[2]==st_p):
            st_id=a[0]
            flg=1
        if(a[2]==end_p):
            end_id=a[0]
            flg1=1
        if(flg==1 and flg1==1):
            break
    s_id.append(st_id)
    s_id.append(end_id)
searchstop_id(l,s_id)
#print(s_id)
fstops.close()



ftrips=open("trips.txt","r")
l2=ftrips.readlines()
start=[0]*543
end=[0]*543
p=-1
for i in range(1,len(l2)):
    b=l2[i].split(',')
    r_id=int(b[0])
    if(r_id==p):
        continue
    else:
        start[r_id]=int(b[2])
        end[p]=int(b[2])-1
    p=r_id
end[542]=16561
ftrips.close()


def findroute(trip):
    for i in range(543):
        if(trip>=start[i] and trip<=end[i]):
            return i


fstop_times=open("stop_times.txt","r")
l1=fstop_times.readlines()
zhop=[]
ohop=[]
for i in range(1,len(l1)):
    a=l1[i].split(',')
    if(a[3]==s_id[0]):
        temp=a[0]
        a0=l1[i-1].split(',')
        a1=l1[i-2].split(',')
        a00=l1[i+1].split(',')
        a11=l1[i+2].split(',')
        if(a0[0]==temp):
            trip=int(temp)
            route=findroute(trip)
            zhop.append([a0[3],route])
        if(a00[0]==temp):
            trip=int(temp)
            route=findroute(trip)
            zhop.append([a00[3],route])
        if(a1[0]==temp):
            trip=int(temp)
            route=findroute(trip)
            ohop.append([a1[3],route])
        if(a11[0]==temp):
            trip=int(temp)
            route=findroute(trip)
            ohop.append([a11[3],route])
#print(zhop)
#print(ohop)
fstop_times.close()

myset0=set()
for i in zhop:
    if(i[0]==s_id[1]):
        myset0.add(i[1])

myset1=set()
for i in ohop:
    if(i[0]==s_id[1]):
        myset1.add(i[1])
if(len(myset0)==0):
    print("No Zero hop routes")
else:
    print("zero hop routes are=",myset0)
if(len(myset1)==0):
    print("NO One hop routes present")
else:
    print("one hop routes are=",myset1)


        
