---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preview
title: 预览(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 预览(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:49+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:d295309dd504ce45f449e30d5cca6ece871a2203912a2844fca3a9c5d1eb23db
---

## 概述

在移动设备普及的今天，相机已成为人们生活中不可或缺的工具。在移动端开发中，自定义相机具有极高的实用价值，开发者能够根据不同的应用场景和用户需求，定制独特的拍摄功能与交互体验。

如果开发者仅需调用系统相机拍摄照片或录制视频，可直接使用[CameraPicker](../harmonyos-references/js-apis-camerapicker.md)。但构建高度自定义的相机应用或实现对相机数据流进行实时分析等复杂功能时，则需要使用[Camera Kit](../harmonyos-references/camera-api.md)（相机服务）访问和操作相机硬件来实现。

相机预览是相机镜头采集画面的实时展示，为后续的拍照、录像等操作提供基础。本文将对实现基础预览、预览画面的调整（如镜头切换、设置闪光灯、调焦、对焦等）、预览进阶功能（网格线、水平仪等）、获取预览帧数据四个章节进行讲解，提供自定义相机预览部分由基础到进阶的开发实践。

## 实现基础预览

### 场景描述

基础预览是自定义相机核心的功能，用户打开相机应用后，首先看到的就是实时的预览画面，该功能为画面调整、拍摄等操作提供基础。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/9RfryMvARcmSAiENYe_Xhg/zh-cn_image_0000002712244768.gif)

### 实现原理

**关键技术**

* Surface：图像数据缓冲区的抽象概念。
* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)：用于满足开发者较为复杂的自定义渲染需求的渲染组件。为相机提供Surface，相机将预览流数据写入Surface，[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)从Surface读取数据并显示。
* [Camera Kit](../harmonyos-references/camera-api.md)：用于相机设备管理，相机输出流管理以及相机会话管理。相机会话用于配置输入流和输出流，以及设置闪光灯、焦距等参数。

**开发流程**

1. 申请权限。
2. 获取相机设备，创建并启动相机输入流。
3. 使用XComponent创建Surface，并获取surfaceId。
4. 创建预览输出流。
5. 配置相机会话Session并启动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/agQZRKWcSTis5mXyVhYNxw/zh-cn_image_0000002742003721.png)

### 开发步骤

