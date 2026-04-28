---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-transparent-backplate-form-development
title: 背板透明卡片开发指导
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS背板透明卡片 > 背板透明卡片开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4fb59c4078681c4209fa67a785eb35862f7bddc9a4b41af6916e10eeb6bcd0e4
---

从API version 22开始，Form Kit提供卡片背板元素透明显示的能力，满足更丰富的UI设计以及美观诉求。

说明

示例效果请以真机运行为准，当前不支持DevEco Studio预览器。

## 约束和限制

1. 非透明区域要求大于等于10%，不能有大面积全透明，让用户误以为此区域没有卡片的UI设计和实现。
2. 为保障卡片内容和文字清晰可见，建议根据加卡时系统告知的推荐颜色值来显示文字。

## 开发准备

### 透明卡片开放能力申请

因为背板透明卡片仅使用于符合UI规范以及声明使用的场景，不允许对用户隐藏卡片显示或者功能按钮的恶意设计，所以需要开发者申请上架开放能力。

1. 登录AppGallery Connect，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/mFBH1d6RR0qJvXJVcJ2ITA/zh-cn_image_0000002583438349.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=1BE7963DC22A8DBD66CFE8D31E31EFDBF81E2F6999188E7DBE03CD4CE037E722)
2. 在项目列表中找到您的项目，并点击选择需开启开放能力的应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/5hajCnpfRV-rvYmnhAagiA/zh-cn_image_0000002552958304.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=73BFAA5443C74242F7AB49C9C6E1C7CFB2A2714176BCC288D27C0E70EFCD59E6)
3. 在“开放能力管理”页面，点击背板透明卡片对应的申请按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/t8_7Z3HORnCT2Ys-E-h-8g/zh-cn_image_0000002583478305.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=DD7007A0ECFCCC390D4E587CEEA26267040438FF80877B8E1DEEE6DD786589A4)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，包括应用介绍、使用场景、申请用途，不超过256个字符。上传附件：必填，提供对应卡片UI设计释义材料，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/njMmVkIjSe2RSG7Do1WQmA/zh-cn_image_0000002552798656.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=E9B801416587F8EE241EE9E34657A37A592F3A94B2BCA76FF6852BF39616E68B)
5. 返回“开放能力管理”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/1lTs6TAoSQu-DPH3nP1kpQ/zh-cn_image_0000002583438351.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=56C4CE18C076488C7377ED5317690A739E0B7B1FE48D2383B605DE3F287F678D)
6. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ghNL0GTYTTqOy5aAW68UrA/zh-cn_image_0000002552958306.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=3F6594BFF45F171D7980C67F9158C3D8678B1E883B9D28DA2C8346D4C948F332)
7. 能力申请通过后，勾选背板透明卡片的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/JEHsRkDCQ8STooo5ho4Wiw/zh-cn_image_0000002583478307.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=34A579B11A658E7ABF528C574A0A29D32613899362BF5712DFEC0330AAA0E979)

## 开发步骤

