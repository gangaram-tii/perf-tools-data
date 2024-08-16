# Set the output file name (change "cpu_load.txt" if desired)
OUTPUT_FILE="cpu_load.txt"

while true; do
  # Get CPU load using sar (change to vmstat if preferred)
  cpu_idle=$(sar -u 1 1 | grep "^Average" | awk '{print $8}')

  # Use bc for floating-point calculations
  cpu_load=$(echo "scale=2; 100 - $cpu_idle" | bc)

  # Append timestamp and CPU load (rounded to 2 decimals) to the file
  echo "$(printf "%.2f\n" $cpu_load)" >> "$OUTPUT_FILE"

  # Sleep for 3 seconds
  #sleep 3
  sleep 1
done
