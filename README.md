# Concert Ticket Counter (Dua Lipa - Estadio Nacional)

This repository contains a Python script that simulates the ticket distribution for a Dua Lipa concert at Chile's Estadio Nacional. The program generates a randomized dataset of 1.000.000 tickets across the venue's official seating sections, organizes the entries alphabetically, tallies attendance per area using parallel lists, and identifies the most popular section of the event.

## Why Random Simulation & Pre-Sorting Matter

To test the counting logic against a realistic volume of data without manually hardcoding a massive list, the script imports Python's built-in `random` module. Using `random.choices()`, it generates an unsorted list of 1.000.000 tickets sampled with replacement from `OFF_Section` (which holds the nine official seating areas of Estadio Nacional: `Cancha`, `Cancha VIP`, `Galeria`, `Andes`, `Pacifico Bajo`, `Pacifico Medio`, `Pacifico Alto`, `Pacifico Lateral`, and `Silla de Ruedas`). A fixed seed (`random.seed(42)`) is included to keep the randomized output consistent and reproducible across runs.

Before running the counting loop, the script sorts the entire `tickets` list alphabetically in a case-insensitive manner using `.sort(key=str.lower)`. Sorting the raw data beforehand is a deliberate design choice: it groups identical section names together consecutively and ensures that the resulting `sections` and `counts` lists are built in clean alphabetical order automatically, eliminating the need for extra sorting steps after the data has been processed.

## Counting Logic

The core algorithm relies on two synchronized parallel lists (`sections` and `counts`) where each index represents a specific seating area and its corresponding tally. As a `for` loop iterates through the sorted `tickets` list, an `if/else` check determines whether the current section has already been registered. If it is a new section, it gets appended to `sections` while a `1` is appended at the exact same index in `counts`; if it already exists, the program finds its position via `.index()` and increments its counter by one. Once all 1.000.000 tickets are tallied, `max(counts)` and `.index()` pinpoint the highest attendance figure and match it back to its section name to display the final summary.

## Usage

Make sure you have Python 3 installed locally, then run the script from your terminal:

```bash
python concert_tickets.py
