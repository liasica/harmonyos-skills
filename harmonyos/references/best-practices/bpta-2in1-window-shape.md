---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-2in1-window-shape
title: PC/2in1异形窗口
breadcrumb: 最佳实践 > 应用框架 > 窗口与屏幕管理 > PC/2in1异形窗口
category: best-practices
scraped_at: 2026-04-29T14:11:01+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:6a559bfbdda82e430d55b5ca094c18fd4526ae36ec360edf6fbf7927cc567456
---

## 概述

一般情况下，UI开发都是在矩形窗口上操作，但在PC/2in1设备上，应用还可以使用各类异形窗口来展现交互内容。这里的异形是指除默认矩形以外的形状，包括但不限于圆形、三角形以及其他不规则的形状等。开发者通过使用这些异形形状的窗口，结合窗口中的内容展示UI交互的多样性，一定程度上能够提升应用体验。类似的示例有：文字应用中的放大镜、带指示箭头的气泡框、提供辅助功能的悬浮窗等。

本文主要介绍在PC/2in1设备上实现异形窗口。根据窗口的形状类别，可分为以下场景：

* [图形形状窗口](bpta-2in1-window-shape.md#section6137113512381)
* [不规则形状窗口](bpta-2in1-window-shape.md#section42071254407)

## 实现原理

在创建窗口时，ArkUI以宽、高为参数描绘窗口初始大小，其形状默认为矩形，可以通过设置掩码改变窗口最终呈现的形状。

该掩码是一个二维数组，其大小对应初始窗口的宽和高，所以可以把该数组中的元素与窗口中的像素一一对应起来；数组中的每一项值只能是0或1，其中数字0表示窗口对应位置的像素是透明的，数字1代表对应像素不透明。

简单来说，掩码即是由数字1描绘的窗口形状点阵图。具体使用可参考[setWindowMask()](../harmonyos-references/arkts-apis-window-window.md#setwindowmask12)接口。

### 开发流程

1. 创建异形子窗口或悬浮窗，设置窗口的位置、大小等属性，设置窗口加载的page页面。
2. 根据待实现的异形形状，计算出与其对应的二维数组掩码，对目标窗口设置该掩码。
3. 根据逻辑需要，显示目标异形窗口。

说明

掩码windowMask二维数组的大小需要与窗口初始宽、高一致，且每项值只能是0或1，否则设置的形状不会生效。

## 图形形状窗口

### 场景案例

待开发的异形窗口，其形状是具有一定规则的几何图形，通过描述语言能得到精确且唯一的形状。本节以下面两种形状的实现为例进行说明：直径为500的圆形；底500、高500的等腰三角形。

### 创建子窗口

在得到异形窗口前，需要先创建一个默认的矩形窗口，开发步骤如下：

1. 为使用setWindowMask()等接口，需要额外[配置syscap.json文件](../harmonyos-references/syscap.md#加入自定义syscap)，在模块/src/main目录下，创建syscap.json文件，填入以下内容：

   ```
   1. // entry/src/main/syscap.json
   2. {
   3. "devices": {
   4. "general": [
   5. "2in1"
   6. ]
   7. },
   8. "development": {
   9. "addedSysCaps": [
   10. "SystemCapability.Window.SessionManager"
   11. ]
   12. }
   13. }
   ```
2. 具体代码中，使用createSubWindow()创建子窗口（参考[设置应用子窗口](../harmonyos-guides/application-window-stage.md#设置应用子窗口)），或使用createWindow()接口创建悬浮窗（参考[设置悬浮窗受限开放](../harmonyos-guides/application-window-stage.md#设置全局悬浮窗受限开放)），设置窗口的位置、大小及其他属性等，然后使用setUIContent()接口设置窗口加载的page页面。

   ```
   1. windowStage = AppStorage.get('windowStage');
   2. if (windowStage === null) {
   3. hilog.error(0x0000, 'Sample', 'Failed to create the subwindow. Cause: windowStage is null');
   4. return;
   5. }
   6. const windowWidth = 500;
   7. const windowHeight = 500;
   8. try {
   9. subWindow = await windowStage!.createSubWindow('mySubWindow');
   10. subWindow.moveWindowTo(300, 300);
   11. subWindow.resize(windowWidth, windowHeight);
   12. subWindow.setUIContent('pages/SubPage');
   13. // ...
   14. subWindow.showWindow();
   15. } catch (exception) {
   16. hilog.error(0x0000, 'Sample', 'Failed to create sub window. Cause: ' + JSON.stringify(exception));
   17. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/pages/Index.ets#L39-L71)

### 设置窗口形状

1. 根据要实现的异形窗口形状，计算二维数组掩码windowMask。
   * 以下是以原矩形中点为圆心、直径为500的圆。最终效果见圆形子窗口效果。

     ```
     1. function fillCircle(array: number[][], x: number, y: number, radius: number): void {
     2. for (let i = x - radius; i <= x + radius; i++) {
     3. for (let j = y - radius; j <= y + radius; j++) {
     4. const distSquared = (i - x)**2 + (j - y)**2;
     5. if (distSquared <= radius**2 && i >= 0 && j >= 0 && i < array.length && j < array[0].length) {
     6. array[i][j] = 1;
     7. }
     8. }
     9. }
     10. }

     12. async function getCircleMask(width: number, height: number): Promise<number[][]> {
     13. const radius = Math.min(width, height) / 2;
     14. const maskArray: number[][] = new Array(height).fill(null).map(() => new Array(width).fill(0));
     15. fillCircle(maskArray, height / 2, width / 2, radius);
     16. return maskArray;
     17. }
     ```

     [WindowUtils.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/utils/WindowUtils.ets#L41-L57)
   * 以下以原矩形宽为底边、原矩形高为高的等腰三角形。最终效果见三角形子窗口效果。

     ```
     1. function fillTriangle(array: number[][], base: number, height: number): void {
     2. // i < height-10 in order to remove the round corner
     3. for (let i = 0; i < height - 10; i++) {
     4. for (let j = 0; j < base; j++) {
     5. if (j >= base / 2 - base / 2 * i / height && j <= base / 2 + base / 2 * i / height) {
     6. array[i][j] = 1;
     7. }
     8. }
     9. }
     10. }

     12. async function getTriangleMask(width: number, height: number): Promise<number[][]> {
     13. const maskArray: number[][] = new Array(height).fill(null).map(() => new Array(width).fill(0));
     14. fillTriangle(maskArray, width, height);
     15. return maskArray;
     16. }
     ```

     [WindowUtils.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/utils/WindowUtils.ets#L22-L37)
2. 使用setWindowMask(windowMask)接口，设置窗口形状。

   ```
   1. async function setWindowShape(win: window.Window, width: number,
   2. height: number, getMaskFunc: (w: number, h: number, picPath?: string) => Promise<number[][]>,
   3. picPath?: string): Promise<void> {
   4. const windowMask = await getMaskFunc(width, height, picPath);
   5. if (canIUse('SystemCapability.Window.SessionManager')) {
   6. try {
   7. win.setWindowMask(windowMask);
   8. } catch (e) {
   9. let err = e as BusinessError;
   10. hilog.error(0x0000, 'Simple', `failed code=${err.code}, message=${err.message}`);
   11. }
   12. } else {
   13. hilog.info(0x0000, 'Simple', 'can not use SessionManager syscap');
   14. }
   15. }

   17. /**
   18. * Set the window with circle shape
   19. * @param win The target window
   20. * @param width The original window width
   21. * @param height The original window height
   22. */
   23. export async function setWindowCircleShape(win: window.Window, width: number,
   24. height: number): Promise<void> {
   25. setWindowShape(win, width, height, getCircleMask)
   26. }

   28. /**
   29. * Set the window with triangle shape
   30. * @param win The target window
   31. * @param width The original window width
   32. * @param height The original window height
   33. */
   34. export async function setWindowTriangleShape(win: window.Window, width: number,
   35. height: number): Promise<void> {
   36. setWindowShape(win, width, height, getTriangleMask)
   37. }
   ```

   [WindowUtils.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/utils/WindowUtils.ets#L84-L122)
3. 使用showWindow()接口显示异形子窗口。

   ```
   1. subWindow.showWindow();
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/pages/Index.ets#L67-L67)

### 实现效果

**图1** 圆形子窗口效果  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vukPWxrOSFaseXZYPrbX8A/zh-cn_image_0000002229337273.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=6FA39027064A8344D647E503D04FA03AD3B8CCBCF1E5BF4D8678D716C81A84C8 "点击放大")

**图2** 三角形子窗口效果  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/cwpF7jf2RHGrORTyN51icA/zh-cn_image_0000002194011476.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=9C46714F19BA63B61B98A61145E0EAFBD6140C01BC0373F0B9E2BD722ABCFBA4 "点击放大")

## 不规则形状窗口

### 场景案例

待开发的异形窗口，呈现出不规则的形状。这种情况通常先由设计人员提供图形文件，开发人员以文件为输入，基于ArkUI提供的图片处理能力，转化为相应的形状掩码，最后实现不规则的窗口形状。

**图3** 不规则示例图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/hGRqj_cfS9W_P2H8ZbTJGA/zh-cn_image_0000002229451765.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=54D5DF1BF46808C574E6B9ED68F6E0D4B053A47602D84A04283261837E53143E)

本节以上图为例说明不规则形状窗口的实现过程。

### 开发步骤

首先同样需要先[创建子窗口](bpta-2in1-window-shape.md#section10343161441819)，然后再依以下步骤开发。

1. 读取图片文件，将其转化为pixelMap数据。

   ```
   1. /**
   2. * Convert image to PixelMap object
   3. */
   4. export async function image2PixelMap(Context: Context, icon: string, w: number, h: number): Promise<image.PixelMap> {
   5. try {
   6. const rawFileDescriptor: resourceManager.RawFileDescriptor = Context.resourceManager.getRawFdSync(icon);
   7. const imageSource: image.ImageSource = image.createImageSource(rawFileDescriptor);
   8. const pixelMap: Promise<PixelMap> = imageSource.createPixelMap({
   9. editable: false,
   10. desiredPixelFormat: image.PixelMapFormat.BGRA_8888,
   11. desiredSize: { width: w, height: h }
   12. });
   13. imageSource.release()
   14. return pixelMap;
   15. } catch (e) {
   16. let err = e as BusinessError;
   17. hilog.error(0x0000, 'Simple', `failed code=${err.code}, message=${err.message}`);
   18. }
   19. return new Promise<image.PixelMap>((resolve, reject) => {
   20. reject('null')
   21. });
   22. }
   ```

   [ImageUtils.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/utils/ImageUtils.ets#L23-L45)
2. 从pixelMap数据中取出颜色信息数组，将每个像素的透明度单独提取至allPixels，再转化生成为对应形状的二维数组掩码maskArray。

   ```
   1. export async function getPicMask(Context: Context,width: number, height: number, picPath: string): Promise<number[][]> {
   2. const maskArray: number[][] = new Array(height).fill(null).map(() => new Array(width).fill(0));
   3. const pixelMap: image.PixelMap = await image2PixelMap(Context, picPath, width, height);
   4. const pixelArrayBuffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
   5. await pixelMap.readPixelsToBuffer(pixelArrayBuffer);
   6. const allPixels: number[] = [];
   7. const unit8Pixels: Uint8Array = new Uint8Array(pixelArrayBuffer);
   8. for (let i = 0, j = 0; i < unit8Pixels.length; i += 4, j++) {
   9. // unit8Pixels[i+3] is alpha channel of BGRA_8888
   10. allPixels[j] = unit8Pixels[i + 3] > 0 ? 1 : 0;
   11. }
   12. pixelMap.release()
   13. let k = 0;
   14. for (let i = 0; i < width; i++) {
   15. for (let j = 0; j < height; j++) {
   16. maskArray[i][j] = allPixels[k++];
   17. }
   18. }
   19. return maskArray;
   20. }
   ```

   [WindowUtils.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/utils/WindowUtils.ets#L61-L80)
3. 使用setWindowMask(windowMask)接口，设置窗口形状。

   ```
   1. async function setWindowShape(win: window.Window, width: number,
   2. height: number, getMaskFunc: (w: number, h: number, picPath?: string) => Promise<number[][]>,
   3. picPath?: string): Promise<void> {
   4. const windowMask = await getMaskFunc(width, height, picPath);
   5. if (canIUse('SystemCapability.Window.SessionManager')) {
   6. try {
   7. win.setWindowMask(windowMask);
   8. } catch (e) {
   9. let err = e as BusinessError;
   10. hilog.error(0x0000, 'Simple', `failed code=${err.code}, message=${err.message}`);
   11. }
   12. } else {
   13. hilog.info(0x0000, 'Simple', 'can not use SessionManager syscap');
   14. }
   15. }
   16. /**
   17. * Set the window with pic shape
   18. * @param win The target window
   19. * @param width The original window width
   20. * @param height The original window height
   21. * @param picPath The pic path in rawfile
   22. */
   23. export async function setWindowPicShape(win: window.Window, Context: Context, width: number,
   24. height: number, picPath: string): Promise<void> {
   25. setWindowShape(win, width, height, (w, h, picPath) => {
   26. return getPicMask(Context,w, h, picPath!)
   27. }, picPath)
   28. }
   ```

   [WindowUtils.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/utils/WindowUtils.ets#L85-L138)
4. 使用showWindow()接口显示异形子窗口。

   ```
   1. subWindow.showWindow();
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/special-window-shape/blob/master/entry/src/main/ets/pages/Index.ets#L67-L67)

### 实现效果

**图4** 不规则形状子窗口效果  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/nAGt5YKeSTCgj1JIERicnQ/zh-cn_image_0000002193851884.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=C5A512A70E577E4C16665A62359899181565B9F648B037CD8D492BC37ACA211A)

## **示例代码**

* [实现PC/2in1异形窗口](https://gitcode.com/harmonyos_samples/special-window-shape)
