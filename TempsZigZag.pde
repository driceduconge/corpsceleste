void setup() {

  size(400, 400);

  background(255);

  int largeur = 7;
  int decalY = -1;
  int posX = 0;
  int sensX = 1;
  int distance= 20;

  for (int i=0; i<40; i++) {

    if (i%(largeur*2 - 2) == 0 || i%(largeur*2 - 2) >= largeur) {
      decalY ++;
    }
    rect(posX * distance, decalY * distance, 10, 10);
    posX = posX + sensX;
    if (posX == 0 || posX >=(largeur-1)) {
      sensX = sensX * -1;
    }
  }
}
