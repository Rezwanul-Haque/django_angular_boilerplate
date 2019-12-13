import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
import { Observable } from 'rxjs';

// Models
import { Flight } from '../models/flight';
// Services
import { FlightService } from '../services/flight.service';

@Component({
  selector: 'app-flight-edit',
  templateUrl: './flight-edit.component.html',
  styleUrls: ['./flight-edit.component.css']
})
export class FlightEditComponent implements OnInit {

  flight: Observable<Flight>;
  flightId: number;
  sucess: boolean = false;
  trip_types = ['One Way', 'Round Trip', 'Multiple Destinations'];

  constructor(private flightService: FlightService,
              private activatedRoute: ActivatedRoute
    ) { }

  ngOnInit() {
    this.activatedRoute.paramMap.subscribe(
      params => {
        this.flightId = Number(params.get('id'));
      }
    )
    this.loadFlightData();
  }

  loadFlightData() {
    this.flightService.getFlight(this.flightId).subscribe(
      data => {
        this.flight = data;
      }
    )
  }

  onSubmit() {
    this.updateFlight();
  }

  updateFlight() {
    this.flightService.updateFlight(this.flightId, this.flight).subscribe(
      data => {
        this.flight = data as Observable<Flight>;
        this.sucess = true;
      },
      error => {
        console.log("Oops, can't update flight. " + error)
      }
    );
  }

}
