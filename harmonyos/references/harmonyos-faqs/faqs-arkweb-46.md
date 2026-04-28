---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-46
title: 如何在webview中使用H5中的alert
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何在webview中使用H5中的alert
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:db10ae6e4da79b930b3fccf2a5089da23b4e8c5d8adb3a88c58e4add968e5b3d
---

**参考代码**

使用Web组件的[onAlert](../harmonyos-references/arkts-basic-components-web-events.md#onalert)属性可以监听网页触发alert()告警弹窗事件，之后使用[警告弹窗 (AlertDialog)](../harmonyos-references/ts-methods-alert-dialog-box.md)实现弹窗的效果与逻辑。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebviewAlert {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: $rawfile('WebviewAlert.html'), controller: this.controller })
11. .onAlert((event) => {
12. if (event) {
13. console.log('event.url:' + event.url);
14. console.log('event.message:' + event.message);
15. this.getUIContext().showAlertDialog({
16. title: 'onAlert',
17. message: 'text',
18. primaryButton: {
19. value: 'cancel',
20. action: () => {
21. event.result.handleCancel();
22. }
23. },
24. secondaryButton: {
25. value: 'ok',
26. action: () => {
27. event.result.handleConfirm();
28. }
29. },
30. cancel: () => {
31. event.result.handleCancel();
32. }
33. })
34. }
35. return true;
36. })
37. }
38. }
39. }
```

[UseAlertInWebview.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UseAlertInWebview.ets#L21-L59)

H5侧：

```
1. <!DOCTYPE html>
2. <html>
3. <head>
4. <meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
5. </head>
6. <body>
7. <h1>WebView onAlert Demo</h1>
8. <button onclick="myFunction()">Click here</button>
9. <script>
10. function myFunction() {
11. alert("Hello World");
12. }
13. </script>
14. </body>
15. </html>
```

[UseAlertInWebview\_Fragment.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/UseAlertInWebview_Fragment.html#L21-L35)
