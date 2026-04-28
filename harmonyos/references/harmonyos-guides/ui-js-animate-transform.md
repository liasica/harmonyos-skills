---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-transform
title: transform样式动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > CSS动画 > transform样式动画
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:33+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:dbc034125a808374258b2fddd43f0715cafc4aecb6e6c0e58bb72f6544e4afae
---

设置transform属性对组件进行旋转、缩放、移动和倾斜。

## 设置静态动画

创建一个正方形并旋转90°变成菱形，并用下方的长方形把菱形下半部分遮盖形成屋顶，设置长方形translate属性值为(150px,-150px)确定坐标位置形成门，再使用position属性使横纵线跟随父组件（正方形）移动到指定坐标位置，接着设置scale属性使父子组件一起变大形成窗户大小，最后使用skewX属性使组件倾斜后设置坐标translate(200px,-710px)得到烟囱。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="top"></div>
4. <div class="content"></div>
5. <div class="door"></div>
6. <!-- 窗户 -->
7. <div class="window">
8. <div class="horizontal"></div>
9. <div class="vertical"></div>
10. </div>
11. <div class="chimney"></div>
12. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. background-color:#F1F3F5;
6. align-items: center;
7. flex-direction: column;
8. }
9. .top{
10. z-index: -1;
11. position: absolute;
12. width: 428px;
13. height: 428px;
14. background-color: #860303;
15. transform: rotate(45deg);
16. margin-top: 284px;
17. margin-left: 148px;
18. }
19. .content{
20. margin-top: 500px;
21. width: 600px;
22. height: 400px;
23. background-color: white;
24. border:  1px solid black;
25. }
26. .door{
27. width: 100px;
28. height: 135px;
29. background-color: #1033d9;
30. transform: translate(150px,-137px);
31. }
32. .window{
33. z-index: 1;
34. position: relative;
35. width: 100px;
36. height: 100px;
37. background-color: white;
38. border: 1px solid black;
39. transform: translate(-150px,-400px) scale(1.5);
40. }
41. /* 窗户的横轴 */
42. .horizontal{
43. position: absolute;
44. top: 50%;
45. width: 100px;
46. height: 5px;
47. background-color: black;
48. }
49. /* 窗户的纵轴 */
50. .vertical{
51. position: absolute;
52. left: 50%;
53. width: 5px;
54. height: 100px;
55. background-color: black;
56. }
57. .chimney{
58. z-index: -2;
59. width: 40px;
60. height: 100px;
61. border-radius: 15px;
62. background-color: #9a7404;
63. transform: translate(200px,-710px) skewX(-5deg);
64. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/AZ49kAz6QrOYkxkoaPjQ6w/zh-cn_image_0000002583478143.png?HW-CC-KV=V1&HW-CC-Date=20260427T234032Z&HW-CC-Expire=86400&HW-CC-Sign=FF9779EB6061D8DB00FFF901C59734C54936DB13E220F4B0E2E0C556D4D1959D)

## 设置平移动画

