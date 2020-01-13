def ficha():
    ficha.numero +=1
    return ficha.numero
ficha.numero = 0

def menu():
    N= "0"
    while N != "5":
        print("BIENVENIDO AL SERVICIO DE URGENCIA")
        print("..................................")
        print("""Selecione:
1.-Ingrese ficha del paciente
2.-Ingrese profesional
3.-Ingrese medicamento
4.-Estadisticas
5.-Salir""")

        N= input("digite opción: ")

        if N=="1":
            fichaClinica()
        elif N=="2":
            profesional()
        elif N=="3":
            medicamento()
        elif N=="4":
            estadistica()
        elif N=="5":
            salir()
        else:
            print("digite nuevamente")
        print()
        
def fichaClinica():
    print("hola bienvenido")
    print("Nombre del personal que ingresa la ficha")
    recepcionista=input()
    print("Ficha de ingreso N°",ficha())
    input("ingrese fecha y hora de atención: ")
    print("IDENTIFIQUE AL PACIENTE")
    
    nombre= input("nombre: ")
    apellido=input("apellido: ")
    run=input("RUN: ")
    while True:
        sexo = str(input("ingrese el sexo (M/F): "))
        if sexo=="M":
            break
        if sexo=="F":
            break
        else:
            print("ingrese bien el sexo")
                 
    while True:
        edad = int(input("edad: "))
        if edad>=0 and edad<=120:
            break
        else:
            print("digite edad entre 0 hasta 120 años")
    input("estado civil: ")
    input("domicilio: ")
    input("fono: ")
    input("grupo sanguíneo: ")
    print("tipo de urgencia")
    input("nivel de urgencia: ")
    print("acompañado (si/no): ")
    acompañante = input("digite opcion: ")

    if(acompañante =="si"and"s"):
        print("ingrese los datos del acompañante")
        input("nombre: ")
        input("apellidos: ")
        input("RUN: ")
        input("grado de parentesco: ")
        input("fono: ")

    elif(acompañante =="no"and"n"):
        print("no es necesario llenar")
        print()

def profesional():
    print("Profesional")
    input("nombre: ")
    input("especialidad: ")
    input("sintomas detectados del paciente: ")
    input("diagnostico: ")
    print("reposo: si/no")
    reposo = str(input())
    if(reposo=="si"):
        días=int(input("ingrese cantidad de días: "))

def medicamento():
    global paracetamol
    global omeprazol
    global licodaina
    global penicilina

    paracetamol= 0
    omeprazol= 0
    licodaina= 0
    penicilina= 0

    remedios = 0
    while remedios !=4:
        print("bienvenido a la farmacia only")
        print("_____________________________")
        print("""ingrese medicamento:
1.-parcetamol
2.-omeprazol
3.-licodaina
4.-penicilina""")
        remedios= int(input())
        if(remedios== 1):
                print("ingrese la cantidad de paracetamol:")
                paracetamol = int(input())
                input("dosis: ")
                input("cantidad de días a utilizar: ")
                print("¿necesita volver al menu para mas medicamentos?")
                reme= str(input("si/no: "))
                if reme=="si":
                    remedios
                else:
                    menu()
        if(remedios== 2):
                        print("ingrese la cantidad de omeprazol:")
                        omeprazol= int(input())
                        input("dosis: ")
                        input("cantidad de días a utilizar: ")
                        print("¿necesita volver al menu pra mas medicamentos?")
                        reme= str(input("si/no: "))
                        if reme=="si":
                            remedios
                        else:
                            menu()
        if(remedios==3):
                                print("ingrese la cantidad de licodaina")
                                licodaina= int(input())
                                input("dosis: ")
                                input("cantidad de días a utilizar: ")
                                print("¿necesita volver al menu para mas medicamentos?")
                                reme= str(input())
                                if reme=="si":
                                    remedios
                                else:
                                    menu()
        if(remedios==4):
                                        print("ingrese la cantidad de penicilina")
                                        penicilina= int(input())
                                        input("dosis: ")
                                        input("cantidad de días a utilizar: ")
                                        print("¿necesita volver al menu para mas medicamento?")
                                        reme= str(input())
                                        if reme=="si":
                                            remedios
                                        else:
                                            menu()
       

def estadistica():
    ficha.numero -=1

    print("candidad de fichas que hay")
    print(ficha())
    print("cantidad de personas atendidas:",ficha.numero)
    print("paracetamol:",paracetamol)
    print("omeprazol:",omeprazol)
    print("licodaina:",licodaina)
    print("penicilina:",penicilina)
    print("Cantidad total de medicinas:",paracetamol+omeprazol+licodaina+penicilina)
    
menu()
    
    
    
    


