# TDEE Calculator (CLI)

A terminal-based Python application designed to calculate your Total Daily Energy Expenditure (TDEE) and manage user data locally.

## Description

This project provides a command-line interface (CLI) to help users estimate their daily caloric needs based on their physical measurements and activity level. It currently operates entirely in the terminal (no graphical user interface / GUI yet).

## Features

- **TDEE & BMR Calculation:** Calculates Basal Metabolic Rate and applies activity multipliers to determine total daily calorie expenditure.
- **Automatic Local Storage:** Automatically saves user profile data to a local `user_data.json` file, allowing returning users to review their stats without re-entering information.
- **Interactive Prompts:** Input validation to ensure accurate physical measurements are provided.

## Planned Features (Roadmap)

- [ ] **Calorie Tracker:** Helper module to log daily meals and track intake against your calculated TDEE.
- [ ] **Profile Updates:** Ability to modify stored measurements (e.g., updating body weight over time).
- [ ] **Graphical User Interface (GUI):** Potential desktop interface in future iterations.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/lilkalimu-glitch/tdee-calculator
