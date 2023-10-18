# 0-1 BFS

## Nguồn

<img src="../../../../assets/images/cpalgorithms.ico" width="16" height="16"/> [0-1 BFS](https://cp-algorithms.com/graph/01_bfs.html)

## Giới thiệu

Bạn chắc hẳn đã quen thuộc với việc tìm đường đi ngắn nhất từ một nguồn đến tất cả các node khác trong **đồ thị không trọng số** trong thời gian $O(|E|)$ bằng thuật toán BFS (khoảng cách là số cạnh nhỏ nhất từ nguồn đến đích). Ta có thể xem đồ thị không trọng số như một đồ thị có trọng số, trong đó mỗi cạnh có trọng số là $1$. Nếu trọng số của các cạnh không bằng nhau, ta cần một thuật toán tổng quát hơn, như Dijkstra, chạy trong thời gian $O(|V|^2 + |E|)$ hoặc $O(|E| \log |V|)$.

Tuy nhiên, nếu trọng số của các cạnh có một số ràng buộc, ta có thể làm tốt hơn. Trong bài viết này, ta sẽ đi vào tìm hiểu cách sử dụng BFS để giải quyết bài toán tìm đường đi ngắn nhất từ một nguồn đến tất cả các node khác trong đồ thị có trọng số $0$ hoặc $1$ trong thời gian $O(|E|)$.

## Thuật toán

Trước hết ta đi vào nghiên cứu thuật toán Dijkstra và xem thử đồ thị đặc biệt của chúng ta có thể có những hệ quả nào. Dạng tổng quát của thuật toán Dijkstra như sau (ở đây ta sử dụng `set` để làm hàng đợi ưu tiên):

```cpp
d.assign(n, INF);
d[s] = 0;
set<pair<int, int>> q;
q.insert({0, s});
while (!q.empty()) {
    int v = q.begin()->second;
    q.erase(q.begin());

    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;

        if (d[v] + w < d[u]) {
            q.erase({d[u], u});
            d[u] = d[v] + w;
            q.insert({d[u], u});
        }
    }
}
```

Trong trường hợp đồ thị của ta (cạnh có trọng số bằng $0$ hoặc $1$), ta thấy rằng $|d[i] - d[j]|$ (với $i$ và $j$ là 2 node bất kỳ trong hàng đợi) không quá 1. Đặc biệt, ta biết rằng $d[v] \le d[u] \le d[v] + 1$ với mọi $u \in Q$. Đó là bởi vì, ta chỉ thêm các node có khoảng cách bằng nhau hoặc khoảng cách lớn hơn 1 so với node hiện tại vào hàng đợi trong mỗi lần lặp. Giả sử tồn tại một node $u$ trong hàng đợi với $d[u] - d[v] > 1$, thì $u$ phải được thêm vào hàng đợi thông qua một node khác $t$ với $d[t] \ge d[u] - 1 > d[v]$. Tuy nhiên điều này là không thể, vì thuật toán Dijkstra lặp qua các node theo thứ tự tăng dần.

Điều này có nghĩa là, thứ tự của hàng đợi sẽ như sau:

$$Q = \underbrace{v}_{d[v]}, \dots, \underbrace{u}_{d[v]}, \underbrace{m}_{d[v]+1} \dots \underbrace{n}_{d[v]+1}$$

Cấu trúc này đơn giản đến mức ta không cần một hàng đợi ưu tiên, tức là ta không cần một cây nhị phân cân bằng. Ta có thể sử dụng một hàng đợi thông thường, và thêm các node mới vào đầu hàng đợi nếu cạnh tương ứng có trọng số $0$, tức là $d[u] = d[v]$, hoặc thêm vào cuối hàng đợi nếu cạnh có trọng số $1$, tức là $d[u] = d[v] + 1$. Như vậy, hàng đợi sẽ giữ nguyên thứ tự sắp xếp.

```cpp
vector<int> d(n, INF);
d[s] = 0;
deque<int> q;
q.push_front(s);
while (!q.empty()) {
    int v = q.front();
    q.pop_front();
    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;
        if (d[v] + w < d[u]) {
            d[u] = d[v] + w;
            if (w == 1)
                q.push_back(u);
            else
                q.push_front(u);
        }
    }
}
```

## Thuật toán Dial

Ta có thể mở rộng thuật toán trên nếu ta cho phép trọng số của các cạnh lớn hơn $1$. Nếu mỗi cạnh có trọng số $\le k$, thì khoảng cách của các node trong hàng đợi sẽ chênh lệch tối đa $k$ so với khoảng cách của node hiện tại đến nguồn. Vì vậy, ta có thể sử dụng $k + 1$ hàng đợi để lưu trữ các node trong hàng đợi, và mỗi khi hàng đợi có khoảng cách nhỏ nhất trở thành rỗng, ta dịch chuyển các hàng đợi để lấy hàng đợi có khoảng cách nhỏ nhất tiếp theo. Biến thể mở rộng này được gọi là **Thuật toán Dial**.

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [Codeforces - Labyrinth](https://codeforces.com/contest/1063/problem/B) | :white_check_mark: | [Submission](https://codeforces.com/contest/1063/submission/228375510) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF1063-D1-B.cpp) | 16/10/2023 |
| [SPOJ - KATHTHI](http://www.spoj.com/problems/KATHTHI/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20KATHTHI.cpp) | 16/10/2023 |
| [TopCoder SRM 436 Round 1 - DoNotTurn](https://community.topcoder.com/stat?c=problem_statement&pm=10337) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/TopCoder/SRM436-D1-500.cpp) | 17/10/2023 |
| [UVA 11573 - Ocean Currents](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2620) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/UVA/UVA%2011573.cpp) | 16/10/2023 |
| [Codeforces - Olya and Energy Drinks](https://codeforces.com/contest/877/problem/D) | :white_check_mark: | [Submission](https://codeforces.com/contest/877/submission/228506864) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF877-D2-D.cpp) | 17/10/2023 |
| [Codeforces - Three States](https://codeforces.com/contest/590/problem/C) | :white_check_mark: | [Submission](https://codeforces.com/contest/590/submission/228627852) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF590-D1-C.cpp) | 18/10/2023 |
| [UVA 11574 - Colliding Traffic](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2621)| :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/UVA/UVA%2011574.cpp) | 18/10/2023 |
| [Codeforces - Chamber of Secrets](https://codeforces.com/contest/173/problem/B) | :white_check_mark: | [Submission](https://codeforces.com/contest/173/submission/228530106) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF173-D12-B.cpp) | 17/10/2023 |
| [Codeforces - Spiral Maximum](https://codeforces.com/contest/173/problem/C) | :white_check_mark: | [Submission](https://codeforces.com/contest/173/submission/228555646) | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF173-D12-C.cpp) | 17/10/2023 |
| [LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/LeetCode/LC1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid.cpp) | 16/10/2023 |
