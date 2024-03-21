import os
import subprocess



def shp2postgis(folder,tableName):
    shpPath = os.path.join("E:\\",folder)
    or2ogrpath = "D:\\ruanjian\\qgis\\bin\\ogr2ogr.exe"
    tableName = "public." + tableName

    argument1 =(or2ogrpath + " -progress --config PG_USE_COPY YES -f PostgreSQL \"PG:host=10.17.102.29 port=5444 dbname=gis password=smart active_schema=public user=smart\" -lco DIM=2 "
                + shpPath +
                " -overwrite -lco GEOMETRY_NAME=geom -lco FID=id -nln  " +tableName+ " -nlt PROMOTE_TO_MULTI  -lco PRECISION=NO")
    bat_file_path = os.path.join("E:\\",folder,"start.bat")

    with open(bat_file_path, 'w') as f:
        f.write(argument1)

    result = subprocess.run(bat_file_path, shell=True)
    if result.returncode !=0:
        print("入库失败： ",folder)

shp2postgis("/FOLDER/1693887085896794112/8、浅层地热能开发利用区划图/CGZYDRQH.shp", "shp_rpzqah082215")