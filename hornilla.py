#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Programa Simple Para Colocar En Un Equipo De Servicio De Quemado De CD  #
# Autor: José David Calderón Serrano                                      #
#        jose.david@calderonbonilla.org                                   #
#                                                                         # #
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

# Módulos
import os
import sys
import pygame
from pygame.locals import *
from modulos.principales import *

def main( ) :
    return 0

if __name__ == '__main__' :
    pantalla = ventana_principal( "Hornilla Quemadora" , 640 , 480 )
    objetos = [ fondo( "imagenes/fondo.png" ) ]
    objetos.append( [ texto( "Hornilla" , 40 , ( 0 , 255 , 0 ) ) , 9 , 21 ] )
    objetos.append( [ texto( "Hornilla" , 40 , ( 179 , 56 , 255 ) ) , 10 , 20 ] )
    objetos.append( [ texto( "Quemadora" , 40 , ( 0 , 255 , 0 ) ) , 9 , 81 ] )
    objetos.append( [ texto( "Quemadora" , 40 , ( 179 , 56 , 255 ) ) , 10 , 80 ] )
    lazo_principal( pantalla , objetos )
    main( )
