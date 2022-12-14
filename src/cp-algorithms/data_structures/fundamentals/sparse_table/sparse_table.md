# Sparse Table

## Nguồn

<img src="../../../../img/cpalgorithms.ico" width="16" height="16"/> [Sparse Table](https://cp-algorithms.com/data_structures/sparse-table.html)

## Lời tựa

Sparse Table là một cấu trúc dữ liệu cho phép trả lời các truy vấn trên đoạn. Nó có thể trả lời hầu hết các truy vấn đoạn trong $O(\log n)$, nhưng sức mạnh thực sự của nó nằm ở việc trả lời các truy vấn tìm min hoặc max của đoạn trong thời gian $O(1)$.

Điểm yếu duy nhất của cấu trúc dữ liệu này là nó chỉ có thể được dùng trên mảng không thay đổi giá trị. Nghĩa là mảng không thể thay đổi giá trị của bất kỳ phần tử nào giữa 2 truy vấn. Nếu có điều đó xảy ra, cả cấu trúc dữ liệu phải được tính lại.

## Ý tưởng

Bất kỳ số không âm nào cũng có thể được biểu diễn bằng duy nhất một tổng giảm dần các số mũ của $2$. Đây chỉ là một biến thể của biểu diễn nhị phân của một số. Ví dụ $13 = (1101)_2 = 8 + 4 + 1$. Ta có nhiều nhất $\lceil \log_2 x \rceil$ số hạng với mỗi số $x$.

Tương tự thì bất kỳ đoạn nào cũng có thể được biểu diễn bằng duy nhất hợp của các đoạn con với độ dài giảm dần các số mũ của $2$. Ví dụ $[2, 14] = [2, 9] \cup [10, 13] \cup [14, 14]$, với đoạn ban đầu có độ dài là $13$, các đoạn con sẽ có độ dài tương ứng là $8$, $4$ và $1$. Và tương tự như trên thì ta có nhiều nhất $\lceil \log_2(\text{độ dài đoạn ban đầu}) \rceil$ đoạn con.

Ý tưởng của Sparse Table chính là việc tính trước tất cả các đáp án của các truy vấn đoạn với các đoạn có độ dài là luỹ thừa của $2$. Sau đó một truy vấn đoạn có thể được trả lời bằng việc chia đoạn đó ra thành các đoạn con độ dài luỹ thừa $2$, lấy kết quả các đoạn con đó với giá trị tính trước, sau đó kết hợp chúng lại với nhau để tạo ra kết quả cuối cùng.

## Tiền xử lý

Ta sẽ dùng một mảng 2 chiều để lưu đáp án các truy vấn tính trước. $\text{st}[i][j]$ lưu đáp án các đoạn $[j, j + 2^i - 1]$ với độ dài $2^i$. Kích thước của mảng 2 chiều sẽ bằng $(K + 1) \times \text{MAXN}$ với $\text{MAXN}$ là độ dài lớn nhất của mảng ban đầu. $\text{K}$ phải thoả mãn $\text{K} \ge \lfloor \log_2 \text{MAXN} \rfloor$, vì $2^{\lfloor \log_2 \text{MAXN} \rfloor}$ là độ dài lớn nhất ta cần hỗ trợ truy vấn. Với mảng có độ dài chấp nhận được (tầm $\le 10^7$ phần tử), ta có thể dùng $K = 25$.

Chiều chứa $\text{MAXN}$ nên nằm sau chiều chứa $K$ để tiện cho việc truy cập các vùng nhớ liên tiếp (cache friendly).

```cpp
int st[K + 1][MAXN];
```

Vì đoạn $[j, j + 2^i - 1]$ có độ dài $2^i$ được chia thành các đoạn $[j, j + 2^{i - 1} - 1]$ và $[j + 2^{i - 1}, j + 2^i - 1]$, có độ dài đều là $2^{i - 1}$, ta có thể sinh bảng bằng cách dùng quy hoạch động.

```cpp
std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = f(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
```

Hàm $f$ sẽ tuỳ thuộc vào loại truy vấn. Với truy vấn tổng đoạn, $f$ là hàm tổng 2 số, còn với truy vấn min đoạn, $f$ là min 2 số.

Tiền xử lý có độ phức tạp thời gian là $O(\text{N} \log \text{N})$.

## Truy vấn tổng đoạn (Range Sum Queries)

Với các truy vấn dạng này, ta muốn tìm tổng tất cả các giá trị trong đoạn. Vì vậy nên hàm $f$ rõ ràng sẽ là $f(x, y) = x + y$. Ta có thể xây dựng cấu trúc dữ liệu như thế này:

```cpp
long long st[K + 1][MAXN];

std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = st[i - 1][j] + st[i - 1][j + (1 << (i - 1))];
```

Để trả lời truy vấn tổng trên đoạn $[L, R]$, ta duyệt tất cả các luỹ thừa 2, tính từ luỹ thừa lớn nhất. Ngay khi ta gặp luỹ thừa $2^i$ nhỏ hơn hoặc bằng dộ dài đoạn ($= R - L + 1$), ta tính đoạn con đầu tiên của đoạn $[L, L + 2^i - 1]$, sau đó tiếp tục với đoạn còn lại $[L + 2^i, R]$.

```cpp
long long sum = 0;
for (int i = K; i >= 0; i--) {
    if ((1 << i) <= R - L + 1) {
        sum += st[i][L];
        L += 1 << i;
    }
}
```

Độ phức tạp của truy vấn tổng đoạn là $O(K) = O(\log \text{MAXN})$.

## Truy vấn min đoạn (Range Minimum Queries - RMQ)

Có những truy vấn khiến Sparse Table trở nên thượng đẳng hơn các cấu trúc dữ liệu khác. Khi ta tính min của một đoạn, không quan trọng là ta xét một giá trị một hoặc hai lần. Vì vậy thay vì chia đoạn ban đầu ra thành nhiều đoạn nhỏ, ta có thể chia đoạn ban đầu thành 2 đoạn có thể chồng lên nhau có độ dài là luỹ thừa của $2$. Ví dụ, ta có thể chia đoạn $[1, 6]$ thành 2 đoạn $[1, 4]$ và $[3, 6]$. Kết quả truy vấn min trên đoạn $[1, 6]$ rõ ràng là y hệt như min của kết quả truy vấn trên đoạn $[1, 4]$ và kết quả truy vấn trên đoạn $[3, 6]$. Nên ta có thể tính min đoạn $[L, R]$ như sau:

$$\min(\text{st}[i][L], \text{st}[i][R - 2^i + 1]) \quad \text{ với } i = \log_2(R - L + 1)$$

Điều này yêu cầu ta phải tính được $\log_2(R - L + 1)$ nhanh. Ta có thể làm được bằng cách tính trước tất cả các giá trị logarit:

```cpp
int lg[MAXN+1];
lg[1] = 0;
for (int i = 2; i <= MAXN; i++)
    lg[i] = lg[i/2] + 1;
```

Nếu bạn không muốn làm như trên thì logarit cũng có thể tính được trực tiếp với thời gian và bộ nhớ hằng số:

```cpp
// C++20
#include <bit>
int log2_floor(unsigned long i) {
    return std::bit_width(i) - 1;
}

// pre C++20
int log2_floor(unsigned long long i) {
    return i ? __builtin_clzll(1) - __builtin_clzll(i) : -1;
}
```
[Benchmark này](https://quick-bench.com/q/Zghbdj_TEkmw4XG2nqOpD3tsJ8U) cho thấy dùng mảng `lg` chậm hơn vì cache miss.

Sau đó ta cần tiền xử lý Sparse Table. Ta định nghĩa $f$ là $f(x, y) = \min(x, y)$.

```cpp
int st[K + 1][MAXN];

std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = min(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
```

Và min của đoạn $[L, R]$ có thể được tính như sau:

```cpp
int i = lg[R - L + 1];
int minimum = min(st[i][L], st[i][R - (1 << i) + 1]);
```

Độ phức tạp về thời gian của một Range Minimum Query là $O(1)$.

## Các cấu trúc dữ liệu tương tự để hỗ trợ nhiều loại truy vấn hơn

Một trong những điểm yếu chính của cách tiếp cận $O(1)$ ở trên là nó chỉ hỗ trợ các truy vấn trên các [hàm idempotent](https://en.wikipedia.org/wiki/Idempotence). Ví dụ nó hiệu quả trên các truy vấn min đoạn, nhưng không dùng được trên các truy vấn tổng đoạn.

Ta cũng có những cấu trúc dữ liệu tương tự có thể xử lý bất kỳ loại hàm kết hợp và truy vấn đoạn nào trong $O(1)$. Một trong số chúng là [Disjoint Sparse Table](../../../../Codechef/data_structures/disjoint_sparse_table/disjoint_sparse_table.md). Một cái khác là [Sqrt Tree](../../trees/sqrt_tree/sqrt_tree.md).

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [SPOJ - RMQSQ](http://www.spoj.com/problems/RMQSQ/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20RMQSQ.cpp) | 15/11/2022 |
| [SPOJ - THRBL](http://www.spoj.com/problems/THRBL/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20THRBL.cpp) | 15/11/2022 |
| [Codechef - MSTICK](https://www.codechef.com/problems/MSTICK) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/80045083) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20MSTICK.cpp) | 15/11/2022 |
| [Codechef - SEAD](https://www.codechef.com/problems/SEAD) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/80051721) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20SEAD.cpp) | 15/11/2022 |
| [Codeforces - CGCDSSQ](http://codeforces.com/contest/475/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/475/submission/181620636) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF475-D12-D.cpp) | 19/11/2022 |
| [Codeforces - R2D2 and Droid Army](https://codeforces.com/contest/514/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/514/submission/181625876) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF514-D2-D.cpp) | 19/11/2022 |
| [Codeforces - Maximum of Maximums of Minimums](https://codeforces.com/contest/872/problem/B) | :white_check_mark: | [Submission](https://codeforces.com/contest/872/submission/181627246) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF872-D2-B.cpp) | 19/11/2022 |
| [SPOJ - Miraculous](http://www.spoj.com/problems/TNVFC1M/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20TNVFC1M.cpp) | 19/11/2022 |
| [Codeforces - Animals and Puzzles](http://codeforces.com/contest/713/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/713/submission/182040161) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF713-D1-D.cpp) | 21/11/2022 |
| [Codeforces - Trains and Statistics](http://codeforces.com/contest/675/problem/E) | :white_check_mark: | [Submission](https://codeforces.com/contest/675/submission/182356839) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF675-D2-E.cpp) | 24/11/2022 |
| [SPOJ - Postering](http://www.spoj.com/problems/POSTERIN/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20POSTERIN.cpp) | 24/11/2022 |
| [SPOJ - Negative Score](http://www.spoj.com/problems/RPLN/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20RPLN.cpp) | 22/11/2022 |
| [SPOJ - A Famous City](http://www.spoj.com/problems/CITY2/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20CITY2.cpp) | 24/11/2022 |
| [SPOJ - Diferencija](http://www.spoj.com/problems/DIFERENC/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20DIFERENC.cpp) | 23/11/2022 |
| [Codeforces - Turn off the TV](http://codeforces.com/contest/863/problem/E) | :white_check_mark: | [Submission](https://codeforces.com/contest/863/submission/182107869) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF863-D12-E.cpp) | 22/11/2022 |
| [Codeforces - Map](http://codeforces.com/contest/15/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/15/submission/182276341) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF15-D12-D.cpp) | 23/11/2022 |
| [Codeforces - Awards for Contestants](http://codeforces.com/contest/873/problem/E) | :white_check_mark: | [Submission](https://codeforces.com/contest/873/submission/182340226) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF873-D12-E.cpp) | 24/11/2022 |
| [Codeforces - Longest Regular Bracket Sequence](http://codeforces.com/contest/5/problem/C) | :white_check_mark: | [Submission](https://codeforces.com/contest/5/submission/182139929) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF5-D12-C.cpp) | 22/11/2022 |
