<h1 align="center">	Ejercicios  de la Alternativa</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Alternativa-ejercicios-)
***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea hemos resuelto una serie de ejercicios a través del uso del **pseudocódigo**. Asimismo hemos añadido su correspondiente diagrama de flujo.
***

## Indice
1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Ejercicio 3](#id3)
4. [Ejercicio 4](#id4)
5. [Ejercicio 5](#id5)
6. [Ejercicio 6](#id6)
7. [Ejercicio 7](#id7)
8. [Ejercicio 8](#id8)

***

## Ejercicio 1:<a name="id1"></a>
Dado un dia de la semana, printar el dia siguiente.

**SOLUCION**
```
algoritmo: día_sucesor
Entrada
d: días {lunes; martes; miércoles; jueves; viernes; sábado; domingo}
Precondición
  ninguna
Realización
  (antiguo d = lunes-> d= martes)
  o si no
  (antiguo d = martes-> d= miércoles)
  o si no
  (antiguo d = miércoles-> d= jueves)
  o si no
  (antiguo d = jueves-> d= viernes)
  o si no
  (antiguo d = viernes-> d= sábado)
  o si no
  (antiguo d = sábado-> d= domingo)
  o si no
  (antiguo d = domingo-> d= lunes)
  fin si

Poscondición
  d= sucesor del valor antiguo de d

fin día_sucesor
```

**DIAGRAMA DE FLUJO**


***

## Ejercicio 2:<a name="id2"></a> 
Dados dos números cualesquiera, clasificarlos respecto a su suma y su producto.

**SOLUCIÓN:**
```
Algoritmo ordenar
  #ordenar a y b con la suma y el producto en orden creciente
Entrada
  a,b: T -> COMPARABLE
variable
  c,d: (T, +, x) -> COMPARABLE
Precondición
  ninguna
Realización
  si a > b entonces intercambiar (a,b) fin si #añadimos c
  si b > c entonces intercambiar (b,c) fin si 
  si a > b entonces intercambiar (a,b) fin si # a < b < c, añadimos d
  si  c > d entonces intercambiar (c,d) fin si
  si a > b entonces intercambiar (a,b) fin si # a < b < c < d
  c <- a + b; d <- a x b
 fin si 

poscondición
  a < b < c < d

fin ordenar 
```

**DIAGRAMA DE FLUJO:**

<img width="739" alt="Captura de pantalla 2022-02-18 a las 12 24 35" src="https://user-images.githubusercontent.com/91721668/154678490-577d4439-49ac-42af-87e6-3cece4e09a7d.png">


## Ejercicio 3:<a name="id3"></a>

**SOLUCIÓN:**
```
Algoritmo calculo descuento
#vamos a calcular el tipo de descuento que se aplica dependiendo del precio

Entrada
 precio: real 

Resultado: real

Precondición 
 precio ≥ 0

realización

  Si precio < 100 entonces
    resultado <- precio
  Si no si 100 < precio < 500 entonces
    resultado <- precio - (precio x 0,05)
  Si no
    #precio>500
    resultado <- precio - (precio x 0,08)
  fin si
  
poscondición

 precio < 100 --> Resultado = precio
 100 < precio < 500 --> Resultado = precio - (precio x 0,05)
 precio > 500 --> Resultado = precio - precio x (precio x 0,08)

 fin calculo descuento
 ``` 
 
 **DIAGRAMA DE FLUJO:**
 
 ![Ejercicio 3 alternativa](https://user-images.githubusercontent.com/91721875/154680297-673b3d6e-9aec-45d4-ae75-7a6c664e4bf5.jpg)

 ***

## Ejercicio 4:<a name="id4"></a>
***

## Ejercicio 5:<a name="id5"></a>
***

## Ejercicio 6:<a name="id6"></a>
***

## Ejercicio 7:<a name="id7"></a>
**SOLUCIÓN**
```
algoritmo: coste_trayecto

Entrada
  precio: 67,30 o 61,00

Precondición
  alumnos > 0

Realización
  si alumnos < 25 entonces 
  precio = 67,30
  si no si entonces 
  precio = 61,00

Poscondición
  alumnos < 25 -> precio= 67,30
  alumnos > 25 -> precio= 61,00

fin coste_trayecto

algoritmo: comida

Entrada
  precio: 3,50
  día: d
Precondición
  ninguna
Realización
  precio = precio x d
Poscondición
  precio = 3,50 x días

fin comida

algoritmo: alojamiento
Entrada
  precio: 4,75 o 4 o 3,50
Precondición
  alumnos > 0
Realización
  si alumnos < 30 
  precio = 4,75
  si no si 31 < alumnos < 35 entonces
  precio = 4
  si no alumnos > 35 entonces
  precio = 3,5
Poscondición
  alumnos < 30 -> precio= 4,75
  31 < alumnos < 35 -> precio= 4
  alumnos > 35 -> precio= 3,5
fin alojamiento

algoritmo coste_total
  coste_total = coste_trayecto + comida + alojamiento

 ```
 
 **DIAGRAMA DE FLUJO**
 

## Ejercicio 8:<a name="id8"></a>
```
algoritmo prima_anual
Entrada

  variable
    euro = €
    kilómetro = km
    años = a
Precondición
  prima_accidentes ≥ 0
  prima ≥ 0
Realización
  si responsabilidad_accidente < 20% entonces
  prima_accidentes = 0
  si responsabilidad_accidente > 20% entonces
  prima_accidentes > 0 
    si num_accidentes = 2
    prima_accidentes = prima / 2
    si num_accidentes = 3
    prima_accidentes = prima / 3
    si num_accidentes > 3
    prima_accidentes = prima

  prima = prima_distancia + prima_antigüedad
    prima_distancia = (o,o1 x €) x km hasta 400 €

    prima_antigüedad(a partir 4 años) = 200 € + a x 20 €

  prima_anual = prima - prima_accidentes

Poscondición
  prima_anual = prima - prima_accidentes
  responsabilidad_accidente < 20% -> prima_accidentes =0
  responsabilidad_accidente > 20% -> prima_accidentes >0
  prima = prima_distancia + prima_antigüedad

fin prima_anual
```

![diagramadeflujoprimas](https://user-images.githubusercontent.com/91721668/154678448-b81ff449-1302-43bd-ab6f-639ef2fb4a7f.png)


