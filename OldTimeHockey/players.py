from main import get_roster
import time



if __name__ == "__main__":
    start = time.time()
    for x in range(4):
        print(get_roster(12086, 62757))

    end = time.time()
    dur = end - start
    print("{:.2f} seconds".format(dur))

