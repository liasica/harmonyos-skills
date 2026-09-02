---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-macro
title: 微距能力设置(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 微距能力设置(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:025bde007819d8baabb699bcf68f1a45ecb2a59eda27d46d92d7dcadb4e9b7e7
---

从API version 19开始，支持设置微距能力。微距能力是指通过光学设计与算法优化，实现近距离对焦并清晰捕捉微小物体细节的相机功能。

## 开发步骤

详细的API说明请参考[Camera](../harmonyos-references/arkts-apis-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过[isMacroSupported](../harmonyos-references/arkts-apis-camera-macroquery.md#ismacrosupported19)接口，查询当前设备是否支持微距能力。

   ```ts
   let isSupported: boolean = photoSession.isMacroSupported();
   ```
3. 通过[enableMacro](../harmonyos-references/arkts-apis-camera-macro.md#enablemacro19)接口，开启或关闭微距能力。

   ```ts
   function EnableMacro(photoSession: camera.PhotoSession): void {
      let isSupported: boolean = photoSession.isMacroSupported();
      if (isSupported) {
         photoSession.enableMacro(true);
      }
   }
   ```

## 状态监听

从API version 20开始，支持监听微距能力是否发生改变。

注册macroStatusChanged事件监听微距能力变化，事件监听可参考[on('macroStatusChanged')](../harmonyos-references/arkts-apis-camera-photosession.md#onmacrostatuschanged20)。

```ts
function callback(err: BusinessError, macroStatus: boolean): void {
   if (err !== undefined && err.code !== 0) {
      console.error(`Callback Error, errorCode: ${err.code}`);
      return;
   }
   console.info(`Macro state: ${macroStatus}`);
}

// 注册回调函数。
function registerMacroStatusChanged(photoSession: camera.PhotoSession): void {
   photoSession.on('macroStatusChanged', callback);
}

// 解注册。
function unregisterMacroStatusChanged(photoSession: camera.PhotoSession): void {
   photoSession.off('macroStatusChanged');
}
```
