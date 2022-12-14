# Luỹ thừa nhị phân

## Nguồn
<img src="/img/cpalgorithms.ico" width="16" height="16"/> [Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html)

## Khái niệm

Luỹ thừa nhị phân (còn được biết đến là luỹ thừa bằng bình phương) là một thủ thuật để tính $a^n$ mà chỉ sử dụng $O(\log n)$ phép nhân (thay vì $O(n)$ phép nhân như trong các phương pháp đơn giản).

Nó còn có những ứng dụng quan trọng trong rất nhiều vấn đề không liên quan đến số học, vì nó có thể được sử dụng trong bất kì phép toán nào có tính chất **kết hợp**:

$$(X \cdot Y) \cdot Z = X \cdot (Y \cdot Z)$$

Rõ ràng nhất là nó được áp dụng cho phép nhân modulo, phép nhân ma trận và các bài toán khác mà chúng ta sẽ thảo luận dưới đây.

## Thuật toán

$a^n$ được biểu thị đơn giản là nhân $a$ $n-1$ lần: $a^{n} = a \cdot a \cdot \ldots \cdot a$. Nhưng rõ ràng cách này không hữu dụng với $a$ lớn hoặc $n$ lớn.

$a^{b+c} = a^b \cdot a^c$ và $a^{2b} = a^b \cdot a^b = (a^b)^2$.

Ý tưởng của luỹ thừa nhị phân là việc chúng ta biểu diễn số mũ thành dạng nhị phân của nó, tiến hành tính từng bit 1 theo hệ thập phân và nhân lại với nhau.

Ví dụ ta biểu diễn $n$ theo hệ nhị phân, ta có:

$$3^{13} = 3^{1101_2} = 3^8 \cdot 3^4 \cdot 3^1$$

Vì số $n$ có $\lfloor \log_2 n \rfloor + 1$ chữ số khi biểu diễn ở hệ nhị phân, ta chỉ cần dùng $O(\log n)$ phép nhân, nếu ta biết kết quả của $a^1, a^2, a^4, a^8, \dots, a^{2^{\lfloor \log n \rfloor}}$.

Vậy ta chỉ cần biết cách tính nhanh của những số mũ trên. Thật may điều này rất đơn giản, vì mỗi số trong dãy trên là bình phương của số ngay trước nó trong dãy.

$$\begin{align}
3^1 &= 3 \\
3^2 &= \left(3^1\right)^2 = 3^2 = 9 \\
3^4 &= \left(3^2\right)^2 = 9^2 = 81 \\
3^8 &= \left(3^4\right)^2 = 81^2 = 6561
\end{align}$$

Vậy để tính $3^{13}$, ta chỉ cần nhân 3 trong số các số trên (bỏ qua $3^2$ vì bit tương ứng trong $n$ không có): $3^{13} = 6561 \cdot 81 \cdot 3 = 1594323$

Độ phức tạp của thuật toán là $O(\log n)$: ta cần tính $\log n$ số mũ của $a$, và sau đó ta phải thực hiện nhiều nhất $\log n$ phép nhân để có được kết quả cuối cùng.

Công thức sau cũng biểu thị ý tưởng ở trên:

$$a^n = \begin{cases}
1 &\text{nếu } n == 0 \\
\left(a^{\frac{n}{2}}\right)^2 &\text{nếu } n > 0 \text{ và } n \text{ chẵn}\\
\left(a^{\frac{n - 1}{2}}\right)^2 \cdot a &\text{nếu } n > 0 \text{ và } n \text{ lẻ}\\
\end{cases}$$

## Cài đặt

Đầu tiên là cách cài đệ quy, cũng là để biểu thị cho công thức đệ quy ở trên

```cpp
long long binpow(long long a, long long b) {
    if (b == 0)
        return 1;
    long long res = binpow(a, b / 2);
    if (b % 2)
        return res * res * a;
    else
        return res * res;
}
```

Cách thứ 2 chúng ta làm không dùng đệ quy. Nó tính tất cả các số mũ trong một vòng lặp, và nhân vào kết quả khi bit tương ứng của $n$ được set. Mặc dù độ phức tạp như nhau, cách này sẽ nhanh hơn cách đầu tiên một chút trong thực tết vì nó không có các hao phí của việc gọi đệ quy.

```cpp
long long binpow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}
```

## Ứng dụng

