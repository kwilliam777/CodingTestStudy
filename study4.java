import java.util.Scanner;
import java.io.FileInputStream;

class study3 {
	public static void main(String args[]) throws Exception {
		System.setIn(new FileInputStream("src/input3.txt"));
		Scanner sc = new Scanner(System.in);
		int cases = 1;

		while (sc.hasNext()) {
			int T = sc.nextInt();

			int nb2 = -1;
			int nb1 = -1;
			int n = -1;
			int na1 = -1;
			int na2 = -1;
			int count = 0;

			for (int test_case = 1; test_case <= T; test_case++) {
				if (nb2 < 0) {
					nb2 = sc.nextInt();
					continue;
				} else if (nb1 < 0) {
					nb1 = sc.nextInt();
					continue;
				} else if (n < 0) {
					n = sc.nextInt();
					continue;
				} else if (na1 < 0) {
					na1 = sc.nextInt();
					continue;
				} else {
					if (na2 < 0) { 
						na2 = sc.nextInt();
					} else {
						nb2 = nb1;
						nb1 = n;
						n = na1;
						na1 = na2;	
						na2 = sc.nextInt();
					}
				}

				int leftTall = Math.max(nb2, nb1);
				int rightTall = Math.max(na1, na2);
				int tallest = Math.max(leftTall, rightTall);

				if (n > tallest) {
					count = count + (n - tallest);
				}
			}
			System.out.println("#" + cases + " " + count);
			cases++;
		}
	}
}