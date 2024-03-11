import React from 'react';
import MapContainer from './Map'; // Import the MapContainer component from Map.js

// Main component of the React application
const App = () => {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      {/* Render the MapContainer component */}
      <MapContainer />
    </div>
  );
};

// Export the App component
export default App;
