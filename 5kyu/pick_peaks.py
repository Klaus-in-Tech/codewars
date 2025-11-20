def pick_peaks(arr):
    pos = []
    peaks = []
    if not arr:
        return {"pos": pos, "peaks": peaks}

    candidate = None
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            # start of a potential peak (or start of a plateau)
            candidate = i
        elif arr[i] < arr[i - 1]:
            # a drop: if we had a candidate, it's a confirmed peak
            if candidate is not None:
                pos.append(candidate)
                peaks.append(arr[candidate])
                candidate = None
        # if equal, keep candidate (plateau) and continue

    return {"pos": pos, "peaks": peaks}


if __name__ == "__main__":
    print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))  # {'pos':[3,7], 'peaks':[6,3]}
    print(pick_peaks([1,2,2,2,1]))                # {'pos':[1],   'peaks':[2]}
    print(pick_peaks([1,2,2,2,3]))                # {'pos':[],    'peaks':[]}
    print(pick_peaks([]))                         # {'pos':[],    'peaks':[]}