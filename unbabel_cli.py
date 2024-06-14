import json
import argparse
from datetime import datetime, timedelta
from collections import deque

def parse_args():
    """
    Parses command line arguments for input file and window size.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='Calculate moving average delivery time for translations.')
    parser.add_argument('--input_file', required=True, help='Path to the input JSON file.')
    parser.add_argument('--window_size', type=int, required=True, help='Window size in minutes for moving average.')
    return parser.parse_args()

def load_events(input_file):
    """
    Loads events from a JSON file.

    Args:
        input_file (str): Path to the input JSON file.

    Returns:
        list: List of events loaded from the JSON file.
    """
    with open(input_file, 'r') as f:
        return [json.loads(line) for line in f]

def calculate_moving_averages(events, window_size):
    """
    Calculates the moving average delivery time for a specified window size.

    Args:
        events (list): List of events.
        window_size (int): Window size in minutes for moving average.

    Returns:
        dict: Dictionary with datetime keys and moving average delivery time values.
    """
    window = deque()
    results = {}
    current_time = None
    sum_durations = 0
    count_durations = 0

    for event in events:
        event_time = datetime.strptime(event["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
        duration = event["duration"]

        if current_time is None:
            current_time = event_time.replace(second=0, microsecond=0)

        # Slide the window up to the current event's minute
        while current_time <= event_time:
            avg_duration = (sum_durations / count_durations) if count_durations > 0 else 0
            results[current_time] = avg_duration
            current_time += timedelta(minutes=1)

            # Remove events that are outside the window
            while window and window[0][0] < current_time - timedelta(minutes=window_size):
                old_time, old_duration = window.popleft()
                sum_durations -= old_duration
                count_durations -= 1

        # Add the current event to the window
        window.append((event_time, duration))
        sum_durations += duration
        count_durations += 1

    # Process any remaining time windows after the last event
    while window:
        avg_duration = (sum_durations / count_durations) if count_durations > 0 else 0
        results[current_time] = avg_duration
        current_time += timedelta(minutes=1)

        while window and window[0][0] < current_time - timedelta(minutes=window_size):
            old_time, old_duration = window.popleft()
            sum_durations -= old_duration
            count_durations -= 1

    return results

def main():
    """
    Main function to parse arguments, load events, calculate moving averages, and print results.
    """
    args = parse_args()
    events = load_events(args.input_file)
    results = calculate_moving_averages(events, args.window_size)

    for time_point in sorted(results.keys()):
        print(json.dumps({
            "date": time_point.strftime("%Y-%m-%d %H:%M:%S"),
            "average_delivery_time": results[time_point]
        }))

if __name__ == "__main__":
    main()
