---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-drag
title: 使用Web组件的拖拽功能与网页交互
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > 使用Web组件的拖拽功能与网页交互
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:125b26a0a04ea499d4bc4c206f30f166be08050fa16e8b8d4151a40ba0c84ce9
---

ArkWeb的拖拽功能使应用能够在网页中实现元素的拖放，用户可以长按可拖拽的元素，将其拖至可放置的元素上，然后松手完成放置。ArkWeb在网页内容中的拖拽功能满足H5标准。

## 将网页内容拖拽至其他应用

ArkWeb目前支持以下四种数据格式。应用按照 H5 标准设置这些格式的拖拽数据，即可将内容拖拽到其他应用中。

| 数据格式 | 说明 |
| --- | --- |
| text/plain | 文本 |
| text/uri-list | 链接 |
| text/html | HTML格式 |
| Files | 文件 |

## 拖拽事件通知

ArkWeb拖拽不同于ArkUI的组件级拖拽，主要针对网页内容的拖拽，因此仅支持部分拖拽事件的监听方法。

| 监听方法 | 说明 |
| --- | --- |
| [onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart) | 不建议使用此方法，否则会影响Web组件的拖拽行为，造成拖拽逻辑不符合预期，如无法触发H5拖拽事件监听，预览图无法创建或预览图错误，拖拽数据无法预置等。 |
| [onDragEnter](../harmonyos-references/ts-universal-events-drag-drop.md#ondragenter) | 拖拽的元素进入Web区域。 |
| [onDragMove](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove) | 拖拽的元素在Web区域移动。 |
| [onDragLeave](../harmonyos-references/ts-universal-events-drag-drop.md#ondragleave) | 拖拽的元素离开Web区域。 |
| [onDrop](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop15) | 拖拽的元素落入Web区域。 |
| [onDragEnd](../harmonyos-references/ts-universal-events-drag-drop.md#ondragend10) | 由Web发起的拖拽元素结束拖拽。 |

## 在ArkTS侧实现拖拽相关逻辑

在多数情况下，应用在H5端实现的拖拽功能能够满足需求。如有需要，请参考以下案例，实现在ArkTS端进行拖拽数据读取等操作。

1. [建立应用侧与前端页面数据通道](web-app-page-data-channel.md)。
2. 在onDrop方法中，做简单逻辑，例如暂存一些关键数据。
3. 在ArkTS侧接收消息的方法中，添加应用处理逻辑，可以进行耗时任务。

由于ArkTS侧的onDrop方法会早于H5中放置事件的处理方法（H5示例中的droppable.addEventListener('drop')）执行，若在onDrop方法中进行页面跳转等操作，将导致H5中的drop方法无法正确执行，产生不符合预期的结果。因此，应建立双向通信机制，在H5中的drop方法执行完毕后，通知ArkTS侧执行相应的业务逻辑，以确保业务逻辑的预期执行。

```
1. import { webview } from '@kit.ArkWeb'
2. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

4. @Entry
5. @Component
6. struct DragDrop {
7. private controller: webview.WebviewController = new webview.WebviewController()
8. @State ports: Array<webview.WebMessagePort> = []
9. @State dragData: Array<unifiedDataChannel.UnifiedRecord> = []

11. build() {
12. Column() {
13. Web({
14. src: $rawfile('drag.html'),
15. controller: this.controller,
16. }).onPageEnd((event) => {
17. // 注册通信端口
18. this.ports = this.controller.createWebMessagePorts();
19. this.ports[1].onMessageEvent((result: webview.WebMessage) => {
20. // ArkTS收到html传来的数据后的处理，可以先打日志确认下消息，双端的消息格式可以自己约定，能唯一识别就行
21. console.info('ETS receive Message: typeof (result) = ' + typeof (result) + ';' + result);
22. // 这里添加result中消息接收到后的处理,可进行耗时任务
23. });
24. console.info('ETS postMessage set h5port ');
25. // 完成通信端口注册后，向前端发送注册完成消息，完成双向的端口绑定
26. this.controller.postMessage('__init_port__', [this.ports[0]], '*');
27. })// onDrop 可做简单逻辑，例如暂存一些关键数据
28. .onDrop((dragEvent: DragEvent) => {
29. console.info('ETS onDrop!')
30. let data: UnifiedData = dragEvent.getData();
31. if(!data) {
32. return false;
33. }
34. let uriArr: unifiedDataChannel.UnifiedRecord[] = data.getRecords();
35. if (!uriArr || uriArr.length <= 0) {
36. return false;
37. }
38. // 可以遍历records取数据暂存，或者以其他方式暂存数据
39. for (let i = 0; i < uriArr.length; ++i) {
40. if (uriArr[i].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
41. let plainText = uriArr[i] as unifiedDataChannel.PlainText;
42. if (plainText.textContent) {
43. console.info('plainText.textContent: ', plainText.textContent);
44. }
45. }
46. }
47. return true
48. })
49. }

51. }
52. }
```

[DragArkTSPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebDragInteraction/entry/src/main/ets/pages/DragArkTSPage.ets#L15-L68)

H5示例:

```
1. <html lang="zh-CN">
2. <head>
3. <meta charset="UTF-8">
4. <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
5. <title>H5 拖拽 Demo</title>
6. </head>
7. <style>
8. body {
9. font-family: Arial, sans-serif;
10. padding: 20px;
11. }

13. .draggable {
14. width: 100px;
15. height: 100px;
16. background-color: #4CAF50;
17. color: white;
18. text-align: center;
19. line-height: 100px;
20. margin-bottom: 20px;
21. cursor: grab;
22. }

24. .droppable {
25. width: 300px;
26. height: 150px;
27. border: 2px dashed #999;
28. background-color: #f0f0f0;
29. text-align: center;
30. line-height: 150px;
31. font-size: 16px;
32. }

34. .success {
35. background-color: #4CAF50;
36. color: white;
37. }
38. </style>
39. <body>

41. <h2>H5 拖拽 Demo</h2>

43. <div id="draggable" class="draggable" draggable="true">可拖拽元素</div>

45. <div id="droppable" class="droppable">请将方块拖到这里</div>

47. <script>
48. const draggable = document.getElementById('draggable');
49. const droppable = document.getElementById('droppable');

51. // 拖拽开始事件
52. draggable.addEventListener('dragstart', function (e) {
53. e.dataTransfer.setData('text/plain', this.id);
54. this.style.opacity = '0.4';
55. });

57. // 拖拽结束事件
58. draggable.addEventListener('dragend', function (e) {
59. this.style.opacity = '1';
60. });

62. // 拖入目标区域时触发
63. droppable.addEventListener('dragover', function (e) {
64. e.preventDefault(); // 必须调用，否则无法触发 drop 事件
65. });

67. // 放置事件
68. droppable.addEventListener('drop', function (e) {
69. e.preventDefault();
70. const data = e.dataTransfer.getData('text/plain');
71. // 传入ArkTS
72. PostMsgToArkTS(data);
73. const draggableEl = document.getElementById(data);
74. this.appendChild(draggableEl);
75. this.classList.add('success');
76. this.textContent = "放置成功！";
77. });

79. // scriptproxy端口在js侧设置
80. var h5Port;
81. window.addEventListener('message', function (event) {
82. console.info("H5 receive settingPort message");
83. if (event.data == '__init_port__') {
84. if (event.ports[0] != null) {
85. console.info("H5 set h5Port " + event.ports[0]);
86. h5Port = event.ports[0];
87. }
88. }
89. });

91. // 通过scriptproxy方式,发送数据到ArkTS侧的实现
92. function PostMsgToArkTS(data) {
93. console.info("H5 PostMsgToArkTS, h5Port " + h5Port);
94. if (h5Port) {
95. h5Port.postMessage(data);
96. } else {
97. console.error("h5Port is null, Please initialize first");
98. }
99. }
100. </script>

102. </body>
103. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/_rMchByyTX6P6KcT83wd3g/zh-cn_image_0000002552798574.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=2C63AFAF05C276A28DEE08D76277356DAB2D8CC5ACD5690CA71558721D97B6F5)

日志打印：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ks6bK0A7Sx-UKGUzcsPYAw/zh-cn_image_0000002583438269.png?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=9C37F75C9F5CD2EB213B16376FC42F12DC0E166CD34EDDB86710B7D6D64776C5)

## 常见问题

### 为什么H5设置的拖拽事件没有触发？

请检查相关CSS资源是否正常设置，因为有些网页UA做了判断，针对特定设备的UA才会进行CSS样式设置。可以考虑在Web组件设置自定义UA解决这种问题，例如：

```
1. import { webview } from '@kit.ArkWeb'

3. @Entry
4. @Component
5. struct Index {
6. private webController: webview.WebviewController = new webview.WebviewController()
7. build(){
8. Column() {
9. Web({
10. src: 'example.com',
11. controller: this.webController,
12. }).onControllerAttached(() => {
13. // 特定UA
14. let customUA = 'android'
15. this.webController.setCustomUserAgent(this.webController.getUserAgent() + customUA)
16. })
17. }
18. }
19. }
```

[SetUAPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebDragInteraction/entry/src/main/ets/pages/SetUAPage.ets#L15-L35)

### 如何禁用web组件拖拽能力

在未进行特殊配置的情况下，web组件默认支持拖拽功能。如果不需要拖拽功能，可以参考以下示例禁用拖拽。

禁用拖拽方式主要分为两类：

1. 网页侧通过W3C CSS、JS进行拦截/禁用。
2. 应用侧通过Web组件runJavaScriptExt接口注入JS进行拦截/禁用。

H5示例1:

```
1. <html lang="zh-CN">
2. <head>
3. <meta charset="UTF-8">
4. <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
5. <title>w3c通用属性/方法禁用拖拽</title>
6. </head>
7. <style>
8. body {
9. font-family: Arial, sans-serif;
10. padding: 20px;
11. }
12. .normal {
13. width: 100px;
14. height: 100px;
15. margin-bottom: 40px;
16. }
17. .undraggable {
18. width: 100px;
19. height: 100px;
20. margin-bottom: 40px;
21. -webkit-user-drag: none;
22. }

24. </style>
25. <body>

27. <h2>w3c通用属性/方法禁用拖拽</h2>

29. <!--一，通过显式设置draggable样式为false来禁用该元素的拖拽-->
30. <!--仅对img或div这种整个元素节点的拖拽行为生效，对节点中选中的文字不生效-->
31. <div>draggable设置禁用拖拽</div>
32. <img class="normal" draggable="false" src="./any-pic.png"><br>

34. <!--二，通过引用一个样式class，class中设置-webkit-user-drag为none来禁用拖拽-->
35. <!--生效范围同方式一-->
36. <div>-webkit-user-drag设置禁用拖拽</div>
37. <img class="undraggable" src="./any-pic.png"><br>

39. <!--三，通过对设置ondragstart事件监听并preventDefault来禁用拖拽-->
40. <!--对任意内容的拖拽行为都生效-->
41. <!--可通过扩大监听器监听的范围来禁用更大区域内的拖拽，比如监听在window上可实现整个web组件的拖拽禁用-->
42. <!--由于生效节点较靠后，拖拽事实上已进行部分，会对菜单功能产生影响-->
43. <div>ondragstart设置禁用拖拽</div>
44. <div ondragstart="dragstartHandler(event)">
45. <img class="normal" src="./any-pic.png">
46. <p>
47. 此段文本用于验证ondragstart脚本对选中文本的禁用拖拽效果
48. </p>
49. </div>

51. <script>
52. function dragstartHandler(event) {
53. console.info('forbid drag when drag start');
54. event.preventDefault();
55. }
56. </script>

58. </body>
59. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/-6WkWdBWSg2sizax690aCw/zh-cn_image_0000002552958224.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=A686F47DAAB1A5B0A6B4BB26F4366AEA2E6226AB6A3C224B2C416CD05AF267D8)

html示例2:

```
1. <html lang="zh-CN">
2. <head>
3. <meta charset="UTF-8">
4. <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
5. <title>runJavascriptExt注入js禁用拖拽</title>
6. </head>
7. <style>
8. body {
9. font-family: Arial, sans-serif;
10. padding: 20px;
11. }
12. .normal {
13. width: 100px;
14. height: 100px;
15. margin-bottom: 40px;
16. }
17. </style>
18. <body>

20. <h2>runJavascriptExt注入js禁用拖拽</h2>

22. <div>
23. <img class="normal" src="./any-pic.png">
24. <p>
25. 此段文本用于验证runJavascriptExt注入js对选中文本的禁止拖拽效果
26. </p>
27. </div>

29. </body>
30. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/IGvmDfatTU64C_wEx4Yl7A/zh-cn_image_0000002583478225.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=57768934F6FC21AE4B590D15227A0C4F01D42AF909BD4E78F718DB458BBE91C4)

ArkTS示例:

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. webViewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Button('w3cDemoPage')
11. .onClick(() => {
12. this.webViewController.loadUrl($rawfile('w3c-forbid.html'));
13. })
14. Button('runJsDemoPage')
15. .onClick(() => {
16. this.webViewController.loadUrl($rawfile('runJs-forbid.html'));
17. })
18. Button('runJsForbidDrag')
19. .onClick(() => {
20. try {
21. // 使用runJavaScriptExt执行脚本添加dragstart事件监听器去禁用拖拽
22. this.webViewController.runJavaScriptExt(
23. 'window.addEventListener(\'dragstart\', (ev) => {\n' +
24. 'ev.preventDefault();\n' +
25. '});',
26. (error, result) => {
27. if (error) {
28. console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
29. return;
30. }
31. });
32. } catch (resError) {
33. console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
34. }
35. })
36. Web({
37. src: $rawfile('w3c-forbid.html'),
38. controller: this.webViewController
39. })
40. .domStorageAccess(true)
41. .javaScriptAccess(true)
42. .fileAccess(true)
43. }
44. .height('100%')
45. .width('100%')
46. }
47. }
```

[ForbidDragPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebDragInteraction/entry/src/main/ets/pages/ForbidDragPage.ets#L15-L63)