### Tính nhanh số mũ modulo một số khác

**Bài toán:**
Tính $x^n \bmod m$. Đây là một bài rất phổ biến. Ví dụ như nó được dùng để tính [nghịch đảo modulo]().

**Lời giải:**
Vì ta biết rằng toán tử modulo không can thiệp vào các phép nhân ($a \cdot b \equiv (a \bmod m) \cdot (b \bmod m) \pmod m$), ta có thể dùng lại code ở trên, chỉ cần thay thế mỗi phép nhân bằng phép nhân modulo:

```cpp
long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
```

**Lưu ý:** Nếu $m$ là số nguyên tố, ta có thể tăng tốc tính toán một chút bằng cách tính $x^{n \bmod (m-1)}$ thay vì tính $x ^ n$. Đây là ứng dụng của [Định lý Fermat nhỏ]()

### Tính nhanh số Fibonacci

**Bài toán:** Tính số Fibonacci thứ $n$ ($F_n$).

**Lời giải:** 
Ở đây chúng ta sẽ chỉ đi sơ lược về thuật toán. Nếu bạn muốn tìm hiểu thêm, xin hãy đọc bài [Số Fibonacci](). Để tính số Fibonacci tiếp theo, ta chỉ cần 2 số trước đó, vì $F_n = F_{n-1} + F_{n-2}$. Ta có thể tạo một ma trận $2 \times 2$ để mô tả sự biến đổi như sau: sự chuyển tiếp từ $F_i$ và $F_{i+1}$ sang $F_{i+1}$ và $F_{i+2}$. Ví dụ, sau khi dùng phép biến đổi này, cặp $F_0$ và $F_1$ sẽ chuyển thành $F_1$ và $F_2$. Vì vậy, ta có thể luỹ thừa phép biến đổi này lên mũ $n$ để tìm $F_n$ trong độ phức tạp $O(\log n)$.

### Hoán vị $k$ lần { data-toc-label='Hoán vị <script type="math/tex">k</script> lần' }

**Bài toán:** Cho dãy độ dài $n$. Hoán vị $k$ lần dãy đó bằng một hoán vị khác

**Lời giải:** Hoán vị cái hoán vị được cho lên $k$ lần dùng luỹ thừa nhị phân, sau đó áp dụng lên dãy độ dài $n$ đã cho. Độ phức tạp của lời giải này là $O(n \log k)$.

```cpp
vector<int> applyPermutation(vector<int> sequence, vector<int> permutation) {
    vector<int> newSequence(sequence.size());
    for(int i = 0; i < sequence.size(); i++) {
        newSequence[permutation[i]] = sequence[i];
    }
    return newSequence;
}

vector<int> permute(vector<int> sequence, vector<int> permutation, long long b) {
    while (b > 0) {
        if (b & 1) {
            sequence = applyPermutation(sequence, permutation);
        }
        permutation = applyPermutation(permutation, permutation);
        b >>= 1;
    }
    return sequence;
}
```

**Lưu ý:** Bài toán này có thể được giải một cách hiệu quả hơn với độ phức tạp tuyến tính bằng cách tạo một đồ thị hoán vị và xét từng chu trình riêng lẻ. Sau đó bạn có thể tính modulo $k$ kích thước của chu kỳ và tìm vị trí cuối cùng của mỗi số nằm trong chu trình đó.

### Áp dụng nhanh một nhóm các phép toán hình học lên một nhóm các điểm

**Bài toán:** Cho $n$ điểm $p_i$, áp dụng $m$ phép biến đổi cho mỗi điểm này. Mỗi phép biến đổi có thể là phép dịch chuyển, phép nhân toạ độ, hoặc phép xoay quanh một trục toạ độ theo một góc cho trước. Ngoài ra cũng có thể có một "vòng lặp" bao gồm một số phép biến đổi và vòng lặp đó được lặp $k$ lần (thậm chí các vòng lặp có thể lồng nhau). Độ phức tạp của bài toán nên là $O(n \cdot length)$ trong đó $length$ là tổng số các phép biến đổi có thể được thực hiện (sau khi mở các vòng lặp).

**Solution:** Chúng ta hãy xem các phép biến đổi thay đổi toạ độ của một điểm như thế nào

