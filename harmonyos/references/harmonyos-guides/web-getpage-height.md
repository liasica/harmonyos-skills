---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-getpage-height
title: 获取网页内容高度
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > Web渲染和布局 > 获取网页内容高度
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c28577dfc339bbaa4bd558572ccf417cd11b5510fa60f759230df509a889f975
---

通过调用[getPageHeight](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getpageheight)可获取当前网页内容的实际高度，开发者可以根据具体需求选择合适的方法。

## 使用场景

在网页加载过程中，获取的高度可能不够精确，特别是在网页还未渲染完成时。因为动态内容加载后会更新这个值。网页内容可能需要长时间加载。目前网站为优化首次加载速度，会使用动态网页加载技术，用户在看到网页首帧时，页面资源还在动态加载页面，特别是包含图片、动态内容的页面。

非静态网页不建议在[onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)、[onPageVisible](../harmonyos-references/arkts-basic-components-web-events.md#onpagevisible9)、[onFirstContentfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onfirstcontentfulpaint10)、[onFirstMeaningfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onfirstmeaningfulpaint12)事件等Web组件生命周期回调和Web性能指标回调中获取。需要根据当前网页的特点，通过JSBridge或延迟等方案，在前端特定的回调通知里获取当前网页内容的实际高度。

## 普通静态展示页面

普通静态网页，可以在onPageEnd等Web组件生命周期回调和Web性能指标回调中通过getPageHeight获取网页内容的高度。

应用侧代码

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Row() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .onPageEnd(() => {
14. console.info("page height: onPageEnd: " + this.controller.getPageHeight());
15. })
16. }
17. .width('100%')
18. .height('100%')
19. }
20. .height('100%')
21. }
22. }
```

## 复杂动态网页使用JSBridge传递特定回调

动态网页可以通过JSBridge传递特定回调，通知到应用侧调用。

应用侧代码

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. class TestClass {
5. testController: webview.WebviewController;

7. constructor(controller: webview.WebviewController) {
8. this.testController = controller;
9. }

11. notifyToGet(): void {
12. console.info("page height: " + this.testController.getPageHeight());
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. controller: webview.WebviewController = new webview.WebviewController();
20. @State jsbObj: TestClass = new TestClass(this.controller);

22. build() {
23. Row() {
24. Column() {
25. Web({ src: $rawfile('index.html'), controller: this.controller })
26. .javaScriptAccess(true)
27. .javaScriptProxy({
28. object: this.jsbObj,
29. name: "jsbObj",
30. methodList: ["notifyToGet"],
31. controller: this.controller
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. .height('100%')
38. }
39. }
```

### 加载普通网页

普通网页可以通过load事件，在网页的所有资源都完全加载完成后触发。

前端代码

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html lang="en">
4. <head>
5. <meta charset="UTF-8">
6. <title>Title</title>
7. </head>
8. <body>
9. <script>
10. window.addEventListener("load", function() {
11. if (typeof jsbObj !== 'undefined') {
12. jsbObj.notifyToGet();
13. } else {
14. console.info("jsbObj is undefined");
15. }
16. })
17. </script>
18. </body>
19. </html>
```

### 加载大图片的网页

当网页含有大图片时，可使用图片加载完成回调触发。

在前端代码中，请将示例图片路径替换为实际使用的图片资源。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html lang="en">
4. <head>
5. <meta charset="UTF-8">
6. <title>Title</title>
7. </head>
8. <body>
9. <img src="example.jpg" id="largeImage" alt="Large Image">
10. <script>
11. var img = document.getElementById('largeImage');

13. img.addEventListener('load', function() {
14. if (typeof jsbObj !== 'undefined') {
15. jsbObj.notifyToGet();
16. } else {
17. console.info("jsbObj is error");
18. }
19. });
20. </script>
21. </body>
22. </html>
```

### 加载大量图片的网页

针对图片密集网页，在所有图片加载完成后触发。

在前端代码中，请替换图片为真实图片。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html lang="en">
4. <head>
5. <meta charset="UTF-8">
6. <title>Title</title>
7. </head>
8. <body>
9. <img src="example1.jpg" >
10. <img src="example2.jpg" >
11. <script>
12. function waitForImages() {
13. const images = Array.from(document.images);
14. const promises = images.map(img => {
15. if (img.complete) return Promise.resolve();
16. return new Promise(resolve => {
17. img.onload = img.onerror = resolve;
18. });
19. });

21. return Promise.all(promises).then(() => {
22. if (typeof jsbObj !== 'undefined') {
23. jsbObj.notifyToGet();
24. } else {
25. console.info("jsbObj is error");
26. }
27. })
28. }
29. document.addEventListener("DOMContentLoaded", waitForImages);
30. </script>
31. </body>
32. </html>
```

## 无法使用JSBridge场景

在无法使用JSBridge的场景下，可以通过添加setTimeout等函数来延迟获取当前页面的高度。具体的延迟时间可以根据网页的复杂度来确定。

应用侧代码

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Row() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .onPageEnd(() => {
14. setTimeout(()=>{
15. console.info("page height: onPageEnd: setTimeout: " + this.controller.getPageHeight());
16. },2000)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. .height('100%')
23. }
24. }
```
