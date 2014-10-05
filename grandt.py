#!/usr/bin/python

from selenium import webdriver
from time import sleep

base_url = "http://www.grandt.clarin.com/"


def crearNavegador(documento, clave):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('permissions.default.stylesheet', 2)
    profile.set_preference("permissions.default.image", 2)
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(base_url + "html/login.html")

    driver.find_element_by_id("dniInput").send_keys(documento)
    driver.find_element_by_id("passInput").send_keys(clave+"\n")
    sleep(3)

    return driver


def buscarJugadores(driver):
    jugadores = []
    driver.get(base_url + "grandt/ini.htm?inpath=../grandt/transferencias.html")
    sleep(5)

    pagina = 0
    iterar = 1
    while iterar:
        sleep(0.2)
        pagina += 1
        driver.execute_script('javascript:buscarJugadores(%d)' % pagina)

        tabla = driver.find_element_by_id('tabla_de_futbolistas')
        for fila in tabla.find_elements_by_tag_name('tr')[1::]:
            if fila.text == "":
                iterar = 0
                break

            columnas = fila.find_elements_by_tag_name('td')

            j = {'nombre': columnas[1].text,
                 'equipo': columnas[2].text,
                 'posicion': columnas[3].text,
                 'cantidad': columnas[6].text,
                 }

            print j

            jugadores.append(j)
    return jugadores
