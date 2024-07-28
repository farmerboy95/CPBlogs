# Lời giải AtCoder Education DP Contest

## Giới thiệu

AtCoder Education DP Contest là một contest rất hay của AtCoder về quy hoạch động (Dynamic Programming). Contest này gồm 26 bài, mỗi bài là một kiểu bài DP khác nhau. Cá nhân mình thấy contest này rất thú vị và đáng để ghi lại lời giải.

Các bạn có thể xem đề bài tại [đây](https://atcoder.jp/contests/dp/tasks).

## Các bài tập

### A - Frog 1

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_a)

Có $N$ viên đá, mỗi viên đá $i$ có chiều cao $h[i]$. Có một con ếch ở viên đá $1$ và muốn nhảy đến viên đá $N$. Ở viên đá $i$, con ếch chỉ có thể nhảy đến viên đá $i+1$ hoặc $i+2$. Chi phí để nhảy từ viên đá $i$ đến viên đá $j$ là $|h[i] - h[j]|$. Hãy tìm chi phí nhỏ nhất để con ếch nhảy từ viên đá $1$ đến viên đá $N$.

Giới hạn:

$2 \leq N \leq 10^5$

$1 \leq h[i] \leq 10^4$

??? tip "Lời giải"
    Ta gọi dp[i] là chi phí nhỏ nhất để con ếch nhảy từ viên đá $1$ đến viên đá $i$. Vì ban đầu con ếch ở viên đá $1$, nên $dp[1] = 0$. Ta có thể nhảy đến viên đá $i$ từ viên đá $i-1$ (khi $i > 1$) hoặc từ viên đá $i-2$ (khi $i > 2). Vậy ta có công thức truy hồi như sau:

    $$dp[i] = \min(dp[i-1] + |h[i] - h[i-1]|, dp[i-2] + |h[i] - h[i-2]|), \forall i, 3 \leq i \leq N$$

    Còn khi $i = 2$, ta chỉ có thể nhảy từ viên đá $1$ đến viên đá $2$, nên $dp[2] = dp[1] + |h[2] - h[1]|$.
    
    Cuối cùng, kết quả sẽ là $dp[N]$.

    Độ phức tạp thời gian của thuật toán là $O(N)$.

    Về mặt không gian, ta có thể dùng mảng $dp$ để lưu kết quả (độ phức tạp $O(N)$), hoặc để ý rằng ta chỉ cần lưu 2 giá trị $dp[i-1]$ và $dp[i-2]$ để cập nhật $dp[i]$, ta có thể lưu chúng vào các biến `dp_1` và `dp_2` để tiết kiệm bộ nhớ (độ phức tạp $O(1)$, tất nhiên là khi không tính mảng đầu vào).

### B - Frog 2

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_b)

Có $N$ viên đá, mỗi viên đá $i$ có chiều cao $h[i]$. Có một con ếch ở viên đá $1$ và muốn nhảy đến viên đá $N$. Ngoài ra ta còn có thêm một số nguyên $K$. Ở viên đá $i$, con ếch chỉ có thể nhảy đến viên đá $i+1, i+2, ..., i+K$. Chi phí để nhảy từ viên đá $i$ đến viên đá $j$ là $|h[i] - h[j]|$. Hãy tìm chi phí nhỏ nhất để con ếch nhảy từ viên đá $1$ đến viên đá $N$.

Giới hạn:

$2 \leq N \leq 10^5$

$1 \leq K \leq 100$

$1 \leq h[i] \leq 10^4$

??? tip "Lời giải"
    Bài trên chính là bài này với $K = 2$. Ta có thể áp dụng cùng một phương pháp để giải bài này.

    Gọi $dp[i]$ là chi phí nhỏ nhất để con ếch nhảy từ viên đá $1$ đến viên đá $i$. Vì ban đầu con ếch ở viên đá $1$, nên $dp[1] = 0$. Để đến viên đá $i$, ta có thể nhảy từ các viên đá $i-j$, $\forall j, 1 \leq j \leq K, i-j > 0$. Vậy ta có công thức truy hồi như sau:

    $$dp[i] = \min_{1 \leq j \leq K, i-j > 0}(dp[i-j] + |h[i] - h[i-j]|)$$

    Cuối cùng, kết quả sẽ là $dp[N]$.

    Độ phức tạp thời gian của thuật toán là $O(NK)$.

    Độ phức tạp không gian của thuật toán là $O(N)$.

### C - Vacation

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_c)

Có $N$ ngày, mỗi ngày $i$ có 3 công việc A, B, C và mỗi công việc sẽ mang lại một số điểm $a[i], b[i], c[i]$. Có một người muốn chọn một công việc mỗi ngày sao cho không chọn 2 công việc cùng một loại liên tiếp. Hãy tìm cách chọn sao cho tổng điểm là lớn nhất.

Giới hạn:

$1 \leq N \leq 10^5$

$1 \leq a[i], b[i], c[i] \leq 10^4$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là tổng điểm lớn nhất có thể đạt được sau $i$ ngày nếu chọn công việc $j$ vào ngày $i$. Ở ngày $i$, ta có thể chọn công việc $j$ nếu $j$ không trùng với công việc $k$ ở ngày $i-1$. Vậy ta có công thức truy hồi như sau:

    $$dp[i][j] = \max(dp[i-1][k] + x[i][j]), \forall k \neq j$$

    Trong đó $x[i][j]$ là điểm của công việc $j$ vào ngày $i$, nghĩa là $x[i][j] = a[i]$ nếu $j = 0$, $x[i][j] = b[i]$ nếu $j = 1$, $x[i][j] = c[i]$ nếu $j = 2$. Ban đầu ta có $dp[1][j] = x[1][j], \forall j, 0 \leq j \leq 2$.
    
    Cuối cùng, kết quả sẽ là $\max(dp[N][j]), \forall j, 0 \leq j \leq 2$.

    Độ phức tạp thời gian của thuật toán là $O(N)$.

    Về mặt không gian, ta để ý rằng $dp[i]$ chỉ phụ thuộc vào $dp[i-1]$ nên ta có thể lưu 2 dòng $dp$ để tiết kiệm bộ nhớ (độ phức tạp $O(1)$, tất nhiên là khi không tính mảng đầu vào).

### D - Knapsack 1

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_d)

Có $N$ món hàng, mỗi món hàng $i$ có khối lượng $w[i]$ và giá trị $v[i]$. Có một cái túi có thể chứa tối đa $W$ kg. Hãy chọn một số món hàng sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị là lớn nhất.

Giới hạn:

$1 \leq N \leq 100$

$1 \leq W \leq 10^5$

$1 \leq w[i] \leq W$

