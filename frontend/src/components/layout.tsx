import { Inter } from "next/font/google";
import React from "react";
import Footer from "./common/Footer";
import Navigation from "./common/Navigation";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <>
      <Navigation />
      <div className="min-h-screen">{children}</div>

      <Footer />
    </>
  );
}
