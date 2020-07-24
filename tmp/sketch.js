// const flock = [];
const cluster = [];

function setup() {
  createCanvas(360, 360);
  cluster[0] = new Wanderer;
  cluster[0].trail = new Trail;
//   spider = new Wanderer;  
  // alignSlider = createSlider(0, 2, 1, 0.1);
  // cohesionSlider = createSlider(0, 2, 1, 0.1);
  // separationSlider = createSlider(0, 2, 1, 0.1);
//   for (let i = 0; i < 2; i++) {
//     flock.push(new Wanderer());
    
//   }

}


function draw() {

//   background(51);
  cluster[0].edges();
  cluster[0].update();
  cluster[0].show();
  cluster[0].trail.update();
//   cluster[0].trail.display();
//   for (let boid of flock) {
//     boid.edges();
//     // boid.flock(flock);
//     boid.update();
//     boid.show();
//   }

}
