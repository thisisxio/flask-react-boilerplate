import React, { useState } from "react";
import Link from "next/link";
// import { AiOutlineClose, AiOutlineMenu } from "react-icons/ai";

export default function Navigation() {
  // Toggle function to handle the navbar's display

  const navItems = [
    { id: 0, text: "Home", url: "/" },
    { id: 2, text: "Research", url: "/research" },
    // { id: 3, text: "Resources" },
    // { id: 4, text: "About" },
    { id: 5, text: "Log In", url: "/log-in" },
  ];

  return (
    <nav className="bg-white">
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        <Link
          href="/"
          className="flex items-center space-x-3 rtl:space-x-reverse"
        >
          Logo
        </Link>
        <button className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm rounded-lg md:hidden">
          <span className="sr-only">Open Main menu</span>
          <svg
            className="w-5 h-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 17 14"
          >
            <path
              stroke="#050909"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M1 1h15M1 7h15M1 13h15"
            />
          </svg>
        </button>
        <div className="hidden w-full md:block md:w-auto">
          <ul className=" font-medium flex flex-col p-4 md:p-0 mt-4 rounded-lg  md:flex-row md:space-x-8 rtl:space-x-reverse md:bg-white ">
            {navItems.map((item) => (
              <li className="block py-2 px-3 text-black rounded md:p-0 cursor-pointer duration-300 hover:text-black">
                <Link key={item.id} href={item.url}>
                  {item.text}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </nav>
  );
}
