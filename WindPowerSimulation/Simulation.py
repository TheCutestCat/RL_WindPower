# wind, angle -> power
# wind, angle -> wind after the wind plant()
# a map 2D of the wind
# a place 2D of the plant
# input : wind_angle
# the wind direction
# we can just simulate this on just 4 plant.
# make sure that there is a corresponding result
import math

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

    direct_wind_speed = wind_speed *math.cos(math.radians(Turbine_angle))>WS_CutOut
    if(direct_wind_speed <WS_CutIn  or direct_wind_speed >WS_CutOut):
        return 0
    elif(WS_Rated<direct_wind_speed < WS_CutOut):
        return WS_Rated
    else:
        return direct_wind_speed