using System.Collections.Generic;

List<int> myList = new List<int>() { 14, 4, 2, 8, 5 };

var sortedList = SelectionSort(myList);

foreach (var item in sortedList)
{
    Console.Write($"{item} ");
}

static int FindSmallest(List<int> arr)
{
    var smallest = arr[0];
    var smallestIndex = 0;
    for (int i = 0; i < arr.Count; i++)
    {
        if (arr[i] < smallest)
        {
            smallest = arr[i];
            smallestIndex = i;
        }
    }
    return smallestIndex;
}

static int[] SelectionSort(List<int> arr)
{
    var newArr = new int[arr.Count];
    for (int i = 0; i < newArr.Length; i++)
    {
        var smallest = FindSmallest(arr);
        newArr[i] = arr[smallest];
        arr.RemoveAt(smallest);
    }
    return newArr;
}
