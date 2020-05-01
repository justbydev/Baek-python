#include <iostream>
#include <algorithm>

using namespace std;
int main(void) {
	int N;
	cin >> N;
	int* num = new int[N];
	int sm = 0;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
		sm += num[i];
	}
	int** dp = new int*[N];
	for (int i = 0; i < N; i++) {
		dp[i] = new int[sm + 1];
	}
	dp[0][0] = 0;
	for (int i = 1; i < sm + 1; i++) {
		dp[0][i] = -1;
	}
	dp[0][num[0]] = num[0];
	for (int i = 1; i < N; i++) {
		for (int j = 0; j < sm + 1; j++) {
			dp[i][j] = dp[i - 1][j];
			if (num[i] + j < sm + 1 && dp[i - 1][num[i] + j] != -1) {
				dp[i][j] = max(dp[i][j], dp[i - 1][num[i] + j]);
			}
			if (num[i] <= j && dp[i - 1][j - num[i]] != -1) {
				dp[i][j] = max(dp[i][j], dp[i - 1][j - num[i]] + num[i]);
			}
			if (num[i] > j && dp[i - 1][num[i] - j] != -1) {
				dp[i][j] = max(dp[i][j], dp[i - 1][num[i] - j] + j);
			}
		}
	}
	if (dp[N - 1][0] <= 0) {
		cout << -1 << endl;
	}
	else {
		cout << dp[N - 1][0] << endl;
	}
	return 0;
}
