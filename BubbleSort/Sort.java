import java.lang.reflect.Array;
import java.util.Arrays;

public class Sort {
    public static void main(String args[]){
        int arr [] = {6,8,4,2,5,8,3};
        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.toString(bubbleSort(arr)));

    }
    public static int [] bubbleSort(int [] arr){
        for (int i = 0; i < arr.length-1;i++){
            int min = arr[i+1];
            int minIndex = i+1;
            for (int j = i+1; j < arr.length;j++){
                    if (min > arr[j]) {
                        minIndex = j;
                        min = arr[j];
                    }

            }
            if (arr[i] > arr[minIndex]){
                int temp = arr[minIndex];
                arr[minIndex] = arr[i];
                arr[i] = temp;
            }
        }
        return arr;
    }

}
