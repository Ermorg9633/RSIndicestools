import arcpy, string

from arcpy import env
from arcpy.sa import *

##Opens the extension so it can be used
arcpy.CheckOutExtension("spatial")

##Inputs by the user
NIR = arcpy.GetParameterAsText(1)
Green = arcpy.GetParameterAsText(0)

##Output image
NDWI = arcpy.GetParameterAsText(2)

##Calculations to get the result
Num = arcpy.sa.Float(Raster(Green) - Raster(NIR))
Denom = arcpy.sa.Float(Raster(NIR) + Raster(Green))
NIR_eq = arcpy.sa.Divide(Num, Denom)

##Saving the result from the calculations
NIR_eq.save(NDWI)

## Will put the result on the display
arcpy.SetParameterAsText(2, NDWI)