$1 \leq v[i] \leq 10^9$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là tổng giá trị lớn nhất có thể đạt được sau khi chọn một số món hàng từ $1$ đến $i$ sao cho tổng khối lượng bằng $j$. Vậy ta có công thức truy hồi như sau:

    $$dp[i][j] = \max \begin{cases} dp[i-1][j] & \text{không chọn món hàng thứ } i \\ dp[i-1][j-w[i]] + v[i] & \text{chọn món hàng thứ } i \text{, và khi } j \leq w[i] \end{cases}$$

    Ban đầu ta có $dp[0][0] = 0$, $dp[0][j] = -\infty, \forall j > 0$ vì ban đầu chưa chọn món hàng nào nên không có giá trị nào cả.

    Vì ta các giá trị không hợp lệ quá nhỏ nên giá trị hợp lệ sẽ lấp đầy mảng $dp$, vì vậy ta không cần phải lo lắng về các giá trị không hợp lệ trong quá trình truy hồi.

    Cuối cùng, kết quả sẽ là $\max(dp[N][j]), \forall j, 0 \leq j \leq W$.

    Độ phức tạp thời gian của thuật toán là $O(NW)$.

    Về mặt không gian, ta có thể

    - Sử dụng mảng $dp$ để lưu kết quả (độ phức tạp $O(NW)$).
    - Sử dụng mảng $dp$ 1 chiều để lưu kết quả của i hiện tại, với công thức truy hồi $dp[j] = \max(dp[j], dp[j-w[i]] + v[i])$, với $j \geq w[i]$. Tuy nhiên vì ta cần cập nhật $dp[j]$ với $dp[j-w[i]] + v[i]$, trong đó $j-w[i] < j$, nên ta cần phải duyệt từ $W$ đến $0$ để tránh tính toán trùng lặp. Vậy độ phức tạp không gian của cách này là $O(W)$.

### E - Knapsack 2

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_e)

Có $N$ món hàng, mỗi món hàng $i$ có khối lượng $w[i]$ và giá trị $v[i]$. Có một cái túi có thể chứa tối đa $W$ kg. Hãy chọn một số món hàng sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị là lớn nhất.

Về cơ bản, bài này giống hệt bài [D - Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d), tuy nhiên với giới hạn $W$ lớn hơn nhiều nhưng $v[i]$ cũng nhỏ hơn.

Giới hạn:

$1 \leq N \leq 100$

$1 \leq W \leq 10^9$

$1 \leq w[i] \leq W$

$1 \leq v[i] \leq 10^3$

??? tip "Lời giải"
    Bạn có thể hơi rối một chút khi xem giới hạn bài toán, vì giá trị lớn nhất của $W$ là $10^9$. Tuy nhiên bạn có thể thấy giá trị lớn nhất của $v[i]$ là $10^3$, nên tổng giá trị lớn nhất có thể đạt được là $10^5$. Ta có thể sử dụng $V$ làm chiều thứ hai của mảng $dp$ giống như $W$ trong bài gốc.

    Gọi $dp[i][j]$ là khối lượng nhỏ nhất có thể đạt được với $i$ món hàng đầu tiên sao cho tổng giá trị là $j$. Ta có thể tính $dp[i][j]$ như sau:

    $$dp[i][j] = \min \begin{cases} dp[i-1][j] & \text{không chọn món hàng thứ } i \\ dp[i-1][j-v[i]] + w[i] & \text{chọn món hàng thứ } i \text{, và } j \geq v[i] \end{cases}$$

    Ban đầu ta có $dp[0][0] = 0$, $dp[0][j] = \infty, \forall j > 0$ vì ban đầu chưa chọn món hàng nào nên không có khối lượng nào cả.

    Vì các giá trị không hợp lệ quá lớn nên giá trị hợp lệ sẽ lấp đầy mảng $dp$, vì vậy ta không cần phải lo lắng về các giá trị không hợp lệ trong quá trình truy hồi.

    Kết quả sẽ là giá trị lớn nhất của $j$ sao cho $dp[N][j] \leq W$.

    Độ phức tạp thời gian của thuật toán là $O(N \sum v[i])$.

    Về mặt không gian, ta có thể

    - Sử dụng mảng $dp$ để lưu kết quả (độ phức tạp $O(N \sum v[i])$).
    - Sử dụng mảng $dp$ 1 chiều để lưu kết quả của i hiện tại, với công thức truy hồi $dp[j] = \min(dp[j], dp[j-v[i]] + w[i])$, với $j \geq v[i]$. Tuy nhiên vì ta cần cập nhật $dp[j]$ với $dp[j-v[i]] + w[i]$, trong đó $j-v[i] < j$, nên ta cần phải duyệt từ $\sum v[i]$ đến $0$ để tránh tính toán trùng lặp. Vậy độ phức tạp không gian của cách này là $O(\sum v[i])$.

### F - LCS

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_f)

Cho 2 xâu $s$ và $t$. Hãy tìm độ dài của dãy con chung dài nhất của 2 xâu.

Giới hạn:

$1 \leq |s|, |t| \leq 3000$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là độ dài của dãy con chung dài nhất của $s[1..i]$ và $t[1..j]$. Ta có thể tính $dp[i][j]$ như sau:

    $$dp[i][j] = \begin{cases} dp[i-1][j-1] + 1 & \text{nếu } s[i] = t[j] \\ \max(dp[i-1][j], dp[i][j-1]) & \text{ngược lại} \end{cases}$$

    Độ dài của dãy con chung dài nhất của $s$ và $t$ sẽ là $dp[|s|][|t|]$. Tuy nhiên ta cần phải truy vết để tìm một dãy con chung dài nhất nào đó. Ta có thể truy vết như sau:

    - Đầu tiên, ta khởi tạo 2 biến $i = |s|$ và $j = |t|$.
    - Nếu $s[i] = t[j]$, ta thêm $s[i]$ vào dãy con chung và giảm $i$ và $j$ đi $1$.
    - Nếu $dp[i-1][j] > dp[i][j-1]$, ta giảm $i$ đi $1$.
    - Ngược lại, ta giảm $j$ đi $1$.

    Nhớ đảo ngược dãy con chung để có kết quả cuối cùng.

    Độ phức tạp thời gian của thuật toán là $O(NM)$, với $n = |s|$ và $m = |t|$.

    Độ phức tạp không gian của thuật toán là $O(NM)$.

### G - Longest Path

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_g)

Cho một đồ thị có hướng không chu trình $G$ với $N$ đỉnh và $M$ cạnh. Hãy tìm độ dài của đường đi dài nhất trong đồ thị.

Giới hạn:

$2 \leq N \leq 10^5$

$1 \leq M \leq 10^5$

??? tip "Lời giải"
    Vì đồ thị $G$ không chứa chu trình, nó là một đồ thị có hướng không chu trình (directed acyclic graph - DAG), vì thế ta có thể dùng dp ở đây.

    Gọi $dp[u]$ là độ dài đường đi dài nhất bắt đầu từ đỉnh $u$. Ban đầu ta có $dp[u] = 0$ với mọi $u$.

    Ta có thể thấy rằng $dp[u] = \max(dp[v] + 1)$ với mọi $v$ mà có cạnh từ $u$ đến $v$. Tuy nhiên ta cần phải chắc chắn rằng ta đã tính $dp[v]$ trước khi tính $dp[u]$. Vì vậy ta cần phải sắp xếp topo để chắc chắn rằng trong quá trình tính toán, tất cả $dp[v]$ đã được tính trước khi tính $dp[u]$.
    Sau khi sắp xếp topo, giả sử rằng nó đang xếp $u$ trước $v$ (với tất cả các cạnh $(u, v)$), ta duyệt ngược từ cuối về đầu, với mỗi cạnh $(i, j)$ khi đang xét đỉnh $i$, ta cập nhật $dp[i] = \max(dp[i], dp[j] + 1)$.

    Cuối cùng, kết quả sẽ là $\max(dp[u])$ với mọi $u$.

    Độ phức tạp thời gian của thuật toán là $O(N+M)$.

    Độ phức tạp không gian của thuật toán là $O(N)$.

### H - Grid 1

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_h)

Cho một bảng $N \times M$ với mỗi ô được đánh dấu là có hoặc không thể đi vào. Hãy tìm số cách để đi từ ô $(1, 1)$ đến ô $(N, M)$.

