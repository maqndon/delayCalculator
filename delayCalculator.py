import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

ms=60000;

#notes to calculate
notes = {
    "1":4,
    "2":2,
    "3":1,
    "4":0.5,
    "5":0.25,
    "6":0.125,
    "7":0.0625,
    "8":0.03125
}

bar1 = {
    "1":2,
    "2":3,
    "3":5,
    "4":9,
    "5":17,
    "6":33,
    "7":65,
    "8":129
}


cero=0
note=1
triplets=0.667
dotted=1.5

window = sg.Window('Columns')

def buildElement(name,value):
    for count in notes:
        first=name+count
        second=count
        if value != 0:
            valor = eq*notes[second]*value
            window.Element(first).Update(round(valor,2))
        else:
            window.Element(first).Update(value ='')

def buildElementBar(name,value,bar):
    for count in bar1:
        first=name+bar+count
        second=count
        barAdded=int(bar)+int(count)
        if value != 0:
            valor = eq*notes[second]*value*bar1[count]
            window.Element(first).Update(round(valor,2))
        else:
            window.Element(first).Update(value ='')

# Columns layout

col0 = [
        [sg.Text('1/1:'),sg.Input([],size=(8, 3), key='note1'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='triplets1'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='dotted1')],
        [sg.Text('1/2:'),sg.Input([],size=(8, 3), key='note2'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='triplets2'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='dotted2')],
        [sg.Text('1/4:'),sg.Input([],size=(8, 3), key='note3'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='triplets3'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='dotted3')],
        [sg.Text('1/8:'),sg.Input([],size=(8, 3), key='note4'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='triplets4'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='dotted4')],
        [sg.Text('1/16:'),sg.Input([],size=(8, 3), key='note5'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='triplets5'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='dotted5')],
        [sg.Text('1/32:'),sg.Input([],size=(8, 3), key='note6'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='triplets6'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='dotted6')],
        [sg.Text('1/64:'),sg.Input([],size=(8, 3), key='note7'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='triplets7'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='dotted7')],
        [sg.Text('1/128:'),sg.Input([],size=(8, 3), key='note8'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='triplets8'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='dotted8')
        ]]


col1 = [
        [sg.Text('1/1:'),sg.Input([],size=(8, 3), key='note11'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='triplets11'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='dotted11')],
        [sg.Text('1/2:'),sg.Input([],size=(8, 3), key='note12'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='triplets12'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='dotted12')],
        [sg.Text('1/4:'),sg.Input([],size=(8, 3), key='note13'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='triplets13'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='dotted13')],
        [sg.Text('1/8:'),sg.Input([],size=(8, 3), key='note14'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='triplets14'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='dotted14')],
        [sg.Text('1/16:'),sg.Input([],size=(8, 3), key='note15'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='triplets15'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='dotted15')],
        [sg.Text('1/32:'),sg.Input([],size=(8, 3), key='note16'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='triplets16'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='dotted16')],
        [sg.Text('1/64:'),sg.Input([],size=(8, 3), key='note17'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='triplets17'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='dotted17')],
        [sg.Text('1/128:'),sg.Input([],size=(8, 3), key='note18'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='triplets18'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='dotted18')
        ]]

col2 = [
        [sg.Text('1/1:'),sg.Input([],size=(8, 3), key='note21'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='triplets21'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='dotted21')],
        [sg.Text('1/2:'),sg.Input([],size=(8, 3), key='note22'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='triplets22'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='dotted22')],
        [sg.Text('1/4:'),sg.Input([],size=(8, 3), key='note23'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='triplets23'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='dotted23')],
        [sg.Text('1/8:'),sg.Input([],size=(8, 3), key='note24'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='triplets24'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='dotted24')],
        [sg.Text('1/16:'),sg.Input([],size=(8, 3), key='note25'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='triplets25'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='dotted25')],
        [sg.Text('1/32:'),sg.Input([],size=(8, 3), key='note26'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='triplets26'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='dotted26')],
        [sg.Text('1/64:'),sg.Input([],size=(8, 3), key='note27'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='triplets27'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='dotted27')],
        [sg.Text('1/128:'),sg.Input([],size=(8, 3), key='note28'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='triplets28'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='dotted28')
        ]]


col3 = [
        [sg.Text('1/1:'),sg.Input([],size=(8, 3), key='note31'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='triplets31'),sg.Text('1/1:'),sg.Input([],size=(8, 3), key='dotted31')],
        [sg.Text('1/2:'),sg.Input([],size=(8, 3), key='note32'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='triplets32'),sg.Text('1/2:'),sg.Input([],size=(8, 3), key='dotted32')],
        [sg.Text('1/4:'),sg.Input([],size=(8, 3), key='note33'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='triplets33'),sg.Text('1/4:'),sg.Input([],size=(8, 3), key='dotted33')],
        [sg.Text('1/8:'),sg.Input([],size=(8, 3), key='note34'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='triplets34'),sg.Text('1/8:'),sg.Input([],size=(8, 3), key='dotted34')],
        [sg.Text('1/16:'),sg.Input([],size=(8, 3), key='note35'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='triplets35'),sg.Text('1/16:'),sg.Input([],size=(8, 3), key='dotted35')],
        [sg.Text('1/32:'),sg.Input([],size=(8, 3), key='note36'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='triplets36'),sg.Text('1/32:'),sg.Input([],size=(8, 3), key='dotted36')],
        [sg.Text('1/64:'),sg.Input([],size=(8, 3), key='note37'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='triplets37'),sg.Text('1/64:'),sg.Input([],size=(8, 3), key='dotted37')],
        [sg.Text('1/128:'),sg.Input([],size=(8, 3), key='note38'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='triplets38'),sg.Text('1/128:'),sg.Input([],size=(8, 3), key='dotted38')
        ]]

tabResults1=[[sg.Text('Notes'),sg.Text('Triplets'),sg.Text('Dotted')],
             [sg.Column(col0)]
            ]
tabResults2=[[sg.Text('Notes'),sg.Text('Triplets'),sg.Text('Dotted')],
             [sg.Column(col1)]
            ]
tabResults3=[]
tabResults4=[]

layout = [[sg.Text('BPM'), sg.Input([],size=(20, 3), key='_bpm_',focus=True), sg.RButton('Calculate Delay Time')],
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
            
            buildElement('note',note)
            buildElement('triplets',triplets)
            buildElement('dotted',dotted)
            
            buildElementBar('note',note,'1')
            buildElementBar('triplets',triplets,'1')
            buildElementBar('dotted',dotted,'1')
            
    except ValueError: 
        window.Element('_bpm_').Update(value ='Please Only Integer')
        buildElement('note',cero)
        buildElement('triplets',cero)
        buildElement('dotted',cero)
        
        buildElementBar('note',cero,'1')
        buildElementBar('triplets',cero,'1')
        buildElementBar('dotted',cero,'1')

window.Close()
