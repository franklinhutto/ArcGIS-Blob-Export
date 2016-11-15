#-------------------------------------------------------------------------------
# Name:        Blob Export
# Purpose: Export Pictures out of a Blob field in ArcSDE
# Franklin Hutto
# http://support.esri.com/technical-article/000011912
# Created:     15/06/2016
#-------------------------------------------------------------------------------
import arcpy
import os
inTable = arcpy.GetParameterAsText(0)
fileLocation = arcpy.GetParameterAsText(1)
with arcpy.da.SearchCursor(inTable, ['DATA', 'ATT_NAME', 'ATTACHMENTID']) as cursor:
    for item in cursor:
        attachment = item[0]
        filenum = "ATT" + str(item[2]) + "_"
        filename = filenum + str(item[1])
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
del item
del filenum
del filename
del attachment