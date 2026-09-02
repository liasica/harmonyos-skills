---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-image
title: 分享图片
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 常见分享场景 > 分享图片
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:e992eb05fea4dfc6e693ca7e1ca234d314f3da4d161c06066731c61f1eb67717
---

图片类型分享支持将一张或多张图片分享到目标设备/目标应用。

* 目标设备接收时，图片会保存到图库中。
* 目标应用接收时，可便捷的处理图片内容。例如：将一张图片分享给畅连，发送给畅连好友。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/sKUowXynR0CMZZuLKtSmTA/zh-cn_image_0000002706835208.png)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { systemShare } from '@kit.ShareKit';
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   import { common } from '@kit.AbilityKit';
   import { fileUri } from '@kit.CoreFileKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造分享数据。

   ```typescript
   // 构造ShareData，需配置一条有效数据信息
   let uiContext: UIContext = this.getUIContext();
   let contextFaker: Context = uiContext.getHostContext() as Context;
   let filePath = contextFaker.filesDir + '/exampleImage.jpg'; // 仅为示例 请替换正确的文件路径
   // 获取精准的utd类型
   let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
   let shareData: systemShare.SharedData = new systemShare.SharedData({
     utd: utdTypeId,
     uri: fileUri.getUriFromPath(filePath),
     title: '图片标题', // 不传title字段时,显示图片文件名
     description: '图片描述', // 不传description字段时,显示图片大小
     // thumbnail: new Uint8Array() // 优先使用传递的缩略图预览  不传则默认使用原图做预览图
   });
   ```

   **说明** 

   沙箱路径可通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)方法获取文件URI。
3. 额外增加一条数据。

   ```typescript
   shareData.addRecord({
     utd: utdTypeId,
     uri: fileUri.getUriFromPath(filePath),
     title: '图片标题', // 不传title字段时,显示图片文件名
     description: '图片描述' // 不传description字段时,显示图片大小
   });
   ```
4. 启动分享面板。

   ```typescript
   // 进行分享面板显示
   let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
   let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
   controller.show(context, {
     selectionMode: systemShare.SelectionMode.SINGLE,
     previewMode: systemShare.SharePreviewMode.DETAIL
   }).then(() => {
     console.info('ShareController show success.');
   }).catch((error: BusinessError) => {
     console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
   });
   ```

   完整示例代码请参见：[samplecode-分享图片](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/ImageScenario.ets)。
