class Lampara: #Declaramos una clase
    #_LAMPARA es una variable de clase
    _LAMPARA = ['''
         _____  
   .'     `.
  /         \
 |           | 
 '.  +^^^+  .'
   `. \./ .'
     |_|_|  
     (___)    
jgs  (___)
     `---' ''',
    '''
              |
 \     _____     /
     /       \
    (         )
-   ( ))))))) )   -
     \ \   / /
      \|___|/
  /    |___|    \
       |___| prs
       |___|
    ''']

    def __init__(self , _is_turned_on): #Método de instancia, este es el constructor
        self._is_turned_on = _is_turned_on


    def turn_on(self):
        self._is_turned_on = True
        self._display_image()


    def turn_off(self):
        self._is_turned_on = False
        self._display_image()


    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPARA[1])
        else:
            print(self._LAMPARA[0])