Giới hạn:

$1 \leq N, M \leq 1000$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là số cách để đi từ ô $(1, 1)$ đến ô $(i, j)$. Ta có thể thấy rằng ô $(i, j)$ chỉ có thể đi từ ô $(i-1, j)$ hoặc $(i, j-1)$. Vậy ta có công thức truy hồi như sau:

    $$dp[i][j] = \begin{cases} dp[i-1][j] + dp[i][j-1] & \text{nếu } \text{grid}[i][j] = 1 \\ 0 & \text{ngược lại} \end{cases}$$

    Ban đầu ta có $dp[1][1] = 1$ vì chỉ có một cách để đi từ ô $(1, 1)$ đến ô $(1, 1)$. Với trạng thái đầu tiên là $dp[1][1]$, ta có thể đặt giá trị các ô $\text{grid}[0][j]$ và $\text{grid}[i][0]$ là 0 vì các ô này không thể đi vào, từ đó giúp tính toán dễ dàng hơn khi không phải xét nhiều điều kiện ở biên trên và bên trái.

    Cuối cùng, kết quả sẽ là $dp[N][M]$.

    Độ phức tạp thời gian của thuật toán là $O(NM)$.

    Về mặt không gian, ta có thể

    - Sử dụng mảng $dp$ để lưu kết quả (độ phức tạp $O(NM)$).
    - Ta thấy rằng $dp[i]$ chỉ phụ thuộc vào $dp[i-1]$. Vậy ta có thể lưu 2 dòng $dp$ để tiết kiệm bộ nhớ (độ phức tạp $O(M)$).

### I - Coins

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_i)

Có $N$ đồng xu ($N$ là số lẻ), mỗi đồng xu $i$ có xác suất $p[i]$ để ra mặt ngửa. Hãy tính xác suất để có số mặt ngửa nhiều hơn số mặt sấp.

Giới hạn:

$1 \leq N \leq 2999$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là xác suất để có $j$ mặt ngửa sau khi tung $i$ đồng xu. Ban đầu ta có $dp[0][0] = 1$ vì ta bắt đầu từ việc tung $0$ đồng xu và có $0$ mặt ngửa. Ta có công thức truy hồi như sau:

    $$dp[i][j] = \begin{cases} dp[i-1][j] \cdot (1 - p[i]) & \text{nếu } j = 0 \\ dp[i-1][j-1] \cdot p[i] + dp[i-1][j] \cdot (1 - p[i]) & \text{ngược lại, lần lượt khi gặp mặt ngửa và mặt sấp} \end{cases}$$

    Kết quả sẽ là tổng của $dp[N][j]$ với $j$ từ $N/2+1$ đến $N$.

    Độ phức tạp thời gian của thuật toán là $O(N^2)$.

    Về mặt không gian, ta có thể

    - Sử dụng mảng $dp$ để lưu kết quả (độ phức tạp $O(N^2)$).
    - Ta thấy rằng $dp[i]$ chỉ phụ thuộc vào $dp[i-1]$. Vậy ta có thể lưu 2 dòng $dp$ để tiết kiệm bộ nhớ (độ phức tạp $O(N)$).

### J - Sushi

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_j)

Có $N$ dĩa sushi, dĩa thứ $i$ có $a[i]$ miếng sushi. Bạn sẽ thực hiện tung xúc xắc có $N$ mặt, mỗi mặt có một số từ $1$ đến $N$. Nếu tung mặt $i$, bạn sẽ ăn một miếng sushi từ dĩa $i$, nếu dĩa $i$ không có miếng sushi nào thì không ăn gì cả. Cứ làm như vậy cho đến khi không còn miếng sushi nào. Hãy tính kỳ vọng số lần tung xúc xắc để ăn hết sushi.

Giới hạn:

$1 \leq N \leq 300$

$1 \leq a[i] \leq 3$

??? tip "Lời giải"
    Bài này cần một ít kiến thức về giá trị kỳ vọng để giải, bạn vui lòng tìm hiểu trước qua các bài dịch của mình trên blog này nhé.

    Gọi $dp[i][j][k]$ là số lần tung xúc xắc để ăn hết sushi, trong đó

    - $i$ là số dĩa sushi có $1$ miếng sushi
    - $j$ là số dĩa sushi có $2$ miếng sushi
    - $k$ là số dĩa sushi có $3$ miếng sushi

    Ta dễ dàng suy ra được $x = N - i - j - k$ là số dĩa sushi không còn miếng sushi nào.

    Ta dùng dp top-down để dễ hình dung, bắt đầu từ $dp[cnt[1]][cnt[2]][cnt[3]]$, với $cnt[i]$ là số dĩa sushi có $i$ miếng sushi.

    Trường hợp cơ bản là khi không còn miếng sushi nào, số lần tung xúc xắc sẽ là $0$. Với mỗi lần tung xúc xắc, ta có công thức truy hồi như sau:

    $$\begin{align}
    dp[i][j][k] &= \frac{x}{n} \cdot (dp[i][j][k] + 1) \text{ (nếu chọn dĩa sushi không còn miếng sushi nào)} \\
    &+ \frac{i}{n} \cdot (dp[i-1][j][k] + 1) \text{ (nếu } i > 0 \text{ và chọn dĩa sushi có } 1 \text{ miếng sushi)} \\
    &+ \frac{j}{n} \cdot (dp[i+1][j-1][k] + 1) \text{ (nếu } j > 0 \text{ và chọn dĩa sushi có } 2 \text{ miếng sushi)} \\
    &+ \frac{k}{n} \cdot (dp[i][j+1][k-1] + 1) \text{ (nếu } k > 0 \text{ và chọn dĩa sushi có } 3 \text{ miếng sushi)}
    \end{align}$$

    Chuyển vế $dp[i][j][k]$ sang trái và rút gọn phương trình, ta có

    $$dp[i][j][k] = \frac{x + i \cdot (dp[i-1][j][k] + 1) + j \cdot (dp[i+1][j-1][k] + 1) + k \cdot (dp[i][j+1][k-1] + 1)}{n - x}$$

    Độ phức tạp thời gian của thuật toán là $O(N^3)$.

    Độ phức tạp không gian của thuật toán là $O(N^3)$.

### K - Stones

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_k)

Cho tập $A = {a_1, a_2, ..., a_N} gồm $N$ số nguyên dương. Taro và Jiro sẽ chơi một trò chơi như sau. Ban đầu ta có một đống đá gồm $K$ viên đá. Người đến lượt phải chọn một phần tử trong tập $A$, giả sử là $x$, và lấy đi đúng $x$ viên đá từ đống đá. Taro chơi trước. Người nào không thể thực hiện đúng thao tác đó sẽ thua. Giả sử cả hai đều chơi một cách tối ưu, hãy xác định người chiến thắng.

Giới hạn:

$1 \leq N \leq 100$

$1 \leq K \leq 10^5$

$1 \leq a_1 < a_2 < ... < a_N \leq K$

??? tip "Lời giải"
    Gọi $dp[i]$ là kết quả của trò chơi nếu còn $i$ viên đá. Ta sẽ có $dp[i] = 1$ nếu người chơi hiện tại thắng, ngược lại thì $dp[i] = 0$. Ta có thể dùng dp top-down để dễ hình dung, bắt đầu từ $dp[K]$.

    Ở mỗi trạng thái $i$, ta có $N$ lựa chọn, nếu có ít nhất một lựa chọn dẫn đến trạng thái thua (tức là $dp[i - a[j]] = 0$), ta có thể chọn lựa chọn đó để thắng, ngược lại thì ta sẽ thua.

    Độ phức tạp thời gian của thuật toán là $O(KN)$.

    Độ phức tạp không gian của thuật toán là $O(K)$.

