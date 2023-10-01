import React, { useState, useEffect } from 'react';

export default function PizzaList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch('/pizzas')
      .then((response) => response.json())
      .then((data) => setPizzas(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h2>Pizzas</h2>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>{pizza.name}</li>
        ))}
      </ul>
    </div>
  );
}


