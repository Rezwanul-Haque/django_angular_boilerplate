import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Models
import { Flight } from '../models/flight';

@Injectable({
  providedIn: 'root'
})
export class FlightService {

  private endpoint = 'http://127.0.0.1:8000/flights/';

  constructor(private http: HttpClient) { }

  // Get all flights
  getAllFlights(): Observable<any> {
    return this.http.get(this.endpoint);
  }


}
