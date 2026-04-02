# Hàm tiền tố - Thuật toán Knuth–Morris–Pratt

## Định nghĩa hàm tiền tố

Cho một xâu $s$ độ dài $n$. **Hàm tiền tố** của xâu này được định nghĩa là một mảng $\pi$ có độ dài $n$, trong đó $\pi[i]$ là độ dài của tiền tố thực sự dài nhất của xâu con $s[0 \dots i]$ mà đồng thời cũng là hậu tố của xâu con đó. Tiền tố thực sự của một xâu là tiền tố không bằng chính xâu đó. Theo định nghĩa, $\pi[0] = 0$.

Về mặt toán học, định nghĩa của hàm tiền tố có thể được viết như sau:

$\pi[i] = \max_ {k = 0 \dots i} \{k : s[0 \dots k-1] = s[i-(k-1) \dots i] \}$

Ví dụ, hàm tiền tố của xâu "abcabcd" là $[0, 0, 0, 1, 2, 3, 0]$, và hàm tiền tố của xâu "aabaaab" là $[0, 1, 0, 1, 2, 2, 3]$.

## Thuật toán đơn giản

Một thuật toán tuân theo chính xác định nghĩa của hàm tiền tố sẽ trông như sau:

```cpp
vector<int> prefix_function(string s) {
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 0; i < n; i++)
        for (int k = 0; k <= i; k++)
            if (s.substr(0, k) == s.substr(i-k+1, k))
                pi[i] = k;
    return pi;
}
```

Dễ thấy độ phức tạp của thuật toán này là $O(n^3)$, và còn có thể cải tiến được.

## Thuật toán hiệu quả

Thuật toán này được đề xuất bởi Knuth và Pratt, và được đề xuất độc lập bởi Morris vào năm 1977. Nó được sử dụng làm hàm chính trong thuật toán tìm kiếm xâu con.

### Tối ưu thứ nhất

Nhận xét quan trọng đầu tiên là giá trị của hàm tiền tố chỉ có thể tăng tối đa một đơn vị.

Thật vậy, nếu ngược lại, $\pi[i + 1] \gt \pi[i] + 1$, thì ta có thể lấy hậu tố kết thúc tại vị trí $i + 1$ có độ dài $\pi[i + 1]$ và bỏ ký tự cuối cùng đi. Ta thu được một hậu tố kết thúc tại vị trí $i$ có độ dài $\pi[i + 1] - 1$, tốt hơn $\pi[i]$, tức là có mâu thuẫn.

Hình minh họa sau đây cho thấy mâu thuẫn này.
Hậu tố thực sự dài nhất tại vị trí $i$ mà cũng là tiền tố có độ dài $2$, và tại vị trí $i+1$ nó có độ dài $4$. Do đó xâu $s_0 ~ s_1 ~ s_2 ~ s_3$ bằng xâu $s_{i-2} ~ s_{i-1} ~ s_i ~ s_{i+1}$, nghĩa là các xâu $s_0 ~ s_1 ~ s_2$ và $s_{i-2} ~ s_{i-1} ~ s_i$ cũng bằng nhau, vì vậy $\pi[i]$ phải bằng $3$.

$\underbrace{\overbrace{s_0 ~ s_1}^{\pi[i] = 2} ~ s_2 ~ s_3}_{\pi[i+1] = 4} ~ \dots ~ \underbrace{s_{i-2} ~ \overbrace{s_{i-1} ~ s_{i}}^{\pi[i] = 2} ~ s_{i+1}}_{\pi[i+1] = 4}$

Như vậy khi chuyển sang vị trí tiếp theo, giá trị của hàm tiền tố có thể tăng thêm một, giữ nguyên, hoặc giảm đi một lượng nào đó. Thực tế này đã cho phép ta giảm độ phức tạp của thuật toán xuống $O(n^2)$, vì trong mỗi bước hàm tiền tố chỉ có thể tăng tối đa một đơn vị. Tổng cộng hàm có thể tăng tối đa $n$ bước, và do đó cũng chỉ có thể giảm tổng cộng $n$ bước. Điều này có nghĩa là ta chỉ cần thực hiện $O(n)$ phép so sánh xâu, và đạt được độ phức tạp $O(n^2)$.

### Tối ưu thứ hai

Đi xa hơn xíu, ta muốn loại bỏ các phép so sánh xâu. Để làm được điều này, ta phải sử dụng tất cả thông tin đã tính được ở các bước trước.

Vậy hãy tính giá trị của hàm tiền tố $\pi$ cho $i + 1$. Nếu $s[i+1] = s[\pi[i]]$, thì ta có thể khẳng định chắc chắn rằng $\pi[i+1] = \pi[i] + 1$, vì ta đã biết rằng hậu tố tại vị trí $i$ có độ dài $\pi[i]$ bằng với tiền tố có độ dài $\pi[i]$. Điều này được minh họa lại bằng một ví dụ.