* Phép dịch chuyển: Thêm một hằng số vào mỗi toạ độ.
* Phép nhân toạ độ: Nhân mỗi toạ độ với một hằng số khác nhau.
* Phép xoay: phép này sẽ hơi phức tạp một chút (chúng ta sẽ không đi sâu vào nó), nhưng mỗi toạ độ của điểm sẽ được thể hiện bằng một hàm tuyến tính của toạ độ trước.

Như các bạn có thể thấy, mỗi phép biến đổi có thể được thể hiện bằng một hàm tuyến tính trên các toạ độ điểm. Vì vậy, một phép biến đổi có thể được viết ra một ma trận $4 \times 4$ như sau:

$$\begin{pmatrix}
a_{11} & a_ {12} & a_ {13} & a_ {14} \\
a_{21} & a_ {22} & a_ {23} & a_ {24} \\
a_{31} & a_ {32} & a_ {33} & a_ {34} \\
a_{41} & a_ {42} & a_ {43} & a_ {44}
\end{pmatrix}$$

Lúc đó, khi được nhân với một vector với các toạ độ điểm và một số đơn vị (1) thì ta cũng nhận được một vector mới với toạ độ điểm mới và một số đơn vị.

$$\begin{pmatrix} x & y & z & 1 \end{pmatrix} \cdot
\begin{pmatrix}
a_{11} & a_ {12} & a_ {13} & a_ {14} \\
a_{21} & a_ {22} & a_ {23} & a_ {24} \\
a_{31} & a_ {32} & a_ {33} & a_ {34} \\
a_{41} & a_ {42} & a_ {43} & a_ {44}
\end{pmatrix}
 = \begin{pmatrix} x' & y' & z' & 1 \end{pmatrix}$$

(Tại sao cần chiều thứ 4 vây? Vì nếu không có nó, chùng ta không thể làm phép dịch chuyển được. Phép này yêu cầu chúng ta thêm một hằng số vào các toạ độ điểm. Nếu không có chiều thứ 4, chùng ta sẽ chỉ áp dụng được các phép kết hợp tuyến tính vào thôi, không thêm hằng số vào được.)

Sau đây là một số ví dụ làm thế nào để chuyển phép biến đổi thành ma trận:

* Phép dịch chuyển: dịch chuyển $x$ lên $5$, $y$ lên $7$ và $z$ lên $9$.

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
5 & 7 & 9 & 1
\end{pmatrix}$$

* Phép nhân toạ độ: nhân toạ độ $x$ lên $10$ và $y$, $z$ lên $5$.

$$\begin{pmatrix}
10 & 0 & 0 & 0 \\
0 & 5 & 0 & 0 \\
0 & 0 & 5 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

* Phép xoay: xoay $\theta$ độ quanh trục $x$ theo quy tắc bàn tay phải (hướng ngược chiều kim đồng hồ).

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \cos \theta & -\sin \theta & 0 \\
0 & \sin \theta & \cos \theta & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

Bây giờ, một phép biến đổi được biểu diễn bởi một ma trận, dãy phép biến đổi sẽ được biểu diễn bởi tích các ma trận đó, và một vòng lặp $k$ được biểu diễn bởi ma trận luỹ thừa $k$ (dễ dàng tính được nếu dùng luỹ thừa nhị phân trong $O(\log{k})$). Bằng cách này, ma trận biểu diễn tất cả các phép biến đổi sẽ được tính trong $O(m \log{k})$, sau đó nó sẽ được áp dụng vào từng điểm trong số $n$ điểm trong $O(n)$ với độ phức tạp cuối cùng là $O(n + m \log{k})$.


### Số đường đi độ dài $k$ trong đồ thị { data-toc-label='Số đường đi độ dài <script type="math/tex">k</script> trong đồ thị' }

**Bài toán:** Cho đồ thị có hướng không trọng số gồm $n$ đỉnh, tìm số đường đi độ dài $k$ từ bất kỳ đỉnh $u$ nào đến bất kỳ đỉnh $v$ nào.

**Lời giải:** Bài này đã được để cập kỹ hơn trong một [bài viết khác](). Thuật toán bao gồm việc luỹ thừa ma trận kề $M$ của đồ thị (ma trận có $m_{ij} = 1$ nếu có cạnh từ $i$ đến $j$, hoặc $0$ nếu không có) lên mũ $k$. Giờ $m_{ij}$ sẽ là số đường đi độ dài $k$ từ $i$ đến $j$. Độ phức tạp của thuật toán này là $O(n^3 \log k)$.

