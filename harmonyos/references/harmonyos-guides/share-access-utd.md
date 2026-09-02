---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-utd
title: 宿主应用发起分享需使用精细化的utd类型
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit体验规范 > 宿主应用发起分享需使用精细化的utd类型
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:66e985d5169b52f1d0855a34aa8a731567d3fb6501d5fd3af2dff963f02e6831
---

utd类型指分享数据的数据类型，精准的数据类型有助于帮助宿主应用匹配到精确的目标应用，让分享内容更好的传递。

当构造分享数据时，推荐宿主应用填写精准的utd类型，可通过以下两种方式获取：

* 根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型的ID。参见：[uniformTypeDescriptor.getUniformDataTypeByFilenameExtension](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformtypedescriptorgetuniformdatatypebyfilenameextension11)。

  ```typescript
  import { common } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { uniformTypeDescriptor as utd } from '@kit.ArkData';
  import { systemShare } from '@kit.ShareKit';

  try {
    let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
    if (utdTypeId) {
      // 构造ShareData，需配置一条有效数据信息
      let shareData: systemShare.SharedData = new systemShare.SharedData({
        utd: utdTypeId,
        uri: 'file://.../xxx.jpg'
      });
      // 构建ShareController
      let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
      // 获取UIAbility上下文对象
      let uiContext: UIContext = this.getUIContext();
      let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
      // 进行分享面板显示
      controller.show(context, {
        previewMode: systemShare.SharePreviewMode.DEFAULT,
        selectionMode: systemShare.SelectionMode.SINGLE
      });
    }
  } catch (e) {
    let error: BusinessError = e as BusinessError;
    console.error(`Failed to getUniformDataTypeByFilenameExtension. Code: ${error.code}, message: ${error.message} `);
  }
  ```
* 根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型的ID。参见：[uniformTypeDescriptor.getUniformDataTypeByMIMEType](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformtypedescriptorgetuniformdatatypebymimetype11)。

  ```typescript
  import { common } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { uniformTypeDescriptor as utd } from '@kit.ArkData';
  import { systemShare } from '@kit.ShareKit';

  try {
    let utdTypeId = utd.getUniformDataTypeByMIMEType('image/jpeg', utd.UniformDataType.IMAGE);
    if (utdTypeId) {
      // 构造ShareData，需配置一条有效数据信息
      let shareData: systemShare.SharedData = new systemShare.SharedData({
        utd: utdTypeId,
        uri: 'file://.../xxx.jpg'
      });
      // 构建ShareController
      let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
      // 获取UIAbility上下文对象
      let uiContext: UIContext = this.getUIContext();
      let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
      // 进行分享面板显示
      controller.show(context, {
        previewMode: systemShare.SharePreviewMode.DEFAULT,
        selectionMode: systemShare.SelectionMode.SINGLE
      });
    }
  } catch (e) {
    let error: BusinessError = e as BusinessError;
    console.error(`Failed to getUniformDataTypeByMIMEType. Code: ${error.code}, message: ${error.message} `);
  }
  ```
