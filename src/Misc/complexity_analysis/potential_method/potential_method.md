# Phương pháp Tiềm năng

## Nguồn

<img src="/CPBlogs/img/wikipedia.png" width="16" height="16"/> [Potential method - Wikipedia](https://en.wikipedia.org/wiki/Potential_method)

## Lời tựa

Trong lý thuyết tính toán độ phức tạp, Phương pháp Tiềm năng là một phương pháp dùng để phân tích độ phức tạp phân bổ (Amortized complexity) về mặt thời gian và bộ nhớ của một cấu trúc dữ liệu. Nó cũng là một thước đo hiệu suất thông qua một chuỗi các thao tác để loại bỏ chi phí của các thao tác không thường xuyên nhưng tốn kém.

## Định nghĩa Thời gian phân bổ (Amortized time)

Trong phương pháp Tiềm năng, một hàm $\Phi$ được chọn để ánh xạ các trạng thái của cấu trúc dữ liệu với các số không âm. Nếu $S$ là một trạng thái của cấu trúc dữ liệu, $\Phi(S)$ tượng trưng cho lượng công việc được giữ (hay "được trả tiền") trong phân tích phân bổ nhưng chưa được thực thi. Vì vậy, $\Phi(S)$ có thể được hiểu là việc tính phần năng lượng tiềm năng lưu trong trạng thái đó. Giá trị tiềm năng trước khi khởi tạo cấu trúc dữ liệu là $0$. Ngoài ra, $\Phi(S)$ có thể được hiểu là lượng hỗn loạn trong trạng thái $S$ hoặc là khoảng cách của trạng thái hiện tại đến trạng thái lý tưởng.

Gọi $o$ là bất cứ thao tác đơn lẻ nào trong một dãy các thao tác trên một cấu trúc dữ liệu nào đó, với $S_{trước}$ là trạng thái của cấu trúc dữ liệu trước thao tác $o$ này và $S_{sau}$ là trạng thái sau khi thao tác $o$ kết thúc. Một khi $\Phi$ được chọn, thời gian phân bổ của thao tác $o$ được định nghĩa là:

$$T_{\text{phân bổ} }(o) = T_{thực}(o) + C \times (\Phi(S_{trước}) - \Phi(S_{sau}))$$

Trong đó $C$ là hằng số tỉ lệ không âm (tính theo đơn vị thời gian) phải cố định trong suốt quá trình phân tích. Nghĩa là, thời gian phân bổ được định nghĩa là thời gian thực tiêu tốn bởi thao tác cộng với $C$ lần chênh lệch tiềm năng tạo ra bởi thao tác đó.

Khi nghiên cứu độ phức tạp tính toán tiệm cận bằng cách sử dụng ký hiệu big O, các yếu tố hằng số không liên quan và do đó hằng số $C$ thường bị bỏ qua.

## Quan hệ giữa thời gian phân bổ và thời gian thực

Mặc dù có vẻ hơi trừu tượng, tổng thời gian phân bổ của một chuỗi thao tác cung cấp cho chúng ta một cận trên tốt so với thời gian thực trên cùng một nhóm thao tác đó.

Với mọi chuỗi thao tác $O = o_1, o_2, ..., o_n$, ta định nghĩa:

- Tổng thời gian phân bổ: $T_{\text{phân bổ} }(O) = \sum_{i=1}^{n} T_{\text{phân bổ} }(o_i)$
- Tổng thời gian thực: $T_{thực}(O) = \sum_{i=1}^{n} T_{thực}(o_i)$

Nên:

$$T_{\text{phân bổ} }(O) = \sum_{i=1}^{n} (T_{thực}(o_i) + C \times (\Phi(S_i) - \Phi(S_{i-1}))) = T_{thực}(O) + C \times (\Phi(S_n) - \Phi(S_0))$$

Trong đó dãy các giá trị của hàm Tiềm năng tạo ra một chuỗi lồng nhau, trong đó tất cả các số hạng không phải đầu tiên và cuối cùng huỷ nhau theo cặp. Chuyển vế ta có:

$$T_{thực}(O) = T_{\text{phân bổ} }(O) - C \times (\Phi(S_n) - \Phi(S_0))$$

Do $\Phi(S_0) = 0$ và $\Phi(S_n) \geq 0$, $T_{thực}(O) \leq T_{\text{phân bổ} }(O)$, nên thời gian phân bổ có thể được dùng để tính cận trên của thời gian thực trên một dãy các thao tác, ngay cả khi thời gian phân bổ của một thao tác nào đó có biên độ lớn so với thời gian thực.

## Phân tích Phân bổ trong trường hợp xấu nhất

Thông thường, phân tích phân bổ được dùng kết hợp với trường hợp xấu nhất của đầu vào. Với trường hợp xấu nhất này, nếu $X$ là loại thao tác được sử dụng trong cấu trúc dữ liệu, và số nguyên $n$ là kích thước của cấu trúc dữ liệu được cho (ví dụ như nó chứa bao nhiêu biến chẳng hạn), thì thời gian phân bổ của các thao tác loại $X$ được định nghĩa là thời gian phân bổ lớn nhất trong tất cả các dãy thao tác có thể có trên cấu trúc dữ liệu kích thước $n$, chỉ tính các thao tác $o_i$ loại $X$ trong nhóm.

Với định nghĩa này, thời gian để thực hiện dãy thao tác có thể được ước lượng bằng cách nhân thời gian phân bổ của mỗi loại thao tác trong dãy với số thao tác của loại thao tác đó.

## Các ví dụ

### Mảng động

Mảng động là một cấu trúc dữ liệu dùng để duy trì một dãy các phần tử, cho phép truy cập nhờ vào vị trí trong mảng và khả năng tăng giới hạn mảng lên 1. Trong Java nó là ArrayList còn trong Python nó là list.

Mảng động có thể được cài như một cấu trúc dữ liệu gồm một mảng $A$ các phần tử, có độ dài $N$ nào đó, với một số $n \leq N$ là các vị trí trong mảng chúng ta đã dùng. Với cấu trúc dữ liệu như thế này, việc truy cập vào mảng động có thể được cài bằng cách truy cập vào cùng ô nhớ trong mảng $A$ đó, và khi $n < N$, thao tác tăng size của mảng động có thể được cài bằng cách tăng n lên. Tuy nhiên, khi $n=N$, ta cần resize lại $A$, một cách phổ biến là tăng gấp đôi size của nó, thay $A$ bằng một mảng có độ dài $2n$.

Cấu trúc dữ liệu này có thể được phân tích nhờ hàm Tiềm năng sau:

$$\Phi = 2n - N$$

Vì việc resize này làm cho $A$ luôn có số phần tử lớn hơn hoặc bằng nửa kích thước, nên hàm tiềm năng luôn không âm.

Thao tác tăng kích thước mảng không phải lúc nào cũng dẫn đến việc resize, $\Phi$ tăng lên 2, một hằng số. Vì vậy, thời gian thực của thao tác và thời gian tăng lên tiềm năng kết hợp lại để tạo ra thời gian phân bổ của thao tác loại này.

Tuy nhiên, nếu việc tăng kích thước dẫn đến resize mảng, $\Phi$ giảm về $0$ sau khi resize. Tạo mảng mới $A$ và sao chép tất cả các giá trị cũ của vào mảng mới này tôn $O(n)$ thời gian thực, nhưng (với hằng số tỉ lệ $C$ tốt) cái này bị tiêu huỷ bới việc giảm hàm tiềm năng, trả về một tổng thời gian phân bổ là hằng số cho thao tác này.

Những thao tác khác của cấu trúc dữ liệu (đọc ghi mảng mà không thay đổi kích thước) không tạo ra thay đổi cho hàm tiềm năng và có cùng thời gian phân bổ hằng số như thời gian thực.

Vì vậy, với việc resize như thế này cộng với hàm tiềm năng, phương pháp tiềm năng cho thấy rằng tất cả các thao tác trên mảng động tốn thời gian phân bổ hằng số. Kết hợp điều này với bất đẳng thức giữa thời gian phân bổ và thời gian thực trên dãy các thao tác, điều này cho thấy rằng bất kỳ dãy $n$ thao tác trên mảng động tốn $O(n)$ thời gian thực trong trường hợp xấu nhất, dù cho một số thao tác đơn lẻ có thể tiêu tốn hơn thời gian tuyến tính.

Khi mảng động chứa các thao tác giảm kích thước mảng cũng như tăng kích thước, hàm tiềm năng cũng phải được thay đổi để tránh việc hàm bị âm. Một cách để làm đó là thêm trị tuyệt đối vào hàm tiềm năng ở trên.

### Multi-Pop Stack

Cho một stack hỗ trợ các thao tác sau:

- $Init$: tạo một stack rỗng.
- $Push$: thêm một phần tử lên đỉnh stack, tăng size của nó lên 1.
- $Pop(k)$: xoá $k$ phần tử từ đỉnh stack, trong đó $k$ không lớn hơn số phần tử hiện thời của stack.

$Pop(k)$ tốn $O(k)$ thời gian, nhưng ta có thể chứng minh được tất cả các thao tác tốn $O(1)$ thời gian phân bổ.

Cấu trúc dữ liệu này có thể được phân tích nhờ hàm Tiềm năng sau:

$$\Phi = \text{số phần tử trong stack}$$

Rõ ràng số phần tử thì luôn không âm.

Một thao tác $Push$ tốn $O(1)$ và tăng $\Phi$ lên $1$, nên thời gian phân bổ là hằng số.

Một thao tác $Pop$ tốn $O(k)$ và giảm $\Phi$ đi $k$, nên thời gian phân bổ cũng là hằng số.

Điều này chứng tỏ bất kì chuỗi $m$ thao tác nào cũng tổn $O(m)$ thời gian trong trường hợp xấu nhất.

### Bộ đếm nhị phân

Xét một bộ đếm dùng số nhị phân với các thao tác như sau:

- $Init$: tạo bộ đếm với giá trị là $0$.
- $Inc$: thêm $1$ vào giá trị của bộ đếm.
- $Read$: trả về giá trị hiện thời của bộ đếm.

Trong ví dụ này ta coi việc tăng giá trị tốn 1 đơn vị thời gian cho mỗi thao tác bit. Ta muốn chứng minh là thao tác $Inc$ tốn $O(1)$ thời gian phân bổ.

Cấu trúc dữ liệu này có thể được phân tích nhờ hàm Tiềm năng sau:

$$\Phi = \text{số bit 1 của giá trị bộ đếm} = \text{khoảng-cách-hamming}(\text{bộ đếm})$$

Rõ ràng số phần tử thì luôn không âm.

Một thao tác $Inc$ đảo bit đầu tiên (bit bên phải ngoài cùng). Sau đó, nếu bit đầu tiên bị đảo từ $1$ về $0$, bit tiếp theo cũng phải bị đảo. Việc này tiếp tục đến khi một bit được đảo từ $0$ sang $1$. Đến đây thì nó dừng đảo. Nếu giá trị ban đầu có $k$ bit $1$ thì ta đảo tổng cộng $k+1$ bit, với thời gian thực là $k+1$, trừ đi phần Tiềm năng là $k-1$ (trước thao tác ta có $k$ bit $1$, sau thao tác ta có $1$ bit $1$, nên $\Phi(S_{trước}) - \Phi(S_{sau}) = k - 1$), thì thời gian phân bổ là $2$. Vậy thời gian thực để chạy $m$ thao tác là $O(m)$.

## Ứng dụng

Hàm Tiềm năng thường được sử dung để phân tích Fibonacci Heap, một loại hàng chờ ưu tiên (priority queue) cho phép xoá phần tử với thời gian phân bổ là $log$, và tất cả các thao tác khác với thời gian phân bổ là hằng số. Nó cũng được dùng để phân tích [Splay Tree](../../data_structures/splay_tree/splay_tree.md), một loại cây nhị phân tìm kiếm tự biến đổi với thời gian phân bổ của mỗi thao tác là $log$.
