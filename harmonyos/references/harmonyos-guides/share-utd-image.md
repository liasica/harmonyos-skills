---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-image
title: 分享图片
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 常见分享场景 > 分享图片
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b710a5642b9efc90e44cd85f8a3f8aa6ba3417eeb3aff3a308f0cfacef8dd9cc
---

图片类型分享支持将一张或多张图片分享到目标设备/目标应用。

* 目标设备接收时，图片会保存到图库中。
* 目标应用接收时，可便捷的处理图片内容。例如：将一张图片分享给畅连，发送给畅连好友。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/BEaJalffRMeckfaUnFAXEQ/zh-cn_image_0000002558765682.png?HW-CC-KV=V1&HW-CC-Date=20260429T054035Z&HW-CC-Expire=86400&HW-CC-Sign=3B81FC7C5743C435EB1A8A19A5D172DF12824A6FC5A4706E5C14C18E625C8B7B)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { systemShare } from '@kit.ShareKit';
   2. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   3. import { common } from '@kit.AbilityKit';
   4. import { fileUri } from '@kit.CoreFileKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造分享数据。

   ```
   1. // 构造ShareData，需配置一条有效数据信息
   2. let uiContext: UIContext = this.getUIContext();
   3. let contextFaker: Context = uiContext.getHostContext() as Context;
   4. let filePath = contextFaker.filesDir + '/exampleImage.jpg'; // 仅为示例 请替换正确的文件路径
   5. // 获取精准的utd类型
   6. let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
   7. let shareData: systemShare.SharedData = new systemShare.SharedData({
   8. utd: utdTypeId,
   9. uri: fileUri.getUriFromPath(filePath),
   10. title: '图片标题', // 不传title字段时,显示图片文件名
   11. description: '图片描述', // 不传description字段时,显示图片大小
   12. // thumbnail: new Uint8Array() // 优先使用传递的缩略图预览  不传则默认使用原图做预览图
   13. });
   ```

   说明

   沙箱路径可通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)方法获取文件URI。
3. 额外增加一条数据。

   ```
   1. shareData.addRecord({
   2. utd: utdTypeId,
   3. uri: fileUri.getUriFromPath(filePath),
   4. title: '图片标题', // 不传title字段时,显示图片文件名
   5. description: '图片描述', // 不传description字段时,显示图片大小
   6. });
   ```
4. 启动分享面板。

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

   完整示例代码请参见：[samplecode-分享图片](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/ImageScenario.ets)。
