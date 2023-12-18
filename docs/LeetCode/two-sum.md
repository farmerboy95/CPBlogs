# Lớp bài tập Two-Sum

## Nguồn

Bài viết này được dựa trên editorial các bài tập có dạng Two-Sum trên LeetCode, nghĩa là các bài toán có dạng: Cho một mảng các số nguyên và một số nguyên `target`, hãy tìm $X$ số trong mảng có tổng theo một tiêu chí nào đó so với `target`.

Code của các bài toán này có thể xem tại phần Luyện tập ở dưới cùng.

## LeetCode 1 - Two Sum

Cho một mảng các số nguyên `nums` có $N$ phần tử và một số nguyên `target`, hãy trả về chỉ số của hai số trong mảng có tổng bằng `target`. Bạn có thể giả sử rằng mỗi input chỉ có một lời giải duy nhất và bạn không thể dùng cùng một phần tử hai lần. Bạn có thể trả về kết quả theo bất kì thứ tự nào.

Giới hạn: $2 \le N \le 10^4$, $-10^9 \le nums_i \le 10^9$, $-10^9 \le target \le 10^9$

Chi tiết đề bài có thể xem tại [đây](https://leetcode.com/problems/two-sum/).

??? tip "Lời giải"
    Ngoài cách duyệt trâu $O(N^2)$ ra, ta có thể để ý rằng khi xét một số $x$ (ở vị trí $i$) trong mảng, ta chỉ cần tìm xem có tồn tại một số $y$ trong mảng sao cho $x + y = target$ hay $y = target - x$. Ta có thể duy trì một hash table chứa các số nằm trước vị trí $i$ để tìm kiếm $y$ trong $O(1)$, nên nhớ là trung bình $O(1)$. Như vậy, với cách này độ phức tạp thời gian là $O(N)$, độ phức tạp bộ nhớ là $O(N)$.

    Ngoài ra ta còn có thể sắp xếp mảng trước, sau đó đặt 2 con trỏ ở đầu và cuối mảng, nếu tổng giá trị của hai con trỏ nhỏ hơn `target` thì ta tăng con trỏ ở đầu, ngược lại ta giảm con trỏ ở cuối. Độ phức tạp thời gian là $O(N \log N)$, độ phức tạp bộ nhớ là $O(1)$.

## LeetCode 15 - 3Sum

Cho một mảng các số nguyên `nums` có $N$ phần tử, hãy trả về tất cả các bộ ba số không trùng nhau trong mảng có tổng bằng 0. Kết quả không được chứa các bộ ba số trùng nhau về mặt giá trị.

Giới hạn: $3 \le N \le 3000$, $-10^5 \le nums_i \le 10^5$

Chi tiết đề bài có thể xem tại [đây](https://leetcode.com/problems/3sum/).

??? tip "Lời giải"
    Với mỗi số $x$ (ở vị trí $i$) trong mảng, ta tìm kiếm xem bên phải nó có tồn tại một bộ đôi $(y, z)$ trong mảng sao cho $y + z = -x$ hay không. Đến đây bài toán lại trở về với bài toán Two Sum. Tuy nhiên, ta không xét các số $x$ bằng nhau vì nó sẽ tạo ra các bộ ba giống nhau. Để bớt thời gian xét bằng nhau thì ta có thể sắp xếp mảng trước, sau đó ta chỉ xét số $x$ một lần khi nó khác số $x$ ở vị trí trước đó. Còn về việc tìm $y$ và $z$. Ta có thể tìm bằng hash table hoặc 2 con trỏ như ở bài Two Sum, tuy nhiên sau khi tìm được một bộ ba, ta phải tránh trùng lặp bằng cách cho di chuyển $y$ hoặc $z$ (tuỳ theo cách làm) sang một giá trị mới. Độ phức tạp thời gian là $O(N^2)$, độ phức tạp bộ nhớ là $O(N)$.

    Ta cũng có thể làm cách không sắp xếp. Đáp án của chúng ta sẽ là một `set` luôn, ta cũng duy trì một hashset để tránh trùng lặp $x$. Khi duyệt tìm $z$ ở bên phải $x$, ta lưu lại xem ta có thấy $y = -x - z$ trong một hash table `seen` hay chưa, trick ở đây là ta lưu `seen[nums[j]] = i` để không phải xoá hash table sau mỗi lần duyệt $x$. Ta cũng không cần phải để ý xem $y$ và $z$ có khả năng trùng không vì nếu trùng thì set đáp án sẽ lo. Độ phức tạp thời gian là $O(N^2)$, độ phức tạp bộ nhớ là $O(N)$.

## LeetCode 16 - 3Sum Closest

## LeetCode 259 - 3Sum Smaller

## LeetCode 18 - 4Sum

## LeetCode 454 - 4Sum II

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [LC 1 - Two Sum](https://leetcode.com/problems/two-sum/) - Hash Table Approach | :white_check_mark: | Unavailable public link | [Code]() | |
| [LC 1 - Two Sum](https://leetcode.com/problems/two-sum/) - 2-pointer Approach | :white_check_mark: | Unavailable public link | [Code]() | |
| [LC 15 - 3Sum](https://leetcode.com/problems/3sum/) - Hash Table Approach | :white_check_mark: | Unavailable public link | [Code]() | |
| [LC 15 - 3Sum](https://leetcode.com/problems/3sum/) - 2-pointer Approach | :white_check_mark: | Unavailable public link | [Code]() | |
| [LC 15 - 3Sum](https://leetcode.com/problems/3sum/) - No-sort Approach | :white_check_mark: | Unavailable public link | [Code]() | |
| | :white_check_mark: | Unavailable public link | [Code]() | |
| | :white_check_mark: | Unavailable public link | [Code]() | |
