#!/bin/bash

# Wait for the file dialog to appear
sleep 2

# Activate the file dialog window
xdotool search --name "Open" windowactivate

# Navigate to the Downloads folder
xdotool type --delay 100 "/Users/user/Documents/SpreeSuite/Latest Data Spree/Latest Data/zyp scenario"
xdotool key Return

# Wait for the folder to load
sleep 3

# Select the Service.json file
xdotool type --delay 50 "zypconnections.csv"
xdotool key Return

# Wait for the dialog to refresh (if needed)
sleep 1

# Press Enter to open the file
xdotool key Return
