import React, { useEffect, useState } from 'react';
import { Map, GoogleApiWrapper, Marker, InfoWindow } from 'google-maps-react';
import BASE_URL from './config.js'; // import base URL from configuration file 

// This component represents the map and its markers
const MapContainer = ({ google }) => {
  // State to store the fetched data from the Flask backend
  const [data, setData] = useState([]);
  const [selectedMarker, setSelectedMarker] = useState(null);
  const [apiKey, setApiKey] = useState('');

  // Fetch data from Flask backend when the component mounts
  useEffect(() => {
    fetchData();
    fetchApiKey();
  }, []);

  // Function to fetch data from the Flask backend
  const fetchData = async () => {
    try {
      // Fetch data from the Flask backend API endpoint
      // const response = await fetch('http://127.0.0.1:5000/api/locations');
      const response = await fetch(`${BASE_URL}/api/locations`);
      // Parse the response as JSON
      const jsonData = await response.json();
      // Set the fetched data to the state
      setData(jsonData);
    } catch (error) {
      // Log any errors that occur during the fetch operation
      console.error('Error fetching data:', error);
    }
  };

  const handleMarkerClick = (marker) => {
    console.log('Marker clicked:', marker);
    setSelectedMarker(marker);
  };

  const handleCloseInfoWindow = () => {
    setSelectedMarker(null);
  };

  const fetchApiKey = async () => {
    try {
      // const response = await fetch('http://127.0.0.1:5000/api/gmaps-api-key');
      const response = await fetch(`${BASE_URL}/api/gmaps-api-key`);
      const jsonData = await response.json();
      setApiKey(jsonData.api_key);
    } catch (error) {
      console.error('Error fetching API key:', error);
    }
  };

  // Render the map and markers using Google Maps API
  return (
    <Map
      // Pass the Google API object received from GoogleApiWrapper
      google={google}
      // Set the initial zoom level of the map
      zoom={4}
      // Set the initial center of the map
      initialCenter={{ lat: 51.5072178, lng: -0.1275862 }}
      // Set the style of the map
      style={{ width: '100%', height: '100%' }}
      // Pass the API key to the Map component
      apiKey = {apiKey}
    >
      {/* Iterate through the fetched data and render a marker for each coordinate */}
      {data.map((item, index) => (
        <Marker
          // Assign a unique key to each marker
          key={index}
          // Set the position of the marker using the lat and lng properties of the data item
          position={{ lat: item.lat, lng: item.lng }}
          onClick={() => handleMarkerClick(item)}
        />
      ))}
    </Map>
  );
};

// Higher-order component provided by google-maps-react to wrap the MapContainer component
export default GoogleApiWrapper({
  // Pass your Google Maps API key as the apiKey prop | pass null initially as we are fetching the key data dynamically
  apiKey: null
})(MapContainer);
