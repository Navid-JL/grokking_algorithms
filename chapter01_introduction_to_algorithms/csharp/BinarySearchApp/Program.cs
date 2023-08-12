List<int> myList = new List<int>() { 1, 2, 3, 4, 5, 6 };

Console.WriteLine(BinarySearch(myList, 2));

static int BinarySearch(List<int> list, int element)
{
    int low = 0;
    int high = list.Count - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        int guess = list[mid];

        if (guess == element)
            return mid;
        else if (guess > element)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}
