import speedtest

# Create an instance of the Speedtest class
test = speedtest.Speedtest()

# Test download speed
down = test.download()

# Test upload speed
upload = test.upload()

# Print results
print(f'Download speed: {down / 1_000_000:.2f} Mbps')
print(f'Upload speed: {upload / 1_000_000:.2f} Mbps')






























