import { useEffect, useState } from "react";

export default function Home() {
  const [properties, setProperties] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/properties")
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log(data);
        setProperties(data);
      });
  }, []);
  return (
    <div>
      <h4>Property Lists</h4>
      {properties.map((property) => (
        <>
          <h4>{property.name}</h4>
          <p>{property.price}</p>
        </>
      ))}
    </div>
  );
}
