from gait_human import * 

q = []; dq = []; u = []; pos = []; time = []
f = 6
from matplotlib import pyplot as plt
start = [-0.6,0.7,0.0,-0.5,-0.3]
start_pos = [[0,0]]
for k in range(f):
    me = walker(start,start_pos[k])
    n1 = nlp(me)
    sol1 = me.opti.solve()
    for j in range(5):
        # tq = []; tdq = []; tu = []; tpos = []
        tempq = [];tempdq = [];tempu = [];temp = []
        for i in range(me.N):
            tempq.append(sol1.value(me.state[i][0][j]))    
            tempdq.append(sol1.value(me.state[i][1][j]))
            temp.append([sol1.value(me.pos[i][j][0]),sol1.value(me.pos[i][j][1])]) 
            if j < 4:
                tempu.append(sol1.value(me.u[i][0][j]))

        if k > 0:
            q[j].extend(tempq)
            dq[j].extend(tempdq)
            pos[j].extend(temp)
            if j < 4:    
                u[j].extend(tempu)
            # print(j)    
        else : 
            q.append(tempq)
            dq.append(tempdq)
            pos.append(temp)   
            u.append(tempu)

    start = [q[4][-1],q[3][-1],q[2][-1],q[1][-1],q[0][-1]]
#     start = [q[0][-1],q[1][-1],q[2][-1],q[3][-1],q[4][-1]]
    
    start_pos.append([pos[4][-1][0],pos[4][-1][1]])

#     if k > 1:
        # print(start_pos[k][1])

time = np.arange(0.0, f*me.T, me.h)

from matplotlib import animation
from celluloid import Camera
# print(len(pos[0]))
fig = plt.figure()
camera = Camera(fig)
k = 0
for i in range(f*me.N):
    # print(i)    
    p1 = [pos[0][i][1],pos[0][i][0]]
    p2 = [pos[1][i][1],pos[1][i][0]]
    p3 = [pos[2][i][1],pos[2][i][0]]
    p4 = [pos[3][i][1],pos[3][i][0]]
    p5 = [pos[4][i][1],pos[4][i][0]]
    # plt.axes(xlim=(-2, 2), ylim=(-2, 2))
    plt.axes(xlim=(-1, 6), ylim=(-2, 2))
    # plt.plot([0,-p1[1]], [0,p1[0]],'r',[-p1[1],-p2[1]], [p1[0],p2[0]],'b',
    #     [-p2[1],-p3[1]], [p2[0],p3[0]],'c',
    #     [-p2[1],p4[1] - 2*p2[1]], [p2[0],2*p2[0]-p4[0]],'b',
    #     [p4[1] - 2*p2[1],p5[1]], [2*p2[0]-p4[0],(p5[0] - 2*p2[0])],'r')
    if i%me.N == 0:
            p0 = start_pos[k]
            print(p0)
            k += 1 

    plt.plot([p0[0],p1[1]], [p0[1],p1[0]],'r',[p1[1],p2[1]], [p1[0],p2[0]],'b',
            [p2[1],p3[1]], [p2[0],p3[0]],'c', [p2[1],p4[1]], [p2[0],p4[0]],'b',
            [p4[1],p5[1]], [p4[0],p5[0]],'r')
    
    plt.plot([-2,6],[0,0],'g')    
    # if cv2.waitKey(0) & 0xFF == ord("q"):
    # #     break
    camera.snap()
animation = camera.animate(interval=60)
# animation.save('path_human.mp4')
plt.show()
plt.close()

name = ['q','dq','u']

plt.subplot(311)
plt.title('Optimised Solution')
plt.plot(q[:][0],'r',q[:][1],'g',q[:][2],'b',
        q[:][3],'y',q[:][4],'c')

# plt.subplot(321)
# plt.title('Initial Guess')
# iniq = n1.initial[0]
# plt.plot(time,np.append(iniq[:][0],iniq[:][0]),'r',time,np.append(iniq[:][1],iniq[:][1]),'g',time,np.append(iniq[:][2],iniq[:][2]),'b',
#         time,np.append(iniq[:][3],iniq[:][3]),'y',time,np.append(iniq[:][4],iniq[:][4]),'c')
plt.ylabel(name[0])

plt.subplot(312)
plt.plot(dq[:][0],'r',dq[:][1],'g',dq[:][2],'b',
        dq[:][3],'y',dq[:][4],'c')

# plt.subplot(323)
# inidq = n1.initial[1]
# plt.plot(time,np.append(inidq[:][0],inidq[:][0]),'r',time,np.append(inidq[:][1],inidq[:][1]),'g',time,np.append(inidq[:][2],inidq[:][2]),'b',
#         time,np.append(inidq[:][3],inidq[:][3]),'y',time,np.append(inidq[:][4],inidq[:][4]),'c')
plt.ylabel(name[1])

plt.subplot(313)
plt.plot(u[:][0],'g',u[:][1],'b',u[:][2],'y',
        u[:][3],'c')

# plt.subplot(325)
# iniu = n1.initial[2]
# plt.plot(time,np.append(iniu[:][0],iniu[:][0]),'r',time,np.append(iniu[:][1],iniu[:][1]),'g',time,np.append(iniu[:][2],iniu[:][2]),'b',
#         time,np.append(iniu[:][3],iniu[:][3]),'y',time,np.append(iniu[:][4],iniu[:][4]),'c')
plt.ylabel(name[2])

plt.suptitle('Five-Link')
plt.show()