$\underbrace{\overbrace{s_0 ~ s_1 ~ s_2}^{\pi[i]} ~ \overbrace{s_3}^{s_3 = s_{i+1}}}_{\pi[i+1] = \pi[i] + 1} ~ \dots ~ \underbrace{\overbrace{s_{i-2} ~ s_{i-1} ~ s_{i}}^{\pi[i]} ~ \overbrace{s_{i+1}}^{s_3 = s_{i + 1}}}_{\pi[i+1] = \pi[i] + 1}$

Nếu không dính trường hợp đó, $s[i+1] \neq s[\pi[i]]$, ta cần thử một xâu ngắn hơn.
Để tăng tốc, ta muốn nhảy ngay đến độ dài $j \lt \pi[i]$ lớn nhất sao cho tính chất tiền tố tại vị trí $i$ vẫn thỏa mãn, tức là $s[0 \dots j-1] = s[i-j+1 \dots i]$:

$\overbrace{\underbrace{s_0 ~ s_1}_j ~ s_2 ~ s_3}^{\pi[i]} ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_j}^{\pi[i]} ~ s_{i+1}$

Thật vậy, nếu ta tìm được độ dài $j$ như vậy, thì ta lại chỉ cần so sánh các ký tự $s[i+1]$ và $s[j]$. Nếu chúng bằng nhau, thì ta gán $\pi[i+1] = j + 1$. Ngược lại, ta cần tìm giá trị lớn nhất nhỏ hơn $j$ mà tính chất tiền tố vẫn thỏa mãn, và cứ tiếp tục như vậy. Có thể xảy ra trường hợp quá trình này tiếp tục cho đến khi $j = 0$. Khi đó nếu $s[i+1] = s[0]$, ta gán $\pi[i+1] = 1$, ngược lại $\pi[i+1] = 0$.

Vậy ta đã có sơ đồ tổng quát của thuật toán. Câu hỏi duy nhất còn lại là làm thế nào để tìm hiệu quả các độ dài $j$. Tóm tắt lại xem nào: với độ dài hiện tại $j$ tại vị trí $i$ mà tính chất tiền tố thỏa mãn, tức là $s[0 \dots j-1] = s[i-j+1 \dots i]$, ta muốn tìm $k \lt j$ lớn nhất mà tính chất tiền tố vẫn thỏa mãn.

$\overbrace{\underbrace{s_0 ~ s_1}_k ~ s_2 ~ s_3}^j ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_k}^j ~s_{i+1}$

Hình minh họa cho thấy giá trị này chính là $\pi[j-1]$, mà ta đã tính trước đó.

### Thuật toán sau cùng

Vậy cuối cùng ta có thể xây dựng một thuật toán không thực hiện bất kỳ phép so sánh xâu nào và chỉ thực hiện $O(n)$ thao tác.

Phương án như sau:

- Ta tính các giá trị tiền tố $\pi[i]$ trong một vòng lặp từ $i = 1$ đến $i = n-1$ ($\pi[0]$ được gán bằng $0$).
- Để tính giá trị hiện tại $\pi[i]$, ta đặt biến $j$ biểu thị độ dài của hậu tố tốt nhất cho $i-1$. Ban đầu $j = \pi[i-1]$.
- Kiểm tra xem hậu tố có độ dài $j+1$ có phải là tiền tố không bằng cách so sánh $s[j]$ và $s[i]$. Nếu chúng bằng nhau thì ta gán $\pi[i] = j + 1$, ngược lại ta giảm $j$ xuống $\pi[j-1]$ và lặp lại bước này.
- Nếu ta đã đạt đến độ dài $j = 0$ mà vẫn không khớp, thì ta gán $\pi[i] = 0$ và chuyển sang chỉ số $i + 1$ tiếp theo.

### Cài đặt

Cài đặt thuật toán KMP siêu ngắn và rõ ràng.

```cpp
vector<int> prefix_function(string s) {
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i-1];
        while (j > 0 && s[i] != s[j])
            j = pi[j-1];
        if (s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}
```

Đây là một thuật toán **trực tuyến** (online), tức là nó xử lý dữ liệu ngay khi nhận được - ví dụ, bạn có thể đọc từng ký tự của xâu và xử lý ngay lập tức, tìm giá trị hàm tiền tố cho mỗi ký tự tiếp theo. Thuật toán vẫn cần lưu trữ chính xâu đó và các giá trị hàm tiền tố đã tính trước đó, nhưng nếu ta biết trước giá trị lớn nhất $M$ mà hàm tiền tố có thể đạt được trên xâu, ta chỉ cần lưu $M+1$ ký tự đầu tiên của xâu và cùng số lượng giá trị của hàm tiền tố.

## Ứng dụng

### Tìm kiếm xâu con trong một xâu - Thuật toán Knuth-Morris-Pratt

Bài toán này là ứng dụng kinh điển của hàm tiền tố.

Cho một văn bản $t$ và một xâu $s$, ta muốn tìm và hiển thị vị trí của tất cả các lần xuất hiện của xâu $s$ trong văn bản $t$.

