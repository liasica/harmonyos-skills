---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-dialog
title: 使用Web组件显示网页弹框
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > 使用Web组件显示网页弹框
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b6145069aace53ed775e932c86760daa8d592e1d30b0646ef149544914a107d
---

在HTML中，可以使用JavaScript创建三种类型的弹框：警告框window.alert(message)、确认框window.confirm(message)和提示框window.prompt(message, defaultValue)。这些弹框可以用于向用户传递信息、确认操作或请求输入。

当前，ArkWeb暂未提供默认的应用弹框。如果需要网页的弹框能够正常使用，应用需要通过[onAlert](../harmonyos-references/arkts-basic-components-web-events.md#onalert)、[onConfirm](../harmonyos-references/arkts-basic-components-web-events.md#onconfirm)和[onPrompt](../harmonyos-references/arkts-basic-components-web-events.md#onprompt9)接口自定义弹框功能。

## 实现Alert弹框

window.alert()用于显示一个包含可选信息的对话框。警告框用于确保用户可以得到某些信息。当警告框出现后，用户需要点击确定按钮才能继续进行操作。

* 可选参数message是要显示在警告对话框中的字符串，如果传入其他类型的值，会转换成字符串。
* 该方法不存在返回值。

应用可以通过[onAlert](../harmonyos-references/arkts-basic-components-web-events.md#onalert)事件监听网页alert方法，并创建合适的弹框。

* 用[AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md)创建弹框。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @State message: string = 'Hello World';
  7. webviewController: webview.WebviewController = new webview.WebviewController();
  8. uiContext: UIContext = this.getUIContext();

  10. build() {
  11. Row() {
  12. Web({ src: $rawfile('test.html'), controller: this.webviewController })
  13. .onAlert((event) => {
  14. if (event) {
  15. console.info('event.url:' + event.url);
  16. console.info('event.message:' + event.message);
  17. this.uiContext.showAlertDialog({
  18. title: 'Warning',
  19. message: event.message,
  20. confirm:{
  21. value: 'confirm',
  22. action: () => {
  23. console.info('Alert confirmed.');
  24. event.result.handleConfirm();
  25. }
  26. },
  27. cancel: () => {
  28. event.result.handleCancel();
  29. }
  30. })
  31. }
  32. return true;
  33. })
  34. }
  35. }
  36. }
  ```

  [AchieveAlertDialogPage1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ShowWebPageDialog/entry/src/main/ets/pages/AchieveAlertDialogPage1.ets#L15-L52)

  加载的HTML。

  ```
  1. <!-- test.html -->
  2. <!DOCTYPE html>
  3. <html lang="en">
  4. <head>
  5. <meta charset="UTF-8">
  6. <meta name="viewport"
  7. content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  8. <meta http-equiv="X-UA-Compatible" content="ie=edge">
  9. <title>Document</title>
  10. <style>
  11. button,label,input {
  12. margin: 5px 0;
  13. }
  14. </style>
  15. </head>
  16. <body>
  17. <input type="text" id="alert-message" placeholder="message for alert"><br/>
  18. <button onclick="handleAlert()">alert</button><br/>
  19. <script>
  20. function handleAlert() {
  21. let message = document.getElementById("alert-message").value;
  22. let result = window.alert(message ? message : 'alert');
  23. }
  24. </script>
  25. </body>
  26. </html>
  ```
* 用[CustomDialog-AlertDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#alertdialog)创建弹框。

  ```
  1. import { AlertDialog } from '@kit.ArkUI';
  2. import { webview } from '@kit.ArkWeb';

  4. @Entry
  5. @Component
  6. struct AlertDialogPage {
  7. @State message: string = 'Hello World';
  8. @State title: string = 'Hello World';
  9. @State subtitle: string = '';
  10. @State result: JsResult | null = null;
  11. webviewController: webview.WebviewController = new webview.WebviewController();
  12. dialogControllerAlert: CustomDialogController = new CustomDialogController({
  13. builder: AlertDialog({
  14. primaryTitle: this.title,
  15. secondaryTitle: this.subtitle,
  16. content: this.message,
  17. primaryButton: {
  18. value: 'confirm',
  19. role: ButtonRole.ERROR,
  20. action: () => {
  21. console.info('Callback when the second button is clicked');
  22. this.result?.handleConfirm();
  23. }
  24. },
  25. }),
  26. onWillDismiss: () => {
  27. this.result?.handleCancel();
  28. this.dialogControllerAlert.close();
  29. }
  30. })
  31. build() {
  32. Column() {
  33. Web({ src: $rawfile('alert.html'), controller: this.webviewController })
  34. .onAlert((event) => {
  35. if (event) {
  36. console.info('event.url:' + event.url);
  37. console.info('event.message:' + event.message);
  38. this.title = 'Warning';
  39. this.message = event.message;
  40. this.result = event.result;
  41. this.dialogControllerAlert.open();
  42. }
  43. return true;
  44. })
  45. }
  46. }
  47. }
  ```

  [AchieveAlertDialogPage2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ShowWebPageDialog/entry/src/main/ets/pages/AchieveAlertDialogPage2.ets#L15-L63)

  加载的html。

  ```
  1. <!-- alert.html -->
  2. <!DOCTYPE html>
  3. <html lang="en">
  4. <head>
  5. <meta charset="UTF-8">
  6. <meta name="viewport"
  7. content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  8. <meta http-equiv="X-UA-Compatible" content="ie=edge">
  9. <title>Document</title>
  10. <style>
  11. button,label,input {
  12. margin: 5px 0;
  13. }
  14. </style>
  15. </head>
  16. <body>
  17. <input type="text" id="alert-message" placeholder="message for alert"><br/>
  18. <button onclick="handleAlert()">alert</button><br/>
  19. <script>
  20. function handleAlert() {
  21. let message = document.getElementById("alert-message").value;
  22. let result = window.alert(message ? message : 'alert');
  23. }
  24. </script>
  25. </body>
  26. </html>
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/DwW6tlWjRAuxmFhBCuRHZQ/zh-cn_image_0000002583438267.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=26457A9E01DB7686B5202AD7F078997A3DC2D1218A938E9FC9EF453AF5C9A33B)