### L - Deque

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_l)

Taro và Jiro chơi một trò chơi như sau. Cho một dãy số $a$ gồm $N$ phần tử. Người đến lượt phải chọn một đầu của dãy số và lấy phần tử đó. Taro chơi trước. Gọi $X$ và $Y$ lần lượt là tổng số điểm của Taro và Jiro. Taro muốn tối đa hóa $X - Y$, còn Jiro muốn tối thiểu hóa $X - Y$. Hãy xác định giá trị của $X - Y$.

Giới hạn:

$1 \leq N \leq 3000$

$1 \leq a[i] \leq 10^9$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là điểm của trò chơi nếu chúng ta còn lại dãy con từ $i$ đến $j$. Ta có thể dùng dp top-down để dễ hình dung, bắt đầu từ $dp[1][n]$ vì Taro bắt đầu chơi còn cả dãy.

    Do điểm của trò chơi là $P = X - Y$, trong đó $X$ là điểm của Taro và $Y$ là điểm của Jiro, nên nếu là lượt của Taro, ta cộng phần tử đã chọn vào $P$, ngược lại, ta trừ phần tử đã chọn khỏi $P$.

    Khoan đã, làm sao ta biết với trạng thái $i, j$ hiện tại, đó là lượt của ai?

    - Ta có thể thêm một chiều nữa vào mảng $dp$ để lưu lượt chơi, 0 cho Taro, 1 cho Jiro.
    - Hoặc có một cách khác, để ý rằng nếu đến lượt Taro, tính chẵn lẻ của độ dài dãy con hiện tại sẽ bằng với tính chẵn lẻ của độ dài dãy ban đầu, nếu không bằng thì là lượt của Jiro.

    Trạng thái cơ bản là khi ta còn lại một phần tử trong dãy con, hay $i = j$, điểm của trò chơi sẽ là $a[i]$ nếu là lượt của Taro, $-a[i]$ nếu là lượt của Jiro.

    Với công thức truy hồi thì, ta biết rằng Taro muốn tối đa hóa $P$, nên ta chọn phần tử ở đầu hoặc cuối dãy con sao cho $P$ lớn nhất. Ngược lại, Jiro muốn tối thiểu hóa $P$, nên ta chọn phần tử sao cho $P$ nhỏ nhất.

    $$dp[i][j] = \begin{cases} \max(dp[i+1][j] + a[i], dp[i][j-1] + a[j]) & \text{nếu là lượt của Taro} \\ \min(dp[i+1][j] - a[i], dp[i][j-1] - a[j]) & \text{nếu là lượt của Jiro} \end{cases}$$

    Độ phức tạp thời gian của thuật toán là $O(N^2)$.

    Độ phức tạp không gian của thuật toán là $O(N^2)$.

### M - Candies

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_m)

Có $N$ học sinh và $K$ viên kẹo. Ta cần chia $K$ viên kẹo cho $N$ học sinh này sao cho mỗi học sinh nhận được từ $0$ đến $a[i]$ viên kẹo. Sau khi chia ta không còn viên kẹo nào. Hãy tính số cách chia kẹo mod $10^9 + 7$.

Giới hạn:

$1 \leq N \leq 100$

$0 \leq a[i] \leq K \leq 10^5$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là số cách chia kẹo cho $i$ học sinh sao cho tổng số kẹo là $j$. Ban đầu ta có $dp[0][0] = 1$.
    
    Ta có công thức truy hồi như sau:

    $$dp[i][j] = \sum_{x=0, j-x \geq 0}^{a[i]} dp[i-1][j-x]$$

    Nếu cài đúng như trên thì độ phức tạp sẽ là $O(NK^2)$, quá chậm. Ta có thể nhận thấy rằng $dp[i][j]$ cần tổng của $dp[i-1]$ từ $j-a[i]$ đến $j$, vậy ta có thể định nghĩa $sum[i][j]$ là tổng của $dp[i]$ từ $dp[i][0]$ đến $dp[i][j]$. Ta có thể tính $sum[i]$ cùng với $dp[i]$.

    Vậy ta có công thức truy hồi mới:

    $$dp[i][j] = \begin{cases} sum[i-1][j] - sum[i-1][j-a[i]-1] & \text{nếu } j > a[i] \\ sum[i-1][j] & \text{ngược lại} \end{cases}$$

    Độ phức tạp thời gian của thuật toán là $O(NK)$.

    Về mặt không gian, ta có thể

    - Sử dụng mảng $dp$ và $sum$ để lưu kết quả (độ phức tạp $O(NK)$).
    - Ta thấy rằng $dp[i]$ chỉ phụ thuộc vào $dp[i-1]$. Vậy ta có thể lưu 2 dòng $dp$ và $sum$ để tiết kiệm bộ nhớ (độ phức tạp $O(K)$).

### N - Slimes

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_n)

Có $N$ viên slime, viên slime thứ $i$ có kích thước $a[i]$. Ta thực hiện thao tác sau cho đến khi chỉ còn một viên slime:

- Chọn hai viên slime cạnh nhau, trộn lại với nhau để tạo ra một viên slime mới. Viên slime mới có kích thước bằng tổng kích thước của hai viên slime cũ. Thao tác này có giá trị cũng bằng tổng kích thước của hai viên slime cũ.

Hãy tính giá trị nhỏ nhất có thể đạt được khi thực hiện đến khi chỉ còn một viên slime.

Giới hạn:

$2 \leq N \leq 400$

$1 \leq a[i] \leq 10^9$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là giá trị nhỏ nhất có thể đạt được khi trộn từ viên slime $i$ đến viên slime $j$ để có một viên slime duy nhất. Kết quả sẽ là $dp[1][n]$. Ban đầu ta có $dp[i][i] = 0$ vì không cần phải làm gì cả.

    Với mỗi cặp $(i, j)$ (với $i < j$), ta có thể chia dãy thành 2 phần tại vị trí $k$ ($i \leq k < j$):

    - Ta trộn phần bên trái trước, sau đó đến phần bên phải.
    - Giá trị để trộn phần bên trái là $dp[i][k]$, phần bên phải là $dp[k+1][j]$.
    - Giá trị để trộn cả dãy là $dp[i][k] + dp[k+1][j] + \text{sum}[i][j]$ (với $\text{sum}[i][j]$ là tổng của dãy từ $i$ đến $j$).
    - Vậy ta có $dp[i][j] = \min(dp[i][j], dp[i][k] + dp[k+1][j] + \text{sum}[i][j])$ (với $i \leq k < j$).

    Độ phức tạp thời gian của thuật toán là $O(N^3)$.

    Độ phức tạp không gian của thuật toán là $O(N^2)$.

### O - Matching

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_o)

Có $N$ người đàn ông và $N$ người phụ nữ. Cho một bảng $N \times N$ với mỗi ô $(i, j)$ là $a[i][j]$. $a[i][j] = 1$ khi người đàn ông $i$ và người phụ nữ $j$ hợp nhau, ngược lại thì $a[i][j] = 0$. Hãy tính số cách ghép cặp sao cho mỗi người đều được ghép với một người khác hợp với mình.

Giới hạn:

