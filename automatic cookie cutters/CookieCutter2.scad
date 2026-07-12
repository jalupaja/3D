wallThick = 2;
cutterMinimum = 1; // Aiming for double line thickness for strength
baseHeight = 1.5;
height = 12;
flangeWidth = 4;
stampDepth = 1;
lineDepth = 1.5;
fileName = "epsilon.dxf";
cookiecutter();
//stamp();
module stamp() {
union(){
	difference() {
		difference(){
			baseShape(stampDepth + baseHeight);
			translate([0,0,baseHeight]) linear_extrude(height=stampDepth*1.1) import(file = fileName, layer = "Stamp");
		}
		translate([0,0,-1]) {
			minkowski() { outline(); cylinder(r = 0.8, h = (stampDepth + baseHeight)*2);}
		}
	}
}
}
module cookiecutter() {
	difference(){ //Cut holes in the flange
	union(){ //Add the supports and lines
	difference(){ //Cut out the inside of the cutter
		minkowski(){ 
			outline(cutterMinimum/2);
			cylinder(r1 = wallThick/3, r2 = cutterMinimum/2, h = height);
		}
		baseShape(height + baseHeight * 2);
	}
	flange();
	supports(baseHeight);
	lines(height - lineDepth);
	}
	holes(height + baseHeight * 2);
	};
}
module flange(){
  difference(){
    minkowski(){
      baseShape(baseHeight/2);
      cylinder(r = flangeWidth, h = baseHeight/2);
    }
    translate([0,0,-baseHeight/2])baseShape(baseHeight*2);
  };
}
module supports(H){
	linear_extrude(height=H) import(file = fileName, layer = "Supports");
}
module holes(H){
	translate([0,0,-H]) linear_extrude(height=H*3) import(file = fileName, layer = "Holes");
}
module baseShape(H){
	linear_extrude(height=H) import(file = fileName, layer = "CC");
}
module lines(H){
	linear_extrude(height=H) import(file = fileName, layer = "Lines");
}
module outline(thickness){
  difference(){
    minkowski(){
      baseShape(baseHeight/3);
      cylinder(r = thickness, h = baseHeight/3);
    }
    translate([0,0,-baseHeight/2]) baseShape(baseHeight*2);
  };
};
