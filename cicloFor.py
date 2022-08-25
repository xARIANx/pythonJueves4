'''
for i in range(2):
    print(f'el contador vale {i}')
    
for i in range(1,6,2):
    print(f'el contador vale {i}')
'''

#Listas en python
nombres=['juan','Ana','carlos','martha']

#como recorro una lista en python
#esculcar el arreglo
#optener por separado cada elemento de la lista

for nombre in nombres:
    print(nombre)
    
    #javascript
    
    nombres.forEach(function(nombre){
        console.log(nombre)
    })