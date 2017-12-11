import arcpy, string

from arcpy import env
from arcpy.sa import *

##Opens the extension so it can be used
arcpy.CheckOutExtension("spatial")

##Inputs by the user
Green = arcpy.GetParameterAsText(0)
NIR = arcpy.GetParameterAsText(1)

##Output image
ChplVeg= arcpy.GetParameterAsText(2)

##Calculations to get the result
Num = arcpy.sa.Float(Raster(NIR))
Denom = arcpy.sa.Float(Raster(Green))
NIR_eq = arcpy.sa.Divide(Num, Denom)
Nir_eq2 = arcpy.sa.Minus(NIR_eq, 1)

##Saving the result from the calculations
Nir_eq2.save(ChplVeg)

## Will put the result on the display
arcpy.SetParameterAsText(2, ChplVeg)
