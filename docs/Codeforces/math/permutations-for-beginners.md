# Hoán vị cho người mới bắt đầu

## Nguồn

<img src="../../../assets/images/codeforces.png" width="16" height="16"/> [[Tutorial] A comprehensive guide to permutations for beginners](https://codeforces.com/blog/entry/111187)

## Định nghĩa, các tính chất cơ bản và các ký hiệu

### Định nghĩa

Để bắt đầu thì ta sẽ cùng xem xét định nghĩa của hoán vị mà chắc bạn đã thấy rất nhiều lần trên Codeforces.

**Định nghĩa**: Một hoán vị kích thước $n$ là một mảng kích thước $n$ chứa các số nguyên từ $1$ đến $n$ mà mỗi số chỉ xuất hiện đúng một lần.

Nhưng tại sao ta lại quan tâm đến mấy cái mảng hay dãy số như thế? Lý do thực ra khá đơn giản.

Xét dãy $a$ chứa $n$ số nguyên. Ta có thể đánh dấu chúng với các số nguyên từ $1$ đến $n$, vậy số nguyên thứ $i$ trong dãy là $a_i$. Để hiểu những điều sau đây, sẽ rất hữu ích khi ta xét ví dụ với $a_i = i$ với mọi $i$.

Giờ ta xáo mảng này lên (một số phần tử có thể ở yên tại chỗ sau khi xáo). Ta sẽ tạo một hoán vị từ việc xáo này theo hai cách:

1. Chỉ số của phần tử lúc đầu ở vị trí $i$ là gì? (Trong trường hợp $a_i = i$, điều này có nghĩa là tìm vị trí của $i$ trong mảng sau khi xáo). Gọi chỉ số này là $f(i)$. Thì $f$ là hàm ánh xạ từ tập $\{1, 2, \dots, n\}$ đến chính nó. Giờ để ý rằng khi ta có mảng $[f(1), f(2), \dots, f(n)]$, nó thoả mãn định nghĩa của hoán vị! Ví dụ, ban đầu ta có mảng $1, 2, 3, 4, 5$, sau khi xáo ta có mảng $2, 4, 1, 5, 3$. Vậy thì mảng $f$ sẽ là $3, 1, 5, 2, 4$.
2. Chỉ số cũ của phần tử ở vị trí $i$ bây giờ là gì? (Trong trường hợp $a_i$ = i$, điều này có nghĩa là xem số ở vị trí $i$ bây giờ là bao nhiêu). Gọi chỉ số này là $g(i)$. Thì $g$ cũng là hàm ánh xạ từ tập $\{1, 2, \dots, n\}$ đến chính nó. Khi ta có mảng $[g(1), g(2), \dots, g(n)]$, nó cũng thoả mãn định nghĩa của hoán vị! Ví dụ, ban đầu ta có mảng $1, 2, 3, 4, 5$, sau khi xáo ta có mảng $2, 4, 1, 5, 3$. Trong trường hợp này mảng $g$ cũng sẽ là $2, 4, 1, 5, 3$. Để ý rằng $f$ và $g$ không được định nghĩa giống nhau, và các hoán vị được sinh ra cũng khác nhau. Thực tế, không khó để nhận ra rằng $f(g(x)) = g(f(x)) = x$ với mọi $x$ trong tập $\{1, 2, \dots, n\}$. 

Như vậy việc xáo các phần tử (hay việc đổi chỗ / hoán vị các phần tử) là một cách khác để thể hiện hoán vị.

Nó cho thấy rằng làm thế nào các hoán vị lại liên quan đến các hàm ánh xạ từ tập $\{1, 2, \dots, n\}$ đến chính nó sao cho tất cả các ảnh đều khác nhau (và tất cả các ảnh đều tương ứng với một vị trí gốc duy nhất). Nói cách khác, một hoán vị có thể được coi là một [song ánh](https://vi.wikipedia.org/wiki/Song_%C3%A1nh) trên một tập, đây là định nghĩa tự nhiên nhất để sử dụng cho khá nhiều ứng dụng. Góc nhìn thứ hai (hàm $g$) là cái tương ứng với định nghĩa này, trong khi hoán vị trong cách thứ nhất (hàm $f$) là cái mà ta thường gọi là **mảng vị trí** của hoán vị trong cách thứ hai (tên này không chuẩn lắm). Sau này ta sẽ thấy rằng nó chính là cái được gọi là **nghịch đảo** của hoán vị.

Lưu ý rằng giải thích vừa rồi khá quan trọng trong việc hiểu rõ hoán vị là gì. Hãy đọc lại một vài lần và thử một vài ví dụ cho đến khi bạn hiểu được hoán vị, cũng như cách các hàm $f$ và $g$ tương tác với nhau.

### Ký hiệu hai dòng (Two-line notation)

Để ý rằng hoán vị $[a_1, a_2, \dots, a_n]$ của $[1, 2, \dots, n]$ tương ứng với một hàm $f$ trên tập ${1, 2, \dots, n}$ định nghĩa bởi hàm $f(i) = a_i$. Nghĩa là, tập các cặp $(i, a_i)$ xác định một hoán vị duy nhất (nó chỉ là một tập các ánh xạ từ vị trí đến phần tử) và ngược lại. Để hiểu kết hợp và nghịch đảo (giới thiệu ở các phần sau) rõ hơn, ta xét ký hiệu sau đây:

$$
\begin{equation*}
\begin{pmatrix} 1 & 2 & \cdots & n \\ a_1 & a_2 & \cdots & a_n \end{pmatrix}
\end{equation*}
$$

Ở đây ta đặt các cặp trên từng cột, từ trái sang phải. Lưu ý rằng các cặp này có thể bị xáo trộn (như domino ấy), dẫn đến một số tính chất thú vị sau:

1. Điều gì sẽ xảy ra khi ta đảo các cặp (thay $(i, a_i)$ bằng $(a_i, i)$ với mọi $i$, tương ứng với việc đổi chỗ hai dòng ấy)? Nếu hoán vị ban đầu tương ứng với hàm $g$, hoán vị sau khi đảo sẽ tương ứng với hàm $f$! Điều này sẽ cho thấy rõ hơn về mối quan hệ giữa $f$ và $g$. Vậy nên thao tác này sẽ nghịch đảo hàm.
2. Giả sử ta có hai hoán vị $p_1$ và $p_2$. Ta sắp xếp các cặp của $p_2$ sao cho hàng trên của nó giống hệt hàng dưới của $p_1$, chuyện gì sẽ xảy ra? Nếu hàm $g$ của $p_1$ là $g_1$, của $p_2$ là $g_2$, thì có thể xác định rằng hàm $g$ của hoán vị mới sẽ là hàm được tạo ra bởi việc áp dụng $g_1$, rồi $g_2$. Vậy nên thao tác này sẽ kết hợp hàm.

### Các giá trị bất biến của hoán vị

Để ý rằng khi một hoán vị được sắp xếp, nó sẽ là $[1, 2, \dots, n]$. Vậy nên bất kỳ thao tác tích luỹ nào trên mảng hoán vị (như tổng, tích, xor, tổng bình phương, số số lẻ, vân vân) mà không phụ thuộc vào thứ tự của các phần tử trong mảng sẽ cho ra kết quả như nhau với mọi hoán vị cùng kích thước.

## Góc nhìn thứ tự

### Các điểm cố định

Một điểm cố định của hoán vị $a$ là một chỉ số $i$ sao cho $a_i = i$. Các điểm này là các điểm không bị ảnh hưởng bởi hoán vị, vậy nên nếu ta bỏ qua những gì xảy ra với các điểm này, ta sẽ không bị mất đi bất kỳ thông tin nào về hoán vị đó. Đây cũng là lý do tại sao các chỉ số $i$ này thường được bỏ qua trong ký hiệu hai dòng (và cũng trong ký hiệu chu trình, sẽ được giới thiệu ở phần sau).

**Lưu ý**: nếu bạn đã quen với chu trình hoặc đang đọc lại bài viết này, bạn có thể nhận thấy rằng ý này phù hợp hơn với chu trình và tổ hợp, nhưng mình vẫn để nó ở đây vì nó có chung một số ý tưởng với các phần nhỏ khác trong phần này. Tương tự, điều này cũng áp dụng cho phần tiếp theo.

### Các derangement

Một derangement là một hoán vị không có điểm cố định nào. Nghĩa là với mọi $i$, ta có $a_i \neq i$. Gọi $D_n$ là số hoán vị độ dài $n$ là derangement. Có ít nhất 3 cách khác nhau để đếm:

#### Giải các phương trình tuyến tính

Ta nhóm tất cả các hoán vị bằng số điểm cố định của chúng. Nếu có $i$ điểm cố dịnh, ta đánh số $n-i$ phần tử còn lại từ $1$ đến $n-i$ thì ta sẽ có một derangement. Vậy số hoán vị $n$ phần tử với $i$ điểm cố định sẽ là $\binom{n}{i} \cdot D_{n-i}$.

Tổng hết lại trên mọi $i$ sẽ cho ta identity là $n! = \sum_{i=0}^{n} \binom{n}{i} \cdot D_{n-i}$.

Cùng với $D_0 = 1$ và $D_1 = 0$, ta có thể dùng quy nạp để có $D_n = n! \cdot \sum_{i=0}^{n} \frac{(-1)^i}{i!}$. Ta cũng có thể dùng identity sau để có được kết quả này:

??? note "Trường hợp đặc biệt của nghịch đảo Mobius"
    Nếu có các hàm $f$ và $g$ ánh xạ từ $\mathbb{Z}_{\ge 0}$ đến $\mathbb{R}$, thì hai mệnh đề sau đây tương đương:
    
    1. $g(n) = \sum_{i = 0}^n (-1)^i \binom{n}{i} f(i)$
    2. $f(n) = \sum_{i = 0}^n (-1)^i \binom{n}{i} g(i)$

#### Đệ quy

Giả sử $a_n = k \neq n$. Xét $a_k$. Nếu $a_k = n$ thì ta có $D_{n-2}$ cách để hoán vị các phần tử còn lại. Nếu $a_k \neq n$, ta để ý rằng bài toán sẽ quay về tính số derangement cho $n-1$ phần tử bằng cách thay $n$ (được gán trong $n-2$ slot còn lại) bằng $k$.

Như vậy công thức sẽ là $D_n = (n-1) \cdot (D_{n-1} + D_{n-2})$, dùng quy nạp cũng có thể giải ra được.

#### Dùng nguyên tắc bao hàm và loại trừ

Gọi $S_i$ là tập các hoán vị có $i$ là điểm cố định (phần còn lại hoán vị thoải mái). Ta sẽ có đáp án là $n! - |\cup_{i} S_i|$. Với nguyên tắc Bao hàm - Loại trừ, vì giao của bất kỳ $k$ thằng $S_i$ nào cũng có kích thước là $(n - k)!$, ta sẽ có công thức tương tự cho $D_n$.

### Các nghịch thế

Một nghịch thế trong một mảng (không nhất thiết là mảng hoán vị) là bất kỳ cặp chỉ số $(i, j)$ sao cho $i < j$ và $a_i > a_j$. Số nghịch thế ít nhất là bao nhiêu? Là 0, vì ta chỉ cần cho $a_i = i$. Số nghịch thế nhiều nhất là bao nhiêu? Là $\frac{n \cdot (n-1)}{2}$ vì ta chỉ cần cho $a_i = n - i + 1$, khi đó thì bất kỳ cặp chỉ số nào cũng là nghịch thế.

Xét bài tập sau. Cho một hoán vị (hay một mảng các phần tử đôi một khác nhau), ta được phép thực hiện thao tác sau vô số lần: Chọn bất kỳ chỉ số $1 \le i < n$ nào và đổi chỗ $a_i$ và $a_{i+1}$. Có hai câu hỏi ở đây:

1. Ta có thể sắp xếp mảng mà chỉ dùng các thao tác như trên không?
2. Nếu có, số lần thao tác ít nhất ta cần là bao nhiêu?

Lưu ý rằng nếu ta làm được trên hoán vị, ta cũng làm được trên mảng các phần tử đôi một khác nhau (chỉ cần thay các phần tử bằng chỉ số của chúng trong mảng đã sắp xếp).

Với câu hỏi đầu tiên, câu trả lời là **có**. Ý tưởng chính ở đây là tìm số bé nhất rồi cứ đổi chỗ nó với phần tử trước nó cho đến khi đến được vị trí đầu tiên, sau đó làm tương tự với số bé nhì, và tiếp tục như vậy.

Còn số thao tác thì sao nhỉ? Để chuyển số bé nhất thì ta cần bao nhiêu thao tác? Lưu ý rằng tất cả các số trước $1$ trong hoán vị ban đầu sẽ góp phần tạo ra một nghịch thế trong đó phần tử thứ hai là $1$ (là $j$ trong cặp chỉ số $(i, j)$ ấy). Giờ sau khi $1$ đã ở đúng vị trí của nó (vị trí đầu tiên), sẽ không còn nghịch thế nào liên quan đến $1$ nữa. Với phần còn lại của hoán vị, ta có thể tiếp tục dùng cách này, với phần tử bé nhất là $2$. Nhưng để làm được điều đó, ta cần xem chuyện gì sẽ xảy ra với các nghịch thế không có $1$ trong đó. Lưu ý rằng thứ tự tương đối của các cặp khác không thay đổi nên các nghịch thế còn lại vẫn y nguyên. Vậy tổng số thao tác rõ ràng là số nghịch thế trong hoán vị.

Đó có phải là số thao tác ít nhất để sắp xếp mảng không? Hoá ra câu trả lời là **có**. Xét một thao tác nào đó đã xong. Vì nó đổi chỗ hai phần tử kề nhau, sẽ có nhiều nhất một nghịch thế mất đi. Vậy tổng số nghịch thế giảm đi nhiều nhất là $1$. Trong mảng đã sắp xếp, không có nghịch thế nào cả. Vậy số thao tác sẽ ít nhất là số nghịch thế trong hoán vị.

Giờ bạn có thể nghĩ, làm sao ta có thể đếm số nghịch thế trong một hoán vị đây? Bạn có thể dùng merge sort hoặc các cấu trúc dữ liệu trên đoạn như Fenwick tree hay Segment tree. Giải bằng merge sort thì bạn có thể xem tại [đây](https://www.cp.eng.chula.ac.th/~prabhas//teaching/algo/algo2008/count-inv.htm), còn với cấu trúc dữ liệu thì như sau:

- Ban đầu, ta có mảng $A$ độ dài $n$ gồm toàn số $0$ (khi khởi tạp cấu trúc dữ liệu).
- Với mỗi $i$ từ $1$ đến $n$, tìm tổng tiền tố của $A$ từ $0$ đến $a_i - 1$, và thêm nó vào đáp án. Sau đó, tăng $A_i$ lên $1$.

### Dãy con tăng dài nhất (Longest Increasing Subsequence - LIS) và định lý Erdős–Szekeres

Một dãy con tăng của một mảng $a$ (không nhất thiết phải là hoán vị) là một dãy các chỉ số $i_1 < i_2 < \dots < i_k$ sao cho $a_{i_1} < a_{i_2} < \dots < a_{i_k}$. Dãy con giảm cũng được định nghĩa tương tự.

Bạn có thể xem thuật toán tìm dãy con tăng dài nhất (hoặc dãy con không giảm dài nhất) của một mảng tại [đây](https://youtu.be/watch?v=22s1xxRvy28). Nhưng ở đây ta sẽ không quan tâm đến phần này cho lắm.

Cái ta quan tâm là giới hạn độ dài của bất kỳ dãy con tăng dài nhất nào (từ giờ gọi là **LIS** - Longest Increasing Subsequence nhé). Tuy nhiên, với dãy con giảm, LIS có độ dài là $1$. Định lý Erdős–Szekeres cho ta biết rằng trong những trường hợp như vậy, độ dài dãy con giảm dài nhất sẽ lớn.

Định lý phát biểu rằng trong bất kỳ hoán vị nào (hoặc mảng có các phần tử đôi một khác nhau) độ dài $xy + 1$, ta sẽ luôn có một dãy con tăng dài $x + 1$ hoặc một dãy con giảm dài $y + 1$.

Cách dễ nhất để chứng minh định lý này là dùng nguyên tắc chuồng chim (Pigeonhole principle).

Ta phản chứng rằng định lý sai với một hoán vị $a$ nào đó. Với mọi $i$, xét độ dài dãy con tăng dài nhất kết thúc ở vị trí $i$ và độ dài dãy con giảm dài nhất cũng kết thúc ở vị trí $i$. Gọi các số này là $x_i$ và $y_i$. Lưu ý rằng tất cả $x_i$ là số nguyên và nằm giữa $1$ và $x$, và tất cả $y_i$ là số nguyên và nằm giữa $1$ và $y$. Vậy nên ta sẽ có nhiều nhất $xy$ cặp $(x_i, y_i)$ khác nhau. Theo nguyên tắc chuồng chim, sẽ tồn tại $i < j$ sao cho $x_i = x_j$ và $y_i = y_j$. Vì tất cả các phần tử đều khác nhau, $a_i < a_j$ hoặc $a_i > a_j$, trong trường hợp đầu, không thể xảy ra chuyện $x_i = x_j$ và trong trường hợp sau, không thể xảy ra chuyện $y_i = y_j$. Điều này mâu thuẫn với giả thiết ban đầu, vậy nên định lý đúng.

Có một chứng minh tinh tế và sâu hơn dùng định lý Dilworth. [Blog này](https://codeforces.com/blog/entry/100910) dùng nó để chứng minh một trường hợp đặc biệt của định lý, mặc dù ta cũng có thể sửa nó một chút để chứng minh toàn bộ định lý.

### Hoán vị tiếp theo

Hoán vị chỉ là một dãy số nguyên, nên ta có thể sắp xếp tập tất cả các dãy độ dài $n$ theo thứ tự từ điển. Điều này định ra thứ tự tự nhiên của mỗi hoán vị. Giờ làm sao để tìm hoán vị tiếp theo của một hoán vị cho trước?

Cách dễ nhất (trong C++) là dùng `std::next_permutation`, nhưng ta sẽ xem sơ lược về cách nó hoạt động.

Đầu tiên ta cần tìm chỉ số $i$ từ phải sang sao cho $a_i < a_{i+1}$. Vì $i$ là chỉ số đầu tiên thoả mãn điều này, tất cả các giá trị nằm trong các chỉ số từ $i$ đến $n$ sẽ tạo thành một mảng giảm dần. Lưu ý rằng số nhỏ nhất trong dãy giảm này mà lớn hơn $a_i$ sẽ là phần tử mới ở vị trí $i$, và phần còn lại (cùng với số $a_i$ bây giờ) sẽ được sắp xếp tăng dần. Cái này có thể được cài trong $O(n-i+1)$.

Để ý rằng bắt đầu từ hoán vị có thứ tự từ điển nhỏ nhất (là $[1, 2, \dots, n]$), số hoán vị giữa (và bao gồm) hoán vị này và hoán vị có chỉ số $i$ đầu tiên mà $a_i \ne i$ là $k$ sẽ ít nhất là $(n-k)! + 1$. Điều này có nghĩa là nếu bạn dùng `next_permutation` nhiều lần, số phần tử trong hoán vị thay đổi sẽ không nhiều (trừ khi bạn bắt đầu ở một hoán vị nào đó, và ngay cả trong trường hợp đó, ngoài một thay đổi với tất cả các chỉ số tiềm năng, kết luận tương tự vẫn giữ nguyên).

Vậy nếu ta có một hoán vị độ dài $n$, bạn dùng `next_permutation`(như cài đặt ở trên) trong $O(n^k)$ lần, thời gian cần sẽ là khoảng (ít hơn nhiều so với) $O(kn^k \log n)$. Ta cũng có thể mô phỏng kết quả của $r$ thao tác `next_permutation` trong $O(r+n)$ (cho ra kết quả chính xác chứ không cài đặt tương tự như trên). Phân tích cũng tương tự với việc phân tích độ phức tạp khi tăng một số nhị phân $n$ bit lên $r$ lần.

### Các hoán vị ngẫu nhiên

Có tổng cộng $n!$ hoán vị độ dài $n$. Làm sao để tạo ra một hoán vị ngẫu nhiêu nếu ta chỉ có một trình sinh số ngẫu nhiên (random number generator - RNG) cho ta một số nguyên trong một đoạn tự chọn nào đó?

Về việc nghĩ cách làm sao để tạo dần một hoán vị như thế, hãy thử loại bỏ tất cả các phần tử $> k$ với một số $k$. Lưu ý rằng vị trí của $k$ trong mảng này có khả năng là bất cứ số nguyên nào từ $1$ đến $k$. Tuy nhiên nó sẽ không đưa ta đến một thuật toán hiệu quả ngay được.

Ta sẽ muốn tạo một hoán vị từ trái sang phải. Giả sử ta chọn ra được một tiền tố. Lưu ý rằng hoán vị của tất cả các phần tử còn lại đều có khả năng như nhau. Thêm nữa, tất cả các phần tử bên phải cũng có khả năng như nhau để trở thành phần tử đầu tiên của hậu tố (phần tử tiếp theo của tiền tố ấy). Nhận xét này dẫn đến biến thể Durstenfeld của [thuật toán xáo Fisher-Yates](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle).

Giờ ta xem xét một vài thông số của hoán vị ngẫu nhiên:

Đầu tiên, độ dài kỳ vọng của dãy tăng dần được chọn tham lam bằng thuật toán này là bao nhiêu:

- Nếu không có gì trong dãy hoặc phần tử mới lớn hơn phần tử được chọn cuối cùng, chọn phần tử này.

Lưu ý rằng một phần tử được chọn khi và chỉ khi nó lớn hơn tất cả các phần tử được chọn trước nó. Vậy nên ta dùng kỳ vọng tuyến tính:

$E[l] = E[\sum_i(a_i \text{ được chọn})] = \sum_i P[a_i \text{ được chọn}] = \sum_i P[a_i > \max(a_1, \dots, a_{i - 1})] = \sum_i \frac{1}{i}$ xấp xỉ $\ln n$

Tuy nhiên, thực ra kỳ vọng độ dài của LIS là $\Theta(\sqrt{n})$, cho nên thuật tham lam sẽ tệ hơn nhiều so với việc tính LIS bài bản.

Để biết thêm số liệu thống kê hoán vị ngẫu nhiên cũng có một số thông tin về số liệu thống kê được lấy từ một số phần tiếp theo, bạn có thể xem tại [đây](https://en.wikipedia.org/wiki/Random_permutation_statistics).

## Góc nhìn phân rã chu trình

Giờ ta sẽ đến với phần rất quan trọng trong lý thuyết hoán vị - phân rã chu trình. Bạn sẽ thấy rằng bản thân dùng những thứ sau đây khá nhiều khi giải các bài tập về hoán vị.

### Chu trình

Giả sử ta có một hoán vị $a$. Cố định vị trí $i$. Giờ nhìn vào dãy $i$, $a_i$, $a_{a_i}$, $a_{a_{a_i}}$, $\dots$. Đến cùng thì nó sẽ lặp lại vì chỉ có nhiều nhất $n$ giá trị mà dãy này có thể có. Để cho tiện thì gọi phần tử thứ $j$ của dãy này là $b_j$.

Tiếp theo thì với $k$ nào đó mà $k < l$, ta sẽ có $b_k = b_l$. Cho $k$ là chỉ số bé nhất có tính chất như vậy, và $l$ là chỉ số bé nhất ứng với $k$. Nếu $k$ không phải $1$ thì ta sẽ có $b_{k-1} = b_{l-1}$, vì $a$ là song ánh. Tuy nhiên, điều này mâu thuẫn với tính tối giản của $k$. Nghĩa là phần tử đầu tiên lặp trong dãy này thực ra lại là $i$.

Giờ giả sử có gì đó trong dãy giữa $1$ và $l$ lặp lại (ở các vị trí $1 < m < o < l$). Ta lập luận song ánh $m-1$ lần, ta sẽ có $b_{o - m + 1} = b_1 = i$, nên là $o - m + 1 \ge l$, cái này cũng mâu thuẫn luôn. Điều này nghĩa là dãy bắt đầu lặp từ $l$ và tạo một **chu trình** (cycle).

Ta gọi nó là chu trình vì nếu ta tạo một đồ thị có các cạnh có hướng từ $i$ đến $a_i$, thì $i$ sẽ nằm trong một chu trình độ dài $l - 1$.

Ta đã xong với một $i$. Làm tương tự với tất cả $i$ nghĩa là tất cả các phần tử sẽ nằm trong một chu trình nào đó trong đồ thị. Vì bậc vào và bậc ra của mỗi $i$ đều là $1$, các chu trình này riêng rẽ với nhau.

Ví dụ, ta có hoán vị $[2,3,1,5,4]$. Các chu trình của mỗi phần tử là:

- $1 \to 2 \to 3 \to 1$
- $2 \to 3 \to 1 \to 2$
- $3 \to 1 \to 2 \to 3$
- $4 \to 5 \to 4$
- $5 \to 4 \to 5$

Các chu trình này tương ứng với các chu trình $1 \to 2 \to 3 \to 1$ và $4 \to 5 \to 4$ trong đồ thị.

### Ký hiệu chu trình

Vì các chu trình này độc lập, ta có thể nói rằng với mỗi chu trình, các phần tử nằm ngoài nó sẽ không liên quan. Vậy với bất kỳ hoán vị nào, ta chỉ cần chỉ ra những chu trình của chúng và ta có thể xác định được hoán vị đó.

Vậy ta chỉ cần biểu diễn hoán vị dưới dạng một dãy các chu trình của nó. Ví dụ, hoán vị $[2,3,1,5,4]$ có thể được biểu diễn là $(123)(45)$.

Lưu ý, ký hiệu này có ý nghĩa sâu xa hơn liên quan đến kết hợp hoán vị và cách các chu trình rời rạc tác động đến kết hợp hoán vị.

### Tìm giá trị thứ k tiếp theo, đồ thị chức năng

Xét bài toán sau: với một hoán vị, tìm giá trị của $a_{a_{\ddots_{i}}}$ với mọi $i$ khi ta có $k$ chữ $a$ trong ký hiệu, $k \le 10^{18}$.

Lưu ý rằng nếu tìm được các chu trình, ta có thể dùng modulo độ dài chu trình để tìm ra kết quả.

Chuyện gì sẽ xảy ra nếu $a$ không đảm bảo là một hoán vị nhưng tất cả các phần tử trong $a$ vẫn nằm trong đoạn $[1,n]$? Khi đó thì đồ thị sẽ không còn chỉ tồn tại các chu trình nữa, nhưng nó sẽ có tính chất như sau:

- Mỗi thành phần liên thông yếu bao gồm 2 phần: một chu trình có hướng và các cây có hướng với gốc tại các đỉnh riêng biệt trong chu trình, hướng về gốc (còn gọi là các cụm cây định hướng ngược - reverse-oriented arborescences).

Bài toán tương tự cũng có thể được giải theo cách này, dùng binary lifting cho mỗi đỉnh cho đến khi đạt đến chu trình "chính" của thành phần liên thông chứa nó.

Nói theo cách của lý thuyết đồ thị, đồ thị như vậy được gọi là **đồ thị chức năng (functional graph)**, chúng có bậc ra của mỗi đỉnh là $1$.

Một số bài luyện tập là bài [Planet Queries I](https://cses.fi/problemset/task/1750) và [Planet Queries II](https://cses.fi/problemset/task/1160) trên CSES.

### Đổi chỗ / chuyển vị

Bắt đầu từ mảng $[1, 2, \dots, n]$, dùng một số phép đổi chỗ trên mảng này cho đến khi ta đến được một hoán vị mong muốn $a = [a_1, a_2, \dots, a_n]$. Lưu ý rằng ta luôn có thể áp dụng các phép đổi chỗ, bằng cách tạo hoán vị từ trái sang phải. Các phép đổi chỗ này còn được gọi là các phép chuyển vị (transpositions).

### Đổi chỗ trong chu trình

Giờ ta xem chuyện gì xảy ra khi ta áp dụng một phép đổi chỗ trên một hoán vị. Giả sử phép đổi chỗ này đổi chỗ hai phần tử ở vị trí $i$ và $j$. Xét đồ thị biểu diễn hoán vị này. Trong đồ thị, đổi chỗ hai phần tử ở vị trí $x$ và $z$ sẽ tương đương với việc bẻ hai cạnh $x \to y$ và $z \to w$ và tạo hai cạnh $x \to w$ và $z \to y$ (giống bắt chéo nhau ấy).

Có hai trường hợp ở đây:

1. $i$ và $j$ nằm khác chu trình: hai chu trình sẽ nhập làm một.
2. $i$ và $j$ nằm trong cùng một chu trình: chu trình này sẽ tách ra làm hai.

Bạn có thể làm thử bài [1768D - Lucky Permutation](https://codeforces.com/contest/1768/problem/D).

Thêm một bài sắp xếp hoán vị khác, nhưng ta không chỉ có thể đổi chỗ hai phần tử cạnh nhau, ta có thể đổi chỗ bất kỳ cặp nào. Số lần đổi chỗ ít nhất cần để sắp xếp mảng này là bao nhiêu?

Lưu ý rằng ở kết quả cuối cùng (hoán vị đã sắp xếp), ta sẽ có đúng $n$ chu trình (đỉnh nối chính nó). Giả sử giờ ta có $c$ chu trình. Vì số chu trình tăng 1 mỗi lần đổi chỗ, ta sẽ cần ít nhất $n - c$ lần đổi chỗ để sắp xếp hoán vị này.

Nhưng đó có phải đáp án thực sự không? Đúng. Ta có thể đổi chỗ các phần tử trong cùng chu trình khi độ dài chu trình từ $2$ trở lên, và đến cuối cùng nó sẽ sắp xếp hoán vị đề bài.

## Góc nhìn kết hợp hoán vị

### Định nghĩa

Giả sử ta có hai hoán vị $a$ và $b$ có cùng độ dài $n$. Giờ ta muốn định nghĩa kết hợp hoán vị như sau: $ab$ được định nghĩa là mảng $c$ sao cho $c_i = a_{b_i}$.

Điều này tương ứng với việc tìm hợp của hàm $g$ của $a$ và $b$, với $g$ của $b$ được áp dụng trước.

Để cho dễ hiểu thì ta đi vào phân tích một chút. Đầu tiên ta xét trường hợp khi tất cả $b_i = i$ (hoán vị đồng nhất), thì $c = a$ theo định nghĩa. Tương tự, nếu $a$ là hoán vị đồng nhất thì $c = b$. Như vậy việc kết hợp với hoán vị đồng nhất theo bất kỳ thứ tự nào cũng sẽ cho ra lại hoán vị ban đầu.

Giờ ta hãy dùng ký hiệu hai dòng để diễn tả. Xét hai hoán vị $a$ và $b$ như sau:

$$
\begin{equation*}
\begin{pmatrix} 1 & 2 & \cdots & n \\ a_1 & a_2 & \cdots & a_n \end{pmatrix}
\end{equation*}
$$

và 

$$
\begin{equation*}
\begin{pmatrix} 1 & 2 & \cdots & n \\ b_1 & b_2 & \cdots & b_n \end{pmatrix}
\end{equation*}
$$

Sắp xếp lại các cột trong ký hiệu hai dòng của $a$ sao cho hàng dưới của $b$ ứng với hàng trên của $a$. Tuy nhiên, điều này tương đương với việc xáo các cột của $a$ theo $b$:

$$
\begin{equation*}
\begin{pmatrix} b_1 & b_2 & \cdots & b_n \\ a_{b_1} & a_{b_2} & \cdots & a_{b_n} \end{pmatrix}
\end{equation*}
$$

Lưu ý rằng đây vẫn là ký hiệu hai dòng chuẩn cho $a$. Giờ nếu ta "chập" nó với ký hiệu hai dòng của $b$, ta sẽ có ký hiệu hai dòng của hợp của $a$ và $b$.

Điều này giải thích một cách tự nhiên vì sao hoán vị lại được xem như một song ánh trên một tập hợp.

Ta bắt đầu với hoán vị đồng nhất, rồi áp hoán vị đầu tiên vào, rồi áp hoán vị thứ hai vào. Áp dụng vào nghĩa là thay $x \mapsto a_x$. Ký hiệu hai dòng của hoán vị $a$ có tính chất như sau:

- Nếu hoán vị hàng trên là $p$ thì hoán vị hàng dưới là $ap$.

### Ví dụ - chu trình và đổi chỗ

Lưu ý rằng ta có thể liên kết một chu trình với một hoán vị, trong đó các phần tử không phải là chu trình là các điểm cố định, và phần còn lại được ánh xạ theo chu trình. Theo nghĩa này, các chu trình là các hoán vị.

Cũng lưu ý rằng một phép đổi chỗ cũng là một hoán vị theo nghĩa như vậy. Thực tế, một thao tác đổi chỗ chỉ là một chu trình độ dài $2$.

Bạn có thể viết ra vài ví dụ về đổi chỗ và chu trình và viết chúng dưới dạng ký hiệu hai dòng để hiểu cách chúng được tạo thành và ánh xạ.

Đến đây, ta cần nhớ hai điều sau:

1. Khi giới thiệu về chu trình, ta viết chúng dưới một format nhất định. Thực tế, bạn có thể viết các chu trình rời rạc mà không cần quan tâm đến thứ tự chúng được viết như thế nào. Việc này đi từ thực tế rằng chúng độc lập theo một cách nào đó (một phần tử được di chuyển trong một hoán vị sẽ là điểm cố định của các hoán vị còn lại). Bạn cũng có thể thấy rằng ký hiệu $(123)(45)$ cũng cho ta thấy rằng hoán vị này bao gồm hai chu trình $(123)$ và $(45)$.
2. Khi ta nói về việc đổi chỗ, ý ở đây là thực sự đổi chỗ các phần tử. Nó tương ứng với việc nhân hoán vị với một hoán vị đổi chỗ tương ứng. Sẽ dễ hiểu hơn nếu bạn có một số ví dụ về việc đổi chỗ và cách chúng có thể kết hợp với nhau.

Điều quan trọng cần lưu ý là hợp hoán vị có tính kết hợp.

Giả sử ta có một hoán vị được tạo ra từ việc áp dụng 3 hoán vị sau: $(12)$, $(312)(43)$ và $(53241)$ theo thứ tự như vậy, ta sẽ viết chúng thành $(53241)(312)(43)(12)$. Lưu ý rằng $(12)$ và $(43)$ là các chu trình độ dài $2$, nghĩa là chúng là các phép đổi chỗ.

Giờ làm sao để đưa nó về lại một hoán vị bình thường? Có một cách là viết hoán vị của mỗi chu trình và tạo ra nó. Một cách tốt để làm việc này là: với mỗi phần tử, đi từ bên phải, và thay nó bằng cái mà chu trình chứa nó ánh xạ tới. Ví dụ, nếu ta muốn tìm ảnh của $1$, chu trình đầu tiên sẽ ánh xạ $1$ tới $2$, chu trình thứ hai sẽ ánh xạ $2$ tới $2$, chu trình thứ ba sẽ ánh xạ $2$ tới $3$, và chu trình cuối cùng sẽ ánh xạ $3$ tới $2$.

### Tính chẵn lẻ của hoán vị

Ở trên thì ta đã đề cập đến việc đổi chỗ hai phần tử cạnh nhau sẽ giảm số nghịch thế đi $1$. Chính xác hơn thì nó sẽ $\pm 1$ số nghịch thế, và sẽ thay đổi tính chẵn lẻ của số nghịch thế của hoán vị.

Ta định nghĩa **tính chẵn lẻ** của hoán vị là tính chẵn lẻ của số nghịch thế của hoán vị đó.

Điều này quan trọng vì nó giúp xác định tính chẵn lẻ của các phép đổi chỗ (không chỉ là các phép đổi chỗ liền kề) cũng như một số thông tin về tính chẵn lẻ của các chu trình, như sau.

Xét một phép đổi chỗ hai phần tử ở vị trí $i < j$. Vậy thì nó sẽ tương đương với việc áp dụng $j-i$ phép đổi chỗ liền kề để mang $a_j$ về vị trí $i$, và $j-i-1$ phép đổi chỗ liền kề để mang $a_i$ (từ vị trí mới của nó) đến vị trí $j$. Nó sẽ tốn số lẻ lần đổi chỗ liền kề, nên nó sẽ thay đổi tính chẵn lẻ của hoán vị.

Như một hệ quả tất yếu, việc áp dụng bất kỳ phép đổi chỗ nào sẽ làm thay đổi tính chẵn lẻ của hoán vị, và cụ thể hơn, tất cả các hoán vị đổi chỗ đều có tính lẻ.

Giờ lưu ý rằng với một chu trình, ta có thể tạo ra nó với một số phép đổi chỗ. Cụ thể hơn, nếu chu trình là $(i_1, i_2, \dots, i_k)$, ta có thể dùng $k-1$ phép đổi chỗ để áp dụng biến đổi tương tự như hoán vị chu trình.

Vậy tất cả các chu trình chẵn sẽ có tính lẻ, và tất các chu trình lẻ sẽ có tính chẵn.

Xét một sự phân rã bất kỳ của một hoán vị thành các chu trình (có thể không rời rạc). Theo kết quả ở trên, tính chẵn lẻ của hoán vị là lẻ khi và chỉ khi số chu trình chẵn là lẻ.

Cụ thể, với việc phân rã một hoán vị thành các phép đổi chỗ, tính chẵn lẻ của hoán vị sẽ giống tính chẵn lẻ của số lần đổi chỗ trong phân rã đó. Lưu ý rằng điều này cũng tương đuơng với việc không thể có hai cách phân rã với hiệu số lần đổi chỗ là lẻ.

Từ kết quả trên, ta có một fact là nếu cần một số lẻ phép đổi chỗ để tạo ra một hoán vị, hoán vị đó sẽ có tính lẻ và ngược lại.

### Tính chẵn lẻ khi kết hợp

Rõ ràng, từ trên ta suy ra được tính chẵn lẻ cộng dồn với modulo 2 khi kết hợp. Cái này khá quan trọng để có một phần riêng vì nó tóm tắt tất cả các ý ở trên.

### Nghịch đảo của hoán vị

Ta xét hoán vị trong hoàn cảnh thực tế. Có cách nào để có được hoán vị ban đầu sau khi có một số hoán vị khác đã được áp dụng vào nó không? Từ các lưu ý trong phần ký hiệu hai dòng, chỉ cần làm như sau là đủ với hoán vị ban đầu là hoán vị đồng nhất. Giả sử hoán vị được áp dụng là $a$:

$$
\begin{equation*} 
\begin{pmatrix} 1 & 2 & \cdots & n \\ a_1 & a_2 & \cdots & a_n \end{pmatrix} 
\end{equation*}
$$

Theo như lưu ý về kết hợp hoán vị dùng ký hiệu hai dòng, ta cần đảo hai dòng như sau:

$$
\begin{equation*}
\begin{pmatrix} a_1 & a_2 & \cdots & a_n\\ 1 & 2 & \cdots & n \end{pmatrix}
\end{equation*}
$$

Xét mảng vị trí $p$ của $a$ ta định nghĩa ở trên, tức là $p_i$ là vị trí mà có $a$ có giá trị là $i$, nghĩa là $a_{p_i} = i$. Lưu ý rằng $a$ có giá trị $a_i$ ở vị trí $i$, nên $p_{a_i}$ là vị trí mà $a$ có giá trị là $a_i$, nghĩa là $p_{a_i} = i$. Suy ra $pa = ap$, và giá trị chung này gọi là hoán vị đồng nhất - identity permutation, ta sẽ gọi nó là $\text{id}$ luôn nhé.

Nói cách khác, $p$ và $a$ nghịch nhau khi kết hợp. Lưu ý rằng $a$ cũng là mảng vị trí của $p$. Ta gọi $p$ là $a^{-1}$.

Giờ ta có một số hiểu biết về hoán vị nghịch đảo theo ký hiệu hai dòng, còn theo chu trình, đổi chỗ, kết hợp thì như thế nào?

1. Nghịch đảo của chu trình $(i_1, i_2, \dots, i_k)$ sẽ là $(i_k, \dots, i_2, i_1)$. Ta đơn giản đảo tất cả các cạnh có hướng của đồ thị.
2. Nghịch đảo của một phép đổi chỗ là chính nó. Đơn giản là vì nó là chu trình độ dài $2$.
3. Nghịch đảo của một phép kết hợp hoán vị $ab$ là $b^{-1} a^{-1}$. Điều này tương ứng với việc hoàn tác việc áp dụng hoán vị trên một stack và cũng có ý nghĩa đại số như sau: $abb^{-1}a^{-1} = aa^{-1} = \text{id} = b^{-1}b = b^{-1}a^{-1}ab$.

Cụ thể, để phân tách một hoán vị thành các chu trình (không nhất thiết phải rời rạc), ta chỉ cần lấy ảnh phản chiếu của phân rã đó, nó sẽ tương ứng với nghịch đảo của hoán vị!

Thêm nữa, tính chẵn lẻ của hoán vị nghịch đảo cũng y như tính chẵn lẻ của hoán vị gốc.

### Involution

Một involution là một hoán vị có nghịch đảo là chính nó. Xét sự phân tách một hoán vị $a$ thành các chu trình rời rạc $a = c_1 \dots c_k$. $a = a^{-1}$ nghĩa là $\text{id} = a^2 = \prod_i c_i^2$. Ta viết được như thế vì các chu trình rời rạc giao hoán và các chu trình giống nhau cũng vậy. $c_i^2$ phải là một map nhận dạng trên các phần tử của $c_i$ vì nếu không thì hoán vị kết quả sẽ không phải là $\text{id}$. Điều này có nghĩa là $c_i$ có độ dài $1$ hoặc $2$. Ngược lại, có thể kiểm tra xem các hoán vị này có phải involution hay không.

### Mũ k của hoán vị

Vì phép kết hợp hoán vị có tính kết hợp, ta có thể dùng luỹ thừa nhị phân để tính hoán vị. Một cách toán học hơn để làm là dùng cách tương tự với phần trước. Với định nghĩa tương tự phần trước, với mọi $a$, $a^k = \prod_i c_i^k$, vì thế nên cấu trúc chu trình sẽ được xác định bởi số mũ của chu trình.

Việc tìm mũ $k$ của một chu trình cũng tương ứng với việc ánh xạ nó đến điểm thứ $k$ tiếp theo của nó trên chu trình. Nếu độ dài chu trình là $c$ và $g = gcd(c, k)$, thì việc phân tách chu trình rời rạc $c^k$ gồm $g$ chu trình, với mỗi chu trình tương ứng với một bước độ dài $k$ dọc theo chu trình ban đầu.

### Thứ tự của hoán vị

Thứ tự của hoán vị $a$ được định nghĩa là $k$ nhỏ nhất sao cho $a^k$ là hoán vị đồng nhất. Xem lại phần trước, với chu trình $c$ độ dài $l$ cần phân tách thành các điểm cố định, điểu kiện cần và đủ là số mũ của hoán vị chia hết cho $l$. Vậy thự tự của hoán vị chỉ là bội chung nhỏ nhất của độ dài của tất cả các chu trình.

### Căn bậc hai của hoán vị

Phần này ta sẽ giải bài tập sau [612E - Square Root of Permutation](https://codeforces.com/contest/612/problem/E). Bài này sẽ không khó với những kiến thức ở các phần trước.

### Liên hợp và lớp liên hợp

Cho hai hoán vị $a$, $b$. Xét hoán vị $aba^{-1}$. Nhớ lại cách kết hợp ký hiệu hai dòng cho việc kết hợp các hoán vị này, đây chỉ là một hoán vị có phân tách chu trình gần giống $b$, nhưng $a$ được áp dụng cho mỗi phần tử trong chu trình. Nói cách khác, ta diễn giải lại các chu trình bằng cách ánh xạ tới và từ một ground set riêng biệt thông qua hoán vị $a$.

Cụ thể hơn, gọi phân tách chu trình của $b$ là $c_1 \cdots c_k$, trong đó $c_i = (x_{i1}, \dots, x_{il_i})$. Ta nói rằng $aba^{-1}$ có phân tách chu trình là $c'_1 \cdots c'_k$ trong đó $c'_i = (a_{x_{i1}}, \dots, a_{x_{il_i}})$.

Chứng minh sẽ làm rõ mệnh đề ở đầu phần này. Xét phần tử $i$, ta sẽ xem chuyện gì xảy ra với $i$ khi mỗi hoán vị được áp dụng vào nó:

1. $aba^{-1}$: Tồn tại một $j$ sao cho $a_j = i$ vì $a$ là một hoán vị. Nên $(aba^{-1})_i = a_{b_{a^{-1}_i}} = a_{b_j}$.
2. $c'_1 \cdots c'_k$: Không làm mất đi tính tổng quát, ta cho $i$ là phần tử đầu tiên của $c'_1$, nghĩa là $i = a_{x_{i1}}$. Giờ nó sẽ được ánh xạ thành $a_{x_{i2}} = a_{b_{x_{i1}}} = a_{b_j}$

Vì cả hai đều cho ra cùng kết quả, ta có điều phải chứng minh.

Điều này nói lên rằng thao tác $aba^{-1}$ không gì khác là việc chuyển các nhãn của $b$ theo $a$.

Theo kết quả này, vì ta chỉ áp dụng hoán vị cho mọi thứ bên trong chu trình, ta có thể ánh xạ bất kỳ tích nào của các chu trình rời rạc tới bất kỳ tích nào khác của các chu trình rời rạc, miễn multiset của kích thước các chu trình không thay đổi.

Ta nói $b$ và $c$ liên hợp nếu tồn tại $a$ sao cho $c = aba^{-1}$ và gọi đây là thao tác liên hợp.

Do đó, điều này dẫn đến sự phân chia tất cả các hoán vị thành các lớp tương đương (sau khi xác minh một vài tiên đề), trong đó mọi thứ bên trong một lớp được liên hợp với mọi thứ khác trong lớp. Lưu ý rằng bất kỳ lớp tương đương nào cũng được xác định duy nhất bởi multiset của kích thước các chu trình. Các lớp tương đương này được gọi là các lớp liên hợp.

## Các topic khác

Phần này chủ yếu đề cập đến một số tài liệu tham khảo và nhằm mục đích cho người đọc biết về một số chủ đề trước đây chưa từng nghe thấy, nhưng có liên quan đến bài viết này. Trong tương lai có thể có những blog khác liên quan đến các chủ đề này, nhưng vẫn sẽ rất tốt nếu bạn biết sơ lược trước về chúng.

### Lý thuyết nhóm

Một tập các hoán vị kích thước $n$ tạo thành một "nhóm", ký hiệu là $S_n$, và hóa ra tất cả các nhóm hữu hạn có kích thước $n$ đều đẳng cấu với một nhóm con nào đó của $S_n$. Đây là lý do tại sao đã có rất nhiều nghiên cứu về hoán vị từ góc độ lý thuyết nhóm. Phần về kết hợp hoán vị dưới góc nhìn của lý thuyết nhóm là tốt nhất.

Việc phân tích rất nhiều trò chơi có thể được thực hiện bằng cách sử dụng lý thuyết nhóm, chẳng hạn như, [trò 15](https://en.wikipedia.org/wiki/15_Puzzle), trò Rubik, hình vuông Latin, vân vân...

Có một nhóm con các hoán vị tương ứng với tất cả các hoán vị chẵn. Nhóm này cũng đơn giản và có thể được sử dụng để cho biết kết quả về các trò chơi, ví dụ như trò 15.

### Đếm: Burnside, liệt kê Polya, số Stirling

Với các ý tưởng về lý thuyết nhóm, bổ đề Burnside và định lý liệt kê Polya xuất hiên và giúp đếm các lớp đối tượng (tương đương theo quan hệ nào đó) thay vì bản thân các đối tượng đó.

Số Stirling khá hữu ích khi đến những thứ liên quan đến hoán vị và xứng đáng có một bài viết riêng.

### Nén toạ độ

Ở trên, đặc biệt là trong phần về thứ tự, ta dùng mảng các phần tử riêng biệt và các hoán vị thay thế cho nhau. Bất cứ khi nào một cái gì đó chỉ phụ thuộc vào các quan hệ $\le$, $<$, $>$, $\ge$, $=$ giữa các phần tử chứ không phải bản thân các phần tử đó, thì việc thay thế các phần tử bằng thứ hạng của chúng là điều hợp lý. Trong trường hợp của các phần tử riêng biệt, "phiên bản nén" này trở thành một hoán vị.

### DP trên thành phần liên thông

Giống như ý tưởng thất bại về việc sinh hoán vị, ý tưởng đó cũng có thể được dùng cho DP. Bạn xem [ở đây](https://codeforces.com/blog/entry/92602) để biết thêm chi tiết.

### Young tableaus

Ý tưởng của Young tableaus liên quan chặt chẽ đến LIS và các khái niệm sắp xếp khác. Đây là một lý thuyết rất thú vị và [blog này](https://codeforces.com/blog/entry/98167) là một tài liệu tham khảo hay về nó.

### Thuật toán Schreier Sims

Giả sử ta có một nhóm con được tạo thành bởi một số hoán vị và ta muốn tìm kích thước nhóm con này. Thuật toán Schreier Sims giúp tìm kích thước, bạn có thể đọc tại [đây](https://codeforces.com/blog/entry/111290).

### Cây hoán vị

Có một loại cấu trúc dữ liệu khá thú vị có thể đáp ứng một số loại truy vấn trên hoán vị và mảng con. [Blog này](https://codeforces.com/blog/entry/78898) giới thiệu về nó.

## Luyện tập

Dưới đây chỉ là các bài tập được nhắc đến trong bài. Bạn có thể tìm thêm các bài hoán vị (chẳng hạn tìm bằng từ khoá "permutation" trên Codeforces) trên các trang Online Judge.

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [CSES - Planet Queries I](https://cses.fi/problemset/task/1750) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/CSES/CSES%201750.cpp) | 09/12/2023 | 
| [CSES - Planet Queries II](https://cses.fi/problemset/task/1160) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/CSES/CSES%201160.cpp) | 09/12/2023 |
| [Codeforces - Lucky Permutation](https://codeforces.com/contest/1768/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/1768/submission/236517320) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF1768-D2-D.cpp) | 09/12/2023 |
| [Codeforces - Square Root of Permutation](https://codeforces.com/contest/612/problem/E) | :white_check_mark: | [Submission](https://codeforces.com/contest/612/submission/236874904) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF612-D12-E.cpp) | 12/12/2023 |
