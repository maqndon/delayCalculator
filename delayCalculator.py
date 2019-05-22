import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

ms=60000;
note=1
triplets=0.667
dotted=1.5

#notes num 1/1,num 1/2,num 1/4,num 1/8,num 1/16,num 1/32,num 1/64,num 1/128
# num*1+1, num*2+1, num*4+1, num*8+1, num*16+1, num*32+1, num*64+1, num*128+1
def barFunc(num):
    barAdd={"1":1,"2":2,"3":4,"4":8,"5":16,"6":32,"7":64,"8":128}        
    barN = []
    for bar in barAdd:
        mul = barAdd[bar]
        barN.append(num*mul+1)
    return barN
 
def buildElementBar(name,value,bar):
    
    notes = {"0":4,"1":2,"2":1,"3":0.5,"4":0.25,"5":0.125,"6":0.0625,"7":0.03125}
    barN = barFunc(int(bar))
    cuenta=-1

    for count in barN:
        cuenta+=1
        nombre=str(name)+str(bar)+str(cuenta)

        if value != 0:
            valor = eq*notes[str(cuenta)]*value*barN[int(cuenta)]
            window.Element(nombre).Update(round(valor,2))
        else:
            window.Element(nombre).Update(value ='')
        
# Columns layout

col0 = [
        [sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='note00', justification='right', disabled=True),sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets00', justification='right',
        disabled=True),sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted00', justification='right', disabled=True)],
        [sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='note01', justification='right', disabled=True),sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets01', justification='right',
        disabled=True),sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted01', justification='right', disabled=True)],
        [sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='note02', justification='right', disabled=True),sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets02', justification='right',
        disabled=True),sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted02', justification='right', disabled=True)],
        [sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='note03', justification='right',disabled=True),sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets03', justification='right',
        disabled=True),sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted03', justification='right', disabled=True)],
        [sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='note04', justification='right',disabled=True),sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets04', justification='right',
        disabled=True),sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted04', justification='right', disabled=True)],
        [sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='note05', justification='right',disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets05', justification='right',
        disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted05', justification='right', disabled=True)],
        [sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='note06', justification='right', disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets06', justification='right',
        disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted06', justification='right', disabled=True)],
        [sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='note07', justification='right', disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets07', justification='right',
        disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted07', justification='right', disabled=True)
        ]]


col1 = [
        [sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='note10', justification='right', disabled=True),sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets10', justification='right', disabled=True),sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted10', justification='right', disabled=True)],
        [sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='note11', justification='right', disabled=True),sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets11', justification='right', disabled=True),sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted11', justification='right', disabled=True)],
        [sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='note12', justification='right', disabled=True),sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets12', justification='right', disabled=True),sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted12', justification='right', disabled=True)],
        [sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='note13', justification='right', disabled=True),sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets13', justification='right', disabled=True),sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted13', justification='right', disabled=True)],
        [sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='note14', justification='right', disabled=True),sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets14', justification='right', disabled=True),sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted14', justification='right', disabled=True)],
        [sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='note15', justification='right', disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets15', justification='right', disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted15', justification='right', disabled=True)],
        [sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='note16', justification='right', disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets16', justification='right', disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted16', justification='right', disabled=True)],
        [sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='note17', justification='right', disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets17', justification='right', disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted17', justification='right', disabled=True)
        ]]

col2 = [
        [sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='note20', justification='right', disabled=True),sg.Text(' 1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets20', justification='right', disabled=True),sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted20', justification='right', disabled=True)],
        [sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='note21', justification='right', disabled=True),sg.Text(' 1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets21', justification='right', disabled=True),sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted21', justification='right', disabled=True)],
        [sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='note22', justification='right', disabled=True),sg.Text(' 1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets22', justification='right', disabled=True),sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted22', justification='right', disabled=True)],
        [sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='note23', justification='right', disabled=True),sg.Text(' 1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets23', justification='right', disabled=True),sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted23', justification='right', disabled=True)],
        [sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='note24', justification='right', disabled=True),sg.Text(' 1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets24', justification='right', disabled=True),sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted24', justification='right', disabled=True)],
        [sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='note25', justification='right', disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets25', justification='right', disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted25', justification='right', disabled=True)],
        [sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='note26', justification='right', disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets26', justification='right', disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted26', justification='right', disabled=True)],
        [sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='note27', justification='right', disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets27', justification='right', disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted27', justification='right', disabled=True)
        ]]


