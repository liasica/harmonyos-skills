---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screenproperty-guideline
title: 使用Display实现屏幕属性查询及状态监听 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 屏幕管理 > 使用Display实现屏幕属性查询及状态监听 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3a3a3dcf8e484661dfeb9eacc053c6d1626b3505f99d952fb45a9d61b892929e
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

```typescript
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  hilog.info(DOMAIN, 'DisplayTest', `The display info is: ${JSON.stringify(displayClass)}`);
} catch (exception) {
  hilog.error(DOMAIN, 'DisplayTest',
    `Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
}
```

## 获取屏幕相关属性

1. 确保获取到Display对象之后（具体可见[获取Display对象](screenproperty-guideline.md#获取display对象)），可以通过相关属性查询屏幕的一些基础信息。

   ```typescript
   let displayClass: display.Display | null = null;
   try {
     displayClass = display.getDefaultDisplaySync();
     // 获取屏幕Id
     hilog.info(DOMAIN, 'DisplayTest', `The screen Id is ${displayClass.id}.`);
     // 获取屏幕刷新率
     hilog.info(DOMAIN, 'DisplayTest', `The screen is ${displayClass.refreshRate}.`);
     // 获取屏幕宽度
     hilog.info(DOMAIN, 'DisplayTest', `The screen width is ${displayClass.width}.`);
     // 获取屏幕高度
     hilog.info(DOMAIN, 'DisplayTest', `The screen height is ${displayClass.height}.`);
     // ...
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```
2. 还可以通过getCutoutInfo()获取挖孔屏、刘海屏、瀑布屏等不可用的屏幕区域信息，以在UI布局时更好地规避该区域。也可以通过getAvailableArea()获取当前设备屏幕的可用区域。

   ```typescript
   let displayClass: display.Display | null = null;
   try {
     displayClass = display.getDefaultDisplaySync();
     displayClass.getCutoutInfo().then((cutoutInfo: display.CutoutInfo) => {
       // 在有挖孔信息的时候进行处理
       if (cutoutInfo.boundingRects.length > 0) {
         hilog.info(DOMAIN, 'DisplayTest', `cutoutInfo boundingRects: ${JSON.stringify(cutoutInfo.boundingRects)}`);
       } else {
         hilog.info(DOMAIN, 'DisplayTest', 'There is no cutout info on the screen.');
       }
       // 处理瀑布屏的区域信息
       hilog.info(DOMAIN, 'DisplayTest',
         `cutoutInfo waterfallDisplayAreaRects: ${JSON.stringify(cutoutInfo.waterfallDisplayAreaRects)}`);
     }).catch((err: BusinessError) => {
       hilog.error(DOMAIN, 'DisplayTest',
         `Failed to obtain the cutout info object. Code: ${err.code}, message: ${err.message}`);
     });
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```
3. 此外，还可以通过display.isCaptured()判断当前设备是否正在截屏、投屏或录屏。

   ```typescript
   try {
     hilog.info(DOMAIN, 'DisplayTest', `The screen is captured or not : ${display.isCaptured()}`);
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to get display isCaptured. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```

## 监听屏幕状态变化

1. 可以通过display.on('add'|'remove'|'change')监听设备屏幕变化，支持监听屏幕设备的增加、移除和改变等，可以通过display.off('add'|'remove'|'change')关闭对应的监听。

   ```typescript
   /**
    * 注册监听的callback参数要采用对象传递.
    * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
    */
   let callback1: Callback<number> = (displayId: number) => {
     hilog.info(DOMAIN, 'DisplayTest', `Listening enabled. displayId: ${displayId}`);
   };
   try {
     // 此处以监听显示设备的增加为例
     display.on('add', callback1);
     hilog.info(DOMAIN, 'DisplayTest', `register add success`);

     // 关闭单个callback监听
     display.off('add', callback1);
     hilog.info(DOMAIN, 'DisplayTest', `unregister add success`);
     // 如果通过on注册多个callback，同时关闭所有callback监听
     display.off('add');
     hilog.info(DOMAIN, 'DisplayTest', `unregister all add success`);
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```
2. 可以通过display.on('captureStatusChange')开启屏幕截屏、投屏或录屏状态变化的监听；可以通过display.off('captureStatusChange')关闭对应的监听。

   ```typescript
   let callback2: Callback<boolean> = (captureStatus: boolean) => {
     // captureStatus为true表示显示设备开始截屏、投屏或录屏，false表示结束截屏、投屏或录屏
     hilog.info(DOMAIN, 'DisplayTest', 'Listening capture status: ' + captureStatus);
   };

   try {
     // 开启屏幕截屏、投屏、录屏状态变化的监听
     display.on('captureStatusChange', callback2);
     hilog.info(DOMAIN, 'DisplayTest', `register captureStatusChange success`);
     // 关闭屏幕截屏、投屏、录屏状态变化的监听
     display.off('captureStatusChange', callback2);
     hilog.info(DOMAIN, 'DisplayTest', `unregister captureStatusChange success`);
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```
3. 此外，还可以通过on('availableAreaChange')监听当前屏幕对象（Display对象）的可用区域变化；可通过off('availableAreaChange')关闭对应的监听。

   ```typescript
   /**
    * 注册监听的callback参数要采用对象传递.
    * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
    */
   let callback3: Callback<display.Rect> = (data: display.Rect) => {
     hilog.info(DOMAIN, 'DisplayTest', 'Listening enabled. Data: ' + JSON.stringify(data));
   };
   let displayClass: display.Display | null = null;
   try {
     displayClass = display.getDefaultDisplaySync();
     // 开启当前屏幕可用区域变化的监听
     displayClass.on('availableAreaChange', callback3);
     hilog.info(DOMAIN, 'DisplayTest', `register availableAreaChange success`);
     // 关闭当前屏幕可用区域变化的监听
     displayClass.off('availableAreaChange', callback3);
     hilog.info(DOMAIN, 'DisplayTest', `unregister availableAreaChange success`);
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```

## 监听折叠设备状态变化

1. 可以通过display.isFoldable()接口查询当前设备是不是折叠设备。

   ```typescript
   let isFoldableDevice: boolean = false;
   try {
     isFoldableDevice = display.isFoldable();
     // 打印此设备是否为折叠设备
     hilog.info(DOMAIN, 'DisplayTest', `This device is foldable: ${isFoldableDevice}`);
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to get foldable message. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```
2. 若当前设备为折叠设备，可以通过display.on('foldStatusChange')开启折叠设备折叠状态变化的监听；可通过display.off('foldStatusChange')关闭对应的监听。

   ```typescript
   /**
    * 注册监听的callback参数要采用对象传递.
    * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
    */
   let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
     hilog.info(DOMAIN, 'DisplayTest', 'Listening enabled. Data: ' + JSON.stringify(data));
   };
   try {
     display.on('foldStatusChange', callback);
     // 如果通过on注册多个callback，同时关闭所有callback监听
     hilog.info(DOMAIN, 'DisplayTest', `register foldStatusChange success`);

     // 关闭单个callback监听
     display.off('foldStatusChange', callback);
     hilog.info(DOMAIN, 'DisplayTest', `unregister all foldStatusChange success`);
     // 关闭所有callback监听
     display.off('foldStatusChange');
     hilog.info(DOMAIN, 'DisplayTest', `unregister foldStatusChange success`);
   } catch (exception) {
     hilog.error(DOMAIN, 'DisplayTest',
       `Failed to register/unregister callback. Code: ${exception.code}, message: ${exception.message}`);
   }
   ```
