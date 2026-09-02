---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-4
title: 如何检测当前相机服务的状态
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何检测当前相机服务的状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:68b9e696fff8dbf6b1adc78edee1fab3d3db4267cbb01122890b43540981d4a2
---

设置状态回调以返回相机状态。

```ts
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
const context = AppStorage.get("context") as UIContext;
let cameraManager = camera.getCameraManager(context.getHostContext()!);
cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
  console.log(`camera : ${cameraStatusInfo.camera.cameraId}`);
  console.log(`status: ${cameraStatusInfo.status}`);
});
```

相机状态：CameraStatus

CameraStatus是一个枚举，表示相机状态。

## 参考链接

[CameraStatus](../harmonyos-references/arkts-apis-camera-e.md#camerastatus)
