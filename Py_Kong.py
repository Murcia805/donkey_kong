###############################################################################
###############################################################################
###############################################################################
###Bibliografia                                                             ###
###https://www.youtube.com/playlist?list=PL46E99FE946C1C946                 ###
###https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq ###
###https://www.youtube.com/playlist?list=PLpOqH6AE0tNherBf6bzGiDM1uIy_E0WJH ###
###https://www.youtube.com/playlist?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO ###
###############################################################################
###############################################################################
###############################################################################

import pygame

pygame.init()

pygame.display.set_caption("Donkey Kong")
color=(0,0,0)
blanco=(255,255,255)
pantalla=pygame.display.set_mode((720,480))

frame=pygame.time.Clock()



#Color Pantalla
pantalla.fill(color)

tipodeletra=pygame.font.SysFont("comicsansms",25)
otrotipodeletra=pygame.font.SysFont("comicsansms",15)

talves = True

#barriles
listbarl=pygame.sprite.Group()

class barriles(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load("barril1.png").convert_alpha()
        self.rect=self.imagen.get_rect()

        self.vel = 3

        self.rect.left,self.rect.top = (x,y)

        self.mox=0

    def colision(self,obj = pygame.sprite.Group()):
        self.gravedad(3)

        colision_lista=pygame.sprite.spritecollide(self,obj,False)
        for grupopiso in colision_lista:
            if self.rect.y > 0:
                #direccion arriba
                self.rect.bottom = grupopiso.rect.top
            elif self.rect.y < 0:
                #direccion abajo
                self.rect.top = grupopiso.rect.bottom

    def move(self):

        if 80 < self.rect.top < 150:
            self.rect.left +=5
        if 150 < self.rect.top < 300:
            self.rect.left -=5
        if 300 < self.rect.top < 400:
            self.rect.left+=5
        if 400 < self.rect.top < 600:
            self.rect.left-=5


    def gravedad(self, quieto):
        if self.rect.top == 0:
            self.rect.top += quieto
        else:
            self.rect.top += quieto

    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)

class jugador(pygame.sprite.Sprite):
    def __init__(self,width=25, height=25, left=10,top=370,hola=False):
        pygame.sprite.Sprite.__init__(self)
        self.imagen1=pygame.image.load("1.png").convert_alpha()
        self.imagen2=pygame.image.load("2.png").convert_alpha()
        self.imagen3=pygame.image.load("1.1.png").convert_alpha()
        self.imagen4=pygame.image.load("2.1.png").convert_alpha()
        self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
        self.anima=0
        self.orientacion=0
        self.imagen= self.imagenes[self.orientacion][0]

        self.rect = self.imagen.get_rect()
        self.rect.top,self.rect.left = (top,left)
        self.tieneg=hola

        self.hsvel=0
        self.vsvel=0

        self.tienemove=False
        self.ladoderecho=False
        self.ladoizquierdo=False

    def velocidad(self,hsvel,vsvel):
        self.hsvel += hsvel
        self.vsvel += vsvel

    def animacion(self,temp):
        if self.tienemove == True:
            if temp == 4:
                    self.orientacion+=1
            if self.ladoderecho == True:
                    self.imagen=self.imagenes[self.orientacion][0]
                    self.orientacion=0
            if self.ladoizquierdo == True:
                    self.imagen=self.imagenes[self.orientacion][1]
                    self.orientacion=0
        if self.tienemove == False:
            if self.ladoderecho == True:
                self.imagen=self.imagenes[0][0]
                self.ladoizquierdo=False
            if self.ladoizquierdo == True:
                self.imagen=self.imagenes[0][1]
                self.ladoderecho = False

    def colision(self,esc = pygame.sprite.Group(),obj = pygame.sprite.Group(), event = None):

        if self.tieneg == False:
            self.gravedad(2,2)

        self.rect.x += self.hsvel

        colision_lista=pygame.sprite.spritecollide(self,obj,False)

        for grupopiso in colision_lista:
            if self.hsvel > 0:
                #direccion derecha
                self.rect.right = grupopiso.rect.left
                self.tieneg=False
            elif self.hsvel < 0:
                #direccion izquierda
                self.rect.left = grupopiso.rect.right
                self.tieneg=False

        self.rect.y += self.vsvel

        colision_lista=pygame.sprite.spritecollide(self,obj,False)

        for grupopiso in colision_lista:
            if self.vsvel > 0:
                #direccion arriba
                self.rect.bottom = grupopiso.rect.top
                self.vsvel =0
                self.tieneg=False
            elif self.vsvel < 0:
                #direccion abajo
                self.rect.top = grupopiso.rect.bottom
                self.vsvel = 0
                self.tieneg=False

        if not event == None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.velocidad(-5,0)
                    self.tienemove=True
                    self.ladoizquierdo = True
                    self.ladoderecho = False
                    self.anima = 0
                if event.key == pygame.K_RIGHT:
                    self.velocidad(5,0)
                    self.tienemove=True
                    self.ladoderecho = True
                    self.ladoizquierdo=False
                    self.anima = 1
                if event.key == pygame.K_UP:
                    if self.vsvel == 0:
                        self.velocidad(0,-15)
                if event.key == pygame.K_DOWN:
                    self.velocidad(0,5)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if (self.hsvel != 0):
                        self.hsvel = 0
                        self.tienemove=False
                        self.ladoizquierdo=True
                        self.ladoderecho=False
                if event.key == pygame.K_RIGHT:
                    if (self.hsvel != 0):
                        self.hsvel = 0
                        self.tienemove=False
                        self.ladoderecho=True
                        self.ladoizquierdo=False
                if event.key == pygame.K_UP:
                    if (self.vsvel != 0):
                        self.vsvel = 0
                if event.key == pygame.K_DOWN:
                    if (self.vsvel != 0):
                        self.vsvel = 0

    def gravedad(self, quieto , fuergrav):
        if self.vsvel == 0:
            self.vsvel = quieto
        else:
            self.vsvel += fuergrav

    def colisionescalera(self,obj):
        if pygame.sprite.spritecollide(self,obj,False):
            self.tieneg=True
        if not pygame.sprite.spritecollide(self,obj,False):
            self.tieneg=False

    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)

