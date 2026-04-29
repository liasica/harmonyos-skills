---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-chart
title: chart开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > chart开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:50f9bce163255cbb588acc033b23c36631436ba176437063766c3fd20ad77ddd
---

chart为图表组件，用于呈现线形图、柱状图和量规图界面。具体用法请参考[chart](../harmonyos-references/js-components-basic-chart.md)。

## 创建chart组件

在pages/index目录下的hml文件中创建一个chart组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <chart class="chart-data" type="line" options="{{lineOps}}" datasets="{{lineData}}"></chart>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .chart-data {
11. width: 700px;
12. height: 600px;
13. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. lineData: [
5. {
6. data: [763, 550, 551, 554, 731, 654, 525, 696, 595, 628, 791, 505, 613, 575, 475, 553, 491, 680, 657, 716]
7. }
8. ],
9. lineOps: {
10. xAxis: {
11. min: 0,
12. max: 20,
13. display: false,
14. },
15. yAxis: {
16. min: 0,
17. max: 1000,
18. display: false,
19. },
20. series: {
21. lineStyle: {
22. width: 15,
23. },
24. }
25. },
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/2Cey9l-AQAmVh9aOV5BHpQ/zh-cn_image_0000002558764608.png?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=52BA2E8637488450E7FDA234BFE3B5F0EAEA17C402740FA7CE9C5B30EC56414C)

## 设置图表类型

chart组件通过设置type属性定义图表类型，如将图表设置为柱状图。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="container">
4. <div class="switch-block">
5. <text class="title">
6. {{ title }}
7. </text>
8. </div>
9. <tabs class="tabs" index="0" vertical="false" onchange="changes">
10. <tab-content class="tabcontent" scrollable="true">
11. <tabs >
12. <tab-bar class="tab-bar" mode="fixed"style="margin-bottom: 50px;">
13. <text class="tab-text">线形图</text>
14. <text class="tab-text">柱状图</text>
15. <text class="tab-text">量规图</text>
16. </tab-bar>
17. <tab-content>
18. <div class="bar-block" style="margin-left: 30px;">
19. <chart class="chart-data" type="line" ref="linechart" options="{{ lineOps }}" datasets="{{ lineData }}">
20. </chart>
21. </div>
22. <div class="bar-block">
23. <chart class="data-bar" type="bar" id="bar-chart" options="{{ barOps }}" datasets="{{ barData }}">
24. </chart>
25. </div>
26. <div class="chart-block">
27. <chart type="gauge" ></chart>
28. </div>
29. </tab-content>
30. </tabs>
31. </tab-content>
32. </tabs>
33. </div>
34. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. background-color: #F1F3F5;
8. }
9. .tab-bar{
10. background-color: #F1F3F5;
11. }
12. .chart-data {
13. width: 700px;
14. height: 600px;
15. }
16. .title{
17. margin-left: 50px;
18. margin-top: 50px;
19. font-size: 50px;
20. }
21. .line-block{
22. align-items: center;
23. justify-content: center;
24. }
25. .bar-block{
26. align-items: center;
27. justify-content: center;
28. }
29. .chart-block{
30. width: 90%;
31. margin-left: 30px;
32. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. title: "类型展示",
5. barData: [
6. {
7. fillColor: '#3848e8',
8. data: [763, 550, 551, 554, 731, 654, 525, 696, 595],
9. }
10. ],
11. lineData: [
12. {
13. strokeColor: '#0081ff',
14. fillColor: '#cce5ff',
15. data: [763, 550, 551, 554, 731, 654, 525, 696, 595, 628, 791, 505, 613, 575, 475, 553, 491, 680, 657, 716],
16. gradient: true,
17. }
18. ],
19. lineOps: {
20. xAxis: {
21. min: 0,
22. max: 20,
23. display: false,
24. },
25. yAxis: {
26. min: 0,
27. max: 1000,
28. display: false,
29. },
30. series:{
31. lineStyle: {
32. width: "5px",
33. smooth: true,
34. },
35. headPoint: {
36. shape:"circle",
37. size: 20,
38. strokeWidth: 5,
39. fillColor: '#ffffff',
40. strokeColor: '#007aff',
41. display: true,
42. },
43. loop:{
44. margin: 2,
45. gradient: true
46. }
47. },
48. },
49. barOps: {
50. xAxis: {
51. min: 0,
52. max: 20,
53. display: false,
54. axisTick: 10,
55. },
56. yAxis: {
57. min: 0,
58. max: 1000,
59. },
60. },
61. },
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/nPooaM3NSkS4PougmqHrMg/zh-cn_image_0000002558604952.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=2E98F4E9A860B0A9C6B17E30928B5C1D88D7015F20FF0BAD25517C02035D83C1)