小球下降动画，改变小球的Y轴坐标实现小球下落，在下一段时间内减小Y轴坐标实现小球回弹，让每次回弹的高度逐次减小直至回弹高度为0，就模拟出了小球下降的动画。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="circle"></div>
4. <div class="flower"></div>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. background-color:#F1F3F5;
6. display: flex;
7. justify-content: center;
8. }
9. .circle{
10. width: 100px;
11. height: 100px;
12. border-radius: 50px;
13. background-color: red;
14. /* forwards停在动画的最后一帧 */
15. animation: down 3s fast-out-linear-in forwards;
16. }
17. .flower{
18. position: fixed;
19. width: 80%;
20. margin-left: 10%;
21. height: 5px;
22. background-color: black;
23. top: 1000px;
24. }
25. @keyframes down {
26. 0%{
27. transform: translate(0px,0px);
28. }
29. /* 下落 */
30. 15%{
31. transform: translate(10px,900px);
32. }
33. /* 开始回弹 */
34. 25%{
35. transform: translate(20px,500px);
36. }
37. /* 下落 */
38. 35%{
39. transform: translate(30px,900px);
40. }
41. /* 回弹 */
42. 45%{
43. transform: translate(40px,700px);
44. }
45. 55%{
46. transform: translate(50px,900px);
47. }
48. 65%{
49. transform: translate(60px,800px);
50. }
51. 80%{
52. transform: translate(70px,900px);
53. }
54. 90%{
55. transform: translate(80px,850px);
56. }
57. /* 停止 */
58. 100%{
59. transform: translate(90px,900px);
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/uTCsc3E-Q4-ZdSb73aaYQQ/zh-cn_image_0000002552798494.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234032Z&HW-CC-Expire=86400&HW-CC-Sign=DE60EAB335AE60090E15E5DF0D2553AB7DA3C83221ABC3787480B81323D73BC3)

## 设置旋转动画

设置不同的原点位置（transform-origin）改变元素所围绕的旋转中心。rotate3d属性前三个参数值分别为X轴、Y轴、Z轴的旋转向量，第四个值为旋转角度，旋转角度可为负值，负值则代表旋转方向为逆时针方向。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="rotate">
4. <div class="rect rect1"></div>
5. <div class="rect rect2"></div>
6. <div class="rect rect3"></div>
7. </div>
8. <!-- 3d属性 -->
9. <div class="rotate3d">
10. <div class="content">
11. <div class="rect4"></div>
12. <div class="rect5"> </div>
13. </div>
14. <div class="mouse"></div>
15. </div>
16. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. background-color:#F1F3F5;
5. display: flex;
6. align-items: center;
7. justify-content: center;
8. width: 100%;
9. height: 100%;
10. }
11. .rect {
12. width: 100px;
13. height: 100px;
14. animation: rotate 3s infinite;
15. margin-left: 30px;
16. }
17. .rect1 {
18. background-color: #f76160;
19. }
20. .rect2 {
21. background-color: #60f76f;
22. /* 改变原点位置*/
23. transform-origin: 10% 10px;
24. }
25. .rect3 {
26. background-color: #6081f7;
27. /*  改变原点位置*/
28. transform-origin: right bottom;
29. }
30. @keyframes rotate {
31. from {
32. transform: rotate(0deg)
33. }
34. to {
35. transform: rotate(360deg);
36. }
37. }
38. /* 3d示例样式 */
39. .rotate3d {
40. margin-top: 150px;
41. flex-direction: column;
42. background-color:#F1F3F5;
43. display: flex;
44. align-items: center;
45. width: 80%;
46. height: 600px;
47. border-radius: 300px;
48. border: 1px solid #ec0808;
49. }
50. .content {
51. padding-top: 150px;
52. display: flex;
53. align-items: center;
54. justify-content: center;
55. }
56. /* rect4 rect5 翻转形成眼睛 */
57. .rect4 {
58. width: 100px;
59. height: 100px;
60. animation: rotate3d1 1000ms infinite;
61. background-color: darkmagenta;
62. }
63. .rect5 {
64. width: 100px;
65. height: 100px;
66. animation: rotate3d1 1000ms infinite;
67. margin-left: 100px;
68. background-color: darkmagenta;
69. }
70. .mouse {
71. margin-top: 150px;
72. width: 200px;
73. height: 100px;
74. border-radius: 50px;
75. border: 1px solid #e70303;
76. animation: rotate3d2 1000ms infinite;
77. }
78. /* 眼睛的动效 */
79. @keyframes rotate3d1 {
80. 0% {
81. transform:rotate3d(0,0,0,0deg)
82. }
83. 50% {
84. transform:rotate3d(20,20,20,360deg);
85. }
86. 100% {
87. transform:rotate3d(0,0,0,0deg);
88. }
89. }
90. /* 嘴的动效 */
91. @keyframes rotate3d2 {
92. 0% {
93. transform:rotate3d(0,0,0,0deg)
94. }
95. 33% {
96. transform:rotate3d(0,0,10,30deg);
97. }
98. 66% {
99. transform:rotate3d(0,0,10,-30deg);
100. }
101. 100% {
102. transform:rotate3d(0,0,0,0deg);
103. }
104. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/ovQwiRn1QPOIregEkUR2ig/zh-cn_image_0000002583438189.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234032Z&HW-CC-Expire=86400&HW-CC-Sign=84C845D8637DE3332F2956D16786E23E35E730625F4BA63D2EB47A963B9BF857)

