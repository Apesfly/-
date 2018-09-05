package Algorithms;

public class InsertSort implements IArraySort {
    @Override
    public int[] sort(int[] array) {
        for (int i = 1; i< array.length; i++) {
            int right = array[i];
            int leftPointer = i - 1;
            while(leftPointer >= 0 && array[leftPointer] > right) {
                array[leftPointer + 1] = array[leftPointer];
                leftPointer -= 1;
            }
            array[leftPointer + 1] = right;
        }
        return array;
    }
}
