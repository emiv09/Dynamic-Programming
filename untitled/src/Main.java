import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static long calculateEarningsPerEachRide(int L, ArrayList<Integer> queue){
        long earnings = 0;
        int numberOfElementsInQueue = queue.size();
        int i=0;

        while(i+queue.get(0) <= L){
            if(numberOfElementsInQueue==0) break;

            numberOfElementsInQueue-=1;
            i+=queue.get(0);
            int firstElementInQueue = queue.remove(0);
            earnings+=firstElementInQueue;

            queue.add(firstElementInQueue);

        }

        return earnings;
    }

    public static void main(String args[]) {

        long start = System.currentTimeMillis();
// ...


        Scanner in = new Scanner(System.in);
        int L = in.nextInt();
        int C = in.nextInt();
        int N = in.nextInt();

        ArrayList<Integer> queue = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int pi = in.nextInt();
            queue.add(pi);
        }

        long total = 0;

        for(int i = 0; i < C; i++) {
            total += calculateEarningsPerEachRide(L,queue);
        }

        System.out.println(total);

        long finish = System.currentTimeMillis();
        long timeElapsed = finish - start;

        System.out.println(timeElapsed);
    }

}