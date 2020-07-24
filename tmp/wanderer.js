class Wanderer {
    constructor() {
        this.position = createVector(random(width), random(height));
        this.heading = random(TWO_PI);
        this.r = random(5.0, 30.0);
        this.speed = 1 // p5.Vector.random2D();

    }
  
    edges() {
      if (this.position.x > width) {
        this.position.x = 0;
      } else if (this.position.x < 0) {
        this.position.x = width;
      }
      if (this.position.y > height) {
        this.position.y = 0;
      } else if (this.position.y < 0) {
        this.position.y = height;
      }
    }

    update() {
        this.heading += 0.3 * random(-1, 1);
        this.position.x += this.speed * cos(this.heading);
        this.position.y += this.speed * sin(this.heading);
      }
    
      show() {
        strokeWeight(2);
        stroke(50);
        point(this.position.x, this.position.y);
      }
    }
