import { useEffect, useState } from "react";

export default function Home() {
  const [properties, setProperties] = useState([]);
  //   useEffect(() => {
  //     fetch("http://127.0.0.1:5000/api/properties")
  //       .then((res) => {
  //         return res.json();
  //       })
  //       .then((data) => {
  //         console.log(data);
  //         setProperties(data);
  //       });
  //   }, []);
  return (
    <div className="h-auto py-4 mx-auto max-w-[1240px] px-4">
      <h2 className="text-xl font-bold font-title">Property Lists</h2>
      <div className="py-4 flex">LANDING PAGE</div>
    </div>
  );
}
