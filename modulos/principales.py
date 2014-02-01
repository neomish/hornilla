#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Librería De Módulos Para Complementar Al                        #
# Progrma Simple Para Colocar En Un Equipo De Servicio De Quemado #
# Autor: José David Calderón Serrano                              #
#        jose.david@calderonbonilla.org, gato@debian.ues.edu.sv   #
#                                                                 # # # # # #
# Este programa es software libre: usted puede redistribuirlo y / o         #
# modificarlo bajo los términos de la GNU General Public License publicada  #
# por la Free Software Foundation, bien de la versión 3 de la Licencia, o   #
# (a su elección) cualquier versión posterior.                              #
#                                                                           #
# Este programa se distribuye con la esperanza de que sea útil, pero SIN    #
# NINGUNA GARANTÍA, incluso sin la garantía implícita de COMERCIALIZACIÓN o #
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulte la GNU General Public    #
# License para más detalles.                                                #
#                                                                           #
# Debería haber recibido una copia de la Licencia Pública General GNU junto #
# con este programa, vease el archivo licencia/gpl.v3.es.txt, Si no, vea    #
# <http://www.viti.es/gnu/licenses/gpl.html>.                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import sys
import pygame
import time
from pygame.locals import *

pygame.init( )
pygame.mixer.init()

POSICION_MENU = 0
LISTA_DE_ISOS = 0
ACCION = 0
PARPADEO = 1
ISO_A_QUEMAR = ""
QUEMANDO = pygame.mixer.Sound("sonidos/02 - No more virus in heaven.ogg" )

def ventana_principal ( TITULO , ANCHO , ALTO ) :
    pantalla = pygame.display.set_mode( ( ANCHO , ALTO ) )
    pygame.display.set_caption( TITULO )
    return pantalla

def fondo ( FONDO ) :
    imagen = pygame.image.load( FONDO )
    imagen = imagen.convert( )
    return imagen , 0 , 0

def poner_musica( ) :
    sonido = pygame.mixer.Sound("sonidos/menu.ogg" )
    sonido.play( -1 , 0 , 3 )

def tocar_sonido( audio ) :
    sonido = pygame.mixer.Sound("sonidos/" + audio + ".ogg")
    sonido.play( )

def evaluar_eventos ( ) :
    global POSICION_MENU
    global LISTA_DE_ISOS
    global ACCION
    for eventos in pygame.event.get( ) :
        if ACCION == 0 :
            if eventos.type == QUIT :
                tocar_sonido( "jurgen3" )
                time.sleep( 2 )
                sys.exit( 0 )
            if eventos.type == KEYDOWN :
                if eventos.key == K_q :
                    tocar_sonido( "jurgen3" )
                    time.sleep( 2 )
                    sys.exit( 0 )
                if eventos.key == K_f :
                    cambiar_modo_de_pantalla_completa ( )
                if eventos.key == K_UP :
                    POSICION_MENU -= 1
                    if POSICION_MENU < 0 :
                        POSICION_MENU = 0
                    tocar_sonido( "7" )
                if eventos.key == K_DOWN :
                    POSICION_MENU +=1
                    if POSICION_MENU == LISTA_DE_ISOS :
                        POSICION_MENU = LISTA_DE_ISOS - 1
                    tocar_sonido( "7" )
                if eventos.key == K_RETURN :
                    tocar_sonido( "bonus" )
                    quemar_cd ( )

def quemar_cd ( ) :
    global ISO_A_QUEMAR
    if ACCION == 0 :
        # Para prueba usar la siguiente línea
        # os.system ("echo wodim -v isos/" + ISO_A_QUEMAR + " && sleep 10s &" )
        # Para produccion usar la siguiente linea
        os.system ("eject -t && wodim -v -eject isos/" + ISO_A_QUEMAR + " &" )

