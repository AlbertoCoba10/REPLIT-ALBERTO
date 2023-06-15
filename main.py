Horariosemanal={
          'Lunes a las 8h':'Matemáticas',
          'Lunes a las 9h' :'TRB',
          'Lunes a las 10h' :'TRB',
          'Lunes a las 11h':'HMC',
          'Lunes a las 12h':'Programación',
          'Lunes a las 13h' :'EdFisica' ,
          "Lunes a las 14h": "No tienes clase",
          "Martes a las 8h": "Castellano",
          "Martes a las 9h": "Religión",
          "Martes a las 10h": "Ingles",
          "Martes a las 11h": "Economia",
          "Martes a las 12h": "Filosofia",
          "Martes a las 13h": "Catalán",
          "Martes a las 14h":"Tutoria", 
          "Miercoles a las 8h": "Catalán",
          "Miercoles a las 9h:": "Castellano",
          "Miercoles a las 10h": "Ingles",
          "Miercoles a las 11h": "Programación",
          "Miercoles a las 12h": "EdFisica",
          "Miercoles a las 13h": "HMC",
          "Miercoles a las 14h": "No tienes clase",
          "Jueves a las 8h": "HMC",
          "Jueves a las 9h": "Matemáticas",
          "Jueves a las 10h": "Religión",
          "Jueves a las 11h": "Catalán",
          "Jueves a las 12h": "EdFisica",
          "Jueves a las 13h": "Economia",
          "Jueves a las 14h": "Filosofia" ,
          "Viernes a las 8h": "Matemáticas",
          "Viernes a las 9h": "Ingles",
          "Viernes a las 10h": "Economia",
          "Viernes a las 11h": "Programación",
          "Viernes a las 12h": "Filosofia",
          "Viernes a las 13h": "Castellano",
          "Viernes a las 14h": "No tienes clase"}

dia = input("Introduce un día de la semana: ")
diacorrecto = 1

if dia not in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]:
 while diacorrecto < 2:    
    dia=input('Inserta un dia de la semana correcto ')
    if dia  in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]:
      diacorrecto +=2
horas=1
horaasignatura=input('Introduce una hora desde las 8 a las 14 ')
if horaasignatura not in ["8", "9", "10", "11", "12","13","14"]:
 while horas < 2:    
    x=input('Inserta una hora correcta ')
    if x  in ["8", "9", "10", "11", "12","13","14"]:
      horas +=2


hora = input("Introduce dia y hora(formato (Lunes a las 8h),importante poner la h )")
if hora not in Horariosemanal.keys():
        print("Hora incorrecta.")
        
asignatura = Horariosemanal[hora]

print('El ' ,hora, ' tienes ',asignatura )
