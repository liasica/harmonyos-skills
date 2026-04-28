---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-comment
title: 添加留言区域
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 构建布局 > 添加留言区域
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dea44675b236edd1b76ed3f7e266db61b85815347db48163955706bc9e108dce
---

留言框的功能为：用户输入留言后点击完成，留言区域即显示留言内容。用户点击右侧的删除按钮可删除当前留言内容并重新输入。

留言区域由div、text、input关联click事件实现。开发者可以使用input组件实现输入留言的部分，使用text组件实现留言完成部分，使用commentText的状态标记此时显示的组件（通过if属性控制）。在包含文本完成和删除的text组件中关联click事件，更新commentText状态和inputValue的内容。具体的实现示例如下：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="comment-title">Comment</text>
4. <div if="{{!commentText}}">
5. <input class="comment" value="{{inputValue}}" onchange="updateValue()"></input>
6. <text class="comment-key" onclick="update" focusable="true">Done</text>
7. </div>
8. <div if="{{commentText}}">
9. <text class="comment-text" focusable="true">{{inputValue}}</text>
10. <text class="comment-key" onclick="update" focusable="true">Delete</text>
11. </div>
12. </div>
```

```
1. /* xxx.css */
2. .container {
3. margin-top: 24px;
4. background-color: #ffffff;
5. }
6. .comment-title {
7. font-size: 40px;
8. color: #1a1a1a;
9. font-weight: bold;
10. margin-top: 40px;
11. margin-bottom: 10px;
12. }
13. .comment {
14. width: 550px;
15. height: 100px;
16. background-color: lightgrey;
17. }
18. .comment-key {
19. width: 150px;
20. height: 100px;
21. margin-left: 20px;
22. font-size: 32px;
23. color: #1a1a1a;
24. font-weight: bold;
25. }
26. .comment-key:focus {
27. color: #007dff;
28. }
29. .comment-text {
30. width: 550px;
31. height: 100px;
32. text-align: left;
33. line-height: 35px;
34. font-size: 30px;
35. color: #000000;
36. border-bottom-color: #bcbcbc;
37. border-bottom-width: 0.5px;
38. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. inputValue: '',
5. commentText: false,
6. },
7. update() {
8. this.commentText = !this.commentText;
9. },
10. updateValue(e) {
11. this.inputValue = e.text;
12. },
13. }
```
