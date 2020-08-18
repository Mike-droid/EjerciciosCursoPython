def binary_search(numbers, number_to_find, low, high):
    
    if low > high:
        return False

    mid = (low+high) // 2

    if numbers[mid] == number_to_find:
        return True
    
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid-1)
    
    else:
        return binary_search(numbers, number_to_find, mid+1, high)


if __name__ == "__main__":
    numbers = [1,4,6,8,9,3,10,65,23,55,12,333,673,345]
    #numbers.sort()
    print(sorted(numbers))

    number_to_find = int(input("Ingresa un numero: "))

    result = binary_search(numbers, number_to_find, 0, len(numbers)-1)

    if result is True:
        print("El número sí está en la lista")
    
    else:
        print("El número no está en la lista :(")