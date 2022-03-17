#includepath "C:/Users/creep/Documents";

#include "basiljs/bundle/basil.js";

var loops = 0;
var liste_blocs = {};

function draw() {


  d = b.doc();

  b.clear(d);

  for (var os = 0; os < d.objectStyles.length; os++) {
    switch (d.objectStyles[os].name) {
      case "image":
        var imageStyle = d.objectStyles[os];
        break;
    }
  }

  b.units(b.CM);

  b.canvasMode(b.MARGIN);

  b.noStroke();

  // b.rect(0,0,10,10);

  b.imageMode(b.CENTER);


  var file = File('D:/A4_S2/Mulhouse_BPM/Basil/data/data_mtsclf1.csv'); // get the file
  var csv_data = []
  file.encoding = 'WINDOWS-1252'; // set some encoding
  file.lineFeed = "Windows";
  file.open('r'); // read the file
  do {
    csv_data.push(file.readln())
  } while (!file.eof);
  file.close();
  var data = []; // will hold the data
  var keys = csv_data[0].split(','); // get the heads
  // loop the data*/
  for (var i = 1; i < csv_data.length; i++) {
    var obj = {}; // temp object
    var cells = csv_data[i].split(','); // get the cells
    // assign them to the heads
    obj[keys[3]] = cells[3];
    obj[keys[2]] = cells[2];
    obj[keys[10]] = cells[10];

    data.push(obj); // add to data
  }

  var temp_console = [];

  for (var i = 0; i < data.length; i++) {
    if (tempPx >= d.documentPreferences.pageWidth) {
      posX = 0;
      decalY += 10
    }
    //on recupere les mot-clefs
    var mots_clefs = data[i]["mots"];

    var mot_array = mots_clefs.split("|")
    var encodage = 0;
    var encodage_nom = 0;
    //pour chaque mot
    for (var a = 0; a < mot_array.length; a++) {
      for (var ltr = 0; ltr < mot_array[a].length; ltr++) { //chaque lettre
        encodage += mot_array[a].charCodeAt(ltr);
      }
    }
    for (var ltr = 0; ltr < data[i]["nom"].length; ltr++) { //chaque lettre
      encodage_nom += data[i]["nom"].charCodeAt(ltr);
    }
    temp_console.push(" encodage : " + encodage.toString()+" noms : " + encodage_nom.toString());

    if(encodage_nom<=400){var tempPx = b.map(encodage_nom, 200, 500, 0, 15);}
    else if (encodage_nom>=600 && encodage_nom<=900) {var tempPx = b.map(encodage_nom, 600, 900, 16, 43);}
    else{var tempPx = b.map(encodage_nom, 1000, 1900, 43,  d.documentPreferences.pageHeight);}

    if(encodage<=1000){var tempPy = b.map(encodage, 0, 1000, 0, 20);}
    else if (encodage>=2000 && encodage<=3500) {var tempPy = b.map(encodage, 2000, 3500, 22, 72);}
    else{var tempPy = b.map(encodage, 3500, 5000, 72,  d.documentPreferences.pageHeight);}
    var image = b.image(data[i]["fichier"].toString(), tempPx, tempPy);

    image.appliedObjectStyle = imageStyle;
    rotation(image, b.random(45) - 22.5);

    if (loops >= 1) {
      for (var name in liste_blocs) {
        oldImage = liste_blocs[name]
        while(b.itemX(image) - b.itemWidth(image)/2 < b.itemX(oldImage) + b.itemWidth(oldImage)/2 &&
              b.itemX(image) + b.itemWidth(image)/2 > b.itemX(oldImage) - b.itemWidth(oldImage)/2 &&
              b.itemY(image) - b.itemHeight(image)/2 < b.itemY(oldImage) + b.itemHeight(oldImage)/2 &&
              b.itemY(image) + b.itemHeight(image)/2 > b.itemY(oldImage) - b.itemHeight(oldImage)/2){
          tempPx +=0.1;tempPy+=0.1;
          b.itemX(image, tempPx);b.itemY(image, tempPy);
        }

      }
    }
    liste_blocs[loops] = image;
    //var old_decalY = decalY;
    var tempImage = image;
    loops++;
    posX = tempPx;
    tempPy = tempPy;
  }
  var page = d.pages.item(0);

  var tf = page.textFrames.add({
    geometricBounds: [10, 10, 60, 60],
    contents: temp_console.toSource()
  });

}




function rotation(object, angle) {
  var myTrans = app.transformationMatrices.add({
    counterclockwiseRotationAngle: angle
  });
  object.transform(CoordinateSpaces.pasteboardCoordinates, AnchorPoint.CENTER_ANCHOR, myTrans);
}


b.go();
