import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import RestaurantList from './RestaurantList';
import RestaurantDetail from './RestaurantDetail';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/restaurants" exact component={RestaurantList} />
          <Route path="/restaurants/:id" component={RestaurantDetail} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
