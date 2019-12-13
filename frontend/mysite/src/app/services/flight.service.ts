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

  // Get a single flight
  getFlight(id: number): Observable<any> {
    return this.http.get(this.endpoint + id);
  }

  // Get all flights
  getAllFlights(): Observable<any> {
    return this.http.get(this.endpoint);
  }

  // POST - Create flight
  createFlight(flightPayload: Flight): Observable<object> {
    return this.http.post(this.endpoint, flightPayload);
  }

  // PUT - Update flight
  updateFlight(id: number, flightPayload: any): Observable<object> {
    return this.http.put(this.endpoint + id, flightPayload);
  }
}
