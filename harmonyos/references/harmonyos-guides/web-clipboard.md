---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-clipboard
title: 使用Web组件与系统剪贴板交互处理网页内容
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > 使用Web组件与系统剪贴板交互处理网页内容
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a609306848c901f1f28aecf04cf7734ed0a9d29047ffec9c7d85331f162f923
---

开发者能够通过Web组件和系统剪贴板进行交互，实现各种类型数据的复制和粘贴。支持通过[菜单](web-menu.md)、键盘快捷键以及[W3C剪贴板接口](https://www.w3.org/TR/clipboard-apis/)对网页内容执行剪切、复制和粘贴操作。

## 通过菜单或键盘快捷键与系统剪贴板交互

开发者能够自定义菜单中的功能选项，当用户选择特定选项时，开发者可以通过调用[cut](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#cut9)、[copy](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#copy9)、[copyImage](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#copyimage9)、[paste](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#paste9)、[pasteAndMatchStyle](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#pasteandmatchstyle20)等接口，将网页中的文本、HTML或图片数据复制到系统剪贴板，或从系统剪贴板粘贴到网页的可输入区域。

菜单功能接口的使用可参考[使用Web组件菜单处理网页内容](web-menu.md)。

当设备有物理键盘时，用户也能够通过键盘快捷键：CTRL + X（剪切）、CTRL + C（复制）、CTRL + V（粘贴），与剪贴板进行交互。

说明

通过[paste](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#paste9)、[pasteAndMatchStyle](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md#pasteandmatchstyle20)接口读取系统剪贴板数据，需[申请访问剪贴板权限](get-pastedata-permission-guidelines.md)：ohos.permission.READ\_PASTEBOARD。

## 通过W3C异步剪贴板接口与系统剪贴板交互

[异步剪贴板接口（Async Clipboard API）](https://www.w3.org/TR/clipboard-apis/#async-clipboard-api)提供给网页开发者读写系统剪贴板的方法，这让Web应用程序可以实现剪切、复制和粘贴的功能。

* writeText：将文本内容写入系统剪贴板。

```
1. // 写入文本到剪贴板
2. await navigator.clipboard.writeText("文本内容");
```

* write：将任意类型内容写入系统剪贴板。

```
1. // 写入 HTML到剪贴板
2. const clipboardItem = new ClipboardItem({
3. 'text/html': new Blob(["HTML内容"], { type: 'text/html' })
4. });
5. await navigator.clipboard.write([clipboardItem]);
```

* readText：从系统剪贴板读取文本内容。

```
1. // 从剪贴板读取文本
2. const text = await navigator.clipboard.readText()
```

* read()：从系统剪贴板读取任意类型内容。

```
1. // 从剪贴板读取 HTML
2. const clipboardItems = await navigator.clipboard.read();
3. const htmlBlob = await clipboardItems[0].getType('text/html');
```

说明

通过异步剪贴板接口read()和readText()方法读取系统剪贴板数据，需[申请访问剪贴板权限](get-pastedata-permission-guidelines.md)：ohos.permission.READ\_PASTEBOARD。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: $rawfile('clipboard.html'), controller: this.controller })
11. }
12. }
13. }
```

[WebClipboard.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebClipboard/entry/src/main/ets/pages/WebClipboard.ets#L16-L30)

加载的html：

```
1. <!--clipboard.html-->
2. <!DOCTYPE html>
3. <html lang="zh">
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. <title>Clipboard API demo</title>
8. <style>
9. #output {
10. margin-top: 20px;
11. border: 1px solid #ccc;
12. padding: 10px;
13. min-height: 50px;
14. }
15. .button-group {
16. margin-bottom: 10px;
17. }
18. </style>
19. </head>
20. <body>
21. <h1>Clipboard API demo</h1>
22. <div class="button-group">
23. <button id="copyTextButton">复制文本</button>
24. <button id="copyHtmlButton">复制HTML</button>
25. </div>

27. <div class="button-group">
28. <button id="pasteTextButton">粘贴文本</button>
29. <button id="pasteHtmlButton">粘贴HTML</button>
30. <button id="clearOutputButton">清空输入框</button>
31. </div>

33. <div id="result"></div>
34. <div id="output" contenteditable="true"></div>

36. <script>
37. const textContent = "这是一些文本内容";
38. const htmlContent = `<strong><em>这是一些 HTML 内容</em></strong>`;

40. // writeText()接口
41. async function copyText() {
42. await navigator.clipboard.writeText(textContent);
43. document.getElementById('result').innerText = "文本已复制到剪贴板！";
44. }

46. // write()接口
47. async function copyHtml() {
48. const clipboardItem = new ClipboardItem({
49. 'text/html': new Blob([htmlContent], { type: 'text/html' })
50. });
51. await navigator.clipboard.write([clipboardItem]);
52. document.getElementById('result').innerText = "HTML 已复制到剪贴板！";
53. }

55. // readText()接口
56. async function pasteText() {
57. const text = await navigator.clipboard.readText();
58. document.getElementById('output').innerText = text;
59. }

61. // read()接口
62. async function pasteHtml() {
63. const items = await navigator.clipboard.read();
64. for (const item of items) {
65. const types = item.types;
66. if (types.includes('text/html')) {
67. const blob = await item.getType('text/html');
68. const html = await blob.text();
69. document.getElementById('output').innerHTML = html;
70. return;
71. }
72. }
73. document.getElementById('result').innerText = "剪贴板中没有 HTML 内容。";
74. }

