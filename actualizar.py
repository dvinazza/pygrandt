#!/usr/bin/python

from base import Database
from grandt import crearNavegador, buscarJugadores
from credenciales import documento, clave
from IPython import embed

from datetime import datetime

db = Database()
driver = crearNavegador(documento, clave)
jugadores = buscarJugadores(driver)


def insertarJugador(j):
    try:
        j['equipo_id'] = db.session.query(db.equipos).\
            filter_by(nombre=j['equipo'])[0][0]
    except:
        db.equipos.insert({'nombre': j['equipo']}).execute()
        j['equipo_id'] = db.session.query(db.equipos).\
            filter_by(nombre=j['equipo'])[0][0]

    try:
        j['posicion_id'] = db.session.query(db.posiciones).\
            filter_by(nombre=j['posicion'])[0][0]
    except:
        db.posiciones.insert({'nombre': j['posicion']}).execute()
        j['posicion_id'] = db.session.query(db.posiciones).\
            filter_by(nombre=j['posicion'])[0][0]

    j.pop('equipo')
    j.pop('posicion')
    try:
        db.jugadores.insert(j).execute()
    except:
        print "Fallo: %s" % j


for j in jugadores:
    # insertarJugador(j)
    try:
        j_id = db.session.query(db.jugadores).filter_by(nombre=j['nombre'])[0][0]
    except:
        continue

    registro = {'jugador_id': j_id, 'cantidad': j['cantidad']}

    try:
        db.equipos_gdt.insert(registro).execute()
    except:
        print "Fallo: %s" % registro


driver.close()
