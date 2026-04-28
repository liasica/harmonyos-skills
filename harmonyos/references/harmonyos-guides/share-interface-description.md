---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-interface-description
title: 应用内处理分享内容
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 应用内处理分享内容
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a1cd6ee163637f1958b226ff41b26b0c5be36ad4f06f131fce3bd515995c03fc
---

目标应用可以通过[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)构建接收分享内容的界面，并将应用显示到分享面板应用推荐区内，以实现将分享内容传递到目标应用内进行处理。开发时需要接入方实现[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)并于module.json5中注册支持分享内容的能力。

## 接口说明

getSharedData接口用于从want中获取分享数据；getContactInfo接口用于从want中获取联系人信息（仅当用户选择联系人分享时有返回值）。具体API说明详见[接口文档](../harmonyos-references/share-system-share.md#getshareddata)。

**表1** 目标应用解析分享数据接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| [getSharedData](../harmonyos-references/share-system-share.md#getshareddata)(want: [Want](../harmonyos-references/js-apis-inner-ability-want.md)): Promise<[SharedData](../harmonyos-references/share-system-share.md#shareddata)> | 从want中获取分享数据 |
| [getContactInfo](../harmonyos-references/share-system-share.md#getcontactinfo)(want: [Want](../harmonyos-references/js-apis-inner-ability-want.md)): Promise<[ContactInfo](../harmonyos-references/share-system-share.md#contactinfo)> | 从want中获取联系人信息 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { systemShare } from '@kit.ShareKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 目标应用可实现[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)。在Ability被启动后，可以在其[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中获取传入的want参数。将want参数通过[getSharedData](../harmonyos-references/share-system-share.md#getshareddata)解析后得到分享数据。

   ```
   1. export default class TestUIAbility extends UIAbility {
   2. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   3. systemShare.getSharedData(want)
   4. .then((data: systemShare.SharedData) => {
   5. data.getRecords().forEach((record: systemShare.SharedRecord) => {
   6. // 处理分享数据
   7. });
   8. })
   9. .catch((error: BusinessError) => {
   10. console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
   11. this.context.terminateSelf();
   12. });
   13. }
   14. onWindowStageCreate(windowStage: window.WindowStage): void {
   15. // Main window is created, set main page for this ability
   16. windowStage.loadContent('pages/Index', (error) => {
   17. if (error.code) {
   18. console.error(`Failed to load the content. Code: ${error.code}, message: ${error.message}`);
   19. return;
   20. }
   21. console.info('Succeeded in loading the content.');
   22. });
   23. }
   24. }
   ```
3. 构建完UIAbility，需要在应用配置文件（src/main/module.json5）的[skills](module-configuration-file.md#skills标签)配置中注册。配置actions为ohos.want.action.sendData；uris需穷举所有支持的数据类型。

   ```
   1. "abilities": [
   2. {
   3. "name": "TestUIAbility",
   4. "srcEntry": "./ets/entryability/TestUIAbility.ets",
   5. "description": "$string:EntryAbility_desc",
   6. "icon": "$media:layered_image",
   7. "label": "$string:EntryAbility_label",
   8. "startWindowIcon": "$media:startIcon",
   9. "startWindowBackground": "$color:start_window_background",
   10. "exported": true,
   11. "skills": [
   12. {
   13. "actions": [
   14. "ohos.want.action.sendData"
   15. ],
   16. // scheme为预留字段，在此处不生效，配置file仅为示例
   17. // 目标应用在配置支持接收的数据类型时，需穷举支持的UTD，比如：支持全部图片类型，可声明：general.image
   18. // maxFileSupported 对于归属指定类型的文件，标识一次支持接收的最大数量。默认为0，代表不支持此类文件的分享。
   19. // 文件类型归属关系参考：@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)
   20. "uris": [
   21. {
   22. "scheme": "file",
   23. "utd": "general.text",
   24. "maxFileSupported": 1
   25. },
   26. {
   27. "scheme": "file",
   28. "utd": "general.png",
   29. "maxFileSupported": 1
   30. },
   31. {
   32. "scheme": "file",
   33. "utd": "general.jpeg",
   34. "maxFileSupported": 1
   35. }
   36. ]
   37. }
   38. ]
   39. }
   40. ]
   ```
