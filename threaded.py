import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

thread_local = threading.local()

def get_session():
    if getattr(thread_local, "session", None) is None:
    # if 'session' not in thread_local:
        thread_local.session = requests.Session()
    return thread_local.session

def download(url):
    session = get_session()
    with session.get(url) as response:
        # response_con = response.content
        print("Read {} from {}".format(len(response.content), url))

def download_all(sites):
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download, sites, timeout=10)
    # with requests.Session() as session:
        # for url in sites:
        #     download(url, session)

def main():
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    download_all(sites)

if __name__ == "__main__":
    import time
    # times = timeit.timeit(stmt="main()", setup="from __main__ import main", number=3)
    # print(times)
    start = time.time()
    main()
    duration = time.time() - start
    print("Completed in {} s".format(duration))