76. function clearOutput() {
77. document.getElementById('result').innerText = " ";
78. document.getElementById('output').innerHTML = '';
79. }

81. // 事件监听
82. document.getElementById('copyTextButton').addEventListener('click', copyText);
83. document.getElementById('copyHtmlButton').addEventListener('click', copyHtml);
84. document.getElementById('pasteTextButton').addEventListener('click', pasteText);
85. document.getElementById('pasteHtmlButton').addEventListener('click', pasteHtml);
86. document.getElementById('clearOutputButton').addEventListener('click', clearOutput);
87. </script>
88. </body>
89. </html>
```

module.json5权限配置：

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](get-pastedata-permission-guidelines.md)。

```
1. {
2. "module": {
3. // ···
4. "requestPermissions": [
5. {
6. "name" : "ohos.permission.READ_PASTEBOARD",
7. "reason": "$string:module_desc",
8. "usedScene": {
9. "abilities": [
10. "FormAbility"
11. ],
12. "when":"inuse"
13. }
14. }
15. ]
16. }
17. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebClipboard/entry/src/main/module.json5#L16-L81)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/HC2zNj1QQki6zDNzP9Dntg/zh-cn_image_0000002558605076.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=693C3FB18075D962EE62C33A0D186C104D367AF75628A7813FF8AC30FCF2E967)

## 通过W3C剪贴板事件接口与系统剪贴板交互

[剪贴板事件（Clipboard Event）](https://www.w3.org/TR/clipboard-apis/#clipboard-events-and-interfaces)描述了与剪贴板相关的cut、copy和paste事件。当用户执行剪切、复制或粘贴操作时，相应的事件将被触发。开发者可以通过监听这些事件，对系统剪贴板进行读写操作，或拦截默认行为，以更改复制或粘贴的结果。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: $rawfile('clipboard_event.html'), controller: this.controller })
11. }
12. }
13. }
```

[WebClipboardEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebClipboard/entry/src/main/ets/pages/WebClipboardEvent.ets#L16-L30)

加载的html：

```
1. <!--clipboard_event.html-->
2. <!DOCTYPE html>
3. <html lang="zh">
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. <title>Clipboard Event demo</title>
8. <style>
9. .output {
10. margin-top: 20px;
11. border: 1px solid #ccc;
12. padding: 10px;
13. max-width: 400px;
14. }
15. </style>
16. </head>
17. <body>
18. <h2>Clipboard Event监听示例</h2>
19. <textarea id="inputArea" rows="4" cols="50" placeholder="在这里输入文本，尝试复制和粘贴..."></textarea>

21. <div class="output" id="output">
22. <h3>输出内容:</h3>
23. <p id="resultText">没有复制或粘贴内容。</p>
24. </div>

26. <script>
27. const inputArea = document.getElementById('inputArea');
28. const resultText = document.getElementById('resultText');

30. // 监听复制事件
31. inputArea.addEventListener('copy', (event) => {
32. const selection = document.getSelection();
33. const copiedText = selection.toString() + "(复制自ArkWeb)"
34. event.clipboardData.setData("text/plain", copiedText);
35. event.preventDefault();
36. resultText.textContent = `复制的内容: "${copiedText}"`;
37. });

39. // 监听粘贴事件
40. inputArea.addEventListener('paste', (event) => {
41. const pastedData = event.clipboardData.getData('text');
42. resultText.textContent = `粘贴的内容: "${pastedData}"`;
43. });

45. // 监听剪切事件
46. inputArea.addEventListener('cut', (event) => {
47. const selection = document.getSelection();
48. const cutText = selection.toString() + "(剪切自ArkWeb)"
49. event.clipboardData.setData("text/plain", cutText);
50. selection.deleteFromDocument();
51. event.preventDefault();
52. resultText.textContent = `剪切的内容: "${cutText}"`;
53. });
54. </script>
55. </body>
56. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/dFDx93dLT-a5aGa3f1W05A/zh-cn_image_0000002589324601.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=212DCE8CC60715BE194A96597688F250FC48A317A3EA5C7A947E52B687071001)

## 设置剪贴板复制范围选项

开发者可以通过设置Web组件的[copyOptions](../harmonyos-references/arkts-basic-components-web-attributes.md#copyoptions11)属性，来指定Web组件上剪贴板复制的范围。可以指定的选项有：CopyOptions.None（不支持复制）、CopyOptions.InApp（支持应用内复制）以及CopyOptions.LocalDevice（支持设备内复制）。默认值为：CopyOptions.LocalDevice，即默认支持设备内部的复制。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();
7. @State copyOption: CopyOptions = CopyOptions.LocalDevice;

9. build() {
10. Column() {
11. Web({ src: $rawfile('copyOptions.html'), controller: this.controller })
12. .copyOptions(this.copyOption)
13. }
14. }
15. }
```

[WebCopyOptions.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebClipboard/entry/src/main/ets/pages/WebCopyOptions.ets#L16-L32)

加载的html：

```
1. <!--copyOptions.html-->
2. <!DOCTYPE html>
3. <html lang="zh">
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. <title>Clipboard CopyOption demo</title>
8. </head>
9. <body>
10. <h2>Clipboard CopyOption示例</h2>
11. <textarea id="inputArea"></textarea>
12. </body>
13. </html>
```
