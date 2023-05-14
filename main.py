# 测试了很多的强化学习算法之后，发现还不如选择直接去模拟，这样的效果简单又直接。。
# 下面就是模拟的解法啦。
from WindPowerSimulation.FlorisEnv import FlorisEnv
import time
# 我们选择角度间隔为10度，范围是 [-60,60] 间隔为10，总共12个。
# 我们让最后的三个是保持不运动的。直接暴力穷举计算大概30000次计算
# 又因为风力是从上往下的，所以我们可以先利用前两个风力去对整个系统进行计算，找到最优解，随后再去对中间的进行计算，找到最优解。
def optimize(Min = -60,Max = 60,Precision=10,show=False):
    start_time = time.time()
    myenv = FlorisEnv()

    index_save_x1 = 0
    index_save_x2 = 0
    index_save_x3 = 0
    index_save_x4 = 0
    index_save_x5 = 0
    index_save_x6 = 0
    ans_max_save = - 10000
    #直接三个循环啦，迎风进行计算。。
    for x1 in range(Min, Max, Precision):
        for x2 in range(Min, Max, Precision):
            ans =  myenv.RUN(angle = [x1,x2,0,0,0,0])
            if(ans > ans_max_save):
                ans_max_save = ans
                index_save_x1 = x1
                index_save_x2 = x2

    for x3 in range(Min, Max, Precision):
        for x4 in range(Min, Max, Precision):
            ans =  myenv.RUN(angle = [index_save_x1,index_save_x2,x3,x4,0,0])
            if(ans > ans_max_save):
                ans_max_save = ans
                index_save_x3 = x3
                index_save_x4 = x4

    for x5 in range(Min, Max, Precision):
        for x6 in range(Min, Max, Precision):
            ans =  myenv.RUN(angle = [index_save_x1,index_save_x2,index_save_x3,index_save_x4,x5,x6])
            if(ans > ans_max_save):
                ans_max_save = ans
                index_save_x5 = x5
                index_save_x6 = x6
    if(show):
        myenv.RUN(angle=[index_save_x1, index_save_x2, index_save_x3, index_save_x4, index_save_x5, index_save_x6],show = True)
    end_time = time.time()
    print(f'the final result is {index_save_x1,index_save_x2,index_save_x3,index_save_x4,index_save_x5,index_save_x6} with reuslt of {ans_max_save:.2f} time cost {end_time - start_time:.2f}')

if __name__ =='__main__':

    optimize(Precision = 5,show=True)