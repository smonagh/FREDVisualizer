# FREDVisualizer

A powerful visualization tool for Federal Reserve Economic Data (FRED). Easily fetch, analyze, and display economic indicators with an intuitive interface.

## Features

- **Data Retrieval**: Fetch real-time economic data from the FRED API
- **Interactive Visualizations**: Create and customize charts for economic indicators
- **Data Comparison**: Compare multiple economic series side-by-side
- **User-Friendly Interface**: Intuitive design for quick analysis

## Requirements

- Python 3.8+
- Node
- Docker
- FRED API Key (get one at [https://fred.stlouisfed.org/docs/api/](https://fred.stlouisfed.org/docs/api/))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FREDVisualizer.git
   cd FREDVisualizer
   ```

2. Set up your FRED API key:
   ```bash
   export FRED_API_KEY="your_api_key_here"
   ```

## Usage

Run the application:
```bash
docker compose up
```

Then navigate to the interface and:
1. Enter a FRED series ID (e.g., `GDP`, `UNRATE`)
2. Select your desired date range
3. Choose visualization type
4. Click "Generate" to display the chart

## API Documentation

For more information about available FRED series, visit:
- [FRED Series Search](https://fred.stlouisfed.org/series/)
- [FRED API Documentation](https://fred.stlouisfed.org/docs/api/)

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Support

For issues or questions, please open an issue on GitHub or contact the maintainers.
