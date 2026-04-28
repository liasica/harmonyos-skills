---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi_game
title: 多设备游戏界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备游戏界面
category: best-practices
scraped_at: 2026-04-28T08:21:33+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:0dace571d6ea6ff04c214f3d0fe2d3cbde94a8bfaf67761c0fe9a49b867c26f4
---

## 概述

本文选择游戏类应用作为典型案例，详细介绍“一多”策略在实际开发中的应用。游戏类应用由于其较强的互动性和操作性，特别重视用户的沉浸式体验，并且在大屏设备上，这类应用能够展现更广阔的视野，提供更加高效便捷的交互体验。

* 关键场景：

  Native一多适配：通过监听断点变化，动态调整页面布局和元素。开发者可以从ArkTS侧获取断点值，并传入Native侧，使Native侧根据不同的断点值适配不同的页面及效果。

  安全区避让：在游戏类应用中，为确保用户的沉浸式体验，导航条会自动隐藏。这不仅增加可用的屏幕空间，还减少了视觉干扰，使用户更加专注于游戏本身。

  窗口旋转：由于不同游戏可能有特定的窗口方向偏好，可根据应用需求，自定义设置窗口的旋转方向，这对于游戏类应用尤其重要。

游戏类应用需要适配多种屏幕尺寸，当前游戏类应用支持的主要产品形态包括手机、折叠屏和平板三种。下文将围绕这几种产品形态展开，同时从[UX设计](bpta-multi_game.md#section163791453125612)、[页面开发](bpta-multi_game.md#section1383916515715)两个角度分析介绍“一多”游戏类应用在开发过程中的关键场景实现方案。

* [UX设计](bpta-multi_game.md#section163791453125612)章节介绍游戏类应用的页面逻辑与通用设计要点，提供可直接应用于实际项目中的设计模板与建议。
* [页面开发](bpta-multi_game.md#section1383916515715)章节涵盖页面区域划分、一多适配、安全区域避让及屏幕旋转设置四个方面的详细指导，帮助开发者理解和实现游戏类应用中的关键开发场景。

## UX设计

**断点设计策略**

游戏视野的大小对用户的游戏体验是一个重要的影响因素。在不同的设备和屏幕尺寸下，合理适配视野可以为用户提供更佳的游戏体验。以下是针对不同设备和屏幕尺寸的游戏视野适配策略：

1. 手机（sm）

   基础视野。
2. 双折叠展开态（md）

   双折叠设备提供独特的挑战与机遇。在展开状态下，开发者可利用更大的屏幕空间扩展游戏视野，以增强游戏的沉浸感和信息显示，例如战绩展示。

   推荐做法：

   * 基于手机视野，横向适当缺失部分视野，垂直方向扩充部分视野，确保补偿和缺失的面积相似，调整后整体视野同手机相似。
   * 手机与双折叠展开态的横向视野保持一致，垂直方向拓展视野或利用留黑区域显示辅助信息，而非简单留黑，以优化屏幕空间利用，提升用户体验。
3. 平板（lg）

   平板设备的布局策略与双折叠展开态类似：
   * 基于手机视野，横向适当缺失部分视野，垂直方向扩充部分视野，确保补偿和缺失的面积相似，调整后整体视野同手机相似。
   * 手机与平板的横向视野保持一致，垂直方向扩展视野或使用留黑区域显示辅助信息，建议避免上下留黑。
4. 特殊考虑

   对于休闲类游戏，尤其是垂直屏幕模式，可在双折叠展开态和平板上适当放大游戏画面，以适应更大的屏幕空间。

通过以上策略，开发者可根据不同设备的特点优化游戏视野，进而提高游戏的可玩性和用户体验。详细设计建议参考下方的游戏类多设备响应式设计。

**游戏类多设备响应式设计**

游戏类的多设备响应式设计指南，[点击访问](../design-guides/games-0000001930189974.md)。

## 页面开发

本章阐述游戏类应用如何利用“一多”布局能力，实现页面层级的统一页面、多端适配。下文将从四个方面详细解释页面区域的布局能力，以帮助开发者完成游戏类应用的一多开发与适配。

### 游戏页分区

游戏类应用的首页主要展示全屏游戏区域，即游戏渲染区域。通常使用XComponent组件来渲染OpenGL绘制的图形结果。

* 从游戏页划分出游戏渲染区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

* 对游戏渲染区域的实现方案包括以下三个关键场景：
  1. Native一多适配：通过监听断点变化，动态调整页面布局和元素。开发者可以从ArkTS侧获取断点值并传入Native侧，使Native侧能够根据不同的断点值适配相应的页面及效果。
  2. 安全区避让：在游戏类应用中，为确保用户的沉浸式体验，需隐藏状态栏及导航条。这样不仅增加了可用的屏幕空间，还减少了视觉干扰，使用户更加专注于游戏本身。
  3. 窗口旋转：不同游戏可能有特定的窗口方向偏好，可根据应用需求自定义设置窗口旋转方向，这在游戏类应用中尤为重要。

### Native一多适配

在HarmonyOS上，[XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)控件常用于显示相机预览流和绘制的游戏画面。它可以通过与[NativeWindow](../harmonyos-guides/native-window-guidelines.md)结合使用，创建OpenGL开发环境，并将OpenGL绘制的图形自定义渲染到页面的XComponent控件中进行展示。为了确保游戏在不同设备和屏幕尺寸下的适配效果，可以采取以下两种方法：

1. 获取断点信息以适配不同页面效果：在HarmonyOS中，可以通过监听设备屏幕尺寸的变化来获取断点信息。这些信息能够帮助开发者根据屏幕尺寸的变化调整游戏的画面布局和元素大小。
2. 监听surface大小变化并调整绘制区域：在使用OpenGL进行绘制时，surface的尺寸直接影响绘制区域的大小。因此，监听surface尺寸的变化，并据此调整绘制区域的大小，是实现多设备适配的关键。

**获取断点信息**

将从ArkTS侧获取的断点值传递给Native侧，Native侧可以根据游戏设计需求，在不同的断点下实现不同的页面效果。本案例仅展示断点值的传递过程，适配过程可根据不同需求在Native侧自行完成。

1. 使用UIContext中提供的[getWindowWidthBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowwidthbreakpoint13)和[getWindowHeightBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowheightbreakpoint13)接口，在EntryAbility文件的windowStage.loadContent()页面加载函数中直接获取横向和纵向的断点值，并监听窗口大小变化以获取新的断点值。更多获取断点策略可参考[断点实现原理](bpta-multi-device-responsive-layout.md#section191481952131414)。

   ```
   1. export default class EntryAbility extends UIAbility {
   2. public uiContext?: UIContext;
   3. public onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
   4. let widthBp: WidthBreakpoint = this.uiContext!.getWindowWidthBreakpoint();
   5. AppStorage.setOrCreate('currentWidthBreakpoint', widthBp);
   6. let heightBp: HeightBreakpoint = this.uiContext!.getWindowHeightBreakpoint();
   7. AppStorage.setOrCreate('currentHeightBreakpoint', heightBp);
   8. AppStorage.setOrCreate('windowHeight', windowSize.height);
   9. AppStorage.setOrCreate('windowWidth', windowSize.width);
   10. };
   11. // ...

   13. onWindowStageCreate(windowStage: window.WindowStage) {
   14. // Main window is created, set main page for this ability
   15. // ...
   16. windowStage.loadContent('pages/Index', (err, data) => {
   17. // ...
   18. windowStage.getMainWindow((err: BusinessError, data) => {
   19. if (err.code) {
   20. Logger.error('Failed to obtain the main window. Cause: %{public}s', JSON.stringify(err) ?? '');
   21. return;
   22. }
   23. // Window size acquisition and monitoring.
   24. let properties = data.getWindowProperties();
   25. AppStorage.setOrCreate('windowHeight', properties.windowRect.height);
   26. AppStorage.setOrCreate('windowWidth', properties.windowRect.width);
   27. // Breakpoint acquisition and listening.
   28. this.uiContext = data.getUIContext();
   29. let widthBp: WidthBreakpoint = this.uiContext.getWindowWidthBreakpoint();
   30. let heightBp: HeightBreakpoint = this.uiContext.getWindowHeightBreakpoint();
   31. AppStorage.setOrCreate('currentWidthBreakpoint', widthBp);
   32. AppStorage.setOrCreate('currentHeightBreakpoint', heightBp);
   33. data.on('windowSizeChange', this.onWindowSizeChange);
   34. // ...
   35. })
   36. });
   37. }

   39. // ...
   40. };
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L23-L156)
2. 页面获取断点值，监听断点变化并传入Native侧。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // ...
   5. // Define the variables passed into the Native side.
   6. @State cutoutAreas: Areas = {
   7. top: 0,
   8. right: 0,
   9. bottom: 0,
   10. left: 0,
   11. heightBreakpoint: 0,
   12. widthBreakpoint: 0
   13. };
   14. // ...
   15. // Watching the changes in horizontal and vertical breakpoint values.
   16. @StorageLink('currentHeightBreakpoint') @Watch('breakPointChange') heightBreakpoint: HeightBreakpoint =
   17. HeightBreakpoint.HEIGHT_SM;
   18. @StorageLink('currentWidthBreakpoint') @Watch('breakPointChange') widthBreakpoint: WidthBreakpoint =
   19. WidthBreakpoint.WIDTH_XS;
   20. // ...

   22. // Breakpoint change, triggering value transfer.
   23. breakPointChange() {
   24. this.cutoutAreas.heightBreakpoint = this.heightBreakpoint;
   25. this.cutoutAreas.widthBreakpoint = this.widthBreakpoint;
   26. // Encapsulate the Native method and pass in a breakpoint.
   27. tetrahedron_napi.objectPassing(this.cutoutAreas);
   28. }
   29. // ...
   30. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/pages/Index.ets#L82-L271)

**监听Surface大小变化**

XComponent持有一个Surface，该Surface的默认位置及大小与XComponent组件相同。在Native层获取Native XComponent实例，作为ArkTS层和Native层XComponent绑定的桥梁。利用Native XComponent提供的接口注册XComponent的生命周期和事件回调，最后通过调用[NativeWindow](../harmonyos-guides/native-window-guidelines.md)等接口开发自定义绘制内容，并申请和提交Buffer到图形队列，以此方式将自定义绘制内容传送至XComponent持有的Surface。具体XComponent的开发流程可参考[自定义渲染](../harmonyos-guides/napi-xcomponent-guidelines.md)。

在Native XComponent的事件回调中，OnSurfaceCreated()和OnSurfaceChanged()两个接口分别在Surface创建和Surface大小变化时进行回调，因此在适配不同屏幕尺寸设备时，应重点关注这两个接口。

* OnSurfaceCreated()：Surface创建时进行回调。
* OnSurfaceChanged()：Surface大小变化时进行回调。具体使用场景包括游戏横竖屏切换导致的Surface宽高变化，或双折叠设备在折叠和展开状态变化下的Surface大小变化。

在OnSurfaceCreated()和OnSurfaceChanged()回调中，使用[OH\_NativeXComponent\_GetXComponentSize()](../harmonyos-references/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_getxcomponentsize)获取XComponent持有的Surface的大小，且每次Surface改变后都会重新获取对应的宽高，并通过自定义的reSizeWindow()方法，重新设置OpenGL绘制区域的大小，以实现对不同设备和屏幕尺寸的良好适配。

```
1. void AppNapi::OnSurfaceCreated(OH_NativeXComponent* component, void* window)
2. {
3. LOGE("AppNapi::OnSurfaceCreated");
4. OH_NativeXComponent_RegisterOnFrameCallback(component, OnFrameCB);
5. // Get surface size.
6. int32_t ret = OH_NativeXComponent_GetXComponentSize(component, window, &width_, &height_);
7. // Draw the image to be displayed on the window and set the size of the drawing area.
8. LOGE("Offset : x = %{public}f, y = %{public}f ", x_, y_);
9. if (ret == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
10. tetrahedron_->Init(window, width_, height_);
11. tetrahedron_->reSizeWindow(width_, height_);
12. tetrahedron_->Update(angleX_, angleY_);
13. isCreated_++;
14. xcHeight_ = height_;
15. xcWidth_ = width_;

17. LOGE("AppNapi::OnSurfaceCreated success ");
18. } else {
19. LOGE("AppNapi::OnSurfaceCreated failed");
20. }
21. }

23. void AppNapi::OnSurfaceChanged(OH_NativeXComponent* component, void* window)
24. {
25. LOGE("AppNapi::OnSurfaceChanged");
26. // Retrieve surface size again
27. int32_t ret = OH_NativeXComponent_GetXComponentSize(component, window, &width_, &height_);
28. int32_t ret1;

30. // Set the size of the drawing area.
31. if (ret == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
32. tetrahedron_->reSizeWindow(width_, height_);
33. xcHeight_ = height_;
34. xcWidth_ = width_;
35. LOGE("after width = %{public}d, height = %{public}d", xcWidth_, xcHeight_);
36. ret1= OH_NativeXComponent_GetXComponentOffset(component, window, &x_, &y_);
37. off_x = x_;
38. off_y = y_;
39. // ...
40. }
41. }
```

[app\_napi.cpp](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/cpp/app_napi.cpp#L202-L251)

### 安全区避让

游戏类应用主要采用沉浸式界面设计。[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)主要是通过调整状态栏、应用界面和导航条的显示效果，以减少这些系统界面给用户带来的突兀感，从而提供更好的UI体验。

为了获得更好的游戏体验，游戏应用不仅需要设置沉浸式界面，还需要扩展布局并隐藏避让区，即隐藏状态栏和导航条（示意图所示的导航条在真实使用场景下已隐藏）。界面元素示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/65owQBqkTX-Y4KWfvxoaYw/zh-cn_image_0000002276709524.png?HW-CC-KV=V1&HW-CC-Date=20260428T002130Z&HW-CC-Expire=86400&HW-CC-Sign=0CDECF98E3950A11E52A6E26324658DF83D0CF4CE9EBEDE531AA13840C82E4B9 "点击放大")

在这样的场景下，挖孔区（即摄像头区域）可能会遮挡部分页面信息或用户操作按钮。因此，为了优化用户体验，操作按钮需要移动到挖孔区的另一侧，同时避免侧边出现大量留白，需要获取挖孔区域并进行相应的避让设计。具体步骤分为以下三步：

**应用扩展布局，隐藏避让区**

首先调用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口布局为沉浸式布局，接着调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)接口设置状态栏和导航条的具体显示/隐藏状态，此场景下将其设置为隐藏。

```
1. onWindowStageCreate(windowStage: window.WindowStage) {
2. // ...

4. try {
5. // Set the main window to immersive and hide the navigation bar.
6. windowStage.getMainWindowSync().setWindowLayoutFullScreen(true);
7. windowStage.getMainWindowSync().setWindowSystemBarEnable([]);
8. } catch (error) {
9. let err = error as BusinessError;
10. hilog.error(0x0000, 'EntryAbility',
11. `Failed to set the window state. Error code=${err.code}, message=${err.message}`);
12. }

14. // ...
15. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L53-L135)

**挖孔区获取**

1. 使用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口获取刘海屏区域，一般为前置摄像头位置，并使用[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听其位置信息的变化。

   ```
   1. public onAvoidAreaChange: (avoidArea: window.AvoidAreaOptions) => void = (avoidArea: window.AvoidAreaOptions) => {
   2. if (avoidArea.type === window.AvoidAreaType.TYPE_CUTOUT) {
   3. AppStorage.setOrCreate('cutout', avoidArea);
   4. }
   5. }

   7. // ...

   9. onWindowStageCreate(windowStage: window.WindowStage) {
   10. // ...
   11. windowStage.getMainWindow((err: BusinessError, data) => {
   12. // ...
   13. windowStage.loadContent('pages/Index', (err, data) => {
   14. // ...
   15. // Monitor changes in the location of the cutout area.
   16. let avoidArea: window.AvoidArea = data.getWindowAvoidArea(window.AvoidAreaType.TYPE_CUTOUT);
   17. this.onAvoidAreaChange({ type: window.AvoidAreaType.TYPE_CUTOUT, area: avoidArea });
   18. data.on('avoidAreaChange', this.onAvoidAreaChange);
   19. })
   20. });
   21. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L35-L136)
2. 监听到挖孔区位置变化后，计算避让区域的top、bottom、left和right。

   ```
   1. @StorageLink('cutout') @Watch('cutoutChange') avoidAreas: window.AvoidAreaOptions | undefined = undefined;
   2. @StorageLink('windowHeight') windowHeight: number = 0;
   3. @StorageLink('windowWidth') windowWidth: number = 0;
   4. // ...
   5. cutoutChange() {
   6. let topPX = getTop(this.avoidAreas);
   7. let rightPX = getRight(this.avoidAreas, this.windowWidth);
   8. let bottomPX = getBottom(this.avoidAreas, this.windowHeight);
   9. let leftPX = getLeft(this.avoidAreas);

   11. // ...
   12. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/pages/Index.ets#L111-L157)

   ```
   1. function getTop(avoidArea: window.AvoidAreaOptions | undefined): number {
   2. let result: number = 0;
   3. if (avoidArea !== undefined) {
   4. if (avoidArea.area.topRect.height) {
   5. result = avoidArea.area.topRect.top + avoidArea.area.topRect.height;
   6. }
   7. } else {
   8. hilog.error(0x0000, '3D', 'Can not get TopSafeAreaPixel, avoidArea visible false');
   9. }
   10. return result;
   11. }

   13. function getBottom(avoidArea: window.AvoidAreaOptions | undefined, windowHeight: number): number {
   14. let result: number = 0;
   15. if (avoidArea !== undefined) {
   16. if (avoidArea.area.bottomRect.height) {
   17. result = windowHeight - avoidArea.area.bottomRect.top;
   18. }
   19. } else {
   20. hilog.error(0x0000, '3D', 'Can not get BottomSafeAreaPixel, avoidArea visible false');
   21. }
   22. return result;
   23. }

   25. function getLeft(avoidArea: window.AvoidAreaOptions | undefined): number {
   26. let result: number = 0;
   27. if (avoidArea !== undefined) {
   28. if (avoidArea.area.leftRect.width) {
   29. result = avoidArea.area.leftRect.left + avoidArea.area.leftRect.width;
   30. }
   31. } else {
   32. hilog.error(0x0000, '3D', 'Can not get LeftSafeAreaPixel, avoidArea visible false');
   33. }
   34. return result;
   35. }

   37. function getRight(avoidArea: window.AvoidAreaOptions | undefined, windowWidth: number): number {
   38. let result: number = 0;
   39. if (avoidArea !== undefined) {
   40. if (avoidArea.area.rightRect.width) {
   41. result = windowWidth - avoidArea.area.rightRect.left;
   42. }
   43. } else {
   44. hilog.error(0x0000, '3D', 'Can not get RightSafeAreaPixel, avoidArea visible false');
   45. }
   46. return result;
   47. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/pages/Index.ets#L32-L78)

**安全区域避让**

在获得挖孔避让区域后，可以在Native侧的surface上设置避让，或者在ArkTS侧进行避让。本篇文章将采用ArkTS侧避让，并将避让区域的值传递到Native侧。开发者可以根据游戏设计需求，使用传入的值在Native侧自行适配。

* ArkTS侧避让

  获取到挖孔区域位置后，设置页面的padding值为该区域大小，可实现安全区域避让的效果。

  ```
  1. @State localPadding: LocalizedPadding = { top: LengthMetrics.vp(0), start: LengthMetrics.vp(0) };
  2. // ...
  3. @StorageLink('cutout') @Watch('cutoutChange') avoidAreas: window.AvoidAreaOptions | undefined = undefined;
  4. // ...
  5. cutoutChange() {
  6. let topPX = getTop(this.avoidAreas);
  7. let rightPX = getRight(this.avoidAreas, this.windowWidth);
  8. let bottomPX = getBottom(this.avoidAreas, this.windowHeight);
  9. let leftPX = getLeft(this.avoidAreas);

  11. // ...

  13. this.localPadding = {
  14. top: LengthMetrics.px(topPX),
  15. end: LengthMetrics.px(rightPX),
  16. bottom: LengthMetrics.px(bottomPX),
  17. start: LengthMetrics.px(leftPX)
  18. }
  19. // ArkTS2Native
  20. tetrahedron_napi.objectPassing(this.cutoutAreas);
  21. }

  23. // ...

  25. build() {
  26. // ...
  27. .padding(this.localPadding)
  28. }
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/pages/Index.ets#L100-L268)
* Native侧避让

  定义数据传递函数，用于将避让区域从ArkTS侧传输到Native侧，后续可根据应用需求自定义实现区域避让。更多数据交互可参考[object类型数据交互](bpta-complex-type-pass.md#section412816619212)。

  ```
  1. // Responsible for transferring data from ArkTS to Native.
  2. static napi_value objectPassingTs2Napi(napi_env env, napi_callback_info info)
  3. {
  4. size_t argc = 1;
  5. napi_value args[1];
  6. napi_get_cb_info(env, info, &argc, args, NULL, NULL);

  8. if (argc < 1) {
  9. napi_throw_error(env, NULL, "Wrong number of arguments");
  10. return NULL;
  11. }

  13. napi_value obj = args[0];
  14. napi_value keys;
  15. napi_get_property_names(env, obj, &keys); // Get all attribute names.

  17. uint32_t length;
  18. napi_get_array_length(env, keys, &length); // Obtain the number of attributes.

  20. for (uint32_t i = 0; i < length; ++i) {
  21. napi_value key;
  22. napi_get_element(env, keys, i, &key); // Get the i-th attribute name.

  24. // Convert attribute names to strings.
  25. char keyStr[128];
  26. size_t keyLen;
  27. napi_get_value_string_utf8(env, key, keyStr, sizeof(keyStr), &keyLen);

  29. // Get attribute values.
  30. napi_value value;
  31. napi_get_property(env, obj, key, &value);

  33. // Determine the type of attribute value and process it.
  34. napi_valuetype type;
  35. napi_typeof(env, value, &type);

  37. if (type == napi_string) {
  38. char valueStr[4];
  39. size_t valueLen;
  40. napi_get_value_string_utf8(env, value, valueStr, sizeof(valueStr), &valueLen);
  41. }
  42. if (type == napi_number) {
  43. double num;
  44. napi_get_value_double(env, value, &num);
  45. }
  46. }
  47. return NULL;
  48. }

  50. // Define data transfer function.
  51. static napi_value objectPassing(napi_env env, napi_callback_info info)
  52. {
  53. objectPassingTs2Napi(env, info);
  54. return nullptr;
  55. }
  ```

  [module.cpp](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/cpp/module.cpp#L29-L83)

### 窗口旋转

由于不同游戏可能有特定的窗口方向偏好，通常仅支持横屏或竖屏，因此可以根据应用需求，使用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口自定义设置窗口的旋转方向。这一点对于游戏类应用较为重要。本篇文章以仅支持竖屏旋转为例，介绍如何实现游戏类应用的窗口旋转设置。

```
1. // Automatically rotate vertically following the sensor.
2. let orientation = window.Orientation.AUTO_ROTATION_PORTRAIT;
3. try {
4. windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
5. if (err.code) {
6. Logger.error('Failed to set window orientation. Cause: %{public}s', JSON.stringify(err) ?? '');
7. return;
8. }
9. Logger.info('Succeeded in setting window orientation. Data: %{public}s');
10. })
11. } catch (exception) {
12. Logger.error('Failed to set window orientation. Cause: %{public}s', JSON.stringify(exception) ?? '');
13. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/ndk-opengl/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L83-L95)

## 示例工程

* [多设备游戏界面](https://gitcode.com/harmonyos_samples/ndk-opengl)
