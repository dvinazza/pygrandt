#!/usr/bin/python
# -*- coding: utf -*-

from sqlalchemy import create_engine, MetaData, select, and_
from sqlalchemy import Table, Column, Integer, String, \
    ForeignKey, UniqueConstraint, Date
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

class Database():
    def __init__(self, echo=False):

        self.db = create_engine('sqlite:///datos.sqlite',
                                convert_unicode=True,
                                echo=echo)
        # encoding defaults to utf8
        self.metadata = MetaData(bind=self.db)
        self.session = scoped_session(sessionmaker(self.db, autoflush=True,
                                                   autocommit=True))

        try:
            self.equipos = Table('equipos', self.metadata, autoload=True)
        except:
            self.equipos = Table('equipos', self.metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('nombre', String(64)))
            self.equipos.create()

        try:
            self.posiciones = Table('posiciones', self.metadata, autoload=True)
        except:
            self.posiciones = Table('posiciones', self.metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('nombre', String(64)),)
            self.posiciones.create()

        try:
            self.jugadores = Table('jugadores', self.metadata, autoload=True)
        except:
            self.jugadores = Table('jugadores', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('nombre', String(64)),
                                   Column('equipo_id', String(32),
                                          ForeignKey('equipos.id')),
                                   Column('posicion_id', String(3),
                                          ForeignKey('posiciones.id')),
                                   UniqueConstraint('nombre', 'equipo_id',
                                                    'posicion_id'))
            self.jugadores.create()

        try:
            self.equipos_gdt = Table('equipos_gdt', self.metadata,
                                     autoload=True)
        except:
            self.equipos_gdt = Table('equipos_gdt', self.metadata,
                                     Column('id', Integer, primary_key=True),
                                     Column('jugador_id', Integer,
                                            ForeignKey('jugadores.id')),
                                     Column('cantidad', Integer),
                                     Column('fecha', Date,
                                            default=datetime.utcnow))
            self.equipos_gdt.create()
