import arcpy, string

from arcpy import env
from arcpy.sa import *

##Opens the extension so it can be used
arcpy.CheckOutExtension("spatial")

##Inputs by the user
Red = arcpy.GetParameterAsText(0)
Blue = arcpy.GetParameterAsText(1)

##Output image
Color = arcpy.GetParameterAsText(2)

##Calculations to get the result
Num = arcpy.sa.Float(Raster(Red) - Raster(Blue))
Denom = arcpy.sa.Float(Raster(Red))
NIR_eq = arcpy.sa.Divide(Num, Denom)

##Saving the result from the calculations
NIR_eq.save(Color)

## Will put the result on the display
arcpy.SetParameterAsText(2, Color)
