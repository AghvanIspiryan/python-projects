s
import webbrowser, random, time
websites = ["www.google,com", "www.instagram.com", "www.youtube.com"]


for i in range(30):
    tabs = random.choice(websites)
    webbrowser.open(tabs, new=1)
    time.sleep(.5)