Để thuận tiện, ta ký hiệu $n$ là độ dài của xâu $s$ và $m$ là độ dài của văn bản $t$.

We generate the string $s + \# + t$, where $\#$ is a separator that appears neither in $s$ nor in $t$.
Let us calculate the prefix function for this string.
Now think about the meaning of the values of the prefix function, except for the first $n + 1$ entries (which belong to the string $s$ and the separator).
By definition the value $\pi[i]$ shows the longest length of a substring ending in position $i$ that coincides with the prefix.
But in our case this is nothing more than the largest block that coincides with $s$ and ends at position $i$.
This length cannot be bigger than $n$ due to the separator.
But if equality $\pi[i] = n$ is achieved, then it means that the string $s$ appears completely in at this position, i.e. it ends at position $i$.
Just do not forget that the positions are indexed in the string $s + \# + t$.

Ta tạo xâu $s + \# + t$, trong đó $\#$ là ký tự phân cách không xuất hiện trong cả $s$ lẫn $t$.
Hãy tính hàm tiền tố cho xâu này.
Bây giờ hãy nghĩ về ý nghĩa của các giá trị hàm tiền tố, ngoại trừ $n + 1$ phần tử đầu tiên (thuộc về xâu $s$ và ký tự phân cách).
Theo định nghĩa, giá trị $\pi[i]$ cho biết độ dài lớn nhất của xâu con kết thúc tại vị trí $i$ mà trùng với tiền tố.
Nhưng trong trường hợp của ta, đây chính là khối lớn nhất trùng với $s$ và kết thúc tại vị trí $i$.
Độ dài này không thể lớn hơn $n$ nhờ ký tự phân cách.
Nhưng nếu đẳng thức $\pi[i] = n$ đạt được, thì điều đó có nghĩa là xâu $s$ xuất hiện hoàn toàn tại vị trí này, tức là nó kết thúc tại vị trí $i$.
Chỉ cần đừng quên rằng các vị trí được đánh chỉ số trong xâu $s + \# + t$.

Thus if at some position $i$ we have $\pi[i] = n$, then at the position $i - (n + 1) - n + 1 = i - 2n$ in the string $t$ the string $s$ appears.

Vì vậy nếu tại vị trí $i$ nào đó ta có $\pi[i] = n$, thì tại vị trí $i - (n + 1) - n + 1 = i - 2n$ trong xâu $t$, xâu $s$ xuất hiện.

As already mentioned in the description of the prefix function computation, if we know that the prefix values never exceed a certain value, then we do not need to store the entire string and the entire function, but only its beginning.
In our case this means that we only need to store the string $s + \#$ and the values of the prefix function for it.
We can read one character at a time of the string $t$ and calculate the current value of the prefix function.

Như đã đề cập trong phần mô tả tính toán hàm tiền tố, nếu ta biết rằng các giá trị tiền tố không bao giờ vượt quá một giá trị nhất định, thì ta không cần lưu trữ toàn bộ xâu và toàn bộ hàm, mà chỉ cần phần đầu của nó.
Trong trường hợp của ta, điều này có nghĩa là ta chỉ cần lưu xâu $s + \#$ và các giá trị hàm tiền tố tương ứng.
Ta có thể đọc từng ký tự một của xâu $t$ và tính giá trị hiện tại của hàm tiền tố.

Thus the Knuth-Morris-Pratt algorithm solves the problem in $O(n + m)$ time and $O(n)$ memory.

Như vậy thuật toán Knuth-Morris-Pratt giải bài toán trong thời gian $O(n + m)$ và bộ nhớ $O(n)$.

### Counting the number of occurrences of each prefix

### Đếm số lần xuất hiện của mỗi tiền tố

Here we discuss two problems at once.
Given a string $s$ of length $n$.
In the first variation of the problem we want to count the number of appearances of each prefix $s[0 \dots i]$ in the same string.
In the second variation of the problem another string $t$ is given and we want to count the number of appearances of each prefix $s[0 \dots i]$ in $t$.

Ở đây ta thảo luận hai bài toán cùng lúc.
Cho một xâu $s$ có độ dài $n$.
Trong biến thể thứ nhất, ta muốn đếm số lần xuất hiện của mỗi tiền tố $s[0 \dots i]$ trong chính xâu đó.
Trong biến thể thứ hai, cho thêm một xâu $t$ và ta muốn đếm số lần xuất hiện của mỗi tiền tố $s[0 \dots i]$ trong $t$.

First we solve the first problem.
Consider the value of the prefix function $\pi[i]$ at a position $i$.
By definition it means that the prefix of length $\pi[i]$ of the string $s$ occurs and ends at position $i$, and there is no longer prefix that follows this definition.
At the same time shorter prefixes can end at this position.
It is not difficult to see, that we have the same question that we already answered when we computed the prefix function itself:
Given a prefix of length $j$ that is a suffix ending at position $i$, what is the next smaller prefix $\lt j$ that is also a suffix ending at position $i$.
Thus at the position $i$ ends the prefix of length $\pi[i]$, the prefix of length $\pi[\pi[i] - 1]$, the prefix $\pi[\pi[\pi[i] - 1] - 1]$, and so on, until the index becomes zero.
Thus we can compute the answer in the following way.

