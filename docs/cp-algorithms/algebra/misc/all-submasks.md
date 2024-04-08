# Duyệt submask

## Nguồn
<img src="../../../../assets/images/cpalgorithms.ico" width="16" height="16"/> [Submask Enumeration](https://cp-algorithms.com/algebra/all-submasks.html)

## Duyệt tất cả submask của một mask

Cho bitmask $m$, ta muốn duyệt qua tất cả các submask của nó, tức là các mask $s$ mà chỉ có các bit 1 trong $m$ mới có thể là bit 1 trong $s$.

Xét cài đặt thuật toán sau, dựa trên các thao tác xử lý bit

```cpp
int s = m;
while (s > 0) {
    ... ta có thể dùng s ...
    s = (s-1) & m;
}
```

hoặc một cách ngắn gọn hơn, sử dụng vòng lặp `for`:

```cpp
for (int s = m; s; s = (s-1) & m)
    ... ta có thể dùng s ...
```

Trong cả hai cài đặt trên, submask bằng 0 sẽ không được xử lý. Ta có thể xử lý nó bên ngoài vòng lặp, hoặc dùng một cách cục súc hơn, như sau:

```cpp
for (int s = m; ; s = (s-1) & m) {
    ... ta có thể dùng s ...
    if (s == 0) {
        break;
    }
}
```

Vì sao code trên lại duyệt qua tất cả các submask của $m$ mà không bị lặp lại, và duyệt theo thứ tự giảm dần?

Giả sử ta có một bitmask $s$, và ta muốn đến bitmask tiếp theo (là một submask đấy). Bằng cách trừ 1 từ mask $s$, ta sẽ xóa đi bit 1 cuối cùng, và tất cả các bit bên phải nó sẽ trở thành 1. Sau đó ta xóa đi tất cả các bit "thừa" không nằm trong mask $m$ và do đó không thể là một phần của submask. Ta thực hiện câu vừa rồi bằng phép toán đơn giản `(s-1) & m`. Kết quả là ta "cắt" mask $s-1$ để tìm ra giá trị submask lớn nhất mà nó có thể nhận được, tức là submask tiếp theo sau $s$ theo thứ tự giảm dần.

Như vậy, thuật toán này sinh ra tất cả các submask của mask $m$ theo thứ tự giảm dần, với chỉ hai phép toán trong mỗi lần lặp.

Trường hợp đặc biệt là khi $s = 0$. Sau khi thực hiện `s-1` ta sẽ có một mask mà tất cả các bit đều là 1 (biểu diễn bit của -1), và sau khi thực hiện `(s-1) & m` ta sẽ có $s$ bằng $m$. Do đó, với mask $s = 0$ ta phải cẩn thận — nếu vòng lặp không kết thúc ở 0, thuật toán có thể rơi vào vòng lặp vô hạn.

## Duyệt tất cả các mask với các submask của nó

Trong nhiều bài toán, đặc biệt là các bài DP bitmask, ta sẽ cần phải duyệt tất cả các mask, và với mỗi mask, duyệt qua tất cả các submask của nó:

```cpp
for (int m = 0; m < (1<<n); ++m)
    for (int s = m; s; s = (s-1) & m)
        ... s và m ...
```

Ta sẽ đi chứng minh rằng vòng lặp sẽ lặp tổng cộng $O(3^n)$ lần.

**Cách 1**: Xét bit thứ $i$. Có ba trường hợp:

1. nó không nằm trong mask $m$ (và do đó không nằm trong submask $s$),
2. nó nằm trong $m$, nhưng không nằm trong $s$, hoặc
3. nó nằm trong cả $m$ và $s$.

Vì có tất cả $n$ bit, ta sẽ có $3^n$ tổ hợp khác nhau.

**Cách 2**: Lưu ý rằng nếu mask $m$ có $k$ bit 1, thì nó sẽ có $2^k$ submask. Do ta có tổng cộng $\binom{n}{k}$ mask có $k$ bit 1, thì tổng với tất cả các mask sẽ là:

$$\sum_{k=0}^n \binom{n}{k} \cdot 2^k$$

Để tính tổng này, ta thấy rằng nó bằng với khai triển của $(1+2)^n$ bằng định lý nhị thức Newton. Do đó, ta có $3^n$ tổ hợp khác nhau.

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [AtCoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder187-ABC-F.cpp) | 31/01/2024 |
| [Codeforces - Nuclear Fusion](https://codeforces.com/contest/71/problem/E) | :white_check_mark: | [Submission](https://codeforces.com/contest/71/submission/248432927) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF71-D2-E.cpp) | 27/02/2024 |
| [Codeforces - Sandy and Nuts](https://codeforces.com/contest/599/problem/E) | :white_check_mark: | [Submission](https://codeforces.com/contest/599/submission/253590555) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF599-D2-E.cpp) | 28/03/2024 |
| [UVA 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/UVA/UVA%201439.cpp) | 13/03/2024 |
| [UVA 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/UVA/UVA%2011825.cpp) | 07/03/2024 |
