---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screenproperty-guideline
title: 使用Display实现屏幕属性查询及状态监听 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 屏幕管理 > 使用Display实现屏幕属性查询及状态监听 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df34b2eb0033264d3092bd08879468d3a2ed656d333c6fe35df1c7acfc8c8847
---

## 场景介绍

[Display](../harmonyos-references/js-apis-display.md)屏幕属性提供管理设备屏幕的一些基础能力，例如获取默认显示设备的相关信息、获取全部显示设备的信息，此外还能对显示设备的插拔行为进行监听。应用可以根据对应的屏幕信息、屏幕状态变化、屏幕折叠状态等适配不同的UI界面显示。

屏幕属性的常见使用场景有以下几种：

* 查询屏幕信息：包括屏幕的分辨率、物理像素密度、逻辑像素密度、刷新率、屏幕尺寸、屏幕旋转方向、屏幕旋转角度等，具体可见[Display属性](../harmonyos-references/js-apis-display.md#属性)。
* 监听屏幕状态变化，包括屏幕旋转变化，屏幕分辨率变化、屏幕刷新率变化等。
* 查询当前设备是否为可折叠设备，同时支持折叠状态（展开/折叠）变化的监听。

## 接口说明

屏幕属性的常用接口如下表所示，更多功能及接口说明和使用请见[@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)。

| 接口 | 描述 |
| --- | --- |
| getAllDisplays(): Promise<Array<Display>> | 获取当前所有的Display对象，使用Promise异步回调。 |
| getDefaultDisplaySync(): Display | 获取当前默认的Display对象。 |
| getDisplayByIdSync(displayId: number): Display | 根据DisplayId获取对应的Display对象。 |
| on(type: 'add'|'remove'|'change', callback: Callback<number>): void | 开启显示设备变化的监听。 |
| off(type: 'add'|'remove'|'change', callback?: Callback<number>): void | 关闭显示设备变化的监听。 |
| on(type: 'captureStatusChange', callback: Callback<boolean>): void | 开启屏幕截屏、投屏、录屏状态变化的监听。 |
| off(type: 'captureStatusChange', callback?: Callback<boolean>): void | 关闭屏幕截屏、投屏、录屏状态变化的监听。 |
| on(type: 'availableAreaChange', callback: Callback<Rect>): void | 开启当前设备屏幕的可用区域监听。当前设备屏幕有可用区域变化时，触发回调函数，返回可用区域。 |
| off(type: 'availableAreaChange', callback?: Callback<Rect>): void | 关闭当前设备屏幕可用区域变化的监听。 |
| isFoldable(): boolean | 检查设备是否可折叠，true表示设备可折叠，false表示设备不可折叠。 |
| on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void | 开启折叠设备折叠状态变化的监听。 |
| off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void | 关闭折叠设备折叠状态变化的监听。 |

## 获取Display对象

Display对象，即屏幕实例，提供屏幕相关属性及监听变化的接口。目前有以下几种不同获取Display的方式，开发者可根据具体场景需要选择使用。

* 获取当前默认的Display对象：使用getDefaultDisplaySync()接口获取。
* 获取当前所有Display对象：使用getAllDisplays()获取。
* 根据屏幕Id获取对应的Display对象：使用getDisplayByIdSync()接口获取。

此处，以使用getDefaultDisplaySync()获取当前默认Display对象为例，示例如下：

```
1. let displayClass: display.Display | null = null;
2. try {
3. displayClass = display.getDefaultDisplaySync();
4. hilog.info(DOMAIN, 'DisplayTest', `The display info is: ${JSON.stringify(displayClass)}`);
5. } catch (exception) {
6. hilog.error(DOMAIN, 'DisplayTest',
7. `Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
8. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L110-L119)

## 获取屏幕相关属性

