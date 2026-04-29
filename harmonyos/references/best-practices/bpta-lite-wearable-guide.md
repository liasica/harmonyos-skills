---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lite-wearable-guide
title: 轻量级智能穿戴应用开发
breadcrumb: 最佳实践 > 多端设备体验提升 > 穿戴 > 轻量级智能穿戴应用开发
category: best-practices
scraped_at: 2026-04-29T14:13:07+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:b3613f17bd1569ce2242b934f05a96611134d3aa74632196c0984a50f47a0790
---

## 概述

对于轻量级智能穿戴（Lite Wearable），应用可以通过HarmonyOS提供的接口实现传感器、UI交互等常规业务的开发。开发者可以根据轻量级智能穿戴的特点，打造针对轻量级智能穿戴的独特应用。当前支持产品有：HUAWEI WATCH GT系列、Watch D系列、Fit系列、Watch Ultimate系列。

轻量级智能穿戴产品系列对应的分辨率和支持API如下表所示：

| 产品系列 | 分辨率（px） | 支持API |
| --- | --- | --- |
| WATCH GT 2 | 390\*390 | 5 |
| WATCH GT 2 Pro | 454\*454 | 6 |
| WATCH GT 3 | 466\*466 | 6 |
| WATCH GT 4 | 466\*466 | 10 |
| WATCH GT 5 | 466\*466 | 12 |
| WATCH GT 6 | 466\*466 | 20 |
| WATCH D | 280\*456 | 6 |
| WATCH D2 | 408\*480 | 12 |
| WATCH FIT 2 | 336\*480 | 6 |
| WATCH FIT 3 | 408\*480 | 10 |
| WATCH FIT 4 | 408\*480 | 19 |

本章节后续部分将以创建“Hello World”的轻量级智能穿戴应用为例，逐步讲解如何在应用中构建布局、绘制样式、添加组件、绑定事件、实现页面路由跳转等。

说明

本文档适用于轻量级智能穿戴应用开发，针对智能穿戴应用请参考[智能穿戴](bpta-smartwatch.md)。

## 体验应用

### 搭建环境和创建项目

* 搭建环境：请参考[安装DevEco Studio](../harmonyos-guides/ide-software-install.md)，配置开发环境。
* 创建项目：请参考[创建一个新的工程](../harmonyos-guides/ide-create-new-project.md)，模板选择“[Lite]Empty Ability”，设备类型选择“Lite Wearable”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/SIeKJiqgRuyco4scLYM3sw/zh-cn_image_0000002230878012.png?HW-CC-KV=V1&HW-CC-Date=20260429T061301Z&HW-CC-Expire=86400&HW-CC-Sign=44A4DF1CA5FA48E2B48A75E7F07396422E3D78282DB7D5690692EA378FE34CDE "点击放大")

### 工程目录介绍

HelloWorld工程目录如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/05ptXwsET6WWFLKI5BnwPQ/zh-cn_image_0000002231037832.png?HW-CC-KV=V1&HW-CC-Date=20260429T061301Z&HW-CC-Expire=86400&HW-CC-Sign=BA9D152EDE3C7FB4115421D55ABDC79826064539F54DD6FFB614252E586DFE18 "点击放大")

**pages/index/index.hml****：**此文件定义了index页面的布局，在index页面中用到的组件，以及这些组件的层级关系。以下示例代码包含了一个text组件，内容为“Hello World”。

```
1. <!-- Output the content of the text component. -->
2. <div class="container">
3. <text class="title">
4. Hello {{ title }}
5. </text>
6. </div>
```

