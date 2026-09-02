---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-system-pressure
title: 压力管控(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 压力管控(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c431460ed4fe53ebb8eef847dba5b03e5221c77324e03ceec43ce3f464db5cb0
---

从API version 20开始，相机框架提供对系统压力等级的监听。

在长时间使用相机的场景（如直播业务）中，相机应用可以通过监听系统压力等级变化，动态调整画质（如帧率、分辨率等），平衡功耗、发热和系统负载，保证功能长时间可用。

## 状态监听

可以通过注册[systemPressureLevelChange](../harmonyos-references/arkts-apis-camera-photosession.md#onsystempressurelevelchange20)的回调函数获取系统压力的监听结果。

当系统压力发生变化时，callback返回SystemPressureLevel参数。

参数的具体内容可参考相机管理器回调接口实例[SystemPressureLevel](../harmonyos-references/arkts-apis-camera-e.md#systempressurelevel20)。

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, systemPressureLevel: camera.SystemPressureLevel): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`systemPressureLevel: ${systemPressureLevel}`);
}

function registerSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
    photoSession.on('systemPressureLevelChange', callback);
}
```
