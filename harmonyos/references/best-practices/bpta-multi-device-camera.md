---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-camera
title: 相机硬件差异
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备功能开发 > 相机硬件差异
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-05-30
content_hash: sha256:d9301336c2423a2b35f9af7f218f412918b804c5213ae2b7f2d5df9dfc95db1c
---

## 概述

在移动端应用开发中，相机页面的多设备适配一直是开发者面临的一大难题。由于不同设备的屏幕尺寸、相机镜头、折叠形态以及系统特性等方面存在较大差异，相机界面的开发往往会遇到一系列[兼容性问题](bpta-multi-device-camera.md#section1684283074912)，影响用户体验。

本文介绍如何将手机相机页面（含预览、拍摄和查看照片功能）适配至双折叠、Pura X、三折叠和平板等多种设备形态。在基础相机功能（预览、拍照、查看照片）之上，适配折叠屏和平板设备时，需要重点关注以下核心问题：

* [通过断点实现多套页面布局](bpta-multi-device-camera.md#section181143569262)，并设置横竖屏旋转策略。
* [选择相机设备](bpta-multi-device-camera.md#section13854163154917)。
* [设置多设备上相机预览画面比例](bpta-multi-device-camera.md#section882216138497)。
* [设置拍照旋转角度](bpta-multi-device-camera.md#section0752024124911)。
* [实现悬停态相机页面](bpta-multi-device-camera.md#section50639679)。

## 通过断点实现多套页面布局

“两个宽度相近的窗口，页面布局应相同”。首先，根据这条原则，确认要适配窗口的宽度范围，手机、双折叠、Pura X、三折叠、平板设备共涉及到3种横向断点：sm、md和lg，因此应用首次开发时需要单独设计3种页面布局。

“对于高度相对宽度较小的窗口，呈现横向窗口或类方形窗口时，页面布局需进行差异化设计”。其次根据这条规则，因为Pura X外屏独特的小方形窗口形态，布局会与手机略有差异。UX设计图如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 断点 | 横向断点sm，纵向断点md | 横向断点sm，纵向断点lg | 横向断点md | 横向断点lg |
| UX图 |  |  |  |  |

### 开发步骤

1. 分析三种横向断点对应的UX设计。sm断点的相机按钮布局分布在上下两侧，需要单独实现，Pura X外屏与手机布局的差异通过纵向断点进行区分；md、lg断点的相机按钮布局相同，分布在左右两侧，可以使用一套代码实现。使用Stack组件，展示相机预览画面上的控制按钮，并使用断点控制在三折叠不同使用状态下的显示与隐藏。相机页面中XComponent组件宽高均可设置为100%，预览画面的大小可通过设置XComponent组件对应Surface区域的宽高实现，代码可参考[设置多设备上相机预览画面比例](bpta-multi-device-camera.md#section882216138497)。

   ```screen
   Stack() {
     // Camera View.
     Column() {
       XComponent({
         type: XComponentType.SURFACE,
         controller: this.xComponentController
       }) {}
       // ...
     }
     .width('100%')
     .height(this.isHalfFolded ? this.creaseRegion[0] : '')
     .layoutWeight(this.isHalfFolded ? 0 : 1)
     // ...

     // Shooting button view.
     Stack() {
       // Setting view for sm.
       Column() {
         // ...
       }
       .width(this.heightBp === HeightBreakpoint.HEIGHT_MD ? 30 : 48)
       .height('100%')
       .margin({ right: 16 })
       .padding({ top: this.heightBp === HeightBreakpoint.HEIGHT_MD ? 16 : 108 })
       .visibility(this.widthBp === WidthBreakpoint.WIDTH_SM ? Visibility.Visible : Visibility.None)

       // Choose music for sm.
       Row() {
         // ...
       }
       .width('100%')
       .height(this.heightBp === HeightBreakpoint.HEIGHT_MD ? 28 : 40)
       .position({
         x: 0,
         y: this.heightBp === HeightBreakpoint.HEIGHT_MD ? 16 : 28
       })
       .justifyContent(FlexAlign.Center)
       .visibility(this.widthBp === WidthBreakpoint.WIDTH_SM ? Visibility.Visible : Visibility.None)

       // Shooting button for sm.
       Column() {
         // ...
       }
       .visibility(this.widthBp === WidthBreakpoint.WIDTH_SM ? Visibility.Visible : Visibility.None)
       .height(this.heightBp === HeightBreakpoint.HEIGHT_MD ? 96 : 132)
       .width('100%')
       .margin({ bottom: this.heightBp === HeightBreakpoint.HEIGHT_MD ? 16 : 84 })

       // Setting view for md/lg.
       Column() {
         // ...
       }
       .width(this.widthBp === WidthBreakpoint.WIDTH_MD ? 144 : 152)
       .height('100%')
       .justifyContent(FlexAlign.Start)
       .padding({ left: this.heightBp === HeightBreakpoint.HEIGHT_MD ? 24 : 32 })
       .position({ x: 0, y: 0 })
       .alignItems(HorizontalAlign.Start)
       .visibility(this.widthBp === WidthBreakpoint.WIDTH_MD || this.widthBp === WidthBreakpoint.WIDTH_LG ?
         Visibility.Visible : Visibility.None)

       // Shooting button for md/lg.
       Column() {
         // ...
       }
       .width(92)
       .height('100%')
       .justifyContent(FlexAlign.Center)
       .padding({ right: 16 })
       .visibility(this.widthBp === WidthBreakpoint.WIDTH_MD || this.widthBp === WidthBreakpoint.WIDTH_LG ?
         Visibility.Visible : Visibility.None)
     }
     .height('100%')
     .width('100%')
     .alignContent(Alignment.BottomEnd)
     .visibility(this.isHalfFolded ? Visibility.None : Visibility.Visible)
     // ...
   }
   .height('100%')
   .width('100%')
   .alignContent(this.widthBp === WidthBreakpoint.WIDTH_MD ? (this.isHalfFolded ? Alignment.Top : Alignment.Start) :
     Alignment.Center)
   ```
2. 相机页面在不同设备上横竖屏旋转，请参考[为多设备配置旋转策略](bpta-multi-device-window-direction.md#section12636154743220)。以本应用为例，横向断点为sm时不支持旋转；md、lg时支持旋转。因此，当窗口宽度、高度的最小值大于等于600vp时，窗口支持旋转。

   ```screen
   onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
     this.setOrientation(this.uiContext!.px2vp(windowSize.width), this.uiContext!.px2vp(windowSize.height));
     // ...
   }

   setOrientation(width: number, height: number): void {
     // When the minimum value of window width and height is greater than the md breakpoint threshold, rotation is supported.
     if (Math.min(width, height) >= 600) {
       this.windowData?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_RESTRICTED).catch((error: BusinessError) => {
         hilog.error(0x0000, `MultiDeviceCamera`,
           `Set window orientation failed. Code: ${error.code}, message: ${error.message}`);
       });
     } else {
       this.windowData?.setPreferredOrientation(window.Orientation.PORTRAIT).catch((error: BusinessError) => {
         hilog.error(0x0000, `MultiDeviceCamera`,
           `Set window orientation failed. Code: ${error.code}, message: ${error.message}`);
       });
     }
   }

   // ...
   onWindowStageCreate(windowStage: window.WindowStage): void {
     // ...
     windowStage.loadContent('pages/Index', (err) => {
       // ...
       windowStage.getMainWindow().then((data: window.Window) => {
         // ...
         // Monitor window size changes and update breakpoints.
         data.on('windowSizeChange', this.onWindowSizeChange);
         let rect: window.Rect = data.getWindowProperties().windowRect;
         this.setOrientation(this.uiContext.px2vp(rect.width), this.uiContext.px2vp(rect.height));
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Error occured, error code: ${err.code}, error message: ${err.message}`);
       })
     });
   }
   ```

## 选择相机设备

完整的相机页面，除了实现页面的按钮组件，还需要实现相机预览画面。在创建相机预览对象之前，首先要使用[createCameraInput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createcamerainput)确认使用的相机设备。

### 开发步骤

1. 手机、双折叠、Pura X、三折叠、平板均配有后置相机和前置相机。相机页面显示时，根据isFront变量选择对应CameraPosition的相机，默认使用后置相机。

   ```screen
   onPageShow(): void {
     abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.permissions).then(() => {
       setTimeout(() => {
         // After obtaining permission, load the camera preview stream and ensure it is consistent with the aspect ratio of the surface.
         // ...
         if (this.isFront) {
           this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_FRONT);
         } else {
           this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_BACK);
         }
       }, 200);
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'testTag', `Failed to requestPermissionsFromUser. Code: ${err.code}, message: ${err.message}`);
     })
   }
   ```

   CameraPosition是相对的而不是固定的，例如Pura X外屏的相机。

   * 在折叠态时CameraPosition为CAMERA\_POSITION\_FRONT，效果图如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/AHrYatKGQwW7AOHB-VU6MA/zh-cn_image_0000002355147089.png "点击放大")
   * 在展开态时CameraPosition为CAMERA\_POSITION\_BACK，效果图如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/LWA-gRajQj2ya3M8riWTHA/zh-cn_image_0000002321148366.png "点击放大")
2. 其他需要重置预览流的场景需要开发者单独处理。折叠状态切换（例如双折叠的折叠态切换至半折叠态），会导致显示屏幕变化，需要重新选择相机设备。所以在[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)中判断变化前后的折叠状态，并根据变化前使用的相机位置，选择变化后使用前置相机或后置相机。

   ```screen
   onFoldStatusChange: (foldStatus: display.FoldStatus) => void = (foldStatus: display.FoldStatus) => {
     if (foldStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED) {
       let orientation: display.Orientation = display.getDefaultDisplaySync().orientation;
       // Determine the page layout that has entered half folded status and prohibit portrait orientation.
       if (this.widthBp === WidthBreakpoint.WIDTH_MD && (orientation === display.Orientation.LANDSCAPE ||
         orientation === display.Orientation.LANDSCAPE_INVERTED)) {
         this.isHalfFolded = true;
         this.windowUtil.setMainWindowOrientation(window.Orientation.LANDSCAPE);
         this.cameraUtil.setHalfFoldedRect(this.windowUtil.getWindowSize());
       } else {
         if (this.oldFoldStatus === display.FoldStatus.FOLD_STATUS_FOLDED) {
           if (this.isFront) {
             this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_FRONT);
           } else {
             this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_BACK);
           }
         }
       }
       return;
     }
     // ...
     // Exit the half folded status page.
     if (this.isHalfFolded) {
       this.isHalfFolded = false;
       this.cameraUtil.setXComponentRect(this.windowUtil.getWindowSize());
     } else {
       if (foldStatus === display.FoldStatus.FOLD_STATUS_FOLDED ||
         (this.oldFoldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED &&
           foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED) ||
         (this.oldFoldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED &&
           foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED)) {
         if (this.isFront) {
           this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_FRONT);
         } else {
           this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_BACK);
         }
       }
     }
     // ...
   }

   aboutToAppear(): void {
     try {
       display.on('foldStatusChange', this.onFoldStatusChange);
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'MultiDeviceCamera', `Failed to obtain fold status. Code: ${err.code}, message: ${err.message}`);
     }
     // ...
   }
   ```

   需要注意，PuraX外屏只存在前置相机。如果在内屏使用的是后置相机，切换外屏后，后置相机将不再可用，则返回可用相机列表中默认的相机。

   ```screen
   getCamera(cameras: Array<camera.CameraDevice>, cameraPosition: camera.CameraPosition): number {
     // Choose front or rear camera.
     for (let i: number = 0; i < cameras.length; ++i) {
       if (cameras[i].cameraPosition === cameraPosition) {
         if (cameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK) {
           AppStorage.setOrCreate('isFront', false);
         }
         if (cameraPosition === camera.CameraPosition.CAMERA_POSITION_FRONT) {
           AppStorage.setOrCreate('isFront', true);
         }
         return i;
       }
     }
     hilog.error(0x0000, 'testLog', `Failed to find the camera with the corresponding position.`);
     if (cameras[0].cameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK) {
       AppStorage.setOrCreate('isFront', false);
     }
     if (cameras[0].cameraPosition === camera.CameraPosition.CAMERA_POSITION_FRONT) {
       AppStorage.setOrCreate('isFront', true);
     }
     return 0;
   }
   ```

## 设置多设备上相机预览画面比例

选择相机之后，需要通过[createPreviewOutput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createpreviewoutput12)创建预览输出对象，绑定至XComponent组件展示预览画面，实现流程可参考[拍照实践](../harmonyos-guides/camera-shooting-case.md)。在开发多设备上相机预览画面时，需要通过以下步骤避免压缩、拉伸、异常旋转的问题。

XComponent组件对应Surface区域的宽高比，取决于用户预览时设备的屏幕顺时针旋转角度。如果display.rotation为0°或180°，则Surface与相机预览流宽高比互为倒数；如果display.rotation为90°或270°，则Surface与相机预览流宽高比一致。

以获取预览流宽高比4:3为例（Pura X折叠态为1:1），多设备不同状态的Surface宽高比如下表：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Pura X折叠态 | 手机/双折叠折叠态/三折叠F态/Pura X展开态 | 双折叠展开态/三折叠M态 | 三折叠G态 | 平板 |
| 设备方向 | 以充电口朝右为例  display.rotation=270 | 以充电口朝下为例  display.rotation=0 | 以充电口朝下为例  display.rotation=0 | 以充电口朝下为例  display.rotation=0 | 以充电口朝下为例  display.rotation=0 |
| Surface宽高比 | 1:1 | 3:4 | 3:4 | 3:4 | 3:4 |
| 设备方向 | 页面不支持旋转 | 页面不支持旋转 | 以充电口朝右为例  display.rotation=270 | 以充电口朝右为例  display.rotation=270 | 以充电口朝右为例  display.rotation=270 |
| Surface宽高比 | 4:3 | 4:3 | 4:3 |

多设备不同状态的预览效果图如下表：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Pura X折叠态 | 手机/双折叠折叠态/三折叠F态/Pura X展开态 | 双折叠展开态/三折叠M态 | 三折叠G态 | 平板 |
|  |  |  |  |  |
| 页面不支持旋转 | 页面不支持旋转 |  |  |  |

### 开发步骤

1. 在窗口横竖屏旋转时，实现[setXComponentSurfaceRect()](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)方法重新设置XComponent组件中surface区域的宽和高，确保与多设备相机的预览流、拍照流宽高比一致。

   ```screen
   setXComponentRect(windowSize: window.Size): void {
     try {
       // Initialize the width and height of the surface to match the full screen of the window.
       let rect: SurfaceRect = {
         surfaceWidth: windowSize.width,
         surfaceHeight: windowSize.height
       };
       let widthBp: WidthBreakpoint = this.uiContext!.getWindowWidthBreakpoint();
       let heightBp: HeightBreakpoint = this.uiContext!.getWindowHeightBreakpoint();
       let displayRotation: number = display.getDefaultDisplaySync().rotation * 90;
       if (widthBp === WidthBreakpoint.WIDTH_SM && heightBp === HeightBreakpoint.HEIGHT_MD) {
         this.xComponentController!.setXComponentSurfaceRect(rect);
         return;
       }
       if (AppStorage.get('isHalfFolded')) {
         this.setHalfFoldedRect(windowSize);
         return;
       }
       if (displayRotation === 0 || displayRotation === 180) {
         if (windowSize.height * 3 / 4 > windowSize.width) {
           rect.surfaceHeight = windowSize.width / 3 * 4;
         } else {
           rect.surfaceWidth = windowSize.height / 4 * 3;
         }
         if (widthBp === WidthBreakpoint.WIDTH_MD && heightBp === HeightBreakpoint.HEIGHT_MD) {
           rect.offsetX = 0;
           rect.offsetY = 0;
         }
       }
       if (displayRotation === 90 || displayRotation === 270) {
         if (windowSize.width * 3 / 4 > windowSize.height) {
           rect.surfaceWidth = windowSize.height / 3 * 4;
         } else {
           rect.surfaceHeight = windowSize.width / 4 * 3;
         }
       }
       this.xComponentController!.setXComponentSurfaceRect(rect);
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'MultiDeviceCamera', `Failed to set XComponent rect. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
2. 在窗口横竖屏旋转时，会刷新窗口尺寸，需要调用setXComponentRect()方法刷新预览画面比例，避免预览画面异常压缩或拉伸。

   ```screen
   export default class EntryAbility extends UIAbility {
     // ...
     isFirstTime: boolean = true;
     onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
       // ...
       if (!this.isFirstTime) {
         this.cameraUtil!.setXComponentRect(this.windowUtil!.getWindowSize());
       } else {
         this.isFirstTime = false;
       }
     }
     // ...
     onWindowStageCreate(windowStage: window.WindowStage): void {
       // ...
       windowStage.loadContent('pages/Index', (err) => {
         // ...
         windowStage.getMainWindow().then((data: window.Window) => {
           // ...
           // Monitor window size changes and update breakpoints.
           data.on('windowSizeChange', this.onWindowSizeChange);
           // ...
         }).catch((err: BusinessError) => {
           hilog.error(0x0000, 'testTag', `Error occured, error code: ${err.code}, error message: ${err.message}`);
         })
       });
     }
     // ...
   }
   ```
3. 最后调用[setXComponentSurfaceRotation()](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerotation12)设置XComponent的Surface区域在屏幕旋转时锁定方向，确保相机预览画面旋转时的用户体验。

   ```screen
   XComponent({
     type: XComponentType.SURFACE,
     controller: this.xComponentController
   }) {}
   .onLoad(() => {
     // ...
     // Set surface to lock direction when screen rotates.
     this.xComponentController.setXComponentSurfaceRotation({ lock: true });
   })
   ```

## 设置拍照旋转角度

在横竖屏拍照场景下，需确保图片始终正向显示，避免出现照片方向异常（如旋转90°或倒置）。

### 开发步骤

在[capture()](../harmonyos-references/arkts-apis-camera-photooutput.md#capture-3)方法中，通过重力传感器获取当前拍照的角度，并区分后置相机与前置相机，设置拍照时的旋转角度rotation。

```screen
capture(): void {
  let rotation: number = 0;
  let isFront: boolean | undefined = AppStorage.get('isFront');
  try {
    // Obtain the angle of the gravity sensor during shooting and set the shooting rotation angle.
    sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
      if (Math.abs(data.z) > OVERLOOKING_GRAVITY_OF_Z_AXIS) {
        rotation = this.lastRotation;
      }
      else {
        let degree: number = this.getCalDegree(data.x, data.y, data.z);
        if ((degree >= 0 && degree <= 30) || degree >= 300) {
          rotation = camera.ImageRotation.ROTATION_0;
        } else if (degree > 30 && degree <= 120) {
          if (isFront) {
            // Use ROTATION_270 when degree range is (30, 120] for front camera.
            rotation = camera.ImageRotation.ROTATION_270;
          } else {
            // Use ROTATION_90 when degree range is (30, 120] for back camera.
            rotation = camera.ImageRotation.ROTATION_90;
          }
        } else if (degree > 120 && degree <= 210) {
          // Use ROTATION_180 when degree range is (120, 210].
          rotation = camera.ImageRotation.ROTATION_180;
        } else if (degree > 210 && degree <= 300) {
          if (isFront) {
            // Use ROTATION_90 when degree range is (210, 300] for front camera.
            rotation = camera.ImageRotation.ROTATION_90;
          } else {
            // Use ROTATION_270 when degree range is (210, 300] for back camera.
            rotation = camera.ImageRotation.ROTATION_270;
          }
        };
      }

      let setting: camera.PhotoCaptureSetting = {
        quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
        rotation: rotation,
        mirror: isFront
      }
      this.photoOutput?.capture(setting);
    })
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, 'MultiDeviceCamera', `Capture failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## 实现悬停态相机页面

悬停态对应折叠状态为FOLD\_STATUS\_HALF\_FOLDED。在进入悬停态时，可以设计特殊的用户体验，UX效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/S1II-ms-T6WqgWb_6dM86Q/zh-cn_image_0000002355266965.png "点击放大")

### 开发步骤

使用[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)监听折叠状态的变化。当折叠状态为半折叠且屏幕显示方向为横屏或反向横屏时，记录悬停状态isHalfFolded为true，重新计算Xcomponent的Surface显示区域宽高并调整旋转策略，展示悬停态的相机页面布局；否则，记录悬停态状态为false。

```screen
onFoldStatusChange: (foldStatus: display.FoldStatus) => void = (foldStatus: display.FoldStatus) => {
  if (foldStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED) {
    let orientation: display.Orientation = display.getDefaultDisplaySync().orientation;
    // Determine the page layout that has entered half folded status and prohibit portrait orientation.
    if (this.widthBp === WidthBreakpoint.WIDTH_MD && (orientation === display.Orientation.LANDSCAPE ||
      orientation === display.Orientation.LANDSCAPE_INVERTED)) {
      this.isHalfFolded = true;
      this.windowUtil.setMainWindowOrientation(window.Orientation.LANDSCAPE);
      this.cameraUtil.setHalfFoldedRect(this.windowUtil.getWindowSize());
    } else {
      if (this.oldFoldStatus === display.FoldStatus.FOLD_STATUS_FOLDED) {
        if (this.isFront) {
          this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_FRONT);
        } else {
          this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_BACK);
        }
      }
    }
    return;
  }
  if (this.widthBp !== WidthBreakpoint.WIDTH_SM) {
    this.windowUtil.setMainWindowOrientation(window.Orientation.AUTO_ROTATION_RESTRICTED);
  }
  // Exit the half folded status page.
  if (this.isHalfFolded) {
    this.isHalfFolded = false;
    this.cameraUtil.setXComponentRect(this.windowUtil.getWindowSize());
  } else {
    if (foldStatus === display.FoldStatus.FOLD_STATUS_FOLDED ||
      (this.oldFoldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED &&
        foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED) ||
      (this.oldFoldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED &&
        foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED)) {
      if (this.isFront) {
        this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_FRONT);
      } else {
        this.cameraUtil.cameraShooting(this.surfaceId, this.context!, camera.CameraPosition.CAMERA_POSITION_BACK);
      }
    }
  }
  this.oldFoldStatus = foldStatus;
}
```

## 常见问题

### 按钮大小异常、被截断

**问题现象**

在不同设备上显示按钮大小异常或被截断。

**可能原因**

未设计不同设备对应的多套相机页面布局。

**解决方案**

针对不同横向断点设计多套相机页面布局并实现。详情请参考[通过断点实现多套页面布局](bpta-multi-device-camera.md#section181143569262)。

### 大屏相机页面的可操作组件不支持旋转

**问题现象**

在三折叠G态、双折叠展开态、平板等大屏幕，相机页面的可操作组件不支持旋转，不易操作。

**可能原因**

未设置窗口支持旋转。

**解决方案**

相机页面的横向断点为sm时，不支持旋转；为md、lg时，支持旋转。因此当窗口宽度、高度的最小值大于等于600vp时，窗口支持旋转。详情请参考[通过断点实现多套页面布局](bpta-multi-device-camera.md#section181143569262)。

### 预览画面压缩、拉伸

**问题现象**

预览画面的显示内容被压缩或拉伸。

**可能原因**

相机预览对象绑定XComponent组件时，未正确设置Surface区域宽高的值，导致宽高比与预览流旋转后的宽高比不一致。

**解决方案**

设置XComponent组件对应Surface区域的宽高比，使其与预览流旋转后的宽高比保持一致。详情请参考[设置多设备上相机预览画面比例](bpta-multi-device-camera.md#section882216138497)。

### 拍完照片显示角度异常

**问题现象**

拍摄完成后，照片的实际内容与预期方向不符，可能发生90°、180°或270°的旋转，导致用户需要手动调整才能正常查看。

**可能原因**

拍照时旋转了设备，且未设置正确的拍照角度。

**解决方案**

设置拍照时的旋转角度。详情请参考[设置拍照旋转角度](bpta-multi-device-camera.md#section0752024124911)。

### 折叠屏切换折叠状态时出现黑屏

**问题现象**

在折叠屏开合，切换折叠状态后，相机预览页面出现黑屏。

**可能原因**

切换折叠状态过程，导致折叠前选择的相机不再可用，预览画面黑屏。

**解决方案**

折叠状态切换过程窗口尺寸会变化，通过监听窗口尺寸变化，重新选择相机生成预览流。详情请参考[选择相机设备](bpta-multi-device-camera.md#section13854163154917)。

## 示例代码

* [基于相机开放能力和一多能力实现多设备相机](https://gitcode.com/harmonyos_samples/MultiDeviceCamera)
