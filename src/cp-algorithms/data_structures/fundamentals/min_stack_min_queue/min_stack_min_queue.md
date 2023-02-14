# Minimum Stack / Minimum Queue

## Nguồn

<img src="../../../../../img/cpalgorithms.ico" width="16" height="16"/> [Minimum stack / Minimum queue](https://cp-algorithms.com/data_structures/stack_queue_modification.html)

## Lời tựa

Trong bài viết này chúng ta sẽ xem xét 3 bài toán: bài đầu tiên ta sẽ biến đổi một stack sao cho nó có thể tìm min của stack trong $O(1)$, sau đó ta làm điều tương tự với queue, cuối cùng ta sẽ dùng những cấu trúc dữ liệu đó để tìm min của tất cả các dãy con độ dài $M$ không đổi của mảng trong $O(n)$.

## Biến đổi stack

Ta muốn biến đổi cấu trúc dữ liệu stack mà nó có thể tìm min của stack trong thời gian $O(1)$ mà vẫn giữ các tính chất tương tự stack bình thường trong việc thêm và bớt đi phần tử. Một lưu ý nhỏ là trong stack ta chỉ thêm và bớt phần tử cuối cùng.

Để làm được việc này, ta sẽ không chỉ lưu các phần tử trong stack, mà sẽ lưu chúng theo cặp: phần tử đó và min của stack từ phần tử này trở về trước.

```cpp
stack<pair<int, int>> st;
```

Rõ ràng là tìm min của cả stack chỉ là giá trị ```stack.top().second```.

Cũng rất rõ ràng là việc thêm và bớt phần tử của stack có thể được thực hiện trong thời gian hằng số.

### Cài đặt

Thêm phần tử:

```cpp
int new_min = st.empty() ? new_elem : min(new_elem, st.top().second);
st.push({new_elem, new_min});
```

Xoá phần tử:

```cpp
int removed_element = st.top().first;
st.pop();
```

Tìm min:

```cpp
int minimum = st.top().second;
```

## Biến đổi queue (phương pháp 1)

Giờ ta muốn có kết quả tương tự như trên nhưng với một cái queue, nghĩa là ta muốn thêm phần tử vào phía sau và xoá phần tử ở phía trước.

Ở đây ta xét một cách đơn giản để biến đổi queue. Nó có một yếu điểm lớn, vì queue sau khi biến đổi sẽ không lưu tất cả các phần tử.

Mấu chốt là chỉ lưu các phần tử quyết định min trong queue mà thôi. Ta sẽ giữ lại các phần tử trong queue theo thử tự không giảm (min sẽ nằm ở đầu queue). Với cách này thì min sẽ luôn nằm ở đầu queue. Trước khi thêm phần tử vào queue, ta sẽ làm như sau: ta xoá tất cả các phần tử tính từ sau cùng về trước mà nó lớn hơn phần từ mới này, và thêm phần tử này vào queue. Với cách này ta sẽ không phá vỡ thứ tự của queue, và sẽ không làm mất đi phần tử hiện tại nếu nó là min ở bất kỳ bước nào. Tất cả các phần tử bị xoá không thể là min được. Khi ta muốn xem một phần tử ở đầu queue, nó có thể không có ở đó vì ta đã xoá nó khi thêm vào một phần tử nhỏ hơn rồi. Vì vậy khi xoá một phần tử trong queue, ta cần biết giá trị của phần tử đó. Nếu phần tử đầu queue có cùng giá trị, ta có thể xoá nó một cách an toàn, ngược lại ta không làm gì cả.

### Cài đặt

```cpp
deque<int> q;
```

Tìm min:
```cpp
int minimum = q.front();
```

Thêm phần tử:

```cpp
while (!q.empty() && q.back() > new_element)
    q.pop_back();
q.push_back(new_element);
```

Xoá phần tử:

```cpp
if (!q.empty() && q.front() == remove_element)
    q.pop_front();
```

Ta thấy rõ rằng trung bình thì các thao tác này tốn thời gian $O(1)$ vì mọi phần tử chỉ có thể được thêm và bớt đi đúng một lần.

## Biến đổi queue (phương pháp 2)

Đây là phương pháp 1 với một chút biến đổi. Ta muốn xoá phần tử mà không muốn biết phải xoá phần tử nào. Ta có thể làm được bằng cách lưu chỉ số của một phần tử của queue. Và ta cũng lưu số phần tử ta đã thêm và xoá đi.

### Cài đặt

```cpp
deque<pair<int, int>> q;
int cnt_added = 0;
int cnt_removed = 0;
```

Tìm min:

```cpp
int minimum = q.front().first;
```

Thêm phần tử:

```cpp
while (!q.empty() && q.back().first > new_element)
    q.pop_back();
q.push_back({new_element, cnt_added});
cnt_added++;
```

Xoá phần tử:

```cpp
if (!q.empty() && q.front().second == cnt_removed) 
    q.pop_front();
cnt_removed++;
```

## Biến đổi queue (phương pháp 3)

Ta xét một cách khác để biến đổi queue để tìm min trong $O(1)$. Cách này cài đặt khá phức tạp, nhưng ta lưu tất cả các phần tử. Và ta cũng có thể xoá một phần tử ở đầu mà không cần biết giá trị của nó.

Ý tưởng là quy bài toán về stack. Giờ ta chỉ cần biết cách mô phỏng một queue với 2 stack.

Ta tạo 2 stack, `s1` và `s2`. Tất nhiên 2 stack này sẽ ở dạng đã biến đổi, nến ta tìm min được trong $O(1)$. Ta sẽ thêm các phần tử mới vào trong `s1` và xoá phần tử khỏi `s2`. Nếu ở bất cứ thời điểm nào `s2` rỗng, ta di chuyển tất cả phần tử từ `s1` sang `s2` (lúc này thứ tự sẽ đảo ngược). Cuối cùng tìm min của queue sẽ là tìm min của 2 stack.

Vậy ta thực hiện tất cả các thao tác trong trung bình là $O(1)$ (mỗi phần tử sẽ được thêm vào stack `s1` một lần, chuyển vào `s2` một lần, xoá khỏi `s2` một lần).

### Cài đặt:

```cpp
stack<pair<int, int>> s1, s2;
```

Tìm min:

```cpp
if (s1.empty() || s2.empty()) 
    minimum = s1.empty() ? s2.top().second : s1.top().second;
else
    minimum = min(s1.top().second, s2.top().second);
```

Thêm phần tử:

```cpp
int minimum = s1.empty() ? new_element : min(new_element, s1.top().second);
s1.push({new_element, minimum});
```

Xoá phần tử:

```cpp
if (s2.empty()) {
    while (!s1.empty()) {
        int element = s1.top().first;
        s1.pop();
        int minimum = s2.empty() ? element : min(element, s2.top().second);
        s2.push({element, minimum});
    }
}
int remove_element = s2.top().first;
s2.pop();
```

## Tìm min của tất cả dãy con độ dài $M$ không đổi { data-toc-label='Tìm min của tất cả dãy con độ dài <script type="math/tex">M</script> không đổi' }

Cho một mảng $A$ độ dài $N$ và số $M \leq N$. Ta tìm min của mỗi dãy con độ dài $M$ trong mảng này, nghĩa là tìm:

$$ \min_{0 \le i \le M-1} A[i], \min_{1 \le i \le M} A[i], \min_{2 \le i \le M+1} A[i],~\dots~, \min_{N-M \le i \le N-1} A[i] $$

Ta cần giải bài này trong thời gian $O(N)$.

Ta có thể dùng một trong 3 cách biến đổi queue ở trên để giải. Ta thêm vào queue $M$ phần tử đầu của mảng, tìm và in ra min của chúng, sau đó thêm phần tử tiếp theo vào queue và xoá phần tử đầu của mảng ra, tìm và in min của số còn lại, vân vân. Vì tất cả các thao tác được thực hiện trong thời gian trung bình hằng số, độ phức tạp của thuật toán là $O(N)$.


## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [HackerRank - Queries with Fixed Length](https://www.hackerrank.com/challenges/queries-with-fixed-length/problem) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/HackerRank/HACKR%20queries-with-fixed-length.cpp) | 13/11/2022 |
| [Codechef - Binary Land](https://www.codechef.com/problems/BINLAND) | :white_check_mark: | [Submission](https://www.codechef.com/viewsolution/79928542) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codechef/CODECHEF%20BINLAND.cpp) | 14/11/2022 |
