# -*- coding: utf-8 -*-
'''
Una serie di poster rettangolari sono stati affissi ad un muro.  I
   loro lati sono orizzontali e verticali. Ogni poster può essere
   parzialmente o totalmente coperto dagli altri. Chiameremo
   perimetro la lunghezza del contorno dell'unione di tutti i posters
   sul muro. Si guardi l'immagine in "posters.png" in cui i poster sulla
   parete compaiono in bianco coi bordi blu e la si confronti con l'immagine
   "posters1.png" in cui in rosso vengono evidenziati i soli
   bordi che contribuiscono al perimetro.

Vogliamo un programma che calcola il perimetro dei poster e produce
   una immagine simile a "posters1.png".

Progettare dunque una funzione
     ex1(ftesto, filepng)
   che prenda come parametri
   - ftesto, l'indirizzo di un file di testo contenente le informazioni sulla
     posizione dei poster sul muro,

   - filepng, nome del file immagine in formato PNG da produrre

   e restituisca il perimetro dei poster come numero di pixel rossi.

Il file di testo contiene tante righe quanti sono i poster,
   nell'ordine in cui sono stati affissi alla parete. In ciascuna
   riga ci sono le coordinate intere del vertice in basso a sinistra e
   del vertice in alto a destra del poster. I valori di queste
   coordinate sono dati come coppie ordinate della coordinata x
   seguita dalla coordinata y. Si veda ad esempio il file
   rettangoli_1.txt contenente le specifiche per i 7 posters in
   "posters.png".
   
L'immagine da salvare in filepng deve avere lo sfondo nero, altezza h
   +10 e larghezza w+10 dove h è la coordinata x massima del muro su
   cui compaiono poster e w la coordinata y massima del muro su cui
   compaiono posters. I bordi visibili dei poster sono colorati di
   rosso o di verde a seconda che appartengano al perimetro o meno.
   Notare che un pixel si trova sul perimetro (e quindi è rosso) se nel
   suo intorno (gli 8 pixel adiacenti) si trova almeno un pixel esterno
   a tutti i poster.

   Per caricare e salvare i file PNG si possono usare le funzioni load
   e save presenti nel modulo "images".

Per esempio: ex1('rettangoli_1.txt', 'test_1.png') deve costruire un file PNG
   identico a "posters1.png" e restituire il valore 1080.
   
NOTA: il timeout previsto per questo esercizio è di 1.5 secondi per ciascun
   test

ATTENZIONE: quando caricate il file assicuratevi che sia nella
    codifica UTF8 (ad esempio editatelo dentro Spyder)

'''

import images

def crea_immagine(x,y,colore):
    return [ [colore] *x   for riga in range(y) ]

        
 
def draw_rectangle(img,x1,y1,x2,y2): 
  for y in range(y1, y2+1):
      for x in range(x1, x2+1):
          img[y][x] = (255,255,255)

def draw_perimetro(img, x, y):
     ad={(x-1,y-1),(x,y-1),(x-1,y),(x+1,y-1),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)}
     flag=False
     for nx,ny in ad :
             if img[ny][nx]==(0,0,0):
                 flag=True 
                 break
     if flag :
          img[y][x] = (255,0,0)
          
     else:
         img[y][x] = (0,255,0)          
'''
def draw_h_line2(img, x, y, x2):
    for X in range(x, x2+1):
      flag=False
      ad={(X-1,y-1),(X,y-1),(X-1,y),(X+1,y-1),(X+1,y),(X-1,y+1),(X,y+1),(X+1,y+1)}
      for nx,ny in ad :
            if img[ny][nx]==(0,0,0):
                flag=True 
                break
      if flag :
              img[y][X] = (255,0,0)
              
      else:
             img[y][X] = (0,255,0)
        
def draw_v_line2(img, x, y, y2):
    altezza= len(img)
    ymin = min(max(y, 0), altezza-1)
    ymax = max(min(y2, altezza-1),0)
    for Y in range(ymin, ymax+1):
        ad={(x-1,Y-1),(x,Y-1),(x-1,Y),(x+1,Y-1),(x+1,Y),(x-1,Y+1),(x,Y+1),(x+1,Y+1)}
        flag=False
        for nx,ny in ad :
                if img[ny][nx]==(0,0,0):
                    flag=True 
                    break
        if flag :
                  img[Y][x] = (255,0,0)
                  
        else:
                 img[Y][x] = (0,255,0) 
             
def draw_empty_rectangle2(img,x1,y1,x2,y2):
    if y1>y2 : y1,y2=y2,y1  
    draw_h_line2(img, x1, y1, x2)
    draw_h_line2(img, x1, y2, x2)
    draw_v_line2(img, x1, y1, y2)
    draw_v_line2(img, x2, y1, y2)
'''
         
def draw_empty_rectangle(img,x1,y1,x2,y2):
           for x in range(x1, x2+1):
               draw_perimetro(img, x, y1)
               draw_perimetro(img, x, y2)
           for y in range(y1, y2+1):
               draw_perimetro(img, x1, y)
               draw_perimetro(img, x2, y)
    
def ex1(ftesto, filepng ):
    # inserisci qui il tuo codice
    with open(ftesto,"r",encoding="utf8") as f :
        poster = [tuple(map(int, riga.split())) for riga in f ] 
    


    tx =max(poster,key=lambda x: x[0])[0]
    tx2 =max(poster,key=lambda x: x[2])[2]
    if tx2 > tx: max_x=tx2
    else: max_x=tx
    ty =max(poster,key=lambda x: x[1])[1]
    ty2 =max(poster,key=lambda x: x[3])[3]
    if ty2 > ty: max_y=ty2
    else: max_y=ty
    
    img = crea_immagine(max_x+10,max_y+10,colore=(0,0,0))
    for tupla in poster:
        x1,y1,x2,y2=tupla
        if y1>y2 : y1,y2=y2,y1 
        draw_rectangle(img,x1,y1,x2,y2)

    
    for tupla in poster:
        x1,y1,x2,y2=tupla
        if y1>y2 : y1,y2=y2,y1 
        draw_rectangle(img,x1,y1,x2,y2)
        draw_empty_rectangle(img,x1,y1,x2,y2)   
    
    perimetro = sum([riga.count((255, 0, 0)) for riga in img])  

    images.save(img, filepng)
    images.visd(img)



    
    return perimetro
    pass
    




if __name__ == '__main__':
    pass
    print(ex1('rectangles_1.txt', 'test_1.png'))
