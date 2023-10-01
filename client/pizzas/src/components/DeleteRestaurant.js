import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';

function DeleteRestaurant() {
  const { id } = useParams();
  const history = useHistory();

  const handleDelete = () => {
    fetch(`/restaurant/${id}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if (response.status === 404) {
          throw new Error('Restaurant not found');
        }
        return response.json();
      })
      .then(() => {
        history.push('/restaurants');
      })
      .catch((error) => console.error(error));
  };

  return (
    <div>
      <h2>Delete Restaurant</h2>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
}

export default DeleteRestaurant;
