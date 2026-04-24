import React, { useState } from "react";

export default function Sidebar() {
  const [searchQuery, setSearchQuery] = useState("");
  const [searchLoading, setSearchLoading] = useState(false);
  const [searchResults, setSearchResults] = useState([]);
  const [showDropdown, setShowDropdown] = useState(false);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!searchQuery.trim()) return;

    try {
      setSearchLoading(true);
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/search/${encodeURIComponent(searchQuery)}`,
        { method: "GET" }
      );

      if (!res.ok) {
        throw new Error("Search failed");
      }

      const data = await res.json();
      console.log("Search results:", data);
      setSearchResults(data["data"] || []);
      setShowDropdown(true);
    } catch (err) {
      console.error("Search error:", err);
    } finally {
      setSearchLoading(false);
    }
  };
  return (
    <aside className="w-64 bg-gray-800 text-white p-4">
    <div>
      <form onSubmit={handleSearch} className="flex flex-col gap-2 mb-4">
        <input
        type="text"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        placeholder="Search for series..."
        className="px-3 py-2 rounded-lg bg-white text-black text-sm w-full"
        />
        <button
        type="submit"
        disabled={searchLoading}
        className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm disabled:opacity-50 w-full"
        >
        {searchLoading ? "..." : "Search"}
        </button>
      </form>
      {showDropdown && (
        <div className="bg-gray-700 rounded-lg shadow-lg max-h-64 overflow-y-auto">
        {searchResults.length > 0 ? (
          searchResults.map((result: any, index: number) => (
            <div
            key={index}
            className="px-4 py-2 hover:bg-gray-600 cursor-pointer border-b last:border-b-0"
            >
            <div className="font-semibold text-sm">{result.id}</div>
            <div className="text-xs text-gray-400">{result.title}</div>
            </div>
          ))
        ) : (
          <div className="px-4 py-2">
            <p className="text-sm text-gray-400">No results found</p>
          </div>
        )}
        </div>
      )}
    </div>
    </aside>
  );
}