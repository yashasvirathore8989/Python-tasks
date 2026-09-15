import java.util.Scanner;


public class GradeCalculator {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter marks for Physics: ");

        double physics = scanner.nextDouble();


        System.out.print("Enter marks for Chemistry: ");

        double chemistry = scanner.nextDouble();


        System.out.print("Enter marks for Biology: ");

        double biology = scanner.nextDouble();


        System.out.print("Enter marks for Mathematics: ");

        double mathematics = scanner.nextDouble();


        System.out.print("Enter marks for Computer: ");

        double computer = scanner.nextDouble();


        double totalMarks = physics + chemistry + biology + mathematics + computer;

        double percentage = (totalMarks / 500) * 100;

        char grade;

        if (percentage >= 90) {

            grade = 'A';

        } else if (percentage >= 80) {

            grade = 'B';

        } else if (percentage >= 70) {

            grade = 'C';

        } else if (percentage >= 60) {

            grade = 'D';

        } else if (percentage >= 40) {

            grade = 'E';

        } else {

            grade = 'F';

        }


        System.out.printf("Total Marks: %.2f / 500.00\n", totalMarks);

        System.out.printf("Percentage: %.2f%%\n", percentage);

        System.out.println("Grade: " + grade);


        scanner.close();

    }
}
