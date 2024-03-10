import React, { Component } from 'react';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

class MapContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      locations: [] // This will hold the location coordinates fetched from backend
    };
  }

  componentDidMount() {
    // Update this.state.locations with the fetched coordinates
    fetch('backend/path')
}

  render() {
    return (
      <Map
        google={this.props.google}
        zoom={8}
        initialCenter={{ lat: 37.7749, lng: -122.4194 }} // Initial center of the map
      >
        {this.state.locations.map((location, index) => (
          <Marker
            key={index}
            position={{ lat: location.lat, lng: location.lng }}
          />
        ))}
      </Map>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: 'AIzaSyDNgl2UOlCrczRmcmIi8zJRNgYbaRx6paY' // Replace with your Google Maps API key
})(MapContainer);