col3 = [
        [sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='note30', justification='right', disabled=True),sg.Text(' 1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets30', justification='right', disabled=True),sg.Text('1/1:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted30',justification='right', disabled=True)],
        [sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='note31', justification='right', disabled=True),sg.Text(' 1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets31', justification='right', disabled=True),sg.Text('1/2:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted31',justification='right', disabled=True)],
        [sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='note32', justification='right', disabled=True),sg.Text(' 1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets32', justification='right', disabled=True),sg.Text('1/4:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted32',justification='right', disabled=True)],
        [sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='note33', justification='right', disabled=True),sg.Text(' 1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets33', justification='right', disabled=True),sg.Text('1/8:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted33',justification='right', disabled=True)],
        [sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='note34', justification='right', disabled=True),sg.Text(' 1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets34', justification='right', disabled=True),sg.Text('1/16:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted34',justification='right', disabled=True)],
        [sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='note35', justification='right', disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets35', justification='right', disabled=True),sg.Text('1/32:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted35',justification='right', disabled=True)],
        [sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='note36', justification='right', disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets36', justification='right', disabled=True),sg.Text('1/64:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted36',justification='right', disabled=True)],
        [sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='note37', justification='right', disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='triplets37', justification='right', disabled=True),sg.Text('1/128:', size=(4,1)),sg.Input([],size=(8, 3), key='dotted37',justification='right', disabled=True)
        ]]

tabResults1=[[sg.Text('Notes', size=(13,1), justification='right'),sg.Text('Triplets',size=(13,1), justification='right'),sg.Text('Dotted',size=(13,1), justification='right')],
             [sg.Column(col0)]
            ]
tabResults2=[[sg.Text('Notes',size=(13,1), justification='right'),sg.Text('Triplets',size=(13,1), justification='right'),sg.Text('Dotted',size=(13,1), justification='right')],
             [sg.Column(col1)]
            ]
tabResults3=[[sg.Text('Notes',size=(13,1), justification='right'),sg.Text('Triplets',size=(13,1), justification='right'),sg.Text('Dotted',size=(13,1), justification='right')],
             [sg.Column(col2)]
            ]
tabResults4=[[sg.Text('Notes',size=(13,1), justification='right'),sg.Text('Triplets',size=(13,1), justification='right'),sg.Text('Dotted',size=(13,1), justification='right')],
             [sg.Column(col3)]
            ]

layout = [[sg.Text('BPM'), sg.Input([],size=(20, 3), key='_bpm_',focus=True, justification='right'), sg.RButton('Calculate Delay Time',bind_return_key=True)],
          [sg.TabGroup([[sg.Tab('Results', tabResults1), sg.Tab('1 Bar Added', tabResults2), sg.Tab('2 Bars Added', tabResults3), sg.Tab('3 Bars Added', tabResults4)]])],
          [sg.Text('1,000 milliseconds (ms) = 1 second')]
          
         ]

window = sg.Window('BPM Delay Time Calculator', layout)

while True:      
    event, values = window.Read()

    if event is None or event == 'Exit':
        break

    try:
        eq=ms/int(values['_bpm_'])
            
        for b in range(4):
            buildElementBar('note',note,b)
            buildElementBar('triplets',triplets,b)
            buildElementBar('dotted',dotted,b)
            
    except ValueError: 
        window.Element('_bpm_').Update(value ='Please Only Integer')
        
        for b in range(4):
        
            buildElementBar('note',0,b)
            buildElementBar('triplets',0,b)
            buildElementBar('dotted',0,b)
        
window.Close()
