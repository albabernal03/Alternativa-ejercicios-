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
***


## Ejercicio 2:<a name="id2"></a> 
Dados dos números culesquiera.
Clasificarlos respecto a su suma y a su producto.

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

fin ordenar4 
```
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
 ***

## Ejercicio 4:<a name="id4"></a>
***

## Ejercicio 5:<a name="id5"></a>
***

## Ejercicio 6:<a name="id6"></a>
***

## Ejercicio 7:<a name="id7"></a>
***

## Ejercicio 8:<a name="id8"></a>
Escribir el algoritmo de cálculo de la prima anual que se concederá a cada conductor.
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