[initpage.hml](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/initpage/initpage.hml#L2-L7)

**pages/index/index.css****：**此文件定义了index页面的样式。以下示例代码定义了“container”和“title”的样式。

```
1. .container {
2. display: flex;
3. justify-content: center;
4. align-items: center;
5. left: 0px;
6. top: 0px;
7. width: 466px;
8. height: 466px;
9. }
10. .title {
11. font-size: 30px;
12. text-align: center;
13. width: 200px;
14. height: 100px;
15. }
```

**pages/index/index.js****：**此文件定义了index页面的业务逻辑，比如数据绑定，事件处理等。以下示例代码变量通过动态绑定的形式定义“title”字符串为“World”。

```
1. export default {
2. data: {
3. title: 'World'
4. }
5. }
```

[initpage.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/initpage/initpage.js#L2-L6)

**resources****：**此目录用于存放系统级资源配置文件，如应用图标等。

**config.json****：**此文件是配置文件，主要定义了页面路由和应用信息，可根据DevEco Studio的工程和页面创建向导自动完成填充。

```
1. {
2. "app": {
3. "bundleName": "com.example.litewearable",
4. "vendor": "example",
5. "version": {
6. "code": 1000000,
7. "name": "1.0.0"
8. }
9. },
10. "deviceConfig": {},
11. "module": {
12. "deviceType": [
13. "liteWearable"
14. ],
15. "distro": {
16. "deliveryWithInstall": true,
17. "moduleName": "entry",
18. "moduleType": "entry"
19. },
20. // ...
21. "abilities": [
22. {
23. "name": ".MainAbility",
24. "srcLanguage": "js",
25. "srcPath": "MainAbility",
26. "icon": "$media:icon",
27. "description": "$string:MainAbility_desc",
28. "label": "$string:MainAbility_label",
29. "type": "page"
30. }
31. ],
32. "js": [
33. {
34. "pages": [
35. "pages/index/index",
36. // ...
37. ],
38. "name": ".MainAbility"
39. }
40. ]
41. }
42. }
```

### 运行应用

使用预览器查看效果，请参考[查看ArkTS/JS预览效果](../harmonyos-guides/ide-previewer-arkts-js.md)。

在Lite Wearable中运行应用/服务，依赖HarmonyOS NEXT版本以前的华为手机上的**运动健康**和**应用调测助手**APP辅助进行。

**前提条件**

* 已将**运动健康APP**升级至最新版本。
* 从华为应用市场安装**应用调测助手APP**。
* 在Lite Wearable中运行应用/服务，需要根据[应用/元服务签名](../harmonyos-guides/ide-signing.md)，提前对应用/服务进行签名。

  说明

  因Lite Wearable设备无法与DevEco Studio进行连接，因此在对Lite Wearable应用/服务签名时，不能采用自动化签名方案，只能使用[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)，然后再手动配置签名信息。

**操作步骤**

1. 使用USB连接线将手机和电脑进行连接，确保连接状态是正常的。
2. 手机与电脑使用USB连接时，在手机上选择**传输文件**连接方式。
3. 在工程目录中的**Build > outputs >hap**中选择生成的HAP，通过手工拷贝的方式将HAP拷贝至手机中的“/sdcard/haps/”目录。
4. 将Lite Wearable通过蓝牙与华为手机进行连接。
   1. 进入**运动健康**APP，在设备页签中，单击**添加设备**按钮。
   2. 进入**手表**列表中，选择对应的Lite Wearable型号。
   3. 单击**开始配对**，按照界面指引完成Lite Wearable与华为手机之间的连接。
5. 打开**应用调测助手**APP，界面会显示已经与华为手机连接的Lite Wearable。

   说明

   * 如果Lite Wearable与华为手机未连接，请单击**应用调测助手**APP界面的**连接设备**按钮，手机会自动打开**运动健康**APP添加Lite Wearable。
   * [申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)时，需先[注册设备](../app/agc-help-add-device-0000002283189937.md)，再选择调试设备。
6. 单击**应用调测助手**APP界面中的**应用管理**按钮，选择需要安装的HarmonyOS安装包进行安装。
7. 安装完成后，单击Lite Wearable中的应用图标，运行HarmonyOS应用。

## 构建布局

### 布局说明

本文以轻量级智能穿戴中的圆形表盘为例，把466px（px为逻辑像素，非物理像素）作为基准宽度。在构建页面布局时，需要对基本元素进行分析：

* 元素的尺寸和排列位置是否合理
* 是否有重叠的元素
* 是否需要设置对齐、内间距或者边界
* 是否包含子元素及其排列位置
* 是否需要容器组件

  说明

  将页面中的元素分解之后再逐个对基本元素进行自上而下的实现，可以减少多层嵌套造成的视觉混乱，尽可能的避免出现逻辑混乱，还可以提高代码的可读性，方便对页面做后续的调整和增改。

### 实现应用页面

应用页面由组件声明（.hml）、css样式（.css）和script脚本（.js）三部分构成。组件声明在“pages/index/index.hml”文件中实现，使用<text>组件显示文字，并用一个容器组件来包裹<text>组件，这里以<div>为例进行说明。示例代码如下：

```
1. <!-- The "style" contains the style information of the component. -->
2. <!-- The detailed introduction about the style will be presented in the next subsection. -->
3. <div style="width: 466px; height: 466px;">
4. <text style="width: 200px; height: 100px;">
5. <!-- The content to be displayed in the <text> component. -->
6. Hello World
7. </text>
8. </div>
```

[style1.hml](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/style1/style1.hml#L2-L9)

现在已经完成了一个简单应用开发的第一步，在后续章节中将继续介绍样式、事件的开发方法，不断优化和完善应用。

## 绘制样式

组件标签中类似“style="width:466px;height:466px;"”的语句即为样式设置语句，通过样式可以设置组件的显示大小、背景颜色、对齐方式等属性。本章节以<div>和<text>组件为例来介绍如何设置样式，样式主要有三种设置方式：行内样式、选择器样式和动态绑定样式，三种方式设置的样式效果一致。

### 行内样式

行内样式是将样式内容直接放到组件的style属性中，多个样式值则是通过分号间隔。以下示例代码通过行内样式对div和text组件设置了高度、宽度或其他属性。

```
1. <!-- Set the child components within the div to be flexible layout and display them centered; -->
2. <!-- ensure that the text component is displayed in the middle of the screen. -->
3. <div style="width: 466px; height: 466px; display: flex; justify-content: center; align-items: center;">
4. <!-- Set the text component to display the text centered; -->
5. <!-- ensure that "Hello World" is displayed right in the middle of the screen. -->
6. <text style="width: 200px; height: 100px; font-size: 30px; text-align: center;">
7. Hello World
8. </text>
9. </div>
```

[style2.hml](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/style2/style2.hml#L2-L10)

### 选择器样式

使用行内样式存在以下缺点：

* 针对每个组件都要设置样式。
* 如果多个组件需要设置相同的样式，则每个组件都写同样的样式，导致代码冗余；而且修改样式时，需要修改所有代码，工作量大。

针对以上问题，我们可以采用选择器样式，将所有的样式代码写到pages/index/index.css文件中，然后通过class、id等方式和组件关联起来。以上节中的代码为例，修改后的代码如下：

```
1. /* index.css */
2. /* . For the class selector, all components with the class attribute set to "container" will apply this style. */
3. .container {
4. display: flex;
5. justify-content: center;
6. align-items: center;
7. width: 466px;
8. height: 466px;
9. } /* # For the ID selector, the component with the ID "title" will apply this style. */
10. #title {
11. font-size: 30px;
12. text-align: center;
13. width: 200px;
14. height: 100px;
15. }
```

```
1. <!-- index.hml -->
2. <!-- Link the style code block of .container in index.css -->
3. <div class="container">
4. <!-- Link to the #title style code block in index.css -->
5. <text id="title">
6. Hello World
7. </text>
8. </div>
```

[style3.hml](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/style3/style3.hml#L2-L9)

### 动态绑定样式

在行内样式和选择器样式中，样式设置方式是静态的，即代码开发中设置的样式在程序运行的时候不能更改，这种方式限制了程序的显示效果。如果要在程序运行过程中动态地改变样式，需要用到动态绑定样式。动态绑定就是值和变量动态关联，随着值的变更而显示不同的效果。动态绑定的使用方式为“{{变量名}}”，其中变量名是js文件中data对象的属性值。目前动态绑定样式只支持绑定行内样式。

以下示例代码中，text的字体大小和data中的fontSize属性绑定，字体颜色和data中的fontColor属性绑定：

```
1. <!-- index.hml -->
2. <div class="container">
3. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
4. Hello World
5. </text>
6. </div>
```

[style4.hml](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/style4/style4.hml#L2-L7)

```
1. // index.js:
2. export default {
3. data: {
4. fontSize: '30px',
5. fontColor: '#FF0000',
6. }
7. };
```

[style4.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/style4/style4.js#L2-L8)

现在已经完成了字体大小和颜色的样式绑定，下一节交互事件将介绍如何通过按钮的点击事件实现动态改变字体的样式。

## 交互事件

### 通用事件

每个组件都有一些通用事件和特有事件，开发者可在这些事件中实现应用的功能和逻辑。组件中添加事件的格式如下：

```
1. <element onevent="eventAction">
```

常见的组件事件如下表所示：

| 事件 | 描述 |
| --- | --- |
| click | 组件被点击时触发，使用方法参见下面示例。 |
| longpress | 组件被长按时触发，使用方法与click相同。 |
| swipe | 组件上快速滑动时触发，使用方法参见应用退出章节。 |

以<input>组件的onclick事件为例，介绍事件的使用方法。首先，在index.hml文件中添加一个<input>组件，添加后的代码示例如下：

```
1. <!-- index.hml -->
2. <div class="container">
3. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
4. Hello World
5. </text>
6. <input type="button" value="Change" style="width: 200px; height: 50px;" onclick="clickAction"></input>
7. </div>
```

[event.hml](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/event/event.hml#L2-L8)

在以上代码中，页面里添加了一个<input>组件，包含了onclick事件及其处理函数。clickAction()是一个JavaScript函数，点击按钮改变字体的大小和颜色。它的实现在pages/index/index.js文件中，示例代码如下：

```
1. // index.js:
2. export default {
3. data: {
4. fontSize: '30px',
5. fontColor: '#FF0000',
6. },
7. clickAction() {
8. this.fontSize = '38px';
9. this.fontColor = '#FFFFFF';
10. }
11. };
```

[event.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/event/event.js#L2-L12)

### 表冠事件

轻量级智能穿戴的表冠，旋转操作可触发实时交互响应。目前支持旋转表冠的组件有list，slider，swiper。

表冠事件的适配需要如下操作：

1. 页面启动时，在onShow()生命周期激活焦点。
2. 指定一个组件获焦（仅支持list，slider，swiper）。
3. 在需要页面切换时或不需要使用时释放焦点。

具体开发步骤可参考开发[示例](../harmonyos-references/js-lite-components-container-list.md#示例)。

## 页面路由

应用通常由多个页面组成，需要页面路由来实现页面间的跳转。页面路由router根据uri的地址来找到目标页面，实现跳转。下面以两个简单页面之间的跳转为例说明页面跳转的操作，具体实现步骤如下：

1. 在“pages”目录右键，选择“New > Page”，将“Page name”设置为“details”。如果使用其他方式添加页面，则在添加页面后需要修改配置文件config.json中的pages标签。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/RJiSwKXcQmyd3P6u8bgzzw/zh-cn_image_0000002266037277.png?HW-CC-KV=V1&HW-CC-Date=20260429T061301Z&HW-CC-Expire=86400&HW-CC-Sign=950FFB226AFBFD5841B20D9C0C463295DF4E04CE4933EBC4F21B20D18D1DCDD6 "点击放大")
2. 在index.hml页面添加一个文本和一个按钮，文本通过用来指明当前页面，按钮绑定clickAction()方法，用来实现两个页面之间的相互跳转。

   ```
   1. <!-- index.hml -->
   2. <div class="container">
   3. <text class="title">
   4. Hello World
   5. </text>
   6. <input class="btn" type="button" value="View" onclick="clickAction"></input>
   7. </div>
   ```

   [detail.hml](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/detail/detail.hml#L2-L8)
3. 在details.hml页面添加一个文本和一个按钮，按钮绑定clickAction()方法。

   ```
   1. <!-- details.hml -->
   2. <div class="container">
   3. <text class="title">
   4. Details Page
   5. </text>
   6. <input class="btn" type="button" value="Back" onclick="clickAction"></input>
   7. </div>
   ```

   [details.hml](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/details/details.hml#L2-L8)
4. 在index.js文件中实现clickAction()方法，调用router.replaceUrl()函数跳转到详情页。

   ```
   1. import router from '@ohos.router';

   3. // index.js
   4. export default {
   5. clickAction() {
   6. router.replaceUrl({
   7. uri: 'pages/details/details'
   8. });
   9. }
   10. };
   ```

   [detail.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/detail/detail.js#L2-L11)
5. 在details.js文件中实现clickAction()方法点击按钮调用router.replaceUrl()回到首页。

   ```
   1. import router from '@ohos.router';

   3. // details.js
   4. export default {
   5. clickAction() {
   6. router.replaceUrl({
   7. uri: 'pages/index/index'
   8. });
   9. }
   10. };
   ```

   [details.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/details/details.js#L2-L11)
6. 使用Preview预览效果，详情请参考[查看ArkTS/JS预览效果](../harmonyos-guides/ide-previewer-arkts-js.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/nIwV-iDjSHqMkEXpewqceA/zh-cn_image_0000002265917341.png?HW-CC-KV=V1&HW-CC-Date=20260429T061301Z&HW-CC-Expire=86400&HW-CC-Sign=14A61605CA745209255D4DC0C90832C26E25114BDB78C25C54BF0E4E2908E3AC)

## 应用退出

应用退出除使用物理按键触发外，还可以通过组件的事件触发。本章节以右滑表盘退出为例，讲解实现应用退出的方式。

1. 在index.hml页面的最外层父容器中绑定onswipe事件，当页面右滑的时候会触发onswipe事件绑定的函数。示例代码如下：

   ```
   1. <!-- index.hml: Binding swipe event to div element -->
   2. <div class="container" onswipe="touchMove">
   3. <text id="title">
   4. Hello {{ title }}
   5. </text>
   6. <input type="button" value="View" style="width: 200px; height: 50px;" onclick="clickAction"></input>
   7. </div>
   ```

   [exit.hml](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/exit/exit.hml#L2-L8)
2. 在index.js文件中实现touchMove()方法，调用app模块的terminate()方法实现应用退出。因为swipe是有方向属性的，在事件函数处理中要注意判断方向，否则任意方向的滑动都会触发退出应用操作，示例代码如下：

   ```
   1. // index.js
   2. import router from '@ohos.router';
   3. // Import the app module.
   4. import app from '@system.app';

   6. export default {
   7. data: {
   8. title: 'World'
   9. },
   10. clickAction() {
   11. router.replaceUrl({
   12. uri: 'pages/details/details'
   13. });
   14. },
   15. touchMove(e) { // Handle swipe events.
   16. if (e.direction == 'right') { // Swipe right to exit.
   17. app.terminate();
   18. }
   19. }
   20. };
   ```

   [exit.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/exit/exit.js#L2-L21)

## 应用与页面的生命周期

轻量级智能穿戴应用的生命周期主要有两个：应用创建时会触发app.js文件中的的onCreate()，应用销毁时触发onDestroy()。

一个应用中可能会有多个页面，每个页面都包括onInit()、onReady()、onShow()、onHide()和onDestroy()，在页面初始化、准备、显示、隐藏和销毁时触发调用的事件：

* onInit()：表示页面的数据已经准备好，可以使用js文件中的data数据。
* onReady()：表示页面已经编译完成，可以将界面显示给用户。
* onShow()：方舟开发框架只支持应用同时运行并展示一个页面，当打开一个页面时，上一个页面会被销毁。当一个页面显示的时候，会调用onShow。
* onHide()：页面消失时被调用。
* onDestroy()：页面销毁时被调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/XgAO41ptQKyn2q8qT4f8-g/zh-cn_image_0000002230878016.png?HW-CC-KV=V1&HW-CC-Date=20260429T061301Z&HW-CC-Expire=86400&HW-CC-Sign=DE663C5D625BEE51E6211E895F15748EAC316DDF6D5A2E7A5259B0C32CB39211 "点击放大")

常用场景如下：

* 当应用从页面A跳转到页面B时，首先调用页面A的onDestroy()函数。页面A销毁后，依次调用页面B的onInit()、onReady()、onShow()函数来初始化和显示页面B。
* 应用不具备后台运行能力，当用户执行返回系统桌面操作时，应用进程将被销毁，且会触发应用生命周期的onDestroy()回调。
* 系统暂未开放熄屏动作的监听接口，应用无法注册熄屏相关的监听回调。

## 百分比使用

说明

从API Version 5 开始支持。

绘制样式中的部分字段（width，height，margin，top，left）支持使用百分比设置，通过指定百分比，应用在运行时可以自动换算成真实像素值。百分比可以在一定程度上帮助应用进行显示自适应，在不同尺寸的屏幕上显示尽可能做到一致或合理的布局。本章节将介绍百分比在绘制样式中具体的使用。

1. 在index.hml首页中定义一个div容器，在容器内添加一个包含按钮的stack容器和另一个按钮。

   ```
   1. <!-- index.hml -->
   2. <div class="container">
   3. <stack class="stackContainer">
   4. <input class="button" type="button" value="Button"></input>
   5. </stack>
   6. <input class="button2" type="button" value="Exit"></input>
   7. </div>
   ```

   [index.hml](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/pages/index/index.hml#L2-L8)
2. 在index.css文件中，对container的class，设置width和height为100%，设置背景色为碧绿色，效果将覆盖整个屏幕。

   ```
   1. /* index.css */
   2. .container {
   3. width: 100%;   /* The width of the container is set to 100%. */
   4. height: 100%;  /* The height of the container is set to 100%. */
   5. justify-content: center;
   6. align-items: center;
   7. flex-direction: column;
   8. background-color: aquamarine;  /* Set the background color to light green. */
   9. }
   ```
3. 在index.css文件中，对stackContainer的class，设置width和height为50%，背景色为白色，stack容器的宽高则均为父组件的一半。对button的class，设置width为父组件（stack容器）宽度的50%，height为stack容器高度的30%，top距离顶部为stack容器高度的10%，left距离左侧为stack容器宽度的10%；对button2的class，设置width为父组件（div容器）宽度的50%，height为div容器高度的20%，margin-top上方距离stack容器为div容器高度的2%。

   ```
   1. /* index.css */
   2. .stackContainer {
   3. width: 50%;
   4. height: 50%;
   5. background-color: white;
   6. }

   8. .button {
   9. top: 10%;   /* Set the position on the y-axis to be 10% of the height of the parent component from the top. */
   10. left: 10%;  /* Set the position on the x-axis to be 10% of the width of the parent component from the parent component itself. */
   11. width: 50%;
   12. height: 30%;
   13. font-size: 30px;
   14. background-color: black;
   15. }

   18. .button2 {
   19. width: 50%;
   20. height: 20%;
   21. font-size: 30px;
   22. background-color: black;
   23. margin-top: 2%;  /* 2% of the height of the parent component. */
   24. }
   ```
4. 在preview中预览在轻量级智能穿戴上的显示效果，如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/jcXqVUkSSYuoYg756djK5g/zh-cn_image_0000002231037836.png?HW-CC-KV=V1&HW-CC-Date=20260429T061301Z&HW-CC-Expire=86400&HW-CC-Sign=515B5F28184DA51DA35400307A10E602DFA4DA513BFD9F0DBD5A216C1923E2C5 "点击放大")

说明

百分比计算会通过浮点数计算后保留整数部分。

## 方表适配

应用如果需要同时适配方形的轻量级智能穿戴设备，需要完成以下步骤。

1. 在DevEco Studio中右键工程目录，选择“New -> Module ”，创建新的“Empty Ability”，将已有entry的内容拷贝至新建的entry，并修改Module的Name。
2. 打开新建entry的config.json文件，修改deviceType为liteWearable，并添加distroFilter属性如下：（以方表分辨率408\*480为例）

   ```
   1. {
   2. // ...
   3. "module": {
   4. "deviceType": [
   5. "liteWearable"
   6. ],
   7. "distro": {
   8. "deliveryWithInstall": true
   9. "moduleName": "entry",
   10. "moduleType": "entry"
   11. },
   12. "distroFilter": {
   13. "screenShape": {
   14. "policy": "include",
   15. "value": [
   16. "rect"
   17. ]
   18. },
   19. "screenWindow": {
   20. "policy": "include",
   21. "value": [
   22. "408*480"
   23. ]
   24. }
   25. },
   26. // ...
   27. }
   28. }
   ```
3. 参考绘制样式章节，将方表对应的页面布局参数修改为408\*480或百分比。修改完成后，点击“File -> Sync And Refresh Project”重新同步工程。

   说明

   应用上架时，应用市场会根据“distroFilter”属性对方形和圆形的轻量级智能穿戴进行分发。

## 多语言适配

轻量级智能穿戴应用开发时可以通过配置语言资源文件，无需开发多个不同语言的版本，就可以同时支持多种语言的切换，为项目维护带来便利。

1. 多语言资源文件放在[文件组织](../harmonyos-guides/js-framework-file.md)中指定的i18n文件夹内，命名规则为：语言-国家/地区.json，如zh-CN.json为简体中文，en-US.json为英文。限制词取值要求可参考[定义资源文件](../harmonyos-guides/js-framework-multiple-languages.md#定义资源文件)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/vvkSNxnsSHOfJhvv2SbJ_Q/zh-cn_image_0000002505798198.png?HW-CC-KV=V1&HW-CC-Date=20260429T061301Z&HW-CC-Expire=86400&HW-CC-Sign=C30C5A21F3A47ACB34DF4849B3BCEF198B0A107BC8A9C13E1B61151981CA2043)

   说明

   * 应用进行印度尼西亚语言适配时，需要添加两个语言资源文件in-ID.json和id-ID.json并配置，如上图所示。
   * 轻量级智能穿戴设备只支持语言-国家/地区配置方式。
   * 切换语言时，需在与手表配对的手机上同步调整语言和地区设置。例如，若要使用繁体中文，请将手机语言设为“繁体中文”，地区设为“中国香港”，并配置zh-HK.json文件。
2. 创建语言资源文件后，在配置文件中配置索引和语言的映射关系，格式为："key值索引": "语言文本"，如下所示。

   ```
   1. {
   2. "strings": {
   3. "hello": "Hello",
   4. "world": "World"
   5. }
   6. }
   ```
3. 配置好语言资源文件后，可在hml文件或js文件中使用$t方法引用资源，详细请参考[引用资源](../harmonyos-guides/js-framework-multiple-languages.md#引用资源)中的简单格式化方法。

## 安全接口的使用

轻量级智能穿戴设备应用开发的安全相关接口，包含通用密钥库系统、加解密算法库框架和锁屏管理。

说明

轻量级智能穿戴设备目前不支持异步接口，所有异步接口会等待回调函数执行完成，再执行下一行代码。本章节所有异步接口可理解为同步接口。

### @ohos.security.huks（通用密钥库系统）

通用密钥库系统提供的接口，包含常见的对称加密算法、常见的非对称加密算法、常见的消息认证码（MAC）算法和公共接口。

**常见的对称加密算法**如下表所示：

| 算法类型 | 算法 | 用法 | 分组模式 | 填充模式 | 密钥长度 |
| --- | --- | --- | --- | --- | --- |
| 对称算法 | AES | 密钥生成、加密、解密 | CBC | NoPadding | 128/192/256 |
| ECB | NoPadding | 128/192/256 |
| GCM | NoPadding | 128/192/256 |
| DES | 密钥生成、加密、解密 | CBC | NoPadding | 64 |
| ECB | NoPadding | 64 |
| 3DES | 密钥生成、加密、解密 | CBC | NoPadding | 128/192 |
| ECB | NoPadding | 128/192 |

DES加密算法是一种对称加密算法，支持按照CBC/ECB 两种分组模式，填充模式为NoPadding，密钥长度为64位。下文以DES算法CBC分组模式为例，介绍在轻量级穿戴设备应用中实现密钥生成、加密和解密。

1. 生成DES-CBC算法密钥：定义一个 getDesCBCEncryptProperties()的函数，用于生成一个包含 DES-CBC加密算法相关属性的数组。这些属性用于配置加密操作的参数，并在generateDESKey()方法中生成密钥。

   ```
   1. import huks from '@ohos.security.huks';

   3. // Alias, used to distinguish the generated KEY.
   4. const DES_CBC_64_KEY_ALIAS = 'DesCBC64KeyAlias';
   5. // ...

   7. // Configure the Tag required for generating the key.
   8. function getDesGenProperties() {
   9. let properties = new Array();
   10. let index = 0;
   11. // DES algorithm.
   12. properties[index++] = {
   13. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   14. value: huks.HuksKeyAlg.HUKS_ALG_DES
   15. };
   16. // Key length: 64.
   17. properties[index++] = {
   18. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   19. value: huks.HuksKeySize.HUKS_DES_KEY_SIZE_64
   20. };
   21. // Key usage, encryption and decryption.
   22. properties[index++] = {
   23. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   24. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
   25. };

   27. return properties;
   28. }

   30. // Generate a key.
   31. function generateDESKey() {
   32. let huksInfo;
   33. let options = { properties: getDesGenProperties() }
   34. huks.generateKeyItem(DES_CBC_64_KEY_ALIAS, options, (err, data) => {
   35. if (err) {
   36. huksInfo = 'generateKeyDES return code:' + err.code + ' ： ' + err.message;
   37. } else {
   38. huksInfo = 'The key has been generated:' + JSON.stringify(data);
   39. }
   40. });
   41. return huksInfo;
   42. }
   ```

   [DES.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/DES.js#L2-L56)
2. 使用DES-CBC算法进行加密：调用huks.initSession()初始化加密会话，并设置相关属性；调用huks.updateSession()处理明文的前16个字符；调用huks.finishSession()处理明文的剩余16个字符，并完成加密。

   ```
   1. // Alias, used to distinguish the generated KEY.
   2. const DES_CBC_64_KEY_ALIAS = 'DesCBC64KeyAlias';
   3. // Three-part handle, used for connecting three-part context.
   4. let handle;
   5. let IV = '12345678';
   6. // Plain text, data before encryption.
   7. let plainText = 'DESAAAdffssghCBC5612345612345L64';
   8. // Ciphertext, storing the encrypted data.
   9. let cipherText = '';

   11. // ...
   12. function getDesCBCEncryptProperties() {
   13. let properties = new Array();
   14. let index = 0;
   15. // algorithm.
   16. properties[index++] = {
   17. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   18. value: huks.HuksKeyAlg.HUKS_ALG_DES
   19. };

   21. // key length.
   22. properties[index++] = {
   23. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   24. value: huks.HuksKeySize.HUKS_DES_KEY_SIZE_64
   25. };

   27. // Key usage.
   28. properties[index++] = {
   29. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   30. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
   31. };

   33. // Filling method.
   34. properties[index++] = {
   35. tag: huks.HuksTag.HUKS_TAG_PADDING,
   36. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
   37. };

   39. // packet mode.
   40. properties[index++] = {
   41. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
   42. value: huks.HuksCipherMode.HUKS_MODE_CBC
   43. };

   45. // Group encryption offset vector, more secure.
   46. properties[index++] = {
   47. tag: huks.HuksTag.HUKS_TAG_IV,
   48. value: stringToUint8Array(IV)
   49. };

   51. return properties;
   52. }

   54. function encryptDES() {
   55. let huksInfo;
   56. let ret = true;
   57. let initOptions = {
   58. properties: getDesCBCEncryptProperties(),
   59. inData: new Uint8Array()
   60. }

   62. let updateOptions = {
   63. properties: getDesCBCEncryptProperties(),
   64. inData: stringToUint8Array(plainText.substring(0, 16))
   65. }

   67. let finishOptions = {
   68. properties: getDesCBCEncryptProperties(),
   69. inData: stringToUint8Array(plainText.substring(16, 32))
   70. }

   72. huks.initSession(DES_CBC_64_KEY_ALIAS, initOptions, (initErr, initData) => {
   73. if (initErr) {
   74. huksInfo = 'encryptDES initSession return code:' + initErr.code + ' ： ' + initErr.message;
   75. ret = false;
   76. huks.abortSession(initData.handle, initOptions, (abortErr, abortData) => {
   77. if (abortErr) {
   78. huksInfo = 'encryptDES init abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   79. }
   80. });
   81. } else {
   82. handle = initData.handle;
   83. }
   84. });

   86. if (!ret) {
   87. return huksInfo;
   88. }

   90. huks.updateSession(handle, updateOptions, (updateErr, updateData) => {
   91. if (updateErr) {
   92. huksInfo = 'encryptDES updateSession return code:' + updateErr.code + ' ： ' + updateErr.message;
   93. ret = false;
   94. huks.abortSession(handle, updateOptions, (abortErr, abortData) => {
   95. if (abortErr) {
   96. huksInfo = 'encryptDES update abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   97. }
   98. });
   99. } else {
   100. // Encrypted message reception
   101. cipherText = uint8ArrayToString(updateData.outData);
   102. huksInfo = cipherText
   103. }
   104. });
   105. if (!ret) {
   106. return huksInfo;
   107. }

   109. huks.finishSession(handle, finishOptions, (finishErr, finishData) => {
   110. if (finishErr) {
   111. ret = false;
   112. huksInfo = 'encryptDES finishSession return code:' + finishErr.code + ' ： ' + finishErr.message;
   113. huks.abortSession(handle, finishOptions, (abortErr, abortData) => {
   114. if (abortErr) {
   115. huksInfo =
   116. 'encryptDES finish  abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   117. }
   118. });
   119. } else {
   120. // Encrypted message reception
   121. cipherText = cipherText + uint8ArrayToString(finishData.outData);
   122. huksInfo = cipherText
   123. }
   124. });

   126. return huksInfo;
   127. }
   128. function stringToUint8Array(str) {
   129. let arr = [];
   130. for (let i = 0, j = str.length; i < j; ++i) {
   131. arr.push(str.charCodeAt(i));
   132. }

   134. return new Uint8Array(arr);
   135. }

   137. function uint8ArrayToString(fileData) {
   138. let dataString = '';
   139. for (let i = 0; i < fileData.length; i++) {
   140. dataString += String.fromCharCode(fileData[i]);
   141. }

   143. return dataString;
   144. }
   ```

   [DES.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/DES.js#L5-L191)
3. 使用DES-CBC算法进行解密：调用huks.initSession()初始化解密会话；调用huks.updateSession()处理密文的前16个字节，并将解密后的数据转换为字符串存储在outPlainText中；调用huks.finishSession()处理密文的剩余16个字节，并将解密后的数据追加到outPlainText中。

   ```
   1. // Alias, used to distinguish the generated KEY.
   2. const DES_CBC_64_KEY_ALIAS = 'DesCBC64KeyAlias';
   3. // Three-part handle, used for connecting three-part context.
   4. let handle;
   5. let IV = '12345678';
   6. // Plain text, data before encryption.
   7. let plainText = 'DESAAAdffssghCBC5612345612345L64';
   8. // Ciphertext, storing the encrypted data.
   9. let cipherText = '';

   11. // ...
   12. function stringToUint8Array(str) {
   13. let arr = [];
   14. for (let i = 0, j = str.length; i < j; ++i) {
   15. arr.push(str.charCodeAt(i));
   16. }

   18. return new Uint8Array(arr);
   19. }

   21. function uint8ArrayToString(fileData) {
   22. let dataString = '';
   23. for (let i = 0; i < fileData.length; i++) {
   24. dataString += String.fromCharCode(fileData[i]);
   25. }

   27. return dataString;
   28. }

   30. function GetDesCBCDecryptProperties() {
   31. let properties = new Array();
   32. let index = 0;
   33. // algorithm
   34. properties[index++] = {
   35. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   36. value: huks.HuksKeyAlg.HUKS_ALG_DES
   37. };
   38. // key length
   39. properties[index++] = {
   40. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   41. value: huks.HuksKeySize.HUKS_DES_KEY_SIZE_64
   42. };
   43. // Key usage
   44. properties[index++] = {
   45. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   46. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
   47. };
   48. // Filling method
   49. properties[index++] = {
   50. tag: huks.HuksTag.HUKS_TAG_PADDING,
   51. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
   52. };
   53. // packet mode
   54. properties[index++] = {
   55. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
   56. value: huks.HuksCipherMode.HUKS_MODE_CBC
   57. };
   58. // Group encryption offset vector, more secure
   59. properties[index++] = {
   60. tag: huks.HuksTag.HUKS_TAG_IV,
   61. value: stringToUint8Array(IV)
   62. };
   63. return properties;
   64. }

   66. function decryptDES() {
   67. let huksInfo;
   68. let ret = true;
   69. let outPlainText;
   70. let initOptions = {
   71. properties: GetDesCBCDecryptProperties(),
   72. inData: new Uint8Array()
   73. }
   74. let updateOptions = {
   75. properties: GetDesCBCDecryptProperties(),
   76. inData: stringToUint8Array(cipherText.substring(0, 16))
   77. }

   79. let finishOptions = {
   80. properties: GetDesCBCDecryptProperties(),
   81. inData: stringToUint8Array(cipherText.substring(16, 32))
   82. }

   84. huks.initSession(DES_CBC_64_KEY_ALIAS, initOptions, (initErr, initData) => {
   85. if (initErr) {
   86. ret = false;
   87. huksInfo = 'decryptDES initSession return code:' + initErr.code + ' ： ' + initErr.message;
   88. huks.abortSession(initData.handle, initOptions, (abortErr, abortData) => {
   89. if (abortErr) {
   90. huksInfo =
   91. 'decryptDES initSession abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   92. }
   93. });
   94. } else {
   95. handle = initData.handle;
   96. }
   97. });

   99. if (!ret) {
   100. return huksInfo;
   101. }

   103. huks.updateSession(handle, updateOptions, (updateErr, updateData) => {
   104. if (updateErr) {
   105. ret = false;
   106. huksInfo = 'decryptDES updateSession return code:' + updateErr.code + ' ： ' + updateErr.message;
   107. huks.abortSession(handle, updateOptions, (abortErr, abortData) => {
   108. if (abortErr) {
   109. huksInfo = 'decryptDES update abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   110. }
   111. });
   112. } else {
   113. // Clear text reception
   114. outPlainText = uint8ArrayToString(updateData.outData);
   115. huksInfo = outPlainText;
   116. }
   117. });

   119. if (!ret) {
   120. return huksInfo;
   121. }

   123. huks.finishSession(handle, finishOptions, (finishErr, finishData) => {
   124. if (finishErr) {
   125. ret = false;
   126. huksInfo = 'decryptDES finishSession return code:' + finishErr.code + ' ： ' + finishErr.message;
   127. huks.abortSession(handle, finishOptions, (abortErr, abortData) => {
   128. if (abortErr) {
   129. huksInfo = 'decryptDES abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   130. }
   131. });
   132. } else {
   133. // Clear text reception
   134. outPlainText = outPlainText + uint8ArrayToString(finishData.outData);
   135. huksInfo = outPlainText;
   136. }
   137. });

   139. return huksInfo;
   140. }
   ```

   [DES.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/DES.js#L6-L305)

**常见的非对称加密算法**如下表所示：

| 算法类型 | 算法 | 用法 | 分组模式 | 摘要模式 | 填充模式 | 密钥长度 | 标准 | 开闭源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 非对称算法 | RSA | 密钥生成、加密、解密 | ECB |  | NoPadding | [1024,2048] | RFC | 开源 |
| ECB |  | PKCS#1 V1.5 | [1024,2048] | RFC | 开源 |
| ECB | SHA256 | OAEP | [1024,2048] | RFC | 开源 |
| 密钥生成、签名、验签 |  | SHA256 | PKCS#1 V1.5 | [1024,2048] | RFC | 开源 |
|  | SHA256 | PSS | [1024,2048] | RFC | 开源 |
|  | SHA1 | ISO/IEC 9796-2 | [1024,2048] | ISO-9796 | 闭源 |

RSA加密算法是一种非对称加密算法，支持密钥对生成、加解密、签名和验签操作。RSA的填充模式通常为PKCS#1 V1.5或OAEP，密钥长度通常为1024位、2048位，密钥长度越长，安全性越高，但计算开销也越大。下文以RSA算法、填充模式PKCS#1 V1.5为例，介绍在轻量级穿戴设备应用中实现密钥对生成、加解密、签名和验签。

1. 生成RSA算法密钥：定义一个 getRSAGenProperties()的函数，用于生成一个包含 RSA加密算法相关属性的数组。这些属性用于配置加密操作的参数，并在generateRSAKey()方法中生成密钥。

   ```
   1. import huks from '@ohos.security.huks';

   3. // Alias, used to distinguish the generated KEY.
   4. const RSA_KEY_ALIAS = 'RSAKeyAlias';
   5. // The custom key length must be between 1024 and 2048, and it must be a multiple of 8.
   6. const HUKS_RSA_KEY_SIZE_1024 = 1024;
   7. // ...
   8. function getRSAGenProperties() {
   9. let properties = new Array();
   10. let index = 0;
   11. // algorithm.
   12. properties[index++] = {
   13. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   14. value: huks.HuksKeyAlg.HUKS_ALG_RSA
   15. };
   16. // key length.
   17. properties[index++] = {
   18. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   19. value: HUKS_RSA_KEY_SIZE_1024
   20. };
   21. // Key usage.
   22. properties[index++] = {
   23. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   24. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
   25. };
   26. return properties;
   27. }

   29. function generateRSAKey() {
   30. let huksInfo;
   31. let options = { properties: getRSAGenProperties() };
   32. huks.generateKeyItem(HUKS_RSA_KEY_SIZE_1024, options, (err, data) => {
   33. if (err) {
   34. huksInfo = 'generateRSAKey return code:' + err.code + ' ： ' + err.message;
   35. } else {
   36. huksInfo = 'The key has been generated:' + JSON.stringify(data);
   37. }
   38. });
   39. return huksInfo;
   40. }
   ```

   [RSA.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/RSA.js#L2-L56)
2. 使用RSA算法进行加密：调用huks.initSession()初始化加密会话，并设置相关属性；调用huks.updateSession()对明文的前半部分进行加密；调用huks.finishSession()对明文的后半部分进行加密，并获取最终的密文。

   ```
   1. // Alias, used to distinguish the generated KEY.
   2. const RSA_KEY_ALIAS = 'RSAKeyAlias';
   3. // The custom key length must be between 1024 and 2048, and it must be a multiple of 8.
   4. const HUKS_RSA_KEY_SIZE_1024 = 1024;
   5. // Plain text, data before encryption.
   6. let plainText = 'RSASSAdffssghCBC5612345612345192';
   7. // Plain text, the length of the data before encryption.
   8. let plainTextLen = 32;
   9. // Ciphertext, storing the encrypted data.
   10. let cipherText = '';
   11. // Operation handle.
   12. let handle;

   14. // ...
   15. function getRSAEncryptProperties() {
   16. let properties = new Array();
   17. let index = 0;
   18. // algorithm.
   19. properties[index++] = {
   20. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   21. value: huks.HuksKeyAlg.HUKS_ALG_RSA
   22. };
   23. // key length.
   24. properties[index++] = {
   25. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   26. value: HUKS_RSA_KEY_SIZE_1024
   27. };

   29. // Key usage.
   30. properties[index++] = {
   31. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   32. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
   33. };
   34. // Key PADDING method.
   35. properties[index++] = {
   36. tag: huks.HuksTag.HUKS_TAG_PADDING,
   37. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
   38. };
   39. properties[index++] = {
   40. tag: huks.HuksTag.HUKS_TAG_DIGEST,
   41. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
   42. }
   43. return properties;
   44. }

   46. function encryptProcess() {
   47. let ret = true;
   48. let huksInfo;
   49. let initOptions = {
   50. properties: getRSAEncryptProperties(),
   51. inData: new Uint8Array()
   52. }
   53. let updateOptions = {
   54. properties: getRSAEncryptProperties(),
   55. inData: stringToUint8Array(plainText.substring(0, plainTextLen / 2))
   56. }
   57. let finishOptions = {
   58. properties: getRSAEncryptProperties(),
   59. inData: stringToUint8Array(plainText.substring(plainTextLen / 2, plainTextLen))
   60. }
   61. huks.initSession(RSA_KEY_ALIAS, initOptions, (initErr, initData) => {
   62. if (initErr) {
   63. huksInfo = 'encryptProcess initSession return code:' + initErr.code + ' ： ' + initErr.message;
   64. ret = false;
   65. huks.abortSession(initData.handle, initOptions, (abortErr, abortData) => {
   66. if (abortErr) {
   67. huksInfo =
   68. 'encryptProcess init abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   69. }
   70. });
   71. } else {
   72. handle = initData.handle;
   73. }
   74. });
   75. if (!ret) {
   76. return huksInfo;
   77. }

   79. huks.updateSession(handle, updateOptions, (updateErr, updateData) => {
   80. if (updateErr) {
   81. huksInfo = 'encryptProcess updateSession return code:' + updateErr.code + ' ： ' + updateErr.message;
   82. ret = false;
   83. huks.abortSession(handle, updateOptions, (abortErr, abortData) => {
   84. if (abortErr) {
   85. huksInfo = 'encryptProcess updateSession abortSession return code:' + abortErr.code + ' ： ' +
   86. abortErr.message;
   87. }
   88. });
   89. }
   90. });

   92. if (!ret) {
   93. return huksInfo;
   94. }

   96. huks.finishSession(handle, finishOptions, (finishErr, finishData) => {
   97. if (finishErr) {
   98. ret = false;
   99. huksInfo = 'encryptProcess finishSession return code:' + finishErr.code + ' ： ' + finishErr.message;
   100. huks.abortSession(handle, finishOptions, (abortErr, abortData) => {
   101. if (abortErr) {
   102. huksInfo =
   103. 'encryptProcess finish  abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   104. }
   105. });
   106. } else {
   107. // Encrypted message reception.
   108. cipherText = uint8ArrayToString(finishData.outData);
   109. huksInfo = cipherText;
   110. }
   111. });
   112. return huksInfo;
   113. }

   115. function uint8ArrayToString(fileData) {
   116. let dataString = '';
   117. for (let i = 0; i < fileData.length; i++) {
   118. dataString += String.fromCharCode(fileData[i]);
   119. }
   120. return dataString;
   121. }

   123. function stringToUint8Array(str) {
   124. let arr = [];
   125. for (let i = 0, j = str.length; i < j; ++i) {
   126. arr.push(str.charCodeAt(i));
   127. }
   128. return new Uint8Array(arr);
   129. }
   ```

   [RSA.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/RSA.js#L6-L174)
3. 使用RSA算法进行解密：调用huks.getRSADecryptProperties()设置RSA算法的秘钥长度、填充模式、摘要算法等属性；调用huks.initSession()初始化解密会话；调用huks.updateSession()处理密文的前半部分，并将解密后的数据转换为字符串存储在outPlainText中；调用huks.finishSession()处理密文的后半部分，并将解密后的数据追加到outPlainText中。

   ```
   1. import huks from '@ohos.security.huks';

   3. // Alias, used to distinguish the generated KEY.
   4. const RSA_KEY_ALIAS = 'RSAKeyAlias';
   5. // The custom key length must be between 1024 and 2048, and it must be a multiple of 8.
   6. const HUKS_RSA_KEY_SIZE_1024 = 1024;
   7. // Plain text, data before encryption.
   8. let plainText = 'RSASSAdffssghCBC5612345612345192';
   9. // Plain text, the length of the data before encryption.
   10. let plainTextLen = 32;
   11. // Ciphertext, storing the encrypted data.
   12. let cipherText = '';
   13. // Operation handle.
   14. let handle;

   16. // ...
   17. function getRSADecryptProperties() {
   18. let properties = new Array();
   19. let index = 0;
   20. // algorithm.
   21. properties[index++] = {
   22. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   23. value: huks.HuksKeyAlg.HUKS_ALG_RSA
   24. };
   25. // key length.
   26. properties[index++] = {
   27. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   28. value: HUKS_RSA_KEY_SIZE_1024
   29. };

   31. // Key usage.
   32. properties[index++] = {
   33. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   34. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
   35. };

   37. // Key PADDING method.
   38. properties[index++] = {
   39. tag: huks.HuksTag.HUKS_TAG_PADDING,
   40. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
   41. };

   43. // digest algorithm.
   44. properties[index++] = {
   45. tag: huks.HuksTag.HUKS_TAG_DIGEST,
   46. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
   47. }

   49. return properties;
   50. }

   52. function decryptProcess() {
   53. // Length of encrypted ciphertext.
   54. let len = HUKS_RSA_KEY_SIZE_1024 / 8;
   55. let ret = true;
   56. let outPlainText;
   57. let huksInfo;
   58. let initOptions = {
   59. properties: getRSADecryptProperties(),
   60. inData: new Uint8Array()
   61. }
   62. let updateOptions = {
   63. properties: getRSADecryptProperties(),
   64. inData: stringToUint8Array(cipherText.substring(0, len / 2))
   65. }
   66. let finishOptions = {
   67. properties: getRSADecryptProperties(),
   68. inData: stringToUint8Array(cipherText.substring(len / 2, len))
   69. }
   70. huks.initSession(RSA_KEY_ALIAS, initOptions, (initErr, initData) => {
   71. if (initErr) {
   72. huksInfo = 'decryptProcess initSession return code:' + initErr.code + ' ： ' + initErr.message;
   73. ret = false;
   74. huks.abortSession(initData.handle, initOptions, (abortErr, abortData) => {
   75. if (abortErr) {
   76. huksInfo =
   77. 'decryptProcess init abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   78. }
   79. });
   80. } else {
   81. handle = initData.handle;
   82. }
   83. });
   84. if (!ret) {
   85. return huksInfo;
   86. }
   87. huks.updateSession(handle, updateOptions, (updateErr, updateData) => {
   88. if (updateErr) {
   89. huksInfo = 'decryptProcess updateSession return code:' + updateErr.code + ' ： ' + updateErr.message;
   90. ret = false;
   91. huks.abortSession(handle, updateOptions, (abortErr, abortData) => {
   92. if (abortErr) {
   93. huksInfo = 'decryptProcess updateSession abortSession return code:' + abortErr.code + ' ： ' +
   94. abortErr.message;
   95. }
   96. });
   97. }
   98. });

   100. if (!ret) {
   101. return huksInfo;
   102. }
   103. huks.finishSession(handle, finishOptions, (finishErr, finishData) => {
   104. if (finishErr) {
   105. ret = false;
   106. huksInfo = 'decryptProcess finishSession return code:' + finishErr.code + ' ： ' + finishErr.message;
   107. huks.abortSession(handle, finishOptions, (abortErr, abortData) => {
   108. if (abortErr) {
   109. huksInfo =
   110. 'decryptProcess finish  abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   111. }
   112. });
   113. } else {
   114. // Clear text reception.
   115. outPlainText = uint8ArrayToString(finishData.outData);
   116. }
   117. });
   118. if (!ret) {
   119. return huksInfo;
   120. } else {
   121. huksInfo = 'Success:' + outPlainText;
   122. }
   123. return huksInfo;
   124. }
   ```

   [RSA.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/RSA.js#L3-L285)

**常见的消息认证码（MAC）算法**如下：

| 算法类型 | 算法 | 用途 | 分组模式 | 填充模式 | 密钥长度 | 标准 | 开闭源 | 摘要算法 | 加密算法 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 消息认证码（MAC）算法 | CMAC | MAC | CBC | ISO/IEC-9797\_1 | 128 | ISO-9797 | 闭源 |  | 3DES |
| HMAC | MAC |  |  | 按照现有密钥规格 | RFC | 开源 | SHA256 |  |

HMAC是基于哈希函数的消息认证码算法，用于验证消息的完整性和真实性。下文将以HMAC为例，介绍消息认证码算法的使用。

1. 生成HMAC密钥：定义一个 getRSAGenProperties()的函数，用于生成一个包含 RSA加密算法相关属性的数组。这些属性用于配置加密操作的参数，并在generateHMACKey()方法中生成密钥。

   ```
   1. import huks from '@ohos.security.huks';

   3. // HMACKeyAlias - Alias used to distinguish the generated KEY.
   4. const HMAC_KEY_ALIAS = 'HMACKeyAlias';
   5. // ...
   6. function getHMACGenProperties() {
   7. let properties = new Array();
   8. let index = 0;
   9. // algorithm
   10. properties[index++] = {
   11. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   12. value: huks.HuksKeyAlg.HUKS_ALG_AES
   13. };
   14. // key length.
   15. properties[index++] = {
   16. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   17. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
   18. };
   19. // Key usage.
   20. properties[index++] = {
   21. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   22. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
   23. };
   24. return properties;
   25. }

   27. function generateHMACKey() {
   28. let huksInfo;
   29. let options = {
   30. properties: getHMACGenProperties()
   31. }
   32. huks.generateKeyItem(HMAC_KEY_ALIAS, options, (err, data) => {
   33. if (err) {
   34. huksInfo = 'generateKeyHMAC return code:' + err.code + ' ： ' + err.message;
   35. } else {
   36. huksInfo = 'The key has been generated' + JSON.stringify(data);
   37. }
   38. });
   39. return huksInfo;
   40. }
   ```

   [HMAC.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/HMAC.js#L2-L50)
2. 生成HMAC密文：定义getHMACProperties()方法，生成一个包含HMAC操作所需属性的数组，包括HMAC算法、密钥长度、密钥用途和摘要算法；并在HMACProcess()方法中分别调用huks.initSession()、huks.updateSession()、huks.finishSession()生成HMAC密文。

   ```
   1. import huks from '@ohos.security.huks';

   3. // HMACKeyAlias - Alias used to distinguish the generated KEY.
   4. const HMAC_KEY_ALIAS = 'HMACKeyAlias';
   5. // Plain text, data before encryption.
   6. let plainText = 'HMACSAdffssghABC5612345612345192';
   7. // Ciphertext, storing the encrypted data.
   8. let cipherText = '';
   9. // Operation handle.
   10. let handle;
   11. // ...
   12. function uint8ArrayToString(fileData) {
   13. let dataString = '';
   14. for (let i = 0; i < fileData.length; i++) {
   15. dataString += String.fromCharCode(fileData[i]);
   16. }
   17. return dataString;
   18. }

   20. function stringToUnit8Array(str) {
   21. let arr = [];
   22. for (let i = 0, j = str.length; i < j; ++i) {
   23. arr.push(str.charCodeAt(i));
   24. }
   25. return new Uint8Array(arr);
   26. }

   28. function getHMACProperties() {
   29. let properties = new Array();
   30. let index = 0;
   31. // algorithm.
   32. properties[index++] = {
   33. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   34. value: huks.HuksKeyAlg.HUKS_ALG_HMAC
   35. };
   36. // key length.
   37. properties[index++] = {
   38. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   39. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
   40. };
   41. // Key usage.
   42. properties[index++] = {
   43. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   44. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
   45. };
   46. // digest algorithm.
   47. properties[index++] = {
   48. tag: huks.HuksTag.HUKS_TAG_DIGEST,
   49. value: huks.HuksKeyPurpose.HUKS_DIGEST_SHA256
   50. };
   51. return properties;
   52. }

   54. function HMACProcess() {
   55. let huksInfo;
   56. let ret = true;
   57. let initOptions = {
   58. properties: getHMACProperties(),
   59. inData: new Uint8Array()
   60. }
   61. let updateOptions = {
   62. properties: getHMACProperties(),
   63. inData: stringToUnit8Array(plainText.substring(0, 16))
   64. }
   65. let finishOptions = {
   66. properties: getHMACProperties(),
   67. inData: stringToUnit8Array(plainText.substring(16, 32))
   68. }

   70. huks.initSession(HMAC_KEY_ALIAS, initOptions, (initErr, initData) => {
   71. if (initErr) {
   72. huksInfo = 'HMAC initSession return code:' + initErr.code + ' ： ' + initErr.message;
   73. ret = false;
   74. huks.abortSession(initData.handle, initOptions, (abortErr, abortData) => {
   75. if (abortErr) {
   76. huksInfo = 'HMAC init abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   77. }
   78. });
   79. } else {
   80. handle = initData.handle;
   81. }
   82. });
   83. if (!ret) {
   84. return huksInfo;
   85. }

   87. huks.updateSession(handle, updateOptions, (updateErr, updateData) => {
   88. if (updateErr) {
   89. huksInfo = 'HMAC updateSession return code:' + updateErr.code + ' ： ' + updateErr.message;
   90. ret = false;
   91. huks.abortSession(handle, updateOptions, (abortErr, abortData) => {
   92. if (abortErr) {
   93. huksInfo = 'HMAC update abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   94. }
   95. });
   96. }
   97. });

   99. if (!ret) {
   100. return huksInfo;
   101. }

   103. huks.finishSession(handle, finishOptions, (finishErr, finishData) => {
   104. if (finishErr) {
   105. ret = false;
   106. huksInfo = 'encrypt HMAC finishSession return code:' + finishErr.code + ' ： ' + finishErr.message;
   107. huks.abortSession(handle, finishOptions, (abortErr, abortData) => {
   108. if (abortErr) {
   109. huksInfo =
   110. 'encrypt HMAC finish abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
   111. }
   112. });
   113. } else {
   114. // HMAC ciphertext reception.
   115. cipherText = uint8ArrayToString(finishData.outData);
   116. }
   117. });
   118. if (!ret) {
   119. return huksInfo;
   120. } else {
   121. huksInfo = 'success:' + cipherText;
   122. }
   123. return huksInfo;
   124. }
   ```

   [HMAC.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/HMAC.js#L3-L165)

**公共接口**包含导入密钥、导出密钥、查询密钥是否存在和删除密钥。

* 导入密钥

  定义导入密钥的相关配置项，并调用huks.importKeyItem()方法导入密钥。

  ```
  1. import huks from '@ohos.security.huks';

  3. // Key material.
  4. let plainTextKey = new Uint8Array([
  5. 0x1d, 0x2c, 0x3a, 0x4b, 0x5e, 0x6f, 0x7d, 0x8a, 0x9c, 0xab, 0xbc, 0xcd, 0xde, 0xef, 0xf1, 0x23
  6. ]);
  7. // Confirm the key alias.
  8. const KEY_ALIAS = 'keyAlias';

  10. // Package the set of key attributes and key materials.
  11. function getImportKeyProperties() {
  12. let properties = new Array();
  13. let index = 0;
  14. // algorithm.
  15. properties[index++] = {
  16. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  17. value: huks.HuksKeyAlg.HUKS_ALG_AES
  18. };
  19. // Key length (128/192/256).
  20. properties[index++] = {
  21. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
  22. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  23. };
  24. // Key usage: When generating the key,
  25. // using it can limit the usage rights of the key (AES is generally used for encryption and decryption).
  26. properties[index++] = {
  27. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
  28. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  29. };
  30. return properties
  31. }

  33. // Explicitly imported key.
  34. function importKey() {
  35. let huksInfo;
  36. let ret = true;
  37. let options = {
  38. properties: getImportKeyProperties(),
  39. inData: plainTextKey
  40. }
  41. huks.importKeyItem(KEY_ALIAS, options, (initErr, initData) => {
  42. if (initErr) {
  43. ret = false;
  44. huksInfo = 'import key:' + initErr.code + ' ： ' + initErr.message;
  45. huks.abortSession(initData.handle, options, (abortErr, abortData) => {
  46. if (abortErr) {
  47. huksInfo = 'import key init abortSession return code:' + abortErr.code + ' ： ' + abortErr.message;
  48. }
  49. });
  50. } else {
  51. huksInfo = uint8ArrayToString(initData.outData);
  52. }
  53. });

  55. if (!ret) {
  56. return huksInfo + ' import failed';
  57. }

  59. return huksInfo + ' import succeed';
  60. }

  62. function uint8ArrayToString(fileData) {
  63. let dataString = '';
  64. for (let i = 0; i < fileData.length; i++) {
  65. dataString += String.fromCharCode(fileData[i]);
  66. }

  68. return dataString;
  69. }
  ```

  [KeyAlias.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/KeyAlias.js#L2-L74)

* 导出密钥

  ```
  1. import huks from '@ohos.security.huks';

  3. // ...
  4. // Confirm the key alias.
  5. const KEY_ALIAS = 'keyAlias';

  7. // ...
  8. function exportKeyProcess() {
  9. let huksInfo;
  10. let emptyOptions = {
  11. properties: []
  12. }

  14. huks.exportKeyItem(KEY_ALIAS, emptyOptions, (err, data) => {
  15. if (err) {
  16. huksInfo = 'exportKeyItem error return code:' + err.code + ' ： ' + err.message;
  17. } else {
  18. huksInfo = uint8ArrayToString(data.outData);
  19. }
  20. })

  22. return huksInfo;
  23. }
  ```

  [KeyAlias.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/KeyAlias.js#L3-L92)
* 查询密钥是否存在

  调用huks.isKeyItemExist()方法，检查指定别名（KEY\_ALIAS）的密钥项是否存在于密钥管理系统中。

  ```
  1. import huks from '@ohos.security.huks';

  3. const KEY_ALIAS = 'DesCBC64KeyAlias';
  4. function isKeyItemExist() {
  5. let huksInfo;
  6. let emptyOptions = {
  7. properties: []
  8. };

  10. huks.isKeyItemExist(KEY_ALIAS, emptyOptions, (err, data) => {
  11. if (data) {
  12. huksInfo = 'The key:' + KEY_ALIAS + ' exists';
  13. } else {
  14. huksInfo = 'The key doesn\'t exist errcode:' + err.code + ' ： ' + err.message;
  15. }
  16. });

  18. return huksInfo;
  19. }
  ```

  [DesCBC64.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/DesCBC64.js#L2-L22)
* 删除密钥

  调用huks.deleteKeyItem()方法，删除指定别名的密钥。

  ```
  1. import huks from '@ohos.security.huks';

  3. const KEY_ALIAS = 'DesCBC64KeyAlias';
  4. // ...
  5. function deleteKeyProcess() {
  6. let huksInfo;
  7. let emptyOptions = {
  8. properties: []
  9. };
  10. huks.deleteKeyItem(KEY_ALIAS, emptyOptions, (err, data) => {
  11. if (err) {
  12. huksInfo = 'deleteKeyItem error return code:' + err.code + ' ： ' + err.message;
  13. } else {
  14. huksInfo = 'The key has been deleted';
  15. }
  16. })
  17. return huksInfo;
  18. }
  ```

  [DesCBC64.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/security/DesCBC64.js#L3-L38)

### @ohos.security.cryptoFramework (加解密算法库框架)

加解密算法库框架包含消息摘要算法和安全随机数的生成。消息摘要算法是一种能将任意长度的输入消息，通过特定运算生成固定长度摘要的算法；安全随机数能够生成不可预测、均匀分布的随机数，确保系统的安全性和可靠性。

* 消息摘要算法

  首先通过cryptoFramework.createMd()方法创建基于SHA256算法的摘要操作实例，将其赋值给handle；其次调用handle的updateSync()方法，将待摘要的消息转换为Uint8Array后传入，用于更新摘要操作实例中的数据；最后调用handle的digest方法，获取摘要计算的结果，并用handle的getMdLength()方法获取摘要的长度。

  ```
  1. import cryptoFramework from '@ohos.security.cryptoFramework';
  2. // ...
  3. function stringToUint8Array(str) {
  4. let arr = [];
  5. for (let i = 0, j = str.length; i < j; ++i) {
  6. arr.push(str.charCodeAt(i));
  7. }
  8. let tmpUint8Array = new Uint8Array(arr);
  9. return tmpUint8Array;
  10. }

  12. function doMd() {
  13. let mdAlgName = 'SHA256'; // Abstract algorithm name.
  14. let message = 'mdTestMessage'; // The data to be summarized.
  15. let handle;
  16. let mdResult;
  17. let mdLen;
  18. // Specify the digest algorithm SHA256 and generate an instance of the digest operation.
  19. try {
  20. handle = cryptoFramework.createMd(mdAlgName);
  21. } catch (error) {
  22. console.error(`createMd error, code: ${error.code}, msg: ${error.message}`);
  23. }
  24. try {
  25. // When the data volume is small, only one update operation can be performed, and all the data can be sent in.
  26. // The interface does not impose any restrictions on the length of the input parameters.
  27. handle?.updateSync({ data: stringToUint8Array(message) });
  28. } catch (error) {
  29. console.error(`updateSync error, code:+${error.code}, msg: ${error.message}`);
  30. }
  31. // Obtain the summary calculation results.
  32. try {
  33. mdResult = handle?.digest();
  34. } catch (error) {
  35. console.error(`digest error, code: ${error.code}, msg: ${error.message}`);
  36. }
  37. console.info('Md result:' + mdResult?.data);
  38. // Obtain the length of the summary calculation, with the unit being bytes.
  39. try {
  40. mdLen = handle?.getMdLength();
  41. } catch (error) {
  42. console.error(`getMdLength error, code: ${error.code}, msg: ${error.message}`);
  43. }
  44. console.info(`md len: ${mdLen}`);
  45. }
  ```

  [cryptoFramework.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/cryptoFramework/cryptoFramework.js#L2-L55)

  说明

  在同一应用内，开发者应该避免连续多次调用handle.digest()接口，否则会导致不必要的内存开销。
* 安全随机数的生成

  首先调用cryptoFramework.createRandom()方法创建随机数操作实例，并赋值给rand；其次调用rand的setSeed()方法为随机数生成池设置种子（可选）；最后调用rand的generateRandomSync()方法生成指定长度的随机安全数，并将结果赋值给randData。

  ```
  1. function doRand() {
  2. let rand;
  3. let ret = true;
  4. let randData
  5. // Example of generating random numbers operation.
  6. try {
  7. rand = cryptoFramework.createRandom();
  8. } catch (error) {
  9. ret = false;
  10. console.error(`createRandom error, code:+${error.code}, msg: ${error.message}`);
  11. }
  12. let len = 24; // Generate a 24-byte random number.
  13. // (Optional) Call Random.setSeed to set the seed for the random number generation pool.
  14. let seed = new Uint8Array([1, 2, 3]);
  15. try {
  16. rand?.setSeed({ data: seed });
  17. } catch (error) {
  18. ret = false;
  19. console.error(`setSeed error, code:+${error.code}, msg: ${error.message}`);
  20. }

  22. try {
  23. // Generate secure random numbers.
  24. randData = rand?.generateRandomSync(len);
  25. } catch (error) {
  26. ret = false;
  27. console.error(`generateRandomSync error, code:+${error.code}, msg: ${error.message}`);
  28. }
  29. if (ret) {
  30. return randData?.data;
  31. } else {
  32. console.error(`doRand error`);
  33. return 'doRand error';
  34. }
  35. }
  ```

  [cryptoFramework.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/cryptoFramework/cryptoFramework.js#L58-L92)

  说明

  在同一应用内，开发者应该避免连续多次调用rand.generateRandomSync()接口，否则会导致不必要的内存开销。

### @ohos.screenLock (锁屏管理)

锁屏管理服务向三方应用提供解锁屏幕、查询锁屏状态、查询当前锁屏是否安全的能力。

* 解锁屏幕：调用screen.unlockScreen()方法解锁。

  ```
  1. import screenLock from '@ohos.screenLock';

  3. // ...

  5. function unlockScreen() {
  6. let result;
  7. screenLock.unlockScreen((err) => {
  8. if (err) {
  9. result = `Failed to unlock the screen, Code: ${err.code}, ${err.message}`;
  10. } else {
  11. result = `call unlockScreen sucess`;
  12. }
  13. });

  15. return result;
  16. }
  ```

  [screenLock.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/screenLock/screenLock.js#L2-L27)
* 查询锁屏状态：调用screenLock.isScreenLocked()方法查询。

  ```
  1. function isScreenLocked() {
  2. let isLocked = false;
  3. let result;
  4. screenLock.isScreenLocked((err, data) => {
  5. if (err) {
  6. result = `call isScreenLocked erro ${err.message}`;
  7. } else {
  8. isLocked = data
  9. result = `call isScreenLocked sucess islocked: ${isLocked}`
  10. }
  11. });
  12. return result;
  13. }
  ```

  [screenLock.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/screenLock/screenLock.js#L30-L42)
* 查询当前锁屏是否安全：调用screenLock.isSecureMode()方法查询。

  ```
  1. function isSecureMode() {
  2. let result;
  3. let isSafety = false;
  4. screenLock.isSecureMode((err, data) => {
  5. if (err) {
  6. result = `call isSecureMode erro ${err.message}`;
  7. } else {
  8. isSafety = data
  9. result = `call isSecureMode sucess isSafety ${isSafety}`;
  10. }
  11. });
  12. return result;
  13. }
  ```

  [screenLock.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LiteWearable/entry/src/main/js/MainAbility/screenLock/screenLock.js#L45-L57)

## 常见问题

### 轻量级智能穿戴调试问题

问题现象：运动表（如GT/FIT系列）在系统设置中无WiFi调试选项，运动表该如何进行调试

解决方案：

运动表无法通过WiFi进行调试，需要通过**应用调测助手APP**进行调试，具体流程开发者可参考[运行应用](bpta-lite-wearable-guide.md#section489201684214)章节。

### 轻量级智能穿戴网络请求大小限制问题

问题现象：运动表发起fetch请求时，请求失败。

可能原因：

1. WATCH GT5及更早运动表版本与iOS手机配对，无法发起fetch请求。

2. 欧洲地区运动表均无法发起fetch请求。

3. fetch请求携带数据过大，例如 请求头大小超过2KB，或者传输层单包数据超过7KB。

解决方案：

针对原因3，需要减少对应fetch请求数据的大小。

### 轻量级智能穿戴安装app包常见错误

**问题现象****：**运动表安装hap出现的常见问题以及对应的解决方案。

**可能原因：**

1. 错误码40：配置文件格式错误
2. 错误码31：签名验证错误
3. 错误码47：配置文件app.apiVersion字段不合法
4. 错误码34：内部错误

**解决方案：**

**错误码40：配置文件格式错误**

1.检查一下配置文件，比如compileSdkVersion 的配置。

2.检查config.json中"label": "$string:squarewatch\_MainAbility"，label的string名字是否过长（不要超过22个字符）

3.排查下应用图标是否太大（正常图标大小为80×80和114×114）

**错误码31：签名验证错误**

1. 检查签名中是否添加了手表的udid，udid操作请参考[注册设备](../app/agc-help-add-device-0000002283189937.md)。
2. 检查添加的udid是否超过10个。
3. 检查签名证书是否过期。
4. 手动签名详情请参考[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。

**错误码47：配置文件app.apiVersion字段不合法**

原因：

厂商配置sdk版本如下，compatibleSdkVersion的版本过高导致。

```
1. compileSdkVersion 6
2. defaultConfig {
3. compatibleSdkVersion 6
4. }
```

解决：

compatibleSdkVersion版本改为3，如下所示

```
1. compileSdkVersion 6
2. defaultConfig {
3. compatibleSdkVersion  3
4. }
```

**安装失败34：内部错误**

解决：

单个js页面过大，超过48kb，减小单个js页面。

## 示例代码

* [轻量级智能穿戴应用开发](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/LiteWearable)
