def convertStringToAListAndCapitalize(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    return arr
