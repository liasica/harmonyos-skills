---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-gesture
title: 使用Web组件的手势与应用交互
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > 使用Web组件的手势与应用交互
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d369f9700f0d33997bfccbfa9d5b9491e317659999b6791b7cb4a2c9391bc2d0
---

在移动端或支持触控的Web应用中，用户通过触摸屏与页面交互，Web组件支持了常见的手势识别，例如长按、滑动、点击等，以支持丰富的用户交互体验。

## ArkWeb手势识别

ArkWeb接收ArkUI的[触摸事件](arkts-interaction-development-guide-touch-screen.md#触摸事件)，并识别出手势（触摸事件的分发策略详见[交互基础机制说明](arkts-interaction-basic-principles.md)）。ArkWeb手势符合W3C标准：Touch Events、UI Events、Pointer Events。

常见事件识别说明：

| 手势事件 | 触发条件 |
| --- | --- |
| Tap | 按下并抬起时触发，且间隔较短未触发长按。 |
| LongPress | 按下且不移动，经过一段延迟后触发。 |
| ScrollBegin | 滚动开始时触发。 |
| ScrollUpdate | 滚动时触发，包括抛滑和拖滑。手指未离开屏幕时的滚动为拖滑；若手指离开屏幕时带有速度，离手后页面继续滚动，被称为抛滑。 |
| ScrollEnd | 滚动结束时触发。 |
| FlingStart | 滚动过程中手指抬起，且抬手速度足够快，触发了抛滑。 |
| FlingCancel | 取消抛滑时触发。 |
| PinchBegin | 捏合开始时触发。 |
| PinchUpdate | 捏合过程中触发。 |
| PinchEnd | 捏合结束时触发。 |

## ArkWeb手势与ArkUI手势

ArkUI提供了[手势绑定](arkts-gesture-events-binding.md)，Web组件有独立的手势识别，因此需要区分两种手势：

* ArkWeb手势：Web组件接收触摸事件自动生成的手势，这些手势作用于网页上。
* ArkUI手势：Web组件作为通用组件会接收ArkUI手势，ArkUI手势并不直接作用于网页，而作用于Web组件上。

以缩放为例说明两种手势的区别：

* 在Web上使用双指捏合时，Web组件中的内容将会缩放。这是由于ArkWeb识别了Pinch事件并将其作用于网页上。
* 使用三指捏合，Web组件本身会进行缩放。这是因为ArkWeb接收到ArkUI识别出的[PinchGesture](arkts-gesture-events-single-gesture.md#捏合手势pinchgesture)，执行绑定的回调函数。同时，ArkWeb支持scale方法，能够调整Web组件的缩放比例。

说明

该示例仅用于说明ArkUI手势和ArkWeb手势的区别，不建议使用此方法进行Web组件的缩放。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. @State scaleValue: number = 1;
7. @State pinchValue: number = 1;
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. // 在组件上绑定缩放比例，可以通过修改缩放比例来实现组件的缩小或者放大
14. .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
15. .zoomAccess(true)
16. .gesture(
17. // 在组件上绑定三指触发的捏合手势
18. PinchGesture({ fingers: 3 })
19. .onActionStart((event: GestureEvent|undefined) => {
20. console.info('Pinch start');
21. })
22. // 当捏合手势触发时，可以通过回调函数获取缩放比例，从而修改组件的缩放比例
23. .onActionUpdate((event: GestureEvent|undefined) => {
24. if(event){
25. this.scaleValue = this.pinchValue * event.scale;
26. console.info(`Pinch update: ${this.scaleValue}`);
27. }
28. })
29. .onActionEnd(() => {
30. this.pinchValue = this.scaleValue;
31. console.info('Pinch end');
32. })
33. )
34. }
35. }
36. }
```

[DistinguishTwoGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebGestureInteraction/entry/src/main/ets/pages/DistinguishTwoGesture.ets#L15-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/d127PP1JSSKON45lWQAVOA/zh-cn_image_0000002589324581.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052919Z&HW-CC-Expire=86400&HW-CC-Sign=F50A5C1F3B82E4EFA7A57DF46F7021811109027CDAEA1B0534271CFF461BD0CA)

## Web组件的手势拦截

* ArkUI手势

  ArkWeb会消费部分ArkUI手势，例如[滑动手势](arkts-gesture-events-single-gesture.md#滑动手势pangesture)，若希望自行处理这些手势而非由ArkWeb消费，可以参考ArkUI的[手势冲突处理](arkts-gesture-events-gesture-judge.md)。
* ArkWeb手势

  ArkWeb手势的生成需要Web组件接收触摸事件，有两种拦截方案：

  1. 完全禁止触摸事件发送给Web组件，详见[触摸测试](arkts-interaction-basic-principles.md#触摸测试)。
  2. 发送TouchCancel触摸事件给Web组件，CAPI接口介绍详见[OH\_ArkUI\_TouchRecognizer\_CancelTouch](../harmonyos-references/capi-native-gesture-h.md#函数)，具体示例请参考[NdkGestureSetting](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkGestureSetting)。

## 常见问题

### 如何禁用缩放手势

Web组件提供了接口[zoomAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#zoomaccess)，控制是否可以缩放。网页上有user-scalable属性也会影响缩放。详见[使用Web组件管理网页缩放](web-scale-zoom.md)。

### Web组件中如何通过手势滑动返回上一个Web页面

**解决措施**

通过重写onBackPress函数来自定义返回逻辑，使用WebviewController判断是否返回上一个Web页面。

**示例代码**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com', controller: this.controller }) // 需要手动替换为真实网站
11. }
12. }

14. onBackPress() {
15. try {
16. // 当前页面是否可前进或者后退给定的step步(-1),正数代表前进，负数代表后退
17. if (this.controller.accessStep(-1)) {
18. this.controller.backward(); // 返回上一个Web页面
19. // 执行用户自定义返回逻辑
20. return true;
21. }
22. } catch (err) {
23. console.error(`copyUrlPicToDir failed with error: ${err.code}, ${err.message}`);
24. }
25. // 执行系统默认返回逻辑，返回上一个页面
26. return false;
27. }
28. }
```

[ReturnLastWebPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebGestureInteraction/entry/src/main/ets/pages/ReturnLastWebPage.ets#L15-L41)

### 为什么Web组件加载后网页无法交互？

网页可能基于其他平台的User-Agent进行判断。为解决此问题，可以在Web组件中设置自定义User-Agent，例如：

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. private webController: webview.WebviewController = new webview.WebviewController();
7. build(){
8. Column() {
9. Web({
10. src: 'https://www.example.com',
11. controller: this.webController,
12. }).onControllerAttached(() => {
13. // 自定义User-Agent
14. let customUA = 'Mozilla/5.0 (Phone; Android; HarmonyOS 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36';
15. this.webController.setCustomUserAgent(customUA);
16. })
17. }
18. }
19. }
```

[SetUserAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/WebGestureInteraction/entry/src/main/ets/pages/SetUserAgent.ets#L15-L35)
