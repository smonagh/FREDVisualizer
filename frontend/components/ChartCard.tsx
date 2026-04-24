"use client";
import SeriesForm from "@/components/SeriesForm";
import Chart from "@/components/Chart";
import { useState } from "react";

export default function ChartCard() {
  const [chartData, setChartData] = useState<any[]>([]);
  return (
    <div className="bg-white rounded-2xl shadow p-4 flex flex-col">
      <div><SeriesForm onData={setChartData} /></div>
      <div className="flex-1 border-2 rounded-xl flex items-center justify-center text-gray-400">
        <Chart data={chartData} />
      </div>
    </div>
  );
}