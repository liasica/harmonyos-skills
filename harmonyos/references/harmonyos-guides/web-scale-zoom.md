---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-scale-zoom
title: 使用Web组件管理网页缩放
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > 使用Web组件管理网页缩放
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d0df246432e1ff55ecc14c54c12d128bb36701ed6017e737816b733996561f1
---

Web组件支持手势缩放、鼠标滚轮、键盘缩放，以方便用户调整到舒适的显示大小。并对应用提供监听、控制页面缩放比例的功能，以便应用实现个性化的视觉效果。

## 启用/禁用网页缩放

### 启用/禁用网页手势缩放

通过属性[zoomAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#zoomaccess)控制网页缩放功能，当设置为false时，网页不允许手势缩放行为。

当html网页设置<meta name="viewport" id="viewport" content="user-scalable=no">时，网页不允许手势缩放。

仅当zoomAccess和viewport标签都设置为允许缩放时，才允许手势缩放。

说明

在PC/2in1设备上，viewport标签不生效，仅能通过设置zoomAccess为false来禁用手势缩放。

以上方法仅能控制缩放功能的开关，但如果网页在viewport标签中设置了minimum-scale和maximum-scale，那么缩放的范围也会受到这两个属性的限制，当最大、最小值相等时，网页也是不能缩放的。

另外，网页的内容宽度也会限制缩小的比例。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .zoomAccess(false)
12. }
13. }
14. }
```

[ControlWebGestureZooming.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebManagementZooming/entry/src/main/ets/pages/ControlWebGestureZooming.ets#L15-L30)

### 启用/禁用手势强制缩放

通过属性[forceEnableZoom](../harmonyos-references/arkts-basic-components-web-attributes.md#forceenablezoom21)控制网页强制缩放功能，当设置为true时，手势缩放行为不受minimum-scale和maximum-scale以及user-scalable=no的限制。

### 启用/禁用网页键盘鼠标缩放

ArkWeb默认支持通过Ctrl+按键'-'/'+' 或者 Ctrl+鼠标滚轮进行缩放。应用可以通过拦截键盘事件来阻止按键缩放。

通过拦截键盘事件来阻止按键缩放：

```
1. import { webview } from '@kit.ArkWeb';
2. import { KeyCode } from '@kit.InputKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .zoomAccess(true)
13. .onKeyPreIme((event) => {
14. if (event.type === KeyType.Down &&
15. event.getModifierKeyState &&
16. event.getModifierKeyState(['Ctrl']) &&
17. (event.keyCode === KeyCode.KEYCODE_MINUS || event.keyCode === KeyCode.KEYCODE_EQUALS ||
18. event.keyCode === KeyCode.KEYCODE_NUMPAD_SUBTRACT || event.keyCode === KeyCode.KEYCODE_NUMPAD_ADD)) {
19. return true;
20. }
21. return false;
22. })
23. }
24. }
25. }
```

[ControlMouseAndKeyBoardZooming.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebManagementZooming/entry/src/main/ets/pages/ControlMouseAndKeyBoardZooming.ets#L15-L41)

或者通过属性[zoomControlAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#zoomcontrolaccess22)设置是否允许通过组合按键（Ctrl+'-/+'或Ctrl+鼠标滚轮/触摸板）进行缩放。

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
12. .zoomControlAccess(false)
13. }
14. }
15. }
```

## 监听页面缩放比例变化

应用可以通过[onScaleChange](../harmonyos-references/arkts-basic-components-web-events.md#onscalechange9)接口监听页面缩放比例的变化。该接口事件对应手势事件(双指缩放)，event.newScale对应网页属性visualViewport.scale。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .onScaleChange((event) => {
12. console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
13. })
14. }
15. }
16. }
```

[MonitorZoomRatio.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebManagementZooming/entry/src/main/ets/pages/MonitorZoomRatio.ets#L15-L32)

## 控制网页的缩放比例

应用可以通过设置[initialScale](../harmonyos-references/arkts-basic-components-web-attributes.md#initialscale9)属性设置页面初始缩放比例。

应用可以通过[zoom](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoom)、[zoomIn](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomin)、[zoomOut](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomout)接口控制页面缩放。

说明

使用以上接口控制页面缩放时，必须设置属性zoomAccess为true。zoomAccess为false时，zoom类接口会抛出异常17100004。

### 以固定比例缩放页面

zoomIn将当前网页进行放大，比例为25%；zoomOut将当前网页进行缩小，比例为20%。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Button('zoomIn')
11. .onClick(() => {
12. try {
13. this.controller.zoomIn();
14. } catch (error) {
15. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
16. }
17. })
18. Button('zoomOut')
19. .onClick(() => {
20. try {
21. this.controller.zoomOut();
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. .zoomAccess(true)
28. }
29. }
30. }
```

[ControlZoomByFixedRatio.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebManagementZooming/entry/src/main/ets/pages/ControlZoomByFixedRatio.ets#L15-L46)

### 根据输入值控制页面缩放比例:

zoom基于当前网页比例进行缩放，入参要求大于0，当入参为1时为默认加载网页的缩放比例，入参小于1为缩小，入参大于1为放大。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State factor: number = 1;

10. build() {
11. Column() {
12. TextInput()
13. .type(InputType.NUMBER_DECIMAL)
14. .onChange((value)=>{
15. this.factor = Number(value);
16. })
17. Button('zoom')
18. .onClick(() => {
19. try {
20. this.controller.zoom(this.factor);
21. } catch (error) {
22. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
23. }
24. })
25. Web({ src: 'www.example.com', controller: this.controller })
26. .zoomAccess(true)
27. }
28. }
29. }
```

[ControlZoomByInput.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebManagementZooming/entry/src/main/ets/pages/ControlZoomByInput.ets#L15-L45)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/_gQzddwrTwS94_ULDbEsWw/zh-cn_image_0000002583478221.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=3D27AED6F1E9DA22683C9955B29728927C2F1D099AFA4FD5696200C4F0171106)

### 缩放页面到目标比例:

通过onScaleChange接口，应用可以得知当前网页的缩放比例，配合zoom接口即可实现将页面缩放至指定比例的功能。根据当前页面缩放比例pageFactor和目标比例targetFactor计算zoom入参的公式为：

```
1. factor = 100 * targetFactor / pageFactor
```

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State targetFactor: number = 1;
9. // This represents the page zoom level
10. @State pageFactor: number = 100;
11. // Represents the integer 100
12. intNumber: number = 100;

14. build() {
15. Column() {
16. TextInput()
17. .type(InputType.NUMBER_DECIMAL)
18. .onChange((value)=>{
19. this.targetFactor = Number(value);
20. })
21. Button('zoom')
22. .onClick(() => {
23. try {
24. let factor = this.targetFactor * this.intNumber / this.pageFactor;
25. this.controller.zoom(factor);
26. } catch (error) {
27. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
28. }
29. })
30. Web({ src: 'www.example.com', controller: this.controller })
31. .zoomAccess(true)
32. .onScaleChange((event) => {
33. console.error('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
34. this.pageFactor = event.newScale;
35. })
36. }
37. }
38. }
```

[ControlZoomToFixedRatio.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebManagementZooming/entry/src/main/ets/pages/ControlZoomToFixedRatio.ets#L15-L54)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/kxAzuIQ5SpmXX5GjXpyrOA/zh-cn_image_0000002552798572.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234056Z&HW-CC-Expire=86400&HW-CC-Sign=AA17201018A96DC3A31CEF5E9087826EBB21E130EE6D5478F1AF9512B553024A)
