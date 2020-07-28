from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from VDNA.models import VDNA
from django.forms import modelformset_factory

def VDNA_views(context, request):
    '''### VDNA CONTROL PANEL ##################################################'''
    ### Paramter Forms ############################################################
    vdnaParameterFormSet = modelformset_factory(VDNA, exclude = ['Geometry'])
    if(request.method == 'POST' and 'parameter_form' in request.POST):
        formset = vdnaParameterFormSet(request.POST, queryset=VDNA.objects.all())
        if(formset.is_valid()):
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            VDNA.objects.validate()
    else:
        formset = vdnaParameterFormSet(queryset=VDNA.objects.none())

    ### Preset Buttons ############################################################
    if(request.method == 'POST' and 'Reset_All' in request.POST):
        VDNA.objects.Default()
    if(request.method == 'POST' and 'Straight' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Straight"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Bend(Roll)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Bend(Roll)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Bend(Tilt)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Bend(Tilt)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Tilt-a-gon' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Tilt-a-gon"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Roll-a-gon' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Roll-a-gon"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'RollTilt-a-gon' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "RollTilt-a-gon"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Shear(Shift)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Shear(Shift)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Shear(Slide)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Shear(Slide)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Twist(DNA)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Twist(DNA)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Untwisted DNA' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Untwisted DNA"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Circle(Roll)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Circle(Roll)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Circle(Tilt)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Circle(Tilt)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Circular DNA' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Circular DNA"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Torsion Helix(+)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Torsion Helix(+)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Torsion Helix(-)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Torsion Helix(-)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Shear Helix(+)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Shear Helix(+)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Shear Helix(-)' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Shear Helix(-)"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Thermal' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Thermal"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Trajectory' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Trajectory"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Chromatin1' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Chromatin1"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Chromatin2' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Chromatin2"
        update.save()
        VDNA.objects.setVars()
    if(request.method == 'POST' and 'Default' in request.POST):
        key = VDNA.objects.last().Save_Key
        update = VDNA.objects.get(pk=key)
        update.Geometry = "Default"
        update.save()
        VDNA.objects.setVars()

    ### Error Messages ############################################################
    '''SaveKey, Geometry = VDNA.objects.last().Save_Key, VDNA.objects.last().Geometry
    Tilt, Roll, Twist = VDNA.objects.last().TiltStrng, VDNA.objects.last().RollStrng, VDNA.objects.last().TwistStrng
    Shift, Slide, Rise = VDNA.objects.last().ShiftStrng, VDNA.objects.last().SlideStrng, VDNA.objects.last().RiseStrng
    MaxS, Lk, Nuc = VDNA.objects.last().sMax, VDNA.objects.last().Lk, VDNA.objects.last().Nuc
    V1, V2, Cores = VDNA.objects.last().V1Strng, VDNA.objects.last().V2Strng, VDNA.objects.last().IsNucStrng'''
    SaveKey = VDNA.objects.last().Save_Key
    Tilt = VDNA.objects.last().TiltStrng
    Roll = VDNA.objects.last().RollStrng
    Twist = VDNA.objects.last().TwistStrng
    Shift = VDNA.objects.last().ShiftStrng
    Slide = VDNA.objects.last().SlideStrng
    Rise = VDNA.objects.last().RiseStrng
    MaxS = VDNA.objects.last().sMax
    Lk = VDNA.objects.last().Lk
    Nuc = VDNA.objects.last().Nuc
    V1 = VDNA.objects.last().V1Strng
    V2 = VDNA.objects.last().V2Strng
    Cores = VDNA.objects.last().IsNucStrng
    Geometry = VDNA.objects.last().Geometry
    Tilt_E, Roll_E, Twist_E, Shift_E, Slide_E, Rise_E, MaxS_E, Lk_E, Nuc_E, V1Strng_E, V2Strng_E, Cores_E = "", "", "", "", "", "", "", "", "", "", "", ""
    if(Tilt == "" or Roll == "" or Twist == "" or Shift == "" or Slide == "" or Rise == "" or MaxS == "" or Lk == "" or Nuc == "" or V1 == "" or V2 == "" or Cores == ""):
        Errors = "Invalid Characters in Submission: "
    if(Tilt != "" and Roll != "" and Twist != "" and Shift != "" != Slide != "" != Rise != "" and MaxS != "" and Lk != "" and Nuc != "" and V1 != "" and V2 != ""):
        Errors = "Invalid Characters in Submission: NONE"
    if(Tilt == ""):
        Tilt_E = "Tilt,"
    if(Roll == ""):
        Roll_E = "Roll,"
    if(Twist == ""):
        Twist_E = "Twist,"
    if(Shift == ""):
        Shift_E = "Shift,"
    if(Slide == ""):
        Slide_E = "Slide,"
    if(Rise == ""):
        Rise_E = "Rise,"
    if(MaxS == ""):
        MaxS_E = "Max S,"
    if(Lk == ""):
        Lk_E = "Lk,"
    if(Nuc == ""):
        Nuc_E = "Nuc,"
    if(V1 == ""):
        V1Strng_E = "V1,"
    if(V2 == ""):
        V2Strng_E = "V2,"
    if(Cores == ""):
        Cores_E = "Cores,"
    context['Errors'], context['Tilt_E'], context['Roll_E'], context['Twist_E'], context['Shift_E'] = Errors, Tilt_E, Roll_E, Twist_E, Shift_E
    context['Slide_E'], context['Rise_E'], context['MaxS_E'], context['Lk_E'] = Slide_E, Rise_E, MaxS_E, Lk_E
    context['Nuc_E'], context['V1Strng_E'], context['V2Strng_E'], context['Cores_E'] = Nuc_E, V1Strng_E, V2Strng_E, Cores_E
    C = 5
    ### Develepoment Tools ########################################################
    context['Tilt'] = Tilt ########################################################
    context['Roll'] = Roll ########################################################
    context['Twist'] = Twist ######################################################
    context['Shift'] = Shift ######################################################
    context['Slide'] = Slide ######################################################
    context['Rise'] = Rise ########################################################
    context['MaxS'] = MaxS ########################################################
    context['Lk'] = Lk ############################################################
    context['Nuc'] = Nuc ##########################################################
    context['V1'] = V1 ############################################################
    context['V2'] = V2 ############################################################
    context['Cores'] = Cores ######################################################
    context['Geometry'] = Geometry ################################################
    context['SaveKey'] = SaveKey ##################################################
    context['formset'] = formset ##################################################