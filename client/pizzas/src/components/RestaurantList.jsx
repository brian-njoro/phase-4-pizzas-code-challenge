import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Home() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
  }, []);

  return (
    <section>
      <h2>All restaurants</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
          </li>
        ))}
      </ul>
    </section>
  );
}


