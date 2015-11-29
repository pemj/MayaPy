from nimble import cmds as mc
from difflib import SequenceMatcher as sm

#def normTwo(value):
#    return abs(value)/100

# newVal will be between -100 and 100, with negative/positive representing sad and angry respectively
def eyeBrow(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceAngry"
        suffix    = "FaceDeformer.FaceSad"
    else:
        suffix    =  "FaceDeformer.FaceAngry"
        nonSuffix = "FaceDeformer.FaceSad"
    newVal = abs(newVal)/100.0
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix, newVal)
    
# This one needs some work    
def mouthEnbiggen(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceBigMouth"
        suffix    = "FaceDeformer.FaceSmallMouth"
    else:
        suffix    =  "FaceDeformer.FaceBigMouth"
        newVal=newVal*.75
        nonSuffix = "FaceDeformer.FaceSmallMouth"
    newVal = abs(newVal)/100.0
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  newVal)

def eyeEnbiggen(newVal):
    newP=abs(newVal)/100.0 # new percentage
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceBigEye"
        suffix    = "FaceDeformer.FaceSmallEye"
        scaleV = 1 - newP*.4 #woo guess what I learned in sciviz class?
    else:
        suffix    =  "FaceDeformer.FaceBigEye"
        nonSuffix = "FaceDeformer.FaceSmallEye"
        scaleV = 1 + newP*.5 #woo guess what I learned in sciviz class?
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  newP)
    mc.setAttr("LeftEye.scaleZ", scaleV)
    mc.setAttr("LeftEye.scaleX", scaleV)
    mc.setAttr("LeftEye.scaleY", scaleV)
    mc.setAttr("RightEye1.scaleZ", scaleV)
    mc.setAttr("RightEye1.scaleX", scaleV)
    mc.setAttr("RightEye1.scaleY", scaleV)

# smile/frown thing.
def mouth(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.Face6"
        suffix    = "FaceDeformer.FaceFrown"
    else:
        suffix    =  "FaceDeformer.Face6"
        newVal = newVal*.75
        nonSuffix = "FaceDeformer.FaceFrown"
    newVal = abs(newVal)/100.0
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  newVal)


# tall or wide head
def head(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceTall"
        suffix    = "FaceDeformer.FaceWide"
    else:
        suffix    =  "FaceDeformer.FaceTall"
        nonSuffix = "FaceDeformer.FaceWide"
    newVal = abs(newVal)/100.0
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix, newVal)


# wide or narrow eyes
def eyeDistance(newVal):
    newP=abs(newVal)/100.0 # new percentage
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceWideEye"
        suffix    = "FaceDeformer.FaceNarrowEye"
        scaleV= newP*-.25 #woo guess what I learned in sciviz class?
    else:
        suffix    =  "FaceDeformer.FaceWideEye"
        nonSuffix = "FaceDeformer.FaceNarrowEye"
        scaleV= newP*.5 #woo guess what I learned in sciviz class?
        
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  newP)
    mc.setAttr("LeftEye.translateX", scaleV)
    mc.setAttr("RightEye1.translateX", -1*scaleV)


