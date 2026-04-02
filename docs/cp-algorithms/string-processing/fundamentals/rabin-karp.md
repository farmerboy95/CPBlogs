# Thuật toán Rabin-Karp để so sánh xâu

Thuật toán này dựa trên khái niệm băm (hashing), nếu bạn chưa quen với việc xâu, hãy đọc qua bài viết về [Hash xâu](string-hashing.md) nhé.

Thuật toán này được Rabin và Karp công bố vào năm 1987.

Bài toán: Cho hai xâu — một xâu mẫu $s$ và một xâu văn bản $t$, xác định xem xâu mẫu có xuất hiện trong xâu văn bản hay không, và nếu có, liệt kê tất cả các vị trí xuất hiện trong thời gian $O(|s| + |t|)$.

Thuật toán: Tính giá trị hash cho xâu mẫu $s$. Sau đó, tính giá trị hash cho tất cả các tiền tố của xâu văn bản $t$. Giờ ta có thể so sánh một xâu con độ dài $|s|$ trong $t$ với $s$ trong thời gian hằng số với các hash vừa tính ở trên. Ta so sánh lần lượt từng xâu con có độ dài $|s|$ với xâu mẫu $s$. Bước này tốn tổng cộng $O(|t|)$. Do đó, độ phức tạp cuối cùng của thuật toán là $O(|t| + |s|)$: $O(|s|)$ để tính hash của xâu mẫu và $O(|t|)$ để so sánh từng xâu con có độ dài $|s|$ với xâu mẫu.

## Cài đặt
```cpp
vector<int> rabin_karp(string const& s, string const& t) {
    const int p = 31; 
    const int m = 1e9 + 9;
    int S = s.size(), T = t.size();

    vector<long long> p_pow(max(S, T)); 
    p_pow[0] = 1; 
    for (int i = 1; i < (int)p_pow.size(); i++) 
        p_pow[i] = (p_pow[i-1] * p) % m;

    vector<long long> h(T + 1, 0); 
    for (int i = 0; i < T; i++)
        h[i+1] = (h[i] + (t[i] - 'a' + 1) * p_pow[i]) % m; 
    long long h_s = 0; 
    for (int i = 0; i < S; i++) 
        h_s = (h_s + (s[i] - 'a' + 1) * p_pow[i]) % m; 

    vector<int> occurrences;
    for (int i = 0; i + S - 1 < T; i++) {
        long long cur_h = (h[i+S] + m - h[i]) % m;
        if (cur_h == h_s * p_pow[i] % m)
            occurrences.push_back(i);
    }
    return occurrences;
}
```

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20NAJPF.cpp) | 02/04/2026 |
| [Good Substrings - Codeforces](https://codeforces.com/contest/271/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/271/submission/363607571) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF271-D2-D.cpp) | 19/02/2026 |
| [Codeforces - Palindromic Characteristics](https://codeforces.com/contest/835/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/835/submission/368616930) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF835-D2-D.cpp) | 28/03/2026 |
| [Leetcode - Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC1044-longest-duplicate-substring.cpp) | 02/04/2026 |
