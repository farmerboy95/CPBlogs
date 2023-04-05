# Xác suất

## Nguồn

<img src="/CPBlogs/img/brilliant.png" width="16" height="16"/> [Probability - Brilliant](https://brilliant.org/wiki/probability/)

## Lời tựa

Một **xác suất** là một con số biểu diễn khả năng xảy ra của một biến cố không chắc chắn. Xác suất thường có giá trị nằm trong đoạn $[0, 1]$. Xác suất càng cao thì biến cố càng có khả năng xảy ra. Xác suất bằng $0$ nghĩa là biến cố sẽ không xảy ra. Xác suất bằng $1$ nghĩa là biến cố luôn xảy ra. Tất cả các giá trị còn lại nằm giữa $0$ và $1$ thể hiện nhiều cấp độ của khả năng xảy ra của biến cố.

Nghiên cứu về xác suất rất quan trọng vì nó giải quyết các vấn đề định lượng với kết quả không chắc chắn. Ví dụ, trong sản xuất, ta không thể chắc chắn được rằng quy trình sản xuất sẽ không tạo ra các sản phẩm lỗi. Sẽ cực kỳ tốn kém và mất thì giờ để kiểm tra từng sản phẩm khi xuất xưởng. Hiểu được xác suất lỗi này sẽ giúp công ty xử lý lỗi thông minh hơn nhiều.

Các ứng dụng của xác suất gần như là vô hạn, nhưng ta sẽ chỉ đề cập đến một vài trong số đó.

## Giải thích xác suất

Có hai cách hiểu chính về xác suất: **xác suất theo chủ nghĩa khách quan (objectivist probability)** và **xác suất theo chủ nghĩa chủ quan (subjectivist probability)**.

**Xác suất khách quan** đề cập đến các phép thử có thể được lặp lại nhiều lần để phân tích kết quả, ví dụ như việc phân tích các thử nghiệm thuốc lâm sàng. Các nhà khoa học và bác sĩ sẽ đưa cho những người tham gia thử nghiệm một loại thuốc mới, và trong suốt quá trình thử nghiệm, họ sẽ phân tích hiệu quả của loại thuốc đó. Vì có nhiều người tham gia thử nghiệm thuốc nên một thí nghiệm hiệu quả sẽ cho phép các bác sĩ và nhà khoa học chỉ định xác suất hiệu quả của loại thuốc đó. Xác suất này sẽ đại diện cho tỉ lệ người tham gia nhận được tác dụng có lợi từ thuốc.

Một số biến cố không chắc chắn khác không có cơ hội được kiểm tra qua nhiều lần thử, nhưng vẫn mong muốn có một xác suất nào đó. Trong trường hợp này, các nhà toán học sẽ coi xác suất là một thước đo mức độ tin tưởng rằng biến cố nào đó sẽ xảy ra. Điều này được gọi là **xác suất chủ quan**, chẳng hạn như việc dự báo thời tiết. Các nhà khí tượng học sẽ gán xác suất cho một số sự kiện thời tiết xảy ra, như khả năng có mưa ở một khu vực nhất định. Xác xác suất này được tính bằng cách sử dụng dữ liệu thu thập từ vệ tinh cũng như dữ liệu lịch sử. Không giống như xác suất khách quan, xác suất này không thể được kiểm tra qua nhiều thử nghiệm vì các tình huống chính xác dẫn đến dự đoán sẽ không bao giờ lặp lại nữa.

## Xác suất trong tài chính và kinh tế

Mỗi khi một người đi đầu tư, người đó đang tham gia vào phân tích xác suất, dù người đó có nhận ra hay không. Mỗi khoản đầu tử đều có một số mức độ không chắc chắn. Không ai có thể chắc chắn giá trị của khoản đầu tư đó sẽ như thế nào trong tương lai. Bằng cách chi tiền cho một khoản đầu tư, về cơ bản, bạn đang nói rằng có *khả năng cao* là khoản đầu tư đó sẽ tằng giá trị.

Các nhà phân tích tài chính chuyên nghiệp có xu hướng nhấn mạnh rõ ràng hơn về xác suất khi thực hiện phân tích các khoản đầu tư. Họ sẽ dùng các dữ liệu lịch sử và luồng thông tin hàng ngày để ấn định xác suất mà một khoản đầu tư sẽ tăng hoặc giảm giá trị. Các phân tích này sẽ được đưa vào thị trường và ảnh hưởng đến giá cả hàng hoá.

**Ví dụ:** Một nhà phân tích tài chính đã phân tích một công ty mới và ước tính các thông tin sau về nó:

Giá trị hiện tại của công ty là 1,1 triệu USD.

Có một xác suất 0,8 rằng công ty sẽ trị giá 0,9 triệu USD trong một năm.

Có một xác suất 0,15 rằng công ty sẽ trị giá 1,3 triệu USD trong một năm.

Có một xác suất 0,05 rằng công ty sẽ trị giá 2,0 triệu USD trong một năm.

Nếu triển vọng đầu tư dựa trên giá trị dự kiến trong tương lai của công ty, thì triển vọng đầu tư hiện tại vào công ty là gì?

??? tip "Lời giải"
    Có vài kết quả khác nhau về cách thức hoạt động của công ty này nhưng chúng ta có thể ước tính giá trị tương lai của công ty bằng cách dùng xác suất.

    Giá trị tương lai ước tính của công ty tính bằng triệu USD là:

    $$(0.8 \times 0.9) + (0.15 \times 1.3) + (0.05 \times 2.0) = 1.015$$

    Con số này thấp hơn giá trị hiện tại của công ty, vì vậy một nhà đầu tư thông minh sẽ bán cổ phần của họ trong công ty.

Trong ví dụ này, nếu nhiều nhà phân tích tài chính thu được cùng một kết quả khi họ tính toán giá trị tương lai của công ty, thì thị trường sẽ điều chỉnh và giá trị của công ty sẽ thay đổi.

## Xác suất trong dược học

Xác suất được sử dụng trong nghiên cứu y học để định lượng hiệu quả của thuốc và các thủ thuật y tế. Trước khi một loại thuốc có thể đưa ra thị trường, nó phải vượt qua các thử nghiệm lâm sàng. Trong một thử nghiệm lâm sàng, nhiều người tham gia được cho dùng một loại thuốc và hiệu quả của loại thuốc đó được đo lường theo thời gian. Ngoài ra còn có một nhóm người tham gia được gọi là "nhóm đối chứng". Trong nhóm này, những người tham gia được làm cho tin rằng họ được cho dùng thuốc, nhưng thực tế họ được cho dùng giả dược (một viên đường chẳng hạn).

Các nhà khoa học đo lường hiệu quả của nhóm thuốc so với hiệu quả của nhóm đối chứng. Rất nhiều phân tích được thực hiện để đảm bảo rằng thuốc không chỉ hiệu quả mà còn tốt hơn là không làm gì cả (nhóm đối chứng). Việc một loại thuốc có *thực sự* hiệu quả hay không có thể là một nguồn gây tranh cãi lớn trong cộng đồng nghiên cứu y học.

**Ví dụ:**

Các nhà khoa học dược phẩm vừa phát triển một loại thuốc cảm mới, được đặt tên là MiraQuil.

Các nhà khoa học đã đưa loại thuốc này qua nhiều thử nghiệm lâm sàng. Họ phát hiện ra rằng trong số những người tham gia (bị cảm và sau đó được dùng thuốc), 98% trong số họ không có triệu chứng cảm sau một tuần!

Các nhà khoa học đã chứng minh rằng thuốc của họ có hiệu quả chưa? Họ có nên bắt đầu bán thuốc hay không?

??? tip "Lời giải"
    Phần thông tin quan trọng nhất còn thiếu trong các thử nghiệm lâm sàng là hiệu suất của nhóm đối chứng. Nếu không biết những người bị cảm lạnh sẽ như thế nào khi họ không dùng thuốc, thì không thể biết hiệu quả của thuốc.

    Khá hợp lý khi cho rằng nhiều triệu chứng cảm lạnh sẽ biến mất sau một tuần, ngay cả khi không dùng bất kỳ loại thuốc nào. Rất có thể nhóm đối chứng cũng có kết quả "thần kỳ" không kém. Tuy nhiên, không xem số liệu thì không thể biết được.

    Câu trả lời là KHÔNG.

## Xác suất trong sản xuất

Nghiên cứu về xác suất cho phép đưa ra quyết định thông minh trong sản xuất. Đặc biệt, nó cho phép các nhà quản lý nhà máy đưa ra quyết định hiệu quả về chi phí khi kiểm soát chất lượng. Bằng cách phân tích xác suất của một sản phẩm bị lỗi và hậu quả tài chính của một sản phẩm bị lỗi, các nhà quản lý nhà máy có thể sử dụng tiền và nguồn lực của họ một cách hiệu quả nhất để giúp sản xuất các sản phẩm có chất lượng.

**Ví dụ:**

Một nhà máy sản xuất bàn chải đánh răng sản xuất $200000$ bàn chải đánh răng mỗi ngày. Quy trình sản xuất không hoàn hảo và đôi khi có những bàn chải đánh răng bị lỗi.

Một nhà phân tích đã tính toán rằng mỗi bàn chải đánh răng có xác suất bị lỗi là 0,004. Nếu một khách hàng nhận được một sản phẩm bị lỗi, thì công ty sẽ phải trả 5 đô la để thay thế sản phẩm và làm hài lòng khách hàng.

Giám đốc nhà máy có thể chọn thuê một nhóm Đảm bảo Chất lượng để tìm và sửa chữa tất cả các bàn chải đánh răng bị lỗi khi chúng được sản xuất. Số tiền tối đa mà giám đốc nhà máy sẵn sàng chi cho đội này mỗi ngày là bao nhiêu?

??? tip "Lời giải"
    Nếu nhà máy sản xuất $200000$ bàn chải mỗi ngày, mỗi bàn chải có xác suất lỗi là $0.004$, ta có thể ước lượng rằng nhà máy sản xuất $200000 \times 0.004 = 800$ bản chải lỗi mỗi ngày.

    Mỗi bàn chải lỗi làm công ty mất $\$5$ đô, thì tổng thiệt hại một ngày là $\$5 \times 800 = \$4000$.

    Nếu đội đảm bảo chất lượng có thể tìm ra tất cả sản phẩm lỗi, thì chi phí cho đội này phải ít hơn chi phí cho các sản phẩm lỗi. Vì vậy, người quản lý sẽ phải trả tối đa $\$4000$ mỗi ngày cho đội này.
