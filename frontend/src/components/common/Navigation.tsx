import React, { useState } from "react";
import { AiOutlineClose, AiOutlineMenu } from "react-icons/ai";

export default function Navigation() {
  // Toggle function to handle the navbar's display

  const navItems = [
    { id: 1, text: "Home" },
    { id: 2, text: "Company" },
    { id: 3, text: "Resources" },
    { id: 4, text: "About" },
    { id: 5, text: "Contact" },
  ];

  return (
    <nav className="bg-black flex flex-row justify-between items-center h-24 max-w-[1240px] mx-auto px-4 text-white">
      {/* Logo */}
      <h1 className="w-auto text-3xl font-bold text-[#00df9a]">Logo</h1>

      <ul className=" flex">
        {navItems.map((item) => (
          <li
            key={item.id}
            className="p-4 hover:text-[#00df9a] rounded-xl m-2 cursor-pointer duration-300 hover:text-black"
          >
            {item.text}
          </li>
        ))}
      </ul>
    </nav>
  );
}
