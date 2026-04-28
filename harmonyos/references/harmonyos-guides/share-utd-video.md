---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-video
title: 分享视频
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 常见分享场景 > 分享视频
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65173a36a8d1acadf117d33b01ee38af7fac9a072863c0bb54a455e83039a717
---

视频类型分享支持将一个或多个视频分享到目标设备/目标应用。

* 目标设备接收时，视频会保存到图库中。
* 目标应用接收时，可便捷地处理视频内容。例如：将一个视频分享给畅连，发送给畅连好友。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/5IPceGO2T7WoHV4zHUvaFA/zh-cn_image_0000002552799532.png?HW-CC-KV=V1&HW-CC-Date=20260427T235101Z&HW-CC-Expire=86400&HW-CC-Sign=7D443CED00324F469BE2BC9C9AD7606FC568715C90D43B5377BC240B0AB7AC9D)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { systemShare } from '@kit.ShareKit';
   2. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   3. import { common } from '@kit.AbilityKit';
   4. import { fileUri } from '@kit.CoreFileKit';
   5. import { image } from '@kit.ImageKit';
   6. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 生成视频封面图（推荐）。

   ```
   1. // 生成视频封面图
   2. let uiContext: UIContext = this.getUIContext();
   3. let contextFaker: Context = uiContext.getHostContext() as Context;
   4. let thumbnailPath = contextFaker.filesDir + '/exampleImage.jpg'; // 仅为示例 请替换正确的文件路径
   5. let imageSource: image.ImageSource = image.createImageSource(thumbnailPath);
   6. let imagePacker: image.ImagePacker = image.createImagePacker();
   7. let buffer: ArrayBuffer = await imagePacker.packToData(imageSource, {
   8. // 当前只支持'image/jpeg','image/webp'和'image/png'类型图片.
   9. format: 'image/jpeg',
   10. // JPEG编码中设定输出图片质量的参数,取值范围为0-100.
   11. // 建议适当压缩,图片过大无法拉起分享.
   12. quality: 30
   13. });
   ```
3. 构造分享数据。

   ```
   1. // 构造ShareData，需配置一条有效数据信息
   2. let filePath = contextFaker.filesDir + '/exampleVideo.mp4'; // 仅为示例 请替换正确的文件路径
   3. // 获取精准的utd类型
   4. let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.mp4', utd.UniformDataType.VIDEO);
   5. let shareData: systemShare.SharedData = new systemShare.SharedData({
   6. utd: utdTypeId,
   7. uri: fileUri.getUriFromPath(filePath),
   8. title: '视频标题', // 不传title字段时,显示视频文件名
   9. description: '视频描述', // 不传description字段时,显示视频大小
   10. thumbnail: new Uint8Array(buffer), // 优先使用传递的缩略图做预览 不传则默认使用视频第一帧画面做预览图
   11. });
   ```

   说明

   沙箱路径可通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)方法获取文件URI。
4. 额外增加一条数据

   ```
   1. shareData.addRecord({
   2. utd: utdTypeId,
   3. uri: fileUri.getUriFromPath(filePath),
   4. title: '视频标题', // 不传title字段时,显示视频文件名
   5. description: '视频描述', // 不传description字段时,显示视频大小
   6. });
   ```
5. 启动分享面板。

   ```
   1. // 进行分享面板显示
   2. let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
   3. let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
   4. controller.show(context, {
   5. selectionMode: systemShare.SelectionMode.SINGLE,
   6. previewMode: systemShare.SharePreviewMode.DETAIL,
   7. }).then(() => {
   8. console.info('ShareController show success.');
   9. }).catch((error: BusinessError) => {
   10. console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
   11. });
   ```

   完整示例代码请参见：[samplecode-分享视频](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/VideoScenario.ets)。
