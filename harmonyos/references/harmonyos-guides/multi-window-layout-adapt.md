---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-layout-adapt
title: 应用布局适配智慧多窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 智慧多窗应用开发指南 > 应用适配智慧多窗 > 应用布局适配智慧多窗
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d8c6f295b6e3b578361b092a3ed00afacfdcf8a156954185d867e8496b039fc8
---

## 应用布局适配智慧多窗的意义

由于应用从全屏进入智慧多窗（悬浮窗/分屏）模式后，窗口尺寸、宽高比例会发生变化，所以需要开发者适配应用窗口在不同尺寸、不同比例下的自适应布局，以确保应用窗口在各种形态下都能呈现出最佳的视觉效果，提供更好的用户体验。

### 悬浮窗的比例

不同设备支持悬浮窗的比例如下所示：

| 设备 | 竖向悬浮窗宽高比 | 横向悬浮窗宽高比 |
| --- | --- | --- |
| 手机 | 3:4.575 | 16:9 |
| 折叠屏手机展开态 | 9:16 | 16:9 |

说明

* 顶部窗口控制条的避让区域不包含在应用布局区域内，窗口高度去除避让区域的32vp为应用布局区域的高度。
* 手机：悬浮窗模式下，应用窗口真实宽度为屏幕宽度。竖向时，高度根据宽高比3 : 4.575动态调整；横向时，高度根据宽高比16 : 9动态调整（该比例超出屏幕时，以当前全屏屏幕比例计算）。
* 折叠屏手机展开态：悬浮窗模式下，应用窗口真实宽度为折叠屏手机折叠态时的屏幕宽度。竖向时，高度根据宽高比9 : 16动态调整；横向时，高度根据宽高比16 : 9动态调整。

### 分屏的比例

目前支持两种分屏样式：“上下分屏”和“左右分屏”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/kZd3F0SNQjGy8H0b8I-a0Q/zh-cn_image_0000002558605034.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=39C0E450B83C8B827AAE476018D87A363A2EF029514563EED1CA408D02C7583B)

分屏比例指的是分屏下两应用间尺寸的比例，调整分屏比例会调整应用窗口的大小。

默认形成分屏后分屏比例为1:1，拖动中间的分屏条可以改变分屏比例档位。手机“上下分屏”可调节档位1:2、1:1、2:1，“左右分屏”可调节档位为1:1。手机折叠屏展开态可调节档位只有1:1。

| 设备 | 默认分屏比例 | 分屏可调节档位 |
| --- | --- | --- |
| 手机 | 1:1 | “上下分屏”: 1:1, 1:2, 2:1  “左右分屏”: 1:1 |
| 手机折叠屏展开态 | 1:1 | “上下分屏”和 “左右分屏”: 1:1 |

应用布局可以通过自适应布局和响应式布局来更新自身布局，避免出现截断、挤压、堆叠等现象。

## 应用布局适配智慧多窗的方案

无论是悬浮窗还是分屏，当应用进入智慧多窗模式时，应用的窗口尺寸发生变化，所以应用需要根据不同的窗口尺寸调整自身布局。

主要可以通过窗口的[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法实现对窗口尺寸大小变化的监听。再根据窗口的尺寸变化，更新调整自身应用布局以实现适配。

主要步骤和示例如下：

1. 在onWindowStageCreate方法中，获取Window对象。
2. 通过getWindowProperties方法返回值中的windowRect获取窗口尺寸，写入AppStorage中用于UI侧窗口尺寸的首次初始化赋值。
3. 使用on('windowSizeChange')注册窗口尺寸变化时的监听，并写入AppStorage中供UI侧布局使用。
4. UI侧通过@StorageLink绑定窗口尺寸后，AppStorage中属性key值对应的数据一旦改变，UI侧会同步修改。
5. @StorageLink装饰的数据本身是状态变量，所以窗口尺寸发生变化时，会引起组件的重新渲染，开发者可以根据最新的窗口尺寸动态调整应用布局。

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. console.info('Ability onWindowStageCreate.');
8. windowStage.getMainWindow().then((windowClass) => {
9. // 获取窗口尺寸，存入AppStorage
10. AppStorage.setOrCreate('winWidth', windowClass.getWindowProperties().windowRect.width);
11. AppStorage.setOrCreate('winHeight', windowClass.getWindowProperties().windowRect.height);
12. // 监听窗口尺寸变化
13. windowClass.on('windowSizeChange', (windowSize) => {
14. AppStorage.setOrCreate('winWidth', windowSize.width);
15. AppStorage.setOrCreate('winHeight', windowSize.height);
16. });
17. });
18. windowStage.loadContent('pages/Index', (err) => {
19. if (err.code) {
20. console.error('Failed to load the content. Cause: ' + JSON.stringify(err));
21. return;
22. }
23. console.info('Succeeded in loading the content.');
24. });
25. }
26. }
```

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5. // 初始化参数，这里会初始化为AppStorage中存储的值
6. @StorageLink('winWidth') winWidth: number = 1260;
7. @StorageLink('winHeight') winHeight: number = 2224;

9. aboutToAppear() {
10. console.info('Current window size. width: ' + this.winWidth + ', height: ' + this.winHeight);
11. }

13. build() {
14. Row() {
15. // 根据winWidth、winHeight动态调整应用布局
16. // ...
17. }
18. .size({
19. width: this.getUIContext().px2vp(this.winWidth),
20. height: this.getUIContext().px2vp(this.winHeight)
21. })
22. .backgroundColor('#fceaeaea')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/vLpaStk_Q1WtT11mskOvqA/zh-cn_image_0000002589324559.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=224170AE267526BC794D62053C93F6236810B742F6CD35C8D46585ABABB9B0B7)
