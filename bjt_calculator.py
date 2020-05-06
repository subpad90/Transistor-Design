
#Emitter Degeneration Resistor Biasing
Vsignal = 100E-3
B = 100E0
Vcc = 12.0E0
Vce = Vcc/2

Rc = 6E3
RL = 1E6
Rout = 1/((1/Rc)+(1/RL))

Ic = 1E-3

Vrc = Ic * Rc 
Vc = Vcc-Vrc

Ve = 0.50E0

#Vce = Vc - Ve
Vb = Ve + 0.7E0

Ib = Ic/B
IbiasR1 = Ic/10E0
IbiasR2 = IbiasR1 - Ib
Ie = Ic + Ib


R1 = (Vcc - Vb)/IbiasR1
R2 = Vb / IbiasR2
Re = Ve/(Ic+Ib)
re = 25E-3/Ie
Rin = 1/((1/R1)+(1/R2)+(1/(B*(Re+re))))

Av = (Rout/Re)
Vout = Av * Vsignal

Iin = Vsignal / Rin 
Iout = Vout / RL



Transistor = {
        "B" : B,
        "Ic": Ic,
        "Ib": Ib,
        "Ie": Ie,
        "In": Iin,
        "Iout": Iout,
        "Rc": Rc,
        #"Rcreal": Rcreal,
        "Re": Re,
        "R1": R1,
        "R2": R2,
        "Rin": Rin,
        "RL": RL,
        "Rout":Rout,
        "Vrc": Vrc,
        "Vc": Vc,
        "Vb": Vb,
        "Vce": Vce,
        "Ve": Ve,
        "Vcc": Vcc,
        "Av": Av,
        "Vsingal": Vsignal,
        "Vout": Vout        
        }
#print(Transistor)

print ("{:<8} {:<15}".format('Key','Value'))

for k, v in Transistor.items():
    label = v
    print ("{:<8} {:<15}".format(k, label))


if Vc > Vb and (Vb-Ve) > 0.6:
    print ("Transistor in Active Region")
elif Vc < Vb and Ve < Vb:
    print ("Transistor in Sataturation Region")
elif Vb < Ve and Vb < Ve:
    print ("Transistor in Cutoff Region")
else:
    print("Transistor in reverse Active region")
        