$1 \leq N \leq 21$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là bitmask của tập những người phụ nữ đã được ghép. Kết quả sẽ là $dp[n][(1 << n) - 1]$ (nếu chúng ta đánh số từ $1$ đến $N$). Ban đầu, ta có $dp[0][0] = 1$.

    Với mỗi người đàn ông $i$ và bitmask $j$, ta cố gắng tìm một người phụ nữ k chưa được ghép và người đàn ông i hợp với cô ấy, sau đó ta cập nhật $dp[i][j | (1 << (k-1))] += dp[i-1][j]$ ($k-1$ vì chúng ta đánh số từ $1$ đến $N$). Độ phức tạp lúc này sẽ là $O(N^2 * 2^N)$, không ổn để vượt qua các test cuối.

    Để ý rằng khi xét đến người đàn ông $i$, mask $j$ phải có đúng $i-1$ bit được set, vì chúng ta đã ghép $i-1$ người đàn ông với $i-1$ người phụ nữ, vậy ta có thể bỏ qua mask $j$ có nhiều hoặc ít hơn $i-1$ bit được set. Vậy phần "với mỗi người đàn ông $i$ và bitmask $j$" có thể chạy trong $O(2^N)$.

    Độ phức tạp thời gian của thuật toán là $O(N * 2^N)$.

    Về mặt không gian, ta có thể

    - Sử dụng mảng $dp$ 2 chiều để lưu kết quả (độ phức tạp $O(N * 2^N)$).
    - Ta thấy rằng $dp[i]$ chỉ phụ thuộc vào $dp[i-1]$, vậy ta có thể lưu 2 dòng $dp$ để tiết kiệm bộ nhớ (độ phức tạp $O(2^N)$). Thậm chí, ta thấy rằng
    mỗi người đàn ông $i$ sẽ tương ứng với một số mask $j$ có đúng $i-1$ bit được set, vậy ta có thể lưu 1 dòng $dp$, vì các trạng thái của những người đàn ông khác nhau sẽ không trùng với nhau.

### P - Independent Set

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_p)

Cho một cây gồm $N$ đỉnh. Mỗi đỉnh có thể được tô màu đen hoặc trắng. Hãy tính số cách tô màu sao cho không có hai đỉnh kề nào cùng có màu đen.

Giới hạn:

$1 \leq N \leq 10^5$

??? tip "Lời giải"
    Gọi $dp[u][col]$ là số cách tô màu cho cây con của đỉnh $u$ sao cho đỉnh $u$ có màu $col$. Kết quả sẽ là $dp[1][0] + dp[1][1]$.

    Ban đầu ta có $dp[u][0] = dp[u][1] = 1$ vì ta có thể tô màu đen hoặc trắng cho mọi đỉnh.

    Với mỗi đỉnh con $v$ của đỉnh $u$, ta có thể tính $dp[v][0]$ và $dp[v][1]$ theo cách đệ quy. Sau đó, ta có công thức truy hồi như sau:

    $$\begin{align}
    dp[u][1] &= dp[u][1] \cdot dp[v][0] \text{ (nếu đỉnh } u \text{ màu đen, đỉnh } v \text{ phải màu trắng)} \\
    dp[u][0] &= dp[u][0] \cdot (dp[v][0] + dp[v][1]) \text{ (nếu đỉnh } u \text{ màu trắng, đỉnh } v \text{ có thể màu trắng hoặc đen)}
    \end{align}$$

    Độ phức tạp thời gian của thuật toán là $O(N)$.

    Độ phức tạp không gian của thuật toán là $O(N)$.

### Q - Flowers

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_q)

Có $N$ bông hoa xếp thành hàng. Bông hoa thứ $i$ có chiều cao $h[i]$ và sắc đẹp $a[i]$, $h[i]$ đôi một khác nhau. Nhổ bỏ một số bông hoa sao cho chiều cao của những bông hoa còn lại tăng dần. Hãy tính tổng sắc đẹp lớn nhất của các bông hoa còn lại.

Giới hạn:

$1 \leq N \leq 2 \times 10^5$

$1 \leq h[i] \leq N$

$1 \leq a[i] \leq 10^9$

??? tip "Lời giải"
    Gọi $dp[i]$ là tổng sắc đẹp lớn nhất của các bông hoa từ $1$ đến $i$ và bông hoa cuối cùng được giữ lại là bông hoa $i$. Kết quả sẽ là $\max(dp[1], dp[2], ..., dp[N])$.

    Ban đầu ta có $dp[0] = 0$ vì không có bông hoa nào.

    Với mỗi bông hoa $i$, ta có thể tính $dp[i]$ theo công thức truy hồi sau:

    $$dp[i] = \max(dp[j]) + a[i] \text{ với mọi } j < i \text{ và } h[j] < h[i]$$

    Tuy nhiên cách này sẽ chạy trong $O(N^2)$, quá chậm.

    Như vậy ta tối ưu bằng cách nào? Ta cần biết giá trị lớn nhất của $dp[j]$ trước đó và chiều cao của nó nhỏ hơn $h[i]$. Ta có thể sử dụng cây Fenwick (Binary Indexed Tree - BIT) để lưu giá trị $dp[j]$ tại vị trí $h[j]$ trên cây (vì $h[j]$ là duy nhất), sau đó lấy giá trị lớn nhất từ $1$ đến $h[i]-1$.

    Độ phức tạp thời gian của thuật toán là $O(N \log N)$.

    Độ phức tạp không gian của thuật toán là $O(N)$.

### R - Walk

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_r)

Cho đồ thị đơn $G$ có $N$ đỉnh. Với mỗi cặp $i, j$ ($1 \leq i, j \leq N$), giá trị $a[i][j] = 1$ nếu có cạnh nối giữa $i$ và $j$, ngược lại thì $a[i][j] = 0$. Tính số đường đi có hướng độ dài $K$ trong $G$. Đường đi có thể đi qua cùng một cạnh nhiều lần.

Giới hạn:

$1 \leq N \leq 50$

$1 \leq K \leq 10^{18}$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là số cách đi từ đỉnh $i$ đến đỉnh $j$ trong $i$ bước. Kết quả sẽ là tổng của $dp[k][j]$ với $j$ từ $1$ đến $N$.

    Ban đầu ta có $dp[0][i] = 1$ với mọi $i$.

    Ta có công thức truy hồi như sau:

    $$\begin{align}
    dp[i][j] &= \sum_{k=1, a[k][j] = 1}^{N} dp[i-1][k] \\
    &= \sum_{k=1}^{N} dp[i-1][k] \cdot a[k][j]
    \end{align}$$

    Cách này sẽ chạy trong $O(KN^2)$, quá chậm.

    Để ý rằng ta có thể đi từ $dp[i-1]$ đến $dp[i]$ bằng một ma trận, vậy ta có thể áp dụng nhân ma trận để tối ưu. Ma trận $A$ sẽ là ma trận dạng $A[i][j] = a[j][i]$.

    Vậy ta có $dp[k] = A^k \cdot dp[0]$.

    Độ phức tạp thời gian của thuật toán là $O(N^3 \log K)$.

    Độ phức tạp không gian của thuật toán là $O(N^2)$.

### S - Digit Sum

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_s)

Tìm số các số nằm trong khoảng $[1, K]$ sao cho tổng chữ số của số đó chia hết cho $D$.

Giới hạn:

$1 \leq K \leq 10^{10000}$

$1 \leq D \leq 100$

