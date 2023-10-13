import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './home';
import RestaurantsList from './RestaurantList';
import PizzasList from './PizzaList';
import RestaurantDetail from './RestaurantDetail';

function App() {
  return (
    <Router>
      <div>
        <main>
          <Routes>
            <Route path="/pizzas/:id" element={<PizzasList />} />
            <Route path="/restaurants" element={<RestaurantsList />} />
            <Route path="/" element={<Home />} />
            <Route  path="/restaurants/:id" element = { <RestaurantDetail />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
