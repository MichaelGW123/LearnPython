# Michael Williamson
# Speed Test app
# 10/13/2020

import speedtest

test = speedtest.Speedtest() 

down = test.download()
upload = test.upload()

print(f"Download speed: {down}")
print(f"Upload speed: {upload}")