1. 在使用相机相关功能前，需要申请ohos.permission.CAMERA相机权限。申请权限分为以下两步。

   在module.json5中配置该权限，更多相机权限参考[相机开发准备](../harmonyos-guides-V5/camera-preparation-V5.md#申请权限)。

   ```json5
   "requestPermissions": [
     {
       "name": "ohos.permission.CAMERA",
       "reason": "$string:permission_CAMERA",
       "usedScene": {
         "abilities": [
           "EntryAbility"
         ]
       }
     },
     // ...
   ]
   ```

   使用[AtManager.requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法拉起弹窗请求用户授权，若用户拒绝则使用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)方法拉起权限设置弹窗，二次向用户申请授权。具体授权逻辑可根据业务自行调整，可参考[应用权限申请](../best-practices/bpta-permission-application.md)。

   ```typescript
   class PermissionManager {
     private static atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

     static async request(permissions: Permissions[], context: Context): Promise<void> {
       try {
         const data = await PermissionManager.atManager.requestPermissionsFromUser(context, permissions);
         const grantStatus: number[] = data.authResults;
         const deniedPermissions = permissions.filter((_, i) => grantStatus[i] !== 0);
         for (const permission of deniedPermissions) {
           const secondGrantStatus = await PermissionManager.atManager.requestPermissionOnSetting(context, [permission]);
           if (secondGrantStatus[0] !== 0) {
             Logger.error(TAG, 'permission denied');
             throw new Error('permission denied');
           }
         }
       } catch (exception) {
         Logger.error(TAG, `request failed, code is ${exception.code}, message is ${exception.message}`);
         throw new Error('permission failed');
       }
     }
   }
   ```
2. 获取相机设备，创建并启动相机输入流。

   使用[camera.getCameraManager()](../harmonyos-references/arkts-apis-camera-f.md#cameragetcameramanager)方法获取cameraManager实例。

   ```typescript
   this.cameraManager = camera.getCameraManager(context);
   ```

   使用[camera.getSupportedCameras()](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)方法获取相机设备列表。通过[camera.CameraPosition](../harmonyos-references/arkts-apis-camera-e.md#cameraposition)类型获取对应的相机设备。CAMERA\_POSITION\_BACK表示后置镜头，CAMERA\_POSITION\_FRONT表示前置镜头。

   ```typescript
   getCameraDevice(cameraPosition: camera.CameraPosition): camera.CameraDevice | undefined {
     const cameraDevices = this.cameraManager?.getSupportedCameras();
     if (!cameraDevices) {
       Logger.error(TAG, `Failed to get camera device. cameraPosition: ${cameraPosition}}`);
       return undefined;
     }
     const device = cameraDevices?.find(device => device.cameraPosition === cameraPosition) || cameraDevices[0];
     if (!device) {
       Logger.error(TAG, `Failed to get camera device. cameraPosition: ${cameraPosition}}`);
     }
     return device;
   }
   ```

   使用[camera.createCameraInput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createcamerainput)方法创建该相机设备的输入流并打开相机。

   ```typescript
   this.cameraInput = this.cameraManager?.createCameraInput(device);
   await this.cameraInput?.open();
   ```
3. 创建Surface。

   使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件渲染预览画面。指定其type属性为SURFACE。

   使用[getXComponentSurfaceId()](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)方法获取surfaceId。

   使用[setXComponentSurfaceRect()](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)方法设置surface的宽高属性为预览画面显示区域的宽高。

   使用[setXComponentSurfaceRotation()](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerotation12)方法锁定surface在屏幕旋转时的方向。

   **说明** 

   未设置surface宽高时其取值为XComponent组件宽高。建议显式设置surface宽高而不是依赖XComponent宽高，防止surface宽高不对导致画面畸变。

   ```typescript
   XComponent({
     type: XComponentType.SURFACE,
     controller: this.previewVM.xComponentController
   })
     .onLoad(async () => {
       // ...
       this.previewVM.surfaceId = this.previewVM.xComponentController.getXComponentSurfaceId();
       this.previewVM.setPreviewSize();
       this.previewVM.xComponentController.setXComponentSurfaceRotation({ lock: true });
       // ...
     })
   ```

   ```typescript
   setPreviewSize(): void {
     const displaySize: Size = WindowUtil.getMaxDisplaySize(this.getPreviewRatio());
     this.previewSize = displaySize;
     this.xComponentController.setXComponentSurfaceRect({
       surfaceWidth: displaySize.width,
       surfaceHeight: displaySize.height
     });
   }
   ```
4. 创建预览输出流。

   1. 选择对应的[camera.SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)。拍照模式下的预览选择SceneMode.NORMAL\_PHOTO，录像模式下的预览选择SceneMode.NORMAL\_VIDEO。
   2. 根据[camera.SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)获取相机设备的输出能力。
   3. 在输出能力[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)类的previewProfiles属性中查找所需规格的预览输出能力previewProfile。在profile的选择上需要注意以下两点：

      * 分辨率选择。所选择分辨率要保证宽高比与surface的宽高比一致，避免画面产生畸变。同时根据业务需求和设备性能选择合适的分辨率大小，过小可能导致画面模糊，过大可能导致资源浪费，功耗和内存过高等风险。
      * format格式选择。开发者在选择format格式时需要与后续处理相机buffer数据的像素格式保持一致，避免画面产生异常。
   4. 使用[CameraManager.createPreviewOutput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createpreviewoutput)方法创建预览输出流。

   ```typescript
   async createOutput(config: CreateOutputConfig): Promise<camera.PreviewOutput | undefined> {
     const cameraOutputCap = config.cameraManager?.getSupportedOutputCapability(config.device, config.sceneMode);
     const displayRatio = config.profile.size.width / config.profile.size.height;
     const profileWidth = config.profile.size.width;
     const previewProfile = cameraOutputCap?.previewProfiles
       .sort((a, b) => Math.abs(a.size.width - profileWidth) - Math.abs(b.size.width - profileWidth))
       .find(pf => {
         const pfDisplayRatio = pf.size.width / pf.size.height;
         return pf.format === config.profile.format &&
           Math.abs(pfDisplayRatio - displayRatio) <= CameraConstant.PROFILE_DIFFERENCE;
       });
     if (!previewProfile) {
       Logger.error(TAG_LOG, 'Failed to get preview profile');
       return undefined;
     }
     try {
       this.output = config.cameraManager?.createPreviewOutput(previewProfile, config.surfaceId);
       if (this.output) {
         this.addOutputListener(this.output);
       }
     } catch (exception) {
       Logger.error(TAG_LOG, `createPreviewOutput failed, code is ${exception.code}, message is ${exception.message}`);
     }
     return this.output;
   }
   ```

   **说明** 

   以直板机后置相机为例，在设备自然方向下，相机的后置镜头安装角度为90度（不同设备的相机安装角度可通过[CameraDevice.cameraOrientation](../harmonyos-references/arkts-apis-camera-i.md#cameradevice)获取），屏幕旋转角度为0度。所以输出能力profile中的宽高与预览显示区域或surface的宽高比例是倒置的。例如在显示区域宽高为1080\*1920，所需查找profile的宽高为1920\*1080。横屏显示方向下，profile宽高与预览显示区域或surface的宽高比例保持一致。

   ```typescript
   public getProfile: (cameraOrientation: number) => camera.Profile = cameraOrientation => {
     const displaySize: Size = WindowUtil.getMaxDisplaySize(this.getPreviewRatio());
     let displayDefault: display.Display | null = null;
     try {
       displayDefault = display.getDefaultDisplaySync();
     } catch (exception) {
       Logger.error(TAG, `getDefaultDisplaySync failed, code is ${exception.code}, message is ${exception.message}`);
     }
     const displayRotation = (displayDefault?.rotation ?? 0) * 90;
     const isRevert = (cameraOrientation + displayRotation) % 180 !== 0;
     return {
       format: camera.CameraFormat.CAMERA_FORMAT_YUV_420_SP,
       size: {
         height: isRevert ? displaySize.width : displaySize.height,
         width: isRevert ? displaySize.height : displaySize.width
       }
     };
   };
   ```
5. 配置并启动相机会话。

   使用[CameraManager.createSession()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)方法创建相机会话Session。

   使用[Session.beginConfig()](../harmonyos-references/arkts-apis-camera-session.md#beginconfig11)方法开始相机会话配置。

   使用[Session.addInput()](../harmonyos-references/arkts-apis-camera-session.md#addinput11)方法和[Session.addOutput()](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)方法分别将相机的输入流和预览输出流配置到相机会话中。

   使用[Session.commitConfig()](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11-1)方法提交相机会话配置信息。

   使用[Session.start()](../harmonyos-references/arkts-apis-camera-session.md#start11-1)方法启动相机会话。

   ```typescript
   const session = this.cameraManager?.createSession(sceneMode);
   session?.beginConfig();
   session?.addInput(this.cameraInput);
   // ...
   for (const outputManager of this.outputManagers) {
     if (outputManager.isActive) {
       const output = await outputManager.createOutput(config);
       session?.addOutput(output);
     }
   }
   await session?.commitConfig();
   if (sceneMode === camera.SceneMode.NORMAL_VIDEO && session) {
     this.setVideoStabilizationMode(isStabilizationEnabled, session as camera.VideoSession);
   }
   await session?.start();
   ```

   ```typescript
   export interface OutputManager {
     output?: camera.CameraOutput;
     isActive: boolean;
     createOutput: (config: CreateOutputConfig) => Promise<camera.CameraOutput | undefined>;
     release: () => Promise<void>;
   }
   ```
6. 释放资源，注意释放的顺序。

   使用[CameraOutput.release()](../harmonyos-references/arkts-apis-camera-cameraoutput.md#release-1)方法释放预览输出流。

   ```typescript
   async release(): Promise<void> {
     try {
       await this.output?.release();
     } catch (exception) {
       Logger.error(TAG_LOG, `release failed, code is ${exception.code}, message is ${exception.message}`);
     }
     this.output = undefined;
   }
   ```

   使用[CameraInput.close()](../harmonyos-references/arkts-apis-camera-camerainput.md#close-1)方法关闭相机，使用[Session.release()](../harmonyos-references/arkts-apis-camera-session.md#release11-1)方法释放相机会话资源。

   ```typescript
   async release(): Promise<void> {
     try {
       await this.session?.stop();
       for (const outputManager of this.outputManagers) {
         if (outputManager.isActive) {
           await outputManager.release();
         }
       }
       await this.cameraInput?.close();
       await this.session?.release();
     } catch (exception) {
       Logger.error(TAG, `release failed, code is ${exception.code}, message is ${exception.message}`);
     }
   }
   ```
7. 监听预览流状态。

   注册[frameStart](../harmonyos-references/arkts-apis-camera-previewoutput.md#onframestart)预览帧启动和[frameEnd](../harmonyos-references/arkts-apis-camera-previewoutput.md#onframeend)预览帧结束的事件，在事件回调中做对应的业务处理。

   ```typescript
   addFrameStartEventListener(output: camera.PreviewOutput): void {
     output.on('frameStart', (err: BusinessError) => {
       if (err !== undefined && err.code !== 0) {
         Logger.error(TAG_LOG, `FrameStart callback Error, errorMessage: ${err.message}`);
         return;
       }
       Logger.info(TAG_LOG, 'Preview frame started');
       this.onPreviewStart();
     });
   }

   addFrameEndEventListener(output: camera.PreviewOutput): void {
     output.on('frameEnd', (err: BusinessError) => {
       if (err !== undefined && err.code !== 0) {
         Logger.error(TAG_LOG, `frameEnd callback Error, errorMessage: ${err.message}`);
         return;
       }
       Logger.info(TAG_LOG, 'Preview frame end');
     });
   }
   ```

## 预览画面调整

在基础预览功能之上，自定义相机通常需要具备调整预览画面的能力，包括前后置镜头的切换、调焦、对焦、切换闪光灯模式等核心功能。

### 切换前后置镜头

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/nJnICFG7S8GNRf7Uat3H7Q/zh-cn_image_0000002712404734.gif)

预览页面中用isFront属性标识前置还是后置镜头，根据isFront获取[camera.CameraPosition](../harmonyos-references/arkts-apis-camera-e.md#cameraposition)的值。关于折叠屏CameraPosition的选择可参考[相机硬件差异](../best-practices/bpta-multi-device-camera.md#section13854163154917)。

```typescript
public isFront: boolean = false;
// ...
getCameraPosition(): camera.CameraPosition {
  return this.isFront
    ? camera.CameraPosition.CAMERA_POSITION_FRONT
    : camera.CameraPosition.CAMERA_POSITION_BACK;
}
```

给切换镜头按钮绑定点击事件，在回调函数中先切换isFront属性的状态，获取新的CameraPosition，释放掉输入输出流等相机资源，再重新创建新镜头的输入输出流，并启动相机。参考[实现基础预览](camera-preview.md#实现基础预览)开发步骤中的2、4、5步骤。

**说明** 

在本示例中，相机和基础预览的启动流程封装在自定义的CameraManager类的start()方法中，相机资源及输入输出流的释放封装在release()方法中。

```typescript
@Builder
toggleCameraPositionButton() {
  Image($r('app.media.toggle_position'))
    .width(48)
    .height(48)
    .onClick(async () => {
      // ...
      this.previewVM.isFront = !this.previewVM.isFront;
      await this.previewVM.cameraManagerRelease();
      await this.previewVM.cameraManagerStart();
      // ...
    })
}
```

实现前后置切换转场动效可参考[相机基础动效](camera-animation.md)。

### 设置相机焦距

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/tyAvXSwjRx-_bLQrS4Zz-A/zh-cn_image_0000002742123683.gif)

使用[getZoomRatioRange()](../harmonyos-references/arkts-apis-camera-zoomquery.md#getzoomratiorange11)方法获取当前相机设备支持设置的焦距范围，根据业务需求在页面上生成相应焦距的按钮。

```typescript
getZoomRange(): number[] {
  try {
    return this.session!.getZoomRatioRange();
  } catch (exception) {
    Logger.error(TAG, `getZoomRange failed, code is ${exception.code}, message is ${exception.message}`);
    return [];
  }
}
```

在点击焦距按钮事件的回调函数中使用[setSmoothZoom()](../harmonyos-references/arkts-apis-camera-zoom.md#setsmoothzoom11)方法平滑变焦到按钮对应的焦距。

```typescript
setSmoothZoom(zoom: number): void {
  try {
    this.session?.setSmoothZoom(zoom);
  } catch (e) {
    Logger.error(TAG, 'setSmoothZoom error ' + JSON.stringify(e));
  }
}
```

### 设置闪光灯

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Xdhc4hD1StuCS-zfj2vteQ/zh-cn_image_0000002712244770.gif)

使用[setFlashMode()](../harmonyos-references/arkts-apis-camera-flash.md#setflashmode11)方法设置闪光灯模式，在设置前需使用[isFlashModeSupported()](../harmonyos-references/arkts-apis-camera-flashquery.md#isflashmodesupported11)方法检测设备是否支持设置所选闪光灯模式。

```typescript
setFlashMode(flashMode: camera.FlashMode): void {
  try {
    const isSupported = this.session?.isFlashModeSupported(flashMode);
    if (!isSupported) {
      Logger.error(TAG, `setFlashMode error: flash mode ${flashMode} is not supported`);
      return;
    }
    this.session?.setFlashMode(flashMode);
  } catch (e) {
    Logger.error(TAG, 'setFlashMode error ' + JSON.stringify(e));
  }
}
```

### 实现点击对焦

点击预览区域，以点击处为焦点进行对焦，并显示对焦框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/3-3J-zIHSXGDwui8Hai5oA/zh-cn_image_0000002742003723.gif)

设置焦点[camera.Point](../harmonyos-references/arkts-apis-camera-i.md#point)的坐标是以充电口在右侧时横向设备方向为基准，该坐标系左上角为{ 0，0 }，右下角为{ 1，1 }。

设备自然方向上，触碰获取的坐标是以充电口在下方时的竖向方向为基准，因此需要进行坐标系的转换。

设触碰点为{ x, y }，预览区域宽高为{ w, h }。

* 屏幕旋转角度为0：由下图可知，在焦点所处相机画面坐标系中，触碰点距原点在x轴方向的距离为y，在y轴方向的距离为w - x。由于该坐标系为0-1坐标系，所以实际焦点坐标为{ y / h, (w - x) / w }，即{ y / h, 1 - x / w }。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/G_o-i5rtRkyfVZHfgRdjaw/zh-cn_image_0000002712404736.png)

同理，其他屏幕旋转方向上焦点坐标同可以计算出：

* 屏幕旋转角度为90：焦点坐标为{ 1 - x / w, 1 - y / h }。
* 屏幕旋转角度为180：焦点坐标为{ 1 - y / h, x / w }。
* 屏幕旋转角度为270：焦点坐标为{ x / w, y / h }。

```typescript
export function calCameraPoint(eventX: number, eventY: number, width: number, height: number): camera.Point {
  let displayDefault: display.Display | null = null;
  try {
    displayDefault = display.getDefaultDisplaySync();
  } catch (exception) {
    Logger.error('calCameraPoint', `calCameraPoint failed, code is ${exception.code}, message is ${exception.message}`);
  }
  const displayRotation = (displayDefault?.rotation ?? 0) * 90;
  if (displayRotation === 0) {
    return { x: eventY / height, y: 1 - eventX / width };
  }
  if (displayRotation === 90) {
    return { x: 1 - eventX / width, y: 1 - eventY / height };
  }
  if (displayRotation === 180) {
    return { x: 1 - eventY / height, y: eventX / width };
  }
  return { x: eventX / width, y: eventY / height };
}
```

在相机会话启动后，使用[setFocusMode()](../harmonyos-references/arkts-apis-camera-focus.md#setfocusmode11)方法设置对焦模式为FOCUS\_MODE\_CONTINUOUS\_AUTO，当点击预览画面对焦时，设置对焦模式为FOCUS\_MODE\_AUTO，以支持对焦点设置。在设置前需检测相机是否支持该对焦模式。手动对焦结束后将对焦模式切换为FOCUS\_MODE\_CONTINUOUS\_AUTO，以获得更好的对焦体验。

```typescript
setFocusMode(focusMode: camera.FocusMode): void {
  try {
    const isSupported = this.session?.isFocusModeSupported(focusMode);
    if (!isSupported) {
      Logger.error(TAG, `setFocusMode error: focus mode ${focusMode} is not supported`);
      return;
    }
    this.session?.setFocusMode(focusMode);
  } catch (e) {
    Logger.error(TAG, 'setFocusMode error ' + JSON.stringify(e));
  }
}
```

使用[setFoucusPoint()](../harmonyos-references/arkts-apis-camera-focus.md#setfocuspoint11)方法实现点击对焦。

```typescript
setFocusPoint(point: camera.Point): void {
  try {
    this.session?.setFocusPoint(point);
  } catch (e) {
    Logger.error(TAG, 'setFocusPoint error ' + JSON.stringify(e));
  }
}
```

根据预览区域宽高、对焦框宽高以及触碰点的坐标计算对焦框相对预览区域的位置，注意不要超出预览区域的边界。

```typescript
export function getClampedChildPosition(childSize: Size, parentSize: Size, point: Point): Edges {
  let left = point.x - childSize.width / 2;
  let top = point.y - childSize.height / 2;
  if (left < 0) {
    left = 0;
  }
  if (left + childSize.width > parentSize.width) {
    left = parentSize.width - childSize.width;
  }
  if (top < 0) {
    top = 0;
  }
  if (top + childSize.height > parentSize.height) {
    top = parentSize.height - childSize.height;
  }
  return { left, top };
}
```

### 设置曝光区域中心点

点击预览区域，设置点击处为曝光中心点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/vuUUlyfRTSOAq0Dd1BS8tw/zh-cn_image_0000002742123685.gif)

在相机会话启动后，使用[setExposureMode()](../harmonyos-references/arkts-apis-camera-autoexposure.md#setexposuremode11)方法设置曝光模式为EXPOSURE\_MODE\_CONTINUOUS\_AUTO，当点击预览画面时，设置曝光模式为EXPOSURE\_MODE\_AUTO，以支持曝光区域中心点设置。在设置前需检测相机是否支持该曝光模式。手动设置结束后将曝光模式切换为EXPOSURE\_MODE\_CONTINUOUS\_AUTO，以获得更好的曝光体验。

```typescript
setExposureMode(exposureMode: camera.ExposureMode): void {
  try {
    const isSupported = this.session?.isExposureModeSupported(exposureMode);
    if (!isSupported) {
      Logger.error(TAG, `setExposureMode error: focus mode ${exposureMode} is not supported`);
      return;
    }
    this.session?.setExposureMode(exposureMode);
  } catch (e) {
    Logger.error(TAG, 'setExposureMode error ' + JSON.stringify(e));
  }
}
```

点击屏幕预览区域，使用[setMeteringPoint()](../harmonyos-references/arkts-apis-camera-autoexposure.md#setmeteringpoint11)方法设置曝光区域中心点。屏幕布局坐标和相机坐标之间的转换逻辑详见[实现点击对焦](camera-preview.md#实现点击对焦)小节。

```typescript
setMeteringPoint(point: camera.Point): void {
  try {
    this.session?.setMeteringPoint(point);
  } catch (e) {
    Logger.error(TAG, 'setMeteringPoint error ' + JSON.stringify(e));
  }
}
```

### 设置预览帧率

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/hqDy3c8bSwSHOn_3fzE91Q/zh-cn_image_0000002712244772.gif)

使用[PreviewOutput.getSupportedFrameRates()](../harmonyos-references/arkts-apis-camera-previewoutput.md#getsupportedframerates12)方法获取预览流支持的帧率范围。

```typescript
getSupportedFrameRates(): camera.FrameRateRange[] | undefined {
  return this.output?.getSupportedFrameRates();
}
```

在帧率切换按钮点击事件的回调函数中，使用[PreviewOutput.setFrameRate()](../harmonyos-references/arkts-apis-camera-previewoutput.md#setframerate12)方法对预览帧率进行动态调整。

```typescript
setFrameRate(minFps: number, maxFps: number): void {
  try {
    this.output?.setFrameRate(minFps, maxFps);
  } catch (e) {
    Logger.error(TAG_LOG, 'setFrameRate error ' + JSON.stringify(e));
  }
}
```

### 设置白平衡

白平衡是相机为了消除不同光源下的偏色，通过调整颜色的增益，从而使整体色彩看起来更加自然真实。通过白平衡，可以调整拍照、录像的图像颜色。关于白平衡的实现，具体可以参考[白平衡设置(ArkTS)](camera-whitebalance.md)。

### 设置相机控制器

相机控制器仅支持在前置镜头的录像模式场景下开启，提供美颜、背景虚化等功能，具体效果因机型差异而异。在直播、视频通话等场景下，开发者可以使用[enableControlCenter()](../harmonyos-references/arkts-apis-camera-controlcenter.md#enablecontrolcenter20)接口启动相机控制器，快速实现美颜、背景虚化等功能，具体实现可以参考[相机控制器(ArkTS)](camera-control-center.md)。

## 实现预览进阶功能

### 实现手势缩放

在预览画面进行手势捏合操作，预览画面焦距会随捏合手势进行对应缩放调整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/mEMTn_8sSCai1iS5dJXEkQ/zh-cn_image_0000002742003725.gif)

使用[PinchGesture()](../harmonyos-references/ts-basic-gestures-pinchgesture.md)接口给预览区域元素绑定捏合事件。

在捏合手势识别成功onActionStart()事件的回调函数中，记录此次捏合前的焦距。在手势移动过程中onActionUpdate()事件的回调函数中，根据捏合前的焦距以及缩放比例计算出当前的焦距，注意限制在当前相机设备的焦距范围内。

```typescript
XComponent({
  type: XComponentType.SURFACE,
  controller: this.previewVM.xComponentController
})
// ...
  .gesture(
    PinchGesture({ fingers: 2 })
      .onActionStart(() => {
        this.originZoomBeforePinch = this.previewVM.currentZoom;
        this.isZoomPinching = true;
        this.previewVM.sleepTimer?.refresh();
      })
      .onActionUpdate((event: GestureEvent) => {
        if (this.previewVM.isVideoMode() && this.previewVM.isStabilizationEnabled) {
          return;
        }
        const targetZoom = this.originZoomBeforePinch * event.scale;
        this.previewVM.currentZoom = limitNumberInRange(targetZoom, this.previewVM.zoomRange);
        this.previewVM.setCameraZoomRatio();
      })
      .onActionEnd(() => {
        this.isZoomPinching = false;
      })
  )
```

### 网格线

将相机预览画面划分为9个等比例区域（3×3宫格），为用户提供精准的构图参考框架。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/t8EotBFASOyGoSAlY8UwpA/zh-cn_image_0000002712404738.png)

获取预览区域的宽高，通过行数和列数计算出每条网格线的起始坐标，在[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)上进行绘制。注意设置[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性为HitTestMode.Transparent，不影响下方预览区域的正常交互。

```typescript
draw(): void {
  const ctx = this.context;
  ctx.strokeStyle = this.strokeStyle;
  ctx.lineWidth = this.lineWidth;
  const height = this.context.height;
  const width = this.context.width;
  for (let i = 1; i < this.cols; i++) {
    const x = (width / this.cols) * i;
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.stroke();
  }
  for (let i = 1; i < this.rows; i++) {
    const y = (height / this.rows) * i;
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(width, y);
    ctx.stroke();
  }
}

build() {
  Canvas(this.context)
    .width('100%')
    .height('100%')
    .hitTestBehavior(HitTestMode.Transparent)
    .onReady(() => this.draw())
}
```

用[Stack](../harmonyos-references/ts-container-stack.md)组件将网格线组件堆叠在预览区域上层。

```typescript
Stack({
  alignContent: Alignment.Center
}) {
  XComponent({
    type: XComponentType.SURFACE,
    controller: this.previewVM.xComponentController
  })
  // ...
  if (this.previewVM.isGridLineVisible) {
    GridLine();
  }
  // ...

  if (this.isShowBlack) {
    Column()
      .id('black')
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Black)
      .opacity(this.flashBlackOpacity)
  }
}
```

### 水平仪

设备旋转过程中，水平仪指示线始终垂直于重力方向，当设备水平时（x轴或y轴垂直于重力方向），水平仪指示线由虚线变为实线。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/CoVFbH2WTu2LJQJP1uv_pQ/zh-cn_image_0000002742123687.png)

水平仪的实现需要用到重力加速度传感器。通过[sensor](../harmonyos-references/js-apis-sensor.md)模块获取重力加速度在x, y, z轴方向上的分量。以充电口在下的竖屏方向为基准，x, y, z轴的方向如下。

* x轴：水平向右。
* y轴：垂直向上。
* z轴：垂直于屏幕向外。

由下图可知，水平仪指示线与x轴的夹角用θ表示，若要指示线始终垂直重力方向，则tanθ = g(x) / -g(y)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/yY1A-xXBQ52xOMPWGt6cDA/zh-cn_image_0000002712244774.png)

在module.json5中配置加速度传感器权限。

```json5
"requestPermissions": [
  // ...
  {
    "name": "ohos.permission.ACCELEROMETER",
    "reason": "$string:permission_SENSOR",
    "usedScene": {
      "abilities": [
        "EntryAbility"
      ]
    }
  }
]
```

使用[sensor.on()](../harmonyos-references/js-apis-sensor.md#sensoronsensoridaccelerometer9)方法订阅重力加速度传感器数据。

```typescript
addGravityEventListener(): void {
  try {
    sensor.on(sensor.SensorId.GRAVITY, (data) => {
      this.previewVM.acc = data;
    }, { interval: 100 * 1000 * 1000 });
  } catch (exception) {
    Logger.error(TAG, `addGravityEventListener failed, code is ${exception.code}, message is ${exception.message}`);
  }
}
```

计算指示线的旋转角度，以及设备是否水平。设置[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性为HitTestMode.Transparent，不影响下层预览区域的正常交互。

```typescript
@Component
export struct LevelIndicator {
  @Prop acc: sensor.AccelerometerResponse;

  getRotate(): number {
    let displayDefault: display.Display | null = null;
    try {
      displayDefault = display.getDefaultDisplaySync();
    } catch (exception) {
      Logger.error(TAG, `getDefaultDisplaySync failed, code is ${exception.code}, message is ${exception.message}`);
    }
    const rotation = (displayDefault?.rotation ?? 0) * 90;
    if (rotation === 90 || rotation === 270) {
      return -Math.atan2(-this.acc.y, this.acc.x) * (180 / Math.PI);
    }
    return -Math.atan2(-this.acc.x, this.acc.y) * (180 / Math.PI);
  }

  isAlign(): boolean {
    return Math.abs(this.getRotate()) - 0 <= ANGLE_DIFFERENCE ||
      Math.abs(Math.abs(this.getRotate()) - 90) <= ANGLE_DIFFERENCE;
  }

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Line({
        width: 200,
        height: 1
      })
      // ...
        .strokeDashArray([3, this.isAlign() ? 0 : 3])
        .opacity(this.isAlign() ? 1 : 0.5)
        .rotate({ angle: this.getRotate(), centerX: '50%', centerY: '50%' })
        .animation({
          curve: curves.springMotion(0.6, 0.8),
          iterations: 1,
          playMode: PlayMode.Normal
        })
      Circle()
      // ...
        .opacity(this.isAlign() ? 1 : 0.5)
    }
    // ...
    .hitTestBehavior(HitTestMode.Transparent)
  }
}
```

### 超时暂停预览

若相机在超过特定时间内未进行任何操作，则会暂停预览并显示遮罩。点击遮罩可重新启动预览，避免相机资源长时间浪费，从而降低功耗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/0t2wZs1lRY2nNa_SYwc1EQ/zh-cn_image_0000002742003727.gif)

实现带刷新方法的定时器类，初始化时传入计时结束的回调函数。需要重置计时时间，调用refresh()方法实现。

```typescript
class RefreshableTimer {
  private timerId?: number;
  private readonly timeout: number;
  private callback: () => void;
  private isActive: boolean = false;

  constructor(callback: () => void, timeout: number) {
    this.callback = callback;
    this.timeout = timeout;
  }

  start(): void {
    clearTimeout(this.timerId);
    this.timerId = setTimeout(() => {
      this.callback();
      this.isActive = false;
    }, this.timeout);
    this.isActive = true;
  }

  clear(): void {
    clearTimeout(this.timerId);
    this.timerId = undefined;
    this.isActive = false;
  }

  refresh(): void {
    this.clear();
    this.start();
  }

  isRunning(): boolean {
    return this.isActive;
  }
}
```

预览页面初始化时，启动定时器。使用[UIObserver](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getuiobserver11)监听[willClick()](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onwillclick12)事件，30s内如果有操作，则重置定时器，直到30s内无任何操作，设置控制遮罩显隐的状态变量isSleeping为true，并释放相机资源。

```typescript
initSleepTimer(): void {
  this.previewVM.sleepTimer = new RefreshableTimer(() => {
    this.previewVM.openPreviewBlur();
    this.previewVM.isSleeping = true;
    this.previewVM.cameraManagerRelease();
  }, 30 * 1000);
  this.previewVM.sleepTimer.start();
  const observer = this.getUIContext().getUIObserver();
  observer.on('willClick', () => {
    this.previewVM.sleepTimer?.refresh();
  });
}
```

点击遮罩，设置状态变量isSleeping为false并重新启动相机预览。

```typescript
@Builder
wakeupMask() {
  Column() {
    Text($r('app.string.wakeup_text'))
      .fontColor(Color.White)
      .opacity(0.6)
  }
  // ...
  .onClick(async () => {
    this.previewVM.isSleeping = false;
    this.previewVM.sleepTimer?.refresh();
    await this.previewVM.cameraManagerStart();
    this.previewVM.syncButtonSettings();
  })
}
```

### 前后台切换

当相机应用在退后台之后由于安全策略会被强制断流。当从后台切换至前台时，需要重启相机设备的预览流、拍照流以及相机会话。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Rjxdq6nmR2SKSkGKjXEfVw/zh-cn_image_0000002712404740.gif)

使用[ApplicationContext.on('applicationStateChange')](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonapplicationstatechange10)方法注册对当前应用前后台状态变化的监听。在切换至后台触发的[onApplicationBackground()](../harmonyos-references/js-apis-app-ability-applicationstatechangecallback.md#applicationstatechangecallbackonapplicationbackground)回调函数中释放相机相关资源。在切换至前台触发的[onApplicationForeground()](../harmonyos-references/js-apis-app-ability-applicationstatechangecallback.md#applicationstatechangecallbackonapplicationforeground)回调函数中重新启动相机及预览。

```typescript
registerApplicationStateChange(): void {
  this.applicationContext.on('applicationStateChange', {
    onApplicationForeground: async () => {
      await this.previewVM.cameraManagerStart();
      // ...
    },
    onApplicationBackground: () => {
      // ...
      this.previewVM.cameraManagerRelease();
    }
  });
}
```

### 预览人脸检测

相机拍摄人像时，在预览画面上添加人脸检测框可以辅助对焦和构图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/1TRYvMj0TlWdKa6yXFk_HQ/zh-cn_image_0000002742123689.png)

相机的[元数据](camera-metadata.md)输出流携带了人脸检测信息，应用可配置元数据输出流并读取检测信息绘制检测框。相较于[基于Core Vision Kit的人脸检测](core-vision-face-detector.md)能力，元数据输出流在相机预览时返回数据更快，性能更好，具体对比如下：

| 能力 | 人脸检测能力 | 支持的检测数据来源 | 相机预览场景性能 |
| --- | --- | --- | --- |
| 基于相机元数据输出流的人脸检测 | 人脸位置坐标 | 相机预览画面 | 检测结果返回快 |
| 基于Core Vision Kit的人脸检测 | 人脸位置坐标、人脸五官位置、人脸朝向、人脸置信度 | 图像pixelmap | 检测结果返回慢 |

使用元数据输出流实现人脸检测开发步骤如下：

1. 创建相机元数据输出流。

   ```typescript
   async createOutput(config: CreateOutputConfig): Promise<camera.CameraOutput | undefined> {
     const cameraOutputCap = config.cameraManager?.getSupportedOutputCapability(config.device, config.sceneMode);
     if (!cameraOutputCap) {
       Logger.error(TAG_LOG, 'Failed to get supported output capability.');
       return undefined;
     }
     let metadataObjectTypes: camera.MetadataObjectType[] = cameraOutputCap!.supportedMetadataObjectTypes;
     try {
       this.output = config.cameraManager?.createMetadataOutput(metadataObjectTypes);
       if (this.output) {
         this.addOutputListener(this.output);
       }
     } catch (error) {
       Logger.error(TAG_LOG, `Failed to createMetadataOutput, error code: ${error.code}`);
     }
     return this.output;
   }
   ```
2. 将元数据输出流添加到会话中。

   ```typescript
   for (const outputManager of this.outputManagers) {
     if (outputManager.isActive) {
       const output = await outputManager.createOutput(config);
       session?.addOutput(output);
     }
   }
   await session?.commitConfig();
   await session?.start();
   ```
3. 注册[on('metadataObjectsAvailable')](../harmonyos-references/arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)回调，监听元数据流中的人脸信息。

   ```typescript
   addMetadataObjectsAvailableListener(metadataOutput: camera.MetadataOutput): void {
     metadataOutput.on('metadataObjectsAvailable',
       (err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>) => {
       if (err && err.code !== 0) {
         Logger.error(TAG_LOG, `Metadata output on metadataObjectsAvailable error code: ${err.code}`);
         return;
       }
       let boxRectArr: camera.Rect[] = [];
       metadataObjectArr.forEach((obj: camera.MetadataObject)=>{
         boxRectArr.push(obj.boundingBox);
       });
       this.onMetadataObjectsAvailable(boxRectArr);
     });
   }
   ```
4. 通过回调接口返回的归一化数据，计算检测框实际坐标。

   **说明** 

   * 接口返回的坐标数据以预览画面左上角为原点，具体可参考[实现点击对焦](camera-preview.md#实现点击对焦)章节中的页面布局坐标系。
   * 元数据输出流最多返回10个人脸检测框信息。

   ```typescript
   onMetadataObjectsAvailable(faceBoxArr: camera.Rect[]) {
     faceBoxArr.forEach((value) => {
       value.topLeftX *= this.previewVM.getPreviewWidth();
       value.topLeftY *= this.previewVM.getPreviewHeight();
       value.width *= this.previewVM.getPreviewWidth();
       value.height *= this.previewVM.getPreviewHeight();
     })
     this.previewVM.faceBoundingBoxArr = faceBoxArr;
   }
   ```
5. 计算检测框各边的起点和终点位置坐标。

   ```typescript
   export function calFaceBoxLinePoint(faceBoxRect: camera.Rect): LinePoint[] {
     let lineLength: number = Math.min(faceBoxRect.width, faceBoxRect.height) * FACE_BOX_LINE_RATIO;
     let linePoints: LinePoint[] = [];

     let startPoints: camera.Point[] = [
       { x: faceBoxRect.topLeftX, y: faceBoxRect.topLeftY },
       { x: faceBoxRect.topLeftX + faceBoxRect.width, y: faceBoxRect.topLeftY },
       { x: faceBoxRect.topLeftX, y: faceBoxRect.topLeftY + faceBoxRect.height },
       { x: faceBoxRect.topLeftX + faceBoxRect.width, y: faceBoxRect.topLeftY + faceBoxRect.height }];

     startPoints.forEach((startPoint: camera.Point) => {
       let horizontalLine: LinePoint = {
         start: startPoint,
         increment: { x: startPoint.x > faceBoxRect.topLeftX ? -lineLength : lineLength, y: 0 }
       };

       let verticalLine: LinePoint = {
         start: startPoint,
         increment: { x: 0, y: startPoint.y > faceBoxRect.topLeftY ? -lineLength : lineLength }
       };

       linePoints.push(horizontalLine, verticalLine);
     });
     return linePoints;
   }
   ```
6. 使用[Line](../harmonyos-references/ts-drawing-components-line.md)组件，将人脸检测框绘制到预览画面中。

   ```typescript
   @Builder
   faceBox(faceBoxRect: camera.Rect) {
     ForEach(calFaceBoxLinePoint(faceBoxRect), (linePoint: LinePoint) => {
       Line()
         .startPoint([0, 0])
         .endPoint([linePoint.increment.x, linePoint.increment.y])
         .stroke(Color.White)
         .position({ x: linePoint.start.x, y: linePoint.start.y })
     }, (linePoint: LinePoint) => JSON.stringify(linePoint));
   }
   ```

## 获取预览帧数据

### 场景描述

在开发相机应用时，如果预览流仅用于展示，通常使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件实现。若需要获取每帧的图像做二次处理（例如二维码识别或人脸识别等场景），则需要通过[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)监听预览流每帧数据，并创建第二路预览流，也称为双路预览。

### 实现原理

**关键技术**

* [ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)用于创建Surface接收每帧的图像数据。
* 通过[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)中的imageArrival事件监听预览流每帧数据，解析图像内容。
* 判断图像宽度width与stride是否一致，不一致则进行裁剪（stride指图像的一行数据在内存中实际占用的字节数，为了内存对齐和提高读取效率的要求，通常大于图像的宽度）。可参考[相机预览花屏解决方案](camera-preview-glitch-solution.md)。
* 屏幕处于不同的显示方向时，原始图像数据需旋转不同的角度，以确保图像在合适的方向显示。需考虑屏幕旋转角度、相机镜头安装角度，框架具体的实现机制可参考[屏幕旋转角度](camera-rotation-term.md#屏幕旋转角度)。在实际开发中，推荐通过[PreviewOutput.getPreviewRotation()](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)方法直接获取旋转角度。
* 对于前置镜头，还需要根据业务需求将数据进行水平镜像翻转，以模拟镜像效果。

**开发流程**

1. 创建ImageReceiver。
2. 获取SurfaceId。
3. 创建第二路预览输出流PreviewOutput。
4. 添加到Session。
5. 监听帧到达事件。
6. 处理并释放帧数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/M84uIYIsSAScrqL1hyLHSw/zh-cn_image_0000002712244776.png)

### 开发步骤

1. 创建[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)组件并获取surfaceId。

   ```typescript
   async init(size: Size, format = image.ImageFormat.JPEG, capacity = 8): Promise<string> {
     const receiver = image.createImageReceiver(size, format, capacity);
     const surfaceId = await receiver.getReceivingSurfaceId();
     this.onImageArrival(receiver);
     return surfaceId;
   }
   ```
2. 创建预览流并配置到相机会话Session中与实现基础预览一致。参考[实现基础预览](camera-preview.md#实现基础预览)中的第4步骤。
3. 使用[ImageReceiver.on()](../harmonyos-references/arkts-apis-image-imagereceiver.md#on9)方法，注册imageArrival事件接收图像数据。使用[ImageReceiver.read()](../harmonyos-references/arkts-apis-image-imagereceiver.md#readnextimage9-1)方法和[image.getComponent()](../harmonyos-references/arkts-apis-image-image.md#getcomponent9-1)方法解析获取图像的Buffer。

   ```typescript
   onImageArrival(receiver: image.ImageReceiver): void {
     receiver.on('imageArrival', () => {
       Logger.info(TAG, 'image arrival');
       receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
         if (err || nextImage === undefined) {
           nextImage?.release();
           Logger.error(TAG, 'readNextImage failed');
           return;
         }
         nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
           if (err || imgComponent === undefined) {
             Logger.error(TAG, 'getComponent failed');
           }
           if (imgComponent.byteBuffer) {
             // ...
           } else {
             Logger.error(TAG, 'byteBuffer is null');
           }
           // ...
         });
       });
     });
   }
   ```
4. 根据stride和图像宽高对Buffer数据进行裁剪。使用[image.createPixelMap()](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)方法创建pixelMap数据。

   **说明** 

   注意在使用createPixelMap()方法处理Buffer数据时，传入的Buffer数据的像素格式[(srcPixelFormat: PixelMapFormat)](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)要与获取预览输出流能力Profile中的[(format: CameraFormat)](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)输出格式保持一致，防止出现图像数据显示异常。format格式之间的映射关系可参考[双路预览](camera-dual-channel-preview.md#用于处理图像的第一路预览流)。

   ```typescript
   async getPixelMap(imgComponent: image.Component, width: number, height: number,
     stride: number): Promise<image.PixelMap> {
     if (stride === width) {
       return await image.createPixelMap(imgComponent.byteBuffer, {
         size: { height: height, width: width },
         srcPixelFormat: image.PixelMapFormat.NV21,
       });
     }
     const dstBufferSize = width * height * 1.5;
     const dstArr = new Uint8Array(dstBufferSize);
     for (let j = 0; j < height * 1.5; j++) {
       const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
       dstArr.set(srcBuf, j * width);
     }
     return await image.createPixelMap(dstArr.buffer, {
       size: { height: height, width: width },
       srcPixelFormat: image.PixelMapFormat.NV21,
     });
   }
   ```
5. 使用[PreviewOutput.getPreviewRotation()](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)获取图像旋转角度，使用[PixelMap.rotate()](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9-1)方法对图像数据进行旋转。在使用前置镜头时，存在水平镜像和垂直镜像的差异，为了统一翻转逻辑，在屏幕旋转角度为90度或270度时，需额外旋转180度将图像转正，使用[PixelMap.flip()](../harmonyos-references/arkts-apis-image-pixelmap.md#flip9-1)方法将图像数据进行水平翻转，以达到镜像效果。参考[应用自绘制预览角度处理](camera-rotation-term.md#应用自绘制预览角度处理)。

   ```typescript
   nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
     if (err || imgComponent === undefined) {
       Logger.error(TAG, 'getComponent failed');
     }
     if (imgComponent.byteBuffer) {
       const width = nextImage.size.width;
       const height = nextImage.size.height;
       const stride = imgComponent.rowStride;
       Logger.info(TAG, `getComponent with width:${width} height:${height} stride:${stride}`);
       const pixelMap = await this.getPixelMap(imgComponent, width, height, stride);
       let displayDefault: display.Display | null = null;
       try {
         displayDefault = display.getDefaultDisplaySync();
         const displayRotation = (displayDefault?.rotation ?? 0) * camera.ImageRotation.ROTATION_90;
         const rotation = this.output?.getPreviewRotation(displayRotation) || 0;
         if (this.position === camera.CameraPosition.CAMERA_POSITION_FRONT) {
           if (displayRotation === 90 || displayRotation === 270) {
             await pixelMap.rotate((rotation + 180) % 360);
           } else {
             await pixelMap.rotate(rotation);
           }
           await pixelMap.flip(true, false);
         } else {
           await pixelMap.rotate(rotation);
         }
         this.callback(pixelMap);
       } catch (exception) {
         Logger.error(TAG,
           `getDefaultDisplaySync failed, code is ${exception.code}, message is ${exception.message}`);
       }
     } else {
       Logger.error(TAG, 'byteBuffer is null');
     }
     // ...
   });
   ```
6. 对[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)组件获取到的图像数据处理后，需要将对应的图像Buffer释放，以确保Surface的BufferQueue正常轮转，防止出现缓冲区溢出等问题。如果对Buffer进行异步操作，则需要在异步操作结束后，确保当前Buffer没有使用的情况下再释放该资源。

   ```typescript
   nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
     // ...
     nextImage.release();
     Logger.info(TAG, 'image process done');
   });
   ```

## 示例代码

* [实现自定义相机功能](https://gitcode.com/harmonyos_samples/CustomCamera)
