# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define an = Character('Anne')
define az = Character('Azalea')
define ve = Character('Venice')

# El juego comienza aquí.

label start:
    
    # Música inicial.
    # play music "illurock.opus"

    # Muestra una imagen de fondo:

    scene bg room

    # Muestra un personaje:
    
    "Gzzz!"

    show Anne

    # Presenta las líneas del diálogo.
    
    # play music "autosruidosos.algo"

    an "Un día mas aquí me hará enloquecer..."
    
    "He vivido en esta habitación los últimos tres meses, y ya siento que han sido años.
     Fui bastante ingenua al creer que una vida de ciudad iba a ser divertida, decidí dejar mi casa para divertirme como nunca"
    
    "..."
    
    "Sinceramente no había pensado en el dinero que necesitaba para hacer eso."
    
    show an
    
    "Tengo que trabajar horas extras para mantenerme en este lugar, no quiero algo mas barato, ni vecinos mas molestos. Ya tengo suficiente con esos autos."
    
    "Toc Toc"
        
    "¿Qué? Es demasiado tarde... A quién se le ocurre venir a esta hora. Y sí es un criminal... Si abro esa puerta mi vida puede estar en peligro!"
    
    menu:
                      
        "Abrir la puerta":
            jump carta
        
        "No abrir":
            jump puertacerrada
        
    label carta:
    
    "Al momento abrí la puerta, no había nadie. Solo una carta en el suelto"
    
    # scene carta
    
    return
    
    label puertacerrada:
        
    "No abriré aunque revienten mis oidos con el insoportable golpe de puerta!"
        
    "..."
        
    "Ya no tocan. Quizá ya se fueron..."
    
    "Final malo"
    
    return
        
    
    # Finaliza el juego:

    return
