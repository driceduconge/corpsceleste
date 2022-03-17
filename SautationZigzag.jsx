#includepath "C:/Users/creep/Documents";
#include "basiljs/bundle/basil.js";

function draw() {


  d = b.doc();

  b.clear( d );

  for(var os = 0; os < d.objectStyles.length; os ++){
    switch(d.objectStyles[os].name){
      case "image":
        var imageStyle = d.objectStyles[os];
      break;
    }
  }

  b.units( b.CM );

  b.canvasMode(b.MARGIN);

  b.noStroke();

  // b.rect(0,0,10,10);

  b.imageMode(b.CORNER);
  var image = b.image("image.tif", (b.width - 5)/2, b.height - 5, 5, 5);

  image.appliedObjectStyle = imageStyle;

  rotation(image, 25);


  var largeur = 15;
  var decalY = -1;
  var posX = 0;
  var sensX = 1;
  var distance = .75;

  for(var i = 0; i<40; i++){

    if(i%(largeur*2-2) == 0 || i%(largeur*2-2) >= largeur){
      decalY++;
    }
    var rectangle = b.rect(posX*distance,decalY*distance,1,2);

    rotation(rectangle, b.random(45) - 22.5);


    posX = posX + sensX;
    if(posX == 0 || posX >= largeur-1){
      sensX = sensX * -1;
    }

  }

}

function rotation(object, angle){
  var myTrans = app.transformationMatrices.add({counterclockwiseRotationAngle:angle});
  object.transform(CoordinateSpaces.pasteboardCoordinates, AnchorPoint.CENTER_ANCHOR, myTrans);
}


b.go();
