---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-utd
title: 宿主应用发起分享需使用精细化的utd类型
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit体验规范 > 宿主应用发起分享需使用精细化的utd类型
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:afd2063bc0e21ddc748c5dcbc79a41faaf0b48e670eb6dc03107ba853d1132ff
---

utd类型指分享数据的数据类型，精准的数据类型有助于帮助宿主应用匹配到精确的目标应用，让分享内容更好的传递。

当构造分享数据时，推荐宿主应用填写精准的utd类型，可通过以下两种方式获取：

* 根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型的ID。参见：[uniformTypeDescriptor.getUniformDataTypeByFilenameExtension](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformtypedescriptorgetuniformdatatypebyfilenameextension11)。

  ```
  1. import { common } from '@kit.AbilityKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
  4. import { systemShare } from '@kit.ShareKit';

  6. try {
  7. let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
  8. if (utdTypeId) {
  9. // 构造ShareData，需配置一条有效数据信息
  10. let shareData: systemShare.SharedData = new systemShare.SharedData({
  11. utd: utdTypeId,
  12. uri: 'file://.../xxx.jpg'
  13. });
  14. // 构建ShareController
  15. let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
  16. // 获取UIAbility上下文对象
  17. let uiContext: UIContext = this.getUIContext();
  18. let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
  19. // 进行分享面板显示
  20. controller.show(context, {
  21. previewMode: systemShare.SharePreviewMode.DEFAULT,
  22. selectionMode: systemShare.SelectionMode.SINGLE
  23. });
  24. }
  25. } catch (e) {
  26. let error: BusinessError = e as BusinessError;
  27. console.error(`Failed to getUniformDataTypeByFilenameExtension. Code: ${error.code}, message: ${error.message} `);
  28. }
  ```
* 根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型的ID。参见：[uniformTypeDescriptor.getUniformDataTypeByMIMEType](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformtypedescriptorgetuniformdatatypebymimetype11)。

  ```
  1. import { common } from '@kit.AbilityKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
  4. import { systemShare } from '@kit.ShareKit';

  6. try {
  7. let utdTypeId = utd.getUniformDataTypeByMIMEType('image/jpeg', utd.UniformDataType.IMAGE);
  8. if (utdTypeId) {
  9. // 构造ShareData，需配置一条有效数据信息
  10. let shareData: systemShare.SharedData = new systemShare.SharedData({
  11. utd: utdTypeId,
  12. uri: 'file://.../xxx.jpg'
  13. });
  14. // 构建ShareController
  15. let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
  16. // 获取UIAbility上下文对象
  17. let uiContext: UIContext = this.getUIContext();
  18. let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
  19. // 进行分享面板显示
  20. controller.show(context, {
  21. previewMode: systemShare.SharePreviewMode.DEFAULT,
  22. selectionMode: systemShare.SelectionMode.SINGLE
  23. });
  24. }
  25. } catch (e) {
  26. let error: BusinessError = e as BusinessError;
  27. console.error(`Failed to getUniformDataTypeByMIMEType. Code: ${error.code}, message: ${error.message} `);
  28. }
  ```
