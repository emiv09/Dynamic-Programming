import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {
    //public void addElementsToMemo{}

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int earnings = 0;
        List<Integer> groups = new ArrayList<>();
        Map<Integer, Integer> cacheEarnings = new HashMap<>();
        Map<Integer, Integer> cacheIndex = new HashMap<>();
        int index = 0;

        // Read inputs: l, c, n
        int l = sc.nextInt();  // maximum capacity of the rollercoaster
        int c = sc.nextInt();  // number of rides
        int n = sc.nextInt();  // number of groups

        // Read group sizes
        for (int i = 0; i < n; i++) {
            int pi = sc.nextInt();
            groups.add(pi);
        }

        // Simulate the rides
        for (int i = 0; i < c; i++) {
            int placeCount = 0;
            int beginIndex = index;
            boolean beginIndexB = false;

            while (placeCount <= l) {

                // Check cache for earnings and index
                if (cacheEarnings.containsKey(beginIndex)) {
                    earnings += cacheEarnings.get(beginIndex);
                    index = cacheIndex.get(beginIndex);
                    break;
                }

                // If we come back to the same group in the same ride
                if (beginIndex == index) {
                    if (beginIndexB) break;
                    if (!beginIndexB) beginIndexB = true;
                }

                // Check if adding the current group's size fits in the coaster
                if (placeCount + groups.get(index) <= l) {
                    placeCount += groups.get(index);

                    // Update index (move to the next group, or loop back to the start)
                    if (index + 1 < groups.size()) {
                        index++;
                    } else {
                        index = 0;
                    }
                } else {
                    break;
                }
            }

            // Add to total earnings
            earnings += placeCount;

            // Cache the earnings and index for this starting group
            if (!cacheEarnings.containsKey(beginIndex)) {
                cacheEarnings.put(beginIndex, placeCount);
                cacheIndex.put(beginIndex, index);
            }
        }

        // Output total earnings after all rides
        System.out.println(earnings);

        sc.close();
    }

}