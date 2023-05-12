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
    def get_influence_area(self,angle):
        # use the real power gradient
        #使用 self.position_turbine对后续的结构进行相关的分析
        # try to get the influence_area after the turbine and the influence_ratio
        # return influence_area_index,influence_ratio #[N,1] [N,] #这里我们需要给出
        pass
    def update(self,angle):
        # angle 4个风机所选择的对应角度~当前我们的要求是 -90 ~ 90度之间
        # 用来修改我们当前的map，更新风速场
        pass
    def get_power(self,angle):
        return power # return sum of all the power
        pass