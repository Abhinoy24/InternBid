def findnumber(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
        return False
if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8]
    print(findnumber(l,10))
    print(findnumber(l,8))
    print(findnumber(l,1))
    