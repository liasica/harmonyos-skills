---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-angle-adaptation
title: 适配相机旋转角度(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 相机旋转 > 适配相机旋转角度(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:49+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:382dcefbf2235d11c6493b26de926cfdc34d833c63ec7dde0f67fa9d21552c21
---

屏幕处于不同的屏幕状态时，原始图像需旋转不同的角度，以确保图像在合适的方向显示，效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Q5OtMADVRZeE2VPoz6IBqA/zh-cn_image_0000002742003735.png)

本开发指导将指导开发者在预览、拍照、录像等不同场景下，如何适配相机的旋转角度。

* 在预览时，图像旋转角度与屏幕显示旋转角度（[Display](../harmonyos-references/js-apis-display.md#属性).rotation）相关。具体开发指导：[创建会话](camera-rotation-angle-adaptation.md#创建会话) > [预览](camera-rotation-angle-adaptation.md#预览)。
* 在拍照、录像时，图像旋转角度与设备重力方向（即[设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)）相关。

  拍照开发指导：[创建会话](camera-rotation-angle-adaptation.md#创建会话) > [计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度) > [拍照](camera-rotation-angle-adaptation.md#拍照)。

  录像开发指导：[创建会话](camera-rotation-angle-adaptation.md#创建会话) > [计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度) > [录像](camera-rotation-angle-adaptation.md#录像)。

在本开发指导中，提供两种方案来获取预览、拍照、录像的旋转角度：

* 方案一：需要应用通过[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)接口获取[Display](../harmonyos-references/js-apis-display.md#属性)对象并读取其rotation属性值来获取[显示设备的屏幕旋转角度](camera-rotation-term.md#屏幕旋转角度)，通过重力传感器来[计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)。
* 方案二：从API版本23开始，支持通过[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)、[getPhotoRotation](../harmonyos-references/arkts-apis-camera-photooutput.md#getphotorotation12)、[getVideoRotation](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)接口不传入参数来获取旋转角度，由系统侧获取[显示设备的屏幕旋转角度](camera-rotation-term.md#屏幕旋转角度)和[计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

详细的API参考说明，请参考[Camera API文档](../harmonyos-references/js-apis-camera.md)。

## 创建会话

1. 导入相机等相关模块。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建[Session](../harmonyos-references/arkts-apis-camera-session.md)会话。

   相机使用预览等功能前，均需创建相机会话，调用[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)方法创建一个会话，创建会话时需指定创建[SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)为NORMAL\_PHOTO或NORMAL\_VIDEO，创建的session处于拍照或者录像模式。

   ```typescript
   createPhotoSession(cameraManager: camera.CameraManager): camera.Session | undefined {
     let session: camera.Session | undefined = undefined;
     try {
       session = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the session instance. error: ${err}`);
     }
     return session;
   }

   createVideoSession(cameraManager: camera.CameraManager): camera.Session | undefined {
     let session: camera.Session | undefined = undefined;
     try {
       session = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the session instance. error: ${err}`);
     }
     return session;
   }
   ```

## 预览

完成[会话创建](camera-rotation-angle-adaptation.md#创建会话)后，开发者可根据实际需求，配置输出流。

1. 在[会话配置](camera-session-management.md)过程中获取并设置[预览旋转角度](camera-rotation-term.md#预览旋转角度)，即：使用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)接口提交相关配置后调用，建议在[Start](../harmonyos-references/arkts-apis-camera-session.md#start11)起流前调用。

   **接口说明**
   * 通过调用[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)中的[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)接口，获取预览旋转角度。
   * 通过调用[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)中的[setPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#setpreviewrotation12)接口，设置预览旋转角度。如果多次调用，以最新调用设置的预览旋转角度为准。
   * [getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)、[setPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#setpreviewrotation12)接口需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用，如果存在异步执行的情况，previewOutput未添加到session里或者已调用的session.release，导致session与PreviewOutput两者关系未绑定，此时调用会调用失败，并抛出错误码[CameraErrorCode.SERVICE\_FATAL\_ERROR](../harmonyos-references/errorcode-camera.md#section7400201-相机服务异常)。**实现方案**
   * **方案一：**

     由应用通过[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)接口获取[Display](../harmonyos-references/js-apis-display.md#属性)对象并读取其rotation属性值，来计算displayRotation（[显示设备的屏幕旋转角度](camera-rotation-term.md#屏幕旋转角度)），将对应角度填入[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)接口。

     例如，Display.rotation = 1，表示显示设备屏幕顺时针旋转为90°，此处displayRotation填入90。

     + isDisplayLocked：可选入参，默认为false。当设置为false，即屏幕方向未锁定，[预览旋转角度](camera-rotation-term.md#预览旋转角度)将根据[相机镜头角度](camera-rotation-term.md#相机镜头安装角度)和[屏幕显示旋转角度](camera-rotation-term.md#屏幕旋转角度)的值计算；当设置为true，Surface旋转锁定，不跟随窗口变化，旋转角度仅取相机镜头角度计算。

     ```typescript
     import { display } from '@kit.ArkUI';
     import { camera } from '@kit.CameraKit';

     GetAndSetPreviewRotation(previewOutput: camera.PreviewOutput) {
       // previewOutput是创建的预览输出
       try {
         let displayRotation = display.getDefaultDisplaySync().rotation;
         let previewRotation = previewOutput.getPreviewRotation(displayRotation * camera.ImageRotation.ROTATION_90);
         let isDisplayLocked: boolean = false; // 建议与setXComponentSurfaceRotation入参的lock属性保持一致
         previewOutput.setPreviewRotation(previewRotation, isDisplayLocked);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`GetAndSetPreviewRotation call failed. error code: ${err.code}`);
       }
     }
     ```
   * **方案二：**

     从API版本23开始，入参displayRotation为可选参数，当不传入参数时，由系统获取displayRotation进行预览旋转角度计算。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

     + isDisplayLocked：可选入参，默认为false。当设置为false，即屏幕方向未锁定，[预览旋转角度](camera-rotation-term.md#预览旋转角度)将根据[相机镜头角度](camera-rotation-term.md#相机镜头安装角度)和[屏幕显示旋转角度](camera-rotation-term.md#屏幕旋转角度)的值计算；当设置为true，Surface旋转锁定，不跟随窗口变化，旋转角度仅取相机镜头角度计算。

     ```typescript
     import { camera } from '@kit.CameraKit';

     GetAndSetPreviewRotationWithoutDisplayRotation(previewOutput: camera.PreviewOutput) {
       // previewOutput是创建的预览输出
       try {
         let previewRotation = previewOutput.getPreviewRotation();
         let isDisplayLocked: boolean = false; // 建议与setXComponentSurfaceRotation入参的lock属性保持一致
         previewOutput.setPreviewRotation(previewRotation, isDisplayLocked);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`GetAndSetPreviewRotationWithoutDisplayRotation call failed. error code: ${err.code}`);
       }
     }
     ```
2. 通过[监听Display对象变化](../harmonyos-references/js-apis-display.md#displayonadd--remove--change)，感知窗口当前状态，如当前相机窗口发生旋转时，需对预览流进行角度修正。推荐在[会话配置](camera-session-management.md)中完成获取并设置预览旋转后，直接创建监听。

   * **方案一：**

     ```typescript
     display.off('change');
     display.on('change', () => {
       GetAndSetPreviewRotation(previewOutput);
     });
     ```
   * **方案二：**

     从API版本23开始，入参displayRotation为可选参数，当不传入参数时，由系统获取displayRotation进行预览旋转角度计算。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

     ```typescript
     display.off('change');
     display.on('change', () => {
       GetAndSetPreviewRotationWithoutDisplayRotation(previewOutput);
     });
     ```

## 拍照

完成[会话创建](camera-rotation-angle-adaptation.md#创建会话)后，开发者可根据实际需求，配置输出流。

1. 调用[PhotoOutput](../harmonyos-references/arkts-apis-camera-photooutput.md)中的[getPhotoRotation](../harmonyos-references/arkts-apis-camera-photooutput.md#getphotorotation12)可以获取到拍照旋转角度。该接口需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用。

   * **方案一：**

     deviceDegree：设备旋转角度。拍照的旋转角度与重力方向（即设备旋转角度）相关，获取方式请见[计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)。

     ```typescript
     getPhotoRotation(photoOutput: camera.PhotoOutput, deviceDegree: number): camera.ImageRotation {
       let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
       try {
         photoRotation = photoOutput.getPhotoRotation(deviceDegree);
         console.info(`Photo rotation is: ${photoRotation}`);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`The photoOutput.getPhotoRotation call failed. error code: ${err.code}`);
       }
       return photoRotation;
     }
     ```
   * **方案二：**

     从API版本23开始，入参deviceDegree为可选参数，当不传入参数时，由系统获取deviceDegree进行拍照旋转角度计算。当重力传感器数据无效，无法计算deviceDegree时，系统将使用最后一次有效的deviceDegree。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

     ```typescript
     getPhotoRotationWithoutDeviceDegree(photoOutput: camera.PhotoOutput): camera.ImageRotation {
       let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
       try {
         photoRotation = photoOutput.getPhotoRotation();
         console.info(`Photo rotation is: ${photoRotation}`);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`The photoOutput.getPhotoRotationWithoutDeviceDegree call failed. error code: ${err.code}`);
       }
       return photoRotation;
     }
     ```
2. 应用将拍照角度写入[PhotoCaptureSetting](../harmonyos-references/arkts-apis-camera-i.md#photocapturesetting).rotation。
3. 其余参数的配置及拍照，可参考[拍照开发指导](camera-shooting.md)。

## 录像

完成[会话创建](camera-rotation-angle-adaptation.md#创建会话)后，开发者可根据实际需求，配置输出流。

1. 调用[VideoOutput](../harmonyos-references/arkts-apis-camera-videooutput.md)中的[getVideoRotation](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)可以获取到录像的旋转角度。该接口需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用。

   * **方案一：**

     deviceDegree：设备旋转角度。录像的旋转角度与重力方向（即设备旋转角度）相关，获取方式请见[计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)。

     ```typescript
     getVideoRotation(videoOutput: camera.VideoOutput, deviceDegree: number): camera.ImageRotation {
       let videoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
       try {
         videoRotation = videoOutput.getVideoRotation(deviceDegree);
         console.info(`Video rotation is: ${videoRotation}`);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`The videoOutput.getVideoRotation call failed. error code: ${err.code}`);
       }
       return videoRotation;
     }
     ```
   * **方案二：**

     从API版本23开始开始，入参deviceDegree为可选参数，当不传入参数时，由系统获取deviceDegree进行录像旋转角度计算。当重力传感器数据无效，无法计算deviceDegree时，系统将使用最后一次有效的deviceDegree。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

     ```typescript
     getVideoRotationWithoutDeviceDegree(videoOutput: camera.VideoOutput): camera.ImageRotation {
       let videoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
       try {
         videoRotation = videoOutput.getVideoRotation();
         console.info(`Video rotation is: ${videoRotation}`);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`The videoOutput.getVideoRotationWithoutDeviceDegree call failed. error code: ${err.code}`);
       }
       return videoRotation;
     }
     ```
2. 在[AVRecorder.prepare](../harmonyos-references/arkts-apis-media-avrecorder.md#prepare9)后使用[updateRotation](../harmonyos-references/arkts-apis-media-avrecorder.md#updaterotation12)设置录像角度。
3. 其余参数的配置及启动录像，可参考[录像开发指导](camera-recording.md)。

## 计算设备旋转角度

当前可通过调用[once(type: SensorId.GRAVITY, callback: Callback<GravityResponse>)](../harmonyos-references/js-apis-sensor.md#sensoronsensoridgravity9)获取一次重力传感器在x、y、z三个方向上的数据，计算得出设备旋转角度deviceDegree，示例如下所示。

如果无法获得重力传感器数据，需要申请重力传感器权限ohos.permission.ACCELEROMETER。权限申请请参考[声明权限](declare-permissions.md)，如何获取传感器数据请参考[传感器开发指导](sensor-guidelines.md)。

```typescript
getRealData(data: sensor.GravityResponse): number {
  let getDeviceDegree: number = 0;
  let x = data.x;
  let y = data.y;
  let z = data.z;
  if ((x * x + y * y) * 3 < z * z) {
    return getDeviceDegree;
  } else {
    try {
      let sd: Decimal = Decimal.atan2(y, -x);
      let sc: Decimal = Decimal.round(Number(sd) / 3.141592653589 * 180);
      getDeviceDegree = 90 - Number(sc);
      getDeviceDegree = getDeviceDegree >= 0 ? getDeviceDegree % 360 : getDeviceDegree % 360 + 360;
    } catch (error) {
      let err = error as BusinessError;
      console.error(`decimal failed, error: ${err.code}`);
    }
  }
  return getDeviceDegree;
}

async getGravity() : Promise<number> {
  let data: sensor.Sensor[];
  let isSupported: boolean = false;
  try {
    data = await sensor.getSensorList();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`getSensorList failed, error: ${err.code}`);
    return -1; // 异常场景下返回默认值
  }

  for (let i = 0; i < data.length; i++) {
    if (data[i].sensorId === sensor.SensorId.GRAVITY) {
      isSupported = true;
      break;
    }
  }
  try {
    if (isSupported === true) {
      const promise: Promise<number> = new Promise((resolve) => {
        sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
          resolve(this.getRealData(data));
        });
      })
      return promise;
    } else {
      const promise: Promise<number> = new Promise((resolve) => {
        sensor.once(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
          resolve(this.getRealData(data as sensor.GravityResponse));
        });
      })
      return promise;
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(`gePromise failed, error: ${err.code}`);
    return -1; // 异常场景下返回默认值
  }
}

// 获取当前设备旋转角度
async getCurrentDeviceDegree() : Promise<number> {
  getDeviceDegree = await getGravity(); // 调用使用await
  return getDeviceDegree;
}
```

## 视频通话送远端场景

两个设备之间进行视频通话，存在设备间持握方向不一致问题，建议**在本端将画面转正**，再通过网络发送到对端，画面转正参考[自绘制场景预览角度的归一化处理](camera-rotation-angle-adaptation.md#自绘制场景预览角度的归一化处理)。

## 实现相机无损出图

在部分折叠屏设备上，[不同折叠状态](../harmonyos-references/js-apis-display.md#foldstatus10)下的[设备自然方向](camera-rotation-term.md#设备自然方向)会发生改变，导致不同折叠状态下真实的[相机镜头安装角度](camera-rotation-term.md#相机镜头安装角度)不同。为了屏蔽不同设备间的差异，使得不同折叠状态下的相机镜头安装角度一致，系统会自动调整部分折叠状态下的相机采集图像方向（通过旋转裁切的方式）和相机镜头安装角度，因此会存在视场角（Field of View, FOV）损失，可能会导致相机预览、拍照、录像可见范围降低，因此如果需要实现相机无损出图，可以通过[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)接口来实现相机无损出图。具体方式如下：

设备是否支持无损出图，首先需要确认设备的相机镜头安装角度是否可变，可以通过[isPhysicalCameraOrientationVariable](../harmonyos-references/arkts-apis-camera-camerainput.md#isphysicalcameraorientationvariable22)接口查询。

1. 当相机镜头安装角度不可变时，不同折叠状态下的相机出图均为无损出图。
2. 当相机镜头安装角度可变时：

   如应用需要实现相机无损出图，由于相机镜头安装角度与相机旋转相关，需要应用完成[相机旋转的适配](camera-rotation-angle-adaptation.md#top)后，通过[getPhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#getphysicalcameraorientation22)接口获取设备当前折叠状态下真实的相机镜头安装角度，并通过[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)接口实现相机无损出图（相机镜头安装角度不可变时使用[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)将会返回[7400102](../harmonyos-references/errorcode-camera.md#section7400102-非法操作)错误码，未适配相机旋转时使用相机无损出图会导致预览、拍照、录像旋转异常），推荐在[createCameraInput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createcamerainput)后直接使用[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)接口实现相机无损出图。

示例代码如下：

```typescript
enablePhysicalCameraOrientation(cameraInput: camera.CameraInput) {
  // 查询设备的相机镜头安装角度是否可变
  let isVariable: boolean = cameraInput.isPhysicalCameraOrientationVariable();

  if (isVariable) {
    // 获取设备当前折叠状态下真实的相机镜头安装角度
    let physicalOrientation: number = cameraInput.getPhysicalCameraOrientation();
    console.info(`physical Orientation is ${physicalOrientation}`);

    // 选择是否使用真实的相机镜头安装角度, 以实现无损出图
    let isUsed: boolean = true;
    cameraInput.usePhysicalCameraOrientation(isUsed);
  }
}
```

## 常见问题

### 指定XComponent的大小，防止旋转后图像拉伸变形

图像显示出现拉伸或压缩等变形，是因为图像分辨率与[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)的宽高比不匹配。以应用层下发的1920\*1080(16:9)竖屏和横屏为例，器件出图均是按照4:3比例出一张RAW图，在此基础上，根据应用层下发的16:9比例进行裁切，提供数据给应用层。因此，无论手机持握方向如何变化，应用层接收的数据始终是16:9比例的图片。具体图示如下：

| 设备和镜头方向 | 处理过程示意图 | XComponent布局 |
| --- | --- | --- |
| **设备条件：**  手机竖屏、充电口向下。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 0°，[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 0  - **图像预览旋转角度 = 0°+90° = 90°** |  | 出图与最终成像有90度夹角，布局宽高与图像宽高交换。 |
| **设备条件：**  手机横屏、充电口向右。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 270°，[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 3  - **图像预览旋转角度 = 270°+90° = 360° = 0°** |  | 出图与最终成像有0度夹角，布局与图像宽高比一致。 |

从上图可以看出，当手机从竖屏转换为横屏时，图像始终保持16:9的输出比例，但镜头与屏幕显示方向之间的夹角从90度变为0度。如果布局保持9:16不变，那么16:9的图像数据放置在9:16的空间内显示，会导致图像形变。因此，为确保图像显示正常，横屏时需要将布局的宽高比调整为16:9。

首先，将XComponent的宽度和高度作为状态变量进行监听，通过[Window.on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)监听窗口的变化，根据屏幕旋转角度（[Display.rotation](../harmonyos-references/js-apis-display.md#属性) ）与相机镜头角度（[CameraDevice.cameraOrientation](../harmonyos-references/js-apis-display.md#orientation10)）之间的角度来确定布局的宽高比，以确保布局能跟随窗口实时调整。

具体的实现方法如下，在需要进行横竖屏切换的页面中，通常建议在aboutToAppear中执行窗口变化的监听。

```ts
import { bundleManager } from '@kit.AbilityKit';
import { display } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { BusinessError, deviceInfo  } from '@kit.BasicServicesKit';

// ....
let previewOutput : camera.PreviewOutput; // 根据具体使用场景创建的预览输出流
let cameraDevice : camera.CameraDevice; // 根据使用诉求选择符合的相机设备
@Entry
@Component
struct Index {
  @State mXComponentWidth: number = 1280;
  @State mXComponentHeight: number = 720;
  @State mRotate: number = 0;
  @State mConfigRatio: number = 16 / 9;
  private targetVersion: number = 0;
  private mWindowHeight = 0;
  private mWindowWidth = 0;

  private windowClass = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync();
  getBundleInfoForSelf() { // 获取应用的编译版本
    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
    try {
      bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
        console.info(`getBundleInfoForSelf successfully. Data: ${data.targetVersion}`);
        this.targetVersion = data.targetVersion;
      }).catch((err: BusinessError) => {
        console.error(`getBundleInfoForSelf failed ${err}`);
      });
    } catch (err) {
      let message = (err as BusinessError).message;
      console.error(`getBundleInfoForSelf failed ${message}`);
    }
  }

  isIsolateForSpecialType(): boolean { // 兼容平板API14之前的设备
    return deviceInfo.deviceType == "tablet" && this.targetVersion <= 50000013;
  }

  aboutToAppear(): void {
    this.updateXComponentSize();
    this.getBundleInfoForSelf();
    this.windowClass.on('windowSizeChange', (size) => {
      this.mWindowWidth = size.width;
      this.mWindowHeight = size.height;
      this.updateXComponentSize();
    });
    let rotation : number = 0;
    try {
      rotation = display.getDefaultDisplaySync().rotation;
      this.mRotate = rotation * camera.ImageRotation.ROTATION_90;
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to get display rotation: ${err.code}, ${err.message}`);
      this.mRotate = 0;
    }
    display.on('change', () => {
      if (this.mRotate!= rotation * camera.ImageRotation.ROTATION_90) {
        this.mRotate= rotation * camera.ImageRotation.ROTATION_90; // 获取屏幕旋转角度
        this.updateXComponentSize();
        let imageRotation = this.getImageRotation();
        if (!imageRotation) {
          console.error(`current get image rotation is undefined`);
          return;
        }
        let previewRotation = previewOutput.getPreviewRotation(imageRotation); // previewOutput是创建的预览流
        previewOutput.setPreviewRotation(previewRotation, false);
      }
    });
  }
  getImageRotation() : camera.ImageRotation | undefined {
    let displayRotation : number= 0;
    try {
      displayRotation = display.getDefaultDisplaySync().rotation
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to get display rotation: ${err.code}, ${err.message}`);
      return undefined;
    }
    let imageRotation = displayRotation * camera.ImageRotation.ROTATION_90;
    return imageRotation;
  }
  updateXComponentSize(): void {
    let angleDiff = (this.mRotate+ cameraDevice?.cameraOrientation) % 360;
    if (this.isIsolateForSpecialType()) { // 如果设备为平板设备，且使用的API版本＜14，应进入此逻辑。
      if (angleDiff === 90 || angleDiff=== 270) {
      this.mXComponentWidth = this.mConfigRatio * this.mWindowHeight;
      this.mXComponentHeight = this.mWindowHeight;
    } else {
      this.mXComponentWidth = this.mWindowWidth;
      this.mXComponentHeight = this.mConfigRatio * this.mWindowWidth; // 1920 *1080
    }
    } else { // 如果使用API版本≥14，或是API14以下的非平板设备，应进入此逻辑。
      if (angleDiff === 90 || angleDiff=== 270) {
        this.mXComponentWidth = this.mWindowWidth;
        this.mXComponentHeight = this.mConfigRatio * this.mWindowWidth; // 1920 *1080
      } else {
        this.mXComponentWidth = this.mConfigRatio * this.mWindowHeight;
        this.mXComponentHeight = this.mWindowHeight;
      }
    }
  }

  async aboutToDisAppear(): Promise<void> {
    display.off('change');
    this.windowClass.off('windowSizeChange');
    // 解注册
  }
  build() {
    // 根据使用诉求补充界面处理逻辑。
  }
}
```

除了指定XComponent的宽高外，还可以通过设置XComponent的renderFit来实现图片的自适应大小显示、居中裁剪显示等效果。具体详情请参考[RenderFit介绍](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit)。

### 自绘制场景预览角度的归一化处理

在自绘制场景中，对于后置摄像头，可以通过调用[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)获取旋转角度，将图像转正；对于前置摄像头，由于存在水平镜像和垂直镜像的差异，为了简化操作，需先对前置摄像头的图像角度进行归一化处理后，再将图像转正，并根据业务需求决定是否进行镜像处理。

pixelMap处理方式：

```ts
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { display } from '@kit.ArkUI';

let previewOutputReceiver: camera.PreviewOutput | undefined = undefined; // 回调流定义
let curCameraPosition = camera.CameraPosition.CAMERA_POSITION_FRONT; // 相机设备的位置定义，此处以前置为例。
// .....
function  onImageArrival(receiver: image.ImageReceiver): void {
  receiver.on('imageArrival', () => { // imageRecevier回调
    // 获取图像
    receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
      if (err || nextImage === undefined) {
        console.error('readNextImage failed');
        return;
      }
      // 解析图像内容
      nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
        if (err || imgComponent === undefined) {
          console.error('getComponent failed');
        }

        if (imgComponent.byteBuffer) {
          let width = nextImage.size.width; // 获取图片的宽
          let height = nextImage.size.height; // 获取图片的高
          let stride = imgComponent.rowStride; // 获取图片的stride
          // stride与width一致
          if (stride == width) {
            let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
              size: { height: height, width: width },
              srcPixelFormat: image.PixelMapFormat.NV21, // 此处以NV21为例
            })
            updatePixelMap(pixelMap);
          } else {
            // stride与width不一致
            const dstBufferSize = width * height * 1.5 // 以NV21为例（YUV_420_SP格式的图片）YUV_420_SP内存计算公式：长x宽+(长x宽)/2
            const dstArr = new Uint8Array(dstBufferSize)
            for (let j = 0; j < height * 1.5; j++) {
              const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width)
              dstArr.set(srcBuf, j * width)
            }
            let pixelMap = await image.createPixelMap(dstArr.buffer, {
              size: { height: height, width: width },
              srcPixelFormat: image.PixelMapFormat.NV21, // 此处以NV21为例
            });
            updatePixelMap(pixelMap);
          }
        } else {
          console.error('byteBuffer is null');
        }
        // 确保当前buffer没有在使用的情况下，可进行资源释放。
        // 如果对buffer进行异步操作，需要在异步操作结束后再释放该资源（nextImage.release()）。
        nextImage.release();
        console.info('image process done');
      })
    })
  })
}
```

```ts
async function updatePixelMap(pixelMap: image.PixelMap): Promise<void> {
  let rotation : number = 0;
  try {
    rotation = display.getDefaultDisplaySync().rotation * camera.ImageRotation.ROTATION_90;
  } catch (error) {
    const err = error as BusinessError;
    console.error(`Failed to get display rotation: ${err.code}, ${err.message}`);
    return;
  }
  let angle = previewOutputReceiver?.getPreviewRotation(rotation);
  if (angle === undefined) {
    return;
  }
  // 在display.on中对该previewOutput设置过setPreviewRotation，此处可以不执行。
  previewOutputReceiver?.setPreviewRotation(angle);
  if (curCameraPosition === camera.CameraPosition.CAMERA_POSITION_FRONT) {
    if (rotation ===90 || rotation === 270) {
      angle = (angle + 180 ) % 360;
    }
    await pixelMap.rotate(angle);
    await pixelMap.flip(true, false);
  } else {
    await pixelMap.rotate(angle);
  }
}
```

### 适配一多设备

为了适配一多设备，主要分为以下几步：

1. 根据屏幕比例选择合适的预览分辨率。
2. 根据确定的预览分辨率，通过宽/高得到新的比例。
3. 根据上一步的比例计算XComponent宽高，可参考[指定XComponent的大小，防止旋转后图像拉伸变形](camera-rotation-angle-adaptation.md#指定xcomponent的大小防止旋转后图像拉伸变形)，将mConfigRatio应用于布局宽高的计算。

   **说明** 

   在适配折叠屏设备时，每次折叠屏镜头变化都需要重新获取屏幕比例。

```ts
let mConfigRatio: number = 16 / 9; // 设置分辨率比例初始值，此处以16:9宽高比为例。
let reConfigType : number = 720;
let previewProfileObj: camera.Profile = {
  format: 1003,
  size: {
    width: 1280,
    height: 720
  }
};
// 根据屏幕初步计算比例，长边/短边
function getConfigRation(cameraDevice: camera.CameraDevice, cameraManager: camera.CameraManager) : number {
  let previewProfile = getSurfaceSize(cameraDevice, mConfigRatio, cameraManager); // 获取最接近的分辨率
  if (previewProfile === undefined || previewProfile.size === undefined) {
    return 0;
  }
  mConfigRatio = previewProfile.size.width / previewProfile.size.height; // 以新的比例重新计算显示宽高
  return mConfigRatio;
}

// 获取最接近屏幕的分辨率
function getSurfaceSize(cameraDevice: camera.CameraDevice, configRatio: number, cameraManager: camera.CameraManager): camera.Profile | undefined {
  console.info(`previewProfiles is ${configRatio}`);
  let cameraOutputCapability =
    cameraManager.getSupportedOutputCapability(cameraDevice, camera.SceneMode.NORMAL_PHOTO); // 此处以NORMAL_PHOTO为例
  return getPreviewProfile(cameraOutputCapability, configRatio);
}
function getPreviewProfile(cameraOutputCapability: camera.CameraOutputCapability, configRatio: number): camera.Profile | undefined {
  let previewProfiles = cameraOutputCapability.previewProfiles;
  if (previewProfiles.length < 1) {
    return undefined;
  }
  console.info(`previewProfiles this.foramt: ${previewProfileObj.format} configRatio = ${configRatio}`);
  let optimalSize: camera.Profile|undefined;
  let minDiff = Number.MAX_VALUE;
  // 计算屏幕的宽高比
  for (let i = 0; i < previewProfiles.length; i++) {
    if (previewProfiles[i].format !== previewProfileObj.format) {
      continue;
    }
    let ratio = previewProfiles[i].size.width / previewProfiles[i].size.height; // 1088*1080
    // 检查宽高比是否匹配
    if (Math.abs(ratio - configRatio) > 0.2) continue; // 0.2的误差可自行调整
    // 选择最接近的分辨率
    if (Math.abs(previewProfiles[i].size.height - reConfigType) < minDiff) {
      optimalSize = previewProfiles[i];
      minDiff = Math.abs(previewProfiles[i].size.height - reConfigType);
    }
  }

  // 如果没有找到合适的分辨率，选择第一个
  if (optimalSize === undefined) {
    minDiff = Number.MAX_VALUE;
    for (let i = 0; i < previewProfiles.length; i++) {
      if (previewProfiles[i].format !== previewProfileObj.format) {
        continue;
      }
      if (Math.abs(previewProfiles[i].size.height - reConfigType) < minDiff) { // 720
        optimalSize = previewProfiles[i];
        minDiff = Math.abs(previewProfiles[i].size.height - reConfigType);
      }
    }
  }
  return optimalSize;
}
```

### 拍照无法镜像

通过设置[PhotoCaptureSetting](../harmonyos-references/arkts-apis-camera-i.md#photocapturesetting)中的mirror属性改变拍照镜像。

```ts
// this.photoOutput是拍照输出output, this.getDeviceDegree是重力角度
let photoSettings: camera.PhotoCaptureSetting = {
  quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
  mirror: this.photoOutput?.isMirrorSupported() // 设置拍照镜像，true表示镜像，false表示非镜像
};
// ... 省略获取代码
this.photoRotation = getPhotoRotation(this.photoOutput!!,this.getDeviceDegree)
photoSettings.rotation = this.photoRotation // 指定拍照旋转角度
```
