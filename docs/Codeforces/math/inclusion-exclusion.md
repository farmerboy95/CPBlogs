# Nguyên tắc Bao hàm - Loại trừ

## Nguồn

<img src="../../../assets/images/codeforces.png" width="16" height="16"/> [[Tutorial] Inclusion-Exclusion Principle](https://codeforces.com/blog/entry/64625)

## Nhắc lại các ký hiệu về tập hợp

- $\cap$ là giao của hai tập hợp.
- $\cup$ là hợp của hai tập hợp.
- $\setminus$ là hiệu của hai tập hợp.
- $\emptyset$ là tập hợp rỗng.
- $\mathbb{N}$ là tập hợp các số tự nhiên.
- $\mathbb{Z}$ là tập hợp các số nguyên.
- $\mathbb{Q}$ là tập hợp các số hữu tỉ.
- $\mathbb{R}$ là tập hợp các số thực.
- $\mathbb{C}$ là tập hợp các số phức.
- $|X|$ là kích thước của tập hợp $X$.
- $\in$ là ký hiệu cho phần tử thuộc tập hợp.
- $\subset$ là ký hiệu cho tập hợp con.
- $\subseteq$ là ký hiệu cho tập hợp con hoặc bằng.
- $\supset$ là ký hiệu cho tập hợp chứa.
- $\supseteq$ là ký hiệu cho tập hợp chứa hoặc bằng.

## Các định nghĩa

Cho tập hữu hạn $X$ và ba tập con $A$, $B$, $C$. Để có được $|A \cup B \cup C|$, ta lấy tổng $|A| + |B| + |C|$. Trừ khi $A$, $B$, $C$ đôi một không có phần tử chung, ta sẽ đếm bị thừa, vì các phần tử của $A \cap B$, $A \cap C$, $B \cap C$ được đếm hai lần. Vậy nên ta trừ $|A \cap B| + |A \cap C| + |B \cap C|$. Giờ kết quả lại bị thiếu các phần tử trong $A \cap B \cap C$, do nó được thêm 3 lần, nhưng cũng bị trừ đi 3 lần. Vậy kết quả là:

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

hay tương đương với

$$|X \setminus (A \cup B \cup C) = |X| - |A| - |B| - |C| + |A \cap B| + |A \cap C| + |B \cap C| - |A \cap B \cap C|$$

Công thức sau đây sẽ giải quyết trường hợp có nhiều tập hợp hơn.

### Nguyên tắc Bao hàm - Loại trừ hạn chế (The Restricted Inclusion-Exclusion Principle)

Cho $A_1, A_2, \dots, A_n$ là các tập con của $X$. Ta có:

$$|X \setminus \bigcup_{i=1}^n A_i| = |X| - \sum_{i=1}^n |A_i| + \sum_{1 \leq i < j \leq n} |A_i \cap A_j| - \sum_{1 \leq i < j < k \leq n} |A_i \cap A_j \cap A_k| + \dots + (-1)^n |A_1 \cap A_2 \cap \dots \cap A_n|$$

Đây là công thức rất quen thuộc với nhiều bạn, mình sẽ gọi nó là Nguyên tắc Bao hàm - Loại trừ hạn chế (The Restricted Inclusion-Exclusion Principle). Nó có thể chuyển bài toán tính kích thước hợp của các tập hợp thành bài toán tính kích thước giao của các tập hợp.

Không khó để chứng minh tính đúng đắn của công thức này, ta chỉ cần kiểm tra xem một phần tử $x \in X$ được đếm bao nhiêu lần trong cả hai vế. Nếu $x \notin \bigcup_{i=1}^n A_i$ thì nó được đếm một lần trong cả hai vế. Ngược lại, nếu $x \in \bigcup_{i=1}^n A_i$, hay chính xác hơn là $x$ nằm trong $m$ tập hợp trong các tập $A_1, A_2, \dots, A_n$, vế trái nó sẽ không xuất hiện, còn vế phải thì số lần xuất hiện là:

$$1 - \binom{m}{1} + \binom{m}{2} - \binom{m}{3} + \dots + (-1)^m \binom{m}{m} = 0$$

với mọi $m \le 1$, nên dấu bằng xảy ra.

#### Ví dụ 1

Đây là bài [Co-prime](https://acm.hdu.edu.cn/showproblem.php?pid=4135) trên HDU Online Judge. Đây là một bài rất nổi tiếng sử dụng Nguyên tắc Bao hàm - Loại trừ.

Cho $N$, $L$, $R$, bạn cần tính số số nguyên $x$ trong đoạn $[L, R]$ sao cho $x$ nguyên tố cùng nhau với $N$, hay nói cách khác là $\gcd(x, N) = 1$. Có $1 \le T \le 100$ test. Giới hạn là $1 \le N \le 10^9$, $1 \le L \le R \le 10^{15}$.

??? tip "Lời giải"
    Nếu ta có thể tính số số nguyên $x$ trong đoạn $[1, X]$ mà $x$ nguyên tố cùng nhau vơi $N$, ký hiệu là $f(X)$, thì đáp án cuối cùng sẽ là $f(R) - f(L-1)$. Vậy tính $f(X)$ kiểu gì?

    Thay vì đếm số số nguyên tố cùng nhau với $N$, ta có thể đếm số số không nguyên tố cùng nhau với $N$, nghĩa là các số có chung ít nhất một thừa số nguyên tố với $N$. Để làm được điều này, đầu tiên ta có thể sàng tất cả các số nguyên tố không vượt quá $O(\sqrt N)$, sau đó tìm tất cả các thừa số nguyên tố $p_1, p_2, \dots, p_k$ của $N$. Gọi $A_i$ là tập các số chia hết cho $p_i$, thì số số không nguyên tố cùng nhau với $N$ trong đoạn $[1, X]$ sẽ là $|\bigcup_{i=1}^n A_i|$, cái này khá khó để tính trực tiếp. Tuy nhiên, nếu sử dụng Nguyên tắc Bao hàm - Loại trừ, ta có thể chuyển bài toán này thành bài toán tính kích thước giao của các tập hợp $A_i$, sẽ dễ hơn.
    
    Độ phức tạp sẽ là $O(\sqrt N + T \cdot 2^k)$, với $k < 10$ là số thừa số nguyên tố khác nhau của $N$.

Diễn giải chuẩn sẽ đưa ta đến với Nguyên tắc Bao hàm - Loại trừ. Giả sử ta có một tập $X$, gọi là *universe* đi, và một tập $E = \{e_1, e_2, \dots, e_n\}$ các **tính chất** (properties) mà các phần tử của $X$ có thể có hoặc không. Ta có thể định nghĩa bất kỳ tính chất nào mà ta muốn, như là $e = ''\le 5''$, $e = ''\text{là một số nguyên}''$, hay thậm chí $e = ''\text{thích ăn táo}''$ chẳng hạn. Gọi $A_i$ là tập con của các phần tử của X có tính chất $e_i$ (và các phần tử đó có thể có một số tính chất khác, nhưng vẫn có chung tính chất $e_i$). Vậy thì $|X \setminus \bigcup_{i=1}^n A_i|$ là số phần tử trong X **không có** tính chất nào trong $E$. Rõ ràng, $A_{i_1}, A_{i_2}, \dots, A_{i_t}$ là lần lượt là các tập con các phần tử của X có chung tính chất lần lượt là $e_{i_1}, e_{i_2}, \dots, e_{i_t}$ (mỗi phần tử trong một tập có thể có các tính chất khác, nhưng tất cả chúng trong một tập đều phải có chung tính chất được chỉ định). Với các kí hiệu

$$N_{\supseteq T} := \#\{x \in X : \text{T là tập con của tập các tính chất của x}\}$$

(tức là đếm số phần tử $x$ của $X$ sao cho tập các tính chất mà $x$ đang có sẽ là tập chứa tập các tính chất T cho trước) và

$$N_{=T} := \#\{x \in X : \text{T chính là tập các tính chất của x}\}$$

(tức là đếm số phần tử $x$ của $X$ sao cho tập các tính chất mà $x$ đang có sẽ bằng tập các tính chất T cho trước), ta đến với Nguyên tắc Bao hàm - Loại trừ.

### Nguyên tắc Bao hàm - Loại trừ (The Inclusion-Exclusion Principle)

Cho tập $X$, và tập $E = \{e_1, e_2, \dots, e_n\}$ là tập các tính chất. Ta có

$$N_{= \emptyset} = \sum_{T \subseteq E} (-1)^{|T|} N_{\supseteq T} = \sum_{k=0}^n (-1)^k \sum_{T:|T|=k} N_{\supseteq T}$$

Công thức này còn trở nên đơn giản hơn trong trường hợp $N_{\supseteq T}$ chỉ phụ thuộc vào kích thước $|T| = k$. Từ đây ta có thể viết $N_{\supseteq T} = N_{\le k}$ với $|T| = k$, và gọi $E$ là một tập *đồng nhất* các tính chất, và trong trường hợp này $N_{= T} = N_{= k}$ cũng chỉ phụ thuộc vào kích thước của $T$. Vậy với các tính chất đồng nhất, ta có

$$N_{= \emptyset} = N_{= 0} = \sum_{k=0}^n (-1)^k \binom{n}{k} N_{\ge k}$$

Đây là bản chất của Nguyên tắc Bao hàm - Loại trừ. Hãy cố gắng hiểu tất cả các ký hiệu trước khi đọc tiếp. Từ đây ta có thể thấy rằng, khi cho $e_i = \{i \in A_i\}$, ta sẽ có Nguyên tắc Bao hàm - Loại trừ hạn chế.

#### Ví dụ 2

Đây là bài [Character Encoding](http://acm.hdu.edu.cn/showproblem.php?pid=6397) trên HDU Online Judge.

Bài này yêu cầu bạn tính số nghiệm nguyên của phương trình $x_1 + x_2 + \dots + x_n = k$ thoả mãn $0 \le x_i < m$, lấy dư với $998244353$.

Giới hạn: $1 \le n, m \le 10^5$, $0 \le k \le 10^5$, $0 \le \sum n, \sum m, \sum k \le 5 \times 10^6$.

Lưu ý rằng nếu bạn thực sự submit bài này thì để ý là vai trò của $n$ và $m$ sẽ đổi chỗ cho nhau nhé.

??? tip "Gợi ý"
    Số nghiệm nguyên không âm của $x_1 + x_2 + \dots + x_n = k$ là $\binom{n+k-1}{k} = \binom{n+k-1}{n-1}$.

    Làm sao để tính được? Ta có thể tưởng tượng rằng ta trải $k$ viên bi trên một đường thẳng, và ta muốn chia $k$ viên bi này thành $n$ phần, mỗi phần có thể có hoặc không có viên bi nào, mỗi phần gồm các viên bi liên tiếp nhau. Như vậy ta cần có $n-1$ vách ngăn để chia $k$ viên bi thành $n$ phần. Số phần tử trên đường thẳng ta có tất cả là $k + n - 1$, trong đó $k$ viên bi và $n-1$ vách ngăn. Vì mỗi phần có thể có hoặc không có viên bi nào, ta có thể tự do chọn $n-1$ chỗ trong $k+n-1$ chỗ để đặt vách ngăn (các viên bi sẽ được tự dộng đặt vào phần còn lại). Vậy kết quả là $\binom{n+k-1}{n-1}$, cũng bằng với $\binom{n+k-1}{k}$.

??? tip "Lời giải"
    Ta thấy rằng nếu không có điều kiện $x < m$, việc tính số nghiệm sẽ rất dễ dàng, cho nên ta sẽ thử tìm cách bỏ đi được cái điều kiện này. Ta áp dụng Nguyên tắc Bao hàm - Loại trừ ở đây.

    Ta định nghĩa tính chất $e_i  = ''x_i \ge m''$, ta thấy $N_{= \emptyset}$ sẽ là kết quả ta cần. Rõ ràng là tập các tính chất này đồng nhất. Gọi $T = \{1,2, \dots, j\} (j \le n)$, ta có $N_{\supseteq T}$ sẽ là số nghiệm $x_1 \ge m, x_2 \ge m, \dots, x_j \ge m$. Đặt $y_i = x_i - m$ khi $i \le j$, $y_i = x_i$ khi $i > j$ và bài toán trở thành số nghiệm của

    $$y_1 + y_2 + \dots + y_n = k - j \cdot m$$

    Giờ nó không phụ thuộc vào điều kiện nữa, nên ta có thể áp dụng gợi ý ở trên để có được số nghiệm là

    $$N_{= \emptyset} = N_{= 0} = \sum_{j=0}^{n} (-1)^j \binom{n}{j} \binom{n+k-jm-1}{n-1}$$

    Độ phức tạp sẽ là $O(n)$, vì cần phải tính trước các giai thừa và modulo nghịch đảo của chúng.

#### Ví dụ 3

Đây là bài [K-Inversion Permutations](https://www.hackerrank.com/contests/101hack43/challenges/k-inversion-permutations/problem) trên HackerRank.

Cho $N$, $K$, tìm số hoán vị $N$ phần tử mà có $K$ nghịch thế (inversion), lấy dư với $10^9 + 7$.

Giới hạn: $1 \le N \le 10^5$, $1 \le K \le \min(10^5, \binom{N}{2})$.

??? tip "Lời giải"
    Thường thì mọi người có thể có một ý là gọi $dp[i][j]$ là số hoán vị độ dài $i$ có $j$ nghịch thế. Công thức thì cũng đơn giản: $dp[i][j] = \sum_{k=0}^{i-1} dp[i-1][j-k]$, bởi vì khi ta thêm $i$ vào hoán vị từ $1$ đến $i-1$, số nghich thế sẽ càng tăng khi $i$ càng nằm gần đầu dãy. Độ phức tạp sẽ là $O(NK^2)$, và có thể rút thành $O(NK)$ với prefix sum, nhưng tối ưu như thế vẫn là quá ít để AC.

    Với công thức như trên, ta biết rằng, với phần tử thứ $i$, ta sẽ thêm được $0 \le x \le i-1$ vào tổng số nghích thế, như vậy đáp án sẽ bằng số nghiệm của phương trình $x_1 + x_2 + \dots + x_n = K$ với $0 \le x_i \le i-1$.

    Giống với ví dụ 2, ta áp dụng Nguyên tắc Bao hàm - Loại trừ. Gọi $e_i = ''x_i \ge i''$, ta có $N_{= \emptyset}$ sẽ là kết quả ta cần. Áp dụng cách tương tự như với ví dụ 2, ta có thể nhận ra rằng nếu tổng các phần tử của $T$ bằng $s$, thì số nghiệm của phương trình sẽ là $N_{\supseteq T} = \binom{N-1+(K-s)}{N-1}$. Vậy ta có thể gộp các tập như vậy lại với nhau. Theo Nguyên tắc Bao hàm - Loại trừ, ta có

    $$N_{\supseteq T} = \sum_{s=0}^{K} \binom{N-1+(K-s)}{N-1} \cdot f(s)$$

    với $f(n) = \sum_{i \ge 0} (-1)^i g(n,i)$ và $g(i, j)$ là số cách dùng $j$ số khác nhau trong đoạn $[1, N]$ để có tổng bằng $i$.

    Như vậy bài toán trở thành tính tất cả các $g(i, j)$. Để tính $g(i,j)$ thành 2 trường hợp là:

    - Tập $j$ phần tử có chứa $1$: ta cộng $g(i-j, j-1)$ vào kết quả.
    - Tập $j$ phần tử không chứa $1$: ta cộng $g(i-j, j)$ vào kết quả.

    Bạn nghĩ đến đây là đủ sao? Không. Các tập trong $g(i-j, j-1)$ và $g(i-j, j)$ đều có thể chứa $N$, mà vì chứa $N$ nên khi tính vào $g(i, j)$ chúng sẽ thành $N+1$, không thoả điều kiện của chúng ta, nên ta cần phải trừ đi các tập đó. Nên ta trừ đi $g(i - (N+1), j-1)$.

    Vậy $g(i, j) = g(i-j, j-1) + g(i-j, j) - g(i - (N+1), j-1)$.

    Một nhận xét quan trọng nữa là có nhiều nhất $O(\sqrt{K})$ giá trị cho $j$. Vì vậy bài toán có thể được giải trong $O(K \sqrt{K})$.

#### Ví dụ 4

Đây là bài [Problem K](https://www.acmicpc.net/problem/19313) trong kỳ thi `XVIII Open Cup named after E.V. Pankratiev. - Grand Prix of Gomel`.

Cho số nguyên $m$, tìm số tập không rỗng chứa các số nguyên dương, mà ước chung lớn nhất của chúng bằng $1$, bội chung nhỏ nhất của chúng bằng $m$, lấy dư với $998244353$.

Giới hạn: $1 \le m \le 10^{18}$.

??? tip "Lời giải"
    Rõ ràng ta cần phân tích $m$ ra thừa số nguyên tố. Bạn có thể dùng thuật toán Pollard-Rho ở đây. Nhưng có một cách đơn giản hơn: Đoạn sau bạn có thể thấy rằng chỉ có số mũ của số nguyên tố là quan trọng, chứ chính cái số nguyên tố đó thì không. Nên ta có thể thử chia nó cho tất cả các số nguyên tố đến $10^6$ để xem ta còn gì, một số nguyên tố $p$, một bình phương của số nguyên tố $p^2$, hoặc tích của hai số nguyên tố khác nhau $pq$. Ta có thể kiểm tra trường hợp đầu tiên với thuật toán Rabin-Miller, duyệt qua $[\sqrt{m} - 10, \sqrt{m} + 10]$ để kiểm tra trường hợp thứ hai, ngược lại nó là trường hợp cuối cùng.

    Sau khi phân tích thừa số nguyên tố, ta có $m = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$ (viết vậy thôi chứ $p_i$ vẫn không quan trọng nhé). Rõ ràng ta muốn chọn một tập con các ước của $m$ (để bội chung nhỏ nhất của chúng bằng $m$).
    
    Ta cần tránh đếm các trường hợp có $GCD \neq 1$ và $LCM \neq m$, nên ta có thể áp dụng Nguyên tắc Bao hàm - Loại trừ. Gọi $e_{i,1} = \text{GCD chia hết cho } p_i$ và $e_{i,2} = \text{LCM không chia hết cho } p_i^{a_i}$, nên đáp án là $N_{= \emptyset}$. Ta có $2k$ tính chất cần xét ở đây. Như vậy thì ta cần có $2^{2k} = 4^k$ tập giao, và với mỗi tập giao ta cần tính $t$, là số phần tử trong tập thoả mãn trường hợp tập giao đó, sau đó ta thêm $2^t - 1$ vào đáp án với dấu phù hợp.
    
    Với mỗi thừa số nguyên tố thì ta có 4 trường hợp tập giao là $\emptyset$, $e_{i, 1}$, $e_{i, 2}$ và $e_{i, 1} \cap e_{i, 2}$. Vì mỗi thừa số nguyên tố (theo cách ta đặt tính chất) độc lập với nhau nên $t$ sẽ là tích kết quả của mỗi thừa số nguyên tố. Cụ thể như sau:

    - $\emptyset$: ta có $a_i+1$ cách chọn.
    - $e_{i,1}$: ta muốn $\min(a'_i) \ge 1$ nên ta có $a_i$ cách chọn.
    - $e_{i,2}$: ta muốn $\max(a'_i) < a_i$ nên ta cũng có $a_i$ cách chọn.
    - $e_{i, 1} \cap e_{i, 2}$: gộp 2 trường hợp trên lại ta có $a_i - 1$ cách chọn.
    
    Tính trực tiếp ra sẽ tốn $O(4^k)$, sẽ dẫn đến TLE với $k=15$ trong trường hợp xấu nhất. Tuy nhiên, thấy rằng với mỗi thừa số nguyên tố $e_{i,1}$ và $e_{i,2}$ dẫn đến cùng một cách tính, ta có thể gộp chúng lại và độ phức tạp có thể giảm còn $O(3^k)$.

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [HDU 4135 - Co-prime](https://acm.hdu.edu.cn/showproblem.php?pid=4135) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/HDU/HDU%204135.cpp) | 08/11/2023 |
| [HDU 6397 - Character Encoding](http://acm.hdu.edu.cn/showproblem.php?pid=6397) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/HDU/HDU%206397.cpp) | 12/11/2023 |
| [HackerRank - K-Inversion Permutations](https://www.hackerrank.com/contests/101hack43/challenges/k-inversion-permutations/problem) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/HackerRank/HACKR%20k-inversion-permutations.cpp) | 14/11/2023 |
| [XVIII Open Cup named after E.V. Pankratiev. - Grand Prix of Gomel - Problem K](https://www.acmicpc.net/problem/19313) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/OpenCup/XVIIIOpenCup-GPGomel2018-K.cpp) | 16/11/2023 |
