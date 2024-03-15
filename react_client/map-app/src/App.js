import React from 'react';
import MapContainer from './Map'; // Import the MapContainer component from Map.js
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Main component of the React application
const App = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<MapContainer/>} />
      </Routes>
    </Router>
//    <div style={{ width: '100vw', height: '100vh' }}>
//      {/* Render the MapContainer component */}
//      <MapContainer />
//    </div>
  );
};

// Export the App component
export default App;
