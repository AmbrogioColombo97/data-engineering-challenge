# Backend Engineering Challenge

# Moving Average Calculation CLI

This README provides an overview of the CLI application designed to calculate the moving average of translation delivery times over a specified window of minutes.

## Overview

This command line application reads a stream of translation delivery events from a file and calculates a moving average of the delivery times for a specified window size in minutes. The results are output in a JSON format.

## Features

- Reads events from a JSON file.
- Calculates moving averages for delivery times over a specified window.
- Outputs results in a JSON format.

## Usage

### Prerequisites

- Python 3.x
- Required Python packages: `argparse`, `json`, `datetime`, `collections`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AmbrogioColombo97/data-engineering-challenge.git
   ```
   
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
### Running the application
   ```bash
   python unbabel_cli.py --input_file events.json --window_size 10
   ```
- input_file: Path to the input JSON file containing the events.
- window_size: Window size in minutes for calculating the moving average.   

### Example file input
    {"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 20}
	{"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 31}
	{"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb3","source_language": "en","target_language": "fr","client_name": "taxi-eats","event_name": "translation_delivered","nr_words": 100, "duration": 54}

### Example file output
```
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:22:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:23:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}
```