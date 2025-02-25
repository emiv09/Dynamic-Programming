import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int W = in.nextInt(); // width of the building.
        int H = in.nextInt(); // height of the building.
        int N = in.nextInt(); // maximum number of turns before game over.
        int X0 = in.nextInt();
        int Y0 = in.nextInt();

        int dirX = X0;
        int dirY = Y0;

        int left = 0;
        int right = W;
        int up = 0;
        int down = H;

        // game loop
        while (true) {
            String bombDir = in.next(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

            if(bombDir.equals("U"))
            {
                down = dirY;
                dirY = (down+up-1)/2;
            }
            else if(bombDir.equals("D"))
            {
                up = dirY;
                dirY = (down+up+1)/2;
            }
            else if(bombDir.equals("R")) {
                left = dirX;
                dirX = (left+right+1)/2;
            }
            else if(bombDir.equals("L")) {
                right = dirX;
                dirX = (left+right-1)/2;
            }
            else if(bombDir.equals("UR")) {
                left = dirX;
                down = dirY;
                dirY= (up+down-1)/2;
                dirX= (left+right+1)/2;
            }
            else if(bombDir.equals("DR"))
            {   left = dirX;
                up = dirY;
                dirY = (up+down+1)/2;
                dirX= (left+right+1)/2;
            }
            else if(bombDir.equals("DL"))
            {
                right = dirX;
                up = dirY;
                dirY = (up+down+1)/2;
                dirX= (left+right-1)/2;
            }
            else if(bombDir.equals("UL"))
            {   right = dirX;
                down = dirY;
                dirY = ((up+down-1)/2);
                dirX= (right+left-1)/2;
            }


            // the location of the next window Batman should jump to.
            System.out.println(dirX+" "+dirY);
        }
    }
}