1. 确保获取到Display对象之后（具体可见[获取Display对象](screenproperty-guideline.md#获取display对象)），可以通过相关属性查询屏幕的一些基础信息。

   ```
   1. let displayClass: display.Display | null = null;
   2. try {
   3. displayClass = display.getDefaultDisplaySync();
   4. // 获取屏幕Id
   5. hilog.info(DOMAIN, 'DisplayTest', `The screen Id is ${displayClass.id}.`);
   6. // 获取屏幕刷新率
   7. hilog.info(DOMAIN, 'DisplayTest', `The screen is ${displayClass.refreshRate}.`);
   8. // 获取屏幕宽度
   9. hilog.info(DOMAIN, 'DisplayTest', `The screen width is ${displayClass.width}.`);
   10. // 获取屏幕高度
   11. hilog.info(DOMAIN, 'DisplayTest', `The screen height is ${displayClass.height}.`);
   12. // ...
   13. } catch (exception) {
   14. hilog.error(DOMAIN, 'DisplayTest',
   15. `Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
   16. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L123-L140)
2. 还可以通过getCutoutInfo()获取挖孔屏、刘海屏、瀑布屏等不可用的屏幕区域信息，以在UI布局时更好地规避该区域。也可以通过getAvailableArea()获取当前设备屏幕的可用区域。

   ```
   1. let displayClass: display.Display | null = null;
   2. try {
   3. displayClass = display.getDefaultDisplaySync();
   4. displayClass.getCutoutInfo().then((cutoutInfo: display.CutoutInfo) => {
   5. // 在有挖孔信息的时候进行处理
   6. if (cutoutInfo.boundingRects.length > 0) {
   7. hilog.info(DOMAIN, 'DisplayTest', `cutoutInfo boundingRects: ${JSON.stringify(cutoutInfo.boundingRects)}`);
   8. } else {
   9. hilog.info(DOMAIN, 'DisplayTest', 'There is no cutout info on the screen.');
   10. }
   11. // 处理瀑布屏的区域信息
   12. hilog.info(DOMAIN, 'DisplayTest',
   13. `cutoutInfo waterfallDisplayAreaRects: ${JSON.stringify(cutoutInfo.waterfallDisplayAreaRects)}`);
   14. }).catch((err: BusinessError) => {
   15. hilog.error(DOMAIN, 'DisplayTest',
   16. `Failed to obtain the cutout info object. Code: ${err.code}, message: ${err.message}`);
   17. });
   18. } catch (exception) {
   19. hilog.error(DOMAIN, 'DisplayTest',
   20. `Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
   21. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L144-L166)