说明

chart不支持显示每个点的值。

## 设置图表属性

chart组件在options属性中设置对x轴、y轴和数据序列参数的设置，在datasets属性里添加对线条颜色、填充颜色、填充渐变颜色和绘制点集的设置。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <chart class="chart-data" type="line" options="{{lineOps}}" datasets="{{lineData}}"></chart>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .chart-data {
11. width: 700px;
12. height: 600px;
13. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. //线形图数据
5. lineData: [
6. {
7. strokeColor: '#0081ff',
8. fillColor: '#cce5ff',  //填充色
9. data: [463, 250, 251, 254, 431, 354, 225, 396, 295, 328, 491, 205, 313, 275, 475, 553, 491, 380, 357, 416],
10. gradient: true,
11. }
12. ],
13. lineOps: {
14. //x轴参数设置
15. xAxis: {
16. min: 0,
17. max: 20,
18. display: false,
19. },
20. //y轴参数设置
21. yAxis: {
22. min: 0,
23. max: 1000,
24. display: false,
25. },
26. //数据序列参数设置
27. series: {
28. //线样式设置
29. lineStyle: {
30. width: "5px",
31. smooth: true,
32. },
33. //线最前端位置白点的样式和大小
34. headPoint: {
35. shape: "circle",
36. size: 20,
37. strokeWidth: 5,
38. fillColor: '#ffffff',
39. strokeColor: '#007aff',
40. display: true,
41. },
42. //设置屏幕显示满时，是否需要重头开始绘制
43. loop: {
44. margin: 2,
45. gradient: true
46. }
47. }
48. },
49. },
50. }
```

说明

* options只支持柱状图和线形图设置参数，量规图不生效。
* datasets只支持柱状图和线形图设置数据集合，量规图不生效。
* series只有线形图支持。

## 场景示例

开发者可以根据开关Switch的状态来选择数据展示的状态，当Switch状态为true时，通过定时器来实现数据的动态展示。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="container">
4. <div class="switch-block">
5. <text class="title">{{ title }} </text>
6. <switch class="switch" showtext="{{ showText }}" allow-scale="{{ allowScale }}"onchange="change">
7. </switch>
8. </div>
9. <tabs class="tabs" index="0" vertical="false" onchange="changes">
10. <tab-content class="tabcontent" scrollable="true">
11. <div>
12. <tabs class="tabs" index="0" vertical="false" onchange="changes">
13. <tab-content class="tabcontent" scrollable="true">
14. <div class="line-class">
15. <div class="bar-block">
16. <chart class="chart-data" type="line" ref="linechart" options="{{ lineOps }}"
17. datasets="{{ lineData }}">
18. </chart>
19. </div>
20. <div class="bar-block">
21. <chart class="data-bar" type="bar" id="bar-chart" options="{{ barOps }}"datasets="{{ barData }}">
22. </chart>
23. </div>
24. </div>
25. </tab-content>
26. </tabs>
27. </div>
28. <div>
29. <div class="container">
30. <list class="todo-wrapper">
31. <list-item for="{{ barData }}" class="todo-item">
32. <text class="todo-title">{{ $item.data }}</text>
33. </list-item>
34. </list>
35. <list class="todo-wrapper">
36. <list-item for="{{ lineData.data }}" class="todo-item">
37. <text class="todo-title">{{ $item.value }}</text>
38. </list-item>
39. </list>
40. </div>
41. </div>
42. </tab-content>
43. </tabs>
44. </div>
45. </div>
```