def verificar_si_esta_quemando( ) :
    global ACCION
    global QUEMANDO
    # Para prueba usar la siguiente línea
    # tuberia = os.popen( "pgrep sleep" )
    # Para produccion usar la siguiente linea
    tuberia = os.popen( "pgrep wodim" )
    salida_estandar = tuberia.readlines( )
    tuberia.close()
    if len( salida_estandar ) == 0 :
        if ACCION == 1 :
            ACCION = 0
            QUEMANDO.fadeout( 3 )
            tocar_sonido( "bonus" )
            tocar_sonido( "perfect2" )
            QUEMANDO.stop( )
    else :
        if ACCION == 0 :
            ACCION = 1
            QUEMANDO.play( -1 )

def texto( texto , pixeles , color = ( 255 , 255 , 255 ) , fondo = None ) :
    fuente = pygame.font.Font( "fuentes/Erika_Type_BI.ttf" , pixeles )
    if fondo :
        salida = pygame.font.Font.render( fuente , texto , 1 , color , fondo )
    else :
        salida = pygame.font.Font.render( fuente , texto , 1 , color )
    return salida

def poner_boton ( ):
    global ACCION
    global PARPADEO
    if ACCION == 0 :
        boton = pygame.image.load( "imagenes/boton_apagado.png" )
    else :
        if PARPADEO == 1:
            boton = pygame.image.load( "imagenes/boton_encendido.png" )
            PARPADEO = 2
        else :
            boton = pygame.image.load( "imagenes/boton_encendido2.png" )
            PARPADEO = 1
    boton = boton.convert()
    color = boton.get_at((0,0))
    boton.set_colorkey(color, RLEACCEL)
    return boton

def menu ( lista ) :
    global POSICION_MENU
    global LISTA_DE_ISOS
    global ISO_A_QUEMAR
    TOTAL_A_LISTAR = 16
    ESPACIO_ENTRE_ELEMENTOS = 15
    p = 1
    mostrar = []
    for i in lista :
        if POSICION_MENU != p - 1 :
            mostrar.append( texto( lista[ p - 1 ][:25] , 12 ) )
        else:
            mostrar.append( texto( lista[ p - 1 ][:25] , 12 , ( 0 , 255 , 0 ) , ( 179 , 56 , 255 ) ) )
            ISO_A_QUEMAR = lista[ p - 1 ]
        p += 1
    LISTA_DE_ISOS = p - 1
    if POSICION_MENU <= TOTAL_A_LISTAR :
        ver = TOTAL_A_LISTAR
        limite_inferior = 0
    else :
        ver = POSICION_MENU
        limite_inferior = ver - TOTAL_A_LISTAR
    if LISTA_DE_ISOS <= TOTAL_A_LISTAR :
        limite_superior = LISTA_DE_ISOS
    else:
        limite_superior = ver + 1
    regresar = []
    p = 1
    for x in range( limite_inferior , limite_superior ) :
        regresar.append( [ mostrar[ x ] , 60 , 135 + ESPACIO_ENTRE_ELEMENTOS * p ] )
        p += 1
    return regresar

def obtener_isos ( ) :
    tuberia = os.popen( "ls ./isos/" )
    salida_estandar = tuberia.readlines( )
    tuberia.close()
    isos = []
    for linea in salida_estandar:
        isos.append( linea[:-1] )
    return isos

def cambiar_modo_de_pantalla_completa ( ) :
    pygame.display.toggle_fullscreen( )

def lazo_principal( pantalla , objetos ) :
    poner_musica( )
    while True :
        pygame.time.delay(5)
        verificar_si_esta_quemando( )
        evaluar_eventos( )
        for i in range( len( objetos ) ) :
            objeto = objetos[ i ][ 0 ]
            pantalla.blit ( objeto , ( objetos[ i ][ 1 ] , objetos[ i ][ 2 ] ) )
        mover = menu ( obtener_isos ( ) )
        for i in range( len( mover ) ) :
            move = mover[i][0]
            pantalla.blit ( move , ( mover[ i ][ 1 ] , mover[ i ][ 2 ] ) )
        pantalla.blit ( poner_boton( ) , ( 460 , 220 ) )
        pygame.display.flip( )
    return 0