Đầu tiên ta giải bài toán thứ nhất.
Xét giá trị hàm tiền tố $\pi[i]$ tại vị trí $i$.
Theo định nghĩa, điều này có nghĩa là tiền tố có độ dài $\pi[i]$ của xâu $s$ xuất hiện và kết thúc tại vị trí $i$, và không có tiền tố nào dài hơn thỏa mãn định nghĩa này.
Đồng thời các tiền tố ngắn hơn cũng có thể kết thúc tại vị trí này.
Không khó để thấy rằng ta có cùng câu hỏi mà ta đã trả lời khi tính hàm tiền tố:
Cho một tiền tố có độ dài $j$ là hậu tố kết thúc tại vị trí $i$, tiền tố nhỏ hơn tiếp theo $\lt j$ mà cũng là hậu tố kết thúc tại vị trí $i$ là gì.
Vì vậy tại vị trí $i$ kết thúc tiền tố có độ dài $\pi[i]$, tiền tố có độ dài $\pi[\pi[i] - 1]$, tiền tố $\pi[\pi[\pi[i] - 1] - 1]$, và cứ tiếp tục cho đến khi chỉ số bằng không.
Do đó ta có thể tính đáp án theo cách sau.

```{.cpp file=prefix_count_each_prefix}
vector<int> ans(n + 1);
for (int i = 0; i < n; i++)
    ans[pi[i]]++;
for (int i = n-1; i > 0; i--)
    ans[pi[i-1]] += ans[i];
for (int i = 0; i <= n; i++)
    ans[i]++;
```

Here for each value of the prefix function we first count how many times it occurs in the array $\pi$, and then compute the final answers:
if we know that the length prefix $i$ appears exactly $\text{ans}[i]$ times, then this number must be added to the number of occurrences of its longest suffix that is also a prefix.
At the end we need to add $1$ to each result, since we also need to count the original prefixes also.

Ở đây, với mỗi giá trị của hàm tiền tố, ta đầu tiên đếm số lần nó xuất hiện trong mảng $\pi$, sau đó tính đáp án cuối cùng:
nếu ta biết rằng tiền tố có độ dài $i$ xuất hiện đúng $\text{ans}[i]$ lần, thì số này phải được cộng vào số lần xuất hiện của hậu tố dài nhất của nó mà cũng là tiền tố.
Cuối cùng ta cần cộng thêm $1$ vào mỗi kết quả, vì ta cũng cần đếm chính các tiền tố gốc.

Now let us consider the second problem.
We apply the trick from Knuth-Morris-Pratt:
we create the string $s + \# + t$ and compute its prefix function.
The only differences to the first task is, that we are only interested in the prefix values that relate to the string $t$, i.e. $\pi[i]$ for $i \ge n + 1$.
With those values we can perform the exact same computations as in the first task.

Bây giờ hãy xét bài toán thứ hai.
Ta áp dụng kỹ thuật từ Knuth-Morris-Pratt:
ta tạo xâu $s + \# + t$ và tính hàm tiền tố của nó.
Điểm khác biệt duy nhất so với bài toán thứ nhất là ta chỉ quan tâm đến các giá trị tiền tố liên quan đến xâu $t$, tức là $\pi[i]$ với $i \ge n + 1$.
Với các giá trị đó, ta có thể thực hiện các phép tính hoàn toàn giống như trong bài toán thứ nhất.

### The number of different substring in a string

### Số lượng xâu con khác nhau trong một xâu

Given a string $s$ of length $n$.
We want to compute the number of different substrings appearing in it.

Cho một xâu $s$ có độ dài $n$.
Ta muốn tính số lượng xâu con khác nhau xuất hiện trong nó.

We will solve this problem iteratively.
Namely we will learn, knowing the current number of different substrings, how to recompute this count by adding a character to the end.

Ta sẽ giải bài toán này một cách lặp.
Cụ thể, ta sẽ tìm cách, khi biết số lượng xâu con khác nhau hiện tại, tính lại số lượng này khi thêm một ký tự vào cuối.

So let $k$ be the current number of different substrings in $s$, and we add the character $c$ to the end of $s$.
Obviously some new substrings ending in $c$ will appear.
We want to count these new substrings that didn't appear before.

Gọi $k$ là số lượng xâu con khác nhau hiện tại trong $s$, và ta thêm ký tự $c$ vào cuối $s$.
Rõ ràng một số xâu con mới kết thúc bằng $c$ sẽ xuất hiện.
Ta muốn đếm các xâu con mới này mà chưa xuất hiện trước đó.

We take the string $t = s + c$ and reverse it.
Now the task is transformed into computing how many prefixes there are that don't appear anywhere else.
If we compute the maximal value of the prefix function $\pi_{\text{max}}$ of the reversed string $t$, then the longest prefix that appears in $s$ is $\pi_{\text{max}}$ long.
Clearly also all prefixes of smaller length appear in it.