```
1. /* xxx.css */
2. .container{
3. display:flex;
4. flex-direction:column;
5. background-color: #F1F3F5;
6. }
7. .line-class{
8. display: flex;
9. flex-direction: column;
10. }
11. .title{
12. font-size: 40px;
13. margin-left: 40px;
14. }
15. .switch-block {
16. margin-top: 30px;
17. width: 98%;
18. height: 80px;
19. display: flex;
20. justify-content: space-between;
21. }
22. .switch{
23. font-size: 40px;
24. }
25. .bar-block {
26. margin-top: 80px;
27. margin-left: 40px;
28. position: relative;
29. width: 90%;
30. border-radius: 10px;
31. background-color: #25FAB27B;
32. height: 40%;
33. justify-content: center;
34. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. interval: null,
5. title: "数据展示",
6. allowScale: true,
7. dataLength: 30,
8. barGroup: 3,
9. lineData: null,
10. lineOps: {
11. xAxis: {
12. min: 0,
13. max: 5
14. },
15. yAxis: {
16. min: 0,
17. max: 100
18. },
19. series: {
20. lineStyle: {
21. width: '1px',
22. },
23. headPoint: {
24. shape: 'circle',
25. size: 10,
26. strokeWidth: 2,
27. fillColor: '#ffffff',
28. strokeColor: '#8477DF'
29. },
30. loop: {
31. margin: 2
32. }
33. }
34. },
35. barData: [
36. {
37. fillColor: '#97CF0A2C',
38. data: [20, 20,40, 56]
39. },
40. {
41. fillColor: '#6D0A7ACF',
42. data: [52, 40, 2, 67]
43. },
44. {
45. fillColor: '#6A0ACFA1',
46. data: [56, 2, 77, 40]
47. }
48. ],
49. barOps: {
50. xAxis: {
51. min: 0,
52. max: 20,
53. axisTick: 5
54. },
55. yAxis: {
56. min: 0,
57. max: 100
58. }
59. }
60. },
61. onInit() {
62. this.changeLine();
63. },
64. change(e) {
65. if (e.checked) {
66. this.interval = setInterval(() => {
67. this.changeLine();
68. this.changeBar();
69. }, 1000)
70. } else {
71. clearInterval(this.interval);
72. }
73. },
74. changeLine() {
75. var dataArray = [];
76. for (var i = 0; i < this.dataLength; i++) {
77. var nowValue = Math.floor(Math.random() * 99 + 1);
78. var obj = {
79. "value": nowValue,
80. "description": nowValue + "",
81. "textLocation": "top",
82. "textColor": "#CDCACA",
83. "pointStyle": {
84. "shape": "circle",
85. "size": 5,
86. "fillColor": "#CF0A2C",
87. "strokeColor": "#CF0A2C"
88. }
89. };
90. dataArray.push(obj);
91. }
92. this.lineData = [
93. {
94. strokeColor: '#0081ff',
95. fillColor: '#FF07CDC4',
96. data: dataArray,
97. gradient: true,
98. }
99. ]
100. },
101. changeBar() {
102. for (var i = 0;i < this.barGroup; i++) {
103. var dataArray = this.barData[i].data;
104. for (var j = 0;j < 4; j++) {
105. dataArray[j] = Math.floor(Math.random() * 99 + 1);
106. }
107. }
108. this.barData = this.barData.splice(0, this.barGroup + 1);
109. },
110. changes(e) {
111. console.info("Tab index: " + e.index);
112. },
113. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/0KsVKJfpS_emW0qjqxK8Aw/zh-cn_image_0000002589324479.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=CA8607EB357FF0B8061E40B24EDFEEE581CC7271B6765BDFEA3DE8624CDF443E)
