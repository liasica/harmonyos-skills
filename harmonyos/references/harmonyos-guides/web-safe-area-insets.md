---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-safe-area-insets
title: 网页中安全区域计算和避让适配
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > 网页中安全区域计算和避让适配
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:214a2c2f90f11067fb898a281156ff36a8ab6ff2d34ef083103c31865c2b02a4
---

早期设备屏幕多为矩形，应用界面能够完整展示。随着全面屏、刘海屏等异形屏幕的普及，屏幕边缘可能出现圆角、摄像头或系统导航条，导致界面部分被遮挡。

安全区域是指屏幕中未被设备硬件或系统UI遮挡的区域，不与系统非安全区域（如状态栏、挖孔区和导航栏）重叠。应用的布局默认限定在安全区域内，但系统提供沉浸式布局能力，允许应用通过配置使界面扩展至非安全区域。

在沉浸式效果下，Web组件中的网页元素可能会被状态栏、挖孔区及导航条遮挡。此情况下，需要网页开发者进行避让适配，确保网页中的文字、表单和交互组件等关键内容避让非安全区域，从而保证用户可以完整地阅读和操作。

Web组件提供利用W3C CSS进行安全区域计算和避让适配的能力，支持异形屏幕设备在沉浸式效果下网页的正常显示，网页开发者可以利用该能力对被遮挡的元素进行避让。

## 开启Web组件沉浸式效果

Web组件默认布局在安全区域内。开启[沉浸式效果](arkts-develop-apply-immersive-effects.md)后，Web网页将扩展至状态栏和导航栏，从而最大化利用屏幕可视区域，增强视觉连贯性，改善用户的UI体验。开发者可通过以下方式启用Web组件的沉浸式效果。

* 通过[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置应用窗口全屏。窗口全屏时，Web组件可布局至非安全区域。

  ```
  1. // EntryAbility.ets
  2. import { UIAbility } from '@kit.AbilityKit';
  3. import { window } from '@kit.ArkUI';

  5. export default class EntryAbility extends UIAbility {
  6. // ...
  7. onWindowStageCreate(windowStage: window.WindowStage): void {
  8. windowStage.getMainWindow().then(window => {
  9. // 设置窗口全屏
  10. window.setWindowLayoutFullScreen(true);
  11. });
  12. }
  13. }
  ```

  ```
  1. // xxx.ets
  2. import { webview } from '@kit.ArkWeb';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Web({ src: 'www.example.com', controller: this.controller })
  12. .width('100%').height('100%')
  13. }
  14. }
  15. }
  ```
* 通过[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)设置Web组件扩展安全区域，可以自定义扩展类型和方向。下面的示例中，Web组件可扩展至状态栏和导航栏，实现沉浸式效果。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .width('100%').height('100%')
12. // 扩展至系统默认非安全区域（状态栏、导航栏），并设置只扩展上方区域和下方区域
13. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
14. }
15. }
16. }
```

[CalcAdjustSafeArea.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ProcessWebPageCont/entry/src/main/ets/pages/CalcAdjustSafeArea.ets#L15-L32)

## 设置网页在可视窗口中的布局方式

viewport-fit用于设置网页在可视窗口中的布局方式，是<meta name="viewport">标签的一个属性。设置方式如下：

```
1. <meta name='viewport' content='viewport-fit=cover'>
```

如表1所示，viewport-fit默认为auto，与contain表现一致，表示网页内容全部包含在安全区域内。cover表示网页内容完全覆盖可视窗口，可能与非安全区域发生重叠。

**表1** viewport-fit属性取值说明

| viewport-fit取值 | 说明 | 适用场景 |
| --- | --- | --- |
| auto | 默认值，与contain表现一致。 | 无需特殊适配的普通网页。 |
| contain | 网页内容被严格限制在安全区域内，不与非安全区域重叠。 | 需要确保完整显示的网页。 |
| cover | 网页内容完全覆盖可视窗口，可能与非安全区域重叠。 | 需要最大化渲染可视窗口的网页，由网页开发者进行避让适配。 |

说明

Web组件当前还不支持开启沉浸式效果时将网页内容限制在安全区域内。因此，当设置viewport-fit=contain时，表现与cover一致，网页内容完全填充Web组件区域。

## 网页元素避让适配

safe-area-inset-\*是一组CSS环境变量，定义了安全区域与Web可视窗口边缘的距离，即网页内容要完整显示时，在top、right、bottom和left四个方向上需要避让的距离，如下图所示。不同于其他CSS属性，环境变量的属性名称对大小写敏感。

**图1** safe-area-inset-\*示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/cEmxQxtbSWugnsJUEiLyEQ/zh-cn_image_0000002552958234.png?HW-CC-KV=V1&HW-CC-Date=20260427T234104Z&HW-CC-Expire=86400&HW-CC-Sign=4ADC8A2A0CB4F5ECA9B7AF93A75FF45B7E8C151A75A9E20421B98C029959090A)

当设置viewport-fit=cover时，ArkWeb内核将持续监测Web组件及系统非安全区域的位置与尺寸，根据两者的重叠部分计算网页在四个方向上需避让的具体距离，并设置给环境变量safe-area-inset-\*。在矩形显示器（如普通PC/2in1设备的屏幕）上，这些值为零。在非矩形显示器（如圆形表盘或移动设备屏幕）上，safe-area-inset-\*所界定的内矩形区域即为安全区域，网页内容在该区域内可完整显示，避免被非矩形显示区域裁剪。

网页元素的避让适配依赖CSS函数env()，该函数用于获取浏览器或系统提供的环境变量。使用env()函数可以获取safe-area-inset-\*的值。网页开发者无需关注设备非安全区域的具体位置和尺寸，在CSS样式中应用env(safe-area-inset-\*)即可定义网页需要避让的距离，实现跨设备的避让。语法如下：

```
1. /* 分别表示上、右、下、左，四个方向上的避让值 */
2. env(safe-area-inset-top);
3. env(safe-area-inset-right);
4. env(safe-area-inset-bottom);
5. env(safe-area-inset-left);

