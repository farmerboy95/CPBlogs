# Floor, ceiling và bất đẳng thức cho người mới học

## Nguồn

<img src="../../../../img/codeforces.png" width="16" height="16"/> [[Tutorial] Floors, ceilings and inequalities for beginners (with some programming tips)](https://codeforces.com/blog/entry/113633)

## Cơ bản về bất đẳng thức

Trước khi đến với floor và ceiling, ta cần bàn về bất đẳng thức. Giả sử ta đã có một số kiến thức cơ bản về [trục số](https://en.wikipedia.org/wiki/Number_line), ta cùng đi qua một số khái niệm sau:

- Ta nói $a < b$ khi và chỉ khi $a$ ở trước $b$ trên trục số. Số ở đây là số thực.
- Ta nói $a = b$ khi và chỉ khi $a$ và $b$ trùng nhau trên trục số.
- Ta nói $a > b$ khi và chỉ khi $b < a$, nghĩa là $a$ ở sau $b$ trên trục số.
- Ta nói $a \le b$ khi và chỉ khi $a < b$ hoặc $a = b$.
- Ta nói $a \ge b$ khi và chỉ khi $a > b$ hoặc $a = b$.

Luật tam phân quy định như sau: 

- Chỉ có một trong số các quan hệ này là đúng: $a < b$, $a = b$, $a > b$.

Thứ này rất có ích khi bạn muốn chia trường hợp hoặc phản chứng.

Hệ quả tất yếu của điều này là định nghĩa sau đây về các quan hệ dưới dạng $<$ và phủ định (bạn có thể sử dụng bất kỳ quan hệ nào khác $=$ để hiểu tất cả những thứ khác):

- $a = b$ khi và chỉ khi $a \not < b$ và $b \not < a$.
- $a > b$ khi và chỉ khi $b < a$.
- $a \le b$ khi và chỉ khi $b \not < a$.
- $a \ge b$ khi và chỉ khi $a \not < b$.

Để ý rằng nếu ta có một số kết quả về $<$, với các quan hệ trên, ta có thể tìm ra các quan hệ tương ứng với các điều kiện trên.

Ta cũng có thể viết các quan hệ trên theo $\le$ - đây sẽ là bài tập cho các bạn để xác nhận rằng bạn đã hiểu logic đằng sau.

Hiểu được những điều trên sẽ giúp các bạn tìm ra logic của bất đẳng thức dễ dàng hơn.

## Tạo chuỗi các quan hệ

Giả sử $aRb$ và $bRc$ đều đúng, với R là một trong $<$, $>$, $=$, $\le$, $\ge$, ta dễ dàng suy ra $aRc$ cũng đúng. Điều này cho phép ta tạo chuỗi các bất đẳng thức, và viết ra những thứ như $a < b < c$ và nhớ rằng vì ta đọc biểu thức từ trái sang phải, các toán hạng chỉ có tăng.

Tính chất này gọi là bắc cầu, và được nghiên cứu kỹ trong các ngữ cảnh khác. Nhưng với mục đích của chúng ta, nó chỉ giúp đời ta đơn giản hơn thôi.

Đến đây, ta có 2 lưu ý quan trong sau:

- Nếu $a < b$ và $b > c$, ta không thể nói gì về thứ tự của $a$ và $c$. Các bạn mới học mắc lỗi này rất nhiều.
- $<$ là một mệnh đề mạnh hơn $\le$. Ví dụ, ta có $a < b$ và $b \le c$, thì sẽ không có $a = c$. Nên ta có thể nói rằng $a < c$, thay vì mệnh đề yếu hơn $a \le c$. Theo một cách toán học hơn, ta có thể giải thích theo kiểu: $b \le c$ nghĩa là $b < c$ hoặc $b = c$. Trong trường hợp đầu, chuỗi quan hệ đúng. Trong trường hợp thứ hai, vì $b = c$, vị trí của $b$ và $c$ trên trục số trùng nhau, nên kết quả vẫn đúng. 

## Các phép toán số học ảnh hưởng đến bất đẳng thức như thế nào?

Đây là thứ mà nhiều người gặp khó. Ta sẽ đi vào giải thích một số tương tác của các phép toán số học và bất đẳng thức (ta sẽ tập trung vào dấu $<$, nhưng các quan hệ như thế có thể được phát triển cho các quan hệ khác như $>$, $\le$ và sự kết hợp của chúng nữa):

- Phép cộng / phép trừ: giả sử ta có bất đẳng thức $a < b$. Nếu ta di chuyển chúng cùng một đoạn trên trục số, vị trí tương đối của chúng sẽ không đổi. Nói cách khác, nếu ta thêm hằng số $c$ vào cả $a$ và $b$, thứ tự tương đối của $a + c$ và $b + c$ sẽ giống như của $a$ và $b$. Nghĩa là, $a < b$ suy ra $a + c < b + c$. Điều tương tự xảy ra với phép trừ, như vậy ta có quan hệ tương đương:

$$ a < b \iff a + c < b + c $$

- Phép nhân với $0$: cả hai về của bất đẳng thức về $0$, nên sau khi nhân với $0$, bất đẳng thức trở thành đẳng thức.
- Phép nhân với số dương: giả sử ta có bất đẳng thức $a < b$. Điều này nghĩa là $0 < b - a$, nghĩa là $b - a$ dương. Nếu ta nhân nó với một số dương $c$, nó vẫn sẽ dương, nghĩa là $0 < c (b - a)$. Cộng $ac$ vào cả hai vế ta có $ac < bc$. Vì vậy:

$$ c > 0, a < b \implies ac < bc $$

- Phép nhân với số âm: giả sử ta có bất đẳng thức $a < b$ và một số âm $c < 0$. Rõ ràng, ta có $a(-c) < b(-c)$ từ kết quả trước. Cộng $ac + bc$ cho cả hai vế ta có $bc < ac$, hay $ac > bc$. Nghĩa là dấu của bất đẳng thức bị đảo. Vì vậy:

$$ c < 0, a < b \implies ac > bc $$

- Công hai bất đẳng thức cùng chiều: giả sử ta có hai bất đẳng thức $a < b$ và $c < d$. Thì $a + c < b + d$ phải không? Ta thử dùng các kết quả trước để chứng minh. Trừ $c$ cho cả hai vế của bất đẳng thức, thì $a + c < b + d \iff a < b + d - c$. Để ý rằng $c < d$, tương tự ta sẽ có $0 < d - c$. Điều này có nghĩa là $d - c$ là số dương. Nếu ta di chuyển $b$ đơn vị của một số dương sang bên phải trên trục số, ta đang di chuyển $b$ ra xa $a$, và nó vẫn sẽ lớn hơn $a$, có nghĩa là $a < b + d - c$. Với phép tương đương trước đó, $a + c < b + d$ đúng. Vì vậy:

$$ a < b, c < d \implies a + c < b + d $$

- Trừ hai bất đẳng thức ngược chiều: giả sử ta có hai bất đẳng thức $a < b$ và $c > d$. Thì $a - c < b - d$ phải không? Ta nhân $c > d$ với $-1$ được $-c < -d$. Vậy ta có $a - c < b - d$ với kết quả trước đó. Vì vậy:

$$ a < b, c > d \implies a - c < b - d $$

**LƯU Ý**: Trừ các bất đẳng thức cùng chiều và cộng các bất đẳng thức khác chiều đều không được, và bài tập dành cho bạn là xem các bước chứng minh trên sai ở đâu với các trường hợp đó.

Nhân và chia bất đẳng thức phức tạp hơn rất nhiều, nhưng có thể được áp dụng với ý tưởng tương tự. Cụ thể là, với phép nhân hai bất đẳng thức, bạn phải kiểm tra dấu của cả $4$ vế. Với phép chia, cách thức cũng tương tự, nhưng thêm vào đó bạn cần xử lý trường hợp mẫu số khác $0$.

## Floor và ceiling

Ta bắt đầu với định nghĩa hàm floor và ceiling:

- Hàm **floor** là một hàm $\lfloor \cdot \rfloor : \mathbb{R} \to \mathbb{Z}$ mà với mọi số thực $x$, $\lfloor x \rfloor$ là số nguyên $n$ mà $n \le x < n + 1$.
- Hàm **ceiling** là một hàm $\lceil \cdot \rceil : \mathbb{R} \to \mathbb{Z}$ mà với mọi số thực $x$, $\lceil x \rceil$ là số nguyên $n$ mà $n-1 < x \le n$.

Rõ ràng, nếu $n$ tồn tại, nó là duy nhất.

Tại sao những định nghĩa này hợp lý? Để ý rằng các đoạn $[n, n+1)$ với số nguyên $n$ bao phủ trục số, các đoạn này không lấn vào nhau, nên $x$ sẽ luôn nằm trên một trong các đoạn này. Tính chất này cũng tương tự với các đoạn $(n-1, n]$.

Với trường hợp đặc biệt, khi $x$ là số nguyên, cả hai hàm đều trả về $n$.

**LƯU Ý**: Nhớ rằng $\lfloor 1.5 \rfloor = 1$, nhưng $\lfloor -1.5 \rfloor = -2$, không phải $-1$.

Ta nhận ra được rằng:

- $\lfloor x \rfloor$ là số nguyên $n$ lớn nhất mà $n \le x$.
- $\lceil x \rceil$ là số nguyên $n$ nhỏ nhất mà $x \le n$.

Ta chứng minh từ định nghĩa (ở đây ta chỉ chứng minh với floor, còn ceiling thì tương tự): Giả sử rằng nó không đúng, và tồn tại $a > n$ mà $a \le x$. $a > n$ nghĩa là $a \ge n+1$. Nhưng ta biết rằng $x < n+1 \le a$, nên $x < a$ (mâu thuẫn).

Lưu ý, ta có hệ quả $\lfloor x \rfloor \le \lceil x \rceil$, và chúng hơn kém nhau $1$ khi và chỉ khi $x$ không phải là số nguyên. Khi $x$ là số nguyên, chúng sẽ đều bằng $x$.

Ta có thể viết lại chúng như sau để tiện hơn trong việc giải các bài tập.

- Với một số nguyên $n$ và một số thực $x$, thì $n \le x \iff n \le \lfloor x \rfloor$.
- Với một số nguyên $n$ và một số thực $x$, thì $n \ge x \iff n \ge \lceil x \rceil$.

Điều này đặc biệt quan trọng vì các phần tương đương này giúp ta giảm đi rất nhiều các trường hợp khi giải bất đẳng thức, ví dụ như:

??? tip "Ví dụ"
    Đây là comment từ bài [blog này](https://codeforces.com/blog/entry/113259?#comment-1007819).
    
    **Đề bài**: Cho A, C mà $\lceil \frac{A}{B} \rceil < C$. Tìm B nhỏ nhất có thể.
    
    Người viết dùng tìm kiếm nhị phân để tìm B, tuy nhiên có một cách tốt hơn từ comment đó.

    Giả sử $A, B, C$ đều là số nguyên (ngược lại thì chứng minh không hợp lý hoặc không đúng).

    Với mọi số thực $x$ và số nguyên $n$, theo định nghĩa hàm ceiling, ta có:

    - $x \le n$
    - $\lceil x \rceil \le n$

    Để ý rằng vì $\lceil \frac{A}{B} \rceil$ và $C$ đều là số nguyên, $\lceil \frac{A}{B} \rceil < C$ tương đương với $\lceil \frac{A}{B} \rceil \le C - 1$. Kết hợp các điều kiện đó nghĩa là điều kiện ban đầu tương đương $\lceil \frac{A}{B} \rceil \le C - 1$.

    Ta không thể đi tiếp được trừ phi biết dấu của $C - 1$ và giới hạn của B. Rõ ràng, nếu $C > 1$ và $B$ có thể âm, thì $B = -\infty$ là đáp án (hoặc chính xác hơn là $B$ nhỏ nhất không tồn tại). Tương tự, có thể không có đáp án nếu $C < 1$. Giờ ta giả sử $C > 1$ và $B$ chỉ có thể là số nguyên dương.

    Bất đẳng thức bây giờ sẽ tương đương với $B \ge \frac{A}{C-1}$. Với hai gạch đầu dòng ở trên thì ta sẽ có $B \ge \lceil \frac{A}{C-1} \rceil$.

    Vì tất cả đều tương đương, $B$ nhỏ nhất ta cần tìm chính là đây.

    Sau cùng, mấu chốt là phải quen với tính chất của ceiling và floor và thoải mái với đại số và các phép biến đổi bất đẳng thức.


Ta hãy viết lại định nghĩa theo cách khác luôn xem. $n \le x < n + 1$ tương đương với hai bất đẳng thửc $n \le x$ và $x < n + 1$. Bất đẳng thức $x < n + 1$ lại tương đương với $x - 1 < n$. Nên kết hợp lại ta sẽ có $x - 1 < n \le x$. Các bước này đảo lại được, nên nghĩa là đây có thể dùng làm định nghĩa của hàm floor. Tương tự với hàm ceiling, ta có các tính chất sau đây (như là định nghĩa thay thế):

- $x - 1 < \lfloor x \rfloor \le x$
- $x \le \lceil x \rceil < x + 1$

Đôi khi sẽ hữu ích khi nghĩ về phần phân số của một số (ví dụ như khoảng cách từ floor), vì nó chắc chắn là một số thực dương nhỏ hơn $1$. Tương tự, khoảng cách đến ceiling cũng hữu ích.

## Các tính chất của floor và ceiling

Ta cùng xem chuyện gì sẽ xảy ra với floor của một số thực khi ta cộng nó (tương tự với trừ) với một số nguyên.

Cho $n' = \lfloor x + a \rfloor$, với $a$ là một số nguyên. Điều này tương đương với $n' \le x + a < n' + 1$, tương đương tiếp với $n' - a \le x < n' - a + 1$. Vì $n'$ là một số nguyên, $n' - a$ cũng là một số nguyên. Nên bất đẳng thức trước cũng tương đương với việc nói rằng $n' - a = \lfloor x \rfloor$. Nói cách khác, ta đã cho thấy rằng:

$$a \in \mathbb{Z} \implies \lfloor x + a \rfloor = \lfloor x \rfloor + a$$

Tương tự, ta cũng chứng minh được rằng:

$$a \in \mathbb{Z} \implies \lceil x + a \rceil = \lceil x \rceil + a$$

Tuy nhiên, identity này không đúng với phép nhân số nguyên trong trường hợp tổng quát. Ví dụ $\lfloor 1.5 \rfloor = 1$, và $\lfloor 2 \cdot 1.5 \rfloor = 3 \ne 2 \cdot \lfloor 1.5 \rfloor$.

Lưu ý, với cùng ví dụ, ta có thể thấy rằng $\lfloor x + y \rfloor$ **KHÔNG** bằng $\lfloor x \rfloor + \lfloor y \rfloor$ trong trường hợp tổng quát (và tương tự với hàm ceiling). Tuy nhiên, ta có thể chứng minh được các identity sau:

$$\lfloor x \rfloor + \lfloor y \rfloor \le \lfloor x + y \rfloor \le \lfloor x \rfloor + \lfloor y \rfloor + 1$$

$$\lceil x \rceil + \lceil y \rceil - 1 \le \lceil x + y \rceil \le \lceil x \rceil + \lceil y \rceil$$

Giờ ta hãy xem chuyện gì xảy ra khi nhân đối số của các hàm với $-1$.

Từ $n \le x < n + 1 \iff -n - 1 < -x \le -n$, ta có thể thấy rằng $-\lfloor x \rfloor = \lceil -x \rceil$. Thay $x$ bằng $-x$ ta sẽ có $\lfloor -x \rfloor = - \lceil x \rceil$.

Vì hàm ceiling và floor trả về số nguyên, dùng bao nhiêu lần floor và ceiling lên kết quả sẽ không đổi kết quả sau khi dùng một lần.

Một tính chất hay ho khác có thể giúp bạn là, với một số nguyên dương $n$ và số thực $x$ bất kỳ:

- $\lfloor \frac{\lfloor x \rfloor}{n} \rfloor = \lfloor \frac{x}{n} \rfloor$
- $\lceil \frac{\lceil x \rceil}{n} \rceil = \lceil \frac{x}{n} \rceil$

Chứng minh điều này cần một số kiến thức về bổ đề chia Euclid (dư khi chia một số nguyên cho một số nguyên dương là một số nguyên không âm nhỏ hơn số nguyên dương đó), và đây là bài tập dành cho bạn đọc.

Về các ứng dụng và tính chất khác, vui lòng tham khảo [Wikipedia](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions).

## Một số ứng dụng của floor và ceiling

- Thương và số dư: Thương của phép chia số nguyên dương $a$ với một số nguyên dương $b$ khác theo định nghĩa là $\lfloor \frac{a}{b} \rfloor$. Dư sẽ là $a - b * \lfloor \frac{a}{b} \rfloor$.
- Để đếm số bộ của $a$ mà $\le n$, để ý rằng nếu ta có $k$ bội, thì bội lớn nhất của $a$ là $ka$, và nó phải $\le n$. Vì thế $k \le \frac{n}{a}$. Đây cũng là điều kiện đủ để có ít nhất $k$ bội của $a$ nhỏ hơn hoặc bằng $n$, nên $k = \lfloor \frac{n}{a} \rfloor$ theo cực đại của $k$.

## Áp dụng những điều trên để giải bài tập

Giờ ta đã có các công cụ, ta sẽ đi vào cách để giải các bài tập mà không bị mắc kẹt ở quá nhiều trường hợp. Ví dụ ở trên là một cách để suy nghĩ.

### Bài 1

Đây là bài tập [AtCoder ABC165 - D](https://atcoder.jp/contests/abc165/tasks/abc165_d).

**Đề bài**: Cho các số nguyên dương $A$, $B$, và $N$. Tìm giá trị lớn nhất của $\lfloor \frac{Ax}{B} \rfloor - A \times \lfloor \frac{x}{B} \rfloor$ với một số nguyên không âm $x$ không lớn hơn N.

**Giới hạn**: 

- $1 \le N \le 10^6$
- $1 \le A, B \le 10^{12}$

**Cách giải**:

Gọi $f(x) = \lfloor \frac{Ax}{B} \rfloor - A \times \lfloor \frac{x}{B} \rfloor$. 

Dễ thấy $f(x + B) = f(x)$. Cho nên ta chỉ cần quan tâm $0 \le x \le B-1$.

Vậy thì, $f(x) = \lfloor \frac{Ax}{B} \rfloor - A \times \lfloor \frac{x}{B} \rfloor = \lfloor \frac{Ax}{B} \rfloor$, và vì $\lfloor \frac{Ax}{B} \rfloor$ là hàm đơn điệu không giảm, nên với $x$ lớn nhất trong phần giới hạn ($0 \le x \le B-1$, $0 \le x \le N$), $f(x)$ chính là giá trị cần tìm. 

Như vậy kết quả là $f(\min(B-1, N))$.

Code mẫu:

```cpp
#include <bits/stdc++.h>

using namespace std;
 
int main() {
    long long A, B, N;
    cin >> A >> B >> N;

    long long x = 0;
    if (N >= B) x = B - 1;
    else x = N;

    cout << (A * x) / B - A * (x / B);
    return 0;
}
```

### Bài 2

Đây là bài tập [AtCoder ABC230 - E](https://atcoder.jp/contests/abc230/tasks/abc230_e).

**Đề bài**: Cho số nguyên dương $N$. Tìm giá trị của $\sum_{i = 1}^{N} \lfloor \frac{N}{i} \rfloor$.

**Giới hạn**:

- $1 \le N \le 10^{12}$
- N là số nguyên

**Cách giải**:

Để ý rằng $1 \le \lfloor \frac{N}{i} \rfloor \le N$ với mọi $1 \le i \le N$.

Gọi $k_0 = \lfloor \sqrt{N} \rfloor$. Với mỗi $k = 1, 2, \ldots, k_0$, xét số các số $i$ mà $\lfloor \frac{N}{i} \rfloor = k$.

$\lfloor \frac{N}{i} \rfloor = k$, nghĩa là $k \le \frac{N}{i} < k + 1$, tương đương với $\frac{N}{k+1} < i \le \frac{N}{k}$. Số các số $i$ thoả mãn điều này là $\lfloor \frac{N}{k} \rfloor - \lfloor \frac{N}{k+1} \rfloor$.

Tiếp theo, xét trường hợp khi $\lfloor \frac{N}{i} \rfloor \ge k_0 + 1$. Trong trường hợp này $\frac{N}{i} \ge k_0 + 1$, nên $i \le \frac{N}{k_0 + 1} < \sqrt{N}$, và có nhiều nhất $\sqrt{N}$ trường hợp cho $i$, nên ta có thể lấy kết quả lần lượt.

Như vậy, đáp án sẽ là

$$\sum_{k=1}^{k_0} ((\lfloor \frac{N}{k} \rfloor - \lfloor \frac{N}{k+1} \rfloor) \times k) + \sum_{i=1}^{\lfloor \frac{N}{k_0 + 1} \rfloor} \lfloor \frac{N}{i} \rfloor$$

và mỗi phần có thể được tính trong $O(\sqrt{N})$.

Code mẫu:

```cpp
#include <bits/stdc++.h>

using namespace std;

int main(void) {
    long long n, ans, k;
    cin >> n;

    for (long long i = 1; i <= n; i++) {
        if (i*i <= n) k = i;
        else break;
    }

    ans = 0;
    for (long long i = 1; i <= k; i++) ans += ((n / i) - (n / (i + 1))) * i;
    for (long long i = 1; i <= n / (k + 1); i++) ans += (n / i);

    cout << ans << endl;
    return 0;
}
```

## Một số identity và giới hạn

Mình sẽ list ra một số identity và giới hạn, việc chứng minh thì dành cho các bạn.

- **Floor và ceiling cho phân số**: Với số nguyên dương $b$ và một số nguyên bất kỳ $a$, ta có $\lceil \frac{a}{b} \rceil = \lfloor \frac{a+b-1}{b} \rfloor$.
- **Tính chất của Gauss**: Với các số nguyên dương $m$ và $n$, ta có $\sum_{i = 0}^{n - 1} \lfloor \frac{im}{n} \rfloor = \frac{(m-1)(n-1) + gcd(m, n) - 1}{2}$. Để chứng minh, hãy xem số điểm nằm dưới đường thẳng $y = \frac{mx}{n}$ nằm trong tam giác với các góc $(0, 0)$ và $(m, n)$.
- **Identity của Hermite**: Với số nguyên dương $n$ và số thực $x$, các quan hệ sau đúng: $\lfloor nx \rfloor = \sum_{i = 0}^{n - 1} \lfloor x + \frac{i}{n} \rfloor$ và $\lceil nx \rceil = \sum_{i = 0}^{n - 1} \lceil x - \frac{i}{n} \rceil$. Có thể chứng minh bằng các chia trường hợp phần phân số (tương ứng là khoảng cách đến ceiling) là giữa $\frac{i}{n}$ và $\frac{i+1}{n}$.
- **Giới hạn Harmonic**: $\sum_{i = 1}^n \lfloor \frac{x}{i} \rfloor \le x \sum_{i = 1}^n \frac{1}{i} = O(x \log n)$. Hệ quả là một sàng với tất cả các ước từ $1$ đến $n$ với tổng cộng $x$ số nguyên liên tiếp thì có độ phức tạp thời gian là $O(x \log n)$. Đây là lý do vì sao sàng Eratosthenes và biến thể đoạn của nó đủ nhanh. Điều này cũng cho thấy rằng tổng các ước của một số nguyên dương $n$ tối đa là $O(n \log n)$

## Liên quan đến ngôn ngữ lập trình

Bất kỳ khi nào bạn thực hiện phép chia số nguyên bằng bất cứ ngôn ngữ lập trình nào, hãy cố gắng chuyển đổi nó thành dạng có mẫu số dương. Tuy nhiên, với hầu hết ngôn ngữ, ta có `(a / b) * b + (a % b)` bằng `a` luôn đúng.

Thông thường có hai hành vi khi thực hiện phép chia số nguyên với số chia dương:

- Tính floor trong mọi trường hợp: ví dụ như Python. `a // b` sẽ cho ra $\lfloor \frac{a}{b} \rfloor$, và `a % b` sẽ cho ra số dư không âm khi $a$ bị chia bởi $b$.
- Làm tròn kết quả về $0$: ví dụ như C++. Lý do là để phòng ngừa tràn số khi nhân kết quả với mẫu số. Cho nên, với số dương $a$, cách làm sẽ tương tự Python, nhưng với số âm $a$, nó sẽ trả về $\lceil \frac{a}{b} \rceil$, và `a % b` sẽ cho ra khoảng cách âm đến bội tương ứng của $b$.

Để tính ceiling của $\frac{a}{b}$ với số nguyên dương $b$ và số nguyên $a$, ta có thể dùng kết quả trước đó: $\lceil \frac{a}{b} \rceil = \lfloor \frac{a+b-1}{b} \rfloor$. Việc cài đặt thì xin mời bạn đọc. 

Lưu ý rằng `std::floor` và `std::ceil` là các thao tác trên số có dấu chấm động, và kết quả cũng thuộc kiểu đó. Nên chúng có thể không chính xác khi chuyển thành số nguyên, vì vậy chúng không nên được sử dụng trong phần lớn trong thực tế.

# Luyện tập

Ở đây chỉ lưu code của những ví dụ ở trên

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [AtCoder ABC 165 - D](https://atcoder.jp/contests/abc165/tasks/abc165_d) | :white_check_mark: | [Submission](https://atcoder.jp/contests/abc165/submissions/12602056) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder165-ABC-D.cpp) | 02/05/2020 |
| [AtCoder ABC 230 - E](https://atcoder.jp/contests/abc230/tasks/abc230_e) | :white_check_mark: | [Submission](https://atcoder.jp/contests/abc230/submissions/27754365) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/AtCoder/AtCoder230-ABC-E.cpp) | 07/12/2021 |