Ta lấy xâu $t = s + c$ và đảo ngược nó.
Bây giờ bài toán được chuyển thành tính xem có bao nhiêu tiền tố không xuất hiện ở bất kỳ đâu khác.
Nếu ta tính giá trị lớn nhất của hàm tiền tố $\pi_{\text{max}}$ của xâu đảo ngược $t$, thì tiền tố dài nhất xuất hiện trong $s$ có độ dài $\pi_{\text{max}}$.
Rõ ràng tất cả các tiền tố có độ dài nhỏ hơn cũng xuất hiện trong đó.

Therefore the number of new substrings appearing when we add a new character $c$ is $|s| + 1 - \pi_{\text{max}}$.

Do đó số lượng xâu con mới xuất hiện khi ta thêm ký tự $c$ là $|s| + 1 - \pi_{\text{max}}$.

So for each character appended we can compute the number of new substrings in $O(n)$ times, which gives a time complexity of $O(n^2)$ in total.

Vì vậy với mỗi ký tự được thêm vào, ta có thể tính số lượng xâu con mới trong thời gian $O(n)$, cho tổng độ phức tạp thời gian là $O(n^2)$.

It is worth noting, that we can also compute the number of different substrings by appending the characters at the beginning, or by deleting characters from the beginning or the end.

Đáng chú ý rằng ta cũng có thể tính số lượng xâu con khác nhau bằng cách thêm ký tự vào đầu, hoặc xóa ký tự từ đầu hoặc cuối.

### Compressing a string

### Nén xâu

Given a string $s$ of length $n$.
We want to find the shortest "compressed" representation of the string, i.e. we want to find a string $t$ of smallest length such that $s$ can be represented as a concatenation of one or more copies of $t$.

Cho một xâu $s$ có độ dài $n$.
Ta muốn tìm biểu diễn "nén" ngắn nhất của xâu, tức là ta muốn tìm xâu $t$ có độ dài nhỏ nhất sao cho $s$ có thể được biểu diễn dưới dạng nối một hoặc nhiều bản sao của $t$.

It is clear, that we only need to find the length of $t$. Knowing the length, the answer to the problem will be the prefix of $s$ with this length.

Rõ ràng ta chỉ cần tìm độ dài của $t$. Biết được độ dài, đáp án của bài toán sẽ là tiền tố của $s$ với độ dài đó.

Let us compute the prefix function for $s$.
Using the last value of it we define the value $k = n - \pi[n - 1]$.
We will show, that if $k$ divides $n$, then $k$ will be the answer, otherwise there is no effective compression and the answer is $n$.

Hãy tính hàm tiền tố cho $s$.
Sử dụng giá trị cuối cùng, ta định nghĩa $k = n - \pi[n - 1]$.
Ta sẽ chứng minh rằng nếu $k$ chia hết $n$, thì $k$ là đáp án, ngược lại không có cách nén hiệu quả và đáp án là $n$.

Let $n$ be divisible by $k$.
Then the string can be partitioned into blocks of the length $k$.
By definition of the prefix function, the prefix of length $n - k$ will be equal with its suffix.
But this means that the last block is equal to the block before.
And the block before has to be equal to the block before it.
And so on.
As a result, it turns out that all blocks are equal, therefore we can compress the string $s$ to length $k$.

Giả sử $n$ chia hết cho $k$.
Khi đó xâu có thể được chia thành các khối có độ dài $k$.
Theo định nghĩa của hàm tiền tố, tiền tố có độ dài $n - k$ sẽ bằng với hậu tố của nó.
Nhưng điều này có nghĩa là khối cuối cùng bằng khối trước nó.
Và khối trước đó phải bằng khối trước nó nữa.
Và cứ tiếp tục như vậy.
Kết quả là tất cả các khối đều bằng nhau, do đó ta có thể nén xâu $s$ xuống độ dài $k$.

Of course we still need to show that this is actually the optimum.
Indeed, if there was a smaller compression than $k$, than the prefix function at the end would be greater than $n - k$.
Therefore $k$ is really the answer.

Tất nhiên ta vẫn cần chứng minh rằng đây thực sự là tối ưu.
Thật vậy, nếu có cách nén nhỏ hơn $k$, thì giá trị hàm tiền tố ở cuối sẽ lớn hơn $n - k$.
Do đó $k$ thực sự là đáp án.

Now let us assume that $n$ is not divisible by $k$.
We show that this implies that the length of the answer is $n$.
We prove it by contradiction.
Assuming there exists an answer, and the compression has length $p$ ($p$ divides $n$).
Then the last value of the prefix function has to be greater than $n - p$, i.e. the suffix will partially cover the first block.
Now consider the second block of the string.
Since the prefix is equal with the suffix, and both the prefix and the suffix cover this block and their displacement relative to each other $k$ does not divide the block length $p$ (otherwise $k$ divides $n$), then all the characters of the block have to be identical.
But then the string consists of only one character repeated over and over, hence we can compress it to a string of size $1$, which gives $k = 1$, and $k$ divides $n$.
Contradiction.