**Lưu ý:** Trong cùng bài viết đó, một biến thể khác của bài này cũng được nhắc đến: khi các cạnh có trọng số và bạn cần phải tìm đường đi có trọng số nhỏ nhất mà có $k$ cạnh. Bài này cũng có thể được giải bằng việc luỹ thừa ma trận kề. Ma trận sẽ có trọng số của các cạnh từ $i$ đến $j$, hoặc $\infty$ nếu không có cạnh như vậy. Bạn cũng phải dùng một toán tử khác để nhân 2 ma trận: 2 giá trị được cộng vào nhau và sau đó lấy min (thay vì nhân và cộng như nhân ma trận bình thường). Nghĩa là: $result_{ij} = \min\limits_{1\ \leq\ k\ \leq\ n}(a_{ik} + b_{kj})$.

### Biến thể của luỹ thừa nhị phân: nhân 2 số modulo $m$ { data-toc-label='Biến thể của luỹ thừa nhị phân: nhân 2 số modulo <script type="math/tex">m</script>' }

**Bài toán:** Nhân 2 số $a$ và $b$ modulo $m$. Cho $a$ và $b$ nằm trong các kiểu dữ liệu có sẵn trong ngôn ngữ lập trình, nhưng tích của chúng to hơn số 64-bit. Ý tưởng là tính $a \cdot b \pmod m$ mà không dùng xử lý số lớn.

**Lời giải:** Chúng ta sẽ dùng cách xây dựng nhị phân ở trên, và chỉ dùng phép cộng thay vì phép nhân. Nói cách khác, chúng ta mở rộng phép nhân 2 số thành $O (\log m)$ phép cộng và nhân đôi (mà thực ra vẫn là phép cộng 2 số giống nhau thôi).

$$a \cdot b = \begin{cases}
0 &\text{nếu }a = 0 \\
2 \cdot \frac{a}{2} \cdot b &\text{nếu }a > 0 \text{ và }a \text{ chẵn} \\
2 \cdot \frac{a-1}{2} \cdot b + b &\text{nếu }a > 0 \text{ và }a \text{ lẻ}
\end{cases}$$

**Lưu ý:** Bạn có thể giải bài này bằng cách dùng các phép toán liên quan đến dấu chấm động. Đầu tiên tính $\frac{a \cdot b}{m}$ dùng số thực và ép kiểu nó về số nguyên (unsigned) $q$. Lấy $a \cdot b$ trừ $q \cdot m$ dùng các toán tử số nguyên (unsigned) và modulo $m$ kết quả để tìm ra đáp án. Lời giải này nghe có vẻ không đáng tin lắm, nhưng nó rất nhanh và rất dễ cài đặt. Đọc [ở đây](https://cs.stackexchange.com/questions/77016/modular-multiplication) để biết thêm thông tin.

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [UVa 1230 - MODEX](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/UVA/UVA%201230.cpp) | 03/10/2019 |
| [UVa 374 - Big Mod](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/UVA/UVA%20374.cpp) | 03/10/2019 |
| [UVa 11029 - Leading and Trailing](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/UVA/UVA%2011029.cpp) | 04/10/2019 |
| [Codeforces - Parking Lot](http://codeforces.com/problemset/problem/630/I) | :white_check_mark: | [Submission](https://codeforces.com/contest/630/submission/62216039) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF630-D12-I.cpp) | 09/10/2019 |
| [SPOJ - LASTDIG](http://www.spoj.com/problems/LASTDIG/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20LASTDIG.cpp) | 04/10/2019 |
| [SPOJ - LOCKER](http://www.spoj.com/problems/LOCKER/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20LOCKER.cpp) | 12/10/2019 |
| [LA - 3722 Jewel-eating Monsters](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1723) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LiveArchive/LIVEARCHIVE%203722.cpp) | 21/03/2020 |
| [SPOJ - ZSUM](http://www.spoj.com/problems/ZSUM/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20ZSUM.cpp) | 21/03/2020 |
| [Codechef RIFFLES](https://www.codechef.com/problems/RIFFLES) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/76714669) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20RIFFLES.cpp) | 11/10/2022 |
| [Leetcode - Count good numbers](https://leetcode.com/problems/count-good-numbers/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC1922-count-good-numbers.cpp) | 11/10/2022 |