3. 此外，还可以通过display.isCaptured()判断当前设备是否正在截屏、投屏或录屏。

   ```
   1. try {
   2. hilog.info(DOMAIN, 'DisplayTest', `The screen is captured or not : ${display.isCaptured()}`);
   3. } catch (exception) {
   4. hilog.error(DOMAIN, 'DisplayTest',
   5. `Failed to get display isCaptured. Code: ${exception.code}, message: ${exception.message}`);
   6. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L170-L177)

## 监听屏幕状态变化

1. 可以通过display.on('add'|'remove'|'change')监听设备屏幕变化，支持监听屏幕设备的增加、移除和改变等，可以通过display.off('add'|'remove'|'change')关闭对应的监听。

   ```
   1. /**
   2. * 注册监听的callback参数要采用对象传递.
   3. * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
   4. */
   5. let callback1: Callback<number> = (displayId: number) => {
   6. hilog.info(DOMAIN, 'DisplayTest', `Listening enabled. displayId: ${displayId}`);
   7. };
   8. try {
   9. // 此处以监听显示设备的增加为例
   10. display.on('add', callback1);
   11. hilog.info(DOMAIN, 'DisplayTest', `register add success`);

   13. // 关闭单个callback监听
   14. display.off('add', callback1);
   15. hilog.info(DOMAIN, 'DisplayTest', `unregister add success`);
   16. // 如果通过on注册多个callback，同时关闭所有callback监听
   17. display.off('add');
   18. hilog.info(DOMAIN, 'DisplayTest', `unregister all add success`);
   19. } catch (exception) {
   20. hilog.error(DOMAIN, 'DisplayTest',
   21. `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   22. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L181-L204)
2. 可以通过display.on('captureStatusChange')开启屏幕截屏、投屏或录屏状态变化的监听；可以通过display.off('captureStatusChange')关闭对应的监听。

   ```
   1. let callback2: Callback<boolean> = (captureStatus: boolean) => {
   2. // captureStatus为true表示显示设备开始截屏、投屏或录屏，false表示结束截屏、投屏或录屏
   3. hilog.info(DOMAIN, 'DisplayTest', 'Listening capture status: ' + captureStatus);
   4. };

   6. try {
   7. // 开启屏幕截屏、投屏、录屏状态变化的监听
   8. display.on('captureStatusChange', callback2);
   9. hilog.info(DOMAIN, 'DisplayTest', `register captureStatusChange success`);
   10. // 关闭屏幕截屏、投屏、录屏状态变化的监听
   11. display.off('captureStatusChange', callback2);
   12. hilog.info(DOMAIN, 'DisplayTest', `unregister captureStatusChange success`);
   13. } catch (exception) {
   14. hilog.error(DOMAIN, 'DisplayTest',
   15. `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   16. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L205-L222)
3. 此外，还可以通过on('availableAreaChange')监听当前屏幕对象（Display对象）的可用区域变化；可通过off('availableAreaChange')关闭对应的监听。

   ```
   1. /**
   2. * 注册监听的callback参数要采用对象传递.
   3. * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
   4. */
   5. let callback3: Callback<display.Rect> = (data: display.Rect) => {
   6. hilog.info(DOMAIN, 'DisplayTest', 'Listening enabled. Data: ' + JSON.stringify(data));
   7. };
   8. let displayClass: display.Display | null = null;
   9. try {
   10. displayClass = display.getDefaultDisplaySync();
   11. // 开启当前屏幕可用区域变化的监听
   12. displayClass.on('availableAreaChange', callback3);
   13. hilog.info(DOMAIN, 'DisplayTest', `register availableAreaChange success`);
   14. // 关闭当前屏幕可用区域变化的监听
   15. displayClass.off('availableAreaChange', callback3);
   16. hilog.info(DOMAIN, 'DisplayTest', `unregister availableAreaChange success`);
   17. } catch (exception) {
   18. hilog.error(DOMAIN, 'DisplayTest',
   19. `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   20. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L223-L244)

## 监听折叠设备状态变化

1. 可以通过display.isFoldable()接口查询当前设备是不是折叠设备。

   ```
   1. let isFoldableDevice: boolean = false;
   2. try {
   3. isFoldableDevice = display.isFoldable();
   4. // 打印此设备是否为折叠设备
   5. hilog.info(DOMAIN, 'DisplayTest', `This device is foldable: ${isFoldableDevice}`);
   6. } catch (exception) {
   7. hilog.error(DOMAIN, 'DisplayTest',
   8. `Failed to get foldable message. Code: ${exception.code}, message: ${exception.message}`);
   9. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L248-L258)
2. 若当前设备为折叠设备，可以通过display.on('foldStatusChange')开启折叠设备折叠状态变化的监听；可通过display.off('foldStatusChange')关闭对应的监听。

   ```
   1. /**
   2. * 注册监听的callback参数要采用对象传递.
   3. * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
   4. */
   5. let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
   6. hilog.info(DOMAIN, 'DisplayTest', 'Listening enabled. Data: ' + JSON.stringify(data));
   7. };
   8. try {
   9. display.on('foldStatusChange', callback);
   10. // 如果通过on注册多个callback，同时关闭所有callback监听
   11. hilog.info(DOMAIN, 'DisplayTest', `register foldStatusChange success`);

   13. // 关闭单个callback监听
   14. display.off('foldStatusChange', callback);
   15. hilog.info(DOMAIN, 'DisplayTest', `unregister all foldStatusChange success`);
   16. // 关闭所有callback监听
   17. display.off('foldStatusChange');
   18. hilog.info(DOMAIN, 'DisplayTest', `unregister foldStatusChange success`);
   19. } catch (exception) {
   20. hilog.error(DOMAIN, 'DisplayTest',
   21. `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   22. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DisplayBasicSample/entry/src/main/ets/pages/Index.ets#L261-L284)
