# *.* coding: utf-8 *.*

'''
Tämä esimerkki esittelee säikeiden toimintaa yleisesti ja käyttöliittymässä
 
ESIMERKKI JOTA LUET ON ESIMERKKI OIKEASTA TOTEUTUKSESTA, luithan kaikki
väärät esimerkit jotka alustivat tätä esimerkkiä.
 
Tässä versiossa numeroiden rullaus voidaan pysäyttää ja käynnistää. Ohjelma
ei syö tehoa lähes lainkaan. Katsotaan kuinka ongelmat lopulta ratkaistiin.
 
 
Muutokset edellisiin esimerkkeihin löytyvät metodeista wait_until_ready() ja
request-start() selaa niihin asti.

Otto Seppälä 2003-2006, santtu
'''
from PySide import QtGui
from PySide import QtCore

from threading import *
import time


class RunningAnimation(Thread):

    def __init__(self, graphicscene):
        super(RunningAnimation, self).__init__()

        self.condition = Condition()
        self.graphicscene = graphicscene
        self.delay = 0.5  #seconds
        self.number = 0
        self.end_requested = False
        self.stop_requested = True


    def run(self):
        print 'run'
        while not self.end_requested:

            self.wait_until_ready()
            if not self.end_requested:
                
                
                self.number += 1
                text = str(self.number)
                
                self.graphicscene.addText(text)
                print text
                
            try:
                time.sleep(self.delay)
            except KeyboardInterrupt:
                self.stop_requested = False


    '''
    sleep-funktio laittaa säikeen nukkumaan määrätyksi ajaksi. Säikeet voivat
    myös mennä odottamaan(wait) niin, että toinen säie voi herättää ne
    tarvittaessa.
    
    Jotta tämä on mahdollista tarvitaan jokin olio, johon odottamisen
    aloittava säie merkitsee olevansa odottamassa. Toinen säie voi sitten
    myöhemmin herättää kaikki säikeet jotka ovat merkinneet em. olioon
    olevansa odottamassa. Tässä se on Condition.
    
    Vertaus: kaksi säiettä: Matti ja Pentti. Olio : jääkaappi
    
    Kun jääkaapissa on ruokaa Matti syö sitä innokkaasti. Kun ruoka loppuu,
    matin täytyy odottaa. Matti merkitsee odottamisen laittamalla jääkaapin
    kylkeen postit-lapun (Olen nukkumassa) jääkaappi.wait()
    
    Kun Pentti tulee kaupasta hän laittaa ruoan jääkaappiin. Jos pentti
    haluaa, hän voi herättää jonkun joka on merkinnyt olevansa nukkumassa
    kutsumalla metodia jääkaappi.notify(). Tällöin Matti herää ja aloittaa
    syömisen.
    
    Jotta sekaannuksia ei sattuisi sovitaan, että kaapille pääsee vain yksi
    kerrallaan laittamaan ruokaa, lappuja jne. Tämä hoituu condition-olioon
    liittyvällä lukolla. Käytettäessä condition-oliota with-lauseen yhteydessä
    lukon asetus ja vapautus tapahtuvat automaattisesti.
    
    
    wait_until_ready toimii muuten kuten ennenkin, mutta odottaminen on
    hoidettu em. wait() ja notify() metodien avulla. Jos stop-nappulaa on
    painettu, merkitsee numeroita pyörittävä säie condition-olion tilaksi, että
    odottaa. (wait)
    '''

    def wait_until_ready(self):
        if self.stop_requested:
            try:
                with self.condition:
                    print "Animation Thread starts waiting"
                    self.condition.wait()
                    print "Animation Thread stopped waiting!"
            except KeyboardInterrupt:
                self.stop_requested = False


    '''
    Säikeen odottaminen katkaistaan kutsumalla condition-olion
    notify-metodia. (tuohon olioonhan wait()-metodiakin kutsuttiin. Ennen
    säikeen toiminnan jatkamista muutetaan stop-requested muuttujan arvoa,
    jotta odotus ei ala uudestaan.
    '''

    def request_start(self):
        self.stop_requested = False
        with self.condition:
            self.condition.notify()
            print "Event listener thread called notify of the RunningAnimation-object"

    def request_stop(self):
        self.stop_requested = True

    def request_end(self):
        self.stop_requested = False
        self.end_requested = True
        with self.condition:
            self.condition.notify()



        
