"use client"
import { useState } from "react";
import Header from "@/components/Header";
import Sidebar from "@/components/Sidebar";
import ChartCard from "@/components/ChartCard";

export default function Page() {
  const [numCharts, setNumCharts] = useState(4);
  return (
    <div className="h-screen flex flex-col">
      <Header />

      <div className="flex flex-1 overflow-hidden">
        <Sidebar />

        <main className="flex-1 p-6 bg-gray-100 overflow-auto">
          <div className="mb-4 flex items-center gap-2">
            <label htmlFor="chart-selector" className="text-sm font-semibold">
              Number of Charts:
            </label>
            <select
              id="chart-selector"
              value={numCharts}
              onChange={(e) => setNumCharts(parseInt(e.target.value))}
              className="px-3 py-2 border rounded-lg bg-white text-black"
            >
              <option value={1}>1</option>
              <option value={2}>2</option>
              <option value={3}>3</option>
              <option value={4}>4</option>
            </select>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-2 gap-6 h-full">
            {Array.from({ length: numCharts }).map((_, index) => (
              <ChartCard key={index} />
            ))}
          </div>
        </main>
      </div>
    </div>
  );
}
