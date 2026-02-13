import requests
import threading
import time

urls=[
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.rediff.com",
    "https://www.amazon.in",
]

def downloadfiles(urls):
    try:
        resp = requests.get(urls)
        filename = urls.split("/")[-1]+".txt"
        with open(filename,"w",encoding="utf-8") as f:
            f.write(resp.text)
        print(f"downloaded: {filename}")

    except Exception as e:
        print(f"downloading error: {e}")
start = time.time()
for url in urls:
    downloadfiles(url)

sequentialtime = time.time() - start
print(f"sequentialtime: {sequentialtime}")

threads = []
starttime1=time.time()
for url in urls:
    thread = threading.Thread(target=downloadfiles, args=(url,))
    threads.append(thread)
    thread.start()

threadingtime = time.time() - starttime1
print(f"threading download time: {threadingtime}")