class jugador1(pygame.sprite.Sprite):
    def __init__(self,left=10,top=370,hola=False):
        pygame.sprite.Sprite.__init__(self)
        self.imagen1=pygame.image.load("mart1.png").convert_alpha()
        self.imagen2=pygame.image.load("mart2.png").convert_alpha()
        self.imagen3=pygame.image.load("mart1.1.png").convert_alpha()
        self.imagen4=pygame.image.load("mart2.1.png").convert_alpha()
        self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
        self.anima=0
        self.orientacion=0
        self.imagen= self.imagenes[self.orientacion][0]

        self.rect = self.imagen.get_rect()

        self.rect.top,self.rect.left = (top,left)
        self.tieneg=hola

        self.hsvel=0
        self.vsvel=0

        self.tienemove=False
        self.ladoderecho=False
        self.ladoizquierdo=False

    def velocidad(self,hsvel,vsvel):
        self.hsvel += hsvel
        self.vsvel += vsvel

    def colision(self,esc = pygame.sprite.Group(),obj = pygame.sprite.Group(), event = None):

        if self.tieneg == False:
            self.gravedad(2,2)

        self.rect.left += self.hsvel

        colision_lista=pygame.sprite.spritecollide(self,obj,False)

        for grupopiso in colision_lista:
            if self.hsvel > 0:
                #direccion derecha
                self.rect.right = grupopiso.rect.left
                self.tieneg=False
            elif self.hsvel < 0:
                #direccion izquierda
                self.rect.left = grupopiso.rect.right
                self.tieneg=False

        self.rect.top += self.vsvel

        colision_lista=pygame.sprite.spritecollide(self,obj,False)

        for grupopiso in colision_lista:
            if self.vsvel > 0:
                #direccion arriba
                self.rect.bottom = grupopiso.rect.top
                self.vsvel =0
                self.tieneg=False
            elif self.vsvel < 0:
                #direccion abajo
                self.rect.top = grupopiso.rect.bottom
                self.vsvel = 0
                self.tieneg=False

        if not event == None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.velocidad(-5,0)
                    self.imagen=self.imagenes[0][1]
                    self.orientacion = 1
                if event.key == pygame.K_RIGHT:
                    self.velocidad(5,0)
                    self.imagen=self.imagenes[0][0]
                    self.orientacion = 0

                if event.key == pygame.K_SPACE:
                    self.imagen = self.imagenes[1][self.orientacion]
                if event.key == pygame.K_UP:
                    if self.vsvel == 0:
                        self.velocidad(0,-15)
                if event.key == pygame.K_DOWN:
                    self.velocidad(0,5)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if (self.hsvel != 0):
                        self.hsvel = 0
                        self.imagen=self.imagenes[0][1]
                if event.key == pygame.K_RIGHT:
                    if (self.hsvel != 0):
                        self.hsvel = 0
                        self.imagen=self.imagenes[0][0]
                if event.key == pygame.K_UP:
                    if (self.vsvel != 0):
                        self.vsvel = 0
                if event.key == pygame.K_DOWN:
                    if (self.vsvel != 0):
                        self.vsvel = 0
                if event.key == pygame.K_SPACE:
                    self.imagen = self.imagenes[0][self.orientacion]

    def gravedad(self, quieto , fuergrav):
        if self.vsvel == 0:
            self.vsvel = quieto
        else:
            self.vsvel += fuergrav

    def colisionescalera(self,obj):
        if pygame.sprite.spritecollide(self,obj,False):
            self.tieneg=True
        if not pygame.sprite.spritecollide(self,obj,False):
            self.tieneg=False

    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)

class enemigo(pygame.sprite.Sprite):
    def __init__(self,top=114,left=20):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=pygame.image.load("mono1.png").convert_alpha()
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(top,left)
    def dibujar(self):
        pantalla.blit(self.imagen,self.rect)

class princesa(pygame.sprite.Sprite):
    def __init__(self,top=40,left=218):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=pygame.image.load("princesa.png").convert_alpha()
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(top,left)
    def dibujar(self):
        pantalla.blit(self.imagen,self.rect)

class suelo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
    def dibujar(self):
        pantalla.blit(self.imagen,self.rect)
    def posicion(self,x,y):
        self.rect.left,self.rect.top=(x,y)
        self.dibujar()

class escalera(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen
        self.rect=self.imagen.get_rect()

    def posicion(self,x,y):
        self.rect.left,self.rect.top=(x,y)
    
    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)

def mensaje(txt,color,x,y):
        texinpantalla = tipodeletra.render(txt,True,color)
        pantalla.blit(texinpantalla,(x,y))

def puntajeyvida(vida):
    text1= tipodeletra.render("Vidas: "+str(vida), True, blanco)
    pantalla.blit(text1,[0,0])

def mensaje2(txt,color,x,y):
        texinpantalla = otrotipodeletra.render(txt,True,color)
        pantalla.blit(texinpantalla,(x,y))

def pausa():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausado = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            pantalla.fill(blanco)
            mensaje("PAUSADO",color,160,240)
            mensaje("Exit = q , Continue = p",color,160,340)
            pygame.display.update()
            frame.tick(5)

