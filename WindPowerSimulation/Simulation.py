# try to use the floris, this funtion is no more useful
# wind, angle -> power
# wind, angle -> wind after the wind plant()
# a map 2D of the wind
# a place 2D of the plant
# input : wind_angle
# the wind direction
# we can just simulate this on just 4 plant.
# make sure that there is a corresponding result
import math
import numpy as np
def GetPower(wind_speed:float,Turbine_angle:float):
    # wind_speed float 0 ~ max_speed
    # Turbine_angle float -90  ~ 90
    # wind don't change the angle
    # cut_in wind_speed -> begin to generate the power
    WS_CutIn = 1
    # related wind_speed -> minimum wind speed to get the max wind power
    WS_Rated = 5
    # cut_out wind_speed wind power to 0, because the speed is too high..
    WS_CutOut = 10
    # TODO 当前只是一个线性模型哦，需要成对应的实际一个曲线的形式
    if(wind_speed <0 or wind_speed >WS_CutOut+10):
        raise ValueError('wind_speed out of range')
    # set the turbine_angle to -90 ~ 90
    if(Turbine_angle<0 or Turbine_angle >90):
        raise ValueError('Turbine_angle out of range of -90~90')

    direct_wind_speed = wind_speed *math.cos(math.radians(Turbine_angle))
    if(direct_wind_speed <=WS_CutIn  or direct_wind_speed >=WS_CutOut):
        return 0
    elif(WS_Rated<direct_wind_speed < WS_CutOut):
        return WS_Rated - WS_CutIn
    else:
        return direct_wind_speed- WS_CutIn

def GetNeighbor():
    pass

def GenerateMap(length, width, initial_wind_speed = 3):
    if(initial_wind_speed <= 0):
        raise ValueError('initial_wind_speed should larger than 0')
    grid = np.ones([length,width])*initial_wind_speed
    return grid
def GetInfluence(map,initial_pos,width,angle):
    # TODO
    # 这里可以尝试创建很多个的节点去进行要给测验
    # 在对应的位置之后，所有可以有对应关系的节点
    # 还需要给出来在influence map之外的节点
    # 然后根据对应的距离关系给出一个大概的结果
    # 其实我们可以直接将这个结果改编为 update..
    return  #一个对应的比较小的区间位置。
    pass
class Map():
    def __init__(self, length = 500,width = 100,initial_wind_speed = 3):
        self.length = length
        self.width = width
        self.initial_wind_speed = initial_wind_speed
        self.map = GenerateMap(self.length,self.width,self.initial_wind_speed)
        self.position_turbine = self.get_turbine_index()
    def get_turbine_index(self,position_index = None):
        # 确定turbine当前的简单的对应位置
        position_index = [[0.5,0.2],[0.5,0.8]]
        position = []
        for pos in position_index:
            index_x, index_y = pos
            position_x,position_y = int(self.length * index_x), int(self.width * index_y)
            position.append([position_x,position_y])
        return position

    # def get_influence(self,position_index,angle):
    #     # position_index just a real single number.
    #     pos_x,pos_y = self.position_turbine[position_index]
    #     # 同时假设在经过风力发电机之后，其影响的范围是一条直线(一条直线影响后面的结果)
    #     influence_area = [] # just the place after that
    #     # 对应的线性的实现逻辑
    #     #just one angle and one map
    #     return
    #     pass
    def update(self,angle):
        # angle 4个风机所选择的对应角度~当前我们的要求是 -90 ~ 90度之间
        # 用来修改我们当前的map，更新风速场
        # 还是直接去使用update吧。
        # 直接写出来简单的解法。
        pass
    def get_power(self,angle):
        # return power # return sum of all the power
        pass