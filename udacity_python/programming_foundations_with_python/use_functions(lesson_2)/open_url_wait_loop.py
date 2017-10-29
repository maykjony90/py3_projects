import time
import webbrowser

count = 0
total_break = 5

while (count < total_break):
    time.sleep(60 * 25)
    webbrowser.open("https://www.youtube.com/watch?v=pAgnJDJN4VA")
    time.sleep(60 * 25)
    count = count + 1
