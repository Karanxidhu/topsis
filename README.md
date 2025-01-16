# TOPSIS Analysis Tool

A Python-based command-line tool for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis on numerical datasets. This tool processes CSV files containing numerical data (int32, int64, float32, float64) and generates rankings based on multiple criteria.

## Overview

TOPSIS is a multi-criteria decision analysis method that helps identify the best alternative from a set of options based on multiple criteria. The tool normalizes the input data, applies weights to different criteria, and considers whether each criterion should be maximized or minimized.

## Prerequisites

- Python 3.7+
- Required Python packages:
  - pandas
  - numpy

Install dependencies using:
```bash
pip install pandas numpy
```

## Usage

```bash
python algo.py <source_csv> <weights> <impacts> <output_csv>
```

### Parameters

1. `source_csv`: Path to input CSV file
   - Must contain only numerical values (int32, int64, float32, float64)
   - First column will be used as index
   - No missing values allowed

2. `weights`: Comma-separated values representing weights for each column
   - Must sum to 1
   - Number of weights must match number of columns (excluding index)
   - Example: "0.25,0.25,0.25,0.25"

3. `impacts`: Comma-separated signs indicating whether each criterion should be maximized (+) or minimized (-)
   - Use '+' for criteria to be maximized
   - Use '-' for criteria to be minimized
   - Number of impacts must match number of columns (excluding index)
   - Example: "-,+,+,+"

4. `output_csv`: Path where the result CSV will be stored
A Python-based command-line tool for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis on numerical datasets. This tool processes CSV files containing numerical data (int32, int64, float32, float64) and generates rankings based on multiple criteria.
### Example

```bash
python algo.py data.csv 0.25,0.25,0.25,0.25 -,+,+,+ output.csv
```

### Input CSV Format

```csv
Model,Price,Storage,Battery,Performance
1,799,256,12,85
2,999,512,10,92
3,699,128,15,78
```

### Output CSV Format

```csv
Model,Price,Storage,Battery,Performance,TOPSIS Score,Rank
1,799,256,12,85,0.534,2
2,999,512,10,92,0.687,1
3,699,128,15,78,0.423,3
```

## Error Handling

The program will show appropriate error messages for:
- Invalid number of weights or impacts
- Invalid CSV format or data types
- Missing values in the dataset
- Invalid file paths
- Non-numeric data in columns

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