??? tip "Lời giải"
    Giờ ta đến với một biến thể của DP, cụ thể ở đây là Digit DP hay DP chữ số. Ta cần tính số lượng số nguyên nằm trong khoảng từ 0 đến một số nào đó ($K$ chẳng han) và các số đó có một số tính chất nhất định. Thông thường, ta cần xây dựng số từ trái sang phải, và xem xét xem số đó có nhỏ hơn $n$ hay không. Ta cần biết điều đó để biết chữ số tiếp theo có thể nằm trong khoảng nào.

    Gọi $dp[i][j][eq]$ là số cách xây dựng một số có độ dài $i$, tổng chữ số chia dư cho $d$ được $j$, và số đó nhỏ hơn $K$ nếu $eq = 0$, ngược lại $eq = 1$ khi số đó đang có thể bằng $K$. Ban đầu, ta chưa có chữ số nào, tổng chữ số chia dư cho $d$ là $0$, và số đó vẫn có thể bằng $K$, nên $dp[0][0][1] = 1$.

    Công thức truy hồi khá đơn giản, ta lặp qua chữ số tiếp theo, cập nhật tổng chữ số chia dư cho $d$, và xem xét xem số đó có nhỏ hơn $K$ hay không.

    Kết quả sẽ là $dp[N][0][0] + dp[N][0][1] - 1$, vì ta cần loại bỏ số $0$, với $N$ là số chữ số của $K$.

    Độ phức tạp thời gian của thuật toán là $O(ND)$.

    Độ phức tạp không gian của thuật toán là $O(ND)$, bạn có thể tối ưu nó xuống $O(d)$ bằng cách sử dụng 2 dòng.

### T - Permutation

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_t)

Cho số nguyên dương $N$ và một xâu độ dài $N-1$ gồm các ký tự `>` và `<`. Tìm số hoán vị $p_1, p_2, ..., p_N$ sao cho thỏa mãn điều kiện $p_i < p_{i+1}$ nếu ký tự thứ $i$ trong xâu là `<` và $p_i > p_{i+1}$ nếu ký tự thứ $i$ trong xâu là `<`.

Giới hạn:

$2 \leq N \leq 3000$

??? tip "Lời giải"
    Gọi $dp[i][j]$ là số hoán vị có $i$ ô đã được điền, ta còn $n-i$ phần tử còn lại, trong đó $j$ phần tử lớn hơn phần tử cuối cùng ta đã điền. Ban đầu ta điền ô đầu tiên trước, có $N$ cách chọn, và ta có thể chọn bất kỳ phần tử nào để là phần tử đầu tiên. Nếu chúng ta chọn số $j$, có $N-j$ phần tử lớn hơn $j$, vậy $dp[1][N-j] = 1$.

    Sau đó, ta tiếp tục điền vào ô tiếp theo với mỗi trạng thái có ít nhất một cách chọn (mod $10^9+7$):

    - Nếu ký tự là `<`, ta cần thêm $dp[i][j]$ vào $dp[i+1][0]$, $dp[i+1][1]$, ..., $dp[i+1][j-1]$, vì ta cần chọn một phần tử lớn hơn phần tử cuối cùng hiện tại nên $j$ bị giảm đi.
    - Nếu ký tự là `>`, ta cần thêm $dp[i][j]$ vào $dp[i+1][j]$, $dp[i+1][j+1]$, ..., $dp[i+1][n-i-1]$, vì ta cần chọn một phần tử nhỏ hơn phần tử cuối cùng hiện tại nên $j$ được giữ nguyên hoặc tăng lên.
    - Cách này nếu cài lên sẽ chạy trong $O(N^3)$, nhưng ta thấy rằng ta cộng một đoạn cụ thể, vậy ta có thể sử dụng prefix sum để tối ưu nó xuống $O(N^2)$.

    Kết quả cuối cùng sẽ là $dp[N][0]$.

    Độ phức tạp thời gian của thuật toán là $O(N^2)$.

    Độ phức tạp không gian của thuật toán là $O(N^2)$, hoặc $O(N)$ nếu ta sử dụng 2 dòng.

### U - Grouping

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_u)

Cho $N$ con thỏ. Với mỗi cặp thỏ $i, j$, ta có $a[i][j]$ là mức độ tương hợp giữa chúng. Ta cần chia $N$ con thỏ thành các nhóm sao cho mỗi con thỏ thuộc về đúng một nhóm. Nếu hai con thỏ $i, j$ thuộc cùng nhóm thì bạn sẽ được $a[i][j]$ điểm. Hãy tính tổng điểm lớn nhất có thể đạt được.

Giới hạn:

$1 \leq N \leq 16$

$|a[i][j]| \leq 10^9$

$a[i][i] = 0$

$a[i][j] = a[j][i]$

??? tip "Lời giải"
    Gọi $sum[\text{mask}]$ là điểm của nhóm thỏ được biểu diễn bởi $\text{mask}$. Ta sẽ mất $O(2^N \cdot N^2)$ để tính toán cái này.

    Sau đó, ta định nghĩa $dp[\text{mask}]$ là điểm lớn nhất của các nhóm thỏ có thể được tạo ra bởi $\text{mask}$. Ta có thể tính như sau trong $O(3^N)$:

    $$dp[\text{mask}] = \max(dp[\text{mask}], dp[\text{mask} \oplus \text{subMask}] + \text{sum}[\text{subMask}]) \text{ với mọi mask con của mask}$$

    Cuối cùng, kết quả sẽ là $dp[2^N - 1]$.

    Độ phức tạp thời gian của thuật toán là $O(3^N + 2^N \cdot N^2)$.

    Độ phức tạp không gian của thuật toán là $O(2^N)$.

### V - Subtree

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_v)

Cho một cây $N$ đỉnh. Ta tô màu trắng hoặc đen cho các đỉnh sao cho một đỉnh đen chỉ có thể đến được một đỉnh đen khác bằng cách đi qua một số đỉnh đen khác nữa. Tìm số cách tô mod $M$.

Giới hạn:

$1 \leq N \leq 10^5$

$1 \leq M \leq 10^9$

??? tip "Lời giải"
    Giả sử gốc của cây nằm ở node $1$.

    Gọi $res[u]$ là số cách tô màu cho toàn bộ cây, trong đó có một thành phần liên thông chứa $u$ là có màu đen.

    Gọi $subtree[u]$ là số cách tô màu cho cây con gốc $u$, trong đó có một thành phần liên thông chứa $u$ là có màu đen.

    $$subtree[u] = \prod_{v \in \text{con của } u} (subtree[v] + 1)$$

    Rõ ràng ban đầu $res[1] = subtree[1]$.

    Với $res[v]$, gọi $u$ là cha của $v$, ta có:

    $$res[v] = subtree[v] \cdot \left( \frac{res[u]}{subtree[v] + 1} + 1 \right)$$

    Nếu $M$ là số nguyên tố kiểu $10^9 + 7$, ta có thể sử dụng định lý Fermat nhỏ để tính nghịch đảo của $(subtree[v] + 1)$ modulo $M$, nhưng vì $M$ có thể là bất kỳ số nguyên dương nào, ta cần tìm cách để lấy $res[u] / subtree[v]$ modulo $M$ mà không cần phải chia.

    Gọi $parTree[u]$ là số cách tô màu cho cả cây mà không có cây con gốc $u$, trong đó có một thành phần liên thông chứa cha của $u$ là có màu đen. Với $v, v_1, v_2, \ldots, v_k$ là các con của $u$, ta có:

    $$res[u] = (subtree[v] + 1) \cdot (subtree[v_1] + 1) \cdot (subtree[v_2] + 1) \cdot \ldots \cdot (subtree[v_k] + 1) \cdot (parTree[u] + 1)$$

    $$\begin{align}
    parTree[v] &= \frac{(parTree[u] + 1) \cdot (subtree[v_1] + 1) \cdot (subtree[v_2] + 1) \cdot \ldots \cdot (subtree[v_k] + 1)}{subtree[v] + 1} \\
    &= (parTree[u] + 1) \cdot (subtree[v_1] + 1) \cdot (subtree[v_2] + 1) \cdot \ldots \cdot (subtree[v_k] + 1) \\
    \end{align}$$

    Gọi $subtreeOfParWithout[v]$ là $(subtree[v_1] + 1) \cdot (subtree[v_2] + 1) \cdot \ldots \cdot (subtree[v_k] + 1)$.

    Vậy $parTree[v] = (parTree[u] + 1) \cdot subtreeOfParWithout[v]$.

    Và $res[v] = subtree[v] \cdot (parTree[v] + 1)$.

    Độ phức tạp thời gian của thuật toán là $O(N)$.

    Độ phức tạp không gian của thuật toán là $O(N)$.

