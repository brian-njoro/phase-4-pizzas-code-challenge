import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

export default function PizzasList() {
  const [{ data: pizza, error, status }, setPizza] = useState({
    data: null,
    error: null,
    status: "pending",
  });
  const { id } = useParams();

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/pizzas/${id}`).then((r) => {
      if (r.ok) {
        r.json().then((pizza) =>
          setPizza({ data: pizza, error: null, status: "resolved" })
        );
      } else {
        r.json().then((err) =>
          setPizza({ data: null, error: err.error, status: "rejected" })
        );
      }
    });
  }, [id]);

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error.error}</h1>;

  return (
    <section>
      <h2>{pizza.name}</h2>
      <p>{pizza.ingredients}</p>
    </section>
  );
}

 
