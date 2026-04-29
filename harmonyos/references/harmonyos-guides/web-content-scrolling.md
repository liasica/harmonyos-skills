---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-content-scrolling
title: Web页面显示内容滚动
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > Web页面显示内容滚动
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef0d018379c2fcf53f2d37c24ed378db9086b96551dce7c846f96ce955ae6675
---

当Web页面的内容高度或宽度超过可视区域时，页面才能滚动。Web页面滚动有多种方式，包括使用外接设备、ArkTS侧接口调用和JS侧接口调用。

## 使用外接设备控制Web页面滚动

可以使用以下方式，通过触屏、触摸板和鼠标滚轮控制Web页面滚动。

* 通过触屏控制Web页面滚动：支持在触摸屏上单指上下左右滑动可以控制页面滚动。
* 通过触摸板控制Web页面滚动：支持在笔记本触摸板或者外接触摸板双指上下左右滑动，可以控制页面滚动。
* 通过鼠标滚轮控制Web页面滚动：支持用鼠标滚轮上下滑动来控制页面滚动。

## 调用ArkTS侧接口控制Web页面滚动

* [scrollTo](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#scrollto)：在指定时间内，将页面滚动到指定的绝对位置。

  返回页面顶部。

  ```
  1. this.webController.scrollTo(0, 0);
  ```

  [WebScrollDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebScrollDemo/entry/src/main/ets/pages/WebScrollDemo.ets#L76-L78)
* [scrollBy](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#scrollby)：在指定时间内将页面滚动指定的偏移量。

  可以作为Web组件嵌套滚动中，控制Web组件滚动的接口，详见[滚动偏移量由滚动父组件统一派发](web-nested-scrolling.md#滚动偏移量由滚动父组件统一派发)。
* [pageUp](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#pageup)：将Web组件的内容向上滚动半个视口大小或者滚动到页面最顶部，通过top入参控制。
* [pageDown](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#pagedown)：将Web组件的内容向下滚动半个视口大小或者滚动到页面最底部，通过bottom入参控制。

## 调用JS侧接口控制Web页面滚动

* scrollBy：相对当前滚动位置滚动一定距离（正数向下/右，负数向上/左）。

  ```
  1. window.scrollBy(deltaX, deltaY);// deltaX是元素要在横轴上滚动的距离，deltaY是元素要在纵轴上滚动的距离。
  ```

  渐进式滚动（如“阅读更多”按钮）。

  ```
  1. document.getElementById("read-more").addEventListener("click", ()=>{
  2. window.scrollBy(0, 300);
  3. })
  ```
* scrollTo：将页面滚动到绝对坐标位置。

  ```
  1. window.scrollTo(x, y);// X是你想要显示在左上角的元素沿水平轴的像素，Y是你想要显示在左上角的元素沿垂直轴的像素。
  ```

  (1) 返回页面顶部。

  ```
  1. window.scrollTo(0, 0);
  ```

  (2) 跳转到页面特定位置。

  ```
  1. window.scrollTo(0, 500); // 滚动到某个固定像素位置（如：500px）
  ```

## 点击状态栏回顶

当Web页面处于非顶部状态或向下抛滑时，此时若需返回Web页面顶部，可以使用[backToTop](../harmonyos-references/arkts-basic-components-web-attributes.md#backtotop22)方法，开启后通过点击状态栏，打断抛滑并将Web页面滚动到页面顶部。

* 示例代码：

  ```
  1. // xxx.ets
  2. import { webview } from '@kit.ArkWeb';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Web({ src: $rawfile("index.html"), controller: this.controller })
  12. .backToTop(true)
  13. }
  14. }
  15. }
  ```

  加载的HTML文件：

  ```
  1. <!-- index.html -->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
  6. <style>
  7. .blue {
  8. background-color: lightblue;
  9. }
  10. .green {
  11. background-color: lightgreen;
  12. }
  13. .blue, .green {
  14. font-size:16px;
  15. height:200px;
  16. text-align: center;       /* 水平居中 */
  17. line-height: 200px;       /* 垂直居中（值等于容器高度） */
  18. }
  19. </style>
  20. </head>
  21. <body>
  22. <div class="blue" >webArea</div>
  23. <div class="green">webArea</div>
  24. <div class="blue">webArea</div>
  25. <div class="green">webArea</div>
  26. <div class="blue">webArea</div>
  27. <div class="green">webArea</div>
  28. <div class="blue">webArea</div>
  29. <div class="green">webArea</div>
  30. <div class="blue">webArea</div>
  31. </body>
  32. </html>
  ```
* 效果展示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/00qQG4goQ7KgcSwrHOyPdg/zh-cn_image_0000002558605052.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052918Z&HW-CC-Expire=86400&HW-CC-Sign=1ED73BB1BD3CA1681D862608005156FA53D2F471DCC35F4F50EF03ADB8DA9A11)