### W - Intervals

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_w)

Xét một xâu độ dài $N$ gồm các ký tự `0` và `1`. Điểm của xâu này sẽ được tính như sau:

- Với mỗi $i$, $a[i]$ được cộng vào tổng điểm nếu xâu con từ $l[i]$ đến $r[i]$ chứa ít nhất một ký tự `1`.

Hãy tính tổng điểm lớn nhất có thể đạt được.

Giới hạn:

$1 \leq N, M \leq 2 \times 10^5$

$1 \leq l[i], r[i] \leq N$

$|a[i]| \leq 10^9$

??? tip "Lời giải"
    Gọi $dp[i]$ là tổng điểm lớn nhất có thể đạt được cho xâu con từ $1$ đến $i$ và bit $i$ được set (đánh số từ $1$).

    Ta có $dp[i] = \max(dp[j] + \text{cost}(i, j))$ với $j < i$, và $\text{cost}(i, j)$ là tổng điểm của tất cả các đoạn $x$ với $i$ nằm trong $[l_x, r_x]$ và $j$ không nằm trong $[l_x, r_x]$. Kết quả sẽ là $\max(0, \max(dp[i]))$. Cái này sẽ chạy trong $O(N^2)$, quá chậm.

    Xét một biến đổi từ $\text{cost}(i-1, j)$ sang $\text{cost}(i, j)$ khi ta di chuyển từ $i-1$ sang $i$:

    - Khi ta có một đoạn mà $l_x = i$, $\text{cost}$ sẽ tăng thêm $a_x$.
    - Khi ta có một đoạn mà $r_x = i-1$, $\text{cost}$ sẽ giảm đi $a_x$.

    Vậy ta có thể sử dụng một mảng $p$, ở mỗi bước $i$ và $j < i$, $p[j] = \text{cost}(i, j) + dp[j]$. Khi ta di chuyển đến $i$ mới, ta sẽ tăng $p[j]$ thêm $a_x$ nếu có đoạn bắt đầu từ $i$, và giảm $p[j]$ đi $a_x$ nếu có đoạn kết thúc tại $i-1$.

    Ta có thể sử dụng segment tree để duy trì p[j] với mọi j < i, sau đó cập nhật $p[i] = \max(p[0], p[1], \ldots, p[i-1])$ (không có \text{cost} ở đây vì $\text{cost}(i, i) = 0$).

    $p[i]$ ở mỗi bước $i$ cũng chính là $dp[i]$, ta cập nhật kết quả tương ứng.

    Độ phức tạp thời gian của thuật toán là $O(N \log N)$.

    Độ phức tạp không gian của thuật toán là $O(N)$.

### X - Tower

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_x)

Có $N$ phiến đá. Phiến đá thứ $i$ nặng $w[i]$, có độ vững chắc $s[i]$, và giá trị $v[i]$. Ta cần xây một cái tháp với một số phiến đá trong này và xếp chồng chúng lên nhau, sao cho với mỗi phiến đá trong tháp, tổng khối lượng các phiến đá nằm trên nó không vượt quá độ vững chắc của nó. Hãy tính giá trị lớn nhất có thể đạt được của tháp.

Giới hạn:

$1 \leq N \leq 10^3$

$1 \leq w[i], s[i] \leq 10^4$

$1 \leq v[i] \leq 10^9$

??? tip "Lời giải"
    Ta cần các khối đá phải được sắp xếp theo thứ tự nào đó để ta có thể thực hiện DP, nhưng thứ tự nào? Hóa ra nó sẽ là thứ tự $w + s$ tăng dần.

    - Xét thứ tự của hai khối đá $a$ và $b$.
    - Nếu khối đá $a$ nằm dưới khối đá $b$, thì độ vững chắc của tháp là $s[a] - w[b]$ cho các khối đá khác được đặt lên trên khối đá $a$.
    - Nếu khối đá $b$ nằm dưới khối đá $a$, thì độ vững chắc của tháp là $s[b] - w[a]$ cho các khối đá khác được đặt lên trên khối đá $b$.
    - Để có đặt được nhiều khối lượng hơn ở trên khối đá nằm dưới, giá trị nào lớn hơn thì sẽ được chọn. Nghĩa là, nếu ta muốn $a$ nằm dưới (nghĩa là xếp sau theo thứ tự), ta sẽ muốn $s[a] - w[b] \geq s[b] - w[a] \Rightarrow s[a] + w[a] \geq s[b] + w[b]$. Vậy tổng nhỏ hơn sẽ được sắp xếp trước.

    Sau khi sắp xếp, gọi $dp[i][j]$ là giá trị lớn nhất của tháp khi xét $i$ khối đá đầu tiên và độ vững chắc của tháp là $j$. Ta biết rằng khối lượng lớn nhất của tháp là gấp đôi $w_{\text{max}}$.

    Ban đầu, $dp[0][0] = 0$.

    Với mỗi khối đá, ta có thể đặt nó lên tháp hoặc không (nghĩa là đặt dưới cùng đấy). Nếu đặt nó lên tháp, ta cần kiểm tra xem khối đá đó có chịu được cái tháp hiện tại không.

    $$dp[i][j + w[i]] = \max(dp[i][j + w[i]], dp[i - 1][j] + v[i]), \forall j \leq s[i]$$

    Cuối cùng, kết quả sẽ là $\max(dp[n][j])$ với mọi $j$.

    Độ phức tạp thời gian của thuật toán là $O(n \cdot \max(w))$.

    Độ phức tạp không gian của thuật toán là $O(\max(w))$ nếu ta chỉ lưu một hàng của $dp$, $dp[j]$.


### Y - Grid 2

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_y)

Cho một bảng $H \times W$. Có $N$ ô là tường và bạn không đi vào được. Các ô $(1, 1)$ và $(H, W)$ là ô xuất phát và kết thúc, đều là ô trống. Ta bắt đầu từ ô $(1, 1)$ và cần đi đến ô $(H, W)$, mỗi bước chỉ có thể đi sang phải hoặc xuống dưới. Hãy tính số cách đi.

Giới hạn:

$1 \leq H, W \leq 10^5$

$1 \leq N \leq 3000$

