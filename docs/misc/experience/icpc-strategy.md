# Chiến thuật khi thi ICPC

## Nguồn

[Team strategy - lukipuki.github.io](https://lukipuki.github.io/contest-wiki/team-strategy.html)

## Lời tựa

Trước tiên mình muốn trình bày rằng mình không xem bản thân là một người thành công trong cộng đồng Lập trình thi đấu (Competitive Programming - CP) cũng như không phải là một người có khả năng chiến thuật tốt. Bài viết này là một bài mình dịch từ một bài viết trong blog của một cao thủ trong cộng đồng. Đây là một bài khá hay và mình nghĩ sẽ có ích cho các đội thi.

Sơ lược về tác giả: **Lukáš Poláček** - hiện đang là nghiên cứu sinh tại KTH Royal Institute of Technology, Thụy Điển (profile này là năm 2016). Anh ấy từng đạt huy chương đồng tại ACM ICPC 2010 và từng có rating cao nhất là 2676 trên TopCoder.

Sơ lược về kì thi: **ACM-ICPC** (giờ rút gọn thành **ICPC**) là kì thi lập trình thi đấu lớn và uy tín nhất thế giới. Kì thi kéo dài 5 giờ đồng hồ, mỗi đội 3 người sẽ phải suy nghĩ và giải quyết 10-12 bài toán bằng máy tính.

Sau đây là nội dung bài dịch của mình. Ngôi thứ nhất trong bài là chỉ tác giả, không phải chỉ mình.

## Mở đầu

Bài viết này nói về chiến thuật khi thi ICPC, nơi mà bạn sẽ cùng 2 đồng đội khác thi đấu trong vòng 5 giờ đồng hồ. Có nhiều kì thi khác nhau với những luật lệ khác nhau nhưng ở đây ta sẽ chỉ tập trung vào ICPC.

Có 3 yếu tố quan trọng mà bạn cần lưu ý trong suốt kì thi:

- Đây là kì thi đồng đội và mỗi team có 3 người.
- Thời gian sử dụng máy tính (computer time) rất là quý giá (5 tiếng dùng máy, nhưng có 15 tiếng suy nghĩ chia ra cho mỗi người). 
- Giai đoạn đầu là giai đoạn quan trọng nhất của kì thi.

## Chiến thuật chung

Với 3 yếu tố trên, bạn có thể triển khai được một chiến thuật ngon lành. Trong giai đoạn đầu kì thi, người code nhanh nhất đội viết code template và có thể thêm 1 script để biên dịch. Với cách tính điểm của ICPC, giải bài dễ trước là tối ưu nhất, vì vậy, 2 người còn lại có thể đọc sơ qua cả tất cả các bài thi để tìm bài dễ (1 người đọc từ bài A xuống, một người đọc từ bài J lên, ví dụ thế). Khi xác định được bài dễ rồi (giải được trong khoảng 10-15 phút chẳng hạn), đưa bài đó và mô tả nhanh bài đó cho người code nhanh nhất đội.

Hai người còn lại tiếp tục đọc lướt qua đề thi. Nếu có bài dễ hơn bài trước đó (giải được trong 5 phút), thì ưu tiên bài dễ hơn. Sau khi đọc xong toàn bộ đề thi, 2 người không code trong đội nên trao đổi về các bài họ đã đọc.

**Thứ không nên xảy ra trong giai đoạn đầu**: Sau khi đọc bài đầu tiên, mình thấy mình giải được. Mình không đọc các bài khác và cố gắng giải bài đầu trong 2 tiếng mà không xong, trong khi đề có 2 bài dễ hơn mà mình không đọc. Đó là một trong các lý do mà việc đọc hết đề và trao đổi với nhau trong giai đoạn đầu là cực kỳ quan trong.

Team tiếp tục giải các bài. Nếu có người biết cách giải 1 bài nào đó và không ai dùng máy tính, người đó nên làm bài đó luôn. Ngược lại, nếu có người đang code, chịu khó chuẩn bị solution và code sơ bộ trên giấy.

Chiến thuật tốt cần phải được áp dụng dựa theo kĩ năng của từng bạn trong đội. Ví dụ, một người giỏi nghĩ thuật nhưng code không tốt thì nên làm việc chủ yếu trên giấy, sau đó giải thích solution của mình cho người khác để họ code. Team nên train thường xuyên để tìm hiểu điểm mạnh, yếu của nhau và sau đó dùng những điểm đó để xây dựng chiến thuật tốt nhất cho đội. Ngay cả việc thiếu 1 bạn thì 2 người còn lại cũng train được. Ngoài ra, nên nhờ huấn luyện viên của bạn theo dõi tiến độ train của đội để đưa ra những lời khuyên phù hợp.

## Những mẹo khác

Giờ bạn đã thấm nhuần chiến thuật chung, đến những mẹo khác thôi.

- Nếu không chắc về solution của mình, hãy trao đổi với đồng đội. Nếu không có hướng đi, giải thích vấn đề với đồng đội.
- Nếu có thời gian, viết code ra giấy trước khi code trên máy để tiết kiệm thời gian dùng máy. Không cần code quá chi tiết, nên tập trung vào các phần quan trong nhất của code thôi.
- Không nên debug trên máy. In code ra với một số debugging output và debug trên giấy.
- Nếu không tìm ra được hướng làm, nên đi dạo hoặc đi vệ sinh. Đôi khi ý tưởng lại đến khi bạn giải quyết được nỗi buồn.
- Nếu cứ bị Wrong Answer, để bài đó đấy và giải bài khác. Có thể sau đó bạn sẽ tìm được cách giải bài cũ. Đừng ngại code lại toàn bộ, thường chỉ mất tầm 15 phút để code lại hết cả bài nếu như bạn hiểu cách giải bài đó.
- Nếu sinh được test to, hoặc test nhỏ mà bạn biết chính xác đáp án thì nên làm, cẩn thận một chút còn hơn là mất 20 phút penalty.
- Làm xong bài nào thì vứt hết các giấy tờ liên quan đến bài đó đi. Bạn sẽ không bị mất công tìm thứ mình muốn trong một đống bùi nhùi giấy tờ trên bàn, tiết kiệm thời gian sẽ tốt hơn.
- Thường xuyên xem scoreboard. Nếu có bài nhiều đội làm được thì nó hẳn là bài dễ.
- Viết ra thông tin các submission của đội trên giấy, viết thêm ra xem ai làm bài gì.
- Thường xuyên yêu cầu in code, in mỗi khi submit bài (ở đây mình cũng không hiểu ý là in code ra hay là in thông tin biến ra màn hình console để tiện theo dõi).
- Đừng quên chiến thuật lúc gần hết thời gian. Khi gần hết giờ, không nên mỗi người làm một bài mà nên tập trung 3 người làm 1 bài thôi. Đảm bảo ai cũng đang làm gì đó hữu ích (ví dụ 1 người kiểm tra code cùng với người code, 1 người nghĩ test hiểm). Mình biết việc này rất khó làm và không phải ai cũng đủ dũng cảm để bỏ qua những bài còn lại mà mình biết làm nhưng có khả năng bạn sẽ tạch cả 3 bài, hoặc bạn có thể chọn làm 1 bài chắc kèo, tùy bạn thôi.
- Trong vài trường hợp bạn nên cho 1 người thử giải 1 bài khó trong 2-3 tiếng trước khi hết giờ để tránh trường hợp sau. Giả sử mọi thứ đang đi đúng hướng và bạn dùng máy tính, giải bài thứ 8 của đội sau 4 tiếng. Có 2 bài khó nhưng bạn cần 1 giờ nghĩ và 45 phút code. 3 người các bạn có 3 giờ suy nghĩ trong 1 tiếng thời gian thực, rõ ràng nhiều hơn 1 giờ 45 phút, nhưng 1 tiếng suy nghĩ không thể chia ra cho 3 người được, và bạn phải chờ solution của 1 bạn khác trước khi code.
- Chỉ submit bừa khi bạn thấy giải được 1 bài quan trọng hơn penalty và bạn thấy code của bạn có khả năng Accepted. Thường bạn sẽ submit bừa trong vòng 30 phút cuối. Cơ mà nếu đội bạn có penalty không tốt ngay từ đầu rồi (sai rất nhiều trong giai đoạn đầu) thì penalty không quá quan trọng nữa, cứ submit thôi (thời gian submit bừa sẽ được tăng lên, 1-2 tiếng chẳng hạn). 
- Thi 5 tiếng, nhưng train 5 tiếng thì hết cả ngày của bạn rồi. Bạn có thể train 3.5 đến 4 tiếng thôi, và hiệu quả thì như nhau. Ngay cả vận động viên marathon cũng chỉ chạy 30 km mỗi ngày trong khi cuộc đua thật dài 42 km.
