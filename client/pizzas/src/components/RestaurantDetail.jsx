import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

export default function RestaurantDetail() {
    const [{ data: restaurant, error, status }, setRestaurant] = useState({
      data: null,
      error: null,
      status: "pending",
    });
    const { id } = useParams();
  
    useEffect(() => {
      fetch(`http://127.0.0.1:5000/restaurants/${id}`).then((r) => {
        if (r.ok) {
          r.json().then((hero) =>
            setRestaurant({ data: hero, error: null, status: "resolved" })
          );
        } else {
          r.json().then((err) =>
            setRestaurant({ data: null, error: err.error, status: "rejected" })
          );
        }
      });
    }, [id]);
  
    if (status === "pending") return <h1>Loading...</h1>;
    if (status === "rejected") return <h1>Error: {error.error}</h1>;
  
    return (
      <section>
        <h2>{restaurant.name}</h2>
        <h2>{restaurant.address}</h2>
  
        <h3>Pizzas:</h3>
        <ul>
          {restaurant.pizzas ? (
            restaurant.pizzas.map((pizza) => (
              <li key={pizza.id}>
                <Link to={`/pizzas/${pizza.id}`}>{pizza.name}</Link>
              </li>
            ))
          ) : (
            <li>No pizzas available.</li>
          )}
        </ul>

      </section>
    );
  }
  
  