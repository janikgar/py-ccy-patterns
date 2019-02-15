import requests
import multiprocessing
import time

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download(url):
    # session = get_session()
    with session.get(url) as response:
        print("Read {} from {}".format(len(response.content), url))


def download_all(sites):
    # with ThreadPoolExecutor(max_workers=4) as executor:
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download, sites)


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
