def convert(s):
    arr = (s.strip()).split(' ')
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    return arr