说明

transform-origin变换对象的原点位置，如果仅设置一个值，另一个值为50%，若设置两个值第一个值表示X轴的位置，第二个值表示Y轴的位置。

## 设置缩放动画

设置scale样式属性实现涟漪动画，先使用定位确定元素的位置，确定坐标后创建多个组件实现重合效果，再设置opacity属性改变组件不透明度实现组件隐藏与显示，同时设置scale值使组件可以一边放大一边隐藏，最后设置两个组件不同的动画执行时间，实现扩散的效果。

设置scale3d中X轴、Y轴、Z轴的缩放参数实现动画。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="circle">
4. <text>ripple</text>
5. </div>
6. <div class="ripple"></div>
7. <div class="ripple ripple2"></div>
8. <!-- 3d -->
9. <div class="content">
10. <text>spring</text>
11. </div>
12. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. background-color:#F1F3F5;
5. width: 100%;
6. position: relative;
7. }
8. .circle{
9. margin-top: 400px;
10. margin-left: 40%;
11. width: 100px;
12. height: 100px;
13. border-radius: 50px;
14. background-color: mediumpurple;
15. z-index: 1;  position: absolute;
16. }
17. .ripple{
18. margin-top: 400px;
19. margin-left: 40%;
20. position: absolute; z-index: 0;
21. width: 100px;
22. height: 100px;
23. border-radius: 50px;
24. background-color: blueviolet;
25. animation: ripple 5s infinite;
26. }
27. /* 设置不同的动画时间 */
28. .ripple2{
29. animation-duration: 2.5s;
30. }
31. @keyframes ripple{
32. 0%{
33. transform: scale(1);
34. opacity: 0.5;
35. }
36. 50%{
37. transform: scale(3);
38. opacity: 0;
39. }
40. 100%{
41. transform: scale(1);
42. opacity: 0.5;
43. }
44. }
45. text{
46. color: white;
47. text-align: center;
48. height: 100%;
49. width: 100%;
50. }
51. .content {
52. margin-top: 700px;
53. margin-left: 33%;
54. width: 200px;
55. height: 100px;
56. animation:rubberBand 1s infinite;
57. background-color: darkmagenta;
58. position: absolute;
59. }
60. @keyframes rubberBand {
61. 0% {
62. transform: scale3d(1, 1, 1);
63. }
64. 30% {
65. transform: scale3d(1.25, 0.75, 1.1);
66. }
67. 40% {
68. transform: scale3d(0.75, 1.25, 1.2);
69. }
70. 50% {
71. transform: scale3d(1.15, 0.85, 1.3);
72. }
73. 65% {
74. transform: scale3d(.95, 1.05, 1.2);
75. }
76. 75% {
77. transform: scale3d(1.05, .95, 1.1);
78. }
79. 100%{
80. transform: scale3d(1, 1, 1);
81. }
82. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/3dwOjRbyREqMEgZUpAlQ-w/zh-cn_image_0000002552958144.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234032Z&HW-CC-Expire=86400&HW-CC-Sign=C833D4F5E48836A9B729C0235D5888B7AAE116FDAD7AA8E803A961CFE52026AF)

说明

设置transform属性值后，子元素会跟着父元素一起改变，若只改变父元素其他属性值时（如：height，width），子元素不会改变。

## 设置matrix属性