def main():
    hola = False

    tm=0

    vidas = 3

    event = None

    #musica
    oshe=pygame.mixer.Sound("m2.wav")
    oshe.play()

    #relos
    numFPS = 0
    FPS = 60
    start = 60
    azul = (0, 30, 255)
    font = pygame.font.Font(None,25)

    #Princesa
    peach = princesa()
    prin=pygame.sprite.Group()
    prin.add(peach)

    #enemigo
    enemi=enemigo()

    bar=barriles(20,125)
    listbarl.add(bar)

    tiempo=0

    #pisos
    pisos=pygame.image.load("piso1.png").convert_alpha()
    piso1=suelo(pisos)
    piso2=suelo(pisos)
    piso3=suelo(pisos)
    piso4=suelo(pisos)
    piso5=suelo(pisos)
    piso6=suelo(pisos)
    piso7=suelo(pisos)
    piso8=suelo(pisos)
    piso9=suelo(pisos)
    piso10=suelo(pisos)
    piso11=suelo(pisos)
    piso12=suelo(pisos)
    piso13=suelo(pisos)
    piso14=suelo(pisos)
    piso15=suelo(pisos)
    piso16=suelo(pisos)
    piso17=suelo(pisos)
    piso18=suelo(pisos)
    piso19=suelo(pisos)
    piso20=suelo(pisos)
    piso21=suelo(pisos)
    piso22=suelo(pisos)
    piso23=suelo(pisos)
    piso24=suelo(pisos)
    piso25=suelo(pisos)
    piso26=suelo(pisos)
    piso27=suelo(pisos)
    piso28=suelo(pisos)
    piso29=suelo(pisos)
    piso30=suelo(pisos)
    piso31=suelo(pisos)
    piso32=suelo(pisos)
    piso33=suelo(pisos)
    piso34=suelo(pisos)
    piso35=suelo(pisos)
    piso36=suelo(pisos)
    piso37=suelo(pisos)
    piso38=suelo(pisos)
    piso39=suelo(pisos)
    piso40=suelo(pisos)
    piso41=suelo(pisos)
    piso42=suelo(pisos)
    piso43=suelo(pisos)
    piso44=suelo(pisos)
    piso45=suelo(pisos)
    piso46=suelo(pisos)
    piso47=suelo(pisos)
    piso48=suelo(pisos)
    piso49=suelo(pisos)
    piso50=suelo(pisos)
    piso51=suelo(pisos)
    piso52=suelo(pisos)
    piso53=suelo(pisos)
    piso54=suelo(pisos)
    piso55=suelo(pisos)
    piso56=suelo(pisos)
    piso57=suelo(pisos)
    piso58=suelo(pisos)
    piso59=suelo(pisos)
    piso60=suelo(pisos)
    piso61=suelo(pisos)
    piso62=suelo(pisos)
    piso63=suelo(pisos)
    piso64=suelo(pisos)
    piso65=suelo(pisos)
    piso66=suelo(pisos)
    piso67=suelo(pisos)

    grupopiso=pygame.sprite.Group()
    grupopiso.add(piso1,piso2,piso3,piso4,piso5,piso6,piso7,piso8,
                  piso9,piso10,piso11,piso12,piso13,piso14,piso15,
                  piso16,piso17,piso18,piso19,piso20,piso21,piso22,
                  piso23,piso24,piso25,piso26,piso27,piso28,piso29,
                  piso30,piso31,piso32,piso33,piso34,piso35,piso36,
                  piso37,piso38,piso39,piso40,piso41,piso42,piso43,
                  piso44,piso45,piso46,piso47,piso48,piso49,piso50,
                  piso51,piso52,piso53,piso54,piso55,piso56,piso57,
                  piso58,piso59,piso60,piso61,piso62,piso63,piso64,
                  piso65,piso66,piso67)

    #escaleras
    escalera1=pygame.image.load("escalera1.png").convert_alpha()
    stair1=escalera(escalera1)
    stair2=escalera(escalera1)
    stair3=escalera(escalera1)
    stair4=escalera(escalera1)

    escaleras=pygame.sprite.Group()
    escaleras.add(stair1,stair2,stair3,stair4)

    #jugador
    player=jugador()

    jugadores=pygame.sprite.Group()
    jugadores.add(player)

    color2=((0,0,0))
    
    salir=False
    gameover=False
    
    while salir!= True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausa()

        tm+=1
        player.animacion(tm)

        if tm == 4:
            tm=0

        #Color Pantalla
        pantalla.fill(color)

        #Fps
        frame.tick(30)

        #escaleras posicion
        stair1.posicion(573,345)
        stair2.posicion(167,248)
        stair3.posicion(468,145)
        stair4.posicion(363,55)

        #posicion piso
        piso1.posicion(10,440)
        piso2.posicion(45,440)
        piso3.posicion(80,440)
        piso4.posicion(115,440)
        piso5.posicion(150,440)
        piso6.posicion(185,438)
        piso7.posicion(220,438)
        piso8.posicion(255,438)
        piso9.posicion(290,438)
        piso10.posicion(325,438)
        piso11.posicion(360,435)
        piso12.posicion(395,435)
        piso13.posicion(430,435)
        piso14.posicion(465,435)
        piso15.posicion(500,435)
        piso16.posicion(535,433)
        piso17.posicion(570,433)
        piso18.posicion(605,433)
        piso19.posicion(640,433)
        piso20.posicion(675,433)

        piso22.posicion(627,345)
        piso23.posicion(592,345)

        piso25.posicion(535,345)
        piso26.posicion(500,343)
        piso27.posicion(465,343)
        piso28.posicion(430,343)
        piso29.posicion(395,343)
        piso30.posicion(360,343)
        piso31.posicion(325,340)
        piso32.posicion(290,340)
        piso33.posicion(255,340)
        piso34.posicion(220,340)
        piso35.posicion(185,340)
        piso36.posicion(150,338)
        piso37.posicion(115,338)
        piso38.posicion(80,338)
        piso39.posicion(45,338)

        piso44.posicion(130,248)

        piso46.posicion(185,248)
        piso47.posicion(220,248)
        piso48.posicion(255,245)
        piso49.posicion(290,245)
        piso50.posicion(325,245)
        piso51.posicion(360,245)
        piso52.posicion(395,245)
        piso53.posicion(430,235)
        piso54.posicion(465,235)
        piso55.posicion(500,235)
        piso56.posicion(535,235)

        piso61.posicion(395,145)
        piso62.posicion(430,145)
        piso63.posicion(485,145)

        piso21.posicion(10,145)
        piso24.posicion(45,145)

        piso40.posicion(80,145)
        piso41.posicion(115,145)
        piso42.posicion(150,145)
        piso43.posicion(185,145)
        piso45.posicion(220,145)

        piso57.posicion(255,145)
        piso58.posicion(290,145)
        piso59.posicion(325,145)
        piso60.posicion(360,145)

        piso64.posicion(220,55)
        piso65.posicion(255,55)
        piso66.posicion(290,55)
        piso67.posicion(325,55)

        #dibujar princesa
        peach.dibujar()

        #dibujar escalera
        stair1.dibujar(pantalla)
        stair2.dibujar(pantalla)
        stair3.dibujar(pantalla)
        stair4.dibujar(pantalla)

        #dibujar escalera
        stair1.dibujar(pantalla)
        stair2.dibujar(pantalla)

        puntajeyvida(vidas)

        for x in listbarl:
            x.dibujar(pantalla)
            x.colision(grupopiso)
            x.move()

        #tiempo caen barriles
        if tiempo == 40:
            bar=barriles(20,125)
            listbarl.add(bar)
            tiempo=0
        tiempo +=1


        #dibujar enemigo
        enemi.dibujar()

        #if pygame.sprite.spritecollide(player,groupmartillo,False):
        #    tienemartillo = True

        #colisiones + Gravedad + Movimiento
        player.colision(escaleras,grupopiso,event)
        event = None
        #Salir del esenario
        if player.rect.left >= 770 or player.rect.left <= -50 or player.rect.top >= 600:
                vidas -= 1
                player.rect.top,player.rect.left=(370,10)
                if vidas == 0:
                    gameover = True
        #colision
        if pygame.sprite.spritecollide(player,listbarl,False):
            vidas -= 1
            player.rect.top,player.rect.left=(370,10)
            if vidas == 0:
                gameover = True
        #dtescaler
        player.colisionescalera(escaleras)

        #dibujar en pantalla los Sprites
        player.dibujar(pantalla)

        if pygame.sprite.spritecollide(player,prin,False):
            quit()
        #if tienemartillo == True:
            #colisiones + Gravedad + Movimiento
            #pjmartillo.colision(escaleras,grupopiso,event)
            #event = None
            #Salir del esenario
            #if pjmartillo.rect.left >= 770 or pjmartillo.rect.left <= -50 or pjmartillo.rect.top >= 600:
            #        vidas -= 1
            #        pjmartillo.rect.top,pjmartillo.rect.left=(370,10)
            #        if vidas == 0:
            #            gameover = True
            #colision con barriles
            #if (pjmartillo.imagen == pjmartillo.imagenes[1][0]) or (pjmartillo.imagen == pjmartillo.imagenes[1][1]):
            #    if pygame.sprite.spritecollide(pjmartillo,listbarl,False):
            #        listbarl.remove(bar)

            #if (pjmartillo.imagen == pjmartillo.imagenes[0][0]) or (pjmartillo.imagen == pjmartillo.imagenes[0][1]):
            #    if pygame.sprite.spritecollide(pjmartillo,listbarl,False):
            #        pjmartillo.rect.top,pjmartillo.rect.left=(370,10)
            #        vidas -= 1
            #        if vidas == 0:
            #            gameover = True
            #dtescaler
            #pjmartillo.colisionescalera(escaleras)

            #dibujar en pantalla los Sprites
            #pjmartillo.dibujar(pantalla)

            #if pygame.sprite.spritecollide(pjmartillo,prin,False):
            #    salir = False

        #Cronometro
        totseg  = start - (numFPS // FPS)
        if totseg < 0:
            totseg = 0
        minutes = totseg // 60
        seconds = totseg % 60
        outtext = "Time left:{0:2}:{1:00}".format(minutes,seconds)
        salir = False
        text = font.render(outtext, False, azul)
        pantalla.blit(text, [400, 4])
        numFPS +=1

        if totseg == 0:
            salir = True

        #actualizacion
        pygame.display.update()

        #loop secundario
        while gameover == True:
            pantalla.fill(color)
            mensaje(("Perdiste, s para salir, r para reiniciar"),blanco,160,240)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        salir = True
                        gameover = False
                    if event.key == pygame.K_r:
                        main()
                    else:
                        pass

    pygame.quit()

#menu
def intro():
    talves = True
    pygame.mixer.music.load("m1.wav")
    pygame.mixer.music.play()

    while talves == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pantalla.fill((255,255,255))
        mensaje("Bienvenidos a Py Donkey Kong",(0,0,0),160,240)

        boton(100,300,100,50,(34,177,76),(34,255,76),"menuplay")
        mensaje("Jugar",(0,0,0),110,305)

        boton(300,300,100,50,(134,54,156),(200,54,255),"opciones")
        mensaje("Reglas",(0,0,0),310,310)

        boton(500,300,100,50,(40,150,210),(40,220,255),"exit")
        mensaje("Salir",(0,0,0),510,310)

        pygame.display.update()
        frame.tick(30)

def vropciones():
    vropcione = True

    while vropcione == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pantalla.fill((255,255,255))
        mensaje("Te mueves con los direccionales del teclado",(0,0,0),120,50)
        mensaje("Presiona P para entrar en el menu de pausa",(0,0,0),120,100)
        mensaje("Rescata a la princesa que esta en manos de Donkey Kong",(0,0,0),20,150)
        mensaje("para ganar, ¡Suerte!",(0,0,0),200,180)

        boton(300,300,100,50,(134,54,156),(200,54,255),"menu")
        mensaje("Menu",(0,0,0),310,310)

        pygame.display.update()
        frame.tick(30)

def cualjuego():
    vropcione = True
    pygame.mixer.music.stop()

    while vropcione == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pantalla.fill((255,255,255))
        mensaje("Escoje el nivel de Dificultad",(0,0,0),160,200)

        boton(300,300,100,50,(134,54,156),(200,54,255),"play1")
        mensaje2("John Cena",(0,0,0),320,310)

        boton(500,300,100,50,(40,150,210),(40,220,255),"play2")
        mensaje2("Terminator",(0,0,0),515,310)


        pygame.display.update()
        frame.tick(30)

def boton(x,y,width,height,colorinactivo,coloractivo,action=None):

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(pantalla,coloractivo,(x,y,width,height))
        if click[0]==1 and action != None:
            if action == "menu":
                intro()
            if action == "menuplay":
                cualjuego()
            if action == "play1":
                main()
            if action == "play2":
                def main3():
                    pygame.init()

                    pygame.display.set_caption("Donkey Kong")
                    color=(0,0,0)
                    blanco=(255,255,255)
                    pantalla=pygame.display.set_mode((720,480))

                    frame=pygame.time.Clock()

                    #Color Pantalla
                    pantalla.fill(color)

                    tipodeletra=pygame.font.SysFont("comicsansms",25)

                    talves = True

                    class barriles(pygame.sprite.Sprite):
                        def __init__(self,x ,y):
                            pygame.sprite.Sprite.__init__(self)
                            self.imagen = pygame.image.load("barril1.png").convert_alpha()
                            self.rect=self.imagen.get_rect()

                            self.vel = 3

                            self.rect.left,self.rect.top = (x,y)

                            self.mox=0

                        def colision(self,obj = pygame.sprite.Group()):
                            self.gravedad(3)

                            colision_lista=pygame.sprite.spritecollide(self,obj,False)

                            for grupopiso in colision_lista:
                                if self.rect.y > 0:
                                    #direccion arriba
                                    self.rect.bottom = grupopiso.rect.top
                                elif self.rect.y < 0:
                                    #direccion abajo
                                    self.rect.top = grupopiso.rect.bottom

                        def move1(self):
                            self.rect.left+=1
                        def move2(self):
                            self.rect.left-=1
                        def move3(self):
                            if 80 < self.rect.top < 150:
                                self.rect.left +=5
                            if 150 < self.rect.top < 300:
                                self.rect.left -=5
                            if 300 < self.rect.top < 400:
                                self.rect.left+=5
                            if 400 < self.rect.top < 600:
                                self.rect.left-=5


                        def gravedad(self, quieto):
                            if self.rect.top == 0:
                                self.rect.top += quieto
                            else:
                                self.rect.top += quieto

                        def dibujar(self,superficie):
                            superficie.blit(self.imagen,self.rect)

                    class jugador(pygame.sprite.Sprite):
                        def __init__(self,width=25, height=25, left=10,top=370,hola=False):
                            pygame.sprite.Sprite.__init__(self)
                            self.imagen1=pygame.image.load("1.png").convert_alpha()
                            self.imagen2=pygame.image.load("2.png").convert_alpha()
                            self.imagen3=pygame.image.load("1.1.png").convert_alpha()
                            self.imagen4=pygame.image.load("2.1.png").convert_alpha()
                            self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
                            self.anima=0
                            self.orientacion=0
                            self.imagen= self.imagenes[self.orientacion][0]

                            self.rect = self.imagen.get_rect()
                            self.rect.top,self.rect.left = (top,left)
                            self.tieneg=hola

                            self.hsvel=0
                            self.vsvel=0

                            self.tienemove=False
                            self.ladoderecho=False
                            self.ladoizquierdo=False

                        def velocidad(self,hsvel,vsvel):
                            self.hsvel += hsvel
                            self.vsvel += vsvel

                        def animacion(self,temp):
                            if self.tienemove == True:
                                if temp == 4:
                                        self.orientacion+=1
                                if self.ladoderecho == True:
                                        self.imagen=self.imagenes[self.orientacion][0]
                                        self.orientacion=0
                                if self.ladoizquierdo == True:
                                        self.imagen=self.imagenes[self.orientacion][1]
                                        self.orientacion=0
                            if self.tienemove == False:
                                if self.ladoderecho == True:
                                    self.imagen=self.imagenes[0][0]
                                    self.ladoizquierdo=False
                                if self.ladoizquierdo == True:
                                    self.imagen=self.imagenes[0][1]
                                    self.ladoderecho = False

                        def colision(self,esc = pygame.sprite.Group(),obj = pygame.sprite.Group(), event = None):

                            if self.tieneg == False:
                                self.gravedad(2,2)

                            self.rect.x += self.hsvel

                            colision_lista=pygame.sprite.spritecollide(self,obj,False)

                            for grupopiso in colision_lista:
                                if self.hsvel > 0:
                                    #direccion derecha
                                    self.rect.right = grupopiso.rect.left
                                    self.tieneg=False
                                elif self.hsvel < 0:
                                    #direccion izquierda
                                    self.rect.left = grupopiso.rect.right
                                    self.tieneg=False

                            self.rect.y += self.vsvel

                            colision_lista=pygame.sprite.spritecollide(self,obj,False)

                            for grupopiso in colision_lista:
                                if self.vsvel > 0:
                                    #direccion arriba
                                    self.rect.bottom = grupopiso.rect.top
                                    self.vsvel =0
                                    self.tieneg=False
                                elif self.vsvel < 0:
                                    #direccion abajo
                                    self.rect.top = grupopiso.rect.bottom
                                    self.vsvel = 0
                                    self.tieneg=False

                            if not event == None:
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_LEFT:
                                        self.velocidad(-5,0)
                                        self.tienemove=True
                                        self.ladoizquierdo = True
                                        self.ladoderecho = False
                                        self.anima = 0
                                    if event.key == pygame.K_RIGHT:
                                        self.velocidad(5,0)
                                        self.tienemove=True
                                        self.ladoderecho = True
                                        self.ladoizquierdo=False
                                        self.anima = 1
                                    if event.key == pygame.K_UP:
                                        if self.vsvel == 0:
                                            self.velocidad(0,-15)
                                    if event.key == pygame.K_DOWN:
                                        self.velocidad(0,5)
                                if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_LEFT:
                                        if (self.hsvel != 0):
                                            self.hsvel = 0
                                            self.tienemove=False
                                            self.ladoizquierdo=True
                                            self.ladoderecho=False
                                    if event.key == pygame.K_RIGHT:
                                        if (self.hsvel != 0):
                                            self.hsvel = 0
                                            self.tienemove=False
                                            self.ladoderecho=True
                                            self.ladoizquierdo=False
                                    if event.key == pygame.K_UP:
                                        if (self.vsvel != 0):
                                            self.vsvel = 0
                                    if event.key == pygame.K_DOWN:
                                        if (self.vsvel != 0):
                                            self.vsvel = 0

                        def gravedad(self, quieto , fuergrav):
                            if self.vsvel == 0:
                                self.vsvel = quieto
                            else:
                                self.vsvel += fuergrav

                        def colisionescalera(self,obj):
                            if pygame.sprite.spritecollide(self,obj,False):
                                self.tieneg=True
                            if not pygame.sprite.spritecollide(self,obj,False):
                                self.tieneg=False

                        def dibujar(self,superficie):
                            superficie.blit(self.imagen,self.rect)

                    class jugador1(pygame.sprite.Sprite):
                        def __init__(self,left=10,top=370,hola=False):
                            pygame.sprite.Sprite.__init__(self)
                            self.imagen1=pygame.image.load("mart1.png").convert_alpha()
                            self.imagen2=pygame.image.load("mart2.png").convert_alpha()
                            self.imagen3=pygame.image.load("mart1.1.png").convert_alpha()
                            self.imagen4=pygame.image.load("mart2.1.png").convert_alpha()
                            self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
                            self.anima=0
                            self.orientacion=0
                            self.imagen= self.imagenes[self.orientacion][0]

                            self.rect = self.imagen.get_rect()

                            self.rect.top,self.rect.left = (top,left)
                            self.tieneg=hola

                            self.hsvel=0
                            self.vsvel=0

                            self.tienemove=False
                            self.ladoderecho=False
                            self.ladoizquierdo=False

                        def velocidad(self,hsvel,vsvel):
                            self.hsvel += hsvel
                            self.vsvel += vsvel

                        def colision(self,esc = pygame.sprite.Group(),obj = pygame.sprite.Group(), event = None):

                            if self.tieneg == False:
                                self.gravedad(2,2)

                            self.rect.left += self.hsvel

                            colision_lista=pygame.sprite.spritecollide(self,obj,False)

                            for grupopiso in colision_lista:
                                if self.hsvel > 0:
                                    #direccion derecha
                                    self.rect.right = grupopiso.rect.left
                                    self.tieneg=False
                                elif self.hsvel < 0:
                                    #direccion izquierda
                                    self.rect.left = grupopiso.rect.right
                                    self.tieneg=False

                            self.rect.top += self.vsvel

                            colision_lista=pygame.sprite.spritecollide(self,obj,False)

                            for grupopiso in colision_lista:
                                if self.vsvel > 0:
                                    #direccion arriba
                                    self.rect.bottom = grupopiso.rect.top
                                    self.vsvel =0
                                    self.tieneg=False
                                elif self.vsvel < 0:
                                    #direccion abajo
                                    self.rect.top = grupopiso.rect.bottom
                                    self.vsvel = 0
                                    self.tieneg=False

                            if not event == None:
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_LEFT:
                                        self.velocidad(-5,0)
                                        self.imagen=self.imagenes[0][1]
                                        self.orientacion = 1
                                    if event.key == pygame.K_RIGHT:
                                        self.velocidad(5,0)
                                        self.imagen=self.imagenes[0][0]
                                        self.orientacion = 0

                                    if event.key == pygame.K_SPACE:
                                        self.imagen = self.imagenes[1][self.orientacion]
                                    if event.key == pygame.K_UP:
                                        if self.vsvel == 0:
                                            self.velocidad(0,-15)
                                    if event.key == pygame.K_DOWN:
                                        self.velocidad(0,5)
                                if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_LEFT:
                                        if (self.hsvel != 0):
                                            self.hsvel = 0
                                            self.imagen=self.imagenes[0][1]
                                    if event.key == pygame.K_RIGHT:
                                        if (self.hsvel != 0):
                                            self.hsvel = 0
                                            self.imagen=self.imagenes[0][0]
                                    if event.key == pygame.K_UP:
                                        if (self.vsvel != 0):
                                            self.vsvel = 0
                                    if event.key == pygame.K_DOWN:
                                        if (self.vsvel != 0):
                                            self.vsvel = 0
                                    if event.key == pygame.K_SPACE:
                                        self.imagen = self.imagenes[0][self.orientacion]

                        def gravedad(self, quieto , fuergrav):
                            if self.vsvel == 0:
                                self.vsvel = quieto
                            else:
                                self.vsvel += fuergrav

                        def colisionescalera(self,obj):
                            if pygame.sprite.spritecollide(self,obj,False):
                                self.tieneg=True
                            if not pygame.sprite.spritecollide(self,obj,False):
                                self.tieneg=False

                        def dibujar(self,superficie):
                            superficie.blit(self.imagen,self.rect)

                    class enemigo(pygame.sprite.Sprite):
                        def __init__(self,top=114,left=310):
                            pygame.sprite.Sprite.__init__(self)
                            self.imagen=pygame.image.load("mono1.png").convert_alpha()
                            self.rect=self.imagen.get_rect()
                            self.rect.top,self.rect.left=(top,left)
                        def dibujar(self):
                            pantalla.blit(self.imagen,self.rect)

                    class princesa(pygame.sprite.Sprite):
                        def __init__(self,top=63,left=218):
                            pygame.sprite.Sprite.__init__(self)
                            self.imagen=pygame.image.load("princesa.png").convert_alpha()
                            self.rect=self.imagen.get_rect()
                            self.rect.top,self.rect.left=(top,left)
                        def dibujar(self):
                            pantalla.blit(self.imagen,self.rect)

                    class suelo(pygame.sprite.Sprite):
                        def __init__(self,imagen):
                            pygame.sprite.Sprite.__init__(self)
                            self.imagen=imagen
                            self.rect=self.imagen.get_rect()
                        def dibujar(self):
                            pantalla.blit(self.imagen,self.rect)
                        def posicion(self,x,y):
                            self.rect.left,self.rect.top=(x,y)
                            self.dibujar()

                    class escalera(pygame.sprite.Sprite):
                        def __init__(self,imagen):
                            pygame.sprite.Sprite.__init__(self)
                            self.imagen=imagen
                            self.rect=self.imagen.get_rect()

                        def posicion(self,x,y):
                            self.rect.left,self.rect.top=(x,y)

                        def dibujar(self,superficie):
                            superficie.blit(self.imagen,self.rect)

                    def mensaje(txt,color,x,y):
                            texinpantalla = tipodeletra.render(txt,True,color)
                            pantalla.blit(texinpantalla,(x,y))

                    def puntajeyvida(vida):
                        text1= tipodeletra.render("Vidas: "+str(vida), True, blanco)
                        pantalla.blit(text1,[0,0])

                    def pausa():
                        pausado = True
                        while pausado:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_p:
                                        pausado = False
                                    elif event.key == pygame.K_q:
                                        pygame.quit()
                                        quit()
                                pantalla.fill(blanco)
                                mensaje("PAUSADO",color,160,240)
                                mensaje("Exit = q , Continue = p",color,160,340)
                                pygame.display.update()
                                frame.tick(5)

                    def main2():

                        tm=0

                        vidas = 3

                        event = None

                        musicacy=pygame.mixer.Sound("m3.wav")
                        musicacy.play()

                        #reloj
                        numFPS = 0
                        FPS = 60
                        start  =150
                        azul = (0, 30, 255)
                        font = pygame.font.Font(None,25)

                        #Princesa
                        peach = princesa()
                        prin=pygame.sprite.Group()
                        prin.add(peach)

                        #enemigo
                        enemi=enemigo()
                        #barriles
                        listbarl=pygame.sprite.Group()
                        listbar2=pygame.sprite.Group()
                        listbar3=pygame.sprite.Group()
                        #listbar4=pygame.sprite.Group()

                        bar=barriles(310,130)
                        listbarl.add(bar)

                        tiempo=0

                        #pisos
                        pisos=pygame.image.load("piso1.png").convert_alpha()
                        piso1=suelo(pisos)
                        piso2=suelo(pisos)
                        piso3=suelo(pisos)
                        piso4=suelo(pisos)
                        piso5=suelo(pisos)
                        piso6=suelo(pisos)
                        piso7=suelo(pisos)
                        piso8=suelo(pisos)
                        piso9=suelo(pisos)
                        piso10=suelo(pisos)
                        piso11=suelo(pisos)
                        piso12=suelo(pisos)
                        piso13=suelo(pisos)
                        piso14=suelo(pisos)
                        piso15=suelo(pisos)
                        piso16=suelo(pisos)
                        piso17=suelo(pisos)
                        piso18=suelo(pisos)
                        piso19=suelo(pisos)
                        piso20=suelo(pisos)
                        piso21=suelo(pisos)
                        piso22=suelo(pisos)
                        piso23=suelo(pisos)
                        piso24=suelo(pisos)
                        piso25=suelo(pisos)
                        piso26=suelo(pisos)
                        piso27=suelo(pisos)
                        piso28=suelo(pisos)
                        piso29=suelo(pisos)
                        piso30=suelo(pisos)
                        piso31=suelo(pisos)
                        piso32=suelo(pisos)
                        piso33=suelo(pisos)
                        piso34=suelo(pisos)
                        piso35=suelo(pisos)
                        piso36=suelo(pisos)
                        piso37=suelo(pisos)
                        piso38=suelo(pisos)
                        piso39=suelo(pisos)
                        piso40=suelo(pisos)
                        piso41=suelo(pisos)
                        piso42=suelo(pisos)
                        piso43=suelo(pisos)
                        piso44=suelo(pisos)
                        piso45=suelo(pisos)
                        piso46=suelo(pisos)
                        piso47=suelo(pisos)
                        piso48=suelo(pisos)
                        piso49=suelo(pisos)
                        piso50=suelo(pisos)
                        piso51=suelo(pisos)
                        piso52=suelo(pisos)
                        piso53=suelo(pisos)
                        piso54=suelo(pisos)
                        piso55=suelo(pisos)
                        piso56=suelo(pisos)
                        piso57=suelo(pisos)
                        piso58=suelo(pisos)
                        piso59=suelo(pisos)
                        piso60=suelo(pisos)
                        piso61=suelo(pisos)
                        piso62=suelo(pisos)
                        piso63=suelo(pisos)
                        piso64=suelo(pisos)
                        piso65=suelo(pisos)
                        piso66=suelo(pisos)
                        piso67=suelo(pisos)

                        grupopiso=pygame.sprite.Group()
                        grupopiso.add(piso1,piso2,piso3,piso4,piso5,piso6,piso7,piso8,
                                      piso9,piso10,piso11,piso12,piso13,piso14,piso15,
                                      piso16,piso17,piso18,piso19,piso20,piso21,piso22,
                                      piso23,piso24,piso25,piso26,piso27,piso28,piso29,
                                      piso30,piso31,piso32,piso33,piso34,piso35,piso36,
                                      piso37,piso38,piso39,piso40,piso41,piso42,piso43,
                                      piso44,piso45,piso46,piso47,piso48,piso49,piso50,
                                      piso51,piso52,piso53,piso54,piso55,piso56,piso57,
                                      piso58,piso59,piso60,piso61,piso62,piso63,piso64,
                                      piso65,piso66,piso67)

                        #escaleras
                        escalera1=pygame.image.load("escalera1.png").convert_alpha()
                        stair1=escalera(escalera1)
                        stair2=escalera(escalera1)
                        stair3=escalera(escalera1)
                        stair4=escalera(escalera1)
                        stair5=escalera(escalera1)
                        stair6=escalera(escalera1)
                        stair7=escalera(escalera1)


                        escaleras=pygame.sprite.Group()
                        escaleras.add(stair1,stair2,stair3,stair4,stair5,stair6,stair7)

                        #jugador
                        player=jugador()

                        jugadores=pygame.sprite.Group()
                        jugadores.add(player)

                        color2=((0,0,0))

                        salir=False
                        gameover=False

                        while salir!= True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    salir = True
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_p:
                                        pausa()

                            tm+=1
                            player.animacion(tm)

                            if tm == 4:
                                tm=0

                            #Color Pantalla
                            pantalla.fill(color)

                            #Fps
                            frame.tick(30)

                            #escaleras posicion
                            stair1.posicion(573,350)
                            stair2.posicion(167,258)
                            stair3.posicion(468,168)
                            stair4.posicion(363,78)
                            stair5.posicion(97,350)
                            stair6.posicion(540,258)
                            stair7.posicion(237,168)

                            #posicion piso
                            piso1.posicion(10,440)
                            piso2.posicion(45,440)
                            piso3.posicion(80,440)
                            piso4.posicion(115,440)
                            piso5.posicion(150,440)
                            piso6.posicion(185,440)
                            piso7.posicion(220,440)
                            piso8.posicion(255,440)
                            piso9.posicion(290,440)
                            piso10.posicion(325,440)
                            piso11.posicion(360,440)
                            piso12.posicion(395,440)
                            piso13.posicion(430,440)
                            piso14.posicion(465,440)
                            piso15.posicion(500,440)
                            piso16.posicion(535,440)
                            piso17.posicion(570,440)
                            piso18.posicion(605,440)
                            piso19.posicion(640,440)
                            piso20.posicion(675,440)

                            piso22.posicion(627,348)
                            piso23.posicion(592,348)

                            piso25.posicion(535,348)
                            #piso26.posicion(500,343)
                            #piso27.posicion(465,343)
                            #piso28.posicion(430,343)
                            #piso29.posicion(395,343)
                            #piso30.posicion(360,343)
                            #piso31.posicion(325,340)
                            #piso32.posicion(290,340)
                            #piso33.posicion(255,340)
                            #piso34.posicion(220,340)
                            #piso35.posicion(185,348)
                            piso36.posicion(150,348)
                            piso37.posicion(115,348)
                            #piso38.posicion(80,348)
                            piso39.posicion(59,348)

                            piso44.posicion(130,260)

                            piso46.posicion(185,258)
                            piso47.posicion(220,258)
                            #piso48.posicion(255,245)
                            #piso49.posicion(290,245)
                            #piso50.posicion(325,245)
                            #piso51.posicion(360,245)
                            #piso52.posicion(395,245)
                            piso53.posicion(430,258)
                            piso54.posicion(465,258)
                            piso55.posicion(500,258)
                            piso56.posicion(558,258)

                            piso61.posicion(395,167)
                            piso62.posicion(430,167)
                            piso63.posicion(485,167)

                            #piso21.posicion(10,145)
                            #piso24.posicion(45,145)

                            #piso40.posicion(80,145)
                            #piso41.posicion(115,145)
                            #piso42.posicion(150,145)
                            piso43.posicion(198,167)
                            #piso45.posicion(220,145)

                            piso57.posicion(255,167)
                            piso58.posicion(290,167)
                            piso59.posicion(325,167)
                            piso60.posicion(360,167)

                            piso64.posicion(220,78)
                            piso65.posicion(255,78)
                            piso66.posicion(290,78)
                            piso67.posicion(325,78)

                            #dibujar princesa
                            peach.dibujar()

                            #dibujar escalera
                            stair1.dibujar(pantalla)
                            stair2.dibujar(pantalla)
                            stair3.dibujar(pantalla)
                            stair4.dibujar(pantalla)
                            stair5.dibujar(pantalla)
                            stair6.dibujar(pantalla)
                            stair7.dibujar(pantalla)

                            puntajeyvida(vidas)

                            for x in listbarl:
                                x.dibujar(pantalla)
                                x.colision(grupopiso)
                                x.move1()
                            for x in listbar2:
                                x.dibujar(pantalla)
                                x.colision(grupopiso)
                                x.move2()
                            for x in listbar3:
                                x.dibujar(pantalla)
                                x.colision(grupopiso)
                                x.move3()
                            #for x in listbar4:
                            #    x.dibujar(pantalla)
                            #    x.colision(grupopiso)
                            #    x.move4()

                            #tiempo caen barriles
                            if tiempo == 30:
                                bar2 = barriles(310,130)
                                listbar3.add(bar2)

                            #if tiempo == 35:
                            #    bar3=barriles(310,130)
                            #    listbar4.add(bar3)

                            if tiempo == 40:
                                bar=barriles(310,130)
                                bar1=barriles(310,130)
                                listbarl.add(bar)
                                listbar2.add(bar1)
                                tiempo=0
                            tiempo +=1


                            #dibujar enemigo
                            enemi.dibujar()

                            #if pygame.sprite.spritecollide(player,groupmartillo,False):
                            #    tienemartillo = True

                            #colisiones + Gravedad + Movimiento
                            player.colision(escaleras,grupopiso,event)
                            event = None
                            #Salir del esenario
                            if player.rect.left >= 770 or player.rect.left <= -50 or player.rect.top >= 600:
                                    vidas -= 1
                                    player.rect.top,player.rect.left=(370,10)
                                    if vidas <= 0:
                                        gameover = True

                            #colision
                            if pygame.sprite.spritecollide(player,listbarl,False):
                                vidas -= 1
                                player.rect.top,player.rect.left=(370,10)
                            if pygame.sprite.spritecollide(player,listbar2,False):
                                vidas -= 1
                                player.rect.top,player.rect.left=(370,10)
                            if pygame.sprite.spritecollide(player,listbar3,False):
                                vidas -= 1
                                player.rect.top,player.rect.left=(370,10)
                                if vidas <= 0:
                                    gameover = True
                            #dtescaler
                            player.colisionescalera(escaleras)

                            #dibujar en pantalla los Sprites
                            player.dibujar(pantalla)

                            if pygame.sprite.spritecollide(player,prin,False):
                                quit()

                            #if tienemartillo == True:
                                #colisiones + Gravedad + Movimiento
                            #    pjmartillo.colision(escaleras,grupopiso,event)
                            #    event = None
                            #    #Salir del esenario
                            #    if pjmartillo.rect.left >= 770 or pjmartillo.rect.left <= -50 or pjmartillo.rect.top >= 600:
                            #            vidas -= 1
                            #            pjmartillo.rect.top,pjmartillo.rect.left=(370,10)
                            #            if vidas == 0:
                            #                gameover = True
                                #colision con barriles
                            #    if (pjmartillo.imagen == pjmartillo.imagenes[1][0]) or (pjmartillo.imagen == pjmartillo.imagenes[1][1]):
                            #        if pygame.sprite.spritecollide(pjmartillo,listbarl,False):
                            #            listbarl.remove(bar)
                            #        if pygame.sprite.spritecollide(pjmartillo,listbar2,False):
                            #            listbar2.remove(bar)
                            #        if pygame.sprite.spritecollide(pjmartillo,listbar3,False):
                            #            listbar3.remove(bar)

                            #    if (pjmartillo.imagen == pjmartillo.imagenes[0][0]) or (pjmartillo.imagen == pjmartillo.imagenes[0][1]):
                            #        if pygame.sprite.spritecollide(pjmartillo,listbarl,False):
                            #            pjmartillo.rect.top,pjmartillo.rect.left=(370,10)
                            #            vidas -= 1
                            #        if pygame.sprite.spritecollide(pjmartillo,listbar2,False):
                            #            pjmartillo.rect.top,pjmartillo.rect.left=(370,10)
                            #            vidas -= 1
                            #        if pygame.sprite.spritecollide(pjmartillo,listbar3,False):
                            #            pjmartillo.rect.top,pjmartillo.rect.left=(370,10)
                            #            vidas -= 1
                            #        if vidas == 0:
                            #            gameover = True
                                #dtescaler
                            #    pjmartillo.colisionescalera(escaleras)

                                #dibujar en pantalla los Sprites
                            #    pjmartillo.dibujar(pantalla)

                            #    if pygame.sprite.spritecollide(pjmartillo,prin,False):
                            #        salir = False

                            totseg  = start - (numFPS // FPS)
                            if totseg < 0:
                                totseg = 0
                            minutes = totseg // 60
                            seconds = totseg % 60
                            outtext = "Time left:{0:02}:{1:00}".format(minutes,seconds)
                            text = font.render(outtext, False, azul)
                            pantalla.blit(text, [400, 4])
                            numFPS +=1

                            #actualizacion
                            pygame.display.update()

                            #loop secundario
                            while gameover == True:
                                pantalla.fill(color)
                                mensaje(("Perdiste, s para salir, r para reiniciar"),blanco,160,240)
                                pygame.display.update()

                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_s:
                                            salir = True
                                            gameover = False
                                        if event.key == pygame.K_r:
                                            main2()
                                        else:
                                            pass

                        pygame.quit()

                    main2()
                    pygame.quit()
                main3()
            if action == "opciones":
                vropciones()
            if action == "exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(pantalla,colorinactivo,(x,y,width,height))
#menu
intro()
pygame.quit()
