// This is a Java program
// It demonstrates line comments and blank lines

import java.util.Scanner;

public class GreetingProgram {

    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for their name
        System.out.print("Enter your name: ");

        // Read the user's name
        String userName = scanner.nextLine();

        // Check if the user provided a name
        if (!userName.isEmpty()) {
            greetUser(userName);
        } else {
            System.out.println("You didn't enter a name.");
        }
    }

    // This method greets the user
    private static void greetUser(String name) {
        System.out.println("Hello, " + name + "!");
    }
}
