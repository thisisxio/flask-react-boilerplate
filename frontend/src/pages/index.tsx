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
    <div className="h-auto py-4 mx-auto max-w-[1240px] px-4">
      <h2 className="text-xl font-bold">Property Lists</h2>
      <div className="py-4 flex">
        {properties.length ? (
          properties.map(
            (property: { name: string; address: string; price: number }) => (
              <div className="px-2 py-2 border">
                <h4>
                  {" "}
                  <span className="font-bold">Address:</span>
                  {property.address}
                </h4>
                <h4>
                  <span className="font-bold">Price:</span>${property.price}
                </h4>
              </div>
            )
          )
        ) : (
          <p className=" text-base text-center">No properties found </p>
        )}
      </div>
    </div>
  );
}
