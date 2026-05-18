def pick_peaks(arr):
    pos,peaks = [],[]
    dict = {}
    
    for i in range(1,len(arr)-1):
        if arr[i-1]<arr[i]>arr[i+1]:
            peaks.append(arr[i])
            pos.append(i)
            
        elif arr[i-1]<arr[i]==arr[i+1]:
            for j in range(i,len(arr)-1):
                if arr[j]>arr[j+1]:
                    peaks.append(arr[i])
                    pos.append(i)
                    break
                elif arr[j]<arr[j+1]:
                    break
                    
    dict['pos'],dict['peaks']= pos,peaks  
    
    return dict


if __name__ == "__main__":
    print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))  # {'pos':[3,7], 'peaks':[6,3]}
    print(pick_peaks([1,2,2,2,1]))                # {'pos':[1],   'peaks':[2]}
    print(pick_peaks([1,2,2,2,3]))                # {'pos':[],    'peaks':[]}
    print(pick_peaks([]))                         # {'pos':[],    'peaks':[]}
    