#!/usr/bin/python

from base import Database
from grandt import crearNavegador, buscarJugadores
from credenciales import documento, clave

from datetime import datetime
from pyvirtualdisplay import Display

db = Database()

print "Iniciando Display Virtual"
display = Display(visible=0, size=(800, 600))
display.start()

print "Iniciando navegador..."
driver = crearNavegador(documento, clave)
jugadores = buscarJugadores(driver)


fecha = datetime.utcnow()

for j in jugadores:
    # insertarJugador(j)
    try:
        j_id = db.session.query(db.jugadores).filter_by(nombre=j['nombre'])[0][0]
    except:
        print "No encontre a %s" % j['nombre']
        continue

    registro = {'jugador_id': j_id,
                'cantidad': j['cantidad'],
                'fecha': fecha}

    try:
        db.equipos_gdt.insert(registro).execute()
    except:
        print "Fallo: %s" % registro


driver.close()
display.stop()
