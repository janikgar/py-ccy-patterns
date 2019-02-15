import requests
import time

def download(url, session):
    with session.get(url) as response:
        # response_con = response.content
        print("Read {} from {}".format(len(response.content), url))

def download_all(sites):
    with requests.Session() as session:
        for url in sites:
            download(url, session)

def main():
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    download_all(sites)

if __name__ == "__main__":
    start = time.time()
    main()
    duration = time.time() - start
    print("Completed in {} s".format(duration))
