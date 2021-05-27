from sense_hat import SenseHat
import time
import random
c=0
p = 10
s = SenseHat()
O=(0,0,0)
B=(0,0,255)
G=(0,255,0)
R=(255,0,0)
def unounouno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, B, B, O, B, B, 
    B, B, O, B, B, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo

def dueduedue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, G, G, O, G, G, 
    G, G, O, G, G, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def tretretre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, R, R, O, R, R, 
    R, R, O, R, R, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unounodue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, B, B, O, G, G, 
    B, B, O, B, B, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unounotre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, B, B, O, R, R, 
    B, B, O, B, B, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unoduedue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, G, G, O, G, G, 
    B, B, O, G, G, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unoduetre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, G, G, O, R, R, 
    B, B, O, G, G, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unodueuno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, G, G, O, B, B, 
    B, B, O, G, G, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unotreuno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, R, R, O, B, B, 
    B, B, O, R, R, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unotredue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, R, R, O, G, G, 
    B, B, O, R, R, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def unotretre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    B, B, O, R, R, O, R, R, 
    B, B, O, R, R, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def dueunodue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, B, B, O, G, G, 
    G, G, O, B, B, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def dueunotre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, B, B, O, R, R, 
    G, G, O, B, B, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def dueunouno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, B, B, O, B, B, 
    G, G, O, B, B, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def dueduetre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, G, G, O, R, R, 
    G, G, O, G, G, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def duedueuno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, G, G, O, B, B, 
    G, G, O, G, G, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def duetreuno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, R, R, O, B, B, 
    G, G, O, R, R, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def duetredue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, R, R, O, G, G, 
    G, G, O, R, R, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def duetretre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    G, G, O, R, R, O, R, R, 
    G, G, O, R, R, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def treunodue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, B, B, O, G, G, 
    R, R, O, B, B, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def treunotre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, B, B, O, R, R, 
    R, R, O, B, B, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def treduedue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, G, G, O, G, G, 
    R, R, O, G, G, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def treduetre():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, G, G, O, R, R, 
    R, R, O, G, G, O, R, R, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def tredueuno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, G, G, O, B, B, 
    R, R, O, G, G, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def tretreuno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, R, R, O, B, B, 
    R, R, O, R, R, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def tretredue():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, R, R, O, G, G, 
    R, R, O, R, R, O, G, G, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
def treunouno():
  logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    R, R, O, B, B, O, B, B, 
    R, R, O, B, B, O, B, B, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    ]
  return logo
images=[unounouno,dueduedue,tretretre,unounodue,unounotre,unoduedue,unoduetre,unodueuno,unotreuno,unotredue,unotretre,dueduetre,duedueuno,dueunodue,dueunotre,dueunouno,duetreuno,duetredue,duetretre,tretreuno,tretredue,tredueuno,treduedue,treduetre,treunouno,treunodue,treunotre]   

print("BENVENUTO NELLA SLOT MACHINE IN QUESTO GIOCO SE OTTIENI 5 NUMERI UGUALI VINCI 3 PUNTI SE SONO DIVERSI PERDI 1 PUNTO, SI PARTE CON 10 PUNTI, VINCI SE ARRIVI O SUPERI 15 PUNTI E PERDI SE FINISCI I TUOI PUNTI.")
print("VAI MUOVI IL JOYSTICK")
while c==0:
 for event in s.stick.get_events():
  if event.action == "pressed":
    d=random.randint(0,2)
    f=random.randint(0,2)
    g=random.randint(0,2)
    if d==f and f==g :
      p = p+5
      if d==1 and f==1 and g==1 :
        s.set_pixels(images[0]())
      if d==2 and f==2 and g==2 :
        s.set_pixels(images[1]())
      if d==0 and f==0 and g==0 :
        s.set_pixels(images[3]())
      print("NUMERI USCITI: "+str(d)+str(f)+str(g))
      print("HAI FATTO 2 PUNTI ORA IL TUO PUNTEGGIO E DI:"+str(p))
    else :
      p=p-1
      if d==1 and f==1 and g==2 :
        s.set_pixels(images[4]())
      if d==1 and f==1 and g==0 :
        s.set_pixels(images[5]())
      if d==1 and f==2 and g==2 :
        s.set_pixels(images[6]())
      if d==1 and f==2 and g==0 :
        s.set_pixels(images[7]())
      if d==1 and f==2 and g==1 :
        s.set_pixels(images[8]())
      if d==1 and f==0 and g==1 :
        s.set_pixels(images[9]())
      if d==1 and f==0 and g==2 :
        s.set_pixels(images[10]())
      if d==1 and f==0 and g==0 :
        s.set_pixels(images[11]())
      if d==2 and f==2 and g==0 :
        s.set_pixels(images[12]())
      if d==2 and f==2 and g==1 :
        s.set_pixels(images[13]())
      if d==2 and f==1 and g==2 :
        s.set_pixels(images[14]())
      if d==2 and f==1 and g==0 :
        s.set_pixels(images[15]())
      if d==2 and f==1 and g==1 :
        s.set_pixels(images[16]())
      if d==2 and f==0 and g==1 :
        s.set_pixels(images[17]()) 
      if d==2 and f==0 and g==2 :
        s.set_pixels(images[18]()) 
      if d==2 and f==0 and g==0 :
        s.set_pixels(images[19]())
      if d==0 and f==0 and g==1 :
        s.set_pixels(images[20]())
      if d==0 and f==0 and g==2 :
        s.set_pixels(images[21]())
      if d==0 and f==2 and g==1 :
        s.set_pixels(images[22]())
      if d==0 and f==2 and g==2 :
        s.set_pixels(images[23]())
      if d==0 and f==2 and g==0 :
        s.set_pixels(images[24]())
      if d==0 and f==1 and g==1 :
        s.set_pixels(images[25]())
      if d==0 and f==1 and g==2 :
        s.set_pixels(images[26]())
      if d==0 and f==1 and g==0 :
        s.set_pixels(images[27]())
      print("NUMERI USCITI: "+str(d)+str(f)+str(g))
      print("HAI PERSO 1 PUNTO F, ORA IL TUO PUNTEGGIO E DI: "+str(p))
    if p >= 15 :
      print("HAI SUPERATO I 20 PUNTI GG HAI VINTO")
      c = 1
    if p <= 0 :
      print("HAI PERSO F")
      c = 1
