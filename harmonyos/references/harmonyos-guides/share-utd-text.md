---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-text
title: 分享文本
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 常见分享场景 > 分享文本
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:8ba172e2bdc61d92c9382c0df23bff7d7a317c8b9fcce80be9fafd24487f0cbd
---

纯文本类型分享支持将一段文字分享到目标设备/目标应用。

* 目标设备接收时，文本会转化为.txt文件保存在文件管理中。
* 目标应用接收时，可便捷地处理文本内容。例如：将文字分享给备忘录，可新增一条备忘录内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/iXV9npudQhyaszwqhM5jrA/zh-cn_image_0000002706675270.png)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { systemShare } from '@kit.ShareKit';
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造分享数据。

   ```typescript
   // 构造ShareData，需配置一条有效数据信息
   let shareData: systemShare.SharedData = new systemShare.SharedData({
     utd: utd.UniformDataType.TEXT,
     content: '这是一段文本内容',
     title: '文本内容', // 不传title字段时,显示content
     description: '文本描述',
     // thumbnail: new Uint8Array() // 推荐传入适合的缩略图 不传则显示默认text图标
   });
   ```
3. 额外增加一条数据。

   ```typescript
   shareData.addRecord({
     utd: utd.UniformDataType.TEXT,
     content: '这是一段文本内容',
     title: '文本内容', // 不传title字段时,显示content
     description: '文本描述'
   });
   ```
4. 启动分享面板。

   ```typescript
   // 进行分享面板显示
   let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
   let uiContext: UIContext = this.getUIContext();
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

   完整示例代码请参见：[samplecode-分享文本](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/TextScenario.ets)。
