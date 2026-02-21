# Hash xâu

## Nguồn

<img src="../../../../assets/images/cpalgorithms.ico" width="16" height="16"/> [String Hashing](https://cp-algorithms.com/string/string-hashing.html)

## Giới thiệu

Các thuật toán hashing rất hữu ích trong việc giải quyết nhiều bài toán khác nhau.

Giả sử ta muốn so sánh nhanh các xâu. Ta có thể dùng cách trâu là so sánh từng ký tự của hai xâu, có độ phức tạp thời gian là $O(\min(n_1, n_2))$ với $n_1$ và $n_2$ là độ dài của hai xâu đó. Ta có thể làm tốt hơn. Ý tưởng của hashing là: ta ánh xạ mỗi xâu thành một số nguyên và so sánh các số đó thay vì so sánh xâu. Làm như vậy sẽ cho phép ta giảm thời gian so sánh xâu xuống còn $O(1)$.

Để thực hiện việc chuyển đổi này, ta cần một **hash function** (hàm băm). Mục tiêu là biến đổi một xâu thành một số nguyên, gọi là **hash** của xâu đó. Nó phải thỏa điều kiện: nếu hai xâu $s$ và $t$ bằng nhau ($s = t$), thì hash của chúng cũng phải bằng nhau ($\text{hash}(s) = \text{hash}(t)$). Nếu không thỏa mãn điều này, ta sẽ không thể so sánh được các xâu.

Lưu ý, điều ngược lại không nhất thiết phải đúng. Nếu các hash bằng nhau ($\text{hash}(s) = \text{hash}(t)$), thì các xâu không nhất thiết phải bằng nhau. Ví dụ, một hash function hợp lệ có thể đơn giản là $\text{hash}(s) = 0$ với mọi $s$. Ví dụ này hơi xàm vì hàm này sẽ chả có tác dụng gì cả, nhưng nó vẫn là một hash function hợp lệ. Lý do tại sao điều ngược lại không cần phải đúng là vì có vô số xâu. Nếu ta chỉ muốn hash function phân biệt được tất cả các xâu gồm các ký tự thường có độ dài nhỏ hơn 15, thì hash đã không thể nằm trọn trong giới hạn số nguyên 64-bit nữa (ví dụ như unsigned long long), vì có quá nhiều xâu như vậy. Và tất nhiên, ta không muốn so sánh các số nguyên có độ dài tùy ý, vì chính cái việc so sánh đó cũng sẽ có độ phức tạp $O(n)$.

Vì vậy, thông thường ta muốn hash function ánh xạ các xâu vào các số trong một khoảng cố định $[0, m)$, khi đó việc so sánh xâu chỉ là so sánh hai số nguyên có độ dài cố định. Và tất nhiên, ta muốn $\text{hash}(s) \neq \text{hash}(t)$ có xác suất rất cao nếu $s \neq t$.

Nhớ rằng, việc sử dụng hashing sẽ không chính xác 100% được, vì hai xâu hoàn toàn khác nhau có thể có cùng hash (các hash va chạm - collision). Tuy nhiên, trong phần lớn các bài toán, ta có thể bỏ qua một cách an toàn vì xác suất hash giống nhau của hai xâu khác nhau vẫn rất nhỏ. Ta sẽ tìm hiểu một số kỹ thuật để giữ xác suất này ở mức cực thấp.

## Tính toán hash của một xâu

Để hash một xâu $s$ có độ dài $n$, ta thường dùng cách sau:

$$\begin{align}
\text{hash}(s) &= s[0] + s[1] \cdot p + s[2] \cdot p^2 + ... + s[n-1] \cdot p^{n-1} \mod m \\
&= \sum_{i=0}^{n-1} s[i] \cdot p^i \mod m,
\end{align}$$

trong đó $p$ và $m$ là các số dương được chọn trước. Đây được gọi là **polynomial rolling hash function**.

Ta sẽ thường chọn $p$ là một số nguyên tố xấp xỉ bằng số ký tự trong bảng chữ cái đầu vào. Ví dụ, nếu đầu vào chỉ gồm các chữ cái thường trong bảng chữ cái tiếng Anh, ta sẽ chọn $p = 31$. Nếu đầu vào có thể chứa cả chữ hoa và chữ thường, thì $p = 53$ là một ý hay. Code trong bài viết này sẽ sử dụng $p = 31$.

$m$ thì sao? $m$ nên là một số lớn vì xác suất hai xâu ngẫu nhiên có hash giống nhau là khoảng $\approx \frac{1}{m}$. Đôi khi người ta chọn $m = 2^{64}$, vì khi đó việc tràn số của số nguyên 64-bit sẽ giống như phép modulo. Tuy nhiên, ta có một phương pháp có thể tạo ra các xâu có hash giống nhau (không phụ thuộc vào $p$). Vì vậy, trong thực tế, $m = 2^{64}$ không được khuyến khích cho lắm. Sẽ hay hơn nếu $m$ là một số nguyên tố lớn. Code trong bài viết này sẽ sử dụng $m = 10^9+9$. Đây là một số lớn, nhưng vẫn đủ nhỏ để ta có thể thực hiện phép nhân hai giá trị với số nguyên 64-bit.

Đây là một ví dụ về việc tính hash của một xâu $s$ chỉ chứa các chữ cái thường. Ta chuyển đổi mỗi ký tự của $s$ thành một số nguyên. Ở đây ta sử dụng chuyển đổi $a \rightarrow 1$, $b \rightarrow 2$, $\dots$, $z \rightarrow 26$. Lưu ý không nên chuyển đổi $a \rightarrow 0$, vì khi đó hash của các xâu $a$, $aa$, $aaa$, $\dots$ đều có giá trị là $0$.

```cpp
long long compute_hash(string const& s) {
    const int p = 31;
    const int m = 1e9 + 9;
    long long hash_value = 0;
    long long p_pow = 1;
    for (char c : s) {
        hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }
    return hash_value;
}
```

Việc tính trước các lũy thừa của $p$ có thể cải thiện thời gian một tí.

## Các bài toán ví dụ

### Tìm các xâu trùng lặp trong một mảng các xâu

Cho một mảng $n$ xâu $s_i$, mỗi xâu có độ dài không quá $m$ ký tự, tìm tất cả các xâu giống nhau và chia chúng thành các nhóm.

Từ thuật toán hiển nhiên là sắp xếp các xâu, ta sẽ có độ phức tạp thời gian là $O(n m \log n)$ trong đó việc sắp xếp yêu cầu $O(n \log n)$ phép so sánh và mỗi phép so sánh mất $O(m)$ thời gian. Tuy nhiên, bằng cách sử dụng hash, ta giảm thời gian so sánh xuống còn $O(1)$, cho ta một thuật toán chạy trong thời gian $O(n m + n \log n)$.

Ta tính hash cho mỗi xâu, sắp xếp các hash cùng với chỉ số của chúng trong mảng ban đầu, sau đó nhóm các chỉ số theo các hash giống nhau.

```cpp
vector<vector<int>> group_identical_strings(vector<string> const& s) {
    int n = s.size();
    vector<pair<long long, int>> hashes(n);
    for (int i = 0; i < n; i++)
        hashes[i] = {compute_hash(s[i]), i};

    sort(hashes.begin(), hashes.end());

    vector<vector<int>> groups;
    for (int i = 0; i < n; i++) {
        if (i == 0 || hashes[i].first != hashes[i-1].first)
            groups.emplace_back();
        groups.back().push_back(hashes[i].second);
    }
    return groups;
}
```

### Tính hash nhanh của các xâu con trong một xâu cho trước

Cho một xâu $s$ và các chỉ số $i$ và $j$, tìm hash của xâu con $s [i \dots j]$.

Theo định nghĩa, ta có:

$$\text{hash}(s[i \dots j]) = \sum_{k = i}^j s[k] \cdot p^{k-i} \mod m$$

Nhân với $p^i$ ta được:

$$\begin{align}
\text{hash}(s[i \dots j]) \cdot p^i &= \sum_{k = i}^j s[k] \cdot p^k \mod m \\
&= \text{hash}(s[0 \dots j]) - \text{hash}(s[0 \dots i-1]) \mod m
\end{align}$$

Như vậy, nếu biết giá trị hash của mỗi tiền tố của xâu $s$, ta có thể tính hash của bất kỳ xâu con nào bằng công thức này. Vấn đề duy nhất ta gặp phải khi tính toán là ta phải có khả năng chia $\text{hash}(s[0 \dots j]) - \text{hash}(s[0 \dots i-1])$ cho $p^i$. Do đó, ta cần tìm nghịch đảo modulo của $p^i$ và sau đó thực hiện phép nhân với nghịch đảo này. Ta có thể tính trước nghịch đảo của mọi $p^i$, giúp cho việc tính hash của bất kỳ xâu con nào của $s$ trong thời gian $O(1)$.

Tuy nhiên, có một cách dễ hơn. Trong hầu hết các trường hợp, thay vì tính chính xác hash của xâu con nào đó, chỉ cần tính hash nhân với một lũy thừa nào đó của $p$ là đủ. Giả sử ta có hai hash của hai xâu con, một hash được nhân với $p^i$ và hash kia được nhân với $p^j$. Nếu $i < j$ thì ta nhân hash đầu tiên với $p^{j-i}$, ngược lại, ta nhân hash thứ hai với $p^{i-j}$. Bằng cách này, ta có cả hai hash đều được nhân với cùng một lũy thừa của $p$ (là $\max(i, j)$) và bây giờ các hash này có thể được so sánh dễ dàng mà không cần phải chia nữa.

## Ứng dụng của Hashing

Dưới đây là một số ứng dụng điển hình của Hashing:

* Thuật toán Rabin-Karp để tìm kiếm pattern trong xâu trong thời gian $O(n)$
* Tính số lượng xâu con khác nhau của một xâu trong $O(n^2)$ (ở dưới)
* Tính số lượng xâu con palindrome trong một xâu.

### Tính số lượng xâu con khác nhau trong một xâu

Cho một xâu $s$ có độ dài $n$, chỉ gồm các chữ cái tiếng Anh thường, tìm số lượng xâu con khác nhau trong xâu này.

Để giải quyết bài toán này, ta duyệt qua tất cả các độ dài xâu con $l = 1 \dots n$. Với mỗi độ dài xâu con $l$, ta xây dựng một mảng các hash của tất cả các xâu con có độ dài $l$ nhân với cùng một lũy thừa của $p$. Số lượng phần tử khác nhau trong mảng bằng với số lượng xâu con phân biệt có độ dài $l$ trong xâu. Số lượng này được cộng vào đáp án cuối cùng.

Để tiện hơn, ta sẽ sử dụng $h[i]$ là hash của tiền tố có $i$ ký tự, và định nghĩa $h[0] = 0$.

```cpp
int count_unique_substrings(string const& s) {
    int n = s.size();
    
    const int p = 31;
    const int m = 1e9 + 9;
    vector<long long> p_pow(n);
    p_pow[0] = 1;
    for (int i = 1; i < n; i++)
        p_pow[i] = (p_pow[i-1] * p) % m;

    vector<long long> h(n + 1, 0);
    for (int i = 0; i < n; i++)
        h[i+1] = (h[i] + (s[i] - 'a' + 1) * p_pow[i]) % m;

    int cnt = 0;
    for (int l = 1; l <= n; l++) {
        unordered_set<long long> hs;
        for (int i = 0; i <= n - l; i++) {
            long long cur_h = (h[i + l] + m - h[i]) % m;
            cur_h = (cur_h * p_pow[n-i-1]) % m;
            hs.insert(cur_h);
        }
        cnt += hs.size();
    }
    return cnt;
}
```

Lưu ý rằng, $O(n^2)$ không phải là độ phức tạp thời gian tốt nhất có thể cho bài toán này. Ta có thể dùng Suffix Arrays với độ phức tạp $O(n \log n)$, và thậm chí là $O(n)$ với Suffix Tree hoặc Suffix Automaton.

## Cải thiện xác suất không va chạm

Thường thì cách polynomial hash ở trên khá là tốt rồi, và đa số trường hợp sẽ không xảy ra va chạm. Tuy nhiên, xác suất va chạm vẫn là $\approx \frac{1}{m}$. Với $m = 10^9 + 9$, xác suất này là rất thấp, khoảng $10^{-9}$. Nhưng nhớ rằng, xác suất đó tồn tại khi ta chỉ thực hiện một phép so sánh. Nhưng nếu ta so sánh một xâu $s$ với $10^6$ xâu khác nhau, thì xác suất ít nhất một va chạm xảy ra sẽ tăng lên khoảng $\approx 10^{-3}$. Và nếu ta muốn so sánh $10^6$ xâu khác nhau với nhau (ví dụ: bằng cách đếm có bao nhiêu xâu duy nhất tồn tại), thì xác suất ít nhất một va chạm xảy ra đã là $\approx 1$. Điều này có nghĩa là gần như chắc chắn rằng bài toán này sẽ kết thúc với một va chạm và trả về kết quả sai.

Có một mẹo rất đơn giản để có xác suất tốt hơn. Ta có thể tính hai hash khác nhau cho mỗi xâu (bằng cách sử dụng hai $p$ khác nhau, và/hoặc $m$ khác nhau, và so sánh các cặp hash này). Nếu $m$ khoảng $10^9$ cho cả hai hash function thì nó sẽ gần như tương đương với việc có một hash function với $m \approx 10^{18}$. Khi so sánh $10^6$ xâu với nhau, xác suất ít nhất một va chạm xảy ra bây giờ giảm xuống còn $\approx 10^{-6}$.

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [Good Substrings - Codeforces](https://codeforces.com/contest/271/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/271/submission/363607571) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF271-D2-D.cpp) | 19/02/2026 |
| [A Needle in the Haystack - SPOJ](http://www.spoj.com/problems/NHAY/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20NHAY.cpp) | 19/02/2026 |
| [String Hashing - Kattis](https://open.kattis.com/problems/hashing) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Kattis/kattis%20hashing.cpp) | 19/02/2026 |
| [Double Profiles - Codeforces](https://codeforces.com/contest/154/problem/C) | :white_check_mark: | [Submission](https://codeforces.com/contest/154/submission/363710542) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF154-D1-C.cpp) | 20/02/2026 |
| [Password - Codeforces](https://codeforces.com/contest/126/problem/B) | :white_check_mark: | [Submission](https://codeforces.com/contest/126/submission/363712004) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF126-D1-B.cpp) | 20/02/2026 |
| [SUB_PROB - SPOJ](https://www.spoj.com/problems/SUB_PROB/) | | | | |
| [INSQ15_A](https://www.codechef.com/problems/INSQ15_A) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/1238683797) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20INSQ15_A.cpp) | 20/02/2026 |
| [SPOJ - Ada and Spring Cleaning](https://www.spoj.com/problems/ADACLEAN/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20ADACLEAN.cpp) | 20/02/2026 |
| [GYM - Text Editor](https://codeforces.com/gym/101466/problem/E) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF101466-Gym-E.cpp) | 21/02/2026 |
| [12012 - Detection of Extraterrestrial](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3163) | | | | |
| [Codeforces - Games on a CD](https://codeforces.com/contest/727/problem/E) | | | | |
| [UVA 11855 - Buzzwords](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2955) | | | | |
| [Codeforces - Santa Claus and a Palindrome](https://codeforces.com/contest/752/problem/D) | | | | |
| [Codeforces - String Compression](https://codeforces.com/contest/825/problem/F) | | | | |
| [Codeforces - Palindromic Characteristics](https://codeforces.com/contest/835/problem/D) | | | | |
| [SPOJ - Test](https://www.spoj.com/problems/CF25E/) | | | | |
| [Codeforces - Palindrome Degree](https://codeforces.com/contest/7/problem/D) | | | | |
| [Codeforces - Deletion of Repeats](https://codeforces.com/contest/19/problem/C) | | | | |
| [HackerRank - Gift Boxes](https://www.hackerrank.com/contests/womens-codesprint-5/challenges/gift-boxes) | | | | |