Bây giờ giả sử $n$ không chia hết cho $k$.
Ta chứng minh rằng điều này dẫn đến đáp án có độ dài $n$.
Ta chứng minh bằng phản chứng.
Giả sử tồn tại một đáp án, và cách nén có độ dài $p$ ($p$ chia hết $n$).
Khi đó giá trị cuối cùng của hàm tiền tố phải lớn hơn $n - p$, tức là hậu tố sẽ phủ một phần khối đầu tiên.
Bây giờ xét khối thứ hai của xâu.
Vì tiền tố bằng hậu tố, và cả tiền tố lẫn hậu tố đều phủ khối này, và độ lệch giữa chúng $k$ không chia hết độ dài khối $p$ (nếu không thì $k$ chia hết $n$), nên tất cả các ký tự trong khối phải giống nhau.
Nhưng khi đó xâu chỉ gồm một ký tự lặp đi lặp lại, do đó ta có thể nén nó thành xâu có kích thước $1$, cho $k = 1$, và $k$ chia hết $n$.
Mâu thuẫn.

$\overbrace{s_0 ~ s_1 ~ s_2 ~ s_3}^p ~ \overbrace{s_4 ~ s_5 ~ s_6 ~ s_7}^p$

$s_0 ~ s_1 ~ s_2 ~ \underbrace{\overbrace{s_3 ~ s_4 ~ s_5 ~ s_6}^p ~ s_7}_{\pi[7] = 5}$

$s_4 = s_3, ~ s_5 = s_4, ~ s_6 = s_5, ~ s_7 = s_6 ~ \Rightarrow ~ s_0 = s_1 = s_2 = s_3$

### Building an automaton according to the prefix function

### Xây dựng automat theo hàm tiền tố

Let's return to the concatenation to the two strings through a separator, i.e. for the strings $s$ and $t$ we compute the prefix function for the string $s + \# + t$.
Obviously, since $\#$ is a separator, the value of the prefix function will never exceed $|s|$.
It follows, that it is sufficient to only store the string $s + \#$ and the values of the prefix function for it, and we can compute the prefix function for all subsequent character on the fly:

Hãy quay lại việc nối hai xâu qua ký tự phân cách, tức là với các xâu $s$ và $t$ ta tính hàm tiền tố cho xâu $s + \# + t$.
Rõ ràng, vì $\#$ là ký tự phân cách, giá trị hàm tiền tố sẽ không bao giờ vượt quá $|s|$.
Từ đó suy ra rằng chỉ cần lưu xâu $s + \#$ và các giá trị hàm tiền tố tương ứng, và ta có thể tính hàm tiền tố cho tất cả các ký tự tiếp theo một cách trực tiếp:

