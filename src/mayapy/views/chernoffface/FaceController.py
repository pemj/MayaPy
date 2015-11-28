from nimble import cmds as mc
from difflib import SequenceMatcher as sm

# newVal will be between -100 and 100, with negative/positive representing sad and angry respectively
def eyeBrow(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceAngry"
        suffix    = "FaceDeformer.FaceSad"
    else:
        suffix    =  "FaceDeformer.FaceAngry"
        nonSuffix = "FaceDeformer.FaceSad"
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  ((newVal/100.0) + 1.0)/2.0))
    
def mouthEnbiggen(newVal):
    name = "mouthSize.FaceBigMouth"
    mc.setAttr(name,  ((newVal/100.0) + 1.0)/2.0))

def eyeEnbiggen(newVal):
    newP=((newVal/100.0) + 1.0)/2.0 # new percentage
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceBigEye"
        suffix    = "FaceDeformer.FaceSmallEye"
        scaleV=newP + (1-newP)*.6 #woo guess what I learned in sciviz class?
    else:
        suffix    =  "FaceDeformer.FaceBigEye"
        nonSuffix = "FaceDeformer.FaceSmallEye"
        scaleV=newP*1.5 + (1-newP) #woo guess what I learned in sciviz class?
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  newP)
    mc.setAttr("LeftEye.scaleZ", scaleV)
    mc.setAttr("LeftEye.scaleX", scaleV)
    mc.setAttr("LeftEye.scaleY", scaleV)
    mc.setAttr("RightEye1.scaleZ", scaleV)
    mc.setAttr("RightEye1.scaleX", scaleV)
    mc.setAttr("RightEye1.scaleY", scaleV)

# Face6, I know, it's bad, but Maya loses its shit when I try to
# change the name of the thing.
def mouth(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.Face6"
        suffix    = "FaceDeformer.FaceFrown"
    else:
        suffix    =  "FaceDeformer.Face6"
        nonSuffix = "FaceDeformer.FaceFrown"
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  ((newVal/100.0) + 1.0)/2.0))



def head(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceTall"
        suffix    = "FaceDeformer.FaceWide"
    else:
        suffix    =  "FaceDeformer.Tall"
        nonSuffix = "FaceDeformer.FaceWide"
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  ((newVal/100.0) + 1.0)/2.0))


#next up
def eyeDistance(newVal):
    newP=((newVal/100.0) + 1.0)/2.0 # new percentage
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceWideEye"
        suffix    = "FaceDeformer.FaceNarrowEye"
        scaleV=newP*-.25 #woo guess what I learned in sciviz class?
    else:
        suffix    =  "FaceDeformer.FaceWideEye"
        nonSuffix = "FaceDeformer.FaceNarrowEye"
        scaleV=newP*.5 #woo guess what I learned in sciviz class?
        
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  newP)
    ltX = mc.getAttr("LeftEye.translateX")
    rtX = mc.getAttr("RightEye1.translateX")
    mc.setAttr("LeftEye.translateX", ltX+scaleV)
    mc.setAttr("RightEye1.translateX", rtX-scaleV)


    
#this might be extraneous, but I'm a keep it here until I double-check
def findName(namelike):
    objs = mc.ls()
    bodyName = ""
	compareScore = 0
	newScore = 0
    for nm in objs:
		newScore = sm(None, nameLike, nm).ratio()
		if newScore > compareScore:
			compareScore = newScore
			bodyName = nm
	
    print("query for: \"" + namelike + "\" returns: " + bodyName)
    return bodyName

