def uniq_numbers(lst):
    return len(set(lst))

print(uniq_numbers([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8]))


def listIntersectionCount(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return len(set1 & set2)

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [7, 8, 9, 10, 11, 12, 13]
print(listIntersectionCount(lst1, lst2))


def listIntersection(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return sorted(set1 & set2)

lst1 = [1, 2, 13, 3, 4, 5, 6, 7, 8, 9]
lst2 = [7, 5, 8, 9, 10, 11, 12, 13]
print(listIntersection(lst1, lst2))


def yesNo(lst):
    numbers = [int(num) for num in lst.split()]
    uniq = set()

    for number in numbers:
        if number in uniq:
            print('yes')
        else:
            print('no')
            uniq.add(number)

yesNo('11 11 12 13 14 12 4 3 2 11 2')


def text(filename):
    f = open(filename, encoding='utf-8') 
    uniq = set()

    for line in f:
        words = line.split()
        for word in words:
            uniq.add(word.rstrip('\n'))
    
    f.close()
    return len(uniq)

print(text('input.txt'))