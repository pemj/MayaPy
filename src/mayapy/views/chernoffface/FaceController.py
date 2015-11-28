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

def eyeDistance(newVal):
    name = "blendShape1.eyeWidth"
    mc.setAttr(name,  ((newVal/100.0) + 1.0)/2.0))

def mouthEnbiggen(newVal):
    name = "mouthSize.FaceBigMouth"
    mc.setAttr(name,  ((newVal/100.0) + 1.0)/2.0))

def eyeEnbiggen(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.FaceBigEye"
        suffix    = "FaceDeformer.FaceSmallEye"
    else:
        suffix    =  "FaceDeformer.FaceBigEye"
        nonSuffix = "FaceDeformer.FaceSmallEye"
    mc.setAttr(nonSuffix,  0.0)
    newP=((newVal/100.0) + 1.0)/2.0 # new percentage
    mc.setAttr(suffix,  newP)
    scaleV=newP*1.5 + (1-newP)*.6 #woo guess what I learned in sciviz class?
    mc.setAttr("LeftEye.scaleZ", scaleV)
    mc.setAttr("LeftEye.scaleX", scaleV)
    mc.setAttr("LeftEye.scaleY", scaleV)
    mc.setAttr("RightEye1.scaleZ", scaleV)
    mc.setAttr("RightEye1.scaleX", scaleV)
    mc.setAttr("RightEye1.scaleY", scaleV)


def head(newVal):
    name = "blendShape1.headShape"
    mc.setAttr(name,  ((newVal/100.0) + 1.0)/2.0))


def mouth(newVal):
    if newVal < 0:
        nonSuffix = "FaceDeformer.Face6"
        suffix    = "FaceDeformer.FaceFrown"
    else:
        suffix    =  "FaceDeformer.Face6"
        nonSuffix = "FaceDeformer.FaceFrown"
    mc.setAttr(nonSuffix,  0.0)
    mc.setAttr(suffix,  ((newVal/100.0) + 1.0)/2.0))


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

