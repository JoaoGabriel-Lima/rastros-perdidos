import pygame

pygame.init()


# Andamento Casa 1
andamentoFase = []
valorTotalAndamento = 8
timerCasa1Total = 90
timerCasa1 = 90
casa1Completo = False


def casa1Update():
    # reduce timer by 1 each second
    global timerCasa1
    if casa1Completo:
        return
    if timerCasa1 > 0:
        timerCasa1 -= 1/60
    else:
        timerCasa1 = 0

# Andamento Casa 2
listaBotoes = []
buttongroupSala = pygame.sprite.Group()
buttongroupQuarto = pygame.sprite.Group()
andamentoFase2 = [0,0,0,0,0,0]
valorTotalAndamento2 = 6
casa2Completo = False

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, group, mapx=0, mapy=0):
        super().__init__(group)
        self.buttonNotPressed = pygame.image.load('assets/GUI/button.png')
        self.buttonPressed = pygame.image.load('assets/GUI/buttonPressed.png')
        self.image = self.buttonNotPressed
        self.rect = self.image.get_rect()
        self.rect.x = x * 48 + mapx
        self.rect.y = y * 48 + mapy
        self.pressed = False
    
    def activate(self):
        self.image = self.buttonPressed

    def disable(self):
        self.image = self.buttonNotPressed

# andamento Casa 3
casa3Completo = False

# andamento vila final
iniciarFaseFinal = False
faseFinalCompleto = False
def updateIniciarFaseFinal():
    global iniciarFaseFinal
    if casa1Completo and casa2Completo and casa3Completo:
        iniciarFaseFinal = True

# Andamento Jogo todo
balaofala = pygame.image.load('assets/GUI/balaotaylor2.png')
progresso = [0,0,0]
x = 20
y = 20
fonte = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 25)
dica1, dica2, dica3 = "??????????", "??????????", "??????????"
texto = [fonte.render(f"Dicas do assassino:", True, (255,255,255)), fonte.render(f"1. ?????????", True, (255,255,255)), fonte.render(f"2. ?????????", True, (255,255,255)), fonte.render(f"3. ?????????", True, (255,255,255))]

def update(index, valor = 1):
    global dica1, dica2, dica3
    if index == 0 and valor == 1:
        dica1 = "Cabelo preto"
    elif index == 0 and valor == 0:
        dica1 = "??????????"
    if index == 1 and valor == 1:
        dica2 = "Blusa vermelha"
    elif index == 1 and valor == 0:
        dica2 = "??????????"
    if index == 2 and valor == 1:
        dica3 = "Olhos azuis"
    elif index == 2 and valor == 0:
        dica3 = "??????????"
    


    texto[1] = fonte.render(f"1. {dica1}", True, (255,255,255))
    texto[2] = fonte.render(f"2. {dica2}", True, (255,255,255))
    texto[3] = fonte.render(f"3. {dica3}", True, (255,255,255))

update(progresso)

def draw(screen):
    # pygame.draw.rect(screen, (0,0,0), (x - 10, y - 10, 300, 135))
    box_image = pygame.image.load('assets/GUI/dicas.png')
    screen.blit(box_image, (x - 10, y - 10))
    for i in range(len(texto)):
        screen.blit(texto[i], (x+5, y + 10 + i * 30))

def resetValues():
    global andamentoFase, valorTotalAndamento, timerCasa1Total, timerCasa1, casa1Completo, listaBotoes, buttongroupSala, buttongroupQuarto, andamentoFase2, valorTotalAndamento2, casa2Completo, casa3Completo, iniciarFaseFinal, faseFinalCompleto, progresso, dica1, dica2, dica3
    andamentoFase = []
    valorTotalAndamento = 8
    timerCasa1Total = 90
    timerCasa1 = 90
    casa1Completo = False

    listaBotoes = []
    buttongroupSala = pygame.sprite.Group()
    buttongroupQuarto = pygame.sprite.Group()
    andamentoFase2 = [0,0,0,0,0,0]
    valorTotalAndamento2 = 6
    casa2Completo = False

    casa3Completo = False

    iniciarFaseFinal = False
    faseFinalCompleto = False

    progresso = [0,0,0]
    dica1, dica2, dica3 = "??????????", "??????????", "??????????"
    texto = [fonte.render(f"Dicas do assassino:", True, (255,255,255)), fonte.render(f"1. ?????????", True, (255,255,255)), fonte.render(f"2. ?????????", True, (255,255,255)), fonte.render(f"3. ?????????", True, (255,255,255))]
    update(0,0)
    update(1,0)
    update(2,0)