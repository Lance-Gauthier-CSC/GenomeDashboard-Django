from django.db import models
'''from utils.utils import *'''
import math
import numpy as np
from numpy import random
'''import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy.linalg as la
import pyBigWig
import twobitreader
import copy
from urllib.parse import urlparse
import os
import sys'''

class vdnaManager(models.Manager):
    def Default(self):
        '''
        The backend code for the Preset Buttons on the VDNA Control Panel page.
        This function is executed upon instantiation of the website.
        It assigns starting values for most of the variables associated with this program.
        '''
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        s = "0"
        update.sMax = "146"
        t = "0"
        update.Lk = 30
        update.Nuc = "146"
        update.V1Strng = "4.3"
        update.V2Strng = "-0.35"
        update.IsNucStrng = "0"
        update.Geometry = "Default"
        ShStd = "0.76"
        SlStd = "0.68"
        RiStd = "0.37"
        TiStd = "4.6"
        RoStd = "7.2"
        TwStd = "7.3"
        update.save()

    def setVars(self):
        ''' 
        The backend code for the Preset Buttons on the VDNA Control Panel page.
        This function sets the parameter variables to preset values based off
        what the variable Geometry is currently equal to. The preset configurations
        included within this function include Straight, Bend(Roll), Bend(Tilt),
        Tilt-a-gon, Roll-a-gon, Shear(Shift), Shear(Slide), Twist(DNA), Untwisted DNA,
        Circle(Roll), Circle(Tilt), Circular DNA, Torsion Helix(+), Torsion Heix(-),
        Shear Helix(+), Shear Helix(-), Thermal, Trajectory, & Default.
        '''
        ### Determine Value of x ########
        x = "0"
        xf = 0
        MaxS = VDNA.objects.last().sMax
        MaxSf = eval(MaxS)
        MaxSf = round(MaxSf, 3)
        if(xf < MaxSf):
                xf += 1
                x = str(xf)
        ### General Variables ###########
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        Geometry = VDNA.objects.last().Geometry
        IsNucStrng = VDNA.objects.last().IsNucStrng
        IsNucStrngf = eval(VDNA.objects.last().IsNucStrng)
        IsNucStrngf = round(IsNucStrngf, 3)
        Nuc = VDNA.objects.last().IsNucStrng
        Lk = VDNA.objects.last().Lk
        Tw = VDNA.objects.last().TwistStrng
        pi = "(3.14159265358979/180.0)"
        Pi = "(3.14159265358979/70)"
        V1 = VDNA.objects.last().V1Strng
        V1f = eval(VDNA.objects.last().V1Strng)
        V1f = round(V1f, 3)
        V2 = VDNA.objects.last().V2Strng
        V2f = eval(VDNA.objects.last().V2Strng)
        V2f = round(V2f, 3)
        ### Pending Variables ###########
        t = "0"
        tf = 0
        ### Expressions #################
        ### expr1 ##
        expr1s = "(Nuc-t)"
        expr1s = expr1s.replace("Nuc", Nuc)
        expr1s = expr1s.replace("t", t)
        expr1 = eval(expr1s)
        expr1 = round(expr1, 3)
        ### expr2 ##
        tests = "((Lk+Nuc)*(Lk+Nuc)+Nuc)"
        tests = tests.replace("Lk", Lk)
        tests = tests.replace("Nuc", Nuc)
        test = eval(tests)
        if(test != 0):
            expr2s = "(x/(Lk+Nuc)*(Lk+Nuc)+Nuc)"
            expr2s = expr2s.replace("x", x)
            expr2s = expr2s.replace("Lk", Lk)
            expr2s = expr2s.replace("Nuc", Nuc)
            expr2 = eval(expr2s)
            expr2 = round(expr2, 3)
        else:
            expr2 = 0
        ### expr3 ##
        expr3s = "(Nuc+40-t)"
        expr3s = expr3s.replace("t", t)
        expr3s = expr3s.replace("Nuc", Nuc)
        expr3 = eval(expr3s)
        expr3 = round(expr3, 3)
        ### expr4 ##
        expr4s = "(40+t)"
        expr4s = expr4s.replace("t", t)
        expr4 = eval(expr4s)
        expr4 = round(expr4, 3)
        ### Straight ####################
        if(Geometry == "Straight"):
            update.TiltStrng = "0"
            update.RollStrng = "0"
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.RiseStrng = "3.4"
            update.sMax = "50"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "0"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Bend(Roll) ##################
        if(Geometry == "Bend(Roll)"):
            update.TiltStrng = "0"
            update.RollStrng = "2.0"
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.RiseStrng = "3.4"
            update.sMax = "40"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "0"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Bend(Tilt) ##################
        if(Geometry == "Bend(Tilt)"):
            update.TiltStrng = "2.0"
            update.RollStrng = "0"
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.RiseStrng = "3.4"
            update.sMax = "40"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "0"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Tilt-a-gon ##################
        if(Geometry == "Tilt-a-gon" and V1f != 0):
            quotient = "360/V1"
            quotient = quotient.replace("V1", V1)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Tilt-a-gon" and V1f == 0):
            update.TiltStrng = "0"
        if(Geometry == "Tilt-a-gon"):
            update.RollStrng = "0"
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.RiseStrng = "20"
            update.sMax = "10"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "5"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Roll-a-gon ##################
        if(Geometry == "Roll-a-gon" and V1f != 0):
            quotient = "360/V1"
            quotient = quotient.replace("V1", V1)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Roll-a-gon" and V1f == 0):
            update.RollStrng = "0"
        if(Geometry == "Roll-a-gon"):
            update.TiltStrng = "0"
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.RiseStrng = "10"
            update.sMax = "6"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "3"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### RollTilt-a-gon ##############
        if(Geometry == "RollTilt-a-gon" and V1f != 0):
            quotient = "(360/(V1*math.sqrt(2.0)))"
            quotient = quotient.replace("V1", V1)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
            update.RollStrng = str(quotient)
        if(Geometry == "RollTilt-a-gon" and V1f == 0):
            update.TiltStrng = "0"
            update.RollStrng = "0"
        if(Geometry == "RollTilt-a-gon"):
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.RiseStrng = "20"
            update.sMax = "16"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "8"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Shear(Shift) ################
        if(Geometry == "Shear(Shift)"):
            update.TiltStrng = "0"
            update.RollStrng = "0"
            update.TwistStrng = "0"
            update.ShiftStrng = "2"
            update.SlideStrng = "0"
            update.RiseStrng = "3.4"
            update.sMax = "50.0"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "0"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Shear(Slide) ################
        if(Geometry == "Shear(Slide)"):
            update.TiltStrng = "0"
            update.RollStrng = "0"
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "2"
            update.RiseStrng = "3.4"
            update.sMax = "50.0"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "0"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Twist(DNA) ##################
        if(Geometry == "Twist(DNA)"):
            update.TiltStrng = "0"
            update.RollStrng = "0"
            update.TwistStrng = "35.2"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.RiseStrng = "3.4"
            update.sMax = "50.0"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "0"
            update.V2Strng = "0"
            update.IsNucStrng = "0"
            update.save()
        ### Untwisted DNA ###############
        if(Geometry == "Untwisted DNA" and x != 0):
            quotient = "(36.0*math.sin(2*Pi*x)*math.sin(2*Pi*x)*x/35.0)"
            quotient = quotient.replace("Pi", Pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TwistStrng = str(quotient)
        if(Geometry == "Untwisted DNA" and x == 0):
            update.TwistStrng = 0
        if(Geometry == "Untwisted DNA"):
            update.TiltStrng = 0
            update.RollStrng = 0
            update.ShiftStrng = 0
            update.SlideStrng = 0
            update.RiseStrng = "3.4"
            update.sMax = "70.0"
            update.tMax = 0
            update.Lk = 0
            update.Nuc = 0
            update.V1Strng = 0
            update.V2Strng = 0
            update.IsNucStrng = 0
            update.save()
        ### Circle(Roll) ################
        if(Geometry == "Circle(Roll)" and V1f != 0):
            quotient = "(360.0/V1)"
            quotient = quotient.replace("V1", V1)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Circle(Roll)" and V1f == 0):
            update.RollStrng = 0
        if(Geometry == "Circle(Roll)"):
            update.TiltStrng = 0
            update.TwistStrng = 0
            update.ShiftStrng = 0
            update.SlideStrng = 0
            update.RiseStrng = "3.4"
            update.sMax = "49.0"
            update.tMax = 0
            update.Lk = 0
            update.Nuc = 0
            update.V1Strng = "50"
            update.V2Strng = 0
            update.IsNucStrng = 0
            update.save()
        ### Circle(Tilt) ################
        if(Geometry == "Circle(Tilt)" and V2f != 0):
            quotient = "(360.0/V2)"
            quotient = quotient.replace("V2", V2)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Circle(Tilt)" and V2f == 0):
            update.TiltStrng = 0
        if(Geometry == "Circle(Tilt)"):
            update.RollStrng = 0
            update.TwistStrng = 0
            update.ShiftStrng = 0
            update.SlideStrng = 0
            update.RiseStrng = "3.4"
            update.sMax = "49.0"
            update.tMax = 0
            update.Lk = 0
            update.Nuc = 0
            update.V1Strng = 0
            update.V2Strng = "50"
            update.IsNucStrng = 0
            update.save()
        ### Circular DNA ################
        if(Geometry == "Circular DNA" and V1f != 0):
            quotient = "(360.0/V1*math.sin(pi*Tw*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Circular DNA" and V1f != 0):
            quotient = "(360.0/V1*math.cos(pi*Tw*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Circular DNA" and V1f != 0):
            quotient = "(V2*360.0/V1)"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = eval("quotient")
            update.TwistStrng = str(quotient)
        if(Geometry == "Circular DNA" and V1f == 0):
            update.TiltStrng = 0
            update.TwistStrng = 0
        if(Geometry == "Circular DNA"):
            update.ShiftStrng = 0
            update.SlideStrng = 0
            update.RiseStrng = "3.4"
            update.sMax = "69.0"
            update.tMax = 0
            update.Lk = 0
            update.Nuc = 0
            update.V1Strng = "70"
            update.V2Strng = "6"
            update.IsNucStrng = 0
            update.save()
        ### Torsion Helix(+) ############
        if(Geometry == "Torsion Helix(+)" and V1f != 0):
            quotient = "(360.0/V1*math.sin(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Torsion Helix(+)" and V1f != 0):
            quotient = "(360.0/V1*math.cos(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Torsion Helix(+)" and V1f == 0):
            update.TiltStrng = 0
            update.RollStrng = 0
        if(Geometry == "Torsion Helix(+)"):
            update.TwistStrng = "35.2"
            update.ShiftStrng = 0
            update.SlideStrng = 0
            update.RiseStrng = "3.4"
            update.sMax = "140.0"
            update.tMax = 0
            update.Lk = 0
            update.Nuc = 0
            update.V1Strng = "70"
            update.V2Strng = "(-0.5)"
            update.IsNucStrng = 0
            update.save()
        ### Torsion Helix(-) ############
        if(Geometry == "Torsion Helix(-)" and V1f != 0):
            quotient = "360.0/V1*math.sin(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Torsion Helix(-)" and V1f != 0):
            quotient = "360.0/V1*math.cos(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Torsion Helix(-)" and V1f == 0):
            update.TiltStrng = 0
            update.RollStrng = 0
        if(Geometry == "Torsion Helix(-)"):
            update.TwistStrng = "35.2"
            update.ShiftStrng = 0
            update.SlideStrng = 0
            update.RiseStrng = "3.4"
            update.sMax = "140.0"
            update.tMax = 0
            update.Lk = 0
            update.Nuc = 0
            update.V1Strng = "70"
            update.V2Strng = "0.5"
            update.IsNucStrng = 0
            update.save()
        ### Shear Helix(+) ##############
        if(Geometry == "Shear Helix(+)" and V1f != 0):
            quotient = "(360.0/V1*math.sin(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Shear Helix(+)" and V1f != 0):
            quotient = "(360.0/V1*math.cos(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Shear Helix(+)" and V1f == 0):
            update.TiltStrng = 0
            update.RollStrng = 0
        if(Geometry == "Shear Helix(+)"):
            quotient = "(V2*math.sin(pi*Tw*x))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Shear Helix(+)"):
            quotient = "(V2*math.cos(pi*Tw*x))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Shear Helix(+)"):
            update.TwistStrng = "36.0"
            update.RiseStrng = "3.4"
            update.sMax = "140.0"
            update.tMax = 0
            update.Lk = 0
            update.Nuc = 0
            update.V1Strng = "70"
            update.V2Strng = "0.3"
            update.IsNucStrng = 0
            update.save()
        ### Shear Helix(-) ##############
        if(Geometry == "Shear Helix(-)" and V1f != 0):
            quotient = "(360.0/V1*math.sin(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Shear Helix(-)" and V1f != 0):
            quotient = "(360.0/V1*math.cos(pi*(Tw+V2)*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Shear Helix(-)"):
            quotient = "(V2*math.sin(pi*Tw*x))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Shear Helix(-)"):
            quotient = "(V2*math.cos(pi*Tw*x))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Shear Helix(-)" and V1f == 0):
            update.TiltStrng = "0"
            update.RollStrng = "0"
        if(Geometry == "Shear Helix(-)"):
            update.TwistStrng = "36.0"
            update.RiseStrng = "3.4"
            update.sMax = "140.0"
            update.tMax = "0"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = 70
            update.V2Strng = "(-0.3)"
            update.IsNucStrng = "0"
            update.save()
        ### Thermal #####################
        if(Geometry == "Thermal"):
            quotient = "(-0.3+4.6*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Thermal"):
            quotient = "(3.6+7.2*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Thermal"):
            quotient = (32.6 + 7.3 * random.normal(loc=0, scale=1))
            quotient = eval("quotient")
            update.TwistStrng = str(quotient)
        if(Geometry == "Thermal"):
            quotient = (-0.05 + 0.76 * random.normal(loc=0, scale=1))
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Thermal"):
            quotient = (-0.44 + 0.68 * random.normal(loc=0, scale=1))
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Thermal"):
            quotient = (3.32 + 0.37 * random.normal(loc=0, scale=1))
            quotient = eval("quotient")
            update.RiseStrng = str(quotient)
        if(Geometry == "Thermal"):
            update.sMax = "150"
            update.tMax = "25"
            update.Lk = "0"
            update.Nuc = "0"
            update.V1Strng = "0.0"
            update.V2Strng = "0.0"
            update.IsNucStrng = "0"
            update.save()
        ### Trajectory ##################
        if(Geometry == "Trajectory" and IsNucStrngf == xf):
            quotient = "(V1*math.sin(pi*36.0*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Trajectory" and IsNucStrngf == xf):
            quotient = "(V1*math.cos(pi*36.0 *x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Trajectory" and IsNucStrngf == xf):
            quotient = "(V1 *math.sin(pi*36.0*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Trajectory" and IsNucStrngf == xf):
            quotient = "(V1*math.cos(pi*36.0*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Trajectory" and IsNucStrngf != xf):
            update.TiltStrng = "0"
            update.RollStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
        if(Geometry == "Trajectory" and xf < expr1 and xf > tf):
            update.IsNucStrng = 1
        if(Geometry == "Trajectory" and xf >= expr1 and xf <= tf):
            update.IsNucStrng = 0
        if(Geometry == "Trajectory"):
            update.TwistStrng = "36.0"
            update.RiseStrng = "3.3"
            update.sMax = "170"
            update.tMax = "20"
            update.Lk = "30"
            update.Nuc = "146"
            update.V1Strng = "4.3"
            update.V2Strng = "(-0.25)"
            update.save()
        ### Chromatin 1 #################
        if(Geometry == "Chromatin1" and xf < expr2):
            quotient = "(V1*math.sin(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Chromatin1" and xf < expr2):
            quotient = "(V1*math.cos(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Chromatin1" and xf < expr2):
            update.TwistStrng = "34.5"
        if(Geometry == "Chromatin1" and xf < expr2):
            quotient = "(V2*math.sin(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Chromatin1" and xf < expr2):
            quotient = "(V2*math.cos(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Chromatin1" and xf < expr2):
            update.IsNucStrng = "1"
        if(Geometry == "Chromatin1" and xf >= expr2):
            update.TiltStrng = "0"
            update.RollStrng = "0"
            update.TwistStrng = "35.0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.IsNucStrng = "0"
        if(Geometry == "Chromatin1"):
            update.RiseStrng = "3.4"
            update.sMax = "3000"
            update.tMax = "0"
            update.Lk = "28"
            update.Nuc = "146"
            update.V1Strng = "4.3"
            update.V2Strng = "(-0.25)"
            update.save()
        ### Chromatin 2 #################
        if(Geometry == "Chromatin2" and xf < expr2):
            quotient = "(V1*math.sin(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Chromatin2" and xf < expr2):
            quotient = "(V1*math.cos(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Chromatin2" and xf < expr2):
            update.TwistStrng = "34.5"
        if(Geometry == "Chromatin2" and xf < expr2):
            quotient = "(V2*math.sin(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Chromatin2" and xf < expr2):
            quotient = "(V2*math.cos(pi*Tw*(x-(x/(Lk+Nuc)*(Lk+Nuc)))))"
            quotient = quotient.replace("V2", V2)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("Tw", Tw)
            quotient = quotient.replace("x", x)
            quotient = quotient.replace("Lk", Lk)
            quotient = quotient.replace("Nuc", Nuc)
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Chromatin2" and xf < expr2):
            update.IsNucStrng = "1"
        if(Geometry == "Chromatin2" and xf >= expr2):
            update.TiltStrng = "2"
            update.RollStrng = "0"
            update.TwistStrng = "0"
            update.ShiftStrng = "0"
            update.SlideStrng = "0"
            update.IsNucStrng = "0"
        if(Geometry == "Chromatin2"):
            update.RiseStrng = "3.32"
            update.sMax = "3000"
            update.tMax = "0"
            update.Lk = "33"
            update.Nuc = "146"
            update.V1Strng = "(1.70*360.0/146.0)"
            update.V2Strng = "(-20.6*1.70/146.0)"
            update.save()
        ### Default #####################
        if(Geometry == "Default" and IsNucStrngf == xf):
            quotient = "(V1*math.sin(pi*34.5*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf == xf):
            quotient = "(V1*math.cos(pi*34.5*x))"
            quotient = quotient.replace("V1", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf == xf):
            update.TwistStrng = "34.95"
        if(Geometry == "Default" and IsNucStrngf == xf):
            quotient = "(V2*math.sin(pi*34.5*x))"
            quotient = quotient.replace("V2", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf == xf):
            quotient = "(V2*math.cos(pi*34.5*x))"
            quotient = quotient.replace("V2", V1)
            quotient = quotient.replace("pi", pi)
            quotient = quotient.replace("x", x)
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf == xf):
            update.RiseStrng = "3.4"
        if(Geometry == "Default" and IsNucStrngf != xf):
            quotient = "(-0.3+4.6*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.TiltStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf != xf):
            quotient = "(3.6+7.2*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.RollStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf != xf):
            quotient = "(32.6+7.3*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.TwistStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf != xf):
            quotient = "(-0.05+0.76*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.ShiftStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf != xf):
            quotient = "(-0.44+0.68*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.SlideStrng = str(quotient)
        if(Geometry == "Default" and IsNucStrngf != xf):
            quotient = "(3.32+0.37*random.normal(loc=0, scale=1))"
            quotient = eval("quotient")
            update.RiseStrng = str(quotient)
        if(Geometry == "Default" and xf < expr3 and xf > expr4):
            update.IsNucStrng = "1"
        if(Geometry == "Default" and xf >= expr3 and xf <= expr4):
            update.IsNucStrng = "0"
        if(Geometry == "Default"):
            update.sMax = "230"
            update.tMax = "0"
            update.Lk = "30"
            update.Nuc = "146"
            update.save()
        ###########################################################################
        VDNA.objects.evaluate()

    def copy(self):
        '''
        This function creates a copy of the last instance of all objects in the QuerySet.
        The duplicated instance is later used in the validate function as a means of reverting changes made in that function.
        '''
        Tilt, Roll, Twist = VDNA.objects.last().TiltStrng, VDNA.objects.last().RollStrng, VDNA.objects.last().TwistStrng
        Shift, Slide, Rise = VDNA.objects.last().ShiftStrng, VDNA.objects.last().SlideStrng, VDNA.objects.last().RiseStrng
        MaxS, Lk, Nuc = VDNA.objects.last().sMax, VDNA.objects.last().Lk, VDNA.objects.last().Nuc
        V1, V2, Cores = VDNA.objects.last().V1Strng, VDNA.objects.last().V2Strng, VDNA.objects.last().IsNucStrng
        Geometry = VDNA.objects.last().Geometry
        VDNA.objects.create(TiltStrng=Tilt, RollStrng=Roll, TwistStrng=Twist, ShiftStrng=Shift, SlideStrng=Slide, RiseStrng=Rise, sMax=MaxS, Lk=Lk, Nuc=Nuc, V1Strng=V1, V2Strng=V2, Geometry=Geometry, IsNucStrng=Cores)
        VDNA.objects.create(TiltStrng=Tilt, RollStrng=Roll, TwistStrng=Twist, ShiftStrng=Shift, SlideStrng=Slide, RiseStrng=Rise, sMax=MaxS, Lk=Lk, Nuc=Nuc, V1Strng=V1, V2Strng=V2, Geometry=Geometry, IsNucStrng=Cores)

    def validate(self):
        '''
        This function checks if there are any values in the string inputted by the user.
        This safeguard is taken because of the possibility of malicious intent (in regards to the evaluate function).
        This function validates the strings by deleting all valid characters and substrings from the user inputted strings.
        If a string is empty after the delete process is completed then it is deemed valid and has it's changes reverted.
        If a string is not empty after the delete process is completed then it is deemed invalid and is set to an empty string.
        '''
        VDNA.objects.copy()
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        '''Tilt'''
        update.TiltStrng = update.TiltStrng.replace("cos(", "")
        update.TiltStrng = update.TiltStrng.replace("sin(", "")
        update.TiltStrng = update.TiltStrng.replace("tan(", "")
        update.TiltStrng = update.TiltStrng.replace("Pi", "")
        update.TiltStrng = update.TiltStrng.replace("Tl", "")
        update.TiltStrng = update.TiltStrng.replace("Rl", "")
        update.TiltStrng = update.TiltStrng.replace("Tw", "")
        update.TiltStrng = update.TiltStrng.replace("Sh", "")
        update.TiltStrng = update.TiltStrng.replace("Sl", "")
        update.TiltStrng = update.TiltStrng.replace("Rs", "")
        update.TiltStrng = update.TiltStrng.replace("Lk", "")
        update.TiltStrng = update.TiltStrng.replace("Nuc", "")
        update.TiltStrng = update.TiltStrng.replace("Cs", "")
        update.TiltStrng = update.TiltStrng.replace("MaxS", "")
        update.TiltStrng = update.TiltStrng.replace("V1", "")
        update.TiltStrng = update.TiltStrng.replace("V2", "")
        update.TiltStrng = update.TiltStrng.replace(")", "")
        update.TiltStrng = update.TiltStrng.replace("0", "")
        update.TiltStrng = update.TiltStrng.replace("1", "")
        update.TiltStrng = update.TiltStrng.replace("2", "")
        update.TiltStrng = update.TiltStrng.replace("3", "")
        update.TiltStrng = update.TiltStrng.replace("4", "")
        update.TiltStrng = update.TiltStrng.replace("5", "")
        update.TiltStrng = update.TiltStrng.replace("6", "")
        update.TiltStrng = update.TiltStrng.replace("7", "")
        update.TiltStrng = update.TiltStrng.replace("8", "")
        update.TiltStrng = update.TiltStrng.replace("9", "")
        update.TiltStrng = update.TiltStrng.replace("+", "")
        update.TiltStrng = update.TiltStrng.replace("-", "")
        update.TiltStrng = update.TiltStrng.replace("*", "")
        update.TiltStrng = update.TiltStrng.replace("/", "")
        update.save()
        if(update.TiltStrng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.TiltStrng = update2.TiltStrng
            update.save()
        else:
            update.TiltStrng = ""
            update.save()
        '''Roll'''
        update.RollStrng = update.RollStrng.replace("cos(", "")
        update.RollStrng = update.RollStrng.replace("sin(", "")
        update.RollStrng = update.RollStrng.replace("tan(", "")
        update.RollStrng = update.RollStrng.replace("Pi", "")
        update.RollStrng = update.RollStrng.replace("Tl", "")
        update.RollStrng = update.RollStrng.replace("Rl", "")
        update.RollStrng = update.RollStrng.replace("Tw", "")
        update.RollStrng = update.RollStrng.replace("Sh", "")
        update.RollStrng = update.RollStrng.replace("Sl", "")
        update.RollStrng = update.RollStrng.replace("Rs", "")
        update.RollStrng = update.RollStrng.replace("Lk", "")
        update.RollStrng = update.RollStrng.replace("Nuc", "")
        update.RollStrng = update.RollStrng.replace("Cs", "")
        update.RollStrng = update.RollStrng.replace("MaxS", "")
        update.RollStrng = update.RollStrng.replace("V1", "")
        update.RollStrng = update.RollStrng.replace("V2", "")
        update.RollStrng = update.RollStrng.replace(")", "")
        update.RollStrng = update.RollStrng.replace("0", "")
        update.RollStrng = update.RollStrng.replace("1", "")
        update.RollStrng = update.RollStrng.replace("2", "")
        update.RollStrng = update.RollStrng.replace("3", "")
        update.RollStrng = update.RollStrng.replace("4", "")
        update.RollStrng = update.RollStrng.replace("5", "")
        update.RollStrng = update.RollStrng.replace("6", "")
        update.RollStrng = update.RollStrng.replace("7", "")
        update.RollStrng = update.RollStrng.replace("8", "")
        update.RollStrng = update.RollStrng.replace("9", "")
        update.RollStrng = update.RollStrng.replace("+", "")
        update.RollStrng = update.RollStrng.replace("-", "")
        update.RollStrng = update.RollStrng.replace("*", "")
        update.RollStrng = update.RollStrng.replace("/", "")
        update.save()
        if(update.RollStrng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.RollStrng = update2.RollStrng
            update.save()
        else:
            update.RollStrng = ""
            update.save()
        '''Twist'''
        update.TwistStrng = update.TwistStrng.replace("cos(", "")
        update.TwistStrng = update.TwistStrng.replace("sin(", "")
        update.TwistStrng = update.TwistStrng.replace("tan(", "")
        update.TwistStrng = update.TwistStrng.replace("Pi", "")
        update.TwistStrng = update.TwistStrng.replace("Tl", "")
        update.TwistStrng = update.TwistStrng.replace("Rl", "")
        update.TwistStrng = update.TwistStrng.replace("Tw", "")
        update.TwistStrng = update.TwistStrng.replace("Sh", "")
        update.TwistStrng = update.TwistStrng.replace("Sl", "")
        update.TwistStrng = update.TwistStrng.replace("Rs", "")
        update.TwistStrng = update.TwistStrng.replace("Lk", "")
        update.TwistStrng = update.TwistStrng.replace("Nuc", "")
        update.TwistStrng = update.TwistStrng.replace("Cs", "")
        update.TwistStrng = update.TwistStrng.replace("MaxS", "")
        update.TwistStrng = update.TwistStrng.replace("V1", "")
        update.TwistStrng = update.TwistStrng.replace("V2", "")
        update.TwistStrng = update.TwistStrng.replace(")", "")
        update.TwistStrng = update.TwistStrng.replace("0", "")
        update.TwistStrng = update.TwistStrng.replace("1", "")
        update.TwistStrng = update.TwistStrng.replace("2", "")
        update.TwistStrng = update.TwistStrng.replace("3", "")
        update.TwistStrng = update.TwistStrng.replace("4", "")
        update.TwistStrng = update.TwistStrng.replace("5", "")
        update.TwistStrng = update.TwistStrng.replace("6", "")
        update.TwistStrng = update.TwistStrng.replace("7", "")
        update.TwistStrng = update.TwistStrng.replace("8", "")
        update.TwistStrng = update.TwistStrng.replace("9", "")
        update.TwistStrng = update.TwistStrng.replace("+", "")
        update.TwistStrng = update.TwistStrng.replace("-", "")
        update.TwistStrng = update.TwistStrng.replace("*", "")
        update.TwistStrng = update.TwistStrng.replace("/", "")
        update.save()
        if(update.TwistStrng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.TwistStrng = update2.TwistStrng
            update.save()
        else:
            update.TwistStrng = ""
            update.save()
        '''Shift'''
        update.ShiftStrng = update.ShiftStrng.replace("cos(", "")
        update.ShiftStrng = update.ShiftStrng.replace("sin(", "")
        update.ShiftStrng = update.ShiftStrng.replace("tan(", "")
        update.ShiftStrng = update.ShiftStrng.replace("Pi", "")
        update.ShiftStrng = update.ShiftStrng.replace("Tl", "")
        update.ShiftStrng = update.ShiftStrng.replace("Rl", "")
        update.ShiftStrng = update.ShiftStrng.replace("Tw", "")
        update.ShiftStrng = update.ShiftStrng.replace("Sh", "")
        update.ShiftStrng = update.ShiftStrng.replace("Sl", "")
        update.ShiftStrng = update.ShiftStrng.replace("Rs", "")
        update.ShiftStrng = update.ShiftStrng.replace("Lk", "")
        update.ShiftStrng = update.ShiftStrng.replace("Nuc", "")
        update.ShiftStrng = update.ShiftStrng.replace("Cs", "")
        update.ShiftStrng = update.ShiftStrng.replace("MaxS", "")
        update.ShiftStrng = update.ShiftStrng.replace("V1", "")
        update.ShiftStrng = update.ShiftStrng.replace("V2", "")
        update.ShiftStrng = update.ShiftStrng.replace(")", "")
        update.ShiftStrng = update.ShiftStrng.replace("0", "")
        update.ShiftStrng = update.ShiftStrng.replace("1", "")
        update.ShiftStrng = update.ShiftStrng.replace("2", "")
        update.ShiftStrng = update.ShiftStrng.replace("3", "")
        update.ShiftStrng = update.ShiftStrng.replace("4", "")
        update.ShiftStrng = update.ShiftStrng.replace("5", "")
        update.ShiftStrng = update.ShiftStrng.replace("6", "")
        update.ShiftStrng = update.ShiftStrng.replace("7", "")
        update.ShiftStrng = update.ShiftStrng.replace("8", "")
        update.ShiftStrng = update.ShiftStrng.replace("9", "")
        update.ShiftStrng = update.ShiftStrng.replace("+", "")
        update.ShiftStrng = update.ShiftStrng.replace("-", "")
        update.ShiftStrng = update.ShiftStrng.replace("*", "")
        update.ShiftStrng = update.ShiftStrng.replace("/", "")
        update.save()
        if(update.ShiftStrng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.ShiftStrng = update2.ShiftStrng
            update.save()
        else:
            update.ShiftStrng = ""
            update.save()
        '''Slide'''
        update.SlideStrng = update.SlideStrng.replace("cos(", "")
        update.SlideStrng = update.SlideStrng.replace("sin(", "")
        update.SlideStrng = update.SlideStrng.replace("tan(", "")
        update.SlideStrng = update.SlideStrng.replace("Pi", "")
        update.SlideStrng = update.SlideStrng.replace("Tl", "")
        update.SlideStrng = update.SlideStrng.replace("Rl", "")
        update.SlideStrng = update.SlideStrng.replace("Tw", "")
        update.SlideStrng = update.SlideStrng.replace("Sh", "")
        update.SlideStrng = update.SlideStrng.replace("Sl", "")
        update.SlideStrng = update.SlideStrng.replace("Rs", "")
        update.SlideStrng = update.SlideStrng.replace("Lk", "")
        update.SlideStrng = update.SlideStrng.replace("Nuc", "")
        update.SlideStrng = update.SlideStrng.replace("Cs", "")
        update.SlideStrng = update.SlideStrng.replace("MaxS", "")
        update.SlideStrng = update.SlideStrng.replace("V1", "")
        update.SlideStrng = update.SlideStrng.replace("V2", "")
        update.SlideStrng = update.SlideStrng.replace(")", "")
        update.SlideStrng = update.SlideStrng.replace("0", "")
        update.SlideStrng = update.SlideStrng.replace("1", "")
        update.SlideStrng = update.SlideStrng.replace("2", "")
        update.SlideStrng = update.SlideStrng.replace("3", "")
        update.SlideStrng = update.SlideStrng.replace("4", "")
        update.SlideStrng = update.SlideStrng.replace("5", "")
        update.SlideStrng = update.SlideStrng.replace("6", "")
        update.SlideStrng = update.SlideStrng.replace("7", "")
        update.SlideStrng = update.SlideStrng.replace("8", "")
        update.SlideStrng = update.SlideStrng.replace("9", "")
        update.SlideStrng = update.SlideStrng.replace("+", "")
        update.SlideStrng = update.SlideStrng.replace("-", "")
        update.SlideStrng = update.SlideStrng.replace("*", "")
        update.SlideStrng = update.SlideStrng.replace("/", "")
        update.save()
        if(update.SlideStrng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.SlideStrng = update2.SlideStrng
            update.save()
        else:
            update.SlideStrng = ""
            update.save()
        '''Rise'''
        update.RiseStrng = update.RiseStrng.replace("cos(", "")
        update.RiseStrng = update.RiseStrng.replace("sin(", "")
        update.RiseStrng = update.RiseStrng.replace("tan(", "")
        update.RiseStrng = update.RiseStrng.replace("Pi", "")
        update.RiseStrng = update.RiseStrng.replace("Tl", "")
        update.RiseStrng = update.RiseStrng.replace("Rl", "")
        update.RiseStrng = update.RiseStrng.replace("Tw", "")
        update.RiseStrng = update.RiseStrng.replace("Sh", "")
        update.RiseStrng = update.RiseStrng.replace("Sl", "")
        update.RiseStrng = update.RiseStrng.replace("Rs", "")
        update.RiseStrng = update.RiseStrng.replace("Lk", "")
        update.RiseStrng = update.RiseStrng.replace("Nuc", "")
        update.RiseStrng = update.RiseStrng.replace("Cs", "")
        update.RiseStrng = update.RiseStrng.replace("MaxS", "")
        update.RiseStrng = update.RiseStrng.replace("V1", "")
        update.RiseStrng = update.RiseStrng.replace("V2", "")
        update.RiseStrng = update.RiseStrng.replace(")", "")
        update.RiseStrng = update.RiseStrng.replace("0", "")
        update.RiseStrng = update.RiseStrng.replace("1", "")
        update.RiseStrng = update.RiseStrng.replace("2", "")
        update.RiseStrng = update.RiseStrng.replace("3", "")
        update.RiseStrng = update.RiseStrng.replace("4", "")
        update.RiseStrng = update.RiseStrng.replace("5", "")
        update.RiseStrng = update.RiseStrng.replace("6", "")
        update.RiseStrng = update.RiseStrng.replace("7", "")
        update.RiseStrng = update.RiseStrng.replace("8", "")
        update.RiseStrng = update.RiseStrng.replace("9", "")
        update.RiseStrng = update.RiseStrng.replace("+", "")
        update.RiseStrng = update.RiseStrng.replace("-", "")
        update.RiseStrng = update.RiseStrng.replace("*", "")
        update.RiseStrng = update.RiseStrng.replace("/", "")
        update.save()
        if(update.RiseStrng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.RiseStrng = update2.RiseStrng
            update.save()
        else:
            update.RiseStrng = ""
            update.save()
        '''Max S'''
        update.sMax = update.sMax.replace("cos(", "")
        update.sMax = update.sMax.replace("sin(", "")
        update.sMax = update.sMax.replace("tan(", "")
        update.sMax = update.sMax.replace("Pi", "")
        update.sMax = update.sMax.replace("Tl", "")
        update.sMax = update.sMax.replace("Rl", "")
        update.sMax = update.sMax.replace("Tw", "")
        update.sMax = update.sMax.replace("Sh", "")
        update.sMax = update.sMax.replace("Sl", "")
        update.sMax = update.sMax.replace("Rs", "")
        update.sMax = update.sMax.replace("Lk", "")
        update.sMax = update.sMax.replace("Nuc", "")
        update.sMax = update.sMax.replace("Cs", "")
        update.sMax = update.sMax.replace("MaxS", "")
        update.sMax = update.sMax.replace("V1", "")
        update.sMax = update.sMax.replace("V2", "")
        update.sMax = update.sMax.replace(")", "")
        update.sMax = update.sMax.replace("0", "")
        update.sMax = update.sMax.replace("1", "")
        update.sMax = update.sMax.replace("2", "")
        update.sMax = update.sMax.replace("3", "")
        update.sMax = update.sMax.replace("4", "")
        update.sMax = update.sMax.replace("5", "")
        update.sMax = update.sMax.replace("6", "")
        update.sMax = update.sMax.replace("7", "")
        update.sMax = update.sMax.replace("8", "")
        update.sMax = update.sMax.replace("9", "")
        update.sMax = update.sMax.replace("+", "")
        update.sMax = update.sMax.replace("-", "")
        update.sMax = update.sMax.replace("*", "")
        update.sMax = update.sMax.replace("/", "")
        update.save()
        if(update.sMax == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.sMax = update2.sMax
            update.save()
        else:
            update.sMax = ""
            update.save()
        '''Lk'''
        update.Lk = update.Lk.replace("cos(", "")
        update.Lk = update.Lk.replace("sin(", "")
        update.Lk = update.Lk.replace("tan(", "")
        update.Lk = update.Lk.replace("Pi", "")
        update.Lk = update.Lk.replace("Tl", "")
        update.Lk = update.Lk.replace("Rl", "")
        update.Lk = update.Lk.replace("Tw", "")
        update.Lk = update.Lk.replace("Sh", "")
        update.Lk = update.Lk.replace("Sl", "")
        update.Lk = update.Lk.replace("Rs", "")
        update.Lk = update.Lk.replace("Lk", "")
        update.Lk = update.Lk.replace("Nuc", "")
        update.Lk = update.Lk.replace("Cs", "")
        update.Lk = update.Lk.replace("MaxS", "")
        update.Lk = update.Lk.replace("V1", "")
        update.Lk = update.Lk.replace("V2", "")
        update.Lk = update.Lk.replace(")", "")
        update.Lk = update.Lk.replace("0", "")
        update.Lk = update.Lk.replace("1", "")
        update.Lk = update.Lk.replace("2", "")
        update.Lk = update.Lk.replace("3", "")
        update.Lk = update.Lk.replace("4", "")
        update.Lk = update.Lk.replace("5", "")
        update.Lk = update.Lk.replace("6", "")
        update.Lk = update.Lk.replace("7", "")
        update.Lk = update.Lk.replace("8", "")
        update.Lk = update.Lk.replace("9", "")
        update.Lk = update.Lk.replace("+", "")
        update.Lk = update.Lk.replace("-", "")
        update.Lk = update.Lk.replace("*", "")
        update.Lk = update.Lk.replace("/", "")
        update.save()
        if(update.Lk == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.Lk = update2.Lk
            update.save()
        else:
            update.Lk = ""
            update.save()
        '''Nuc'''
        update.Nuc = update.Nuc.replace("cos(", "")
        update.Nuc = update.Nuc.replace("sin(", "")
        update.Nuc = update.Nuc.replace("tan(", "")
        update.Nuc = update.Nuc.replace("Pi", "")
        update.Nuc = update.Nuc.replace("Tl", "")
        update.Nuc = update.Nuc.replace("Rl", "")
        update.Nuc = update.Nuc.replace("Tw", "")
        update.Nuc = update.Nuc.replace("Sh", "")
        update.Nuc = update.Nuc.replace("Sl", "")
        update.Nuc = update.Nuc.replace("Rs", "")
        update.Nuc = update.Nuc.replace("Lk", "")
        update.Nuc = update.Nuc.replace("Nuc", "")
        update.Nuc = update.Nuc.replace("Cs", "")
        update.Nuc = update.Nuc.replace("MaxS", "")
        update.Nuc = update.Nuc.replace("V1", "")
        update.Nuc = update.Nuc.replace("V2", "")
        update.Nuc = update.Nuc.replace(")", "")
        update.Nuc = update.Nuc.replace("0", "")
        update.Nuc = update.Nuc.replace("1", "")
        update.Nuc = update.Nuc.replace("2", "")
        update.Nuc = update.Nuc.replace("3", "")
        update.Nuc = update.Nuc.replace("4", "")
        update.Nuc = update.Nuc.replace("5", "")
        update.Nuc = update.Nuc.replace("6", "")
        update.Nuc = update.Nuc.replace("7", "")
        update.Nuc = update.Nuc.replace("8", "")
        update.Nuc = update.Nuc.replace("9", "")
        update.Nuc = update.Nuc.replace("+", "")
        update.Nuc = update.Nuc.replace("-", "")
        update.Nuc = update.Nuc.replace("*", "")
        update.Nuc = update.Nuc.replace("/", "")
        update.save()
        if(update.Nuc == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.Nuc = update2.Nuc
            update.save()
        else:
            update.Nuc = ""
            update.save()
        '''V1Strng'''
        update.V1Strng = update.V1Strng.replace("cos(", "")
        update.V1Strng = update.V1Strng.replace("sin(", "")
        update.V1Strng = update.V1Strng.replace("tan(", "")
        update.V1Strng = update.V1Strng.replace("Pi", "")
        update.V1Strng = update.V1Strng.replace("Tl", "")
        update.V1Strng = update.V1Strng.replace("Rl", "")
        update.V1Strng = update.V1Strng.replace("Tw", "")
        update.V1Strng = update.V1Strng.replace("Sh", "")
        update.V1Strng = update.V1Strng.replace("Sl", "")
        update.V1Strng = update.V1Strng.replace("Rs", "")
        update.V1Strng = update.V1Strng.replace("Lk", "")
        update.V1Strng = update.V1Strng.replace("Nuc", "")
        update.V1Strng = update.V1Strng.replace("Cs", "")
        update.V1Strng = update.V1Strng.replace("MaxS", "")
        update.V1Strng = update.V1Strng.replace("V1", "")
        update.V1Strng = update.V1Strng.replace("V2", "")
        update.V1Strng = update.V1Strng.replace(")", "")
        update.V1Strng = update.V1Strng.replace("0", "")
        update.V1Strng = update.V1Strng.replace("1", "")
        update.V1Strng = update.V1Strng.replace("2", "")
        update.V1Strng = update.V1Strng.replace("3", "")
        update.V1Strng = update.V1Strng.replace("4", "")
        update.V1Strng = update.V1Strng.replace("5", "")
        update.V1Strng = update.V1Strng.replace("6", "")
        update.V1Strng = update.V1Strng.replace("7", "")
        update.V1Strng = update.V1Strng.replace("8", "")
        update.V1Strng = update.V1Strng.replace("9", "")
        update.V1Strng = update.V1Strng.replace("+", "")
        update.V1Strng = update.V1Strng.replace("-", "")
        update.V1Strng = update.V1Strng.replace("*", "")
        update.V1Strng = update.V1Strng.replace("/", "")
        update.save()
        if(update.V1Strng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.V1Strng = update2.V1Strng
            update.save()
        else:
            update.V1Strng = ""
            update.save()
        '''V2Strng'''
        update.V2Strng = update.V2Strng.replace("cos(", "")
        update.V2Strng = update.V2Strng.replace("sin(", "")
        update.V2Strng = update.V2Strng.replace("tan(", "")
        update.V2Strng = update.V2Strng.replace("Pi", "")
        update.V2Strng = update.V2Strng.replace("Tl", "")
        update.V2Strng = update.V2Strng.replace("Rl", "")
        update.V2Strng = update.V2Strng.replace("Tw", "")
        update.V2Strng = update.V2Strng.replace("Sh", "")
        update.V2Strng = update.V2Strng.replace("Sl", "")
        update.V2Strng = update.V2Strng.replace("Rs", "")
        update.V2Strng = update.V2Strng.replace("Lk", "")
        update.V2Strng = update.V2Strng.replace("Nuc", "")
        update.V2Strng = update.V2Strng.replace("Cs", "")
        update.V2Strng = update.V2Strng.replace("MaxS", "")
        update.V2Strng = update.V2Strng.replace("V1", "")
        update.V2Strng = update.V2Strng.replace("V2", "")
        update.V2Strng = update.V2Strng.replace(")", "")
        update.V2Strng = update.V2Strng.replace("0", "")
        update.V2Strng = update.V2Strng.replace("1", "")
        update.V2Strng = update.V2Strng.replace("2", "")
        update.V2Strng = update.V2Strng.replace("3", "")
        update.V2Strng = update.V2Strng.replace("4", "")
        update.V2Strng = update.V2Strng.replace("5", "")
        update.V2Strng = update.V2Strng.replace("6", "")
        update.V2Strng = update.V2Strng.replace("7", "")
        update.V2Strng = update.V2Strng.replace("8", "")
        update.V2Strng = update.V2Strng.replace("9", "")
        update.V2Strng = update.V2Strng.replace("+", "")
        update.V2Strng = update.V2Strng.replace("-", "")
        update.V2Strng = update.V2Strng.replace("*", "")
        update.V2Strng = update.V2Strng.replace("/", "")
        update.save()
        if(update.V2Strng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.V2Strng = update2.V2Strng
            update.save()
        else:
            update.V2Strng = ""
            update.save()
        '''IsNucStrng'''
        update.IsNucStrng = update.IsNucStrng.replace("cos(", "")
        update.IsNucStrng = update.IsNucStrng.replace("sin(", "")
        update.IsNucStrng = update.IsNucStrng.replace("tan(", "")
        update.IsNucStrng = update.IsNucStrng.replace("Pi", "")
        update.IsNucStrng = update.IsNucStrng.replace("Tl", "")
        update.IsNucStrng = update.IsNucStrng.replace("Rl", "")
        update.IsNucStrng = update.IsNucStrng.replace("Tw", "")
        update.IsNucStrng = update.IsNucStrng.replace("Sh", "")
        update.IsNucStrng = update.IsNucStrng.replace("Sl", "")
        update.IsNucStrng = update.IsNucStrng.replace("Rs", "")
        update.IsNucStrng = update.IsNucStrng.replace("Lk", "")
        update.IsNucStrng = update.IsNucStrng.replace("Nuc", "")
        update.IsNucStrng = update.IsNucStrng.replace("Cs", "")
        update.IsNucStrng = update.IsNucStrng.replace("MaxS", "")
        update.IsNucStrng = update.IsNucStrng.replace("V1", "")
        update.IsNucStrng = update.IsNucStrng.replace("V2", "")
        update.IsNucStrng = update.IsNucStrng.replace(")", "")
        update.IsNucStrng = update.IsNucStrng.replace("0", "")
        update.IsNucStrng = update.IsNucStrng.replace("1", "")
        update.IsNucStrng = update.IsNucStrng.replace("2", "")
        update.IsNucStrng = update.IsNucStrng.replace("3", "")
        update.IsNucStrng = update.IsNucStrng.replace("4", "")
        update.IsNucStrng = update.IsNucStrng.replace("5", "")
        update.IsNucStrng = update.IsNucStrng.replace("6", "")
        update.IsNucStrng = update.IsNucStrng.replace("7", "")
        update.IsNucStrng = update.IsNucStrng.replace("8", "")
        update.IsNucStrng = update.IsNucStrng.replace("9", "")
        update.IsNucStrng = update.IsNucStrng.replace("+", "")
        update.IsNucStrng = update.IsNucStrng.replace("-", "")
        update.IsNucStrng = update.IsNucStrng.replace("*", "")
        update.IsNucStrng = update.IsNucStrng.replace("/", "")
        update.save()
        if(update.IsNucStrng == ""):
            key = VDNA.objects.last().Save_Key
            key -= 1
            update2 = VDNA.objects.get(pk=key)
            update.IsNucStrng = update2.IsNucStrng
            update.save()
        else:
            update.IsNucStrng = ""
            update.save()
        VDNA.objects.convert()
    
    def convert(self):
        '''
        This function converts all user inputted strings into evaluate function friendly strings.
        All variables within the strings are swapped with thier corresponding values.
        All mathmatical operations within the strings are swapped with thier python equivalents.
        '''
        Tilt, Roll, Twist = VDNA.objects.last().TiltStrng, VDNA.objects.last().RollStrng, VDNA.objects.last().TwistStrng
        Shift, Slide, Rise = VDNA.objects.last().ShiftStrng, VDNA.objects.last().SlideStrng, VDNA.objects.last().RiseStrng
        MaxS, Lk, Nuc = VDNA.objects.last().sMax, VDNA.objects.last().Lk, VDNA.objects.last().Nuc
        V1, V2, Cores = VDNA.objects.last().V1Strng, VDNA.objects.last().V2Strng, VDNA.objects.last().IsNucStrng
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        key2 = VDNA.objects.last().Save_Key
        key2 -= 3
        Tilt2, Roll2, Twist2 = VDNA.objects.get(pk=key2).TiltStrng, VDNA.objects.get(pk=key2).RollStrng, VDNA.objects.get(pk=key2).TwistStrng
        Shift2, Slide2, Rise2 = VDNA.objects.get(pk=key2).ShiftStrng, VDNA.objects.get(pk=key2).SlideStrng, VDNA.objects.get(pk=key2).RiseStrng
        MaxS2, Lk2, Nuc2 = VDNA.objects.get(pk=key2).sMax, VDNA.objects.get(pk=key2).Lk, VDNA.objects.get(pk=key2).Nuc
        V12, V22, Cores2 = VDNA.objects.get(pk=key2).V1Strng, VDNA.objects.get(pk=key2).V2Strng, VDNA.objects.get(pk=key2).IsNucStrng
        '''Tilt'''
        for i in range(2):
            update.TiltStrng = update.TiltStrng.replace("Tl", Tilt2)
            update.TiltStrng = update.TiltStrng.replace("Rl", Roll)
            update.TiltStrng = update.TiltStrng.replace("Tw", Twist)
            update.TiltStrng = update.TiltStrng.replace("Sh", Shift)
            update.TiltStrng = update.TiltStrng.replace("Sl", Slide)
            update.TiltStrng = update.TiltStrng.replace("Rs", Rise)
            update.TiltStrng = update.TiltStrng.replace("MaxS", MaxS)
            update.TiltStrng = update.TiltStrng.replace("Lk", Lk)
            update.TiltStrng = update.TiltStrng.replace("Nuc", Nuc)
            update.TiltStrng = update.TiltStrng.replace("V1", V1)
            update.TiltStrng = update.TiltStrng.replace("V2", V2)
            update.TiltStrng = update.TiltStrng.replace("Cs", Cores)
            update.save()
        update.TiltStrng = update.TiltStrng.replace("math.cos(", "cos(")
        update.TiltStrng = update.TiltStrng.replace("math.sin(", "sin(")
        update.TiltStrng = update.TiltStrng.replace("math.tan(", "tan(")
        update.TiltStrng = update.TiltStrng.replace("cos(", "math.cos(")
        update.TiltStrng = update.TiltStrng.replace("sin(", "math.sin(")
        update.TiltStrng = update.TiltStrng.replace("tan(", "math.tan(")
        update.TiltStrng = update.TiltStrng.replace("Pi", "math.pi")
        '''Roll'''
        for i in range(2):
            update.RollStrng = update.RollStrng.replace("Tl", Tilt)
            update.RollStrng = update.RollStrng.replace("Rl", Roll2)
            update.RollStrng = update.RollStrng.replace("Tw", Twist)
            update.RollStrng = update.RollStrng.replace("Sh", Shift)
            update.RollStrng = update.RollStrng.replace("Sl", Slide)
            update.RollStrng = update.RollStrng.replace("Rs", Rise)
            update.RollStrng = update.RollStrng.replace("MaxS", MaxS)
            update.RollStrng = update.RollStrng.replace("Lk", Lk)
            update.RollStrng = update.RollStrng.replace("Nuc", Nuc)
            update.RollStrng = update.RollStrng.replace("V1", V1)
            update.RollStrng = update.RollStrng.replace("V2", V2)
            update.RollStrng = update.RollStrng.replace("Cs", Cores)
            update.save()
        update.RollStrng = update.RollStrng.replace("math.cos(", "cos(")
        update.RollStrng = update.RollStrng.replace("math.sin(", "sin(")
        update.RollStrng = update.RollStrng.replace("math.tan(", "tan(")
        update.RollStrng = update.RollStrng.replace("cos(", "math.cos(")
        update.RollStrng = update.RollStrng.replace("sin(", "math.sin(")
        update.RollStrng = update.RollStrng.replace("tan(", "math.tan(")
        update.RollStrng = update.RollStrng.replace("Pi", "math.pi")
        '''Twist'''
        for i in range(2):
            update.TwistStrng = update.TwistStrng.replace("Tl", Tilt)
            update.TwistStrng = update.TwistStrng.replace("Rl", Roll)
            update.TwistStrng = update.TwistStrng.replace("Tw", Twist2)
            update.TwistStrng = update.TwistStrng.replace("Sh", Shift)
            update.TwistStrng = update.TwistStrng.replace("Sl", Slide)
            update.TwistStrng = update.TwistStrng.replace("Rs", Rise)
            update.TwistStrng = update.TwistStrng.replace("MaxS", MaxS)
            update.TwistStrng = update.TwistStrng.replace("Lk", Lk)
            update.TwistStrng = update.TwistStrng.replace("Nuc", Nuc)
            update.TwistStrng = update.TwistStrng.replace("V1", V1)
            update.TwistStrng = update.TwistStrng.replace("V2", V2)
            update.TwistStrng = update.TwistStrng.replace("Cs", Cores)
            update.save()
        update.TwistStrng = update.TwistStrng.replace("math.cos(", "cos(")
        update.TwistStrng = update.TwistStrng.replace("math.sin(", "sin(")
        update.TwistStrng = update.TwistStrng.replace("math.tan(", "tan(")
        update.TwistStrng = update.TwistStrng.replace("cos(", "math.cos(")
        update.TwistStrng = update.TwistStrng.replace("sin(", "math.sin(")
        update.TwistStrng = update.TwistStrng.replace("tan(", "math.tan(")
        update.TwistStrng = update.TwistStrng.replace("Pi", "math.pi")
        '''Shift'''
        for i in range(2):
            update.ShiftStrng = update.ShiftStrng.replace("Tl", Tilt)
            update.ShiftStrng = update.ShiftStrng.replace("Rl", Roll)
            update.ShiftStrng = update.ShiftStrng.replace("Tw", Twist)
            update.ShiftStrng = update.ShiftStrng.replace("Sh", Shift2)
            update.ShiftStrng = update.ShiftStrng.replace("Sl", Slide)
            update.ShiftStrng = update.ShiftStrng.replace("Rs", Rise)
            update.ShiftStrng = update.ShiftStrng.replace("MaxS", MaxS)
            update.ShiftStrng = update.ShiftStrng.replace("Lk", Lk)
            update.ShiftStrng = update.ShiftStrng.replace("Nuc", Nuc)
            update.ShiftStrng = update.ShiftStrng.replace("V1", V1)
            update.ShiftStrng = update.ShiftStrng.replace("V2", V2)
            update.ShiftStrng = update.ShiftStrng.replace("Cs", Cores)
            update.save()
        update.ShiftStrng = update.ShiftStrng.replace("math.cos(", "cos(")
        update.ShiftStrng = update.ShiftStrng.replace("math.sin(", "sin(")
        update.ShiftStrng = update.ShiftStrng.replace("math.tan(", "tan(")
        update.ShiftStrng = update.ShiftStrng.replace("cos(", "math.cos(")
        update.ShiftStrng = update.ShiftStrng.replace("sin(", "math.sin(")
        update.ShiftStrng = update.ShiftStrng.replace("tan(", "math.tan(")
        update.ShiftStrng = update.ShiftStrng.replace("Pi", "math.pi")
        '''Slide'''
        for i in range(2):
            update.SlideStrng = update.SlideStrng.replace("Tl", Tilt)
            update.SlideStrng = update.SlideStrng.replace("Rl", Roll)
            update.SlideStrng = update.SlideStrng.replace("Tw", Twist)
            update.SlideStrng = update.SlideStrng.replace("Sh", Shift)
            update.SlideStrng = update.SlideStrng.replace("Sl", Slide2)
            update.SlideStrng = update.SlideStrng.replace("Rs", Rise)
            update.SlideStrng = update.SlideStrng.replace("MaxS", MaxS)
            update.SlideStrng = update.SlideStrng.replace("Lk", Lk)
            update.SlideStrng = update.SlideStrng.replace("Nuc", Nuc)
            update.SlideStrng = update.SlideStrng.replace("V1", V1)
            update.SlideStrng = update.SlideStrng.replace("V2", V2)
            update.SlideStrng = update.SlideStrng.replace("Cs", Cores)
            update.save()
        update.SlideStrng = update.SlideStrng.replace("math.cos(", "cos(")
        update.SlideStrng = update.SlideStrng.replace("math.sin(", "sin(")
        update.SlideStrng = update.SlideStrng.replace("math.tan(", "tan(")
        update.SlideStrng = update.SlideStrng.replace("cos(", "math.cos(")
        update.SlideStrng = update.SlideStrng.replace("sin(", "math.sin(")
        update.SlideStrng = update.SlideStrng.replace("tan(", "math.tan(")
        update.SlideStrng = update.SlideStrng.replace("Pi", "math.pi")
        '''Rise'''
        for i in range(2):
            update.RiseStrng = update.RiseStrng.replace("Tl", Tilt)
            update.RiseStrng = update.RiseStrng.replace("Rl", Roll)
            update.RiseStrng = update.RiseStrng.replace("Tw", Twist)
            update.RiseStrng = update.RiseStrng.replace("Sh", Shift)
            update.RiseStrng = update.RiseStrng.replace("Sl", Slide)
            update.RiseStrng = update.RiseStrng.replace("Rs", Rise2)
            update.RiseStrng = update.RiseStrng.replace("MaxS", MaxS)
            update.RiseStrng = update.RiseStrng.replace("Lk", Lk)
            update.RiseStrng = update.RiseStrng.replace("Nuc", Nuc)
            update.RiseStrng = update.RiseStrng.replace("V1", V1)
            update.RiseStrng = update.RiseStrng.replace("V2", V2)
            update.RiseStrng = update.RiseStrng.replace("Cs", Cores)
            update.save()
        update.RiseStrng = update.RiseStrng.replace("math.cos(", "cos(")
        update.RiseStrng = update.RiseStrng.replace("math.sin(", "sin(")
        update.RiseStrng = update.RiseStrng.replace("math.tan(", "tan(")
        update.RiseStrng = update.RiseStrng.replace("cos(", "math.cos(")
        update.RiseStrng = update.RiseStrng.replace("sin(", "math.sin(")
        update.RiseStrng = update.RiseStrng.replace("tan(", "math.tan(")
        update.RiseStrng = update.RiseStrng.replace("Pi", "math.pi")
        '''Max S'''
        for i in range(2):
            update.sMax = update.sMax.replace("Tl", Tilt)
            update.sMax = update.sMax.replace("Rl", Roll)
            update.sMax = update.sMax.replace("Tw", Twist)
            update.sMax = update.sMax.replace("Sh", Shift)
            update.sMax = update.sMax.replace("Sl", Slide)
            update.sMax = update.sMax.replace("Rs", Rise)
            update.sMax = update.sMax.replace("MaxS", MaxS2)
            update.sMax = update.sMax.replace("Lk", Lk)
            update.sMax = update.sMax.replace("Nuc", Nuc)
            update.sMax = update.sMax.replace("V1", V1)
            update.sMax = update.sMax.replace("V2", V2)
            update.sMax = update.sMax.replace("Cs", Cores)
            update.save()
        update.sMax = update.sMax.replace("math.cos(", "cos(")
        update.sMax = update.sMax.replace("math.sin(", "sin(")
        update.sMax = update.sMax.replace("math.tan(", "tan(")
        update.sMax = update.sMax.replace("cos(", "math.cos(")
        update.sMax = update.sMax.replace("sin(", "math.sin(")
        update.sMax = update.sMax.replace("tan(", "math.tan(")
        update.sMax = update.sMax.replace("Pi", "math.pi")
        '''Lk'''
        for i in range(2):
            update.Lk = update.Lk.replace("Tl", Tilt)
            update.Lk = update.Lk.replace("Rl", Roll)
            update.Lk = update.Lk.replace("Tw", Twist)
            update.Lk = update.Lk.replace("Sh", Shift)
            update.Lk = update.Lk.replace("Sl", Slide)
            update.Lk = update.Lk.replace("Rs", Rise)
            update.Lk = update.Lk.replace("MaxS", MaxS)
            update.Lk = update.Lk.replace("Lk", Lk2)
            update.Lk = update.Lk.replace("Nuc", Nuc)
            update.Lk = update.Lk.replace("V1", V1)
            update.Lk = update.Lk.replace("V2", V2)
            update.Lk = update.Lk.replace("Cs", Cores)
            update.save()
        update.Lk = update.Lk.replace("math.cos(", "cos(")
        update.Lk = update.Lk.replace("math.sin(", "sin(")
        update.Lk = update.Lk.replace("math.tan(", "tan(")
        update.Lk = update.Lk.replace("cos(", "math.cos(")
        update.Lk = update.Lk.replace("sin(", "math.sin(")
        update.Lk = update.Lk.replace("tan(", "math.tan(")
        update.Lk = update.Lk.replace("Pi", "math.pi")
        '''Nuc'''
        for i in range(2):
            update.Nuc = update.Nuc.replace("Tl", Tilt)
            update.Nuc = update.Nuc.replace("Rl", Roll)
            update.Nuc = update.Nuc.replace("Tw", Twist)
            update.Nuc = update.Nuc.replace("Sh", Shift)
            update.Nuc = update.Nuc.replace("Sl", Slide)
            update.Nuc = update.Nuc.replace("Rs", Rise)
            update.Nuc = update.Nuc.replace("MaxS", MaxS)
            update.Nuc = update.Nuc.replace("Lk", Lk)
            update.Nuc = update.Nuc.replace("Nuc", Nuc2)
            update.Nuc = update.Nuc.replace("V1", V1)
            update.Nuc = update.Nuc.replace("V2", V2)
            update.Nuc = update.Nuc.replace("Cs", Cores)
            update.save()
        update.Nuc = update.Nuc.replace("math.cos(", "cos(")
        update.Nuc = update.Nuc.replace("math.sin(", "sin(")
        update.Nuc = update.Nuc.replace("math.tan(", "tan(")
        update.Nuc = update.Nuc.replace("cos(", "math.cos(")
        update.Nuc = update.Nuc.replace("sin(", "math.sin(")
        update.Nuc = update.Nuc.replace("tan(", "math.tan(")
        update.Nuc = update.Nuc.replace("Pi", "math.pi")
        '''V1'''
        for i in range(2):
            update.V1Strng = update.V1Strng.replace("Tl", Tilt)
            update.V1Strng = update.V1Strng.replace("Rl", Roll)
            update.V1Strng = update.V1Strng.replace("Tw", Twist)
            update.V1Strng = update.V1Strng.replace("Sh", Shift)
            update.V1Strng = update.V1Strng.replace("Sl", Slide)
            update.V1Strng = update.V1Strng.replace("Rs", Rise)
            update.V1Strng = update.V1Strng.replace("MaxS", MaxS)
            update.V1Strng = update.V1Strng.replace("Lk", Lk)
            update.V1Strng = update.V1Strng.replace("Nuc", Nuc)
            update.V1Strng = update.V1Strng.replace("V1", V12)
            update.V1Strng = update.V1Strng.replace("V2", V2)
            update.V1Strng = update.V1Strng.replace("Cs", Cores)
            update.save()
        update.V1Strng = update.V1Strng.replace("math.cos(", "cos(")
        update.V1Strng = update.V1Strng.replace("math.sin(", "sin(")
        update.V1Strng = update.V1Strng.replace("math.tan(", "tan(")
        update.V1Strng = update.V1Strng.replace("cos(", "math.cos(")
        update.V1Strng = update.V1Strng.replace("sin(", "math.sin(")
        update.V1Strng = update.V1Strng.replace("tan(", "math.tan(")
        update.V1Strng = update.V1Strng.replace("Pi", "math.pi")
        '''V2'''
        for i in range(2):
            update.V2Strng = update.V2Strng.replace("Tl", Tilt)
            update.V2Strng = update.V2Strng.replace("Rl", Roll)
            update.V2Strng = update.V2Strng.replace("Tw", Twist)
            update.V2Strng = update.V2Strng.replace("Sh", Shift)
            update.V2Strng = update.V2Strng.replace("Sl", Slide)
            update.V2Strng = update.V2Strng.replace("Rs", Rise)
            update.V2Strng = update.V2Strng.replace("MaxS", MaxS)
            update.V2Strng = update.V2Strng.replace("Lk", Lk)
            update.V2Strng = update.V2Strng.replace("Nuc", Nuc)
            update.V2Strng = update.V2Strng.replace("V1", V1)
            update.V2Strng = update.V2Strng.replace("V2", V22)
            update.V2Strng = update.V2Strng.replace("Cs", Cores)
            update.save()
        update.V2Strng = update.V2Strng.replace("math.cos(", "cos(")
        update.V2Strng = update.V2Strng.replace("math.sin(", "sin(")
        update.V2Strng = update.V2Strng.replace("math.tan(", "tan(")
        update.V2Strng = update.V2Strng.replace("cos(", "math.cos(")
        update.V2Strng = update.V2Strng.replace("sin(", "math.sin(")
        update.V2Strng = update.V2Strng.replace("tan(", "math.tan(")
        update.V2Strng = update.V2Strng.replace("Pi", "math.pi")
        '''Cores'''
        for i in range(2):
            update.IsNucStrng = update.IsNucStrng.replace("Tl", Tilt)
            update.IsNucStrng = update.IsNucStrng.replace("Rl", Roll)
            update.IsNucStrng = update.IsNucStrng.replace("Tw", Twist)
            update.IsNucStrng = update.IsNucStrng.replace("Sh", Shift)
            update.IsNucStrng = update.IsNucStrng.replace("Sl", Slide)
            update.IsNucStrng = update.IsNucStrng.replace("Rs", Rise)
            update.IsNucStrng = update.IsNucStrng.replace("MaxS", MaxS)
            update.IsNucStrng = update.IsNucStrng.replace("Lk", Lk)
            update.IsNucStrng = update.IsNucStrng.replace("Nuc", Nuc)
            update.IsNucStrng = update.IsNucStrng.replace("V1", V1)
            update.IsNucStrng = update.IsNucStrng.replace("V2", V2)
            update.IsNucStrng = update.IsNucStrng.replace("Cs", Cores2)
            update.save()
        update.IsNucStrng = update.IsNucStrng.replace("math.cos(", "cos(")
        update.IsNucStrng = update.IsNucStrng.replace("math.sin(", "sin(")
        update.IsNucStrng = update.IsNucStrng.replace("math.tan(", "tan(")
        update.IsNucStrng = update.IsNucStrng.replace("cos(", "math.cos(")
        update.IsNucStrng = update.IsNucStrng.replace("sin(", "math.sin(")
        update.IsNucStrng = update.IsNucStrng.replace("tan(", "math.tan(")
        update.IsNucStrng = update.IsNucStrng.replace("Pi", "math.pi")
        ###########################################################################
        update.save()
        VDNA.objects.revise()

    def revise(self):
        '''This function ensures that all variables have been filtered out of the user inputted strings.'''
        Tilt, Roll, Twist = VDNA.objects.last().TiltStrng, VDNA.objects.last().RollStrng, VDNA.objects.last().TwistStrng
        Shift, Slide, Rise = VDNA.objects.last().ShiftStrng, VDNA.objects.last().SlideStrng, VDNA.objects.last().RiseStrng
        MaxS, Lk, Nuc = VDNA.objects.last().sMax, VDNA.objects.last().Lk, VDNA.objects.last().Nuc
        V1, V2, Cores = VDNA.objects.last().V1Strng, VDNA.objects.last().V2Strng, VDNA.objects.last().IsNucStrng
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        Tl, Rl, Tw, Sh, Sl, Rs, Ms, L, Nc, V_1, V_2, Cs= "Tl", "Rl", "Tw", "Sh", "Sl", "Rs", "MaxS", "Lk", "Nuc", "V1", "V2", "Cs"
        '''Tilt'''
        for i in range(2):
            if(Tilt.count(Rl) >= 1):
                Tilt = Tilt.replace("Rl", Roll)
                update.save()
            if(Tilt.count(Tw) >= 1):
                Tilt = Tilt.replace("Tw", Twist)
                update.save()
            if(Tilt.count(Sh) >= 1):
                Tilt = Tilt.replace("Sh", Shift)
                update.save()
            if(Tilt.count(Sl) >= 1):
                Tilt = Tilt.replace("Sl", Slide)
                update.save()
            if(Tilt.count(Rs) >= 1):
                Tilt = Tilt.replace("Rs", Rise)
                update.save()
            if(Tilt.count(Ms) >= 1):
                Tilt = Tilt.replace("MaxS", MaxS)
                update.save()
            if(Tilt.count(L) >= 1):
                Tilt = Tilt.replace("Lk", Lk)
                update.save()
            if(Tilt.count(Nc) >= 1):
                Tilt = Tilt.replace("Nuc", Nuc)
                update.save()
            if(Tilt.count(V_1) >= 1):
                Tilt = Tilt.replace("V1", V1)
                update.save()
            if(Tilt.count(V_2) >= 1):
                Tilt = Tilt.replace("V2", V2)
                update.save()
            if(Tilt.count(Cs) >= 1):
                Tilt = Tilt.replace("Cs", Cores)
                update.save()
        '''Roll'''
        for i in range(2):
            if(Roll.count(Tl) >= 1):
                Roll = Roll.replace("Tl", Tilt)
                update.save()
            if(Roll.count(Tw) >= 1):
                Roll = Roll.replace("Tw", Twist)
                update.save()
            if(Roll.count(Sh) >= 1):
                Roll = Roll.replace("Sh", Shift)
                update.save()
            if(Roll.count(Sl) >= 1):
                Roll = Roll.replace("Sl", Slide)
                update.save()
            if(Roll.count(Rs) >= 1):
                Roll = Roll.replace("Rs", Rise)
                update.save()
            if(Roll.count(Ms) >= 1):
                Roll = Roll.replace("MaxS", MaxS)
                update.save()
            if(Roll.count(L) >= 1):
                Roll = Roll.replace("Lk", Lk)
                update.save()
            if(Roll.count(Nc) >= 1):
                Roll = Roll.replace("Nuc", Nuc)
                update.save()
            if(Roll.count(V_1) >= 1):
                Roll = Roll.replace("V1", V1)
                update.save()
            if(Roll.count(V_2) >= 1):
                Roll = Roll.replace("V2", V2)
                update.save()
            if(Roll.count(Cs) >= 1):
                Roll = Roll.replace("Cs", Cores)
                update.save()
        '''Twist'''
        for i in range(2):
            if(Twist.count(Tl) >= 1):
                Twist = Twist.replace("Tl", Tilt)
                update.save()
            if(Twist.count(Rl) >= 1):
                Twist = Twist.replace("Rl", Roll)
                update.save()
            if(Twist.count(Sh) >= 1):
                Twist = Twist.replace("Sh", Shift)
                update.save()
            if(Twist.count(Sl) >= 1):
                Twist = Twist.replace("Sl", Slide)
                update.save()
            if(Twist.count(Rs) >= 1):
                Twist = Twist.replace("Rs", Rise)
                update.save()
            if(Twist.count(Ms) >= 1):
                Twist = Twist.replace("MaxS", MaxS)
                update.save()
            if(Twist.count(L) >= 1):
                Twist = Twist.replace("Lk", Lk)
                update.save()
            if(Twist.count(Nc) >= 1):
                Twist = Twist.replace("Nuc", Nuc)
                update.save()
            if(Twist.count(V_1) >= 1):
                Twist = Twist.replace("V1", V1)
                update.save()
            if(Twist.count(V_2) >= 1):
                Twist = Twist.replace("V2", V2)
                update.save()
            if(Twist.count(Cs) >= 1):
                Twist = Twist.replace("Cs", Cores)
                update.save()
        '''Shift'''
        for i in range(2):
            if(Shift.count(Tl) >= 1):
                Shift = Shift.replace("Tl", Tilt)
                update.save()
            if(Shift.count(Rl) >= 1):
                Shift = Shift.replace("Rl", Roll)
                update.save()
            if(Shift.count(Tw) >= 1):
                Shift = Shift.replace("Tw", Twist)
                update.save()
            if(Shift.count(Sl) >= 1):
                Shift = Shift.replace("Sl", Slide)
                update.save()
            if(Shift.count(Rs) >= 1):
                Shift = Shift.replace("Rs", Rise)
                update.save()
            if(Shift.count(Ms) >= 1):
                Shift = Shift.replace("MaxS", MaxS)
                update.save()
            if(Shift.count(L) >= 1):
                Shift = Shift.replace("Lk", Lk)
                update.save()
            if(Shift.count(Nc) >= 1):
                Shift = Shift.replace("Nuc", Nuc)
                update.save()
            if(Shift.count(V_1) >= 1):
                Shift = Shift.replace("V1", V1)
                update.save()
            if(Shift.count(V_2) >= 1):
                Shift = Shift.replace("V2", V2)
                update.save()
            if(Shift.count(Cs) >= 1):
                Shift = Shift.replace("Cs", Cores)
                update.save()
        '''Slide'''
        for i in range(2):
            if(Slide.count(Tl) >= 1):
                Slide = Slide.replace("Tl", Tilt)
                update.save()
            if(Slide.count(Rl) >= 1):
                Slide = Slide.replace("Rl", Roll)
                update.save()
            if(Slide.count(Tw) >= 1):
                Slide = Slide.replace("Tw", Twist)
                update.save()
            if(Slide.count(Sh) >= 1):
                Slide = Slide.replace("Sh", Shift)
                update.save()
            if(Slide.count(Rs) >= 1):
                Slide = Slide.replace("Rs", Rise)
                update.save()
            if(Slide.count(Ms) >= 1):
                Slide = Slide.replace("MaxS", MaxS)
                update.save()
            if(Slide.count(L) >= 1):
                Slide = Slide.replace("Lk", Lk)
                update.save()
            if(Slide.count(Nc) >= 1):
                Slide = Slide.replace("Nuc", Nuc)
                update.save()
            if(Slide.count(V_1) >= 1):
                Slide = Slide.replace("V1", V1)
                update.save()
            if(Slide.count(V_2) >= 1):
                Slide = Slide.replace("V2", V2)
                update.save()
            if(Slide.count(Cs) >= 1):
                Slide = Slide.replace("Cs", Cores)
                update.save()
        '''Rise'''
        for i in range(2):
            if(Rise.count(Tl) >= 1):
                Rise = Rise.replace("Tl", Tilt)
                update.save()
            if(Rise.count(Rl) >= 1):
                Rise = Rise.replace("Rl", Roll)
                update.save()
            if(Rise.count(Tw) >= 1):
                Rise = Rise.replace("Tw", Twist)
                update.save()
            if(Rise.count(Sh) >= 1):
                Rise = Rise.replace("Sh", Shift)
                update.save()
            if(Rise.count(Sl) >= 1):
                Rise = Rise.replace("Sl", Slide)
                update.save()
            if(Rise.count(Ms) >= 1):
                Rise = Rise.replace("MaxS", MaxS)
                update.save()
            if(Rise.count(L) >= 1):
                Rise = Rise.replace("Lk", Lk)
                update.save()
            if(Rise.count(Nc) >= 1):
                Rise = Rise.replace("Nuc", Nuc)
                update.save()
            if(Rise.count(V_1) >= 1):
                Rise = Rise.replace("V1", V1)
                update.save()
            if(Rise.count(V_2) >= 1):
                Rise = Rise.replace("V2", V2)
                update.save()
            if(Rise.count(Cs) >= 1):
                Rise = Rise.replace("Cs", Cores)
                update.save()
        '''Max S'''
        for i in range(2):
            if(MaxS.count(Tl) >= 1):
                MaxS = MaxS.replace("Tl", Tilt)
                update.save()
            if(MaxS.count(Rl) >= 1):
                MaxS = MaxS.replace("Rl", Roll)
                update.save()
            if(MaxS.count(Tw) >= 1):
                MaxS = MaxS.replace("Tw", Twist)
                update.save()
            if(MaxS.count(Sh) >= 1):
                MaxS = MaxS.replace("Sh", Shift)
                update.save()
            if(MaxS.count(Sl) >= 1):
                MaxS = MaxS.replace("Sl", Slide)
                update.save()
            if(MaxS.count(Rs) >= 1):
                MaxS = MaxS.replace("Rs", Rise)
                update.save()
            if(MaxS.count(L) >= 1):
                MaxS = MaxS.replace("Lk", Lk)
                update.save()
            if(MaxS.count(Nc) >= 1):
                MaxS = MaxS.replace("Nuc", Nuc)
                update.save()
            if(MaxS.count(V_1) >= 1):
                MaxS = MaxS.replace("V1", V1)
                update.save()
            if(MaxS.count(V_2) >= 1):
                MaxS = MaxS.replace("V2", V2)
                update.save()
            if(MaxS.count(Cs) >= 1):
                MaxS = MaxS.replace("Cs", Cores)
                update.save()
        '''Lk'''
        for i in range(2):
            if(Lk.count(Tl) >= 1):
                Lk = Lk.replace("Tl", Tilt)
                update.save()
            if(Lk.count(Rl) >= 1):
                Lk = Lk.replace("Rl", Roll)
                update.save()
            if(Lk.count(Tw) >= 1):
                Lk = Lk.replace("Tw", Twist)
                update.save()
            if(Lk.count(Sh) >= 1):
                Lk = Lk.replace("Sh", Shift)
                update.save()
            if(Lk.count(Sl) >= 1):
                Lk = Lk.replace("Sl", Slide)
                update.save()
            if(Lk.count(Rs) >= 1):
                Lk = Lk.replace("Rs", Rise)
                update.save()
            if(Lk.count(Ms) >= 1):
                Lk = Lk.replace("MaxS", MaxS)
                update.save()
            if(Lk.count(Nc) >= 1):
                Lk = Lk.replace("Nuc", Nuc)
                update.save()
            if(Lk.count(V_1) >= 1):
                Lk = Lk.replace("V1", V1)
                update.save()
            if(Lk.count(V_2) >= 1):
                Lk = Lk.replace("V2", V2)
                update.save()
            if(Lk.count(Cs) >= 1):
                Lk = Lk.replace("Cs", Cores)
                update.save()
        '''Nuc'''
        for i in range(2):
            if(Nuc.count(Tl) >= 1):
                Nuc = Nuc.replace("Tl", Tilt)
                update.save()
            if(Nuc.count(Rl) >= 1):
                Nuc = Nuc.replace("Rl", Roll)
                update.save()
            if(Nuc.count(Tw) >= 1):
                Nuc = Nuc.replace("Tw", Twist)
                update.save()
            if(Nuc.count(Sh) >= 1):
                Nuc = Nuc.replace("Sh", Shift)
                update.save()
            if(Nuc.count(Sl) >= 1):
                Nuc = Nuc.replace("Sl", Slide)
                update.save()
            if(Nuc.count(Rs) >= 1):
                Nuc = Nuc.replace("Rs", Rise)
                update.save()
            if(Nuc.count(Ms) >= 1):
                Nuc = Nuc.replace("MaxS", MaxS)
                update.save()
            if(Nuc.count(L) >= 1):
                Nuc = Nuc.replace("Lk", Lk)
                update.save()
            if(Nuc.count(V_1) >= 1):
                Nuc = Nuc.replace("V1", V1)
                update.save()
            if(Nuc.count(V_2) >= 1):
                Nuc = Nuc.replace("V2", V2)
                update.save()
            if(Nuc.count(Cs) >= 1):
                Nuc = Nuc.replace("Cs", Cores)
                update.save()
        '''V1'''
        for i in range(2):
            if(V1.count(Tl) >= 1):
                V1 = V1.replace("Tl", Tilt)
                update.save()
            if(V1.count(Rl) >= 1):
                V1 = V1.replace("Rl", Roll)
                update.save()
            if(V1.count(Tw) >= 1):
                V1 = V1.replace("Tw", Twist)
                update.save()
            if(V1.count(Sh) >= 1):
                V1 = V1.replace("Sh", Shift)
                update.save()
            if(V1.count(Sl) >= 1):
                V1 = V1.replace("Sl", Slide)
                update.save()
            if(V1.count(Rs) >= 1):
                V1 = V1.replace("Rs", Rise)
                update.save()
            if(V1.count(Ms) >= 1):
                V1 = V1.replace("MaxS", MaxS)
                update.save()
            if(V1.count(L) >= 1):
                V1 = V1.replace("Lk", Lk)
                update.save()
            if(V1.count(Nc) >= 1):
                V1 = V1.replace("Nuc", Nuc)
                update.save()
            if(V1.count(V_2) >= 1):
                V1 = V1.replace("V2", V2)
                update.save()
            if(V1.count(Cs) >= 1):
                V1 = V1.replace("Cs", Cores)
                update.save()
        '''V2'''
        for i in range(2):
            if(V2.count(Tl) >= 1):
                V2 = V2.replace("Tl", Tilt)
                update.save()
            if(V2.count(Rl) >= 1):
                V2 = V2.replace("Rl", Roll)
                update.save()
            if(V2.count(Tw) >= 1):
                V2 = V2.replace("Tw", Twist)
                update.save()
            if(V2.count(Sh) >= 1):
                V2 = V2.replace("Sh", Shift)
                update.save()
            if(V2.count(Sl) >= 1):
                V2 = V2.replace("Sl", Slide)
                update.save()
            if(V2.count(Rs) >= 1):
                V2 = V2.replace("Rs", Rise)
                update.save()
            if(V2.count(Ms) >= 1):
                V2 = V2.replace("MaxS", MaxS)
                update.save()
            if(V2.count(L) >= 1):
                V2 = V2.replace("Lk", Lk)
                update.save()
            if(V2.count(Nc) >= 1):
                V2 = V2.replace("Nuc", Nuc)
                update.save()
            if(V2.count(V_1) >= 1):
                V2 = V2.replace("V1", V1)
                update.save()
            if(V2.count(Cs) >= 1):
                V2 = V2.replace("Cs", Cores)
                update.save()
        '''Cores'''
        for i in range(2):
            if(Cores.count(Tl) >= 1):
                Cores = Cores.replace("Tl", Tilt)
                update.save()
            if(Cores.count(Rl) >= 1):
                Cores = Cores.replace("Rl", Roll)
                update.save()
            if(Cores.count(Tw) >= 1):
                Cores = Cores.replace("Tw", Twist)
                update.save()
            if(Cores.count(Sh) >= 1):
                Cores = Cores.replace("Sh", Shift)
                update.save()
            if(Cores.count(Sl) >= 1):
                Cores = Cores.replace("Sl", Slide)
                update.save()
            if(Cores.count(Rs) >= 1):
                Cores = Cores.replace("Rs", Rise)
                update.save()
            if(Cores.count(Ms) >= 1):
                Cores = Cores.replace("MaxS", MaxS)
                update.save()
            if(Cores.count(L) >= 1):
                Cores = Cores.replace("Lk", Lk)
                update.save()
            if(Cores.count(Nc) >= 1):
                Cores = Cores.replace("Nuc", Nuc)
                update.save()
            if(Cores.count(V_1) >= 1):
                Cores = Cores.replace("V1", V1)
                update.save()
            if(Cores.count(V_2) >= 1):
                Cores = Cores.replace("V2", V2)
                update.save()
        VDNA.objects.evaluate()

    def evaluate(self):
        '''
        This function executes the strings as python code.
        Because of the execution, the user inputted strings are converted into ints.
        Thus, becuase of necessity of storing back in the model, the user inputs are reverted back to strings.
        '''
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        if(VDNA.objects.last().TiltStrng != ""):
            Tilt = eval(VDNA.objects.last().TiltStrng)
            Tilt = float(Tilt)
            Tilt = round(Tilt, 3)
            update.TiltStrng = str(Tilt)
        if(VDNA.objects.last().RollStrng != ""):
            Roll = eval(VDNA.objects.last().RollStrng)
            Roll = float(Roll)
            Roll = round(Roll, 3)
            update.RollStrng = str(Roll)
        if(VDNA.objects.last().TwistStrng != ""):
            Twist = eval(VDNA.objects.last().TwistStrng)
            Twist = float(Twist)
            Twist = round(Twist, 3)
            update.TwistStrng = str(Twist)
        if(VDNA.objects.last().ShiftStrng != ""):
            Shift = eval(VDNA.objects.last().ShiftStrng)
            Shift = float(Shift)
            Shift = round(Shift, 3)
            update.ShiftStrng = str(Shift)
        if(VDNA.objects.last().SlideStrng != ""):
            Slide = eval(VDNA.objects.last().SlideStrng)
            Slide = float(Slide)
            Slide = round(Slide, 3)
            update.SlideStrng = str(Slide)
        if(VDNA.objects.last().RiseStrng != ""):
            Rise = eval(VDNA.objects.last().RiseStrng)
            Rise = float(Rise)
            Rise = round(Rise, 3)
            update.RiseStrng = str(Rise)
        if(VDNA.objects.last().sMax != ""):
            sMax = eval(VDNA.objects.last().sMax)
            sMax = float(sMax)
            sMax = round(sMax, 3)
            update.sMax = str(sMax)
        if(VDNA.objects.last().Lk != ""):
            Lk = eval(VDNA.objects.last().Lk)
            Lk = float(Lk)
            Lk = round(Lk, 3)
            update.Lk = str(Lk)
        if(VDNA.objects.last().Nuc != ""):
            Nuc = eval(VDNA.objects.last().Nuc)
            Nuc = float(Nuc)
            Nuc = round(Nuc, 3)
            update.Nuc = str(Nuc)
        if(VDNA.objects.last().V1Strng != ""):
            V1 = eval(VDNA.objects.last().V1Strng)
            V1 = float(V1)
            V1 = round(V1, 3)
            update.V1Strng = str(V1)
        if(VDNA.objects.last().V2Strng != ""):
            V2 = eval(VDNA.objects.last().V2Strng)
            V2 = float(V2)
            V2 = round(V2, 3)
            update.V2Strng = str(V2)
        if(VDNA.objects.last().IsNucStrng != ""):
            Cores = eval(VDNA.objects.last().IsNucStrng)
            Cores = float(Cores)
            Cores = round(Cores, 3)
            update.IsNucStrng = str(Cores)
        update.save()

    def integrate(self):
        pi = np.pi / 180
        Tilt, Roll, Twist = float(VDNA.objects.last().ShiftStrng), float(VDNA.objects.last().SlideStrng), float(VDNA.objects.last().RiseStrng)
        Shift, Slide, Rise = float(VDNA.objects.last().ShiftStrng), float(VDNA.objects.last().SlideStrng), float(VDNA.objects.last().RiseStrng)
        til = Tilt * pi
        rol = Roll * pi
        twi = Twist * pi
        r = np.zeros((3, 1))
        D = np.array([[Shift], [Slide], [Rise]])
        bend = np.sqrt(til * til + rol * rol)
        if (bend == 0):
            phi = 0.0
        elif (rol == 0):
            phi = np.pi / 2
        elif (rol < 0):
            phi = np.arctan(til / rol) + np.pi
        else:
            phi = np.arctan(til / rol)
        theta = twi * 0.5 - phi
        RZ1 = np.array([[np.cos(theta), -np.sin(theta), 0.], [np.sin(theta), np.cos(theta), 0.], [0., 0., 1.]])
        y_theta = bend * 0.5
        z_theta = phi
        Ry = np.array([[np.cos(y_theta), 0., np.sin(y_theta)], [0., 1., 0.], [-np.sin(y_theta), 0., np.cos(y_theta)]])
        Rz = np.array([[np.cos(z_theta), -np.sin(z_theta), 0.], [np.sin(z_theta), np.cos(z_theta), 0.], [0., 0., 1.]])
        Tmst = np.dot(RZ1, np.dot(Ry, Rz))
        y_theta = bend
        z_theta = twi * 0.5 + phi
        Ry = np.array([[np.cos(y_theta), 0., np.sin(y_theta)], [0., 1., 0.], [-np.sin(y_theta), 0., np.cos(y_theta)]])
        Rz = np.array([[np.cos(z_theta), -np.sin(z_theta), 0.], [np.sin(z_theta), np.cos(z_theta), 0.], [0., 0., 1.]])
        Ti = np.dot(RZ1, np.dot(Ry, Rz))
        r = r + np.dot(Tmst, D)
        R = r.T.reshape(3)
        D = Ti.T
        #rd = RD(r.T.reshape(3), Ti.T)

    '''def test(self):
        Sh, Sl, Rs = float(VDNA.objects.last().ShiftStrng), float(VDNA.objects.last().SlideStrng), float(VDNA.objects.last().RiseStrng)
        Tl, Rl, Tw = float(VDNA.objects.last().TiltStrng), float(VDNA.objects.last().RollStrng), float(VDNA.objects.last().TwistStrng)
        HP_inter(Sh, Sl, Rs, Tl, Rl, Tw)
        result = HP2RD()'''

    '''def straight_twisted_line(Rise, Twist, step_number):
        """
        Given Rise, Twist, and number of steps, return a list of HPs.
        """
        hps = [HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(0.0, 0.0, 0.0, 0.0, 0.0, 0.0))]
        for i in range(step_number):
            hps.append(HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(0.0, 0.0, Rise, 0.0, 0.0, Twist)))
        return hps


    def circular_DNA(Rise, V1, V2, step_number, step_size=1.0, phase=0):
        hps = [HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(0.0, 0.0, 0.0, 0.0, 0.0, 0.0))]
        V1 = V1 / step_size
        Rise = Rise * step_size
        Twist = 360.0 * V2 / V1
        for s in range(step_number):
            s = s + phase
            Tilt = np.sin(Twist * s * np.pi / 180.0) * 360.0 / V1
            Roll = np.cos(Twist * s * np.pi / 180.0) * 360.0 / V1
            hps.append(HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(0.0, 0.0, Rise, Tilt, Roll, Twist)))
        return hps


    def helix_torsion(Rise, Twist, V1, V2, step_number, step_size=1.0, phase=0):
        hps = [HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(0.0, 0.0, 0.0, 0.0, 0.0, 0.0))]
        V1 = V1 / step_size
        Twist = Twist * step_size
        Rise = Rise * step_size
        V2 = V2 * step_size
        for s in range(step_number):
            s = s + phase
            Tilt = np.sin((Twist + V2) * s * np.pi / 180.0) * 360.0 / V1
            Roll = np.cos((Twist + V2) * s * np.pi / 180.0) * 360.0 / V1
            hps.append(HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(0.0, 0.0, Rise, Tilt, Roll, Twist)))
        return hps


    def helix_shear(Rise, Twist, V1, V2, step_number, step_size=1.0, phase=0):
        hps = [HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(0.0, 0.0, 0.0, 0.0, 0.0, 0.0))]
        V1 = V1 / step_size
        Twist = Twist * step_size
        Rise = Rise * step_size
        V2 = V2 * step_size
        for s in range(step_number):
            s = s + phase
            Tilt = np.sin(Twist * s * np.pi / 180.0) * 360.0 / V1
            Roll = np.cos(Twist * s * np.pi / 180.0) * 360.0 / V1
            Shift = V2 * np.sin(Twist * s * np.pi / 180)
            Slide = V2 * np.cos(Twist * s * np.pi / 180)
            hps.append(HP(HP_intra(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), HP_inter(Shift, Slide, Rise, Tilt, Roll, Twist)))
        return hps


    def circular_DNA_RD(Rise, V1, V2, step_number, step_size=1.0):
        Rise = Rise * step_size
        V1 = V1 / step_size
        Radius = (Rise / 2) / np.sin(np.pi / V1)
        Twist = 2 * np.pi * V2 / V1
        rd = []
        for s in range(step_number):
            r = np.array([-Radius * np.cos(s * 2 * np.pi / V1), 0, Radius * np.sin(s * 2 * np.pi / V1)]) + np.array([Radius, 0, 0])
            d = np.dot(np.array([[np.cos(Twist * s), -np.sin(Twist * s), 0], [np.sin(Twist * s), np.cos(Twist * s), 0], [0, 0, 1]]).T, np.array(
                [[np.cos(s * 2 * np.pi / V1), 0, -np.sin(s * 2 * np.pi / V1)], [0, 1, 0], [np.sin(s * 2 * np.pi / V1), 0, np.cos(s * 2 * np.pi / V1)]]))
            rd.append(RD(r, d))
        return rd


    def helix_torsion_RD(Rise, Twist, V1, V2, step_number, step_size):
        V1 = V1 / step_size
        V2 = V2 * step_size
        Rise = Rise * step_size
        Twist = Twist * step_size * np.pi / 180
        Radius = np.sqrt(Rise**2 / (4 * (np.sin(np.pi / V1)) ** 2 + (np.tan(V2 * np.pi / 180))**2))
        h = Radius * np.tan(V2 * np.pi / 180)
        rd = []
        for s in range(step_number):
            r = np.array([-Radius * np.cos(s * 2 * np.pi / V1), h * s, Radius * np.sin(s * 2 * np.pi / V1)]) + np.array([Radius, 0, 0])
            tor = V2 * np.pi / 180
            phi = np.arctan(h / (np.sqrt(Rise**2 - h**2) * np.cos(np.pi / V1)))
            X = np.array([[1, 0, 0], [0, np.cos(phi), -np.sin(phi)], [0, np.sin(phi), np.cos(phi)]])
            Y = np.array([[np.cos(s * 2 * np.pi / V1), 0, -np.sin(s * 2 * np.pi / V1)], [0, 1, 0], [np.sin(s * 2 * np.pi / V1), 0, np.cos(s * 2 * np.pi / V1)]])
            Z = np.array([[np.cos((Twist - tor) * s), -np.sin((Twist - tor) * s), 0], [np.sin((Twist - tor) * s), np.cos((Twist - tor) * s), 0], [0, 0, 1]])
            d = np.dot(Z.T, np.dot(X, Y))
            rd.append(RD(r, d))
        return rd


    def helix_shear_RD(Rise, Twist, V1, V2, step_number, step_size):
        V1 = V1 / step_size
        V2 = V2 * step_size
        Rise = Rise * step_size
        Twist = Twist * step_size * np.pi / 180
        Radius = (np.sqrt(Rise**2 - V2**2) / 2) / np.sin(np.pi / V1)
        rd = []
        for s in range(step_number):
            r = np.array([-Radius * np.cos(s * 2 * np.pi / V1), s * V2, Radius * np.sin(s * 2 * np.pi / V1)]) + np.array([Radius, 0, 0])
            phi = np.arctan(V2 / (np.sqrt(Rise**2 - V2**2) * np.cos(np.pi / V1)))
            X = np.array([[1, 0, 0], [0, np.cos(phi), -np.sin(phi)], [0, np.sin(phi), np.cos(phi)]])
            Y = np.array([[np.cos(s * 2 * np.pi / V1), 0, -np.sin(s * 2 * np.pi / V1)], [0, 1, 0], [np.sin(s * 2 * np.pi / V1), 0, np.cos(s * 2 * np.pi / V1)]])
            Z = np.array([[np.cos(Twist * s), -np.sin(Twist * s), 0], [np.sin(Twist * s), np.cos(Twist * s), 0], [0, 0, 1]])
            d = np.dot(Z.T, np.dot(X, Y))
            rd.append(RD(r, d))
        return rd'''

class VDNA(models.Model):
    Save_Key = models.AutoField(primary_key=True, verbose_name='Save Key:')
    TiltStrng = models.CharField(max_length=1000, verbose_name='Tilt (Tl):')
    RollStrng = models.CharField(max_length=1000, verbose_name='Roll (Rl):')
    TwistStrng = models.CharField(max_length=1000, verbose_name='Twist (Tw):')
    ShiftStrng = models.CharField(max_length=1000, verbose_name='Shift (Sh):')
    SlideStrng = models.CharField(max_length=1000, verbose_name='Slide (Sl):')
    RiseStrng = models.CharField(max_length=1000, verbose_name='Rise (Rs):')
    sMax = models.CharField(max_length=1000, verbose_name='Max S (MaxS):')
    Lk = models.CharField(max_length=1000, verbose_name='Lk (Lk):')
    Nuc = models.CharField(max_length=1000, verbose_name='Nuc (Nuc):')
    V1Strng = models.CharField(max_length=1000, verbose_name='V1 (V1):')
    V2Strng = models.CharField(max_length=1000, verbose_name='V2 (V2):')
    IsNucStrng = models.CharField(max_length=1000, verbose_name='Cores (Cs):')
    Geometry = models.CharField(max_length=17, default='Default')
    objects = vdnaManager()

    def __str__(self):
        return self.title