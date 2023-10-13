import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; 
import Home from './home';
import RestaurantList from './RestaurantList';
import RestaurantDetail from "./RestaurantDetail"
import PizzaList from './PizzaList';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/restaurants/:id" element={<RestaurantDetail />} />
        <Route path = "/restaurants" element={<RestaurantList />} />
        <Route path = "/pizzas" element = {<PizzaList />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;
