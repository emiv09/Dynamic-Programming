import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Solve this puzzle by writing the shortest code.
 * Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
 * These comments should be burnt after reading!
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int LX = in.nextInt(); // the X position of the light of power
        int LY = in.nextInt(); // the Y position of the light of power
        int TX = in.nextInt(); // Thor's starting X position
        int TY = in.nextInt(); // Thor's starting Y position


        int thorX = TX;
        int thorY = TY;

        String directionX = "";
        String directionY = "";

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The level of Thor's remaining energy, representing the number of moves he can still make.

            if(thorX > LX) {directionX="W"; thorX-=1;}
            else if (thorX < LX) {directionX="E"; thorX+=1;}
            else directionX ="";

            if(thorY > LY) {directionY = "N";thorY-=1;}
            else if (thorY < LY) {directionY = "S";thorY+=1;}
            else directionY="";



                // Write an action using System.out.println()
                // To debug: System.err.println("Debug messages...");


                // A single line providing the move to be made: N NE E SE S SW W or NW
                System.out.println(directionY+directionX);
        }
    }
}