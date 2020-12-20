import draft
import players
from league import get_team_ids
import time




if __name__ == "__main__":
    start = time.time()

    leagues = []
    for x in range(12086, 12102):  # first and last league num for OTH 2019
        leagues.append(x)

    OTH_team_ids = []
    for a in leagues:
        b = get_team_ids(a)
        for c in b:
            OTH_team_ids.append(c)












    end = time.time()
    dur = end - start
    print("{:.2f} seconds".format(dur))
    print(OTH_team_ids)
