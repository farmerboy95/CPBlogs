# Splay Tree: Một mình anh chấp hết

## Nguồn
[Splay Tree: One Tree to Rule Them All - zhtluo.com](https://zhtluo.com/cp/splay-tree-one-tree-to-rule-them-all.html)

## Lời tựa

Bạn có sợ các bài dùng Fenwick Tree, RMQ, Segment Tree trong lập trình thi đấu không?

Bạn có sợ cài đặt các bài tìm giá trị nhỏ nhất, lớn nhất hay tổng đoạn, mà trong đó yêu cầu cập nhật giá trị không?

Không cần phải sợ nữa. Trong bài này tôi sẽ giới thiệu cho các bạn một cấu trúc dữ liệu (CTDL) có thể giải được các dạng bài này - Splay Tree. Một mình anh chấp hếttttttttttt!

**Lưu ý**: Một nhược điểm của Splay Tree là việc nó có hằng số trong độ phức tạp lớn mặc dù nó được khấu hao về $O(\log n)$. Dùng CTDL này trên các bài có limit nhỏ sẽ có nguy cơ TLE rất lớn (bạn hoàn toàn có thể dùng các CTDL ít tốn kém hơn nếu đó là vấn đề).

**Lưu ý từ farmerboy**: Mình đã cố gắng cài đặt lại các code trong bài gốc theo một cách dễ hiểu hơn với phần comment bằng tiếng Việt.

## Tạo cây từ mảng

Cách dễ nhất để lưu trữ một dãy dữ liệu: $(1, 2, 4, 5, 6)$ là cho chúng vào một cái mảng. Mảng rất đơn giản và là một CTDL tốt để tìm các phần tử của mảng trong thời gian $O(1)$ từ vị trí của chúng.

Tuy nhiên, vấn đề xảy ra khi ta muốn chèn thêm vào dãy này. Ví dụ chèn $3$ vào giữa $2$ và $4$. Không có cách nào tốt để thực hiện điều này ngoài việc di chuyển các phần tử sau $3$ (tức là $4$, $5$, $6$). Ta sẽ tốn $O(n)$ thời gian cho $n$ phần tử.

Chắc hẳn các bạn đã biết rằng danh sách liên kết (DSLK) có thể đảo lại được: nó có thể thêm phần tử trong $O(1)$ nhưng lấy phần tử ra thì lại tốn $O(n)$. Cũng vẫn không ổn, còn cây nhị phân thì sao nhỉ?

Đầu tiên, ta cần phải thiết lập mối tương quan giữa 1 cái cây nhị phân và 1 dãy. Ta thử cách dễ trước: giả sử tất cả các phần tử nằm ở cây con trái thì nằm trước phần tử hiện tại trong dãy, và tất cả các phần tử nằm ở cây con phải thì nằm bên phải phần tử hiện tại trong dãy. Để ý là định nghĩa này tạo ra một dãy duy nhất từ 1 cây nhị phân (thứ tự *in-order*, nếu bạn đã biết). Ví dụ dãy ở trên có thể được tạo từ cây nhị phân như sau:

![figure1](figure1.svg){ style="background-color: white; display: block; margin: 0 auto" }

Đến đây việc cài đặt để tìm phần tử thứ $i$ và thêm phần tử vào CTDL rất dễ dàng.

```cpp
struct Node {
    // node cha
    Node *parent;
    // các node con
    Node *children[2];
    // số node trong cây và value của node
    int size, value;
    Node(int value) {
        this->value = value;
    }

    // tính lại số node trên cây
    void update() {
        size = 1;
        for (int i = 0; i < 2; i++) {
            if (children[i]) {
                size += children[i]->size;
            }
        }
    }
};

Node *root;

// - hàm walk này dùng để xác định ta cần đi xuống dưới 
// node con theo hướng nào và update pos
// - dir: hướng. 0 - trái, 1 - phải
// - pos: ta cần tìm node thứ "pos" của cây gốc "node"
// (node thứ 0 là node đầu tiên)
// - trả về số node trên cây con trái của cây gốc "node"
int walk(Node *node, int &dir, int &pos) {
    int leftSize = node->children[0] ? node->children[0]->size : 0;
    // các vị trí từ 0 đến leftSize sẽ nằm bên trái
    // còn lại chắc chắn nằm bên phải
    dir = (leftSize < pos);
    if (dir) {
        // nếu nằm bên phải ta cập nhật lại pos ngay lập tức
        pos -= leftSize + 1;
    }
    return leftSize;
}

// tìm node thứ "pos" trên cây gốc "root"
// (node thứ 0 là node đầu tiên)
Node* find(int pos) {
    Node *cur = root;
    int dir;
    // nếu dir == 1, ta cần đi qua phải
    // ngược lại, nếu pos < leftSize thì ta nên sang trái
    // ngược lại, pos == leftSize, chính node cur là node cần tìm
    while (pos < walk(cur, dir, pos) || dir) {
        cur = cur->children[dir];
    }
    return cur;
}

// chèn node vào vị trí thứ "pos" trên cây gốc "root"
// (node thứ 0 là node đầu tiên)
void insert(Node *node, int pos) {
    Node *cur = root;
    int dir;
    while (1) {
        // ta tìm hướng trước bằng hàm walk để cập nhật dir và pos
        // sau đó đi xuống nếu vẫn đi được
        walk(cur, dir, pos);
        if (!cur->children[dir]) {
            break;
        }
        cur = cur->children[dir];
    }

    // thêm node
    cur->children[dir] = node;
    node->parent = cur;
    
    // cập nhật size
    while (node) {
        node->update();
        node = node->parent;
    }
}
```

Giờ chúng ta xét độ phức tạp của thuật toán này. Ta có thể suy luận ra được độ phức tạp của bất kỳ thao tác nào ở trên là chiều cao cây $O(h)$, và một cây nhị phân có thể lưu $n$ phần tử với chiều cao tối thiểu là $\text{log n}$. Vì vậy ta có thể làm cho độ phức tạp của thao tác Tìm và Chèn thành $O(\log n)$.

Tuy nhiên, dùng một cây đơn giản như trên để giải là điều không dễ dàng. Một cây nhị phân có thể trở thành một "cây gậy" nếu ta không để ý. Xét cây như sau, cây này cũng có thể biểu thị dãy ban đầu:

![figure2](figure2.svg){ style="background-color: white; display: block; margin: 0 auto" }

Cây gậy này có chiều cao $n$, làm cho giả thiết về độ phức tạp của chúng ta không thành hiện thực. Vì vậy, ta cần một cách nào đó để duy trì chiều cao cây là $O(\log n)$ để giữ độ phức tạp như lý thuyết. Việc này được gọi là **cân bằng cây**, và có nhiều cách để làm như AVL, Red-Black Tree, Scapegoat Tree... Tuy nhiên, chúng ta sẽ tìm hiểu một loại cây có thể không chỉ tự cân bằng, mà còn duy trì được các thông tin bổ trợ để giúp ta tìm được những thông tin khó chịu như tổng đoạn - **Splay Tree**!

## Cân bằng cây

### Xoay

Để cân bằng cây nhị phân, ta cần một thao tác nào đó. Một thao tác phổ biến là phép xoay cây

![figure3](figure3.svg){ style="background-color: white; display: block; margin: 0 auto" }

Node $n$ và $p$ là 2 node mà ta cần chú ý, và $A$, $B$, $C$ là 3 cây con của các node này. Để ý rằng 2 cây bên trái và bên phải trong hình có thứ tự in-order là $(A,n,B,p,C)$, nhưng chúng có chiều cao hơi khác nhau một chút. Cũng cần để ý rằng ta có thể thay đổi gốc của cây thành node $n$ qua một phép xoay (là xoay $n$ lên trên)

Phép xoay được cài đặt như sau:

```cpp
// Xoay node lên, ở đây node tượng trưng cho n trong hình, parentNode là p trong hình
void rotate(Node *node) {
    // từ parent node đi xuống thì đi hướng nào mới đến node
    int dirOfNode = (node->parent->children[1] == node);
    Node *parentNode = node->parent;

    // ta cần phải chuyển node B trong hình sau khi xoay, B chính là movingChildOfNode ở đây
    Node *movingChildOfNode = node->children[dirOfNode ^ 1];

    if (parentNode->parent) {
        // update parent của parentNode để nhận node làm con mới
        parentNode->parent->children[parentNode->parent->children[1] == parentNode] = node;
    }

    // update cha và con của node
    node->parent = parentNode->parent;
    node->children[dirOfNode ^ 1] = parentNode;

    // update cha và con của parentNode, lưu ý di chuyển luôn node B
    parentNode->parent = node;
    parentNode->children[dirOfNode] = movingChildOfNode;

    if (movingChildOfNode) {
        // update cha của node B
        movingChildOfNode->parent = parentNode;
    }

    // cuối cùng update size của parentNode và node sau khi xoay
    parentNode->update();
    node->update();
}
```

Ý tưởng cơ bản của Splay rất đơn giản: những trường hợp xấu trên cây nhị phân xảy ra khi ta đến một node rất sâu trong cây (ví dụ cây rất cao chẳng hạn). Vì vậy, để giảm chi phí đến được node này trong tương lai, ta phải xoay nó lên. Thực tế thì, mỗi lần ta đến node đó, ta lại xoay nó lên gốc!

Tuy nhiên, cách này không thực sự hiệu quả. Xoay node dưới cùng trên một "cây gậy" lại tạo ra một cây dạng "gậy" khác, không làm giảm độ phức tạp đi được:

![figure4](figure4.svg){ style="background-color: white; display: block; margin: 0 auto" }

Vì vậy, ta cần tìm cách để xoay một node lên gốc. Hãy xem thao tác Splay nhé!

### Thao tác Splay

Trong thao tác splay, ta thường xoay node $n$ lên 2 lần liên tiếp để giảm độ cao của node đó đi 2 (cách này gọi là *Zig-Zag*) (độ cao của node gốc là thấp nhất):

![figure5](figure5.svg){ style="background-color: white; display: block; margin: 0 auto" }

Tuy nhiên, nếu node $n$ và cha $m$ của nó nằm cùng phía (nghĩa là cả 2 đều là node con trái hoặc đều là node con phải), thay vì xoay n lên 2 lần, ta xoay $m$ lên 1 lần, rồi xoay $n$ lên một lần nữa thì cũng có thể giảm độ cao của node đó đi 2, như sau (cách này gọi là *Zig-Zig*, vì 2 lần xoay đều theo cùng một hướng):

![figure6](figure6.svg){ style="background-color: white; display: block; margin: 0 auto" }

*Lưu ý: Trong trường hợp cha của $n$ là node gốc, chỉ cần xoay $n$ lên gốc một lần là đủ (cách này gọi là Zig).*

Ta không thể thấy ngay rằng vì sao nó hoạt động: cây bên dưới giống "cây gậy" trước và sau thao tác. Nhưng nếu làm theo ví dụ trước, nó trở nên rõ ràng hơn.
Ở hình dưới, ta áp dụng Zig-Zag, sau đó dùng Zig-Zig là sẽ ra được cây sau cùng.

![figure7](figure7.svg){ style="background-color: white; display: block; margin: 0 auto" }

Zig-Zig bằng một cách nào đó có thể làm cây có chiều cao thấp hơn sau một thao tác splay về gốc. Để biết tại sao nó hoạt động, ta cần dùng một chút toán ở đây.

### Độ phức tạp

*Lưu ý: Bạn có thể bỏ qua phần này nếu bạn không quan tâm Splay hoạt động như thế nào.*

#### Phương pháp Tiềm năng (The Potential Method)

Xét một dynamic rotating tree $T$ trên một dãy các thao tác tìm và splay-to-top $Q$.

Đầu tiên, ta thấy rằng việc tìm một node có cùng độ phức tạp thời gian với việc splay một node lên root, bởi vì chúng đều truy cập vào đường đi từ node lên root và chấm hết. Ta sẽ chỉ nói về độ phức tạp của việc splay một node lên root theo phân tích sau đây.

Một giải pháp phổ biến là [Phương pháp Tiềm năng](../../complexity_analysis/potential_method/potential_method.md) (bạn nên đọc bài viết trong link để hiểu hơn), tiếng Anh gọi là the Potential Method. Ở đây ví dụ ta có một cục pin, ta sẽ thực hiện được các hành động như sau:

- Ta có thể sạc pin bất kì lúc nào với $k$ thao tác. Hành động này tốn $k$ thời gian.
- Ta có thể dùng pin cho $k$ thao tác. Hành động này tiết kiệm $k$ thời gian.

Sau khi thực thi các hành động, tổng thời gian thực thi sẽ là:

$$\text{số thao tác ta đã dùng + chênh lệch pin trước và sau khi thực thi các hành động}$$

Thông thường ta muốn cục pin sẽ ứng với cấu trúc dữ liệu ta đang sử dụng. Trong trường hợp này ta định nghĩa cục pin $\Phi$ của cây $T$ là:

$$\begin{align}
k&=\text{số thao tác cần để thực hiện một thao tác Splay}\\
\text{size}(n)&=\text{số node trên cây con có gốc là }n\\
\text{rank}(n)&=\log_2\text{size}(n)\\
\Phi&=k\sum_{n\in T}\text{rank}(n)
\end{align}$$

Để ý rằng $rank(n) \leq \log |T|$, nên $0 \leq \Phi \leq k|T|log|T|$, nghĩa là ta giới hạn được thời lượng pin chênh lệch trước và sau khi thực thi các hành động $\Delta\Phi$ thành $O(|T|log|T|)$. Giờ ta cần chắc chắn rằng mỗi thao tác tốn $O(log|T|)$ thời gian, và ta sẽ có độ phức tạp cuối cùng là $O((|Q|+|T|)log|T|)$

#### Giới hạn thao tác

Xét một thao tác Zig-Zag:

![figure8](figure8.svg){ style="background-color: white; display: block; margin: 0 auto" }

$$\begin{align}
\text{TIME}(\text{Zig-Zag})&=k+k(\text{rank}'(n)+\text{rank}'(m)+\text{rank}'(l)-\text{rank}(n)-\text{rank}(m)-\text{rank}(l))\\
&=k(1+\text{rank}'(n)+\text{rank}'(m)+\text{rank}'(l)-\text{rank}(n)-\text{rank}(m)-\text{rank}(l))
\end{align}$$

Vì $\text{rank}(l)=\text{rank}'(n)$ (cả 2 đều là cây con),

$$\begin{align}
\text{TIME}(\text{Zig-Zag})&=k(1+\text{rank}'(m)+\text{rank}'(l)-\text{rank}(n)-\text{rank}(m))\\
&< k(1+\text{rank}'(m)+\text{rank}'(l)-2\text{rank}(n))\\
\end{align}$$

Vì

$$\begin{align}
1+\text{rank}'(m)+\text{rank}'(l)&=\log 2+\log \text{size}'(m)+\log \text{size}'(l)\\
&=\log 2\text{size}'(m)\text{size}'(l)\\
&<\log (\text{size}'(m)+\text{size}'(l))^2\\
&<\log \text{size}'^2(n)\\
&=\log \text{size}'(n)+\log \text{size}'(n)=2\text{rank}'(n)\text{,}\\
\end{align}$$

Ta chứng minh được

$$\text{TIME}(\text{Zig-Zag})<k(2\text{rank}'(n)-2\text{rank}(n))=2k(\text{rank}'(n)-\text{rank}(n))\text{.}$$

Tương tự với thao tác Zig-Zig:

![figure9](figure9.svg){ style="background-color: white; display: block; margin: 0 auto" }

$$\begin{align}
\text{TIME}(\text{Zig-Zig})&=k+k(\text{rank}'(n)+\text{rank}'(m)+\text{rank}'(l)-\text{rank}(n)-\text{rank}(m)-\text{rank}(l))\\
&=k(1+\text{rank}'(n)+\text{rank}'(m)+\text{rank}'(l)-\text{rank}(n)-\text{rank}(m)-\text{rank}(l))\\
&=k(1+\text{rank}'(m)+\text{rank}'(l)-\text{rank}(n)-\text{rank}(m))\\
&< k(1+\text{rank}'(m)+\text{rank}'(l)-2\text{rank}(n))\\
&=k(\log 2\text{size}'(m)\text{size}'(l)-2\text{rank}(n))\text{.}
\end{align}$$

Giờ ta dùng tính chất của thao tác Zig-Zig, là:

$$\text{size}(n)+\text{size}'(l)+1=(\text{size}(A)+\text{size}(B)+1)+(\text{size}(C)+\text{size}(D)+1)+1=\text{size}'(n)\text{.}$$

Vì vậy,

$$\begin{align}
\text{TIME}(\text{Zig-Zig})&<k(\log 2\text{size}'(m)\text{size}'(l)-2\text{rank}(n))\\
&=k(\log 2\text{size}'(m)(\text{size}'(n)-\text{size}(n)-1)-2\text{rank}(n))\\
&<k(\log 2\text{size}'(n)(\text{size}'(n)-\text{size}(n))-2\text{rank}(n))\\
&=k(\log 2\text{size}'(n)(\text{size}'(n)-\text{size}(n))+\text{rank}(n)-3\text{rank}(n))\\
&=k(\log 2\text{size}'(n)(\text{size}'(n)-\text{size}(n))+\log\text{size}(n)-3\text{rank}(n))\\
&=k(\log 2\text{size}'(n)\text{size}(n)(\text{size}'(n)-\text{size}(n))-3\text{rank}(n))\text{.}
\end{align}$$

