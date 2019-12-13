import { Component, OnInit } from '@angular/core';

// Models
import { Flight } from '../models/flight';
// Services
import { FlightService } from '../services/flight.service';

@Component({
  selector: 'app-flight-create',
  templateUrl: './flight-create.component.html',
  styleUrls: ['./flight-create.component.css']
})
export class FlightCreateComponent implements OnInit {

  flight: Flight = new Flight();
  sucess: boolean = false;
  trip_types = ['One Way', 'Round Trip', 'Multiple Destinations'];

  constructor(private flightService: FlightService) { }

  ngOnInit() {
  }

  onSubmit() {
    this.saveFlight();
  }

  saveFlight() {
    this.flightService.createFlight(this.flight).subscribe(
      data => {
        this.sucess = true;
        console.log("New flight added!!")
      },
      error => {
        console.log("Sorry, Flight cannot be saved. " + error)
      }
    );
  }

}
