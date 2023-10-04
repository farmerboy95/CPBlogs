# Tổng và Giá trị kỳ vọng

## Nguồn

<img src="../../../assets/images/codeforces.png" width="16" height="16"/> [Sums and Expected Value - part 1](https://codeforces.com/blog/entry/62690)

<img src="../../../assets/images/codeforces.png" width="16" height="16"/> [Sums and Expected Value - part 2](https://codeforces.com/blog/entry/62792)

## Mở đầu

Đầu tiên thì bạn cần biết về xác suất và một chút về giá trị kỳ vọng. Về kỳ vọng tuyến tính thì mình có một bài dịch khá dễ hiểu ở [đây](../../Misc/probability/expected_value.md), các bạn có thể tìm đọc.

## Sơ bộ về giá trị kỳ vọng

Ví dụ ta mua một vé số giá 2 đô. Ta thắng giải 10 đô với xác suất là 10%, thắng giải 20 đô với xác suất 2%. Trung bình, nó sẽ cho ta $0.1 \cdot 10 + 0.02 \cdot 20 = 1.4$, nên ta sẽ mất nhiều hơn là được khi mua vé số. Giá trị trung bình vừa tính chính là giá trị kỳ vọng.

**Giá trị kỳ vọng (Expected Value - EV, có thể gọi tắt là kỳ vọng)** là giá trị trung bình của một biến cố / phép thử. Ví dụ, EV của số chấm khi ta tung một con xúc xắc 6 mặt là $3.5$:

$$E(X) = \sum_{\omega \in \Omega} P(\omega) \cdot X(\omega) = \frac{1}{6} \cdot 1 + \frac{1}{6} \cdot 2 + \ldots + \frac{1}{6} \cdot 6 = 3.5$$

Kỳ vọng tuyến tính (rất quan trọng):

$$E(X + Y) = E(X) + E(Y)$$

## Kỹ thuật "góp vào tổng"

Nếu ta muốn tính một tổng nào đó của nhiều cách / khả năng, ta có thể xem xét một phần tử (hay một số, một cạnh, một cặp gì đó) và đếm xem có bao nhiêu lần phần tử đó nằm trong kết quả cuối cùng.

## Các bài EV đơn giản

### Bài 1

Chọn 10 lá bài ngẫu nhiên trong một bộ bài 52 lá tiêu chuẩn. Tìm kỳ vọng số con át (ace) trong đó.

??? tip "Lời giải 1"
    Đây là cách của mình (farmerboy). Nếu bạn đã đọc bài viết kỳ vọng tuyến tính trên trang này thì bạn hẳn sẽ quen với cách giải sau đây.

    Gọi $E_i$ là kỳ vọng con át thứ $i$ được bốc ra khi kết thúc việc chọn 10 lá bài. Như vậy kết quả sẽ là $E_1 + E_2 + E_3 + E_4$, theo kỳ vọng tuyến tính, vì ta có 4 con át. Ta dễ dàng thấy được $E_i = 1 \cdot P_i + 0 \cdot (1 - P_i) = P_i$, hay là kỳ vọng bốc ra được con át thứ $i$ cũng là xác suất bốc ra được con át đó (sử dụng công thức kỳ vọng thì ta suy ra được nó).
    
    Thế thì số cách chọn ra một con át nào đó, ví dụ át cơ là bao nhiêu (và cũng áp dụng với các con át còn lại). Thì ta có

    $$E_i = P_i = \frac{1 \cdot \binom{51}{9}}{\binom{52}{10}} = \frac{10}{52} = \frac{5}{26}$$

    Như vậy kết quả sẽ là $E = E_1 + E_2 + E_3 + E_4 = 4 \cdot E_1 = 4 * \frac{5}{26} = \frac{10}{13}$.

??? tip "Lời giải 2"
    Đây là cách giải của Errichto.

    Ta có xác suất để bốc ra được một con át là $P = \frac{4}{52} = \frac{1}{13}$.

    Gọi $E_i$ là kỳ vọng bốc ra được con át trong lần bốc thứ $i$. Như vậy, theo kỳ vọng tuyến tính $E = \sum_{i=1}^{10} E_i$.

    Ở đây dễ thấy rằng $E_i = P_i$ (lý do tương tự lời giải 1), như vậy $E = \sum_{i=1}^{10} E_i = \sum_{i=1}^{10} P_i = 10 \cdot \frac{1}{13} = \frac{10}{13}$.

    Lưu ý là dù cho ở các lần bốc sau, xác suất bốc ra át có thể thay đổi nhưng ta vẫn có thể tính được như vậy dựa vào kỳ vọng tuyến tính.

    Nếu vẫn thấy khó hiểu vì sao xác suất ở sau vẫn là $\frac{1}{13}$, bạn có thể tưởng tượng rằng nếu mình lấy 10 lá bài lần lượt và mình không nói cho bạn biết 9 lá đầu tiên là gì, thì bạn có nghĩ xác suất lá thứ 10 là con át không phải $\frac{1}{13}$ hay không? Đây là lúc bạn nhận ra vấn đề.

### Bài 2

Giá của một chiếc TV là 1000 đô. Trong $N$ ngày tiếp theo, mỗi ngày giá của TV tăng 5 đô hoặc 10 đô (xác suất như nhau là 50%). Tính kỳ vọng giá TV sau $N$ ngày.

??? tip "Lời giải"
    Gọi $E_i$ là kỳ vọng giá tăng trong ở ngày thứ $i$, như vậy ta sẽ có kết quả là $E = \sum_{i=1}^{N} E_i$. Ta có mỗi ngày giá tăng như đề bài nên $E_i = 5 \cdot 0.5 + 10 \cdot 0.5 = 7.5$.

    Theo đề bài thì ngày nào giá cũng tăng như vậy nên các $E_i$ bằng nhau. Như vậy $E = \sum_{i=1}^{N} E_i = N \cdot E_1 = 7.5 \cdot N$.

    Lưu ý $E$ là giá tăng chứ không phải tổng giá, tổng giá thì đơn giản sẽ là $1000 + N \cdot 7.5$.

### Bài 3

Tung một con xúc xắc 6 mặt hai lần. Tìm kỳ vọng số lớn hơn trong hai lần tung đó.

??? tip "Lời giải"
    Bạn có thể vẽ ra một bảng cho ra số lớn hơn trong hai số kiểu như sau:
    ```
      | 1 2 3 4 5 6
    ---------------
    1 | 1 2 3 4 5 6
    2 | 2 2 3 4 5 6
    3 | 3 3 3 4 5 6
    4 | 4 4 4 4 5 6
    5 | 5 5 5 5 5 6
    6 | 6 6 6 6 6 6
    ```

    Mỗi trường hợp trong đây có xác suất là $\frac{1}{36}$. Như vậy theo công thức kỳ vọng $E(X) = \sum_{\omega \in \Omega} P(\omega) \cdot X(\omega)$, ta chỉ cần tính lần lượt tất cả các trường hợp trên rồi cộng lại với nhau là ra đáp án. Nhưng có vẻ hơi dài.

    Vậy ta có thể tính trong 36 trường hợp này thì có bao nhiêu số 1, 2, 3, ..., 6 không? Ví dụ tính số số 5 đi. Số cách chọn hai số không lớn hơn 5 là $5 \cdot 5 = 25$ cách. Nhưng đó là số cách chọn hai số không lớn hơn 5, có phải chắc chắn có 5 trong đó đâu? Ở đây, ta phải trừ số cách chọn hai số không lớn hơn 4 nữa là có đáp án, như vậy số cách chọn hai số có max là 5 là $5 \cdot 5 - 4 \cdot 4 = 5^2 - 4^2 = 9$. Tương tự ta có thể tính được đáp án của tất cả các số còn lại.

    Như vậy kết quả sẽ là

    $$E = \sum_{i=1}^6 i \cdot \frac{i^2 - (i-1)^2}{6^2} = \frac{\sum_{i=1}^6 i \cdot (i^2 - (i-1)^2)}{36} = \frac{161}{36} = 4.4722 \ldots$$

### Bài 4

Tung một con xúc xắc 6 mặt $N$ lần. Tìm kỳ vọng số lớn nhất trong $N$ lần tung đó.

??? tip "Lời giải"
    Tương tự bài trước, số cách chọn N số có max là $i$ sẽ là $i^N - (i-1)^N$. Không gian mẫu là $6^N$

    Như vậy kết quả là

    $$E = \sum_{i=1}^6 i \cdot \frac{i^N - (i-1)^N}{6^N} = \frac{\sum_{i=1}^6 i \cdot (i^N - (i-1)^N)}{6^N}$$

    Đây cũng là bài 454C trên Codeforces. Code sẽ ở phần Luyện tập nhé.

### Bài 5

Bạn dạy trong một lớp 20 người. Khi ai đó có sinh nhật, bạn phải cho cả lớp chơi game thay vì học bài mới ngày hôm đó. Có thể một số học sinh có ngày sinh nhật trùng nhau, nên sẽ có ít hơn 20 ngày bị lãng phí trong một năm phải không? Tìm kỳ vọng số ngày lãng phí trong năm.

??? tip "Lời giải"
    Ta gọi $E_i$ là kì vọng một ngày thứ $i$ là ngày sinh nhật của bất kỳ học sinh nào trong lớp. Như vậy kỳ vọng số ngày lãng phí trong năm sẽ là $E = \sum_{i=1}^{365} E_i$. Vì kì vọng các ngày bằng nhau nên $E = \sum_{i=1}^{365} E_i = 365 \cdot E_1$.

    Vì $E_i$ là kỳ vọng ngày thứ $i$ là sinh nhật ai đó, nên nó chỉ có đúng hoặc sai (1 hoặc 0), nên $E_i = P_i$, cũng là xác suất ngày thứ $i$ là sinh nhật ai đó. Tính $P_i$ như thế nào?

    Tính thẳng $P_i$ có vẻ khó, giờ ta thử tính $1 - P_i$, hay còn gọi là xác suất để ngày thứ $i$ không phải sinh nhật ai cả, xem sao. Xác suất đó sẽ là $(1 - \frac{1}{365})^{20}$, vì với mỗi học sinh, ta chỉ cần chọn ngày khác với ngày $i$ là xong. Vậy $1 - P_i = (1 - \frac{1}{365})^{20} = (\frac{364}{365})^{20}$. Suy ra $P_i = 1 - (\frac{364}{365})^{20} \approx 0.05339$

    Như vậy $E = \sum_{i=1}^{365} E_i = 365 \cdot E_1 = 365 \cdot (1 - (\frac{364}{365})^{20}) \approx 19.4879$ ngày.

### Bài 6

Cho một đồng xu công bằng (xác suất tung ra mặt ngửa bằng xác suất tung ra mặt sấp). Tìm kỳ vọng số lần tung để ra mặt ngửa.

??? tip "Lời giải"
    Gọi $E_i$ là số lần tung đồng xu để ra mặt ngửa sau khi đã tung $i$ lần. $E_0$ là đáp án của chúng ta. Ta thấy rằng nếu tung lần đầu được mặt sấp, thì kỳ vọng sau đó vẫn sẽ bằng kỳ vọng khi chưa tung lần nào, nghĩa là $E_1 = E_0$.

    Theo công thức kỳ vọng, ta có $E_0 = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot (1 + E_0)$. Nghĩa là, khi tung được mặt ngửa ở lần đầu, ta đã có mặt ngửa rồi nên không tung nữa, số lần tung là 1, còn khi tung ra mặt sấp, ta mất một lần tung và phải tung tiếp. Chuyển $E_0$ về 1 vế và tính, ta sẽ có $E_0 = 2$.

### Bài 7

Cho một đồng xu công bằng. Tìm kỳ vọng số lần tung để ra tổng cộng hai lần mặt ngửa.

??? tip "Lời giải"
    Sau khi tung ra được 1 lần mặt ngửa, kỳ vọng số lần tung để ra mặt ngửa thứ hai là bao nhiêu? Chính xác, là 2 lần, như bài trước. Thế thì kỳ vọng số lần tung để ra lần mặt ngửa đầu tiên là bao nhiêu? Vẫn là 2.

    Như vậy $E(\text{2 ngửa}) = E(\text{1 ngửa} + \text{1 ngửa}) = E(\text{1 ngửa}) + E(\text{1 ngửa}) = 2 + 2 = 4$, theo kỳ vọng tuyến tính.

### Bài 8

Cho một đồng xu công bằng. Tìm kỳ vọng số lần tung để ra tổng cộng hai lần mặt ngửa liên tiếp.

??? tip "Lời giải"
    Gọi $E_i$ kỳ vọng số lần tung để từ $i$ măt ngửa sau cùng ta có $i+1$ mặt ngửa sau cùng. $E_0 + E_1$ là đáp án của chúng ta. Rõ ràng ta có $E_2 = 0$, vì lúc này ta đã có 2 mặt ngửa liên tiếp.

    Ta có $E_0 = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot (1 + E_0)$. Giải ra ta sẽ có $E_0 = 2$.

    Lại có $E_1 = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot (1 + E_0 + E_1)$. Ở đây nghĩa là nếu tung ra mặt ngửa tiếp thì ta đến trạng thái 2 mặt ngửa liên tiếp, ngược lại ta tốn một lượt tung và phải cần $E_0$ lần tung để quay lại trạng thái 1 mặt ngửa, sau đó tung $E_1$ lần để đến trạng thái 2 mặt ngửa. Giải cái này ra ta sẽ có $E_1 = 4$.

    Như vậy kết quả là $E_0 + E_1 = 2 + 4 = 6$.

### Bài 9

12 đội, trong đó có đội của bạn, chơi trong một giải bóng chuyền. Các đội được chia ra làm 4 bảng, mỗi bảng 3 đội. Trong mỗi bảng, các đội đấu vòng tròn một lượt và hai đội đầu bảng sẽ vào vòng knockout. Nếu có các đội bằng điểm và bằng tất cả các chỉ số khác, hai đội ngẫu nhiên sẽ đi tiếp. Vòng knockout có tứ kết, bán kết và chung kết. Trong mỗi trận, xác suất một đội thắng là 50%, không có kết quả hoà.

Tìm xác suất đội của bạn thắng giải này. Tìm kỳ vọng số trận thắng của đội bạn. Tìm kỳ vọng số trận thắng của đội bạn, với điều kiện đội bạn thắng giải (nghĩa là tìm kỳ vọng số trận thắng của đội thắng cuộc).

??? tip "Lời giải"
    Do các đội là như nhau trong một bảng (symmetry - cân đối) nên xác suất để một đội vượt qua vòng bảng là $\frac{2}{3}$ (tương tự xác suất bị loại là $\frac{1}{3}$). Đội của bạn cần thắng tứ kết, bán kết và chung kết để vô địch, với xác suất là 50% mỗi trận, nên xác suất thắng giải là

    $$P(\text{thắng giải}) = \frac{2}{3} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{12}$$

    Kỳ vọng số trận đấu của đội bạn sẽ bằng tổng các tích số trận được thi đấu với xác suất của mỗi trường hợp, theo công thức kỳ vọng, như vậy

    $$\begin{align}
    E(\text{số trận của đội}) &= P(\text{đội bị loại sau vòng bảng}) \cdot 2 + P(\text{đội thua tứ kết}) \cdot 3 + P(\text{đội thua bán kết}) \cdot 4 + P(\text{đội thua chung kết}) \cdot 5 + P(\text{đội thắng chung kết}) \cdot 5\\
    &= \frac{1}{3} \cdot 2 + \frac{2}{3} \cdot \frac{1}{2} \cdot 3 + \frac{2}{3} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot 4 + \frac{2}{3} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot 5 + \frac{2}{3} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot 5\\
    &= \frac{19}{6}\\
    \end{align}$$

    Vậy còn kỳ vọng số trận thắng của đội vô địch? Ta có

    $$E(\text{số trận thắng của đội vô địch}) = E(\text{số trận thắng sau vòng bảng}) + E(\text{số trận thắng vòng knockout})$$

    Số trận thắng vòng knockout thì rõ ràng là 3 vì cần phải thắng hết các trận đó mới vô địch.

    Giờ ta chỉ cần tìm kỳ vọng số trận thắng vòng bảng với **điều kiện** là đội này vượt qua vòng bảng, gọi giá trị này là $E_2$, thì $E = 3 + E_2$. Ta có

    $$E_2 = 0 \cdot P(0|\text{đi tiếp}) + 1 \cdot P(1|\text{đi tiếp}) + 2 \cdot P(2|\text{đi tiếp})$$

    Không có đội nào có thể đi tiếp khi không thắng trận nào ở vòng bảng, nên $P(0|\text{đi tiếp}) = 0$. Suy ra $P(1|\text{đi tiếp}) + P(2|\text{đi tiếp}) = 1$.

    Theo định lý Bayes,

    $$P(2|\text{đi tiếp}) = \frac{P(\text{đi tiếp}|2) \cdot P(2)}{P(\text{đi tiếp})}$$

    Ta biết rằng $P(2) = \frac{1}{4}$ và $P(\text{đi tiếp}) = \frac{2}{3}$. Ta cũng biết rằng nếu thắng 2 trận thì sẽ chắc chắn đi tiếp, nên $P(\text{đi tiếp}|2) = 1$. Vậy

    $$P(2|\text{đi tiếp}) = \frac{P(\text{đi tiếp}|2) \cdot P(2)}{P(\text{đi tiếp})} = \frac{1 \cdot \frac{1}{4} }{\frac{2}{3} } = \frac{3}{8}$$

    Nên $P(1|\text{đi tiếp}) = 1 - P(2|\text{đi tiếp}) = 1 - \frac{3}{8} = \frac{5}{8}$.

    Vậy $E_2 = 1 \cdot \frac{5}{8} + 2 \cdot \frac{3}{8} = \frac{11}{8}$

    Suy ra $E = E_2 + 3 = \frac{11}{8} + 3 = \frac{35}{8}$.

    Lưu ý rằng đây là kỳ vọng có điều kiên, điều kiện ở đây là đội phải qua vòng bảng, nó khác với kỳ vọng bình thường, nơi bạn có thể tính tất cả các trường hợp. Ở đây ta không thể đặt được biến ngẫu nhiên nào mà không có điều kiện qua vòng bảng.

## Các bài tập cho kỹ thuật "góp vào tổng"

### Bài 1

Cho dãy số độ dài $N$ ($N \le 10^5$), đếm các bộ ba $i < j < k$ sao cho $a_i < a_j > a_k$.

**Bonus**: Đếm các đoạn zig-zag độ dài $10$, nghĩa là $i_1 < i_2 < \ldots < i_{10}$ sao cho $a[i_1] < a[i_2] > a[i_3] < a[i_4] > \ldots < a[i_{10}]$.

??? tip "Lời giải"
    Ở đây thì bạn có thể duyệt $j$. Sau đó tìm số các bộ ba chứa $a_j$ (phần tử ở giữa). Số bộ ba chứa $a_j$ ở giữa sẽ là số các số nhỏ hơn $a_j$ nằm bên trái nó và số các số nhỏ hơn $a_j$ nằm bên phải nó. Ta có thể tìm số các số nhỏ hơn này với BIT (Binary Indexed Tree - cây chỉ số nhị phân) trong $O(\log n)$.

    **Bonus**: Nó sẽ phức tạp hơn một chút. Về cơ bản, bạn định nghĩa $dp[i][j]$ là số các bộ zig-zag độ dài $j$ khi xét trong đoạn $[1..i]$ với $a_i$ là phần tử cuối cùng của bộ đó. Với mỗi $j$ ta sẽ tính hết $dp[i][j]$. Ví dụ $j$ là $4$, tại $dp[i][j]$ ta cần tổng các $dp[k][j-1]$, với $k < i$ và $a[k] < a[i]$, để tổng này thì một lần nữa ta lại dùng BIT, với giá trị tại node $k$ sẽ là $dp[k][j-1]$. Lưu ý là qua mỗi $j$ thì dấu so sánh lại đảo nên cũng cần thay đổi một chút trong BIT. Độ phức tạp sẽ là $O(n \log n)$

### Bài 2

Cho một cây có $N$ đỉnh ($N \le 10^5$), tìm tổng tất cả các độ dài các đường đi (Giải không dùng DP phức tạp hoặc centroid).

**Bonus**: Tính tổng bình phương độ dài các đường đi.

??? tip "Lời giải"
    Xét một cạnh $E(u, v)$ trên cây, gọi độ dài của nó là $e$. Vậy $e$ sẽ đóng góp bao nhiêu trong kết quả? $e$ đóng góp vào kết quả khi có đường đi chứa cạnh $E$. Vậy có bao nhiêu đường đi đi qua cạnh $E$? Đó sẽ là số đỉnh bên phía $u$ trên cây nhân với số đỉnh bên phía $v$ trên cây. "Bên phía" $u$ nghĩa là đỉnh có đường đi ngắn nhất đến $u$ không qua cạnh $E$.

    Gọi $num[u]$ là số đỉnh trong cây con gốc $u$. Với một cạnh $E(u, v)$ ($u$ là đỉnh cha của $v$). Số đỉnh bên phía $v$ rõ ràng là $num[v]$. Còn số đỉnh bên phía $u$ sẽ là các đỉnh còn lại, nghĩa là $N - num[v]$. Như vậy $e$ đóng góp vào kết quả là $e \cdot num[v] \cdot (N - num[u])$. Xét tất cả các cạnh, lấy tổng là sẽ có được đáp án.

    **Bonus**: Đầu tiên ta tính tổng bình phương tất cả các đường đi từ gốc của cây, gọi nó là $S$. Ta DFS từ gốc, và khi di chuyển, ta sẽ duy trì $S$ sao cho khi đến đỉnh $u$ nào đó, $S$ sẽ là tổng bình phương tất cả các đường đi từ đỉnh $u$. Sau đó thêm $S$ vào đáp án cuối cùng với mỗi đỉnh $u$.

    Lý thuyết là như vậy, còn làm sao để duy trì? Khi đi từ một đỉnh cha $u$ xuống đỉnh con $v$, các đỉnh nằm trong cây con gốc $v$ sẽ bị giảm giá trị bình phương đường đi từ $v$ đến chúng, còn các đỉnh còn lại sẽ tăng giá trị, mà cụ thể là tăng bao nhiêu?

    Xét giá trị bị giảm đi, giả sử một đường đi từ $u$ đến một đỉnh nào đó trong cây con gốc $v$ có tổng (không bình phương) là $x$, như vậy tổng bình phương là $x^2$. Gọi giá trị cạnh $E(u, v)$ là $e$. Khi đến đỉnh $v$, độ dài đường đi này sẽ là $x - e$, và bình phương của nó là $(x - e)^2$. Bình phương độ dài đường đi sẽ giảm đi $x^2 - (x - e)^2 = 2ex - e^2$. Vậy ta cần bớt đi $2ex - e^2$ từ $x^2$ để có $(x - e)^2$. Ta gọi $numEdges[u]$ là số cạnh trong cây con gốc $u$, và $sum[u]$ là tổng tất cả các cạnh trong cây con gốc $u$. Như vậy tổng giá trị cần bớt từ $S$ sẽ là: $2e \cdot sum[v] - numEdges[v] \cdot e^2$.

    Xét giá trị được tăng lên, tương tự như trên, bình phương độ dài tăng lên là $(x + e)^2 - x^2 = e^2 + 2ex$. Vậy ta cần tăng $e^2 + 2ex$ từ $x^2$ để có $(x + e)^2$. Tuy nhiên ở đây không phải cây con nên sẽ hơi khác một chút. Cụ thể, đây là cây ban đầu không chứa cây con gốc $v$. Tổng giá trị cần tăng lên từ $S$ sẽ là $2e \cdot (sum[root] - sum[v]) + (numEdges[root] - numEdges[v]) \cdot e^2$.

    Sau khi có kết quả là $S$ thì cần lưu ý là một đường đi ở đây đã được tính 2 lần, lần đầu từ 1 đầu của đường đi, lần hai là từ đầu còn lại. Nên ta chia kết quả cho 2 để có được đáp án cuối cùng.

### Bài 3

Có $N$ cuộc thi, cuộc thi thứ $i$ có giải thưởng là $a_i$. Bạn có thể thắng một cuộc thi với xác suất 50%. Tìm kỳ vọng số tiền thắng được.

Bài toán tương đương: Tìm tổng giải trên $2^N$ khả năng có thể xảy ra, in đáp án lấy dư với $10^9 + 7$. (Đáp án ở đây chia $2^N$ sẽ ra đáp án câu trên).

??? tip "Lời giải"
    Với bài toán kỳ vọng, ta dễ dàng tính được kỳ vọng tổng số tiền thắng được sẽ bằng tổng kỳ vọng số tiền thắng được ở mỗi cuộc thi, theo kỳ vọng tuyến tính. Mà kỳ vọng số tiền thắng được ở cuộc thi $i$ sẽ là $\frac{1}{2} \cdot a_i$, nên kết quả sẽ là $E = \sum_{i = 1}^N E_i = \frac{1}{2} \cdot \sum_{i=1}^N a_i$.

    Tuy nhiên, khi đọc vào bài toán tương đương, ta cần tìm xem với mỗi giải thưởng $a_i$, nó sẽ đóng góp vào kết quả cuối cùng là bao nhiêu. Đó sẽ là tích của $a_i$ với số lần xuất hiện của $a_i$ trong $2^N$ khả năng có thể xảy ra. Mà ta biết là $a_i$ sẽ xuất hiện trong $2^{N-1}$ lần trong $2^N$ khả năng. Như vậy giải thưởng $a_i$ sẽ đóng góp $2^{N-1} \cdot a_i$ vào kết quả cuối cùng. Tương tự với các giải thưởng khác, ta sẽ có tổng giải là $2^{N-1} \cdot \sum_{i=1}^N a_i$. Đáp án ở đây chia $2^N$ sẽ ra đáp án câu trên, theo định nghĩa kỳ vọng.

### Bài 4

Đây là bài Math Encoder của Google Kickstart 2017 Round B

Cho dãy độ dài $N$ ($N \le 2000$ hay $N \le 10^5$). Chọn ngẫu nhiên một trong $2^N-1$ tập con không rỗng. Tìm kỳ vọng chênh lệch số lớn nhất và số bé nhất trong tập được chọn.

Bài toán tương đương: Tìm tổng chênh lệch của tất cả các tập con không rỗng, tính kết quả lấy dư với $10^9+7$.

??? tip "Lời giải"
    Đầu tiên, vì thứ tự ở đây không quan trọng lắm, vì ta chọn tất cả các tập con, nên ta có thể sắp xếp tăng dần dãy ban đầu.

    Với bài tính kì vọng, ta cần tìm $E(max - min)$, mà theo kì vọng tuyến tính, $E(max - min) = E(max) - E(min)$. Tính 2 kỳ vọng này thì tương tự nhau. Ví dụ với tính $E(max)$, làm sao để tính xác suất của một số $x$ nào đó là giá trị lớn nhất? Do đã sắp xếp nên $x$ sẽ là một nhóm kề nhau trên dãy. Ta sẽ không chọn các phần tử lớn hơn $x$, gọi số phần tử lớn hơn $x$ là $M$ thì xác suất ở đây sẽ là $\frac{1}{2^M}$. Với các phần tử nhỏ hơn $x$, ta không có yêu cầu gì. Giờ đến việc chọn $x$, ta cần ít nhất một $x$ trong dãy đã chọn, với số phần tử bằng $x$ là $K$ thì xác suất chọn ra được ít nhất một $x$ là $\frac{2^K-1}{2^K}$. Như vậy xác suất để $x$ là số lớn nhất là $\frac{1}{2^M} \cdot \frac{2^K-1}{2^K}$. Tuy nhiên, ta đang giả sử là xác suất chọn một phần tử là $\frac{1}{2}$, khác với việc chọn một $2^N - 1$ tập con. Cái ta giả sử là tương đương với việc chọn $2^N$ tập con. Như vậy xác suất này cần nhân với $2^N$ rồi chia $2^N-1$ mới chính xác. Tính tổng tất cả các $x$ khác nhau trong dãy sẽ ra được $E(max)$. Tương tự ta tính được $E(min)$ và cuối cùng là đáp án.

    Với bài tương đương, ta có thể chọn ra 2 phần tử bất kỳ trong dãy đã sắp xếp, thì sẽ có bao nhiêu lần chênh lệch giữa chúng được đưa vào đáp án. Giả sử có $P$ phần tử nằm giữa hai phần tử đã chọn, thì chênh lệch giữa chúng sẽ đóng góp $2^P$ lần vào đáp án. Như vậy ta sẽ có được một lời giải $O(N^2)$ ở đây. Nếu $N \le 10^5$ thì sao? Để ý rằng đáp án sẽ tăng lên $2^P \cdot (a_r - a_l) = 2^P \cdot a_r - 2^P \cdot a_l$. Ta có thể tách riêng để tính số lần cộng $a_i$ và số lần trừ $a_i$. Cụ thể, ta sẽ cộng $a_i$ được $2^{i-1} - 1$ lần, và trừ $a_i$ đi $2^{n-i} - 1$ lần. Ta có thể giải bài này trong $O(N)$.

### Bài 5

Đây là bài Imbalanced Array của Codeforces Educational Round 23

Tương tự bài trước, nhưng chọn ngẫu nhiên trong $\frac{N \cdot (N+1)}{2}$ đoạn con.

Bonus: Làm trong $O(N)$ nếu input chứa hoán vị các số từ $1$ đến $N$.

??? tip "Lời giải"
    Ta có thể giải cả hai trong $O(N)$.

    Với mỗi đoạn, ta muốn biết giá trị lớn nhất $Max$ và giá trị nhỏ nhất $Min$. Sau đó ta thêm $Max - Min$ vào đáp án cuối cùng. Làm tương tự với tất cả các đoạn thì ta sẽ có kết quả cuối cùng. Ta có thể làm trâu như vậy trong $O(N^3)$ hoặc $O(N^2)$ với RMQ.

    Nhưng thế thì chậm quá. Giờ ta sẽ đi một hướng khác. Câu hỏi sẽ là: Với một vị trí $i$ nào đó, $a[i]$ sẽ là $Max$ bao nhiêu lần. Hay chính xác hơn là, có bao nhiêu đoạn con nhận phần tử thứ $i$ là $Max$? Nếu ta giải được bài này, thì cũng có thể làm tương tự với $Min$.

    Giả sử các phần tử đều khác nhau đôi một (bài bonus). Để phần tử thứ $i$ là giá trị lớn nhất trong đoạn, ta cần xem rằng ta có thể mở rộng đoạn (ban đầu chỉ chứa $a[i]$) về bên trái bao xa, và về bên phải bao xa, mà $a[i]$ vẫn là giá trị lớn nhất. Bên trái thì ta có thể đi cho đến khi gặp một phần tử lớn hơn hoặc đến hết dãy. Bên phải thì ta có thể đi cho đến khi gặp một phần tử lớn hơn hoặc đến hết dãy. Gọi các vị trí này là $l$ và $r$. Như vậy, $a[i]$ có thể đóng góp $(r - i) * (i - l) * a[i]$ vào kết quả cuối cùng. Tương tự với giá trị $Min$, sự khác nhau chỉ là đi đến khi gặp phần tử nhỏ hơn. Ở đây $a[i]$ có thể đóng góp $-(r - i) * (i - l) * a[i]$ vào kết quả cuối cùng.

    Việc tìm giá trị gần nhất lớn / nhỏ hơn bên trái / phải phần tử thứ $i$ có thể được giải bằng kỹ thuật Sliding Window trong $O(N)$, sau đó lưu các vị trí này vào 4 mảng khác nhau.

    Nếu các phần tử không khác nhau thì sao? Nếu làm như trên ta có thể đếm phải những kết quả trùng nhau. Cách tốt nhất để làm ở đây là:

    - Tìm vị trí gần nhất bên trái sao cho giá trị ở đó lớn hơn hoặc BẰNG $a[i]$.
    - Tìm vị trí gần nhất bên phải sao cho giá trị ở đó lớn hơn $a[i]$ (như ở bài khác nhau).
    - Tìm vị trí gần nhất bên trái sao cho giá trị ở đó lớn hơn hoặc BẰNG $a[i]$.
    - Tìm vị trí gần nhất bên phải sao cho giá trị ở đó lớn hơn $a[i]$ (như ở bài khác nhau).
    
    Làm vậy sẽ loại bỏ được các giá trị trùng nhau. Kết lại, ta có thể giải bài này trong $O(N)$.

### Bài 6

Cho một đa giác lồi $N$ đỉnh ($N \le 2000$ hay $N \le 10^5$). Chọn một tập con ngẫu nhiên các đỉnh, nó sẽ tạo thành một đa giác lồi nhỏ hơn. Tính kỳ vọng chu vi của đa giác mới này.

Đây là một phiên bản dễ hơn của bài Randomizer của Codeforces Round 313 Div 1 D. Về bài này, ta được cho một đa giác lồi không có 3 đỉnh nào thẳng hàng. Ta phải chọn một tập con ngẫu nhiên có diện tích khác 0 (nghĩa là ít nhất 3 đỉnh). Tính kỳ vọng số toạ độ nguyên nằm hẳn bên trong đa giác mới.

??? tip "Lời giải"
    **Với bài đầu tiên**, ta cần tính kỳ vọng chu vi (perimeter) của đa giác mới, hay $E(perimeter)$. Mà ta biết rằng chu vi bằng tổng độ dài các cạnh của đa giác, nghĩa là $E(perimeter) = E(\sum L_i) = \sum E(L_i)$, trong đó $L_i$ là độ dài một cạnh thứ $i$ nào đó trong đa giác. Như vậy có nghĩa là, với mọi cạnh, nếu nó xuất hiện trong đa giác, độ dài của nó sẽ được thêm vào trong kết quả. Việc ta cần làm là duyệt các cạnh có thể có, kỳ vọng độ dài của nó trong đáp án là tích của độ dài cạnh với xác suất nó nằm trong đáp án. 
    
    Xét hai đỉnh thứ $i$ và $j$ trong input, xác suất chọn ra được cả hai đỉnh là $\frac{1}{4}$. Ta có thể thấy cạnh này (nối hai đỉnh thứ $i$ và $j$ trong input) sẽ chia đa giác ra làm hai phần, thì ở đây, để chọn ra được một đa giác nào đó, ta cần chọn thêm (ít nhất một) đỉnh ở một trong hai phần, và hoàn toàn bỏ qua phần còn lại. Ta sẽ xem một phần có $j - i - 1$ đỉnh ($j > i$) và phần còn lại có $n - (j - i + 1)$ đỉnh. Vây xác suất để cạnh này nằm trong đa giác là

    $$P = \frac{1}{4} \cdot \left( \left(\frac{1}{2}\right)^{j-i+1} \cdot \frac{2^{n-(j-i+1)} - 1}{ 2^{n-(j-i+1)} } + \left(\frac{1}{2}\right)^{n-(j-i+1)} \cdot \frac{2^{j-i+1} - 1 }{2^{j-i+1} } \right)$$

    Ok, ta đã giải được nhưng cách này tốn $O(N^2)$. Với $N$ lớn, ta cần để ý rằng với $i$ và $j$ nằm quá xa nhau ($j - i + 1 > 60$), $\left(\frac{1}{2}\right)^{j-i+1}$ sẽ rất rất nhỏ. Cho nên ở đây, với mỗi $i$, **ta chỉ cần duyệt các $j$ cách nó trong tầm $60$ đơn vị là được**. Cho nên ta có thể giải như cách trên nhưng bỏ qua các xác suất quá nhỏ, trong $O(N)$. Thêm một điểm nữa, ta không xét lại các cặp $(i, j)$ đã xét nhé, khi $N$ nhỏ rất có thể ta sẽ xét các cặp trùng nhau.

    **Với bài Randomizer**, đầu tiên ta cần biết chút về [**định lý Pick**](https://en.wikipedia.org/wiki/Pick%27s_theorem). Giả sử ta có một đa giác trên hệ toạ độ $Oxy$, với các đỉnh của nó có hoành độ và tung độ là số nguyên. Gọi $i$ là số các đỉnh có toạ độ nguyên nằm hoàn toàn trong đa giác, gọi $b$ là số đỉnh có toạ độ nguyên nằm trên đa giác (nằm trên cả đỉnh và cạnh). Định lý Pick cho ta công thức tính diện tích $A$ của đa giác là

    $$A = i + \frac{b}{2} - 1$$

    Từ đó ta sẽ có:

    $$i = A - \frac{b}{2} + 1$$
    
    Rõ ràng ta cần tính $E(i)$. Theo kỳ vọng tuyến tính, ta sẽ có như sau:

    $$\begin{align}
    E(i) &= E(A - \frac{b}{2} + 1)\\
    &= E(A) - \frac{E(b)}{2} + 1\\
    \end{align}$$

    Ta cùng tính kỳ vọng các đỉnh trên cạnh trước. Với một cạnh nối đỉnh $(0, 0)$ và đỉnh $(x, y)$, ta có thể tính số đỉnh nguyên trên cạnh là $GCD(x, y) + 1$. Nhưng để cho đơn giản, ta sẽ không tính một trong hai đầu mút của cạnh. Lý do ở đây là khi tạo thành một đa giác, số đỉnh nằm trên các cạnh
    chính là tổng trên các cạnh riêng lẻ nhưng không tính một trong hai đầu mút. Bạn có thể vẽ ra để thấy. Ở đây, vì tổng các đỉnh nằm trên cạnh sẽ bằng tổng trên các cạnh riêng lẻ, nên theo kỳ vọng tuyến tính, ta có thể tính kỳ vọng số đỉnh nằm trên mỗi cạnh có thể tạo thành. 
    
    Xét cạnh nối hai đỉnh $i$ và $j$ ($i < j$), ta cần tính xác suất cạnh này xuất hiện trong một đa giác nào đó. Không gian mẫu của việc chọn một đa giác ít nhất 3 đỉnh là sẽ là $2^n - 1 - n - \frac{n(n-1)}{2}$. Điều này là vì ta cần chọn ít nhất 3 đỉnh nên phải loại các trường hợp chọn 0, 1 và 2 đỉnh ra. Để hai đỉnh được chọn trở thành cạnh thì một trong hai phía phải không có đỉnh nào, ta chọn xoá phía có $j - i - 1$ đỉnh, số cách chọn sẽ là $2^{n - (j - i - 1 + 2)} - 1 = 2^{n - (j - i) + 1} - 1$. Ta xoá một phía để không phải xử lý phía còn lại nếu chọn phải cặp $(j, i)$ về sau.
    Tuy nhiên, tương tự bài trên, khi $j - i > 60$ thì xác suất này sẽ trở nên rất nhỏ, nên ta chỉ cần xét các cặp cách nhau không quá 60 là được.

    Như vậy xác suất để chọn ra một cạnh chứa hai đỉnh, đỉnh thứ $i$ và đỉnh thứ $i + k$ là:

    $$\frac{2^{n-k-1} - 1 }{2^n - 1 - n - \frac{n(n-1)}{2} } = \frac{1 - \frac{1}{2^{n - k - 1} } }{2^{k+1} - (n^2 + n + 2) \cdot \frac{1}{2^{n-k} } }$$

    Lưu ý, biểu thức phía sau là để dễ tính hơn khi code.

    Thế còn diện tích thì sao? Khi các đỉnh $(x_i, y_i)$ được sắp xếp theo chiều ngược chiều kim đồng hồ, ta tính được diện tích của đa giác tạo bởi nó như sau:

    $$S = \frac{1}{2} \cdot (x_1y_2 - x_2y_1 + x_2y_3 - x_3y_2 + \ldots + x_{n-1}y_{n} - x_{n}y_{n-1} + x_{n}y_{1} - x_{1}y_{n})$$

    Đây là công thức tính diện tích dựa trên tích có hướng. Vì sao nó đúng thì bạn có thể xem ở [đây](https://math.stackexchange.com/questions/492407/area-of-an-irregular-polygon). Về cơ bản, với cạnh $(i, j)$ ($j$ nằm sau $i$ theo chiều kim đồng hồ), nó sẽ thêm vào đáp án (không tính phần chia 2), một khoảng là $x_iy_j - x_jy_i$. Đến đây thì theo kỳ vọng tuyến tính thì bạn cũng có thể làm tương tự như trên với cùng xác suất.

### Bài 7

Cho $N$ điểm ($B \le 200$ hay $N \le 2000$), không có 3 điểm thẳng hàng. Mỗi điểm biến mất với xác suất 50%. Tìm kỳ vọng kích thước bao lồi của các điểm còn lại (Kích thước bao lồi là số đỉnh của bao lồi).

??? tip "Lời giải"
    Tình cờ là trong một đa giác lồi, số đỉnh bằng số cạnh của đa giác đó (không tính trường hợp có một hoặc hai đỉnh được chọn, bạn có thể xử lý riêng hai trường hợp này). Nên kỳ vọng số đỉnh của bao lồi cũng sẽ là kỳ vọng số cạnh của bao lồi. Mà như bài 6 thì với mỗi cạnh, đường thẳng ứng với cạnh sẽ chia mặt phẳng ra làm 2 phần, trái ($L$) và phải ($R$). Xác suất để cạnh $ij$ đó nằm trong bao lồi (có ít nhất 3 đỉnh là):

    $$P_{ij} = \frac{1}{4} \cdot \left( (\frac{1}{2})^L \cdot \frac{2^R-1}{2^R} + (\frac{1}{2})^R \cdot \frac{2^L-1}{2^L} \right)$$

    Để tính $L$ và $R$ thì bạn có thể làm cách trâu với $O(N^3)$, hoặc với $O(N^2 \log N)$ bằng cách sau, với mỗi đỉnh $i$, sắp xếp các đỉnh còn lại theo góc và duyệt $j$ theo góc, như vậy $L$ và $R$ sẽ không cần phải tính lại.

    Một cách giải khác cho bài này là với mỗi đỉnh, ta tính xác suất của đỉnh đó trở thành một đỉnh trên bao lồi (cũng là kỳ vọng luôn), mà cách này thì hơi khó một tí, ta sẽ không bàn đến ở đây.

### Bài 8

Cho dãy độ dài $N$ ($N \le 2000$ hay $N \le 10^5$). Ta sẽ thực hiện thao tác sau $N-1$ lần: xoá phần tử đầu hoặc cuối, xác suất 50% đầu và 50% cuối. Tìm kỳ vọng giá trị của số còn lại.

??? tip "Lời giải"
    Dễ thấy kỳ vọng giá trị của số còn lại bằng tổng kỳ vọng từng số xuất hiện trong đáp án. Hay nói cách khác, $E = \sum_{i} P_i \cdot a_i$. Trong đó $P_i$ là xác suất mà số thứ $i$ được chọn. Vậy làm sao tính được số này, gọi $L$ là số số bên trái $i$, $R$ là số số bên phải $i$. Thì số cách xoá để sau cùng có được $i$ là $\binom{L+R}{L}$, nghía là ta tiến hành xoá $L + R$ lần, trong đó có $L$ lần xoá bên trái. Với $i$ thì ta đã biết $L$ và $R$ là bao nhiêu rồi, nên $P_i = \frac{\binom{N-1}{i-1}}{2^{N-1}}$. Xác suất này có phần tử số hơi lớn nên bạn cần cẩn thận khi code.

## Lý thuyết kỳ vọng, phần 2

Tung một con xúc xắc 6 mặt. Nhớ rằng, kỳ vọng bình phương của số trên xúc xắc khác bới bình phương của kỳ vọng:

$$E(X^2) = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = 15.1666...$$

$$E(X)^2 = (\frac{1 + 2 + 3 + 4 + 5 + 6}{6})^2 = 3.5^2 = 12.25$$

Hai biến cố gọi là *độc lập* khi kết quả của một biến cố không ảnh hưởng đến phân bố xác suất của biến cố còn lại. Kết quả tung hai xúc xắc (hoặc tung một xúc xắc hai lần) là độc lập, nhưng lượng mưa và sức gió thì phụ thuộc nhau. Tuy nhiên, tính tuyến tính thì luôn đúng:

$$E(X + Y) = E(X) + E(Y)$$

Công thức quan trọng khác là $E(X \cdot Y) = E(X) \cdot E(Y)$ chỉ đúng với biến cố **độc lập**. Nên kỳ vọng của tích các số sau hai lần tung xúc xắc là $3.5^2$, nhưng không thể sử dụng $E(X \cdot X) = E(X) \cdot E(X)$, vì $X$ và $X$ không độc lập.

## Ordered pairs (giải thích bình phương)

Bình phương kích thước của một tập bằng với số **ordered pairs** của các phần tử trong tập. Nên ta có thể duyệt các cặp và với mỗi cặp ta tính góp của nó vào kết quả.

Cụ thể, gọi $X_i$ là biến ngẫu nhiên nào đó cho một biến cố $i$ nào đó. Ta muốn tìm kỳ vọng của bình phương của tổng tất cả các biến ngẫu nhiên này, hay nói cách khác, ta cần tính $E[(X_1 + X_2 + X_3 + \ldots + X_N)^2]$.

Theo kỳ vọng tuyến tính, ta lại có:

$$\begin{align}
E[(X_1 + X_2 + X_3 + \ldots + X_N)^2] &= E[(X_1 + X_2 + X_3 + \ldots + X_N) \cdot (X_1 + X_2 + X_3 + \ldots + X_N)]\\
&= E[X_1 \cdot X_1 + \ldots + X_1 \cdot X_N + X_2 \cdot X_1 + \ldots + X_2 \cdot X_N + \ldots + X_N \cdot X_1 + \ldots + X_N \cdot X_N]\\
&= E[X_1 \cdot X_1] + \ldots + E[X_1 \cdot X_N] + E[X_2 \cdot X_1] + \ldots + E[X_2 \cdot X_N] + \ldots + E[X_N \cdot X_1] + \ldots + E[X_N \cdot X_N]\\
\end{align}$$

Như vậy ta có thể tính kỳ vọng của mỗi cặp và góp vào kết quả.

Tương tự, mũ $k$ thì bằng số dãy độ dài $k$, ta có thể làm giống như trên là tính kỳ vọng của mỗi bộ tích $k$ phần tử và góp nó vào kết quả.

## Kỹ thuật mũ

Nếu muốn duy trì tổng các số mũ $k$, ta cần duy trì tổng các số mũ nhỏ hơn. Ví dụ, tổng của các mũ $0$, mũ $1$ và mũ $2$ lần lượt là $S_0$, $S_1$ và $S_2$, và nếu tăng mỗi phần tử lên $x$. Các tổng mới sẽ là $S_0$, $S_1 + S_0 \cdot x$ và $S_2 + 2 \cdot x \cdot S_1 + x^2 \cdot S_0$. Ta sẽ tập trung vào kỹ thuật "ordered pairs".

## Các bài tập

### Bài 1

Giá của một chiếc TV là 1000 đô. Trong $N$ ngày tiếp theo, mỗi ngày giá của TV tăng 1% hoặc 2% (xác suất như nhau là 50%). Tính kỳ vọng giá TV sau $N$ ngày.

??? tip "Lời giải"
    Ta có công thức tính giá TV sẽ là $1000 \cdot (1 + \Delta_1) \cdot (1 + \Delta_2) \cdot (1 + \Delta_3) \ldots$. Với $\Delta_i$ là phần trăm giá tăng vào ngày thứ $i$

    Nếu tính theo giá, ta thấy số tiền tăng lên sẽ phụ thuộc vào giá hiện tại của chiếc TV. Tuy nhiên, nếu xét việc tăng của giá TV, thì biến cố này cho các ngày khác nhau lại độc lập với nhau. Ta dễ dàng tính được kỳ vọng phần trăm giá tăng của TV là $0.01 \cdot 0.5 + 0.02 \cdot 0.5 = 0.015$ hay 1.5%.

    Như vậy, sau $N$ ngày, kỳ vọng giá của TV sẽ là $E = 1000 \cdot (1 + 0.015)^N$.

### Bài 2

Bạn mua $N$ ($N \le 10^5$) vé số. Cái thứ $i$ có xác suất trúng là $p_i$. Biến cố độc lập (quan trọng!). Tìm kỳ vọng bình phương số vé thắng.

??? tip "Lời giải"
    Gọi $X_i$ là biến ngẫu nhiên cho biến cố vé số thứ $i$ trúng thưởng. Như vậy $E[X_i]$ sẽ là kỳ vọng vé số $i$ trúng thưởng. Do đây là biến ngẫu nhiên chỉ báo nên $E[X_i] = p_i$ tức là kỳ vọng cũng là xác suất vé $i$ trúng thưởng.

    Ta có kết quả cần tìm sẽ là $E[(X_1 + X_2 + X_3 + \ldots + X_N)^2]$. Khai triển ra như trong phần giải thích Ordered pairs thì ta sẽ cần phải tính tổng tất cả các $E[X_i \cdot X_j]$ với mọi $i$ và $j$. Có 2 trường hợp xảy ra:

    1. Khi $i \ne j$, ta cũng biết rằng các biến cố $X_i$ và $X_j$ độc lập với nhau, nên $E[X_i \cdot X_j] = E[X_i] \cdot E[X_j] = p_i \cdot p_j$.
    2. Khi $i = j$, ta biết rằng $X_i$ và $X_i$ không độc lập với nhau, ở đây đơn giản là $E[X_i \cdot X_i] = p_i$. Vì kỳ vọng cho vé $i$ trúng và vé $i$ cũng trúng đều quy về một khả năng.

    Nói thêm một chút để đỡ nhầm lẫn, ta thấy rằng $E[X_i \cdot X_i] = E[X_i^2] = p_i * 1^2$, nghĩa là xác suất có được biến cố vẫn là $p_i$, và giá trị nhận được là $1^2 = 1$. Bạn sẽ hiểu rõ vấn đề khi giải bài [Codeforces - A granite of science](https://codeforces.com/gym/100371/problem/H).

    Gọi $S = p_1 + p_2 + \ldots + p_N$. Như vậy $E[(X_1 + X_2 + X_3 + \ldots + X_N)^2] = \sum_i (p_i \cdot S - p_i^2 + p_i)$. Ta có thể tính kết quả này trong $O(N)$.

    Nếu bạn muốn gọn hơn, ta gọi thêm $S_2 = p_1^2 + p_2^2 + \ldots + p_N^2$. Ta sẽ được $E = S^2 - S_2 + S$. Kết quả này cũng có thể được tính trong $O(N)$.

### Bài 3

Tương tự bài 2 nhưng tìm kỳ vọng của mũ 3 hoặc 4.

??? tip "Lời giải"
    Tuơng tự bài trên, việc của ta sẽ làm là với mỗi bộ 3 $\{i, j, k\}$, ta góp $p_i \cdot p_j \cdot p_k$ vào kết quả, ta có các trường hợp đặc biệt sau:
    
    - Nếu $i = j = k$, ta chỉ góp $p_i$ vào kết quả.
    - Nếu $i = j \ne k$, ta góp $p_i \cdot p_k$ vào kết quả.
    - Nếu $i = k \ne j$, ta góp $p_i \cdot p_j$ vào kết quả.
    - Nếu $k = j \ne i$, ta góp $p_i \cdot p_k$ vào kết quả.
    - Tổng quát thì nếu có nhiều phần tử giống nhau (về vị trí), ta chỉ dùng 1 lần phần tử đó.

    Bây giờ gọi lần lượt:

    - $S = p_1 + p_2 + \ldots + p_N$
    - $S_2 = p_1^2 + p_2^2 + \ldots + p_N^2$
    - $S_3 = p_1^3 + p_2^3 + \ldots + p_N^3$.

    Giờ ta sẽ duyệt $i$ và $j$, ta có hai trường hợp sau:
    
    - Nếu $i = j$, ta sẽ góp vào tổng là $p_i \cdot (S - p_i) + p_i$ **(1)**. Lý do là vì sẽ có trường hợp $k = i$, khi đó $i = j = k$, nên ta chỉ thêm $p_i$, còn lại $i = j \ne k$, nên ta thêm $p_i \cdot (S - p_i)$ vào tổng.
    - Nếu $i \ne j$, ta sẽ góp vào tổng là $p_i \cdot p_j \cdot (S - p_i - p_j) + 2 \cdot p_i \cdot p_j$ **(2)**. Giải thích thì cũng tương tự như trên nhưng ở đây $k$ có thể bằng $i$ hoặc $j$ nên ta có $2 \cdot p_i \cdot p_j$.

    Đến đây thì ta sẽ có kết quả là:

    $$p_i \cdot p_j \cdot (S - p_i - p_j) + 2 \cdot p_i \cdot p_j + p_i \cdot (S - p_i) + p_i$$

    Ta có thể tính tổng này trong $O(N^2)$. Tuy nhiên như thế vẫn chưa đủ.

    Xét phần **(1)**: $p_i \cdot (S - p_i) + p_i$. Phần này không phụ thuộc $j$ nên ta có thể tính thẳng ra tổng sau cùng, nó sẽ giống như bài 2 ở trên và tổng đó sẽ là $S^2 + S - S_2$.

    Xét phần **(2)**: $p_i \cdot p_j \cdot (S - p_i - p_j) + 2 \cdot p_i \cdot p_j$. Bỏ hết ngoặc đi thì ta sẽ được

    $$p_i \cdot p_j \cdot S - p_i^2 \cdot p_j - p_i \cdot p_j^2 + 2 \cdot p_i \cdot p_j$$

    Tính tổng hết các $p_j$ để loại bỏ biến này thì ta có, lưu ý thêm là $i \ne j$ trong trường hợp này:

    $$S \cdot p_i \cdot (S - p_i) - p_i^2 \cdot (S - p_i) - p_i \cdot (S_2 - p_i^2) + 2 \cdot p_i \cdot (S - p_i)$$

    Mở ngoặc ra thì ta có:

    $$S^2 \cdot p_i - S \cdot p_i^2 - S \cdot p_i^2 + p_i^3 - S_2 \cdot p_i + p_i^3 + 2 \cdot S \cdot p_i - 2 \cdot p_i^2$$

    Thu gọn lại thì ta có:

    $$2 \cdot p_i^3 - (2S + 2) \cdot p_i^2 + (S^2 + 2S - S_2) \cdot p_i$$

    Tính tổng hết các $p_i$ để loại bỏ biến này thì ta được:

    $$2S_3 - (2S + 2) \cdot S_2 + (S^2 + 2S - S_2) \cdot S$$

    Như vậy kết quả tổng cộng sẽ là

    $$S^2 + S - S_2 + 2S_3 - (2S + 2) \cdot S_2 + (S^2 + 2S - S_2) \cdot S$$

    Và bạn có thể tính cái này trong $O(N)$.

    Việc giải sẽ phức tạp hơn khi ta cần tính mũ 4, hay thậm chí đến mũ $k$, nhưng vẫn có thể giải được.

### Bài 4

Có $N$ ($N \le 50$) bóng đèn và $M$ ($M \le 50$) công tắc. Với mỗi công tắc, ta biết các bóng đèn kết nối với nó (nghĩa là khi gạt công tắc, các bóng đèn sáng thì tắt, tắt thì sáng). Tất cả các bóng đều đang tắt, và ta gạt các công tắc với xác suất 50%. Tìm kỳ vọng của mũ 3 số các bóng đèn bật.

??? tip "Lời giải"
    Gọi $X_i$ là biến cố bóng đèn thứ $i$ sáng. Như vậy kỳ vọng số bóng đèn sáng sau cùng sẽ là $E[X_1 + X_2 + \ldots + X_N]$. Tuy nhiên ở đây ta cần tìm kỳ vọng của mũ 3, nghĩa là $E[(X_1 + X_2 + \ldots + X_N)^3]$.

    Như trong bài trên thì ta đã biết là kỳ vọng ở trên sẽ là tổng các $E[X_i \cdot X_j \cdot X_k]$, nghĩa là kỳ vọng bóng đèn $i$, $j$ và $k$ đều sáng, cũng là xác suất các bóng đèn này đều sáng (do là biến ngẫu nhiên chỉ báo). Ta duyệt mỗi bộ ba này trong $O(N^3)$.

    Với mỗi bộ ba, ta cần tính xác suất các bóng đèn trong bộ ba này đều sáng. Ta gọi $dp[x][y][z]$ là xác suất để đạt được trạng thái $(x, y, z)$ với $0 \le x, y, z \le 1$, ứng lần lượt với bóng đèn thứ $i$, $j$ và $k$, trong đó $0$ là trạng thái tắt, $1$ là trạng thái sáng. Ban đầu ta có $dp[0][0][0] = 1$, do cả ba bóng đèn ban đầu đều tắt. Với mỗi công tắc, ta sẽ cập nhật mảng $dp$ này (lưu ý là từ mảng $dp$ cũ bạn phải tính vào một mảng $dp$ mới nhé, vì trước khi xử lý công tắc và sau khi xử lý công tắc là hai trạng thái khác nhau). Ta duyệt hết $M$ công tắc và tính toán trong $O(M)$.

    Cuối cùng $E[X_i \cdot X_j \cdot X_k] = dp[1][1][1]$. Ta giải được bài này trong $O(N^3 \cdot M)$.

### Bài 5

Cho dãy số $a$ độ dài $N$ ($N \le 10^5$), tính tổng $sum \cdot len^3$ trên tất cả các đoạn con. In ra đáp án lấy dư với $10^9 + 7$.

??? tip "Lời giải"
    Ta có thể sử dụng kỹ thuật "góp vào tổng" cho bài này. Nghĩa là, với mỗi độ dài $len$, ta tính tổng $sum$ của tất cả các đoạn con độ dài như thế, rồi lấy tích $sum \cdot len^3$, thêm vào kết quả.

    Đầu tiên $len = 1$, $sum_1$ ở đây sẽ là $\sum_{i=1}^N a_i$.

    Tiếp theo $len = 2$, ta thấy mỗi đoạn con trước đó cần thêm giá trị phía bên phải của đoạn, trừ đoạn con cuối cùng (đoạn chứa $a_N$, vì không thể kéo dài đoạn này, ta phải bỏ nó đi), vậy $sum_2 = sum_1 + \sum_{i=2}^N a_i - \sum_{i=N}^N a_i$.

    Tiếp theo $len = 3$, ta thấy mỗi đoạn con trước đó cần thêm giá trị phía bên phải của đoạn, trừ đoạn con cuối cùng (đoạn chứa $a_{N-1} và a_N$, vì không thể kéo dài đoạn này, ta phải bỏ nó đi), vậy $sum_3 = sum_2 + \sum_{i=3}^N a_i - \sum_{i=N-1}^N a_i$.

    Và cứ như thế, tổng quát thì $sum_j = sum_{j-1} + \sum_{i=j}^N a_i - \sum_{i=N-j+2}^N a_i$.

    Ta có thể tính các tổng tiền tố và hậu tố trong $O(N)$.

    Vậy ta có thể tính bài này trong $O(N)$.

### Bài 6

Cho một cây $N$ đỉnh ($N \le 10^5$) và số nguyên $k$ ($k \le 10$). Tìm tổng của $\text{kích thước}^k$ của tất cả các đồ thị con liên thông. In đáp án lấy dư với $10^9+7$.

??? tip "Lời giải"
    Ta bắt đầu với hướng là với mỗi kích thước đồ thị con liên thông, tìm số các đồ thị con có kích thước như vậy. Tuy nhiên làm thế rất là khó và ta sẽ không đi theo hướng này.

    Cái ta cần là $size^k$, ví dụ $size = 3$, $k = 5$ và ta có 3 node trong đồ thị con liên thông là A, B, C. Thì với hiểu biết ở trên về mũ, ta cần thêm số đồ thị con liên thông chứa AAAAA, AAAAB, AAAAC, AAABA, ...., CCCCC. Vì vậy nên ta có thể đổi bài toán này thành, tìm số cách chọn một đồ thị con liên thông và chọn $k$ node trong cái đồ thị con liên thông này, vì mỗi dãy $k$ phần tử sẽ góp $1$ vào đáp án.

    Ta sẽ cần duy trì một mảng $dp[v][i]$, trong đó $v$ là gốc của cây con đang xét, $i$ là số node được chọn trong cây con này (không cần phải là $i$ node khác nhau). Mảng này có nghĩa là số cách chọn ra $i$ node (không cần phân biệt) trong một đồ thị con liên thông nào đó trong cây con gốc $v$.

    Xét node cha $u$ của $v$, giả sử $v$ là node con đầu tiên của $u$ theo thứ tự các node con của $u$ khi DFS, và ta đã có các $dp[v][i]$, việc ta cần làm là thêm node $u$ vào đây, hoặc không thêm. Nếu thêm, ta có thể thêm nhiều node $u$ chứ không phải chỉ một lần, vì thế với mỗi $dp[v][i]$ ta có thể thêm kết quả cho $dp[u][i]$, dp[u][i+1], dp[u][i+2], \ldots$. Nếu thêm $j$ node $u$, ta sẽ có $\binom{i+j}{j}$ cách thêm, vì ta có thể thêm vào bất kỳ vị trí nào.

    Nếu $v$ không phải là node con đầu tiên, ta cần một cách để chập 2 kết quả lại với nhau, ở đây là $dp[u]$ hiện tại và $dp[v]$. Ta xét $i$ node được chọn trong cây gốc $u$ hiện tại, và $j$ node được chọn trong cây gốc $v$, ta sẽ thêm vào $\binom{i+j}{j}$ tương tự như trên để tính $dp[u]$ mới.

    Kết quả của bài này sẽ là $dp[root][k]$, trong đó $root$ là node gốc của cây. Độ phức tạp của bài này sẽ tầm khoảng $O(nk^2)$.

### Bài 7

Bài này là bài DoubleLive của TopCoder SRM 727.

Cho một đội quân gồm $B$ gấu và $H$ người ($B, H \le 2000$). Gấu thì có 2 máu, người thì 1 máu. Đội cung thủ của địch có $T$ mũi tên ($T \le 2 \cdot B + H$). Mỗi mũi tên tiếp theo sẽ đâm vào một trong số quân của bạn một cách ngẫu nhiên, giảm 1 máu của đối tượng đó. Nếu đối tượng còn 0 máu, đối tượng đó chết.

Sức mạnh đội quân được định nghĩa là $\text{số gấu} \cdot \text{số người} \cdot \text{tổng số}$, ví dụ $3 \cdot 7 \cdot 10 = 210$ với một đội quân 3 gấu 7 người. Không quan trọng một số gấu chỉ còn 1 máu trong trường hợp này.

Tính kỳ vọng sức mạnh đội quân sau khi đội cung thủ địch dùng hết mũi tên của chúng.

??? tip "Lời giải"
    Ta sẽ cần tính $E[B \cdot H \cdot (B + H)]$, trong đó $B$ là số gấu sau cuộc tấn công và $H$ là số người sau cuộc tấn công. Ta có thể thấy rằng ta kì vọng cần tìm là tổng kì vọng khi ta chọn 1 gấu, 1 người và một trong các chiến binh còn lại (sau khi kết thúc cuộc tấn công), ở đây nó cũng là xác suất chọn ra.

    Thử gọi $dp[one][two]$ là xác suất để có được $one$ chiến binh 1 máu (không quan tâm nó là gấu hay người), $two$ là số chiến binh 2 máu. Với cách này, ta có thể đi tiếp đến $dp[one-1][two]$ với xác suất $\frac{one}{one+two}$, và đến $dp[one+1][two-1]$ với xác suất $\frac{two}{one+two}$. Tuy nhiên, đến cuối cùng ta lại không thể phân biệt được số người và số gấu.

    Xét một cặp người - gấu nào đó, làm sao để tính được xác suất chúng đều còn sống sau cuộc tấn công? Ta gọi $dp[one][two][hp1][hp2]$ là xác suất để sau cuộc tấn công, ta có $one$ chiến binh 1 máu, $two$ chiến binh 2 máu, với cặp người - gấu có số máu lần lượt là $hp1$ ($0 \le hp1 \le 1$) và $hp2$ ($0 \le hp2 \le 2$). Cách tính cũng tương tự như trên. Kết quả ta cần là $X = dp[one][two][1][1] + dp[one][two][1][2]$, với $one$ và $two$ lúc này là sau cuộc tấn công. Do các con gấu là như nhau và người cũng như nhau, việc tính lại cho các cặp người - gấu khác là không cần thiết, vì vậy xác suất chọn ra được 1 người 1 gấu là $X \cdot B \cdot H$ với $B$, $H$ là số gấu và số người ban đầu.

    Nhưng còn tổng số chiến binh thì sao? Ta biết rằng tổng số chiến binh sẽ là $one + two$ sau cuộc tấn công, như vậy đáp án sẽ cần nhân thêm với $one + two$. Giải thích thêm là bởi vì bạn đã đến được trạng thái với $one$ chiến binh 1 máu và $two$ chiến binh 2 máu, nên xác suất chọn ra được một trong các chiến binh còn lại sẽ là $1$. Ta muốn chọn hết chúng, nên ta cần $one + two$ lần.

    Độ phức tạp của bài này là $O((B+H)^2)$.

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [Codeforces - Little Pony and Expected Maximum](https://codeforces.com/contest/454/problem/C) | :white_check_mark: | [Submission](https://codeforces.com/contest/454/submission/206315938) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF454-D2-C.cpp) | 18/05/2023 |
| [Google Kickstart 2017 Round B - Math Encoder](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201b7b) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Google%20Kickstart/Kickstart%2017-RB-A.cpp) | 30/05/2023 |
| [Codeforces - Imbalanced Array](https://codeforces.com/contest/817/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/817/submission/206312731) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF817-D12-D.cpp) | 18/05/2023 |
| [Codeforces - Randomizer](https://codeforces.com/problemset/problem/559/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/559/submission/207844971) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF559-D1-D.cpp) | 30/05/2023 |
| [Codeforces - Andrey and Problem](https://codeforces.com/problemset/problem/442/B) | :white_check_mark: | [Submission](https://codeforces.com/contest/442/submission/215303463) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF442-D1-B.cpp) | 24/07/2023 |
| [Google Kickstart 2020 Round D — Beauty of Tree](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Google%20Kickstart/Kickstart%2020-RD-C.cpp) | 24/07/2023 |
| [Codeforces - Score of a Tree](https://codeforces.com/contest/1777/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/1777/submission/215479909) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF1777-D2-D.cpp) | 25/07/2023 |
| [Codeforces - Two Arrays and Sum of Functions](https://codeforces.com/contest/1165/problem/E) | :white_check_mark: | [Submission](https://codeforces.com/contest/1165/submission/215677750) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF1165-D3-E.cpp) | 26/07/2023 |
| [Codedrills - Bob and Random Exploration](https://codedrills.io/contests/amrita-icpc-practice-session-6/problems/bob-and-random-exploration) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codedrills/bob-and-random-exploration.cpp) | 28/07/2023 |
| [Atcoder ABC 189 F - Sugoroku2](https://atcoder.jp/contests/abc189/tasks/abc189_f) | :white_check_mark: | [Submission](https://atcoder.jp/contests/abc189/submissions/44016725) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder189-ABC-F.cpp) | 29/07/2023 |
| [Codechef - KALADIN](https://www.codechef.com/problems/KALADIN) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/1011485661) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20KALADIN.cpp) | 31/07/2023 |
| [Codeforces - Game on Tree](https://codeforces.com/contest/280/problem/C) | :white_check_mark: | [Submission](https://codeforces.com/contest/280/submission/216661891) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF280-D1-C.cpp) | 01/08/2023 |
| [E-Olymp - Difficult path](https://www.e-olymp.com/en/problems/7261) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/E-Olymp/EOLYMP%207261.cpp) | 01/08/2023 |
| [E-Olymp - A coincidence](https://www.e-olymp.com/en/problems/7262) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/E-Olymp/EOLYMP%207262.cpp) | 06/08/2023 |
| [E-Olymp - A full set](https://www.e-olymp.com/en/problems/7263) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/E-Olymp/EOLYMP%207263.cpp) | 04/08/2023 |
| [Codeforces - A fish lunch ](https://codeforces.com/gym/100371/problem/D) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-D.cpp) | 03/08/2023 |
| [Codeforces - The secret code](https://codeforces.com/gym/100371/problem/E) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-E.cpp) | 07/08/2023 |
| [Codeforces - Dura Lex](https://codeforces.com/gym/100371/problem/F) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-F.cpp) | 11/08/2023 |
| [Codeforces - A path to knowledge](https://codeforces.com/gym/100371/problem/G) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-G.cpp) | 08/08/2023 |
| [Codeforces - A granite of science](https://codeforces.com/gym/100371/problem/H) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-H.cpp) | 10/08/2023 |
| [Codeforces - Probable diagnosis](https://codeforces.com/gym/100371/problem/I) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-I.cpp) | 11/08/2023 |
| [Codeforces - Zoological experiment](https://codeforces.com/gym/100371/problem/J) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-J.cpp) | 14/08/2023 |
| [Codeforces - A game (High)](https://codeforces.com/gym/100371/problem/K) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-K.cpp) | 08/08/2023 |
| [Codeforces - A dangerous game (High)](https://codeforces.com/gym/100371/problem/L) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF100371-Gym-L.cpp) | 21/08/2023 |
| [Codeforces - Hash-table (High)](https://codeforces.com/gym/100371/problem/M) | | | | |
| [Codechef - MARTING1](https://www.codechef.com/problems/MARTING1) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/1019608588) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20MARTING1.cpp) | 10/09/2023 |
| [Codeforces - Lipshitz Sequence](https://codeforces.com/contest/602/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/601/submission/220110119) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF602-D2-D.cpp) | 24/08/2023 |
| [Topcoder SRM 727 - DoubleLive](https://community.topcoder.com/stat?c=problem_statement&pm=14723) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/TopCoder/SRM727-D1-1500.cpp) | 20/07/2023 |
| [Codechef - CUTTREE](https://www.codechef.com/problems/CUTTREE) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/1023740216) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20CUTTREE.cpp) | 01/10/2023 |
| [Codeforces - Rikka with Subsequences](https://codeforces.com/gym/102012/problem/D) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF102012-Gym-D.cpp) | 19/09/2023 |
| [Codechef - FSSYNC](https://www.codechef.com/problems/FSSYNC) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/1018924523) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20FSSYNC.cpp) | 07/09/2023 |
| [Topcoder TCO Algorithm Round 1C 2013 - TheKnights](https://community.topcoder.com/stat?c=problem_statement&pm=11541&rd=15585&rm=316561&cr=23003389) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/TopCoder/TCOA2013R1-D1-1500.cpp) | 12/09/2023 |
| [Codeforces - Graph Game](https://codeforces.com/contest/235/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/235/submission/223444065) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF235-D1-D.cpp) | 15/09/2023 |
