---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-open-formmanager
title: 应用内拉起卡片管理加桌
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > 应用内请求卡片加桌 > 应用内拉起卡片管理加桌
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ffde48e93e3deda4e067ddf0b7e83077e8e9ec792bd187c67bd7eaddf3401648
---

从API version 18开始，Form Kit提供在应用内将ArkTS卡片添加到桌面的能力，以方便用户后续便捷查看信息或快速进入应用。

## 开发步骤

下面给出示例，实现如下功能：在应用内点击“添加卡片到桌面”按钮，拉起卡片管理页面。用户可在卡片管理页面，点击“添加至桌面”按钮，此时在桌面即可看到新添加的卡片。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 通过[openFormManager](../harmonyos-references/js-apis-app-form-formprovider.md#formprovideropenformmanager18)方法在应用内添加拉起卡片管理页面入口。

   ```
   1. // entry/src/main/ets/pages/Index.ets
   2. import { formProvider } from '@kit.FormKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { Want } from '@kit.AbilityKit';
   5. import { promptAction } from '@kit.ArkUI';
   6. import { hilog } from '@kit.PerformanceAnalysisKit';

   8. const DOMAIN = 0x0000;

   10. @Entry
   11. @Component
   12. struct Index {
   13. build() {
   14. Row() {
   15. Column() {
   16. // 添加拉起卡片管理页面按钮
   17. Button($r('app.string.open_form_manager_button'))
   18. .onClick(() => {
   19. const want: Want = {
   20. bundleName: "com.samples.formmanagerdemo",
   21. abilityName: 'EntryFormAbility',
   22. parameters: {
   23. 'ohos.extra.param.key.form_dimension': 2,
   24. 'ohos.extra.param.key.form_name': 'widget',
   25. 'ohos.extra.param.key.module_name': 'entry'
   26. },
   27. };
   28. try {
   29. // 点击按钮后调用openFormManager方法，拉起卡片管理页面
   30. formProvider.openFormManager(want);
   31. } catch (error) {
   32. promptAction.openToast({ message: (error as BusinessError).message });
   33. hilog.info(DOMAIN, 'testTag', 'catch error ', 'code:', (error as BusinessError).code, 'message:',
   34. (error as BusinessError).message);
   35. }
   36. })
   37. .margin({ top: 10, bottom: 10 })
   38. }
   39. .width('100%')
   40. }
   41. .height('100%')
   42. }
   43. }
   ```

   资源文件如下：

   ```
   1. // entry/src/main/resources/base/element/string.json
   2. {
   3. "string": [
   4. {
   5. "name": "open_form_manager_button",
   6. "value": "添加应用卡片到桌面"
   7. }
   8. ]
   9. }
   ```
3. 用户可在卡片管理页面，点击“添加至桌面”或者“添加至负一屏”，此时在桌面或者负一屏即可看到新添加的卡片。结果示例如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ijZhEjHZQkmTTV2_Cjj4wg/zh-cn_image_0000002552958300.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234130Z&HW-CC-Expire=86400&HW-CC-Sign=DDE62663BEAE72CB1EEE09F24F8FCE75F1E77442B1AAE98AD34BC2B7639BE151)