$\underbrace{s_0 ~ s_1 ~ \dots ~ s_{n-1} ~ \#}_{\text{need to store}} ~ \underbrace{t_0 ~ t_1 ~ \dots ~ t_{m-1}}_{\text{do not need to store}}$

Indeed, in such a situation, knowing the next character $c \in t$ and the value of the prefix function of the previous position is enough information to compute the next value of the prefix function, without using any previous characters of the string $t$ and the value of the prefix function in them.

Thật vậy, trong tình huống như vậy, biết ký tự tiếp theo $c \in t$ và giá trị hàm tiền tố của vị trí trước đó là đủ thông tin để tính giá trị tiếp theo của hàm tiền tố, mà không cần sử dụng bất kỳ ký tự nào trước đó của xâu $t$ và giá trị hàm tiền tố tại chúng.

In other words, we can construct an **automaton** (a finite state machine): the state in it is the current value of the prefix function, and the transition from one state to another will be performed via the next character.

Nói cách khác, ta có thể xây dựng một **automat** (máy trạng thái hữu hạn): trạng thái trong đó là giá trị hiện tại của hàm tiền tố, và bước chuyển từ trạng thái này sang trạng thái khác được thực hiện thông qua ký tự tiếp theo.

Thus, even without having the string $t$, we can construct such a transition table $(\text{old}_\pi, c) \rightarrow \text{new}_\pi$ using the same algorithm as for calculating the transition table:

Vì vậy, ngay cả khi không có xâu $t$, ta vẫn có thể xây dựng bảng chuyển trạng thái $(\text{old}_\pi, c) \rightarrow \text{new}_\pi$ bằng cùng thuật toán dùng để tính bảng chuyển:

```{.cpp file=prefix_automaton_slow}
void compute_automaton(string s, vector<vector<int>>& aut) {
    s += '#';
    int n = s.size();
    vector<int> pi = prefix_function(s);
    aut.assign(n, vector<int>(26));
    for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
            int j = i;
            while (j > 0 && 'a' + c != s[j])
                j = pi[j-1];
            if ('a' + c == s[j])
                j++;
            aut[i][c] = j;
        }
    }
}
```

However in this form the algorithm runs in $O(n^2 26)$ time for the lowercase letters of the alphabet.
Note that we can apply dynamic programming and use the already calculated parts of the table.
Whenever we go from the value $j$ to the value $\pi[j-1]$, we actually mean that the transition $(j, c)$ leads to the same state as the transition as $(\pi[j-1], c)$, and this answer is already accurately computed.

Tuy nhiên ở dạng này, thuật toán chạy trong thời gian $O(n^2 26)$ cho các chữ cái thường trong bảng chữ cái.
Lưu ý rằng ta có thể áp dụng quy hoạch động và sử dụng các phần đã tính của bảng.
Mỗi khi ta đi từ giá trị $j$ đến giá trị $\pi[j-1]$, thực chất ta muốn nói rằng bước chuyển $(j, c)$ dẫn đến cùng trạng thái với bước chuyển $(\pi[j-1], c)$, và đáp án này đã được tính chính xác rồi.

```{.cpp file=prefix_automaton_fast}
void compute_automaton(string s, vector<vector<int>>& aut) {
    s += '#';
    int n = s.size();
    vector<int> pi = prefix_function(s);
    aut.assign(n, vector<int>(26));
    for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
            if (i > 0 && 'a' + c != s[i])
                aut[i][c] = aut[pi[i-1]][c];
            else
                aut[i][c] = i + ('a' + c == s[i]);
        }
    }
}
```

As a result we construct the automaton in $O(26 n)$ time.

Kết quả là ta xây dựng automat trong thời gian $O(26 n)$.

When is such a automaton useful?
To begin with, remember that we use the prefix function for the string $s + \# + t$ and its values mostly for a single purpose: find all occurrences of the string $s$ in the string $t$.

Khi nào automat như vậy hữu ích?
Trước hết, hãy nhớ rằng ta sử dụng hàm tiền tố cho xâu $s + \# + t$ và các giá trị của nó chủ yếu cho một mục đích duy nhất: tìm tất cả các lần xuất hiện của xâu $s$ trong xâu $t$.

Therefore the most obvious benefit of this automaton is the **acceleration of calculating the prefix function** for the string $s + \# + t$.
By building the automaton for $s + \#$, we no longer need to store the string $s$ or the values of the prefix function in it.
All transitions are already computed in the table.

Do đó lợi ích rõ ràng nhất của automat này là **tăng tốc việc tính hàm tiền tố** cho xâu $s + \# + t$.
Bằng cách xây dựng automat cho $s + \#$, ta không cần lưu trữ xâu $s$ hay các giá trị hàm tiền tố trong đó nữa.
Tất cả các bước chuyển đã được tính sẵn trong bảng.

But there is a second, less obvious, application.
We can use the automaton when the string $t$ is a **gigantic string constructed using some rules**.
This can for instance be the Gray strings, or a string formed by a recursive combination of several short strings from the input.

Nhưng có một ứng dụng thứ hai, ít rõ ràng hơn.
Ta có thể sử dụng automat khi xâu $t$ là một **xâu khổng lồ được xây dựng theo một số quy tắc**.
Đây có thể là các xâu Gray, hoặc một xâu được tạo bằng cách kết hợp đệ quy nhiều xâu ngắn từ đầu vào.

For completeness we will solve such a problem:
given a number $k \le 10^5$ and a string $s$ of length $\le 10^5$.
We have to compute the number of occurrences of $s$ in the $k$-th Gray string.
Recall that Gray's strings are define in the following way:

Để hoàn chỉnh, ta sẽ giải một bài toán như vậy:
cho một số $k \le 10^5$ và một xâu $s$ có độ dài $\le 10^5$.
Ta phải tính số lần xuất hiện của $s$ trong xâu Gray thứ $k$.
Nhắc lại rằng các xâu Gray được định nghĩa như sau:

$\begin{align}
g_1 &= \text{"a"}\\
g_2 &= \text{"aba"}\\
g_3 &= \text{"abacaba"}\\
g_4 &= \text{"abacabadabacaba"}
\end{align}$

In such cases even constructing the string $t$ will be impossible, because of its astronomical length.
The $k$-th Gray string is $2^k-1$ characters long.
However we can calculate the value of the prefix function at the end of the string effectively, by only knowing the value of the prefix function at the start.

Trong những trường hợp như vậy, ngay cả việc xây dựng xâu $t$ cũng là không thể, vì độ dài khổng lồ của nó.
Xâu Gray thứ $k$ có độ dài $2^k-1$ ký tự.
Tuy nhiên ta có thể tính giá trị hàm tiền tố ở cuối xâu một cách hiệu quả, chỉ cần biết giá trị hàm tiền tố ở đầu.

In addition to the automaton itself, we also compute values $G[i][j]$ - the value of the automaton after processing the string $g_i$ starting with the state $j$.
And additionally we compute values $K[i][j]$ - the number of occurrences of $s$ in $g_i$, before during the processing of $g_i$ starting with the state $j$.
Actually $K[i][j]$ is the number of times that the prefix function took the value $|s|$ while performing the operations.
The answer to the problem will then be $K[k][0]$.

Ngoài automat, ta còn tính các giá trị $G[i][j]$ - giá trị của automat sau khi xử lý xâu $g_i$ bắt đầu từ trạng thái $j$.
Và thêm vào đó ta tính các giá trị $K[i][j]$ - số lần xuất hiện của $s$ trong $g_i$, trong quá trình xử lý $g_i$ bắt đầu từ trạng thái $j$.
Thực chất $K[i][j]$ là số lần hàm tiền tố nhận giá trị $|s|$ trong quá trình thực hiện các thao tác.
Đáp án của bài toán sẽ là $K[k][0]$.

How can we compute these values?
First the basic values are $G[0][j] = j$ and $K[0][j] = 0$.
And all subsequent values can be calculated from the previous values and using the automaton.
To calculate the value for some $i$ we remember that the string $g_i$ consists of $g_{i-1}$, the $i$ character of the alphabet, and $g_{i-1}$.
Thus the automaton will go into the state:

Làm thế nào để tính các giá trị này?
Đầu tiên các giá trị cơ sở là $G[0][j] = j$ và $K[0][j] = 0$.
Và tất cả các giá trị tiếp theo có thể được tính từ các giá trị trước đó và sử dụng automat.
Để tính giá trị cho $i$ nào đó, ta nhớ rằng xâu $g_i$ gồm $g_{i-1}$, ký tự thứ $i$ trong bảng chữ cái, và $g_{i-1}$.
Vì vậy automat sẽ đi vào trạng thái:

$\text{mid} = \text{aut}[G[i-1][j]][i]$

$G[i][j] = G[i-1][\text{mid}]$

The values for $K[i][j]$ can also be easily counted.

Các giá trị $K[i][j]$ cũng có thể được tính dễ dàng.

$K[i][j] = K[i-1][j] + (\text{mid} == |s|) + K[i-1][\text{mid}]$

So we can solve the problem for Gray strings, and similarly also a huge number of other similar problems.
For example the exact same method also solves the following problem:
we are given a string $s$ and some patterns $t_i$, each of which is specified as follows:
it is a string of ordinary characters, and there might be some recursive insertions of the previous strings of the form $t_k^{\text{cnt}}$, which means that at this place we have to insert the string $t_k$ $\text{cnt}$ times.
An example of such patterns:

Vậy ta có thể giải bài toán cho xâu Gray, và tương tự cho rất nhiều bài toán tương tự khác.
Ví dụ, cùng phương pháp này cũng giải được bài toán sau:
cho một xâu $s$ và một số mẫu $t_i$, mỗi mẫu được xác định như sau:
nó là một xâu gồm các ký tự thông thường, và có thể có một số phép chèn đệ quy các xâu trước đó dưới dạng $t_k^{\text{cnt}}$, nghĩa là tại vị trí đó ta phải chèn xâu $t_k$ $\text{cnt}$ lần.
Một ví dụ về các mẫu như vậy:

$\begin{align}
t_1 &= \text{"abdeca"}\\
t_2 &= \text{"abc"} + t_1^{30} + \text{"abd"}\\
t_3 &= t_2^{50} + t_1^{100}\\
t_4 &= t_2^{10} + t_3^{100}
\end{align}$

The recursive substitutions blow the string up, so that their lengths can reach the order of $100^{100}$.

Các phép thay thế đệ quy làm xâu phình to lên, sao cho độ dài của chúng có thể đạt cỡ $100^{100}$.

We have to find the number of times the string $s$ appears in each of the strings.

Ta phải tìm số lần xâu $s$ xuất hiện trong mỗi xâu.

The problem can be solved in the same way by constructing the automaton of the prefix function, and then we calculate the transitions in for each pattern by using the previous results.

Bài toán có thể được giải theo cùng cách bằng cách xây dựng automat của hàm tiền tố, sau đó ta tính các bước chuyển cho mỗi mẫu bằng cách sử dụng các kết quả trước đó.

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [UVA 455 - Periodic Strings](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396) | | | | |
| [UVA 11022 - String Factoring](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963) | | | | |
| [UVA 11452 - Dancing the Cheeky-Cheeky](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2447) | | | | |
| [UVA 12604 - Caesar Cipher](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4282) | | | | |
| [UVA 12467 - Secret Word](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3911) | | | | |
| [UVA 11019 - Matrix Matcher](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1960) | | | | |
| [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/) | | | | |
| [SPOJ - A Needle in the Haystack](https://www.spoj.com/problems/NHAY/) | | | | |
| [Codeforces - Anthem of Berland](http://codeforces.com/contest/808/problem/G) | | | | |
| [Codeforces - MUH and Cube Walls](http://codeforces.com/problemset/problem/471/D) | | | | |
| [Codeforces - Prefixes and Suffixes](https://codeforces.com/contest/432/problem/D) | | | | |
