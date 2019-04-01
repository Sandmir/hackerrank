def count_substring(string, sub_string):

    count = 0
    while len(string) >= len(sub_string):

        ind = string.find(sub_string)
        if ind == -1: return count
        count +=1
        string = "".join(list(string)[ind+1:])

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)