// g++ main.cpp -o main
// ./main < input.txt > stored_output.txt
#include <iostream>
using namespace std;

int main()
{
	int z, t, n;
	char s[100];
	cin >> t;
	for (z = 0;z < t;z++)
	{
		cin >> n;
		cin >> s;
		for (int i = 0;i < n;i++)
			s[i] = 'z' - s[i] + 'a';
		n = (n / 2) * 2;
		for (int i = 0;i < n;i = i + 2)
		{
			char temp = s[i];
			s[i] = s[i + 1];
			s[i + 1] = temp;
		}
		cout << s << endl;
	}
}
