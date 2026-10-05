


from math import ceil
from typing import List, Set, Dict, Optional
null = None

def minimize_maximum_parcels(parcels: List[int], extra_parcels: int)->int:
    '''
    parcels is a list of delivery workers with packages, we want to distribute packages to them
    while reducing the most work anyone has to do.

    intuition: find what the current max is, then distribute until everyone matches the prev
    max. Then spread the rest evenly.
    '''

    peak = max(parcels)

    for p in parcels:
        if p < peak:
            extra_parcels -= peak - p

    if extra_parcels > 0:
        return peak + ceil(extra_parcels / len(parcels))

    return peak



if __name__ == "__main__":
    print(minimize_maximum_parcels( parcels = [6, 6, 5, 5], extra_parcels = 3)) # expect 7
