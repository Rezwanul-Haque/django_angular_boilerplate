import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

// Models
import { Flight } from '../models/flight';
// Services
import { FlightService } from '../services/flight.service';

@Component({
  selector: 'app-flight-list',
  templateUrl: './flight-list.component.html',
  styleUrls: ['./flight-list.component.css']
})
export class FlightListComponent implements OnInit {

  flights: Observable<Flight[]>;
  sucess: boolean = false;
  constructor(private flightService: FlightService) { }

  ngOnInit() {
    this.loadFlightData();
  }

  loadFlightData() {
    this.flights = this.flightService.getAllFlights();
  }

  deleteFlight(flightId) {
    this.flightService.deleteFlight(flightId).subscribe(
      data => {
        this.sucess = true;
        this.loadFlightData();
      },
      error => {
        console.log("Falied: ", error);
      }
    )
  }

  deleteAllFlights() {
    this.flightService.deleteAllFlights().subscribe(
      data => {
        this.sucess = true;
        this.loadFlightData();
      },
      error => {
        console.log("Falied: ", error);
      }
    )
  }

}