matrix是一个参数为六个值的矩阵，6个值分别代表：scaleX, skewY, skewX, scaleY, translateX, translateY。下面示例中设置了matrix属性为matrix(1,0,0,1,0,200)使组件移动和倾斜。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="rect"> </div>
4. </div>
```

```
1. /* xxx.css */
2. .container{
3. background-color:#F1F3F5;
4. display: flex;
5. justify-content: center;
6. width: 100%;
7. height: 100%;
8. }
9. .rect{
10. width: 100px;
11. height: 100px;
12. background-color: red;
13. animation: down 3s infinite forwards;
14. }
15. @keyframes down{
16. 0%{
17. transform: matrix(1,0,0,1,0,0);
18. }
19. 10%{
20. transform: matrix(1,0,0,1,0,200);
21. }
22. 60%{
23. transform: matrix(2,1.5,1.5,2,0,700);
24. }
25. 100%{
26. transform: matrix(1,0,0,1,0,0);
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/E9R2OxReT5uFYLU08WrOEA/zh-cn_image_0000002583478145.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234032Z&HW-CC-Expire=86400&HW-CC-Sign=084B08CB5F6CD68589F8A190F2D4640C6FAF87D9BA6B8BF8D87ED69C92208834)

## 整合transform属性

transform可以设置多个值并且多个值可同时设置，下面案例中展示同时设置缩放（scale），平移（translate），旋转（rotate）属性时的动画效果。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="rect1"></div>
4. <div class="rect2"></div>
5. <div class="rect3"></div>
6. <div class="rect4"></div>
7. <div class="rect5"></div>
8. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction:column;
6. background-color:#F1F3F5;
7. padding:50px;
8. }
9. .rect1{
10. width: 100px;
11. height: 100px;
12. background-color: red;
13. animation: change1 3s infinite forwards;
14. }
15. .rect2{
16. margin-top: 50px;
17. width: 100px;
18. height: 100px;
19. background-color: darkblue;
20. animation: change2 3s infinite forwards;
21. }
22. .rect3{
23. margin-top: 50px;
24. width: 100px;
25. height: 100px;
26. background-color: darkblue;
27. animation: change3 3s infinite;
28. }
29. .rect4{
30. align-self: center;
31. margin-left: 50px;
32. margin-top: 200px;
33. width: 100px;
34. height: 100px;
35. background-color: darkmagenta;
36. animation: change4 3s infinite;
37. }
38. .rect5{
39. margin-top: 300px;
40. width: 100px;
41. height: 100px;
42. background-color: cadetblue;
43. animation: change5 3s infinite;
44. }
45. /* change1 change2 对比 */
46. @keyframes change1{
47. 0%{
48. transform: translate(0,0);    transform: rotate(0deg)
49. }
50. 100%{
51. transform: translate(0,500px);
52. transform: rotate(360deg)
53. }
54. }
55. /* change2 change3 对比属性顺序不同的动画效果 */
56. @keyframes change2{
57. 0%{
58. transform:translate(0,0) rotate(0deg) ;
59. }
60. 100%{
61. transform: translate(300px,0) rotate(360deg);
62. }
63. }
64. @keyframes change3{
65. 0%{
66. transform:rotate(0deg) translate(0,0);
67. }
68. 100%{
69. transform:rotate(360deg)  translate(300px,0);
70. }
71. }
72. /* 属性值不对应的情况 */
73. @keyframes change4{
74. 0%{
75. transform: scale(0.5);
76. }
77. 100%{
78. transform:scale(2) rotate(45deg);
79. }
80. }
81. /* 多属性的写法 */
82. @keyframes change5{
83. 0%{
84. transform:scale(0) translate(0,0) rotate(0);
85. }
86. 100%{
87. transform: scale(1.5) rotate(360deg) translate(200px,0);
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/G2FrudvfRt-4mvCU-qmjTA/zh-cn_image_0000002552798496.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234032Z&HW-CC-Expire=86400&HW-CC-Sign=5428878AE0CEC68E727D7EEE3E3E53580CFFE0C0E5F354FB4DF74D8C7216B819)

说明

* 当设置多个transform时，后续的transform值会把前面的覆盖掉。若想同时使用多个动画样式可用复合写法，例：transform: scale(1) rotate(0) translate(0,0)。
* transform进行复合写法时，变化样式内多个样式值顺序的不同会呈现不一样的动画效果。
* transform属性设置的样式值要一一对应，若前后不对应，则该动画不生效。若设置多个样式值则只会呈现出已对应值的动画效果。