下面给出示例，实现背板透明卡片功能。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 配置背板透明卡片。

   在form\_config.json配置文件中，背板透明卡片必须配置transparencyEnabled字段为true。具体参考[配置文件字段说明](arkts-ui-widget-configuration.md#配置文件字段说明)。

   ```
   1. // entry/src/main/resources/base/profile/form_config.json

   3. {
   4. "forms": [
   5. {
   6. "name": "widget",
   7. "displayName": "$string:widget_display_name",
   8. "description": "$string:widget_desc",
   9. "src": "./ets/widget/pages/WidgetCard.ets",
   10. "uiSyntax": "arkts",
   11. "window": {
   12. "designWidth": 720,
   13. "autoDesignWidth": true
   14. },
   15. "isDynamic": true,
   16. "isDefault": true,
   17. "updateEnabled": false,
   18. "scheduledUpdateTime": "10:30",
   19. "updateDuration": 1,
   20. "defaultDimension": "2*2",
   21. "transparencyEnabled": true,
   22. "supportDimensions": [
   23. "2*2"
   24. ]
   25. }
   26. ]
   27. }
   ```
3. 设置背板透明卡片字体反色。

   在WidgetCard.ets卡片布局文件中，实现默认卡片反色字体颜色设置。

   ```
   1. // entry/src/main/ets/widget/pages/WidgetCard.ets
   2. const TAG: string = 'WidgetCard';

   4. @Entry
   5. @Component
   6. export struct WidgetCard {
   7. readonly title: string = '已配置form_config为true三方透明卡片';
   8. readonly actionType: string = 'router';
   9. readonly abilityName: string = 'EntryAbility';
   10. readonly message: string = 'add detail';
   11. readonly fullWidthPercent: string = '100%';
   12. readonly fullHeightPercent: string = '100%';

   14. // 获取反色信息
   15. @LocalStorageProp('textColor') @Watch('getTextColor') textColor: string = '#00ff00';

   17. build() {
   18. Row() {
   19. Column() {
   20. Text(this.title)
   21. .fontSize('20vp')
   22. .fontWeight(FontWeight.Medium)
   23. .fontColor(this.textColor)
   24. }
   25. .width(this.fullWidthPercent)
   26. }
   27. .height(this.fullHeightPercent)
   28. .backgroundColor(Color.Transparent)
   29. .onClick(() => {
   30. postCardAction(this, {
   31. action: this.actionType,
   32. abilityName: this.abilityName,
   33. params: {
   34. message: this.message
   35. }
   36. });
   37. })
   38. }

   40. private getTextColor(): void {
   41. console.info(TAG, `this.textColor = ${this.textColor}`);
   42. }
   43. }
   ```

   在卡片Ability生命周期EntryFormAbility.ets文件中，实现反色字体颜色更新。

   ```
   1. // entry/src/main/ets/entryformability/EntryFormAbility.ets
   2. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   3. import { Want } from '@kit.AbilityKit';

   5. const TAG: string = 'ServiceEntryFormAbility';

   7. export default class EntryFormAbility extends FormExtensionAbility {
   8. onAddForm(want: Want) {
   9. console.info(TAG, 'onAddForm', JSON.stringify(want));
   10. let textColor: string = '#707070';
   11. let formData: Record<string, string> = {};
   12. if (want && want.parameters) {
   13. // 获取反色信息
   14. let testColorJsonStr = want.parameters[formInfo.FormParam.HOST_BG_INVERSE_COLOR_KEY] as TextColor;
   15. if (!testColorJsonStr) {
   16. console.error(TAG, `no host_bg_inverse_color in want parameters`);
   17. } else {
   18. textColor = testColorJsonStr.mTextColor;
   19. formData['textColor'] = textColor;
   20. }
   21. }

   23. return formBindingData.createFormBindingData(formData);
   24. }

   26. onCastToNormalForm(formId: string) {}

   28. onUpdateForm(formId: string, wantParams?: Record<string, Object>) {
   29. console.info(TAG, 'onUpdateForm', JSON.stringify(wantParams));
   30. let textColor: string = '#707070';
   31. if (wantParams) {
   32. let testColorJsonStr = wantParams[formInfo.FormParam.HOST_BG_INVERSE_COLOR_KEY] as TextColor;
   33. console.info(TAG, `onUpdate typeof testColorJsonStr = ${JSON.stringify(testColorJsonStr)}`);
   34. // 获取反色信息
   35. if (!testColorJsonStr) {
   36. console.error(TAG, `no host_bg_inverse_color in wantParams parameters`);
   37. return;
   38. } else {
   39. textColor = testColorJsonStr.mTextColor;
   40. }
   41. }

   43. let formMsg: Record<string, string> = {
   44. 'textColor': textColor
   45. };

   47. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(formMsg);
   48. formProvider.updateForm(formId, formData).then((succ) => {
   49. console.info(TAG,`succ = ${JSON.stringify(succ)}`);
   50. }).catch((fail :Error) => {
   51. console.info(TAG,`err = ${JSON.stringify(fail)}`);
   52. })

   54. }

   56. onFormEvent(formId: string, message: string) {}

   58. onRemoveForm(formId: string) {}

   60. onAcquireFormState(want: Want) {
   61. return formInfo.FormState.READY;
   62. }
   63. }

   65. interface  TextColor {
   66. mTextColor: string;
   67. mWallpaperType: number;
   68. }
   ```
4. 在应用调试或发布时，进行[手动签名](ide-signing.md#section297715173233)后运行。
5. 用户可在卡片中心-卡片管理页面，点击“添加至桌面”，此时在桌面即可看到新添加的背板透明卡片。结果示例如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/RPboBBD3R6SLVZZj515OiA/zh-cn_image_0000002552798658.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=314B34A9B64E2DE245F0BCEBFC5DF0F96DA379312D161EC3E33ED774C28F27C3)