## 实现Confirm弹框

window.confirm()用于显示一个包含可选消息的对话框，并等待用户确认或取消该对话框。

* 可选参数message是要显示在对话框中的字符串，如果传入其他类型的值，会转换成字符串。
* 该方法返回一个布尔值，表示是否选择了确定（true）或取消（false）。如果应用忽略了页面内的对话框，那么返回值总是false。

确认框用于验证用户是否接受某个操作，常用于询问用户是否离开网页，以防页面表单等数据丢失。

应用可以通过[onConfirm](../harmonyos-references/arkts-basic-components-web-events.md#onconfirm)事件监听网页confirm方法，并创建合适的弹框。

* 用[AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md)创建弹框。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @State message: string = 'Hello World';
  7. webviewController: webview.WebviewController = new webview.WebviewController();
  8. uiContext: UIContext = this.getUIContext();

  10. build() {
  11. Column() {
  12. Web({ src: $rawfile('test.html'), controller: this.webviewController })
  13. .onConfirm((event) => {
  14. if (event) {
  15. console.info('event.url:' + event.url);
  16. console.info('event.message:' + event.message);
  17. this.uiContext.showAlertDialog({
  18. title: 'Confirm',
  19. message: event.message,
  20. primaryButton: {
  21. value: 'cancel',
  22. action: () => {
  23. event.result.handleCancel();
  24. }
  25. },
  26. secondaryButton: {
  27. value: 'ok',
  28. action: () => {
  29. event.result.handleConfirm();
  30. }
  31. },
  32. cancel: () => {
  33. event.result.handleCancel();
  34. }
  35. })
  36. }
  37. return true;
  38. })
  39. }
  40. }
  41. }
  ```

  [AchieveConfirmDialogPage1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ShowWebPageDialog/entry2/src/main/ets/pages/AchieveConfirmDialogPage1.ets#L15-L57)

  加载的html。

  ```
  1. <!-- test.html -->
  2. <!DOCTYPE html>
  3. <html lang="en">
  4. <head>
  5. <meta charset="UTF-8">
  6. <meta name="viewport"
  7. content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  8. <meta http-equiv="X-UA-Compatible" content="ie=edge">
  9. <title>Document</title>
  10. <style>
  11. button,label,input {
  12. margin: 5px 0;
  13. }
  14. </style>
  15. </head>
  16. <body>
  17. result：<label id="confirmLabel" for="confirm"></label><br/>
  18. <input type="text" id="confirm-message" placeholder="message for confirm"><br/>
  19. <button id="confirm" onclick="handleConfirm()">confirm</button><br/>
  20. <script>
  21. function handleConfirm() {
  22. let message = document.getElementById("confirm-message").value;
  23. let result = window.confirm(message ? message : 'confirm');
  24. console.info(result);
  25. document.getElementById("confirmLabel").innerHTML=String(result);
  26. }
  27. </script>
  28. </body>
  29. </html>
  ```
* 用[CustomDialog-ConfirmDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#confirmdialog)创建弹框。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { ConfirmDialog } from '@kit.ArkUI';

  4. @Entry
  5. @Component
  6. struct DialogConfirmDialog {
  7. @State message: string = 'Hello World';
  8. @State title: string = 'Hello World';
  9. @State result: JsResult | null = null;
  10. webviewController: webview.WebviewController = new webview.WebviewController();
  11. isChecked = false;
  12. dialogControllerCheckBox: CustomDialogController = new CustomDialogController({
  13. builder: ConfirmDialog({
  14. title: this.title,
  15. content: this.message,
  16. // 勾选框选中状态
  17. isChecked: this.isChecked,
  18. // 勾选框说明文本
  19. checkTips: 'No further prompts after prohibition',
  20. primaryButton: {
  21. value: 'prohibited',
  22. action: () => {
  23. this.result?.handleCancel();
  24. },
  25. },
  26. secondaryButton: {
  27. value: 'allow',
  28. action: () => {
  29. this.isChecked = false;
  30. console.info('Callback when the second button is clicked');
  31. this.result?.handleConfirm();
  32. }
  33. },
  34. onCheckedChange: (checked) => {
  35. this.isChecked = checked;
  36. console.info('Callback when the checkbox is clicked');
  37. },
  38. }),
  39. onWillDismiss: () => {
  40. this.result?.handleCancel();
  41. this.dialogControllerCheckBox.close();
  42. },
  43. autoCancel: true
  44. })

  46. build() {
  47. Column() {
  48. Web({ src: $rawfile('confirm.html'), controller: this.webviewController })
  49. .onConfirm((event) => {
  50. if (event) {
  51. if (this.isChecked) {
  52. event.result.handleCancel();
  53. } else {
  54. console.info('event.url:' + event.url);
  55. console.info('event.message:' + event.message);
  56. this.title = 'Confirm';
  57. this.message = event.message;
  58. this.result = event.result;
  59. this.dialogControllerCheckBox.open();
  60. }
  61. }
  62. return true;
  63. })
  64. }
  65. }
  66. }
  ```

  [AchieveConfirmDialogPage2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ShowWebPageDialog/entry2/src/main/ets/pages/AchieveConfirmDialogPage2.ets#L15-L82)

  加载的html。

  ```
  1. <!-- confirm.html -->
  2. <!DOCTYPE html>
  3. <html lang="en">
  4. <head>
  5. <meta charset="UTF-8">
  6. <meta name="viewport"
  7. content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  8. <meta http-equiv="X-UA-Compatible" content="ie=edge">
  9. <title>Document</title>
  10. <style>
  11. button,label,input {
  12. margin: 5px 0;
  13. }
  14. </style>
  15. </head>
  16. <body>
  17. result：<label id="confirmLabel" for="confirm"></label><br/>
  18. <input type="text" id="confirm-message" placeholder="message for confirm"><br/>
  19. <button id="confirm" onclick="handleConfirm()">confirm</button><br/>
  20. <script>
  21. function handleConfirm() {
  22. let message = document.getElementById("confirm-message").value;
  23. let result = window.confirm(message ? message : 'confirm');
  24. console.info(result);
  25. document.getElementById("confirmLabel").innerHTML=String(result);
  26. }
  27. </script>
  28. </body>
  29. </html>
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/LI8DZ8taTKGqFRuWrgtHnA/zh-cn_image_0000002552958222.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=1AF80DF99710F4F4E24623FE0C77EFEC2880A9BAE777813E4DC256C20BEF791C)

## 实现Prompt弹框

window.prompt()用于显示一个对话框，并等待用户提交文本或取消对话框。用户需要输入某个值，然后点击确认或取消按钮。点击确认返回输入的值，点击取消返回null。

* 可选参数message向用户显示的一串文本。如果在提示窗口中没有什么可显示的，可以省略。
* 可选参数defaultValue是一个字符串，包含文本输入字段中显示的默认值。
* 返回值为用户输入文本的字符串，或null。

提示框用于提示用户输入某个值，常用于需要用户输入临时的口令或验证码等场景。

应用可以通过[onPrompt](../harmonyos-references/arkts-basic-components-web-events.md#onprompt9)事件监听网页prompt方法，并创建合适的弹框。

* 用[CustomDialog-CustomContentDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#customcontentdialog12)创建弹框。

  ```
  1. import { CustomContentDialog } from '@kit.ArkUI';
  2. import { webview } from '@kit.ArkWeb';

  4. @Entry
  5. @Component
  6. struct PromptDialog {
  7. @State message: string = 'Hello World';
  8. @State title: string = 'Hello World';
  9. @State result: JsResult | null = null;
  10. promptResult: string = '';
  11. webviewController: webview.WebviewController = new webview.WebviewController();
  12. dialogController: CustomDialogController = new CustomDialogController({
  13. builder: CustomContentDialog({
  14. primaryTitle: this.title,
  15. contentBuilder: () => {
  16. this.buildContent();
  17. },
  18. buttons: [
  19. {
  20. value: 'cancel',
  21. buttonStyle: ButtonStyleMode.TEXTUAL,
  22. action: () => {
  23. console.info('Callback when the button is clicked');
  24. this.result?.handleCancel();
  25. }
  26. },
  27. {
  28. value: 'confirm',
  29. buttonStyle: ButtonStyleMode.TEXTUAL,
  30. action: () => {
  31. this.result?.handlePromptConfirm(this.promptResult);
  32. }
  33. }
  34. ],
  35. }),
  36. onWillDismiss: () => {
  37. this.result?.handleCancel();
  38. this.dialogController.close();
  39. }
  40. });

  42. // 自定义弹出框的内容区
  43. @Builder
  44. buildContent(): void {
  45. Column() {
  46. Text(this.message)
  47. TextInput()
  48. .onChange((value) => {
  49. this.promptResult = value;
  50. })
  51. .defaultFocus(true)
  52. }
  53. .width('100%')
  54. }

  56. build() {
  57. Column() {
  58. Web({ src: $rawfile('prompt.html'), controller: this.webviewController })
  59. .onPrompt((event) => {
  60. if (event) {
  61. console.info('event.url:' + event.url);
  62. console.info('event.message:' + event.message);
  63. console.info('event.value:' + event.value);
  64. this.title = 'Prompt';
  65. this.message = event.message;
  66. this.promptResult = event.value;
  67. this.result = event.result;
  68. this.dialogController.open();
  69. }
  70. return true;
  71. })
  72. }
  73. }
  74. }
  ```

  [AchievePromptDialogPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ShowWebPageDialog/entry/src/main/ets/pages/AchievePromptDialogPage.ets#L15-L90)

  加载的html。

  ```
  1. <!-- prompt.html -->
  2. <!DOCTYPE html>
  3. <html lang="en">
  4. <head>
  5. <meta charset="UTF-8">
  6. <meta name="viewport"
  7. content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  8. <meta http-equiv="X-UA-Compatible" content="ie=edge">
  9. <title>Document</title>
  10. <style>
  11. button,label,input {
  12. margin: 5px 0;
  13. }
  14. </style>
  15. </head>
  16. <body>
  17. result：<label id="promptLabel" for="prompt"></label><br/>
  18. <input type="text" id="prompt-message" placeholder="message for prompt"><br/>
  19. <input type="text" id="prompt-value" placeholder="default value for prompt"><br/>
  20. <button id="prompt" onclick="handlePrompt()">prompt</button><br/>
  21. <script>
  22. function handlePrompt() {
  23. let message = document.getElementById("prompt-message").value;
  24. let defaultValue = document.getElementById("prompt-value").value;
  25. let result = window.prompt(message ? message : 'prompt', defaultValue);
  26. console.info(result);
  27. document.getElementById("promptLabel").innerHTML=result;
  28. }
  29. </script>
  30. </body>
  31. </html>
  ```

需要的资源文件string.json

```
1. {
2. "string": [
3. {
4. "name": "from",
5. "value": "来自"
6. },
7. {
8. "name": "warn",
9. "value": "的警告"
10. },
11. {
12. "name": "notarize",
13. "value": "确认"
14. },
15. {
16. "name": "cancel",
17. "value": "取消"
18. },
19. {
20. "name": "info",
21. "value": "的消息"
22. }
23. ]
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/re0-mn-wRSuz327Tjxqz7Q/zh-cn_image_0000002583478223.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=33C57325D0CBED9BAC43A8A55C454AD62A07B98BBC8C0F7CA911A7F98C9F6B1C)
