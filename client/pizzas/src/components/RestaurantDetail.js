import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

export default function RestaurantDetail() {
  const { id } = useParams();
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    fetch(`/restaurants/${id}`)
      .then((response) => {
        if (response.status === 404) {
          throw new Error('Restaurant not found');
        }
        return response.json();
      })
      .then((data) => setRestaurant(data))
      .catch((error) => console.error(error));
  }, [id]);

  if (!restaurant) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h2>{restaurant.name}</h2>
      <p>Address: {restaurant.address}</p>
      <h3>Pizzas:</h3>
      <ul>
        {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id}>{pizza.name}</li>
        ))}
      </ul>
    </div>
  );
}

