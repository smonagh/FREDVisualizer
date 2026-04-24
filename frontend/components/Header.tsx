"use client";

import React, { useState } from "react";
import Image from "next/image";
import ChartCard from "@/components/ChartCard";

export default function Header() {

  return (
    <header className="h-16 bg-gray-900 text-white flex items-center justify-between px-6 shadow">
      <Image src="/logo-2.png" alt="FREDVisualizer Logo" width={120} height={40} />
    </header>
  );
}