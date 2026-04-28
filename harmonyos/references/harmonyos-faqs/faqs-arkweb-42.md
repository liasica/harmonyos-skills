---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-42
title: Web加载的H5页面跳转后，如何避免原有页面注册的资源被清空
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web加载的H5页面跳转后，如何避免原有页面注册的资源被清空
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ca6896dc16c3955550ea3e070590e4d1fdc814f6c4e0a82b83750652755b8007
---

使用[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)加载JS，是运行时注入，页面跳转后失效，可能会出现跳转后注册资源被清空的情况，使用[javaScriptOnDocumentStart](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptondocumentstart11)注入JS是文档初始化时注入，适用于页面跳转场景，就不会出现H5跳转注册资源被清空的情况。

使用runJavaScript复现问题代码参考：

ArkTS页面：

两个Button使用runJavaScript注册并调用test()方法和bodyOnLoadLocalStorage()，两个方法分别实现了为sessionStorage设置值和根据sessionStorage刷新H5页面。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column({ space: 20 }) {
10. Button('调用注册资源')
11. .onClick(e => {
12. try {
13. this.controller.runJavaScript(
14. 'test()',
15. (error, result) => {
16. if (error) {
17. console.error(`run JavaScript error, ErrorCode: ${error.code},  Message: ${error.message}`);
18. return;
19. }
20. if (result) {
21. console.info(`The test() return value is: ${result}`);
22. }
23. });
24. } catch (error) {
25. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
26. }
27. })
28. Button('调用注册资源')
29. .onClick(e => {
30. try {
31. this.controller.runJavaScript(
32. 'bodyOnLoadLocalStorage()',
33. (error, result) => {
34. if (error) {
35. console.error(`run JavaScript error, ErrorCode: ${error.code},  Message: ${error.message}`);
36. return;
37. }
38. if (result) {
39. console.info(`The bodyOnLoadLocalStorage() return value is: ${result}`);
40. }
41. });
42. } catch (error) {
43. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
44. }
45. })
46. Web({ src: $rawfile('index.html'), controller: this.controller })
47. .javaScriptAccess(true)
48. .domStorageAccess(true)
49. .backgroundColor(Color.Grey)
50. .width('100%')
51. .height('100%')
52. }
53. }
54. }
```

[RunJavaScript1.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/RunJavaScript1.ets#L21-L74)

H5侧：

页面一：

index.html声明了test方法和bodyOnLoadLocalStorage方法。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
8. 页面一：Hello world!
9. <div id="result"></div>
10. <a href="Second.html">点击跳转</a>
11. </body>
12. <script type="text/javascript">
13. function bodyOnLoadLocalStorage() {
14. if (typeof(Storage) !== 'undefined') {
15. document.getElementById('result').innerHTML = sessionStorage.getItem('color');
16. } else {
17. document.getElementById('result').innerHTML = 'Your browser does not support sessionStorage.';
18. }
19. }
20. function test(){
21. if (typeof(Storage) !== 'undefined') {
22. sessionStorage.setItem('color', 'Red');
23. }
24. }
25. </script>
26. </html>
```

[RunJs\_one.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/RunJs_one.html#L21-L46)

页面二：

页面二未声明上述两个方法，利用之前的注册调用后，跳转至页面二时无法正确调用，注册资源清空的问题复现。

```
1. <!-- Second.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;">
8. 页面二：Hello world!
9. <div id="result"></div>
10. </body>
11. <script type="text/javascript">

13. </script>
14. </html>
```

[RunJs\_two.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/RunJs_two.html#L21-L34)

使用javaScriptOnDocumentStart解决问题代码参考：

ArkUI侧

使用javaScriptOnDocumentStart执行test方法。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. controller: webview.WebviewController = new webview.WebviewController();
7. private localStorage: string =
8. "if (typeof(Storage) !== 'undefined') {" +
9. "   sessionStorage.setItem('color', 'Red');" +
10. "}";
11. @State scripts: Array<ScriptItem> = [
12. { script: this.localStorage, scriptRules: ["*"] }
13. ];

15. build() {
16. Column({ space: 20 }) {
17. Web({ src: $rawfile('index.html'), controller: this.controller })
18. .javaScriptAccess(true)
19. .domStorageAccess(true)
20. .backgroundColor(Color.Grey)
21. .javaScriptOnDocumentStart(this.scripts)
22. .width('100%')
23. .height('100%')
24. }
25. }
26. }
```

[RunJavaScript4.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/RunJavaScript4.ets#L21-L46)

H5侧：

页面一：

页面调用bodyOnLoadLocalStorage刷新H5页面。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
8. 页面一：Hello world!
9. <div id="result"></div>
10. <a href="Second.html">点击跳转</a>
11. </body>
12. <script type="text/javascript">
13. function bodyOnLoadLocalStorage() {
14. if (typeof(Storage) !== 'undefined') {
15. document.getElementById('result').innerHTML = sessionStorage.getItem('color');
16. } else {
17. document.getElementById('result').innerHTML = 'Your browser does not support sessionStorage.';
18. }
19. }
20. </script>
21. </html>
```

[RunJs\_3.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/RunJs_3.html#L21-L41)

页面二：

点击跳转后，test方法会调用并生效。

```
1. <!-- Second.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
8. 页面二：Hello world!
9. <div id="result"></div>
10. </body>
11. <script type="text/javascript">
12. function bodyOnLoadLocalStorage() {
13. if (typeof(Storage) !== 'undefined') {
14. document.getElementById('result').innerHTML = sessionStorage.getItem('color');
15. } else {
16. document.getElementById('result').innerHTML = 'Your browser does not support sessionStorage.';
17. }
18. }
19. </script>
20. </html>
```

[RunJs\_4.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/RunJs_4.html#L21-L40)
