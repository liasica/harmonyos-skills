---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-open-in-new-window
title: 在新窗口中打开页面
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 设置基本属性和事件 > 在新窗口中打开页面
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:361eeec922b6a59ac2f86354bccf40b120982e3095fd8b170aeb0449d5fef274
---

Web组件提供了在新窗口打开页面的能力，开发者可以通过[multiWindowAccess()](../harmonyos-references/arkts-basic-components-web-attributes.md#multiwindowaccess9)接口来设置是否允许网页在新窗口打开。当有新窗口打开时，应用侧会在[onWindowNew()](../harmonyos-references/arkts-basic-components-web-events.md#onwindownew9)接口或[onWindowNewExt()](../harmonyos-references/arkts-basic-components-web-events.md#onwindownewext23)接口中收到Web组件新窗口事件。开发者需要在此接口事件中新建窗口来处理Web组件的窗口请求。

说明

* [onWindowNewExt()](../harmonyos-references/arkts-basic-components-web-events.md#onwindownewext23)接口为[onWindowNew()](../harmonyos-references/arkts-basic-components-web-events.md#onwindownew9)接口的功能增强接口，OnWindowNewExtEvent比OnWindowNewEvent新增了[NavigationPolicy](../harmonyos-references/arkts-basic-components-web-e.md#navigationpolicy23)和[WindowFeatures](../harmonyos-references/arkts-basic-components-web-i.md#windowfeatures23)，用于通知应用新窗口的打开方式和位置大小信息。当在同一个Web组件上同时使用这两个接口时，只有[onWindowNewExt()](../harmonyos-references/arkts-basic-components-web-events.md#onwindownewext23)接口会被触发。
* [allowWindowOpenMethod()](../harmonyos-references/arkts-basic-components-web-attributes.md#allowwindowopenmethod10)接口设置为true时，前端页面通过JavaScript函数调用的方式打开新窗口。
* 当在Web页面调用window.open(url, name)打开新窗口时，ArkWeb内核会根据name查找是否存在已绑定的Web组件。若存在，该Web组件将收到[onActivateContent()](../harmonyos-references/arkts-basic-components-web-events.md#onactivatecontent20)接口通知，以便应用可将其展示至前台；若不存在，ArkWeb内核将通过onWindowNew()接口通知应用创建新窗口。
* 如果在onWindowNew()接口通知中创建了新窗口，并将[ControllerHandler.setWebController()](../reference/apis-arkweb/arkts-basic-components-web-ControllerHandler.md#setwebcontroller9)接口的参数设置为新Web组件的WebviewController，则ArkWeb内核会完成name与该新Web组件的绑定。
* 如果在onWindowNew()接口通知中没有创建新窗口，需要将[ControllerHandler.setWebController()](../reference/apis-arkweb/arkts-basic-components-web-ControllerHandler.md#setwebcontroller9)接口的参数设置为null。

在下面的本地示例中，当用户点击“新窗口中打开网页”按钮时，应用会在onWindowNew()接口收到Web组件的新窗口事件。

说明

* 网页要求用户创建新的窗口时触发回调[OnWindowNewEvent()](../harmonyos-references/arkts-basic-components-web-i.md#onwindownewevent12)，该回调函数中isUserTrigger参数，true代表用户触发，false代表非用户触发。

* 应用侧代码。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 在同一界面有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
5. @CustomDialog
6. struct NewWebViewComp {
7. controller?: CustomDialogController;
8. webviewController1: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: '', controller: this.webviewController1 })
13. .javaScriptAccess(true)
14. .multiWindowAccess(false)
15. .onWindowExit(() => {
16. console.info('NewWebViewComp onWindowExit');
17. if (this.controller) {
18. this.controller.close();
19. }
20. })
21. .onActivateContent(() => {
22. // 该Web需要展示到前台，建议应用在这里进行tab或window切换的动作
23. console.info('NewWebViewComp onActivateContent')
24. })
25. }
26. }
27. }

29. @Entry
30. @Component
31. struct WebComponent {
32. controller: webview.WebviewController = new webview.WebviewController();
33. dialogController: CustomDialogController | null = null;

35. build() {
36. Column() {
37. Web({ src: $rawfile('window.html'), controller: this.controller })
38. .javaScriptAccess(true)
39. // 需要使能multiWindowAccess
40. .multiWindowAccess(true)
41. .allowWindowOpenMethod(true)
42. .onWindowNew((event) => {
43. if (this.dialogController) {
44. this.dialogController.close()
45. }
46. let popController: webview.WebviewController = new webview.WebviewController();
47. this.dialogController = new CustomDialogController({
48. builder: NewWebViewComp({ webviewController1: popController }),
49. // isModal设置为false，防止新窗口被销毁而无法触发onActivateContent回调
50. isModal: false
51. })
52. this.dialogController.open();
53. // 将新窗口对应WebviewController返回给Web内核。
54. // 若不调用event.handler.setWebController接口，会造成render进程阻塞。
55. // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
56. event.handler.setWebController(popController);
57. })
58. }
59. }
60. }
```

[OpenPageNewWin.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/OpenPageNewWin.ets#L16-L77)

* window.html页面代码。

  ```
  1. <!DOCTYPE html>
  2. <html>
  3. <head>
  4. <meta name="viewport" content="width=device-width"/>
  5. <title>WindowEvent</title>
  6. </head>
  7. <body>
  8. <input type="button" value="新窗口中打开网页" onclick="OpenNewWindow()">
  9. <script type="text/javascript">
  10. function OpenNewWindow()
  11. {
  12. var txt = '打开的窗口';
  13. let openedWindow = window.open("about:blank", "", "location=no,status=no,scrollbars=no");
  14. openedWindow.document.write("<p>" + "<br><br>" + txt + "</p>");
  15. openedWindow.focus();
  16. }
  17. </script>
  18. </body>
  19. </html>
  ```

**图1** 新窗口中打开页面效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/FGh7h_v-QTmC_o-XNgEGJw/zh-cn_image_0000002583478209.png?HW-CC-KV=V1&HW-CC-Date=20260427T234051Z&HW-CC-Expire=86400&HW-CC-Sign=9DB4E1B66F59F825BAEEA187CEABAEC2760DA5139D20AA93AC7F70AB35A5DFC6)
