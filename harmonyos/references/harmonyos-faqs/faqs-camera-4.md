---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-4
title: 如何检测当前相机服务的状态
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何检测当前相机服务的状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:aaf860ca9352e2c0dda4576250e8183a95045054fbca2626db8b17788a358bde
---

设置状态回调以返回相机状态。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. const context = AppStorage.get("context") as UIContext;
4. let cameraManager = camera.getCameraManager(context.getHostContext()!);
5. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
6. console.log(`camera : ${cameraStatusInfo.camera.cameraId}`);
7. console.log(`status: ${cameraStatusInfo.status}`);
8. });
```

[GetCameraStatus.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetCameraStatus.ets#L21-L28)

相机状态：CameraStatus

CameraStatus是一个枚举，表示相机状态。

**参考链接**

[CameraStatus](../harmonyos-references/arkts-apis-camera-e.md#camerastatus)
