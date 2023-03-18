def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    #https://www.geeksforgeeks.org/heap-sort/
    #https://www.geeksforgeeks.org/building-heap-from-array/
    # start from the last non-leaf node for speed
    # leaf nodes don't have children so they automatically satisfy the heap property
    # which is value of children >= value of parent
    start = n // 2 - 1
    # use reverse order
    for i in range(start, -1, -1):
      # initialize the variable so there's something to compare against
      smol = i
      # use a loop because recursion hurts performance
      while True:
        # find indeces of left and right elements of the data[i]
        l = 2 * i + 1
        r = 2 * i + 2
        # check if the index is smaller than n and if the value at the index
        # is smaller than the current smallest value
        if l < n and data[l] < data[smol]:
          smol = l

        if r < n and data[r] < data[smol]:
          smol = r

        # if there's a new smallest value found - swap
        if smol != i:
          swaps.append((i, smol))
          data[i], data[smol] = data[smol], data[i]
          i = smol

        # if nothing found - assume the element is in place, go to the next one
        else:
          break
          
    return swaps


def main():
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    data = None
    n = None
  
    while True:
      mode = input("Enter input mode (F/I): ")
      
      if mode == "F":
        file = input("Enter filename: ")
        f = open("tests/" + file, "r")
        n = int(f.readline())
        data = list(map(int, f.readline().split()))
        break
        
      elif mode == "I":
        n = int(input("Enter a number of elements in the array: "))
        data = list(map(int, input("Enter the elements: ").split()))
        break
        
      else:
        print("Wrong mode")
        continue
      
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        # note: printing output on a screen takes processing power
        # probably a good idea to not just output everything
        # maybe write to a file?
        print(i, j)


if __name__ == "__main__":
    main()
