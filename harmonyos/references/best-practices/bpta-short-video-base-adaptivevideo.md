---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-short-video-base-adaptivevideo
title: 全屏短视频自适应缩放和沉浸
breadcrumb: 最佳实践 > 行业场景解决方案 > 影音娱乐 > 全屏短视频自适应缩放和沉浸
category: best-practices
scraped_at: 2026-09-02T15:03:20+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:fce298844a60a8b9b95ba9e12dd6cd9ad0ef4ec078d56cf2d63ae194aa409757
---

## 概述

短视频是一种时长较短、内容直观的视频内容形式，单条视频通常为数秒至数分钟。为提升用户的观感体验，短视频页面常采用沉浸式模式展示视频内容。由于设备类型和屏幕尺寸的差异，不同设备短视频页面的沉浸效果、旋转策略可能会有所不同，开发者需额外适配。

对此，[多设备场景库（multidevicelibrary）](https://gitcode.com/HarmonyOS_Samples/MultiDeviceLibrary)提供了完整的适配方案，能够使短视频页面在遵循当前主流沉浸和旋转规则的同时，达到多端一致的观感体验，简化短视频页面开发。下文将介绍多设备场景库（multidevicelibrary）支持的短视频页面开发适配场景，主要内容如下：

1. [短视频自适应沉浸](bpta-short-video-base-adaptivevideo.md#section2355143519245)：介绍短视频布局场景层、视频自适应层的规则逻辑。
2. [短视频自适应旋转](bpta-short-video-base-adaptivevideo.md#section1689619568351)：介绍用户改变设备的持握方向时，短视频常规播放及横屏视频全屏播放两种场景的旋转策略。
3. [开发步骤](bpta-short-video-base-adaptivevideo.md#section921165310471)：介绍开发者如何使用多设备场景库，实现短视频的多端自适应缩放和沉浸模式展示。
4. [示例代码](bpta-short-video-base-adaptivevideo.md#section1629315813517)：提供多设备场景库供开发者下载使用，可结合本文内容配合使用。

## 短视频自适应沉浸

### 场景描述

短视频沉浸是一种通过全屏展示、弱化界面干扰，让用户专注于视频内容的呈现模式。在开发过程中，通常结合屏幕适配、视频裁剪等技术，以增强视觉沉浸感。在当前主流的沉浸式策略中，短视频的呈现方式会根据设备屏幕尺寸进行调整：大屏设备通常会完整呈现视频内容，而小屏设备则根据窗口比例对视频进行适当裁剪，以提升用户的沉浸体验。基于上述策略，短视频在各类设备上的实现效果如下表所示：

|  |  |  |
| --- | --- | --- |
| 设备 | 直板机 | 双折叠展开态 |
| 实现效果图 |  |  |
| 设备 | 平板 | 电脑 |
| 实现效果图 |  |  |

### 设计原则

典型的短视频应用界面由视频区域、顶部状态栏、底部Tab栏、右侧操作栏等元素组成，视频内容通常为9:16竖屏格式。当前沉浸规则适用于所有宽高比的视频，特别对9:16区间（9:16.1 ~ 9:15.9）的视频进行了特殊的自适应与裁剪处理。

短视频沉浸式布局遵循以下两个原则：

1. **9:16竖向视频优先上下沉浸**：对于标准9:16竖屏视频，尽可能让其上下方向延伸到屏幕边缘沉浸显示，最大化利用屏幕空间，避免上下留黑浪费显示区域。
2. **视频裁剪率控制在13%以下**：在自适应填充过程中，保证画面裁切率不高于13%，保留视频主体内容，防止因过度裁切影响观看体验。

**说明** 

规则中判断视频是否为9:16竖屏视频时，采用的并非严格的9:16单一比值，而是一个宽容区间[9:16.1, 9:15.9]。

视频在编码、转码、裁剪过程中，宽高比往往存在微小的误差。使用区间匹配可以兼容这些实际生产中的比例波动，同时区间范围控制在±0.1的比例偏差内，确保不会将非9:16视频误判为标准竖屏视频，从而保证沉浸规则的准确性。

多设备场景库（multidevicelibrary）中综合考虑视频尺寸及页面容器尺寸等信息，根据沉浸规则计算沉浸式布局方案，并依此生成视频的尺寸与位置建议。在实现上拆分为两层计算：

* 短视频布局场景层（AdaptiveShortVideoScene）：处理顶部状态栏、底部Tab栏的沉浸决策和视频区域计算。短视频场景下，页面通常包含顶部状态栏、底部Tab栏等UI元素，需要根据设备屏幕尺寸动态决定视频区域是否延伸到这些区域。
* 视频自适应层（AdaptiveVideoSurface）：在视频渲染中，如何将一个任意宽高比的视频，适配到一个指定尺寸的显示区域内，是一个通用基础问题。无论是短视频、长视频还是视频通话，都需根据视频宽高比与区域宽高比的差异，决策缩放与裁剪策略。该问题不依赖于具体业务场景，因此可提炼为独立复用模块，供各视频场景统一调用。

下文将分别介绍两层计算的具体规则。

### 短视频布局场景层

根据窗口尺寸决定视频在窗口中的沉浸模式，当前短视频布局场景层支持以下三种沉浸模式：

| 沉浸模式 | 含义 | 结果 |
| --- | --- | --- |
| FULL\_IMMERSION | 全屏幕沉浸 | 视频区域覆盖整个窗口 |
| TOP\_IMMERSION\_ONLY | 仅顶部沉浸 | 视频区域沉浸到顶部，但底部保留Tab区域 |
| SAFE\_AREA | 顶部底部均不沉浸 | 视频区域避开顶部状态栏和底部Tab栏 |

具体沉浸规则如下：

| 窗口宽高比x | 沉浸模式 |
| --- | --- |
| x >= 9:18 | FULL\_IMMERSION（全屏幕沉浸） |
| 9:20 <= x < 9:18 | TOP\_IMMERSION\_ONLY（仅顶部沉浸） |
| x < 9:20 | SAFE\_AREA（顶部底部均不沉浸） |

按照上述沉浸规则进行适配后，视频的沉浸效果图如下（红色部分为视频可用区域）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/4XrbiyInQeSgvVMdBfi1mg/zh-cn_image_0000002724382497.png "点击放大")

### 视频自适应层

布局场景层解决的是“视频区域应该多大”的问题，视频自适应层解决的是“在该区域内视频应该如何显示”的问题。当前视频自适应层支持以下几种填充模式：

| 填充模式 | 含义 | 说明 |
| --- | --- | --- |
| CONTAIN | 等比留黑 | 保持宽高比进行缩小或者放大，使得视频完全显示在显示边界内。该模式下，视频完整显示，不发生裁剪。 |
| COVER | 铺满裁切 | 保持宽高比进行缩小或者放大，使得视频两边都大于或等于显示边界，超出部分自适应裁剪。 |
| OVERSCAN | 微溢裁切 | 等比例缩放视频至视频可视区域宽高比为9:17.8，并居中显示在剩余区域，左右超出部分自适应裁剪。 |

**说明** 

OVERSCAN模式中采用了固定的宽度放大系数，使得视频在水平方向做有限放大，整体裁剪率控制在可接受范围（13%）以内。

当前短视频默认缩放规则如下：

| 视频宽高比r | 可用区域宽w（vp） | 可用区域宽高比x | 填充模式 |
| --- | --- | --- | --- |
| 9:16.1 <= r <= 9:15.9 | 320 <= w < 600 | x >= 9:14.4 | CONTAIN（等比留黑） |
| 9:18 <= x < 9:14.4 | COVER（铺满裁切） |
| x < 9:18 | OVERSCAN（微溢裁切） |
| w >= 600 | - | CONTAIN（等比留黑） |
| r > 9:15.9 或 r < 9:16.1  (非9:16区间的视频) | - | - | CONTAIN（等比留黑） |

**说明** 

非9:16区间的视频，在自适应层不考虑可用区域宽高比，统一使用CONTAIN，优先保证视频内容完整。

视频宽高比处于9:16区间的短视频在不同可用宽高比区域的显示效果图如下（红色部分为视频显示区域，但超出可用区域即灰色区域时，会发生裁剪）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/izhg9R9bT6KDQOd-CW8JSg/zh-cn_image_0000002724502423.png "点击放大")

## 短视频自适应旋转

### 场景描述

短视频自适应旋转是指当用户改变设备的持握方向时，视频内容和页面布局能自动适应方向变化，实现画面无缝连续旋转播放。短视频在各类设备上的旋转效果如下表所示：

| 设备 | 竖屏 | 横屏 |
| --- | --- | --- |
| 直板机 |  | 非全屏播放    全屏播放 |
| 双折叠展开态 |  |  |
| 平板 |  |  |
| 电脑 | 无竖屏效果 |  |

### 规则描述

一般情况下，短视频页应保持与桌面方向一致，进入横屏播放场景时切换到新的旋转策略。[多设备场景库（multidevicelibrary）](https://gitcode.com/HarmonyOS_Samples/MultiDeviceLibrary)为上述两种场景预设了相应的旋转策略。

* 短视频常规播放（SHORT\_VIDEO）：使用follow\_desktop，即[跟随桌面的旋转策略](bpta-multi-device-window-direction.md#section3434202623320)。
* 横屏视频全屏播放（LANDSCAPE\_VIDEO\_FULLSCREEN）：根据屏幕长边尺寸（displayLongEdgeVp）、长短边比例（displayLongShortRatio）区分旋转策略。

  | displayLongEdgeVp | displayLongShortRatio | 旋转策略 | 说明 |
  | --- | --- | --- | --- |
  | 600 <= displayLongEdgeVp < 840 | displayLongShortRatio >= 9:7.2 | AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且受控制中心的旋转开关控制。 |
  | 840 <= displayLongEdgeVp < 1440 | displayLongShortRatio >= 9:4.5 |
  | 其他 | | AUTO\_ROTATION\_UNSPECIFIED | 跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |

**说明** 

displayLongEdgeVp：设备屏幕长边（固定为尺寸更大的边）尺寸，单位vp，数值不随设备旋转变化。

displayLongShortRatio：屏幕长边/屏幕短边。

## 开发步骤

### 场景描述

[多设备场景库（multidevicelibrary）](https://gitcode.com/HarmonyOS_Samples/MultiDeviceLibrary)封装上述两层的实现细节，提供高阶组件AdaptiveShortVideoScene及AdaptiveVideoSurface，帮助开发者高效构建视频播放场景。

### 开发步骤

1. 引入多设备场景库模块，并初始化场景控制器。

   ```typescript
   // Wire SceneController + OrientationController.
   if (this.responsiveContext) {
     const orientation: OrientationController = new OrientationController(data, this.responsiveContext);
     this.scene = new SceneController(orientation);
     AppStorage.setOrCreate('multidevicelibrary.scene', this.scene);
   }
   ```
2. 沉浸模式要求将视频页面的内容扩展至状态栏和导航栏，推荐开发者使用[实现沉浸式效果](bpta-multi-device-window-immersive.md#section180431120426)中的组件级沉浸方案（组件设置页面沉浸），可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。此时组件的布局范围将从安全区域延伸至整个窗口。

   ```typescript
   NavDestination() {
     // ...
   }
   // Expands the layout safe area of a component.
   .ignoreLayoutSafeArea()
   .height(LayoutPolicy.matchParent)
   ```
3. 引入布局场景层组件：使用AdaptiveShortVideoScene包裹短视频内容区域，传入顶部状态栏和底部Tab的占位高度。

   AdaptiveShortVideoScene是短视频场景层组件，负责场景生命周期管理和沉浸规则配置。组件内部会自动推送SHORT\_VIDEO（短视频预设场景）并安装沉浸解析器，开发者只需提供两个占位高度即可。

   ```typescript
   AdaptiveShortVideoScene({
     overlayTop: this.statusBarHeightVp, // Top safe-area inset (status bar).
     overlayBottom: this.bottomTabHeight // Bottom tab-bar height.
   }) {
     VideoSwiper(); // Video area laid out within the region resolved by the scene.
   }
   ```
4. 接入自适应视频容器：AdaptiveVideoSurface。

   将视频播放器作为AdaptiveVideoSurface的子内容进行渲染，并传入视频原始宽高。

   ```typescript
   AdaptiveVideoSurface({
     videoWidth: this.oriSurfaceWidth,
     videoHeight: this.oriSurfaceHeight,
     // ...
   }) {
     this.videoContent(); // Video player.
   }
   ```

   组件根据视频原始宽高比与可用显示区域，自动计算并应用视频最终宽高与偏移，开发者无需自行处理布局，只需将子内容的宽高设为100%。

   ```typescript
   XComponent({
     // ...
   })
     .width('100%')
     .height('100%')
   ```
5. 按需接入横屏视频全屏播放：
   1. 当业务需要支持横屏视频全屏播放时，可在播放器中按需将场景切换到ScenePresets。

      ```typescript
      this.capLayerFullScreenId = this.scene.push(ScenePresets.LANDSCAPE_VIDEO_FULLSCREEN);
      ```
   2. 退出全屏时，释放该场景。

      ```typescript
      this.scene?.release(this.capLayerFullScreenId);
      ```

## 示例代码

[多设备场景库](https://gitcode.com/HarmonyOS_Samples/MultiDeviceLibrary)
