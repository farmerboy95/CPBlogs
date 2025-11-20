# Tìm kiếm nhị phân và các phương pháp "chia đôi" khác

## Nguồn

[Binary search and other "halving" methods - nor's blog](https://nor-blog.pages.dev/posts/2021-11-07-binary-search/)

## Ý tưởng chính của tìm kiếm nhị phân

Ý tưởng chính của tìm kiếm nhị phân là việc *giảm tuyến tính không gian tìm kiếm*. Ta sẽ đi vào chi tiết sau đây.

### Ví dụ nho nhỏ

Hãy cùng bắt đầu với một ví dụ đơn giản. Giả sử ta có một mảng như sau: $[1, 7, 9, 12, 19]$, và ta muốn xem thử số $7$ có trong mảng không (trả về chỉ số tính từ $0$). Có một số cách để làm, trong đó trâu nhất là duyệt qua từng phần tử, kiểm tra xem có phần tử nào bằng $7$ không. Cách này tốn 5 lần so sánh.

Để ý rằng mảng đã được sắp xếp. Vậy nên nếu ta kiểm tra phần tử ở vị trí $p$ nào đó trong mảng, ta có 3 khả năng sau:

- Phần tử bằng $7$: ta đã tìm thấy kết quả và có thể dừng tìm kiếm.
- Phần tử nhỏ hơn $7$: do mảng đã được sắp xếp, tất cả các phần tử  ở vị trí $< p$ đều nhỏ hơn $7$, nên ta không cần kiểm tra bất kỳ phần tử nào ở vị trí $\leq p$ nữa.
- Phần tử lớn hơn $7$: tương tự, ta không cần kiểm tra bất kỳ phần tử nào ở vị trí $\geq p$ nữa.

Vậy ta có thể làm như sau: ban đầu không gian tìm kiếm sẽ là đoạn $[0, 4]$. Ta sẽ xét phần tử nằm giữa của không gian tìm kiếm này. Ở đây ta sẽ có 2 trường hợp như sau:

- Ta dừng tìm kiếm nếu phần tử ở vị trí đó bằng $7$.
- Ta giảm không gian tìm kiếm đi một nửa sau mỗi lần kiểm tra.

Ví dụ, xét phần tử giữa của không gian tìm kiếm, nó có giá trị là $9$. Vì $9 > 7$, ta sẽ không cần xét đoạn $[2, 4]$ nữa, và không gian tìm kiếm mới sẽ là $[0, 1]$. Có hai phần tử giữa trong không gian tìm kiếm mới này, ta sẽ mặc định chọn phần tử bên trái, sẽ có giá trị là $1$. Vì $1 < 7$, ta sẽ không cần xét đoạn $[0, 0]$ nữa, và không gian tìm kiếm mới sẽ là $[1, 1]$. Bây giờ chỉ còn một phần tử duy nhất trong không gian tìm kiếm, ta kiểm tra nó và thấy nó bằng $7$, nên ta có thể trả về chỉ số $1$ của nó.

Ủa nếu chỗ đó là số $4$ thay vì $7$ thì sao? Ta sẽ làm tương tự, và cuối cùng không gian tìm kiếm sẽ bị thu hẹp lại thành một đoạn rỗng, và ta có thể trả về kết quả là không tìm thấy. Ta sẽ dùng độ dài của không gian tìm kiếm làm giá trị trả về trong trường hợp không tìm thấy (ta sẽ giải thích vụ này sau).

Cài đặt của thuật toán thì sẽ trông như sau:

```cpp
int find_position(const vector<int>& a, int x) {
    int l = 0;
    int r = (int)a.size() - 1;   // [l, r] là không gian tìm kiếm
    while (l <= r) {             // khi không gian tìm kiếm không rỗng
        int m = l + (r - l) / 2; // vị trí "giữa" (middle) trong đoạn
        if (a[m] == x) return m; // tìm ra rồi
        else if (a[m] < x) {
            l = m + 1;           // loại bỏ tất cả các chỉ số <= m khỏi không gian tìm kiếm
        } else {
            r = m - 1;           // loại bỏ tất cả các chỉ số >= m khỏi không gian tìm kiếm
        }
    }
    return n;                    // không tìm thấy
}
```

Nó có hiệu quả hơn tìm kiếm tuyến tính không? Ở mỗi bước, ta giảm không gian tìm kiếm đi ít nhất một nửa, như vậy trong $1 + \log_2 n$ bước ($n$ là kích thước mảng ban đầu) ta sẽ thu hẹp không gian tìm kiếm về độ dài $< 1$, và vì kích thước là số nguyên, nó sẽ trở thành $0$. Ta có thể dễ dàng biết lúc nào nó dừng lại.

### Tổng quát hơn một tí

Chắc ai cũng biết là, tìm kiếm nhị phân không chỉ được sử dụng một cách đơn giản như trên trong lập trình thi đấu (và cả trong đời thực).

Ta xem xét kỹ hơn thuật toán ở trên nhá. Ta đang dùng một kiểu thứ tự gì đó (thứ tự các số nguyên như trong ví dụ trên) để bỏ đi một phần lớn không gian tìm kiếm (ở đây là một nửa không gian tìm kiếm mỗi lần kiểm tra).

Tổng quát hóa cái này sao ta? Quan trọng hơn là, đề bài kiểu tổng quát sẽ trông như thế nào?

Đầu tiên, ta sẽ chỉnh bài toán ban đầu một chút để dễ tổng quát hóa hơn. Thay vì tìm xem phần tử nào đó có tồn tại trong mảng hay không, ta có thể tìm phần tử đầu tiên lớn hơn hoặc bằng một giá trị cho trước nào đó (nếu không có phần tử như vậy thì trả về độ dài mảng).

Bài này rõ ràng tổng quát hơn bài trước. Nếu đáp án của ta là ở vị trí $i$, ta có thể kiểm tra xem nó có đùng không bằng cách kiểm tra $i < n$ và $a[i] = x$ hay không. Nếu không thì ta không tìm thấy phần tử $x$ trong mảng.

Thử bỏ phần thứ tự đi nhé, xem ta có thể đi được bao xa.

Ta sẽ tưởng tượng việc tạo ra một mảng $b$, với giá trị $b[i]$ là `true` khi và chỉ khi $a[i] < x$.

$b$ sẽ trông như thế nào? Một số (hoặc không có) các phần tử đầu tiên sẽ là `true`, và tất cả các phần tử còn lại sẽ là `false`.

Như vậy bài toán sẽ còn lại việc tìm chỉ số đầu tiên mà tại đó $b[i]$ là `false` (hoặc $n$ nếu không có). Giờ ta có thể quên đi $a$ và $x$, chỉ cần tập trung vào mảng $b$ thôi.

Ta thấy rằng, với bất kỳ mảng $b$ nào, ta cũng có thể tìm được giá trị `false` đầu tiên với cùng ý tưởng giảm không gian tìm kiếm đi một nửa.

Xài tí kí hiệu nhá. Gọi $[l_0, r_0]$ là đoạn mà ta cần tìm kiếm (trong bài toán của ta sẽ là $[0, n-1]$). $l$, $r$ sẽ là các chỉ số ta duy trì ở mỗi bước mà đoạn $[l_0, l]$ trong $b$ sẽ chỉ bao gồm các giá trị `true`, và đoạn $[r, r_0]$ trong $b$ sẽ chỉ bao gồm các giá trị `false`.

Ban đầu ta không có thông tin gì về các phần tử trong mảng $b$, nên các đoạn trên cần phải là các đoạn rỗng. Ta sẽ đặt $l = l_0 - 1$ và $r = r_0 + 1$ (đoạn $[l_0, l]$ và $[r, r_0]$ lúc này đều rỗng). Ta sẽ tăng $l$ và giảm $r$ sao cho hai đoạn này che phủ toàn bộ không gian tìm kiếm. Vậy cuối cùng thì $l$ sẽ là chỉ số cuối cùng mà tại đó $b[l]$ là `true`, và $r$ sẽ là chỉ số đầu tiên mà tại đó $b[r]$ là `false`, ta chỉ cần trả về $r$ là xong.

Giả sử tại một bước nào đó, $r - l > 1$, nghĩa là có ít nhất một phần tử nằm giữa hai chỉ số này mà ta chưa đặt vào một trong hai đoạn. Ta sẽ lấy phần tử giữa của đoạn $(l, r)$, là $m = \lfloor (l+r) / 2 \rfloor$.

- Nếu $b[m]$ là `true`, ta sẽ biết rằng tất cả phần tử nằm bên trái $b[m]$ cũng là `true`, nên ta có thể tăng đoạn $[l_0, l]$ lên thành $[l_0, m]$ (tương đương với việc đặt $l = m$).
- Nếu $b[m]$ là `false`, ta sẽ biết rằng tất cả phần tử nằm bên phải $b[m]$ cũng là `false`, nên ta có thể tăng đoạn $[r, r_0]$ lên thành $[m, r_0]$ (tương đương với việc đặt $r = m$).

Mỗi bước ta sẽ giảm đoạn chưa biết từ $r - l - 1$ xuống $r - m - 1$ hoặc $m - l - 1$, tức là giảm ít nhất một nửa. Vậy số bước sẽ là $\log_2 (r_0 - l_0 + 1) + 1$.

Cài đặt thì sẽ như sau:

```cpp
int find_first_false(const vector<bool>& b) {
    int l = -1;
    int r = (int)b.size();
    while (r - l > 1) {
        int m = l + (r - l) / 2;
        if (b[m]) {
            l = m;
        } else {
            r = m;
        }
    }
    return r;
}
```

Nhưng ta đã nói là không thực sự cần tạo mảng $b$ đúng không? Vậy dùng nó để giải quyết bài toán ban đầu như thế nào?

Để ý rằng $b[i]$ chỉ là giá trị của biểu thức $a[i] < x$, nên ta có thể tính nếu cần. Ta có thể thay $b[m]$ bằng $a[m] < x$ trong cài đặt trên và mọi thứ sẽ được giải quyết.

Khá tiện phải không, giờ ta có thể tóm lại ý mà ta đã phát biểu ở trên:

- Thay vì dùng thứ tự $<$ và giá trị $x$, ta tạo ra một mảng $b$ theo một dạng cụ thể nào đó (tiền tố của mảng $b$ là `true`, hậu tố là `false`), rồi tìm chỉ số đầu tiên mà tại đó $b[i]$ là `false`.

Điều này dẫn đến bài toán tổng quát như sau.

### Bài toán tìm kiếm nhị phân tổng quát

Ta có:

- $[l, r]$: một đoạn chỉ số (trong ví dụ trên là $[0, n-1]$).
- $f$: hàm ánh xạ số nguyên sang giá trị đúng sai, thỏa mãn tính chất sau: tồn tại sô $t$ sao cho với mọi $l \leq x < t$, $f(x)$ là `true`, và với mọi $t \leq i \leq r$, $f(i)$ là `false`.

Nếu cận trên của thời gian tính $f$ là $T(l,r)$, ta có thể tìm được chỉ số $t$ (chỉ số của giá trị `false` đầu tiên) trong thời gian $O(T(l,r) \log_2 (r - l + 1)) + O(1)$.

Hàm $f$ như vậy gọi là một predicate (tiên đề). Trong ví dụ ban đầu, $f$ được gọi là predicate luôn.

Cài đặt nó sẽ như sau (bỏ qua tràn số nhé):

```cpp
template <class Integer, class F>
Integer find_first_false(Integer l, Integer r, F&& f) {
    --l;
    ++r;
    while (r - l > 1) {
        Integer m = l + (r - l) / 2; // nên ưu tiên dùng std::midpoint trong C++20
        if (f(m)) {
            l = m;
        } else {
            r = m;
        }
    }
    return r;
}
```

Để ý rằng cài đặt này có tính chất khá hay rằng $l$ sẽ là chỉ số cuối cùng mà tại đó $f(l)$ là `true`, nên ta có thể tạo một hàm khác tương tự để trả về $l$ nếu cần.

Để dùng hàm này cho việc cài tìm kiếm nhị phân, ta làm như sau:

```cpp
int find_position(const vector<int>& a, int x) {
    auto f = [&](int i) {
        return a[i] < x;
    };
    int n = (int)a.size();
    int pos = find_first_false(0, n - 1, f);
    if (pos == n || a[pos] != x) return n;
    return pos;
}
```

Ta cũng có một kết luận khá hay ở đây: ta không thực sự cần $a$ phải được sắp xếp. Thứ duy nhất ta cần là mọi thử nhỏ hơn $x$ thì phải nằm ở tiền tố mảng, và phần còn lại phải nằm ở hậu tố mảng, và nếu $x$ nằm trong mảng, phần tử đầu tiên của hậu tố đó phải là $x$. Định nghĩa này cũng giải quyết được trường hợp có nhiều phần tử bằng $x$ trong mảng. Điều này sẽ giúp ta giải quyết được nhiều dạng bài toán hơn.

Bài tập: Bạn sẽ làm gì nếu trong $b$, một số phần tử đầu là `false`, còn lại là các phần tử `true`?

## Tìm kiếm nhị phân đáp án

Đôi khi sẽ dễ dàng hơn nếu ta xử lý cận trên dưới của đáp án hơn là chính cái đáp án đó.

Tức là, đôi khi nó sẽ dễ hơn nếu ta có một hàm $f$ trả về `true` khi và chỉ khi input $\leq$ đáp án cần tìm, bằng cách chạy một thuật toán nào đó trả về giá trị đúng sai bằng cách xét một số tính chất của bài toán và input.

Ví dụ, xét bài toán [sau](https://codeforces.com/contest/448/problem/D).

Ta sẽ có một bảng nhân với kích thước $n \times m$, ta cần tìm số nhỏ thứ $k$ trong bảng này (ví dụ nếu sắp xếp tất cả các số trong bảng theo thứ tự tăng dần, ta cần tìm số ở vị trí $k$).

Không dễ để tìm trực tiếp số này. Nhưng nếu ta "đoán" $x$, ta sẽ xem thử nó có gần với đáp án hay không:

Ta sẽ tìm số số nguyên nhỏ hơn $x$ trên mỗi hàng, rồi cộng lại. Ta có thể dùng phép chia đơn giản trên từng hàng.

Nếu tổng số các số nhỏ hơn $x$ nhỏ hơn $k$, ta sẽ trả về `true`, ngược lại trả về `false`. Hàm predicate này hiệu quả vì số các số nhỏ hơn $x$ là hàm không giảm trên $x$ (nghĩa là, nếu ta so sánh $f(x) và $f(x+1)$, và giả sử $f(x)$ trả về `false`, thì $f(x+1)$ chắc chắn cũng trả về `false`). Như vậy giá trị cuối cùng làm cho hàm trả về `true` sẽ là đáp án cần tìm.

Ta dùng tìm kiếm nhị phân để tìm ra đáp án như đã trình bày ở trên.

## Hai cách phổ biến khác để cài đặt tìm kiếm nhị phân

Ta sẽ tìm hiểu 2 cách khác mà người ta thường dùng để cài đặt tìm kiếm nhị phân và sao chúng lại dễ hiểu với họ.

Ta sẽ gọi cách mà ta dùng là cách $(l, r)$, vì nó tương đương với việc duy trì không gian tìm kiếm là đoạn $(l, r)$ (không bao gồm $l$ và $r$).

Phần này sẽ giúp người đọc hiểu hơn cách cài đặt tìm kiếm nhị phân của người khác và tìm ra cách cài đặt phù hợp với mình hơn. Cá nhân tôi (người viết bài) thích cách ở trên hơn, nên sẽ giải thích các cách sau dựa trên cách đó, với một số lý do vì sao người ta thích các cách này.

### Cách $[l, r]$ { data-toc-label='Cách [l, r]' }

Trong cách cài đặt này, ta sẽ duy trì $l+1$ và $r-1$ thay vì $l$ và $r$. Lý do là vì:

$[l, r]$ tương ứng với không gian tìm kiếm hiện tại. Ta sẽ duy trì thêm một giá trị $ans$ nữa, nó sẽ chứa đáp án tốt nhất hiện tại, nghĩa là chỉ số `false` bên trái nhất hiện tại.

Đoạn này không rỗng khi $r \geq l$. Điểm giữa thì cũng y như vậy, $m = \lfloor (l + r) / 2 \rfloor$. Nếu $f(m)$ là `false`, đáp án tốt nhất hiện tại sẽ là $m$, và ta sẽ giảm không gian tìm kiếm xuống thành $[l, m-1]$. Ngược lại, ta sẽ giảm không gian tìm kiếm thành $[m+1, r]$ và không cập nhật đáp án.

Để ý rằng ta sẽ phải duy trì biến $ans$ và khởi tạo nó một cách hợp lý, tùy vào việc ta muốn thằng `false` trái nhất (làm như trên) hay thằng `true` phải nhất (chuyển cập nhật giá trị sang khi $f(m)$ là `true`), đó cũng là lý do mà tôi không dùng cách này lâu rồi. Tuy nhiên, người ta có vẻ thích các dãy đóng nên cách này cũng khá phổ biến.

Một biến thể là khi ta có $l'$ và $r'$ giống với $l$ và $r$ trong cách $(l, r)$, và $l$, $r$ giống $l$ và $r$ trong cách này, khi đó $l' = l-1$ và $ans = r' = r+1$. Nếu muốn tìm thằng `true` phải nhất, ta sẽ có $r' = r+1$ và $ans = l' = l-1$.

Cài đặt như sau:

```cpp
template <class Integer, class F>
Integer find_first_false(Integer l, Integer r, F&& f) {
    Integer ans = n;
    while (l <= r) {
        Integer m = l + (r - l) / 2; // nên ưu tiên dùng std::midpoint trong C++20
        if (f(m)) {
            l = m + 1;
        } else {
            ans = m;
            r = m - 1;
        }
    }
    return ans;
}
```

### Cách $[l, r)$ { data-toc-label='Cách [l, r)' }

Trong cách này, ta sẽ duy trì $l+1$ và $r$ thay vì $l$ và $r$. Lý do là vì không gian tìm kiếm lúc này sẽ là $[l, r)$, nghĩa là bao gồm $l$ nhưng không bao gồm $r$, những người thích đoạn nửa mở sẽ thích cách này. Khi không gian tìm kiếm rỗng, ta sẽ có đoạn $[ans, ans)$ (nếu muốn tìm thằng `false` trái nhất). Cấu trúc của đoạn không khi nào cũng ứng với các cách khác, vì giá trị $m$ sẽ thường hơi khác một chút (thường sẽ là $\lfloor (l + r) / 2 \rfloor$ với $[l, r)$ là không gian tìm kiếm hiện tại, và trong trường hợp có 2 giá trị giữa, ta sẽ chọn giá trị bên phải, không phải bên trái).

Ta có thể hiểu như sau: Giả sử ta có đoạn $[l, r)$, và ta cần chèn một cái `false` sau thằng `true` cuối cùng trên đoạn đó. `false` này sẽ nằm ở đâu?

Một cách khác để nghĩ là: mọi thứ trong đoạn $[l, ans)$ là `true`, mọi thứ trong đoạn $[ans, r)$ là `false`. Nên $ans$ sẽ là một kiểu vách ngăn trên mảng. Ta sẽ xem cách giải thích này ứng dụng như thế nào trong cài đặt trong thư viện STL của C++ sau nhé.

Với điểm giữa của đoạn $[l, r)$, nếu $f(m)$ là `true`, ta sẽ không bao giở đặt `false` vào bất kỳ vị trí nào $\leq m$, nên $l$ sẽ thành $m+1$. Ngược lại, ta sẽ phải đặt nó vào vị trí $\leq m$, nên $r$ sẽ thành $m$.

```cpp
template <class Integer, class F>
Integer find_first_false(Integer l, Integer r, F&& f) {
    ++r;
    while (l < r) {
        Integer m = l + (r - l) / 2; // nên ưu tiên dùng std::midpoint trong C++20
        if (f(m)) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return r;
}
```

## Binary lifting cho tìm kiếm nhị phân

Ta sẽ đi lướt qua phần này thôi, vì ta sẽ chỉ xem xét tổng quan của hàm thay vì giải thích chi tiết.

Xét cài đặt sau:

```cpp
template <class Integer, class F>
Integer find_first_false(Integer l, Integer r, F&& f) {
    if (l > r) return r + 1;
    ++r;
    Integer w = Integer(1) << __lg(r - l);
    --l;
    if (f(l + w)) l = r - w;
    for (w >>= 1; w >= Integer(1); w >>= 1)
        if (f(l + w)) l += w;
    return l + 1;
}
```

Ở đây ta cần đảm bảo rằng độ dài các đoạn là lũy thừa của $2$. Lý do vì sao thì ta sẽ giải thích trong phần tối ưu tìm kiếm nhị phân sau.

Sau khi chắc rằng độ dài đoạn là lũy thừa của $2$, ta chỉ cần tạo biểu diễn nhị phân của $ans - 1 - l$, với $ans$ là giá trị trả về. Ta có thể đi từ bit lớn nhất đến bit nhỏ nhất, và tham lam ở đây với lý do là biểu diễn nhị phân là duy nhất; và dần dần thêm các lũy thừa của $2$ vào khi hàm $f$ vẫn còn trả về `true`.

## Tìm kiếm nhị phân theo ngôn ngữ lập trình

Các ngôn ngữ lập trình phổ biến trong lập trình thi đấu đều có các hàm thư viện để hỗ trợ bạn tìm kiếm nhị phân.

### C++

- `binary_search`: Hàm này trả về một giá trị đúng sai, cho biết phần tử có tồn tại giữa 2 iterator hay không (với một hàm so sánh tùy chọn).
- `lower_bound`, `upper_bound`: Nếu đoạn có phần tử $x$ cần tìm được định nghĩa bởi cặp iterator $[it_l, it_r)$ nằm trong đoạn ban đầu $[\text{input_it}_l, \text{input_it}_r)$, thì `lower_bound` và `upper_bound` lần lượt trả về  $it_l$ và $it_r$. Nói cách khác, `lower_bound(it1, it2, x, comp)` trả về iterator đến phần tử đầu tiên của đoạn iterator $[it1, it2)$, đoạn này $\geq x$ theo hàm so sánh `comp` (tùy chọn và mặc định là thứ tự tăng dần), và `upper_bound` làm y vậy với phần tử $> x$.
- `equal_range`: Trả về cả `lower_bound` và `upper_bound` trong một lần gọi hàm.
- `partition_point`: Giống y như hàm tìm kiếm nhị phân theo cách $[l, r)$ đã trình bày ở trên. Trong C++20, với `ranges::views::iota`, ta có thể dùng nó để tìm kiếm nhị phân đáp án.

### Python

- Module `bisect` có các hàm như `bisect`, `bisect_left`, `bisect_right` có chức năng tương tự như `lower_bound` và `upper_bound`.

### Java

- `Collections.binarySearch` và `Arrays.binarySearch` có chức năng tương tự việc tìm kiếm một phần tử hay chỉ số (không nhất thiết là phần tử đầu tiên hay cuối cùng) với tìm kiếm nhị phân.

## Tối ưu tìm kiếm nhị phân

Trong cài đặt ban đầu, ta trả về ngay khi ta tìm thấy phần tử cần tìm. Đôi khi, sẽ nhanh hơn khi ta dừng tìm kiếm sớm, và trong các trường hợp như vậy, nó là tối ưu theo constant factor.

Binary lifting ở trên cũng là một cách tối ưu theo constant factor trên một số kiến trúc nếu được triển khai thủ công (khả thi do tính chất đơn giản của số tăng và khả năng hardcoding các hằng số), theo cuốn Programming Pearls của John Bentley. Đây là một cải tiến trong một số trường hợp, khi các vị trí tìm kiếm nhị phân ít và lặp lại trong các ứng dụng tìm kiếm nhị phân liên tiếp, dẫn đến việc sử dụng cache tốt hơn. Một ví dụ về việc thực hiện tối ưu hóa đến mức tối đa là việc triển khai nhiều hàm (mỗi hàm có lũy thừa của $2$ khác nhau), lưu các con trỏ hàm trong một mảng và dùng các lệnh nhảy (ví dụ, bằng cách tính lũy thừa $2$ khi cần) để đến đúng hàm khi chạy, giúp tăng tốc trên một số kiến trúc nhất định.

Ví dụ, với một số loại truy vấn nhất định ($l$ hoặc $r$ ít nhiều giống nhau), tốc độ tăng đáng kể. Tuy nhiên, đối với các loại truy vấn khác, phiên bản đơn giản hơn lại hiệu quả hơn. Để thể hiện mức độ tăng tốc bạn có thể đạt được cho một số loại truy vấn nhất định, tôi đã thực hiện một số benchmark trên các truy vấn mà giới hạn bên trái luôn giống nhau. Với code benchmark bên dưới, kết quả như sau:

??? tip "Code benchmark"
    ```cpp
    #pragma GCC optimize("O3,unroll-loops")
    #pragma GCC target("avx2,bmi,bmi2,popcnt,lzcnt")
    #include "bits/stdc++.h"

    using ll = int64_t;
    using ld = long double;

    using namespace std;

    template <typename C = std::chrono::steady_clock,
            typename T1 = std::chrono::nanoseconds,
            typename T2 = std::chrono::milliseconds>
    struct Stopwatch {
        std::string name;
        std::chrono::time_point<C> last_played;
        T1 elapsed_time;
        bool running;
        Stopwatch(const std::string& s) : name(s), running(true) { reset(); }
        Stopwatch() : Stopwatch("Time") {}
        void reset() {
            last_played = C::now();
            elapsed_time = T1::zero();
        }
        void pause() {
            if (!running) return;
            running = false;
            elapsed_time += std::chrono::duration_cast<T1>(C::now() - last_played);
        }
        void play() {
            if (running) return;
            running = true;
            last_played = C::now();
        }
        int_fast64_t elapsed() const {
            return std::chrono::duration_cast<T2>(
                    elapsed_time + (running ? std::chrono::duration_cast<T1>(
                                                    C::now() - last_played)
                                            : T1::zero()))
                .count();
        }
        void print() const { std::cerr << name << ": " << elapsed() << " ms\n"; }
        ~Stopwatch() { print(); }
    };
    struct Random : std::mt19937 {
        using std::mt19937::mt19937;
        using std::mt19937::operator();
        static int64_t gen_seed() {
            return 42;
            // return std::chrono::steady_clock::now().time_since_epoch().count();
        }
        Random() : std::mt19937(gen_seed()) {}
        template <class Int>
        auto operator()(Int a, Int b)
            -> std::enable_if_t<std::is_integral_v<Int>, Int> {
            return std::uniform_int_distribution<Int>(a, b)(*this);
        }
        template <class Int>
        auto operator()(Int a) -> std::enable_if_t<std::is_integral_v<Int>, Int> {
            return std::uniform_int_distribution<Int>(0, a - 1)(*this);
        }
        template <class Real>
        auto operator()(Real a, Real b)
            -> std::enable_if_t<std::is_floating_point_v<Real>, Real> {
            return std::uniform_real_distribution<Real>(a, b)(*this);
        }
    };

    template <class Integer, class F>
    Integer find_first_false(Integer l, Integer r, F&& f) {
        --l, ++r;
        while (r - l > 1) {
            auto mid = l + (r - l) / 2;
            if (f(mid))
                l = mid;
            else
                r = mid;
        }
        return r;
    }

    template <class Integer, class F>
    Integer lifting_find_first_false(Integer l, Integer r, F&& f) {
        if (l > r) return r + 1;
        ++r;
        Integer w = Integer(1) << __lg(r - l);
        --l;
        if (f(l + w)) l = r - w;
        for (w >>= 1; w >= Integer(1); w >>= 1)
            if (f(l + w)) l += w;
        return l + 1;
    }

    template <class Integer, class F>
    Integer unrolled_find_first_false(Integer l, Integer r,
                                    F&& f) requires(sizeof(Integer) == 4) {
        if (l > r) return r + 1;
        ++r;
        int p = __lg(r - l);
        Integer w = Integer(1) << p;
        --l;
        if (f(l + w)) l = r - w;
        switch (p) {
            case 31:
                if (f(l + (1 << 30))) l += 1 << 30;
            case 30:
                if (f(l + (1 << 29))) l += 1 << 29;
            case 29:
                if (f(l + (1 << 28))) l += 1 << 28;
            case 28:
                if (f(l + (1 << 27))) l += 1 << 27;
            case 27:
                if (f(l + (1 << 26))) l += 1 << 26;
            case 26:
                if (f(l + (1 << 25))) l += 1 << 25;
            case 25:
                if (f(l + (1 << 24))) l += 1 << 24;
            case 24:
                if (f(l + (1 << 23))) l += 1 << 23;
            case 23:
                if (f(l + (1 << 22))) l += 1 << 22;
            case 22:
                if (f(l + (1 << 21))) l += 1 << 21;
            case 21:
                if (f(l + (1 << 20))) l += 1 << 20;
            case 20:
                if (f(l + (1 << 19))) l += 1 << 19;
            case 19:
                if (f(l + (1 << 18))) l += 1 << 18;
            case 18:
                if (f(l + (1 << 17))) l += 1 << 17;
            case 17:
                if (f(l + (1 << 16))) l += 1 << 16;
            case 16:
                if (f(l + (1 << 15))) l += 1 << 15;
            case 15:
                if (f(l + (1 << 14))) l += 1 << 14;
            case 14:
                if (f(l + (1 << 13))) l += 1 << 13;
            case 13:
                if (f(l + (1 << 12))) l += 1 << 12;
            case 12:
                if (f(l + (1 << 11))) l += 1 << 11;
            case 11:
                if (f(l + (1 << 10))) l += 1 << 10;
            case 10:
                if (f(l + (1 << 9))) l += 1 << 9;
            case 9:
                if (f(l + (1 << 8))) l += 1 << 8;
            case 8:
                if (f(l + (1 << 7))) l += 1 << 7;
            case 7:
                if (f(l + (1 << 6))) l += 1 << 6;
            case 6:
                if (f(l + (1 << 5))) l += 1 << 5;
            case 5:
                if (f(l + (1 << 4))) l += 1 << 4;
            case 4:
                if (f(l + (1 << 3))) l += 1 << 3;
            case 3:
                if (f(l + (1 << 2))) l += 1 << 2;
            case 2:
                if (f(l + (1 << 1))) l += 1 << 1;
            case 1:
                if (f(l + (1 << 0))) l += 1 << 0;
            default:
                break;
        }
        return l + 1;
    }

    void test2() {
        Random rng;
        int n = 4e6;
        vector<int> a(n);
        generate(begin(a), end(a), [&] { return rng(1, 2 * n); });
        sort(begin(a), end(a));
        ll ans = 0;
        Stopwatch timer;
        for (int i = 0; i < n; ++i) {
            int q = rng(1, 2 * n);
            int d = rng(n);
            ans ^= find_first_false(0, d, [&](int i) { return a[i] < q; });
        }
        cout << "-----------------------------\n";
        cout << "Simple binary search\n";
        cout << ans << '\n';
    }

    void test3() {
        Random rng;
        int n = 4e6;
        vector<int> a(n);
        generate(begin(a), end(a), [&] { return rng(1, 2 * n); });
        sort(begin(a), end(a));
        ll ans = 0;
        Stopwatch timer;
        for (int i = 0; i < n; ++i) {
            int q = rng(1, 2 * n);
            int d = rng(n);
            ans ^= lifting_find_first_false(0, d, [&](int i) { return a[i] < q; });
        }
        cout << "-----------------------------\n";
        cout << "Binary lifting\n";
        cout << ans << '\n';
    }

    void test4() {
        Random rng;
        int n = 4e6;
        vector<int> a(n);
        generate(begin(a), end(a), [&] { return rng(1, 2 * n); });
        sort(begin(a), end(a));
        ll ans = 0;
        Stopwatch timer;
        for (int i = 0; i < n; ++i) {
            int q = rng(1, 2 * n);
            int d = rng(n);
            ans ^= unrolled_find_first_false(0, d, [&](int i) { return a[i] < q; });
        }
        cout << "-----------------------------\n";
        cout << "Binary lifting with unrolling\n";
        cout << ans << '\n';
    }

    int main() {
        int _tests = 1;
        // cin >> _tests;
        for (int _test = 1; _test <= _tests; ++_test) {
            // cout << "Case #" << _test << ": ";
            test2();
            test3();
            test4();
            cout << "-----------------------------\n";
        }
    }
    ```

Kết quả:

```
-----------------------------
Simple binary search
744175
Time: 2184 ms
-----------------------------
Binary lifting
744175
Time: 1504 ms
-----------------------------
Binary lifting with unrolling
744175
Time: 1407 ms
-----------------------------
```

[https://algorithmica.org/en/eytzinger](https://algorithmica.org/en/eytzinger) giải thích một cách khá hay về việc khai thác cache và tăng tốc tìm kiếm nhị phân trong một số trường hợp nhất định với một hệ số khá ấn tượng.

[https://codeforces.com/blog/entry/76182](https://codeforces.com/blog/entry/76182) giải thích một biến thể của tìm kiếm nhị phân chia đoạn không đều, điều này có thể dẫn đến sự thay đổi về mặt độ phức tạp tính toán.

## Tài liệu tham khảo

Bạn có thể tham khảo các tài liệu sau để luyện tập và hiểu thêm về tìm kiếm nhị phân.

Codeforce EDU tutorial (và các bài tập) về tìm kiếm nhị phân.

Một video khá hay giải thích tìm kiếm nhị phân trong post này: [https://codeforces.com/blog/entry/67509](https://codeforces.com/blog/entry/67509).

Một bản mở rộng của tìm kiếm nhị phân gọi là tìm kiếm nhị phân song song (parallel binary search), bài [https://codeforces.com/blog/entry/89694](https://codeforces.com/blog/entry/89694) có một video khá hay về nó.

Binary lifting là một khái niệm chung chung. Hướng dẫn binary lifting trên cây Fenwick có thể tham khảo ở đây [https://codeforces.com/blog/entry/61364](https://codeforces.com/blog/entry/61364). Binary lifting trên cây có thể tham khảo ở đây [https://usaco.guide/plat/binary-jump?lang=cpp](https://usaco.guide/plat/binary-jump?lang=cpp).

Tìm kiếm nhị phân trên segment tree cũng là một kỹ thuật hay, cài đặt và giải thích cho recursive segment tree có thể tham khảo ở đây [https://codeforces.com/blog/entry/83883](https://codeforces.com/blog/entry/83883). Với iterative segment tree, bạn có thể tham khảo cài đặt ở đây [https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp](https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp). Ý tưởng của nó như sau:

??? tip "Ý tưởng"
    Để ý rằng node con của node `x` là các node `(x << 1)` và `(x << 1) | 1`. Ta làm như sau: lấy node tổ tiên của `r` thỏa `predicate(node) = true` (không nhất thiết là tổ tiên, chỉ cần là một node thỏa mãn tính chất sau: nếu đáp án là `l`, node ta cần sẽ là node con bên trái của tổ tiên chung của các node lá tương ứng với `l` và `r`). Khi có được vị trí đó rồi, ta sẽ đi xuống theo segment tree, vì ta biết được đáp án sẽ nằm ở cây con nào (ta sẽ bỏ qua được điều kiện `l < r`).

    ```cpp
    // For implementing this for a lazy segtree, ensure that you have pushed the updates accumulated at ancestors appropriately before accessing the value at a node
    template <class F> int min_left(int r, F f) const {
        assert(0 <= r && r <= _n); // precondition check
        assert(f(e())); // f should evaluate true on the empty range
        if (r == 0) return 0; // has to be empty
        r += size; // get the leaf
        S sm = e(); // accumulator variable
        do {
            r--;
            while (r > 1 && (r % 2)) r >>= 1; // get the highest ancestor of this node which shares the right boundary with this node
            if (!f(op(d[r], sm))) { // if the range (left(ancestor), right(query)) doesn't work, we have found a node which contains the leaf corresponding to the answer in the subtree
                while (r < size) {
                    r = (2 * r + 1); // go to the right child
                    if (f(op(d[r], sm))) { // if right child works, go to the left, else remain there
                        sm = op(d[r], sm);
                        r--;
                    }
                }
                return r + 1 - size;
            }
            sm = op(d[r], sm); // otherwise just update the accumulator and go to the node left of the highest ancestor we found earlier
        } while ((r & -r) != r);
        return 0;
    }
    ```

    Giải thích cho `max_right` cũng tương tự.