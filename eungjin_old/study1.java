import java.util.Scanner;
import java.io.FileInputStream;

class study1 {
	public static void main(String args[]) throws Exception {

		System.setIn(new FileInputStream("src/input.txt"));

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {
			int num = sc.nextInt();
			int num2 = 0;
			int num3 = 0;
			int num5 = 0;
			int num7 = 0;
			int num11 = 0;
			boolean divisable = true;

			while (divisable) {
				if (num % 2 == 0) {
					num = num / 2;
					num2++;
				} else if (num % 3 == 0) {
					num = num / 3;
					num3++;
				} else if (num % 5 == 0) {
					num = num / 5;
					num5++;
				} else if (num % 7 == 0) {
					num = num / 7;
					num7++;
				} else if (num % 11 == 0) {
					num = num / 11;
					num11++;
				} else {
					divisable = false;
				}
			}
			System.out.println("#" + test_case + " " + num2 + " " + num3 + " " + num5 + " " + num7 + " " + num11);
		}
	}
}