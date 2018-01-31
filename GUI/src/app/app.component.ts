import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  counter = 10;
  LunchNow() 
  {
	  if(this.counter >0)
	  {
	 	 setTimeout(()=>{this.LunchNow()}, 1000);
	 	 this.counter = this.counter -1; 
	  }
	  if(this.counter == 0)
	  {
		  window.location.href = "http://www.proziod.com/"
	  }
  }
}
