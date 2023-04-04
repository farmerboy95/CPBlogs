# Kĩ thuật Vector cơ sở cho các bài toán XOR

## Nguồn

<img src="/CPBlogs/img/codeforces.png" width="16" height="16"/> [A Beautiful Technique for Some XOR Related Problems](https://codeforces.com/blog/entry/68953)

## Giới thiệu

Vector cơ sở (hay khử Gauss nhị phân) là một kỹ thuật hay dùng trong các bài toán kiểu tổng XOR (XOR-sum). Một cách tổng quát hơn, dạng bài này như sau: cho một dãy các số, bài toán sẽ yêu cầu tính tổng XOR của tất cả các đoạn con của dãy số đó. Kỹ thuật này cũng có thể được sử dụng trong các bài xử lý online (xử lý trực tiếp truy vấn ngay sau khi nhận, khác với xử lý offline là khi ta nhận tất cả các truy vấn rồi xử lý): bài toán có thể cho các truy vấn để thêm số vo mảng (không xoá số) và giữa các truy vấn đó, sẽ có các truy vấn tìm giá trị giống như bài toán trước.

Kỹ thuật này được chia làm 2 phần trong bài viết này, và một số bài toán có thể được giải chỉ với phần đầu tiên.

1. Biểu diễn mỗi số theo dạng nhị phân và cho nó là một vector trên một không gian vector $\mathbb{Z}_2^d$, với $d$ là số lượng tối đa các bit trong một số. Sau đó, XOR của một số số trong này sẽ tương ứng với tổng của các vector tương ứng trong không gian vector.
2. Bằng một cách nào đó, liên hệ kết quả đó với các truy vấn tổng XOR với cơ sở của các vector trong phần 1.

## Phần 1: Liên hệ giữa XOR và phép cộng vector trong $\mathbb{Z}_2^d$ { data-toc-label='Phần 1: Liên hệ giữa XOR và phép cộng vector trong không gian vector nhị phân d chiều' }

Giả sử ta XOR số $2$ và số $3$, nó trông sẽ như sau:

$$\begin{equation*}\begin{array}{r} (10)_2\\ \underline{\oplus\;(11)_2}\\ (01)_2 \end{array}\end{equation*}$$

Giờ với mỗi cặp bit tương ứng của hai số trên, so sánh kết quả XOR với kết quả tổng modulo $2$:

| Bit thứ | Số đầu tiên | Số thứ hai | $\oplus$ | Tổng | Tổng modulo $2$ |
| :---: | :-----------: | :---: | :---: | :---: | :---: |
| 1 | 0 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 0 | 2 | 0 |

Để ý rằng cột 4 và 6 trông có vẻ giống nhau, nên ta thấy rằng XOR của hai số thực ra cũng giống như, với mỗi bit, tổng mỗi bit riêng biệt modulo $2$.

Xét một mặt phẳng toạ độ với các toạ độ là số nguyên, chỉ bao gồm $0$ và $1$. Nếu bất kì toạ độ nào lớn hơn $1$ hoặc nhỏ hơn $0$, ta sẽ lấy modulo $2$ của nó.

Bằng cách này, sẽ chỉ có bốn điểm trên mặt phẳng toạ độ này: $(0, 0), (0, 1), (1, 0), (1, 1)$. Bất cứ cặp toạ độ nào khác đều sẽ liên hệ đến chúng, ví dụ, điểm $(3, 2)$ trùng với điểm $(1, 0)$ vì $3 \equiv 1$ và $2 \equiv 0$ modulo $2$.

Với hệ toạ độ này, ta có thể biểu diễn số $2 = (10)_2$ thành điểm $(0, 1)$ bằng cách đặt bit đầu tiên của $2$ là $x$ và bit thứ hai là $y$ trên mặt phẳng toạ độ. Đặt điểm này là $P$. Ta sẽ có vector vị trí của $2$ sẽ là $\overrightarrow{OP}$ với $O(0, 0)$ là gốc toạ độ. Tương tự, vector vị trí của $3$ là $\overrightarrow{OQ}$ với $Q = (1, 1)$.

Có một điều thú vị ở đây, nếu ta cộng hai vector vị trí này với nhau, mỗi toạ độ sau khi lấy tổng thì modulo $2$, kết quả sẽ là vector vị trí của XOR của hai vector vị trí ban đầu. Ví dụ, cộng hai vector \overrightarrow{OP} và \overrightarrow{OQ} ta sẽ được \overrightarrow{OR} với $R(1, 0)$ là điểm tương ứng với XOR của $2$ và $3$.

Trước khi đi vào bài tập của phần này, mình sẽ giải thích không gian vector và $\mathbb{Z}_2^d$ là gì.

- Không gian vector: Chỉ là một bộ các vector.
- $\underline{\mathbb{Z_2}}$: $\mathbb{Z_m}$ là bộ số dư khi chia cho $m$. Vậy $\mathbb{Z_2}$ đơn giản là bộ $\{0, 1\}$, vì đây là các số dư có thể có khi chia lấy dư với $2$.
- $\underline{\mathbb{Z_2^d}}$: Một không gian vector $d$ chiều bao gồm tất cả các vector vị trí chứa $d$ chỉ số toạ độ, tất cả các toạ độ này là phần tử của $\mathbb{Z_2}$. Ví dụ, hệ toạ độ ban đầu là một hệ toạ độ hai chiều, nên nó là $\mathbb{Z_2^2}$. $\mathbb{Z_2^3}$ sẽ là một hệ toạ độ 3 chiều với $2^3 = 8$ điểm, tất cả các chỉ số toạ độ modulo $2$.

Vậy nên, toán tử XOR của chúng ta tương đương với phép cộng vector trong không gian vector $\mathbb{Z_2^d}$

### Bài tập 1

[CF 895C - Square Subsets](https://codeforces.com/contest/895/problem/C)

Tìm số các tập con không rỗng (không nhất thiết liên tiếp), modulo $10^9+7$ của mảng $a$ có độ dài $n$ ($1 \le n \le 10^5$) với $1 \leq a_i \leq 70$, mà tích các phần tử trong tập con đó là một số chính phương.

??? tip "Lời giải"
    Rõ ràng là cách giải của chúng ta sẽ xoay quanh $a_i$ vì giá trị lớn nhất của nó chỉ là $70$.

    Để một số là chính phương, mỗi thừa số nguyên tố của nó phải có số mũ chẵn. Chỉ có $19$ số nguyên tố dưới $70$, nên ta có thể dùng số 19 bit để biểu diễn mỗi phần tử của mảng, với bit thứ $i$ là $0$ khi số mũ của số nguyên tố thứ $i$ chẵn, ngược lại là $1$ với trường hợp lẻ.

    Bài toán lúc này thu lại thành tìm số tập con không rỗng của mảng mà tổng XOR của các phần tử trong tập là $0$.

    Ta có thể dùng quy hoạch động để giải. Gọi $dp[at][msk]$ là số tập con trong đoạn $\{a_1, a_2, \ldots, a_{\text{at} }\}$ mà tổng XOR của các phần tử trong các tập con đó bằng $msk$. Thì công thức sẽ như sau

    $$\text{dp[at][msk] = dp[at - 1][msk] + dp[at - 1][msk ^ mask[at]]}$$

    với giá trị ban đầu $dp[0][0] = 1$. Kết quả bài toán sẽ là $dp[n][0]$.

    Nhưng lúc này độ phức tạp là $O(n \cdot 2^{19})$, quá lớn.

    Để ý rằng ngay cả khi $n \leq 10^5$, số các phần tử khác nhau vẫn chỉ là $70$. Cho nên, nếu ta tìm DP cho $70$ mask khác nhau này, và nếu với mỗi $1 \leq at \leq 70$ ta biết số cách để chọn số chẵn / lẻ các số trong mảng với giá trị là $at$, ta có thể dễ dàng tính kết quả với công thức như sau:

    $$\text{dp[at][msk] = dp[at - 1][msk] * poss[at][0] + dp[at - 1][msk ^ mask[at]] * poss[at][1]}$$

    với $poss[at][0]$ là số cách chọn chẵn các số $at$ trong mảng, và $poss[at][1]$ là số cách chọn lẻ các số $at$ trong mảng.

    Code mẫu:

    ```cpp
    #include <bits/stdc++.h>
    
    using namespace std;
    
    const int N = 1e5 + 10;
    const int MAX_A = 70;
    const int TOTAL_PRIMES = 19;
    const int MOD = 1e9 + 7;
    
    int n;
    int poss[MAX_A + 1][2];
    const int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67};
    int mask[MAX_A + 1];
    int dp[MAX_A + 1][1 << TOTAL_PRIMES];
    
    int main() {
        cin >> n;
    
        for (int i = 1; i <= MAX_A; i++) poss[i][0] = 1;
    
        for (int i = 1; i <= n; i++) {
            int a;
            scanf("%d", &a);
    
            int tmp = poss[a][0];
            poss[a][0] = (poss[a][0] + poss[a][1]) % MOD;
            poss[a][1] = (poss[a][1] + tmp) % MOD;
        }
    
        for (int i = 1; i <= MAX_A; i++) {
            for (int p = 0; p < TOTAL_PRIMES; p++) {
                int cnt = 0;
                int at = i;
    
                while (at % primes[p] == 0) {
                    at /= primes[p];
                    cnt++;
                }
    
                if (cnt & 1) mask[i] |= (1 << p);
            }
        }
    
        int max_mask = 1 << TOTAL_PRIMES;
        dp[0][0] = 1;
        
        for (int at = 1; at <= MAX_A; at++)
            for (int msk = 0; msk < max_mask; msk++) {
                dp[at][msk] = dp[at - 1][msk] * 1LL * poss[at][0] % MOD;
    
                dp[at][msk] += dp[at - 1][msk ^ mask[at]] * 1LL * poss[at][1] % MOD;
                dp[at][msk] %= MOD;
            }
    
        cout << (dp[MAX_A][0] + MOD - 1) % MOD << endl;
    
        return 0;
    }
    ```

Vì số các mask chỉ là $70$ trong bài trên, ta có thể sử dụng DP để tìm tất cả các giá trị XOR. Nhưng nếu giới hạn lớn hơn thì sao, ví dụ như $10^5$. Đó là lúc ta cần dùng phần hai của kĩ thuật này, đôi khi nó cũng dùng được với truy vấn online.

## Phần 2: Giới thiệu Vector cơ sở

Ta cần định nghĩa vài thứ ở đây để đi tiếp. Tất cả các vector được đề cập ở dưới, ngoại trừ các vector null.

- **Các vector độc lập**: Một tập các vector $\vec{v_1}, \vec{v_2}, \ldots, \vec{v_n}$ được gọi là độc lập khi không có vector nào là tổng của bất kỳ tổ hợp tuyến tính nào của các vector còn lại.
- **Cơ sở của không gian vector**: Một tập các vector được gọi là cơ sở của không gian vector khi tất cả các vector thành phần của không gian vector đó có thể được biểu diễn duy nhất bằng tổng của một tổ hợp tuyến tính của các thành phần của cơ sở đó.

Một số tính chất của các vector độc lập và vector cơ sở mà ta cần như sau:

1. Trong một tập các vector độc lập, ta có thể thay đổi bất cứ vector nào bằng cách cộng vào nó bất kỳ tổ hợp tuyến tính nào của tập đó, và các vector vẫn độc lập với nhau. Điều thú vị ở đây là, tập vector trong không gian được biểu diễn bằng một số tổ hợp tuyến tính thì giữ nguyên sau khi ta thay đổi một hay một vài vector trước đó.
2. Để ý rằng, trong trường hợp không gian vector $\mathbb{Z}_2^d$, hệ số của tổ hợp tuyến tính các vector cũng phải nằm trong $\mathbb{Z}_2$. Nghĩa là, một vector thành phần chỉ có thể nằm trong hoặc không nằm trong tổ hợp tuyến tính.
3. Cơ sở của không gian vector thực ra là một tập bé nhất các vector sao cho tất cả các vector khác trong không gian vector được biểu diễn bằng một tổ hợp tuyến tính của những vector nằm trong tập này.
4. Các vector cơ sở độc lập với nhau.
5. Với mọi tập vector độc lập mà số vector ít hơn số vector trong cơ sở, sẽ có các vector trong không gian vector không biểu diễn được.
6. Tương tự, nếu số vector trong tập nhiều hơn số vector trong cơ sở, sẽ có một số vector không cần thiết. Nếu $d$ là số vector của cơ sở của không gian vector, khi ta tìm được tập $d$ vector độc lập, nó chính là cơ sở. Ta không thể thêm vector vào tập này, vì vector mới sẽ được biểu diễn bằng tập vector cũ.
7. Với không gian vector $d$ chiều, cơ sở của nó chỉ có thể có nhiều nhất $d$ vector thành phần.

Với những tính chất này, ta có thể giải được một số bài khó với những cách rất hay. Nhưng khoan, ta cần xem làm thế nào ta có thể tìm được cơ sở của không gian vector chứa $n$ vector, các vector này là thành phần của $\mathbb{Z}_2^d$. Thuật toán sau đây chạy trong $O(n \cdot d)$.

## Thuật toán

Tất cả các vector ở đây nằm trong $\mathbb{Z}_2^d$, nên chúng có thể được biểu diễn bằng số nhị phân độ dài $d$.

Giả sử rằng tại mỗi bước, ta có một vector đầu vào $\vec{v_i}$ và ta đã có cơ sở của các vector đầu vào trước đó $\vec{v_1}, \vec{v_2}, \ldots, \vec{v_{i - 1}}$, và giờ ta cần cập nhật cơ sở sao cho nó có thể biểu diễn vector mới $\vec{v_i}$ này.

Để làm được điều đó, đầu tiên ta cần kiểm tra xem $\vec{v_i}$ có thể được biểu diễn bằng cơ sở hiện tại hay không.

Nếu biểu diễn được, cơ sở hiện tại không cần phải cập nhật thêm gì cả. Nhưng nếu không biểu diễn được, ta cần thêm vector $\vec{v_i}$ này vào trong cơ sở.

Việc ta cần làm duy nhất ở đây chính là, làm sao để kiểm tra một cách hiệu quả vector mới có thể được biểu diễn bởi cơ sở hay không. Trước hết ta cần dùng tính chất 1 để sửa lại bất kỳ vector mới nào trước khi đưa vào cơ sở, mà không phá vỡ cơ sở này. Bằng cách này, ta có thể kiểm soát tốt hơn trạng thái của cơ sở của không gian vector. Ta làm như sau:

- Gọi $f(\vec{v})$ là bit 1 đầu tiên của biểu diễn nhị phân của vector. Ta cần đảm bảo mỗi vector trong cơ sở có $f$ khác nhau.
- Đầu tiên, không có vector nào trong cơ sở, nên không có $f$ nào giống nhau được. Giả sử ta đang ở bước thứ $i$, ta đang kiểm tra xem vector $\vec{v_i}$ có thể được biểu diễn bằng cơ sở hay không. Bởi vì tất cả các $f$ của các vector trong cơ sở đã khác nhau rồi, ta lấy vector có giá trị $f$ bé nhất, gọi vector này là $\vec{b_1}$.
- Nếu $f(\vec{v_i}) < f(\vec{b_1})$, ta sẽ không thể biểu diễn vector $\vec{v_i}$ bằng bất cứ tổ hợp tuyến tính nào của cơ sở, vì không có vector nào có bit 1 tại vị trí $f(\vec{v_i})$, theo tính chất 2. Nên $\vec{v_i}$ sẽ là một vector trong cơ sở, và vì $f$ của vector này khác với tất cả các vector đang tồn tại trong cơ sở, ta có thể thêm nó vào tập vector cơ sở, và lưu giá trị $f$ của nó.
- Nhưng nếu $f(\vec{v_i}) == f(\vec{b_1})$, ta cần phải trừ $\vec{b_1}$ ra khỏi $\vec{v_i}$ nếu ta muốn biểu diễn $\vec{v_i}$ là một tổ hợp tuyến tính của tập vector của cơ sở, vì không có vector nào trong cơ sở có bit 1 tại vị trí $f(\vec{v_i}) = f(\vec{b_1})$. Nên ta trừ $\vec{b_1}$ khỏi $\vec{v_i}$ và tiếp tục đến $\vec{b_2}$.
- Lưu ý, thay đổi giá trị $\vec{v_i}$ không gây ra bất cứ vấn đề gì theo tính chất 1. $\vec{v_i}$ và $\vec{v_i} - \vec{b_1}$ là như nhau trong trường hợp này. Nếu trong những bước tiếp theo ta thấy $\vec{v_i}$ không biểu diễn được bằng tập các vector cơ sở, ta vẫn có thể thêm vector đã được thay đổi này (nhiều lần trừ) vào trong cơ sở, vì tập vector trong không gian được biểu diễn bởi cơ sở mới vẫn như không đổi ngay cả khi ta thêm $\vec{v_i}$ ban đầu vào.
- Nếu sau khi duyệt qua tất cả các vector cơ sở trong $\vec{b}$ và trừ chúng ra khỏi $\vec{v_i}$ (nếu cần) rồi, $\vec{v_i}$ vẫn không phải vector null, nghĩa là $\vec{v_i}$ mới có $f$ lớn hơn tất cả các vector trong cơ sở, ta cần thêm vector này vào cơ sở và lưu giá trị $f$ của nó.

Đây là cách cài đặt hàm thêm vector vào cơ sở, các vector được biểu diễn bằng số nhị phân độ dài $d$.

```cpp
int basis[d]; // basis[i] lưu biểu diễn nhị phân (mask) của vector có giá trị f là i, ta lưu dưới dạng số nguyên
int sz; // Kích thước hiện tại của cơ sở

void insertVector(int mask) {
    for (int i = 0; i < d; i++) {
        if ((mask & (1 << i)) == 0) continue; // tiếp tục nếu i != f(mask)

        if (!basis[i]) { // Nếu không có vector nào trong cơ sở có bit 1 ở vị trí i, ta thêm vector đang xét vào cơ sở
            basis[i] = mask;
            ++sz;
            return;
        }

        mask ^= basis[i]; // Ngược lại ta trừ vector trong cơ sở khỏi vector đang xét
    }
}
```

Ta xét một số bài tập.

### Bài tập 2a

[Nguồn bài - Problem 2, Ví dụ 1](https://codeforces.com/blog/entry/60003)

Cho một tập $S$ kích thước $1 \le n \le 10^5$ với các phần tử $0 \le a_i \lt 2^{20}$. Tìm số các số khác nhau có thể được biểu diễn bởi tổng XOR của các phần tử trong set.

??? tip "Lời giải"
    Mỗi phần tử là một vector trong không gian vector nhị phân 20 chiều, tức là $\mathbb{Z}_2^{20}$. Ta có thể tìm cơ sở của nó trong $O(d \cdot n)$. Với mỗi tổ hợp tuyến tính của cơ sở, ta có một tổng XOR khác nhau. Cho nên đáp án sẽ là $2^\text{kích thước của cơ sở}$. Kiểu số nguyên sẽ thích hợp với bài này vì kích thước của cơ sở $\leq d = 20$ theo tính chất 7.

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;    
    const int N = 1e5 + 10, LOG_A = 20;
    int basis[LOG_A];
    int sz;

    void insertVector(int mask) {
        for (int i = 0; i < LOG_A; i++) {
            if ((mask & 1 << i) == 0) continue;

            if (!basis[i]) {
                basis[i] = mask;
                ++sz;
                
                return;
            }

            mask ^= basis[i];
        }
    }

    int main() {
        int n;
        cin >> n;

        while (n--) {
            int a;
            scanf("%d", &a);

            insertVector(a);
        }

        cout << (1 << sz) << endl;

        return 0;
    }
    ```

### Bài tập 2b

[Codechef - XORCMPNT](https://www.codechef.com/problems/XORCMPNT)

Cho một đồ thị có $2^k$ node đánh số từ $0$ đến $2^k - 1$, $1 \leq k \leq 30$. Ngoài ra ta còn được cho thêm $1 \leq M \leq 10^5$ số nguyên $x_1, x_2, \ldots, x_M$ nằm trong khoảng $0 \le x_i \le 2^{k} - 1$. Trong đồ thị, hai đỉnh $u$ và $v$ có cạnh khi và chỉ khi $u \oplus v = x_i$ với một $x_i$ nào đó. Tìm số thành phần liên thông trong đồ thị.

??? tip "Lời giải"
    Lời giải chính thức của bài này các bạn có thể đọc ở [đây](https://discuss.codechef.com/t/xorcmpnt-editorial/25928).
    Từ một đỉnh $u$, một đỉnh $v$ có thể tới được từ $u$ khi và chỉ khi tồn tại một tập con $S$ của mảng $M$ phần tử ban đầu sao cho XOR của các phần tử trong $S$ bằng $u \oplus v$. Lưu ý rằng $u$ luôn đến được $u$ theo tính chất này vì $u \oplus u = 0$ với tập $S$ rỗng.

    Sau khi có được cơ sở của mảng $M$ phần tử ban đầu (không gian vector $\mathbb{Z}_2^{k}$), ta biết được số bit mà cơ sở có thể thay đổi được, dựa vào mảng $basis[i]$, và số các số có thể được tạo ra từ cơ sở là $2^p$ với $p$ là số $basis[i]$ có vector, giống bài trước. Xét một đỉnh $u$, thành phần liên thông chứa $u$ sẽ là $2^p$ vì chỉ có thể thay đổi được $p$ bit. Như vậy các số giống nhau ở các bit không nằm trong $p$ sẽ cùng thành phần liên thông. Từ đó đáp án sẽ là $2^{k - p}$.

### Bài tập 3

[Nguồn bài - Problem 2, Ví dụ 3](https://codeforces.com/blog/entry/60003)

Cho một tập $S$ kích thước $1 \le n \le 10^5$ với các phần tử $0 \le a_i \lt 2^{20}$. Tổng XOR lớn nhất của một tập con của tập S ban đầu là bao nhiêu?

??? tip "Lời giải"
    Trong bài này, ta cần chỉnh sửa một chút ở định nghĩa của $f(\vec{b})$. Thay vì $f$ là bit 1 đầu tiên, ta sẽ cho $f$ là bit 1 cuối cùng.

    Để tìm được giá trị lớn nhất, ta khởi tạo đáp án là $0$ và duyệt các vector cơ sở bắt đầu với vector có $f$ lớn nhất.

    Giả sử ta đang xét vector cơ sở $\vec{b}$ và ta thấy đáp án hiện tại bit thứ $f(\vec{b})$ không phải là bit $1$, ta sẽ thêm $\vec{b}$ vào đáp án. Cách tham lam này chính xác vì vị trí $f(\vec{b})$ là vị trí lớn nhất có bit $1$, và ta phải cho nó bằng $1$ mà không quan tâm đến các bit tiếp theo có về $0$ hay không.

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    const int N = 1e5 + 10, LOG_A = 20;
    int basis[LOG_A];

    void insertVector(int mask) {
        for (int i = LOG_A - 1; i >= 0; i--) {
            if ((mask & 1 << i) == 0) continue;

            if (!basis[i]) {
                basis[i] = mask;
                return;
            }

            mask ^= basis[i];
        }
    }

    int main() {
        int n;
        cin >> n;

        while (n--) {
            int a;
            scanf("%d", &a);

            insertVector(a);
        }

        int ans = 0;

        for (int i = LOG_A - 1; i >= 0; i--) {
            if (!basis[i]) continue;

            if (ans & 1 << i) continue;

            ans ^= basis[i];
        }

        cout << ans << endl;
        return 0;
    }
    ```

### Bài tập 4

[CF 203881 - Godzilla and Pretty XOR](https://codeforces.com/group/qcIqFPYhVr/contest/203881/problem/S)

Cho một tập $S$ ban đầu rỗng, có $1 \leq n \leq 10^6$ truy vấn trên tập này. Gọi $X$ là tập gồm tất cả các tổng XOR có thể có của các phần tử thuộc $S$. Có 2 loại truy vấn như sau:

- Truy vấn dạng 1: Thêm một phần tử $1 \leq k \leq 10^5$ vào tập $S$, nếu đã tồn tại thì bỏ qua.
- Truy vấn dạng 2: Cho $k$, in ra số nhỏ thứ $k$ của $X$, đảm bảo rằng $k \leq |X|$.

??? tip "Lời giải"
    Khá giống với bài trước. Với truy vấn dạng 2, ta duyệt các vector cơ sở theo thứ tự giảm dần của giá trị $f$.

    Giá sử $\vec{b_h}$ có giá trị $f$ lớn nhất. Ban đầu ta biết rằng có $2^\text{kích thước cơ sở}$ phần tử trong $X$. Vậy nên, nếu $k <= 2^\text{kích thước cơ sở - 1}$, ta có thể set bit thứ $f(\vec{b_h})$ là $0$. Ngược lại ta set nó là $1$ và trừ $2^\text{kích thước cơ sở - 1}$ ra khỏi $k$. Sau đó ta tiếp tục với vector cơ sở tiếp theo. Đến cuối cùng $k$ sẽ là $1$ và ta sẽ lấy được đáp án bằng cách set 0 với tất cả các bit từ $f(\vec{b_i})$ trở đi.

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    const int N = 1e6 + 10, LOG_K = 30;
    int basis[LOG_K], sz;
    
    void insertVector(int mask) {
        for (int i = LOG_K - 1; i >= 0; i--) {
            if ((mask & 1 << i) == 0) continue;
    
            if (!basis[i]) {
                basis[i] = mask;
                sz++;
    
                return;
            }
    
            mask ^= basis[i];
        }
    }
    
    int query(int k) {
        int mask = 0;
    
        int tot = 1 << sz;
        for (int i = LOG_K - 1; i >= 0; i--)
            if (basis[i]) {
                int low = tot / 2;
    
                if ((low < k && (mask & 1 << i) == 0) ||
                    (low >= k && (mask & 1 << i) > 0)) mask ^= basis[i];
    
                if (low < k) k -= low;
    
                tot /= 2;
            }
    
        return mask;
    }
    
    int main() {
        int n;
        cin >> n;
    
        while (n--) {
            int t, k;
            scanf("%d %d", &t, &k);
    
            if (t == 1) insertVector(k);
            else printf("%d\n", query(k));
        }
    
        return 0;
    }
    ```

### Bài tập 5

[CF 959F - Mahmoud and Ehab and yet another xor task](https://codeforces.com/contest/959/problem/F)

Cho mảng độ dài $1 \le n \le 10^5$ với các phần tử $0 \le a_i \lt 2^{20}$. Ta cần trả lời $1 \le q \le 10^5$ truy vấn.

Trong mỗi truy vấn ta có hai số nguyên $1 \le l \le n$ và $0 \le x \lt 2^{20}$. Tìm số tập con của $l$ phần tử đầu tiên của mảng, lấy modulo $10^9+7$, sao cho tổng XOR của các phần tử trong tập là $x$.

??? tip "Lời giải"
    Ta có thể trả lời các truy vấn một cách offline. Ban đầu ta lưu các truy vấn theo $l$, tức là với mỗi $l$ ta có một số truy vấn $x_1, x_2, \ldots, x_m$. Sau đó duyệt từng $l$ từ nhỏ đến lớn, với mỗi $l$ ta duy trì cơ sở của không gian vector của tiền tố đó. Tiếp đến ta lần lượt trả lời các truy vấn của $l$ này. Để trả lời truy vấn, ta kiểm tra xem $x$ có được biểu diễn bằng cơ sở hiện tại hay không (mà không cần thêm $x$ vào cơ sở, ở đây ta chỉ cần sửa hàm `insertVector` lại một chút).

    Nếu không biểu diễn được, đáp án cho truy vấn này là $0$. Nếu biểu diễn được, đáp án sẽ là $2^{l - b}$, với $b$ là kích thước cơ sở của tiền tố $l$ phần tử, bởi vì tập này bao gồm $l - b$ vector không nằm trong cơ sở, nên bất cứ tập con nào trong tập các vector này đều có thể kết hợp với một tập con của cơ sở để tạo thành $x$.

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    typedef pair<int, int> ii; 
    #define x first
    #define y second
    
    const int N = 1e5 + 10;
    const int LOG_A = 20;
    const int MOD = 1e9 + 7;
    
    int n;
    int a[N];
    
    int q;
    ii q_data[N];
    vector<int> q_at[N];
    int powers[N];
    int ans[N];
    
    int base[LOG_A], sz;

    bool checkXor(int mask) {
        for (int i = 0; i < LOG_A; i++) {
            if ((mask & 1 << i) == 0) continue;
    
            if (!base[i]) return false;
    
            mask ^= base[i];
        }
    
        return true;
    }

    void insertVector(int mask) {
        for (int i = 0; i < LOG_A; i++) {
            if ((mask & 1 << i) == 0) continue;
    
            if (!base[i]) {
                base[i] = mask;
                sz++;
    
                return;
            }
    
            mask ^= base[i];
        }
    }
    
    int main() {
        cin >> n >> q;
    
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    
        for (int i = 1; i <= q; i++) {
            scanf("%d %d", &q_data[i].x, &q_data[i].y);
            q_at[q_data[i].x].push_back(i);
        }
    
        powers[0] = 1;
        for (int i = 1; i < N; i++)
            powers[i] = powers[i - 1] * 2LL % MOD;
    
        for (int at = 1; at <= n; at++) {
            insertVector(a[at]);
    
            for (int at_q : q_at[at])
                if (checkXor(q_data[at_q].y)) {
                    ans[at_q] = powers[at - sz];
                }
        }
    
        for (int i = 1; i <= q; i++) printf("%d\n", ans[i]);
    
        return 0;
    }
    ```

### Bài tập 6

[CF 1101G - (Zero XOR Subset)-less](https://codeforces.com/contest/1101/problem/G)

Cho mảng độ dài $1 \le n \le 2 \cdot 10^5$ với các phần tử $0 \le a_i \le 10^9$. Ta cần tìm số đoạn lớn nhất mà mảng này có thể phân ra, thoả mãn các điều kiện sau:

1. Mỗi phần tử nằm trong đúng một đoạn.
2. Mỗi đoạn có ít nhất một phần tử.
3. Không tồn tại một tập con các đoạn mà tổng XOR của các phần tử trong các đoạn của tập con đó bằng 0.

In ra $-1$ nếu không phân ra được như vậy.

??? tip "Lời giải"
    Để ý rằng tất cả các tập con của một tập đều có tổng XOR khác $0$ tương đương với việc nói tất cả các tập con của tập đó có tổng XOR đôi một khác nhau. Vì vậy tổng XOR của các đoạn trong đáp án phải là các vector độc lập. Đây là observation đầu tiên trong hai observation quan trọng.

    Observation thứ hai là, giả sử ta chọn được một số đoạn $[l_1 = 1, r_1], [l_2 = r_1 + 1, r_2], \ldots, [l_k = r_{k - 1} + 1, r_k]$. Gọi $p_i$ là XOR của tổng XOR của $i$ đoạn đầu tiên. Sau đó, để ý răng mọi XOR có thể có từ một tập con nào đó của các đoạn này có thể được tạo ra bằng cách XOR một tập con trong tập $\{p_1, p_2, \ldots, p_k\}$ và ngược lại. Điều đó có nghĩa là tập các tổng XOR của các đoạn này và tập các XOR tiền tố của các đoạn này là như nhau trong không gian vector $\mathbb{Z}_2^{31}$. Vì vậy, nếu tổng XOR của các đoạn này phải độc lập, thì XOR tiền tố của các đoạn này cũng phải độc lập. Suy ra, đáp án đơn giản là kích thước cơ sở của $n$ XOR tiền tố của mảng.

    Ngoại lệ duy nhất ở đây là khi đáp án là $-1$, khi tổng XOR của tất cả các phần tử trong mảng bằng $0$.

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    const int N = 2e5 + 10, LOG_PREF = 31;
    
    int n;
    int basis[LOG_PREF];
    
    void insertVector(int mask) {
        for (int i = 0; i < LOG_PREF; i++) {
            if ((mask & 1 << i) == 0) continue;
    
            if (!basis[i]) {
                basis[i] = mask;
                return;
            }
    
            mask ^= basis[i];
        }
    }
    
    int main() {
        cin >> n;
    
        int pref = 0;
    
        for (int i = 1; i <= n; i++) {
            int a;
            scanf("%d", &a);
    
            pref ^= a;
            insertVector(pref);
        }
    
        if (pref == 0) {
            cout << -1 << endl;
            return 0;
        }
    
        int ans = 0;
    
        for (int i = 0; i < LOG_PREF; i++) {
            ans += (basis[i] > 0);
        }
    
        cout << ans << endl;
    
        return 0;
    }
    ```

## Template

```cpp
struct VectorBasis {
    vi basis;
    int d, sz;
    int numVectors;

    VectorBasis(int d) {
        this->d = d;
        this->sz = 0;

        // numVectors là số vector đã được thêm vào basis 
        // (với hàm insertVector, có thể không tăng sz)
        this->numVectors = 0;
        basis.resize(d);
        FOR(i,0,d-1) basis[i] = 0;
    }

    void insertVector(int mask, bool incCnt = true) {
        // thêm mask vào basis
        if (incCnt) numVectors++;
        FOR(i,0,d-1) {
            if (!(mask & (1 << i))) continue;

            if (!basis[i]) {
                basis[i] = mask;
                sz++;
                return;
            }

            mask ^= basis[i];
        }
    }

    bool checkXor(int mask) {
        // xét xem mask có cho được vào basis hay không
        FOR(i,0,d-1) {
            if (!(mask & (1<<i))) continue;
            if (!basis[i]) return false;
            mask ^= basis[i];
        }
        return true;
    }

    void merge(VectorBasis &v) {
        // chập 2 basis với cùng số chiều
        // dùng để kết hợp với segment tree
        numVectors += v.numVectors;
        FOR(i,0,d-1) {
            if (v.basis[i]) {
                insertVector(v.basis[i], false);
            }
        }
    }
};
```

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [CF 895C - Square Subsets](https://codeforces.com/contest/895/problem/C) | :white_check_mark: | [Submission](https://codeforces.com/contest/895/submission/60660185) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF895-D2-C.cpp) | 16/09/2019 |
| [Codechef - XORCMPNT](https://www.codechef.com/problems/XORCMPNT) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/38800971) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20XORCMPNT.cpp) | 10/10/2020 |
| [CF 203881S - Godzilla and Pretty XOR](https://codeforces.com/group/qcIqFPYhVr/contest/203881/problem/S) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF%5BqcIqFPYhVr-203881%5D-S.cpp) | 12/10/2020 |
| [CF 959F - Mahmoud and Ehab and yet another xor task](https://codeforces.com/contest/959/problem/F) | :white_check_mark: | [Submission](https://codeforces.com/contest/959/submission/95427286) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF959-D2-F.cpp) | 13/10/2020 |
| [CF 1101G - (Zero XOR Subset)-less](https://codeforces.com/contest/1101/problem/G) | :white_check_mark: | [Submission](https://codeforces.com/contest/1101/submission/95517720) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF1101-D12-G.cpp) | 14/10/2020 |
| [HackerEarth - Chef & Chutneys](https://www.hackerearth.com/problem/algorithm/chef-f59c8115/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/HackerEarth/HACKER%20chef-and-chutneys.cpp) | 12/12/2022 |
| [AtCoder AGC 045A - Xor Battle](https://atcoder.jp/contests/agc045/tasks/agc045_a) | :white_check_mark: | [Submission](https://atcoder.jp/contests/agc045/submissions/37250405) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder045-AGC-A.cpp) | 13/12/2022 |
| [AtCoder ABC 141F - Xor Sum 3](https://atcoder.jp/contests/abc141/tasks/abc141_f) | :white_check_mark: | [Submission](https://atcoder.jp/contests/abc141/submissions/37245793) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder141-ABC-F.cpp) | 13/12/2022 |
| [CSAcademy 6F - Xor Cycle](https://csacademy.com/contest/archive/task/xor_cycle) | :white_check_mark: | [Submission](https://csacademy.com/submission/4010082/) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/CSAcademy/CSA6-F.cpp) | 13/12/2022 |
| [IZhO 19 - Lyuboyn](https://oj.uz/problem/view/IZhO19_lyuboyn) | :white_check_mark: | [Submission](https://oj.uz/submission/315655) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/IZhO/IZhO%2019-lyuboyn.cpp) | 23/10/2020 |
| [XX Open Cup - GP Nanjing 2020 - A](https://codeforces.com/gym/102994/problem/A) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/XXOpenCup/XXOpenCup-GPNanjing2020-A.cpp) | 27/10/2020 |
