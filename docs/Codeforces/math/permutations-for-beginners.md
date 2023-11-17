# Hoán vị cho người mới bắt đầu

## Nguồn

<img src="../../../assets/images/codeforces.png" width="16" height="16"/> [[Tutorial] A comprehensive guide to permutations for beginners](https://codeforces.com/blog/entry/111187)

## Định nghĩa, các tính chất cơ bản và các ký hiệu

Để bắt đầu thì ta sẽ cùng xem xét định nghĩa của hoán vị mà chắc bạn đã thấy rất nhiều lần trên Codeforces.

**Định nghĩa**: Một hoán vị kích thước $n$ là một mảng kích thước $n$ chứa các số nguyên từ $1$ đến $n$ mà mỗi số chỉ xuất hiện đúng một lần.

Nhưng tại sao ta lại quan tâm đến mấy cái mảng hay dãy số như thế? Lý do thực ra khá đơn giản.

Xét dãy $a$ chứa $n$ số nguyên. Ta có thể đánh dấu chúng với các số nguyên từ $1$ đến $n$, vậy số nguyên thứ $i$ trong dãy là $a_i$. Để hiểu những điều sau đây, sẽ rất hữu ích khi ta xét ví dụ với $a_i = i$ với mọi $i$.

Giờ ta xáo mảng này lên (một số phần tử có thể ở yên tại chỗ sau khi xáo). Ta sẽ tạo một hoán vị từ việc xáo này theo hai cách:

1. Chỉ số của phần tử lúc đầu ở vị trí $i$ là gì? (Trong trường hợp $a_i = i$, điều này có nghĩa là tìm vị trí của $i$ trong mảng sau khi xáo). Gọi chỉ số này là $f(i)$. Thì $f$ là hàm ánh xạ từ ${1, 2, \dots, n}$ đến chính nó. Giờ để ý rằng khi ta có mảng $[f(1), f(2), \dots, f(n)]$, nó thoả mãn định nghĩa của hoán vị! Ví dụ, ban đầu ta có mảng $1, 2, 3, 4, 5$, sau khi xáo ta có mảng $2, 4, 1, 5, 3$. Vậy thì mảng $f$ sẽ là $3, 1, 5, 2, 4$.
2. Chỉ số cũ của phần tử ở vị trí $i$ bây giờ là gì? (Trong trường hợp $a_i$ = i$, điều này có nghĩa là xem số ở vị trí $i$ bây giờ là bao nhiêu). Gọi chỉ số này là $g(i)$. Thì $g$ cũng là hàm ánh xạ từ ${1, 2, \dots, n}$ đến chính nó. Khi ta có mảng $[g(1), g(2), \dots, g(n)]$, nó cũng thoả mãn định nghĩa của hoán vị! Để ý rằng $f$ và $g$ không được định nghĩa giống nhau, và các hoán vị được sinh ra cũng khác nhau. Thực tế, không khó để nhận ra rằng $f(g(x)) = g(f(x)) = x$ với mọi $x$ trong tập hợp ${1, 2, \dots, n}$. Ví dụ, ban đầu ta có mảng $1, 2, 3, 4, 5$, sau khi xáo ta có mảng $2, 4, 1, 5, 3$. Trong trường hợp này mảng $g$ cũng sẽ là $2, 4, 1, 5, 3$.

Như vậy việc xáo các phần tử (hay việc đổi chỗ / hoán vị các phần tử) là một cách khác để thể hiện hoán vị.

Nó cho thấy rằng làm thế nào các hoán vị lại liên quan đến các hàm ánh xạ từ ${1, 2, \dots, n}$ đến chính nó sao cho tất cả các ảnh đều khác nhau (và tất cả các phần tử trong mảng hoán vị tương ứng với một vị trí gốc duy nhất). Nói cách khác, một hoán vị có thể được coi là một ánh xạ đơn ánh trên một tập, đây là định nghĩa tự nhiên nhất để sử dụng cho khá nhiều ứng dụng. Góc nhìn thứ ha (hàm $g$) là cái tương ứng với định nghĩa này, và hoán vị trong cách thứ nhất (hàm $f$) là cái mà ta thường gọi là **mảng vị trí** của hoán vị trong cách thứ hai (tên này không chuẩn lắm). Sau này ta sẽ thấy rằng nó chính là cái được gọi là **nghịch đảo** của hoán vị.

Lưu ý rằng giải thích vừa rồi khá quan trọng trong việc hiểu rõ hoán vị là gì. Hãy đọc lại một vài lần và thử một vài ví dụ cho đến khi bạn hiểu được hoán vị, cũng như cách các hàm $f$ và $g$ tương tác với nhau.

### Ký hiệu hai dòng

Để ý rằng hoán vị $[a_1, a_2, \dots, a_n]$ của $[1, 2, \dots, n]$ tương ứng với một hàm $f$ trên tập ${1, 2, \dots, n}$ định nghĩa bởi hàm $f(i) = a_i$. Nghĩa là, tập các cặp $(i, a_i)$ xác định một hoán vị duy nhất (nó chỉ là một tập các ánh xạ từ vị trí đến phần tử) và ngược lại. Để hiểu kết hợp và nghịch đảo (giới thiệu sau đây) rõ hơn, ta xét ký hiệu sau đây:

$$
\begin{equation*}
\begin{pmatrix} 1 & 2 & \cdots & n \\ a_1 & a_2 & \cdots & a_n \end{pmatrix}
\end{equation*}
$$

Ở đây ta đặt các cặp trên từng cột, từ trái sang phải. Lưu ý rằng các cặp này có thể bị xảo trộn (như domino ấy), và nó dẫn đến một số tính chất thú vị:

1. Điều gì sẽ xảy ra khi ta nghịch đảo các cặp (thay $(i, a_i)$ bằng $(a_i, i)$ với mọi $i$, tương ứng với việc đổi chỗ hai dòng ấy)? Nếu hoán vị ban đầu tương ứng với hàm $g$, hoán vị sau khi nghịch đảo sẽ tương ứng với hàm $f$! Điều này sẽ cho thấy rõ hơn về mối quan hệ giữa $f$ và $g$. Vậy nên thao tác này sẽ nghịch đảo hàm.
2. Điều gì sẽ xảy ra khi ta thử kết hợp hai hoán vị bằng cách lấy nửa dưới của hoán vị đầu tiên $p_1$ và nửa trên của hoán vị thứ hai $p_2$? Nếu hàm $g$ của $p_1$ là $g_1$, của $p_2$ là $g_2$, thì có thể xác định rằng hàm $g$ của hoán vị mới sẽ là hàm được tạo ra bởi việc áp dụng $g_1$, rồi $g_2$. Vậy nên thao tác này sẽ kết hợp hàm.

### Hoán vị bất biến

Để ý rằng khi một hoán vị được sắp xếp, nó sẽ là $[1, 2, \dots, n]$. Vậy nên bất kỳ thao tác tích luỹ nào trên mảng hoán vị (như tổng, tích, xor, tổng bình phương, số số lẻ, vân vân) mà không phụ thuộc vào thứ tự của các phần tử trong mảng sẽ cho ra kết quả như nhau với mọi hoán vị cùng kích thước.

## Góc nhìn thứ tự

### Các điểm cố định

Một điểm cố định của hoán vị $a$ là một chỉ số $i$ sao cho $a_i = i$. Các điểm này là các điểm không bị ảnh hưởng bởi hoán vị, vậy nên nếu ta bỏ qua những gì xảy ra với các điểm này, ta sẽ không bị mất đi bất kỳ thông tin nào về hoán vị đó. Đây cũng là lý do tại sao các chỉ số $i$ này thường được bỏ qua trong ký hiệu hai dòng (và cũng trong ký hiệu chu trình, sẽ được giới thiệu ở phần sau).

Lưu ý, nếu bạn đã quen với chu trình hoặc đang đọc lại bài viết này, bạn có thể nhận thấy rằng ý này phù hợp hơn với chu trình và tổ hợp, nhưng mình vẫn để nó ở đây vì nó chia sẻ một số ý tưởng với các phần khác trong phần này. Tương tự, điều này cũng áp dụng cho phần tiếp theo.

### Derangements

Một derangement là một hoán vị không có điểm cố định nào. Nghĩa là với mọi $i$, ta có $a_i \neq i$. Gọi $D_n$ là số hoán vị độ dài $n$ là derangement. Có ít nhất 3 cách khác nhau để đếm:

#### Giải các phương trình tuyến tính

#### Đệ quy

Giả sử $a_n = k \neq n$. Xét $a_k$. Nếu $a_k = n$ thì ta có $D_{n-2}$ cách để hoán vị các phần tử còn lại. Nếu $a_k \neq n$, ta để ý rằng bài toán sẽ quay về tính số derangement cho $n-1$ phần tử bằng cách thay $n$ (được gán trong $n-2$ slot còn lại) bằng $k$.

Như vậy công thức sẽ là $D_n = (n-1) \dot (D_{n-1} + D_{n-2})$. Dùng quy nạp cũng có thể giải ra được.

#### Dùng nguyên tắc bao hàm và loại trừ

### Các nghịch thế

## Góc nhìn phân rã chu trình

## Góc nhìn thành phần hoán vị

## Các topic khác

## Luyện tập
