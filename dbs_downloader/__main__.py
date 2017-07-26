import downloader
from pprint import pprint

def run():
    rangefnd = downloader.range_eps(68,70)
    singlefnd = downloader.single_eps(71)

    pprint(rangefnd)
    pprint(singlefnd)
    downloader.write_file_single(71, "1.txt")
    # downloader.write_file_range(68, 100, "caps.txt")



if __name__ == '__main__':
    run()
