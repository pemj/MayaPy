# ChernoffFaceWidget.py
# (C)2013
# Scott Ernst, Peter McKay, Ryan Leonard.

import nimble
from math import radians, sin, cos
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
import FaceController as fc

#___________________________________________________________________________________________________ ChernoffFaceWidget
class ChernoffFaceWidget(PyGlassWidget):
    """A class for the finaly Project"""
    
#===================================================================================================
#                                                                                       C L A S S
#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of ChernoffFaceWidget."""
        super(ChernoffFaceWidget, self).__init__(parent, **kwargs)
	# slider pane
        self.eyebrowAngleSlider.sliderReleased.connect(self._handleEyebrowChange)
        self.mouthAngleSlider.sliderReleased.connect(self._handleMouthAngleChange)
        self.eyeSizeSlider.sliderReleased.connect(self._handleEyeSizeChange)
        self.mouthSizeSlider.sliderReleased.connect(self._handleMouthSizeChange)
        self.headShapeSlider.sliderReleased.connect(self._handleHeadShapeChange)
        self.eyeSpacingSlider.sliderReleased.connect(self._handleEyeSpacingChange)
	# nav pane
        self.runBtn.clicked.connect(self._handleRunBtn)
        self.homeBtn.clicked.connect(self._handleReturnHome)
    #===================================================================================================
    #                                                                                 H A N D L E R S
  
    #___________________________________________________________________________________________________ _handleValChange
    def _handleEyebrowChange(self):
        eyeAngle = self.eyebrowAngleSlider.value()
	print("eyebrow angle: "+str(eyeAngle))
	fc.eyeBrow(eyeAngle)
        
  
    #___________________________________________________________________________________________________ _handleValChange
    def _handleEyeSpacingChange(self):
        eyeSpace = self.eyeSpacingSlider.value()
	print("eye spacing: "+str(eyeSpace))
	fc.eyeDistance(eyeSpace)
        
  
    #___________________________________________________________________________________________________ _handleValChange
    def _handleMouthSizeChange(self):
        mouthSize = self.mouthSizeSlider.value()
        print("mouth size: "+str(mouthSize))
	fc.mouthEnbiggen(mouthSize)
        
  
    #___________________________________________________________________________________________________ _handleValChange
    def _handleEyeSizeChange(self):
        eyeSize = self.eyeSizeSlider.value()
        print("eye size: "+str(eyeSize))
	fc.eyeEnbiggen(eyeSize)
        
  
    #___________________________________________________________________________________________________ _handleValChange
    def _handleMouthAngleChange(self):
        mouthAngle = self.mouthAngleSlider.value()
        print("Mouth Angle: "+str(mouthAngle))
	fc.mouth(mouthAngle)
        
    #___________________________________________________________________________________________________ _handleValChange
    def _handleHeadShapeChange(self):
        headShape = self.headShapeSlider.value()
       	print("head shape: "+str(headShape))
        fc.head(headShape)

	#___________________________________________________________________________________________________ _handleRunBtn
    def _handleRunBtn(self):
		print("Generate!")

    #___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