Vì

$$\text{size}(n)(\text{size}'(n)-\text{size}(n)) < \frac{1}{4}\text{size}'^2(n) < \frac{1}{2}\text{size}'^2(n)\text{,}$$

$$\begin{align}
\text{TIME}(\text{Zig-Zig})&<k(\log 2\text{size}'(n)\text{size}(n)(\text{size}'(n)-\text{size}(n))-3\text{rank}(n))\\
&<k(\log \text{size}'^3(n)-3\text{rank}(n))=3k(\text{rank}'(n)-\text{rank}(n))\text{.}
\end{align}$$

Ta kết luận rằng

$$\text{TIME}(\text{Zig-Zag}),\text{TIME}(\text{Zig-Zig})<3k(\text{rank}'(n)-\text{rank}(n))\text{.}$$

Vì việc splay-to-root là một chuỗi các thao tác Zig-Zag và Zig-Zig bắt đầu với node có rank là $rank(n)$ và kết thúc ở node có rank là $rank(root) = log|T|$,

$$\begin{align}
\text{TIME}(\text{Splay-to-root})=3k(\text{rank}(\text{root})-\text{rank}(n))=O(\log |T|)\text{.}
\end{align}$$

Cuối cùng ta giới hạn được thao tác splay-to-root về độ phức tạp $O(log|T|)$ thời gian.

### Cài đặt

Ta cài đặt Splay như sau:

```cpp
// Splay node n đến khi nó là con của desiredParent (hoặc đến root nếu desiredParent null)
void splay(Node *node, Node *desiredParent = NULL) {
    while (node->parent != desiredParent) {
        // lấy node m (cha) và l (cha của m) như trong các hình vẽ
        Node *parent = node->parent, *parentOfParent = parent->parent;

        if (parentOfParent == desiredParent) {
            // nếu l là desiredParent thì ta chỉ cần xoay một lần - Zig
            rotate(node);
        } else if ((parentOfParent->children[0] == parent) == (parent->children[0] == node)) {
            // nếu n và m cùng hướng (cùng là node con trái hoặc cùng là node con phải) - Zig-Zig
            rotate(parent);
            rotate(node);
        } else {
            // trường hợp còn lại - Zig-Zag
            rotate(node);
            rotate(node);
        }
    }

    // nếu desiredParent null thì update root
    if (!desiredParent) {
        root = node;
    }
}
```

## Các thao tác trên Splay Tree

Để tổng hợp lại những gì đã học, chúng ta đã cài Splay Tree giúp

- Tìm một phần tử tại một vị trí xác định;
- Chèn một phần tử vào một vị trí xác định

trong thời gian phân bổ $O(\log n)$. Đó là điều rất tốt vì $O(\log n)$ rất nhỏ. Ta sẽ xem xét một số ví dụ và tôi sẽ trình bày một ví dụ cụ thể với mã nguồn.

### Tổng đoạn

Truy vấn thông dụng nhất trên dãy $(x_1,x_2,\ldots,x_n)$ là tìm tổng đoạn $\sum_{i=l}^{r}x_i$.

Bạn có thể rất ngạc nhiên khi ta đã có cách cài đặt (kiểu thế) cái này trong những code trước rồi. Nhớ lại là chúng ta đã duy trì kích thước mỗi cây con với `node.size` và `node.update()`. Vì vậy nên ta có thể duy trì tổng đoạn theo cách y như vậy. Vấn đề bây giờ là tìm cây con ứng với đoạn $[x_l,x_r]$.

Cách giải khá là đơn giản: ta có thể splay node $x_{r+1}$ về root, và node $x_{l-1}$ về làm con của node $x_{r+1}$. Thì cây con ứng với $[x_l,x_r]$ sẽ xuất hiện:

![figure10](figure10.svg){ style="background-color: white; display: block; margin: 0 auto" }

*Lưu ý: Trong trường hợp này ta giả sử $x_{l-1}$ và $x_{r+1}$ đều có tồn tại. Trong thực tế, ta có thể thêm node đầu và node đuôi giả để điều kiện trên luôn thoả mãn.*

### Xoá đoạn

Xoá trên Splay Tree rất dễ dàng. Ví dụ ta muốn xoá một đoạn $[x_l, x_r]$, ta chỉ cần tìm cây con tương ứng với đoạn đó, rồi xoá nó ra khỏi cây.

### Gán tất cả các phần tử của đoạn bằng một số nào đó

Thông thường ta muốn chỉnh sửa đoạn $[x_l,x_r]$ theo một cách nào đó: thêm giá trị, gán giá trị bằng một số nào đó, ... Ta sẽ xem xét một ví dụ mà ta cần gán tất cả các phần tử trong đoạn $[x_l,x_r]$ bằng một số $v$ nào đó.

Ta sẽ duy trì một lazy label trên mỗi node. Một lazy label có thể là null hoặc giá trị nào đó. Nếu label $c$ không phải null, ta coi cây con của node tương ứng như thể mọi node trên cây con đó đều có giá trị là $c$. Vì vậy, để áp dụng thao tác này, ta chỉ cần tìm cây con $[x_l,x_r]$ và gán cho gốc của cây con này và label của nó là $c$.

Rõ ràng là khi ta thực sự dùng một node, ta cần chắc chắn rằng tổ tiên của nó không có lazy label nào, vì các label này có thể can thiệp vào giá trị của node hiện tại. Thật may là ta có thể dùng `push_down` để xoá label với mọi node tổ tiên, bắt đầu từ node gốc:

1. Áp dụng thao tác gán phần tử trên 2 con của node:
    1. Gán giá trị của 2 con của node thành $c$.
    2. Gán label của 2 con của node thành $c$.
2. Gán label của node thành null.

Ta có thể viết lại hàm `walk` để nó có thể `push_down` liên tục:

```cpp

// - hàm walk này dùng để xác định ta cần đi xuống dưới 
// node con theo hướng nào và update pos
// - dir: hướng. 0 - trái, 1 - phải
// - pos: ta cần tìm node thứ "pos" của cây gốc "node"
// (node thứ 0 là node đầu tiên)
// - trả về số node trên cây con trái của cây gốc "node"
int walk(Node *node, int &dir, int &pos) {
    node->push_down();
    int leftSize = node->children[0] ? node->children[0]->size : 0;
    // các vị trí từ 0 đến leftSize sẽ nằm bên trái
    // còn lại chắc chắn nằm bên phải
    dir = (leftSize < pos);
    if (dir) {
        // nếu nằm bên phải ta cập nhật lại pos ngay lập tức
        pos -= leftSize + 1;
    }
    return leftSize;
}

// tìm node thứ "pos" trên cây gốc "root"
// (node thứ 0 là node đầu tiên)
// nếu sp true thì ta splay
Node* find(int pos, int sp = true) {
    Node *cur = root;
    int dir;
    // thêm node đầu giả vào cây
    pos++;
    // nếu dir == 1, ta cần đi qua phải
    // ngược lại, nếu pos < leftSize thì ta nên sang trái
    // ngược lại, pos == leftSize, chính node cur là node cần tìm
    while (pos < walk(cur, dir, pos) || dir) {
        cur = cur->children[dir];
    }
    if (sp) splay(cur);
    return cur;
}
```

### Đảo đoạn

Cuối cùng ta xét một ví dụ: đảo đoạn $[x_l,x_r]$ trong dãy thành $(x_r, x_{r-1}, \ldots, x_l)$.

Ta cài thao tác này theo cách tương tự như trên: Duy trì một label để coi cây có bị đảo hay không. Sau đó, khi `push_down`:

1. Nếu label được set thì ta áp dụng thao tác đảo trên 2 con của node:
    1. Đảo con trái của 2 node con.
    2. Đảo con phải của 2 node con.
    3. Set label của 2 node con của node hiện tại để đảo label của chúng.
2. Set label của node thành null.

## Ví dụ

Ta sẽ xem ví dụ giải bài [POJ 3580](http://codeforces.com/gym/103997/problem/A)

Ở đây mình đã thêm các comment bằng tiếng Việt để các bạn tiện theo dõi.

```cpp
// Lược bỏ các đoạn define và constant

// Splay Tree Node
struct Node {
    // định nghĩa parent node and 2 node con của nó
    Node* parent, *children[2];
    // kích thước subtree với gốc là node hiện tại
    int size;
    // giá trị node, min của subtree và label của phép cộng lazy
    ll val, Min, labelAdd;
    // label của phép đảo lazy
    int labelReverse;

    // hàm khởi tạo
    Node(int val) {
        parent = children[0] = children[1] = NULL;
        size = 1;
        this->val = val;
        Min = labelAdd = labelReverse = 0;
    }

    // thêm v vào cả subtree
    void add(ll v) {
        // thêm v giá trị node, min và labelAdd
        val += v;
        Min += v;
        labelAdd += v;
    }

    // áp các label vào và đẩy chúng xuống các node con
    void pushDown() {
        if (labelReverse) {
            FOR(i,0,1) {
                if (children[i]) {
                    children[i]->reverse();
                }
            }
            labelReverse = 0;
        }

        if (labelAdd) {
            FOR(i,0,1) {
                if (children[i]) {
                    children[i]->add(labelAdd);
                }
            }
            labelAdd = 0;
        }
    }

    // update kích thước subtree và min của subtree
    void update() {
        size = 1;
        Min = val;
        FOR(i,0,1) {
            if (children[i]) {
                size += children[i]->size;
                ckmin(Min, children[i]->Min);
            }
        }
    }

    // đảo cả subtree, đầu tiên cần đảo 2 con của node trước
    void reverse() {
        swap(children[0], children[1]);
        labelReverse ^= 1;
    }
};

struct SplayTree {
    Node *root;

    // tạo splay tree với 2 node đầu cuối giả
    SplayTree() {
        root = new Node(-1);
        root->children[1] = new Node(-1);
        root->size = 2;
        root->children[1]->parent = root;
    }

    // vì có 2 node giả nên size trả về ít hơn 2 so với size thực
    int size() { 
        return root->size - 2;
    }

    // hàm rotate node
    void rotate(Node *node) {
        int dirOfNode = (node->parent->children[1] == node);
        Node *parentNode = node->parent;

        Node *movingChildOfNode = node->children[dirOfNode ^ 1];

        if (parentNode->parent) {
            parentNode->parent->children[parentNode->parent->children[1] == parentNode] = node;
        }

        node->parent = parentNode->parent;
        node->children[dirOfNode ^ 1] = parentNode;

        parentNode->parent = node;
        parentNode->children[dirOfNode] = movingChildOfNode;

        if (movingChildOfNode) {
            movingChildOfNode->parent = parentNode;
        }

        parentNode->update();
        node->update();
    }

    // splay node để nó nằm ngay dưới desiredParent hoặc nằm ở root nếu desiredParent null
    void splay(Node *node, Node *desiredParent = NULL) {
        while (node->parent != desiredParent) {
            Node *parent = node->parent, *parentOfParent = parent->parent;
            if (parentOfParent == desiredParent) {
                rotate(node);
            } else if ((parentOfParent->children[0] == parent) == (parent->children[0] == node)) {
                rotate(parent);
                rotate(node);
            } else {
                rotate(node);
                rotate(node);
            }
        }
        if (!desiredParent) {
            root = node;
        }
    }

    // hàm walk này dùng để xác định ta cần đi xuống dưới node con theo hướng nào và update pos
    int walk(Node *node, int &dir, int &pos) {
        node->pushDown();
        int leftSize = node->children[0] ? node->children[0]->size : 0;
        dir = (leftSize < pos);
        if (dir) {
            pos -= leftSize + 1;
        }
        return leftSize;
    }

    // thêm node vào vị trí pos
    void insert(Node *node, int pos) {
        Node *cur = root;
        int dir;
        // ta có node đầu giả và pos bắt đầu từ 0, nên ta tăng pos
        pos++;
        while (1) {
            walk(cur, dir, pos);
            if (!cur->children[dir]) {
                break;
            }
            cur = cur->children[dir];
        }

        cur->children[dir] = node;
        node->parent = cur;
        // thêm vào rồi thì ta splay nó lên root
        splay(node);
    }

    // Tìm node ở vị trí pos, nếu sp thì ta splay nó.
    Node* find(int pos, int sp = true) {
        Node *cur = root;
        int dir;
        // ta có node đầu giả và pos bắt đầu từ 0, nên ta tăng pos
        pos++;
        while (pos < walk(cur, dir, pos) || dir) {
            cur = cur->children[dir];
        }
        if (sp) splay(cur);
        return cur;
    }

    // Tìm đoạn [posL, posR)
    // splay node posR lên gốc, sau đó splay posL-1 lên ở ngay dưới posR, sau đó đoạn [posL, posR-1] sẽ thuộc quyền quản lý của node con bên phải node posL-1
    Node *findRange(int posL, int posR) {
        Node *r = find(posR), *l = find(posL - 1, false);
        splay(l, r);
        if (l->children[1]) l->children[1]->pushDown();
        return l->children[1];
    }

    // xoá đoạn [posL, posR)
    // tìm đoạn rồi ngắt nó ra khỏi cây
    Node* eraseRange(int posL, int posR) {
        Node *range = findRange(posL, posR);
        range->parent->children[1] = NULL;
        range->parent->update();
        range->parent->parent->update();
        range->parent = NULL;
        return range;
    }

    // in cây gốc cur theo in-order
    void print(Node *cur, string pref) {
        if (cur == NULL) return;
        // nhớ push down khi đi xuống từng node
        cur->pushDown();
        print(cur->children[1], pref + "  ");
        cout << pref << cur->val << "\n";
        print(cur->children[0], pref + "  ");
    }

    // in cả cây theo thứ tự in-order
    // cây trong output sẽ giống cây thực nếu bạn xoay nó 90 độ theo chiều kim đồng hồ
    void printTree() {
        print(root, "");
        cout << "\n";
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    int n, m;
    cin >> n;
    SplayTree t;
    while (n--) {
        ll x;
        cin >> x;
        t.insert(new Node(x), t.size());
    }

    cin >> m;
    while (m--) {
        string s;
        int x, y, k;
        cin >> s;
        if (s == "ADD") {
            cin >> x >> y >> k;
            // tìm đoạn và thêm k vào
            t.findRange(x-1, y)->add(k);
        } else if (s == "REVERSE") {
            cin >> x >> y;
            // tìm đoạn và đảo nó
            t.findRange(x-1, y)->reverse();
        } else if (s == "REVOLVE") {
            cin >> x >> y >> k;
            // xem ta cần đẩy bao nhiêu, rồi lấy đoạn sau insert vào phía trước
            k %= (y - x + 1);
            if (k) {
                Node *right = t.eraseRange(y-k, y);
                t.insert(right, x-1);
            }
        } else if (s == "INSERT") {
            cin >> x >> k;
            // thêm node k vào vị trí x
            t.insert(new Node(k), x);
        } else if (s == "DELETE") {
            cin >> x;
            // xoá node ở vị trí x
            t.eraseRange(x-1, x);
        } else {
            cin >> x >> y;
            // lấy min của đoạn
            cout << t.findRange(x-1, y)->Min << "\n";
        }
    }
    return 0;
}
```

## Luyện tập

| Problem | Status | Submission | Code | Date |
| :---: | :-----------: | :---: | :---: | :---: |
| [POJ 3580](http://codeforces.com/gym/103997/problem/A) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/Codeforces/CF103997-Gym-A.cpp) | 11/11/2022 |
| [HDU 3487](http://acm.hdu.edu.cn/showproblem.php?pid=3487) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/HDU/HDU%203487.cpp) | 11/11/2022 |
| [SPOJ ADALIST](https://www.spoj.com/problems/ADALIST/) | :white_check_mark: | Unavailable public link | [Code](https://github.com/farmerboy95/CompetitiveProgramming/blob/master/SPOJ/SPOJ%20ADALIST.cpp) | 11/11/2022 | 
