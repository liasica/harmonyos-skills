---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-slider
title: slider开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > slider开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f3493d953412e567b534a2b8295977bce99de1ef1a82484c09444436026c9681
---

slider为滑动条组件，用来快速调节音量、亮度等。具体用法请参考[slider](../harmonyos-references/js-components-basic-slider.md)。

## 创建slider组件

在pages/index目录下的hml文件中创建一个slider组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <slider></slider>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. background-color: #F1F3F5;
6. flex-direction: column;
7. justify-content: center;
8. align-items: center;
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/a6f2-uMIS1mew3J61UlpXQ/zh-cn_image_0000002589244413.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=88D7CCD6B10FCAE7F98C2C9F751990790FC8444D2003C96E4B42BFAFD3623B03)

## 设置样式和属性

slider组件通过color、selected-color、block-color样式分别为滑动条设置背景颜色、已选择颜色和滑块颜色。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <slider class= "sli"></slider>
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
10. .sli{
11. color: #fcfcfc;
12. scrollbar-color: aqua;
13. background-color: #b7e3f3;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/6Gko_oQuTRSoPd-hDGK7CA/zh-cn_image_0000002558764606.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=BB5F0C9A7FF04036AD9EE2DED3D18B4E5E9CF5538F307F0C1C773CD1E7BF1EC2)

通过添加min、max、value、step、mode属性分别为滑动条设置最小值、最大值、初始值、滑动步长和滑动条样式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <slider min="0" max="100" value="1" step="2" mode="inset" showtips="true"></slider>
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
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/NMIIpo2oRg-LG3qCXNOqMQ/zh-cn_image_0000002558604950.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=0565455B5B2F319A2C0DB185493697810D4FAF229F956795C574D58C324F8308)

说明

mode属性为滑动条样式，可选值为：

* outset：滑块在滑杆上。
* inset：滑块在滑杆内。

## 绑定事件

向slider组件添加change事件，添加时需要传入ChangeEvent参数。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text>slider start value is {{startValue}}</text>
4. <text>slider current value is {{currentValue}}</text>
5. <text>slider end value is {{endValue}}</text>
6. <slider min="0" max="100" value="{{value}}" onchange="setValue"></slider>
7. </div>
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
```

```
1. // xxx.js
2. export default {
3. data: {
4. value: 0,
5. startValue: 0,
6. currentValue: 0,
7. endValue: 0,
8. },
9. setValue(e) {
10. if (e.mode === "start") {
11. this.value = e.value;
12. this.startValue = e.value;
13. } else if (e.mode === "move") {
14. this.value = e.value;
15. this.currentValue = e.value;
16. } else if (e.mode === "end") {
17. this.value = e.value;
18. this.endValue = e.value;
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/XgbWUHFDT9GJOIgWNQeIvw/zh-cn_image_0000002589324477.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=1FEACBDDD78EEDCC6E47EAECC948A2DDA64B868235705F7BEDFD6EE96E9CBF82)

## 场景示例

开发者可以通过调整滑动条的值来改变图片大小，并且动态打印当前图片的宽和高。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <image src="common/landscape3.jpg" style=" width: {{WidthVal}}px;height:{{HeightVal}}px;margin-top: -150px;"></image>
4. <div class="txt">
5. <slider min="0" max="100" value="{{value}}" onchange="setValue"></slider>
6. <text>The width of this picture is {{WidthVal}}</text>
7. <text>The height of this picture is {{HeightVal}}</text>
8. </div>
9. </div>
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
10. .text{
11. flex-direction: column;
12. justify-content: center;
13. align-items: center;
14. position: fixed;
15. top: 65%;
16. }
17. .text{
18. margin-top: 30px;
19. }
```

```
1. // xxx.js
2. export default{
3. data: {
4. value: 0,
5. WidthVal: 200,
6. HeightVal: 200
7. },
8. setValue(e) {
9. this.WidthVal = 200 + e.value;
10. this.HeightVal = 200 + e.value
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/1wTpB9IJQIq-tzGzSrbbbQ/zh-cn_image_0000002589244415.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=048EAC978B5F8A4710B71BA2BF2B99CDF6F46319ADF796D02E424B1AE08F8EC7)
