---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-video
title: 分享视频
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 常见分享场景 > 分享视频
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:fca9b6817f931e8dcc47ed7c74c77d0ed1a612e643ea2032e31e76b590aa796a
---

视频类型分享支持将一个或多个视频分享到目标设备/目标应用。

* 目标设备接收时，视频会保存到图库中。
* 目标应用接收时，可便捷地处理视频内容。例如：将一个视频分享给畅连，发送给畅连好友。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/pkcwHb_IRrGByGIVWTXlpg/zh-cn_image_0000002736314313.png)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { systemShare } from '@kit.ShareKit';
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   import { common } from '@kit.AbilityKit';
   import { fileUri } from '@kit.CoreFileKit';
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 生成视频封面图（推荐）。

   ```typescript
   // 生成视频封面图
   let uiContext: UIContext = this.getUIContext();
   let contextFaker: Context = uiContext.getHostContext() as Context;
   let thumbnailPath = contextFaker.filesDir + '/exampleImage.jpg'; // 仅为示例 请替换正确的文件路径
   let imageSource: image.ImageSource = image.createImageSource(thumbnailPath);
   let imagePacker: image.ImagePacker = image.createImagePacker();
   let buffer: ArrayBuffer = await imagePacker.packToData(imageSource, {
     // 当前只支持'image/jpeg','image/webp'和'image/png'类型图片.
     format: 'image/jpeg',
     // JPEG编码中设定输出图片质量的参数,取值范围为0-100.
     // 建议适当压缩,图片过大无法拉起分享.
     quality: 30
   });
   ```
3. 构造分享数据。

   ```typescript
   // 构造ShareData，需配置一条有效数据信息
   let filePath = contextFaker.filesDir + '/exampleVideo.mp4'; // 仅为示例 请替换正确的文件路径
   // 获取精准的utd类型
   let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.mp4', utd.UniformDataType.VIDEO);
   let shareData: systemShare.SharedData = new systemShare.SharedData({
     utd: utdTypeId,
     uri: fileUri.getUriFromPath(filePath),
     title: '视频标题', // 不传title字段时,显示视频文件名
     description: '视频描述', // 不传description字段时,显示视频大小
     thumbnail: new Uint8Array(buffer) // 优先使用传递的缩略图做预览 不传则默认使用视频第一帧画面做预览图
   });
   ```

   **说明** 

   沙箱路径可通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)方法获取文件URI。
4. 额外增加一条数据

   ```typescript
   shareData.addRecord({
     utd: utdTypeId,
     uri: fileUri.getUriFromPath(filePath),
     title: '视频标题', // 不传title字段时,显示视频文件名
     description: '视频描述' // 不传description字段时,显示视频大小
   });
   ```
5. 启动分享面板。

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

   完整示例代码请参见：[samplecode-分享视频](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/VideoScenario.ets)。