??? tip "Lời giải"
    Số cách đi từ ô $(x, y)$ đến ô $(u, v)$ là $\binom{u-x+v-y}{u-x}$ (với $x \leq u, y \leq v$ và không có chướng ngại vật trên đường đi, chỉ được di chuyển sang phải hoặc xuống dưới trong bảng).

    Gọi $dp[i]$ là số cách đi từ ô $(1, 1)$ đến ô $(x[i], y[i])$ mà không đi qua chướng ngại vật nào (nghĩa là không qua ô chướng ngại nào khác ngoài ô thứ $i$).

    Số cách đi từ ô $(1, 1)$ đến ô $(x[i], y[i])$ là $\binom{x[i]+y[i]-2}{x[i]-1}$, nhưng ta cần loại bỏ đường đi từ $(1, 1)$ đến chướng ngại vật bên trong hình chữ nhật $(1, 1, x[i], y[i])$, đó là $dp[j] \cdot \binom{x[i]-x[j]+y[i]-y[j]}{x[i]-x[j]}$ với mọi $j$ sao cho $x[j] \leq x[i]$ và $y[j] \leq y[i]$. Ta có thể sắp xếp các ô ban đầu theo $x[i]$ để các ô như vậy đến trước ô thứ $i$.

    Thêm ô $(H, W)$ vào cuối mảng và bắt đầu tính DP, kết quả sẽ là phần tử cuối cùng của mảng $dp$.

    Độ phức tạp thời gian của thuật toán là $O(\max(n^2, H+W))$.

    Độ phức tạp không gian của thuật toán là $O(\max(n, H+W))$.

### Z - Frog 3

[Link đề bài](https://atcoder.jp/contests/dp/tasks/dp_z)

Có $N$ viên đá, mỗi viên đá $i$ có chiều cao $h[i]$, dãy $h$ tăng dần. Có một con ếch ở viên đá $1$ và muốn nhảy đến viên đá $N$. Từ viên đá $i$, con ếch có thể nhảy đến viên đá $i+1, i+2, ..., N$ với chi phí là $(h[j] - h[i])^2 + C$, với $j$ là viên đá mà con ếch nhảy đến. Hãy tính chi phí nhỏ nhất để con ếch nhảy đến viên đá $N$.

Giới hạn:

$2 \leq N \leq 2 \times 10^5$

$1 \leq C \leq 10^{12}$

$1 \leq h[1] < h[2] < \cdots < h[N] \leq 10^6$

??? tip "Lời giải"
    Gọi $dp[i]$ là chi phí nhỏ nhất để nhảy đến viên đá $i$. Ban đầu, $dp[1] = 0$.

    $$\begin{align}
    dp[i] &= \min(dp[j] + C + (h[i] - h[j])^2), \forall j < i \\
    &= \min(dp[j] + C + h[i]^2 - 2 \cdot h[i] \cdot h[j] + h[j]^2), \forall j < i \\
    &= C + h[i]^2 + \min(dp[j] - 2 \cdot h[j] \cdot h[i] + h[j]^2), \forall j < i
    \end{align}$$

    $dp[j] - 2 \cdot h[j] \cdot h[i] + h[j]^2$ có thể viết lại dưới dạng $(-2 \cdot h[j]) \cdot x + (dp[j] + h[j]^2)$ với $x = h[i]$, tạo thành một đường thẳng $y = mx + b$, $m$ cũng được sắp xếp theo thứ tự giảm dần, vậy ta có thể sử dụng Convex Hull Trick để giải bài toán này, bạn có thể tìm hiểu kỹ thuật này [tại đây](https://codeforces.com/blog/entry/63823).

    Khi $x = h[i]$, vì $x$ tăng dần, đường thẳng ta cần sẽ có xu hướng nằm sau trong danh sách đường thẳng của bao lồi, vậy ta chỉ cần duy trì một con trỏ và di chuyển nó về phía trước cho đến khi đường thẳng tiếp theo không cho ra kết quả tốt hơn đường thẳng hiện tại.

    Độ phức tạp thời gian của thuật toán là $O(N)$.

    Độ phức tạp không gian của thuật toán là $O(N)$.

## Cài đặt

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [A - Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55344258) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-A.cpp) | 07/07/2024 |
| [B - Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55351301) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-B.cpp) | 07/07/2024 |
| [C - Vacation](https://atcoder.jp/contests/dp/tasks/dp_c) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55352036) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-C.cpp) | 07/07/2024 |
| [D - Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55829773) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-D.cpp) | 20/07/2024 |
| [E - Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55829979) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-E.cpp) | 20/07/2024 |
| [F - LCS](https://atcoder.jp/contests/dp/tasks/dp_f) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55829904) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-F.cpp) | 20/07/2024 |
| [G - Longest Path](https://atcoder.jp/contests/dp/tasks/dp_g) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55890151) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-G.cpp) | 22/07/2024 |
| [H - Grid 1](https://atcoder.jp/contests/dp/tasks/dp_h) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55890231) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-H.cpp) | 23/07/2024 |
| [I - Coins](https://atcoder.jp/contests/dp/tasks/dp_i) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55890266) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-I.cpp) | 23/07/2024 |
| [J - Sushi](https://atcoder.jp/contests/dp/tasks/dp_j) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55915567) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-J.cpp) | 23/07/2024 |
| [K - Stones](https://atcoder.jp/contests/dp/tasks/dp_k) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55915506) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-K.cpp) | 23/07/2024 |
| [L - Deque](https://atcoder.jp/contests/dp/tasks/dp_l) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55915619) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-L.cpp) | 23/07/2024 |
| [M - Candies](https://atcoder.jp/contests/dp/tasks/dp_m) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55937618) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-M.cpp) | 24/07/2024 |
| [N - Slimes](https://atcoder.jp/contests/dp/tasks/dp_n) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55937636) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-N.cpp) | 24/07/2024 |
| [O - Matching](https://atcoder.jp/contests/dp/tasks/dp_o) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55960386) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-O.cpp) | 24/07/2024 |
| [P - Independent Set](https://atcoder.jp/contests/dp/tasks/dp_p) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55961069) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-P.cpp) | 25/07/2024 |
| [Q - Flowers](https://atcoder.jp/contests/dp/tasks/dp_q) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55961153) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-Q.cpp) | 25/07/2024 |
| [R - Walk](https://atcoder.jp/contests/dp/tasks/dp_r) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55961200) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-R.cpp) | 25/07/2024 |
| [S - Digit Sum](https://atcoder.jp/contests/dp/tasks/dp_s) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55983470) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-S.cpp) | 26/07/2024 |
| [T - Permutation](https://atcoder.jp/contests/dp/tasks/dp_t) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55983587) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-T.cpp) | 26/07/2024 |
| [U - Grouping](https://atcoder.jp/contests/dp/tasks/dp_u) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/55983771) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-U.cpp) | 26/07/2024 |
| [V - Subtree](https://atcoder.jp/contests/dp/tasks/dp_v) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/56067485) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-V.cpp) | 27/07/2024 |
| [W - Intervals](https://atcoder.jp/contests/dp/tasks/dp_w) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/56068649) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-W.cpp) | 27/07/2024 |
| [X - Tower](https://atcoder.jp/contests/dp/tasks/dp_x) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/56068829) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-X.cpp) | 27/07/2024 |
| [Y - Grid 2](https://atcoder.jp/contests/dp/tasks/dp_y) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/56071266) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-Y.cpp) | 27/07/2024 |
| [Z - Frog 3](https://atcoder.jp/contests/dp/tasks/dp_z) | :white_check_mark: | [Submission](https://atcoder.jp/contests/dp/submissions/56073023) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder-DP-Z.cpp) | 27/07/2024 |