7. /* 基于fallback设置避让值，第二个参数表示环境变量不存在时的回退值 */
8. /* 下述长度单位参见：https://developer.mozilla.org/zh-CN/docs/Web/CSS/length */
9. env(safe-area-inset-top, 20px);
10. env(safe-area-inset-right, 1em);
11. env(safe-area-inset-bottom, 0.5vh);
12. env(safe-area-inset-left, 1.4rem);

14. /* env()可基于部分数学计算函数`calc()`,`min()`,`max()`进行组合计算 */
15. calc(env(safe-area-inset-top) + 10px)
16. min(env(safe-area-inset-left), 50px)
17. max(env(safe-area-inset-bottom), 30px)
```

说明

使用env(safe-area-inset-\*)进行避让时需要设置viewport-fit=cover。viewport-fit=contain时，env(safe-area-inset-\*)值为0。

## 网页元素避让非安全区域最佳实践

Web组件启用沉浸式效果时，渲染内容可能与非安全区域重叠，影响用户的阅读和交互，如图2所示。非安全区域包括顶部状态栏、屏幕挖孔区和底部导航条。在沉浸式效果下，index.html网页的标题栏被屏幕挖孔区遮挡，底部的Tab区域与导航条发生重叠。

**图2** Web组件开启沉浸式效果时网页元素被非安全区域遮挡

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/RGg5D2XgSqi6U-njx0MjFg/zh-cn_image_0000002583478235.png?HW-CC-KV=V1&HW-CC-Date=20260427T234104Z&HW-CC-Expire=86400&HW-CC-Sign=25F42CB846A7743F2E610AD8ADD992C5D1D0F769B001F24A2C3967CFDA408F5E)

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html lang="en">
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
7. <style>
8. body {
9. margin: 0;
10. background: #f6f6f6;
11. }
12. .edge {
13. position: fixed;
14. display: flex;
15. width: 100%;
16. background: #fefefe;
17. }
18. .title-bar {
19. align-items: center;
20. justify-content: center;
21. top: 0;
22. height: 40px;
23. }
24. .content {
25. margin: 8px;
26. padding-top: 40px;
27. }
28. .tabs {
29. justify-content: space-around;
30. bottom: 0;
31. height: 40px;
32. }
33. .tab {
34. padding: 10px;
35. }
36. .tab.active {
37. color: Blue;
38. }
39. </style>
40. </head>
41. <body>
42. <div>
43. <div class="edge title-bar">Example page</div>
44. <div class="content">
45. <p>Contents of page</p>
46. </div>
47. </div>
48. <div class="edge tabs">
49. <div class="tab active">Tab1</div>
50. <div class="tab">Tab2</div>
51. <div class="tab">Tab3</div>
52. </div>
53. </body>
54. </html>
```

网页开发者可利用env(safe-area-inset-\*)定义CSS样式，确保文字、图片和交互组件避让非安全区域。在以下示例中，通过env(safe-area-inset-\*)更新了index.html的CSS样式，使网页主要内容避让非安全区域，效果见图3。

```
1. .title-bar {
2. align-items: center;
3. justify-content: center;
4. top: 0;
5. height: 40px;
6. padding-top: env(safe-area-inset-top); /* 设置padding-top避让上方非安全区域 */
7. }
8. .content {
9. margin: 8px;
10. padding-top: calc(env(safe-area-inset-top) + 40px); /* 同步title-bar增加padding-top高度 */
11. }
12. .tabs {
13. justify-content: space-around;
14. bottom: 0;
15. height: calc(env(safe-area-inset-bottom) + 40px); /* 增加tab区域高度以避让下方非安全区域 */
16. }
```

**图3** Web组件开启沉浸式效果时网页元素避让非安全区域

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/9QCgdhFNRlCwDud5DilPNw/zh-cn_image_0000002552798586.png?HW-CC-KV=V1&HW-CC-Date=20260427T234104Z&HW-CC-Expire=86400&HW-CC-Sign=280BF3E6C8C65A7FC5C24A1200E145F73FE561FC9A56D8D728BC20007A590BAC)
