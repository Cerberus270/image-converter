from genericpath import isdir
from PIL import Image
import os
import argparse
import platform
import sys
import pathlib
import time

#Variable for measure execution time
starTime = time.time()

parser = argparse.ArgumentParser()
system = platform.system()


parser.add_argument('-p','--path', required=True,
                    help="Absolute path to Images to convert")
parser.add_argument('-t','--type',
                    help="Image format to search, with format: rgb,pbm,pgm,ppm,tiff,rast,xbm,jpg,jpeg,bmp,png,webp,exr  Without blank spaces!")
parser.add_argument('-o','--out', required=True,
                    help="Output image format, supported (jpg must be as jpeg): rgb,pbm,pgm,ppm,tiff,rast,xbm,jpeg,bmp,png,webp,exr")

"""
before use path.join, I had a problem with the path (tested in windows and ubuntu)
and this was my try to fix, 
"""
# if(system == 'Windows'):
#     osJoin = '\\'
# elif (system == 'Linux' or system == 'Darwin'):
#     osJoin = '/'
# else:
#     sys.exit("OS cannot be determinated, program will not work")

#convert parser to a dict
args = vars(parser.parse_args())

#supported type files
supportedInputFiles = ('rgb','pbm','pgm','ppm','tiff','rast','xbm','jpeg','jpg','bmp','png','webp','exr')
supportedOutputFiles = ('rgb','pbm','pgm','ppm','tiff','rast','xbm','jpeg','bmp','png','webp','exr')

pathFolder = args["path"]

try:
    #this check if the path given is a directory or a file
    if os.path.isdir(pathFolder):
        #argument values are parser
        typeIn = tuple(args["type"].split(","))
        typeOut = args["out"]
        #files = os.listdir(pathFolder)
        pathImagesToConvert = []
        #filesNames = []

        #Check if parameter --type is empty or file formats are not valid
        if not typeIn:
            print("--- %s seconds ---" % (time.time() - starTime))
            sys.exit("--type argument must have a valid value")
        else:
            for t in typeIn:
                if t not in supportedInputFiles:
                    print("--- %s seconds ---" % (time.time() - starTime))
                    sys.exit("You entered an invalid image format in the --type parameter, valid formats: "+str(supportedInputFiles))
        #Check parameter --t file formats
        if typeOut not in supportedOutputFiles:
            print("--- %s seconds ---" % (time.time() - starTime))
            sys.exit("You entered an invalid image format in the --out parameter, valid formats: "+str(supportedOutputFiles))
                
         #this was the old way to make new path       
        #os.path.exist(args["path"])
        if(os.path.isdir(pathFolder)):
            for file in os.listdir(pathFolder):
                if file.endswith(typeIn):
                    #pathImagesToConvert.append(pathFolder+osJoin+file)
                    pathImagesToConvert.append(os.path.join(pathFolder, file))

            pathSave = pathImagesToConvert
            for ps in typeIn:
                pathSave = list(map(lambda e: e.replace('.'+ps,'.'+typeOut),pathSave))

            #for to convert all images    
            for i in range(0,len(pathImagesToConvert)):
                im = Image.open(pathImagesToConvert[i]).convert("RGB")
                im.save(pathSave[i],typeOut)
            print("Success!")
            print("--- %s seconds ---" % (time.time() - starTime))
        else:
            print("Error, the path is not valid or not exist")
            print("--- %s seconds ---" % (time.time() - starTime))
    elif os.path.isfile(pathFolder):
        typeIn = pathlib.Path(pathFolder).suffix.replace('.','')
        typeOut = args["out"]
        if typeIn not in supportedInputFiles:
            print("--- %s seconds ---" % (time.time() - starTime))
            sys.exit("You entered an invalid image format in the --type parameter, valid formats: "+str(supportedInputFiles))

        if typeOut not in supportedOutputFiles:
            print("--- %s seconds ---" % (time.time() - starTime))
            sys.exit("You entered an invalid image format in the --out parameter, valid formats: "+str(supportedOutputFiles))
        pathSave = pathFolder.replace('.'+typeIn,'.'+typeOut)
        im = Image.open(pathFolder).convert("RGB")
        im.save(pathSave,typeOut)
        print("Success!")
        print("--- %s seconds ---" % (time.time() - starTime))
    else:
        print("--- %s seconds ---" % (time.time() - starTime))
        print("The path is not valid or file not exist")
except AttributeError:
    print("--- %s seconds ---" % (time.time() - starTime))
    sys.exit("The parameter -t was not given, check -h")