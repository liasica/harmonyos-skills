---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-transparent-backplate-form-development
title: ArkTS背板透明卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS背板透明卡片
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:da4d654bca84a2d4f8bc2164f107f67d15226777e3b9e07510047929ea15d768
---

从API version 22开始，Form Kit提供卡片背板元素透明显示的能力，满足更丰富的UI设计以及美观诉求。

**说明** 

示例效果请以真机运行为准，当前不支持DevEco Studio预览器。

## 约束和限制

1. 非透明区域要求大于等于10%，不能有大面积全透明，让用户误以为此区域没有卡片的UI设计和实现。
2. 为保障卡片内容和文字清晰可见，建议根据加卡时系统告知的推荐颜色值来显示文字。

## 开发准备

### 透明卡片开放能力申请

因为背板透明卡片仅使用于符合UI规范以及声明使用的场景，不允许对用户隐藏卡片显示或者功能按钮的恶意设计，所以需要开发者申请上架开放能力。

因此在应用调试或发布时，必须使用[手动签名](ide-signing-manual.md)，并在手动签名[申请Profile](../app/agc-help-debug-profile-0000002248181278.md)过程中[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)，创建应用时参考如下指导为应用接入开放能力。

1. 登录AppGallery Connect，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/PJaOP6y-QrK3_YS_RopVpw/zh-cn_image_0000002791565598.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=A82E9ACA62CE5BA57993C03490BEA140679E9075371E2C2DB890301511A64E98)
2. 在项目列表中找到您的项目，并点击选择需开启开放能力的应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/28BlWXJwSXuAbRpx8Xo_Xw/zh-cn_image_0000002820525551.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B4642511B90C0F142A9F4567E418AC0A81DA9696DFBBD0DEAC8D78EBFDECAD1)
3. 在“开放能力管理”页面，点击背板透明卡片对应的申请按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/22WnQefUT7ueOKzth30S_w/zh-cn_image_0000002820405551.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=95DB74D5D2556FEB296A9B361DE43366FF00B8A0360409FEF677497716B84244)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，包括应用介绍、使用场景、申请用途，不超过256个字符。上传附件：必填，提供对应卡片UI设计释义材料，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/FUj5u3G0TBSymr1neZVf4g/zh-cn_image_0000002791725572.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CDCF696B4EADD8303DDE694C5331D5ECB20B17918CFCBA087CB39441DFA8D16)
5. 返回“开放能力管理”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/sc05ALeDQAW5Kd899rwpRg/zh-cn_image_0000002791565600.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=FACA36D17DE5B2C552441F4E06B53DF0C33FABA064A6656E59665FD2AD99232E)
6. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/-Jz8ZKAhSVGaDyfiMshrLA/zh-cn_image_0000002820525553.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BE0F5681D61BEAB70D4CE1053B893257184D3A29E01DE686E0CA992F0DC4F13)
7. 能力申请通过后，勾选背板透明卡片的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/4nFS9cgpQA6E0C4qaJlGAA/zh-cn_image_0000002820405553.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EA45DE55696D7627EF7FBD0AD37A1329F2D8E16C1B976196407D2072185A054)

## 开发步骤

下面给出示例，实现背板透明卡片功能。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 配置背板透明卡片。

   在form\_config.json配置文件中，背板透明卡片必须配置transparencyEnabled字段为true。具体参考[配置文件字段说明](arkts-ui-widget-configuration.md#配置文件字段说明)。

   ```json5
   // entry/src/main/resources/base/profile/form_config.json

   {
     "forms": [
       {
           "name": "widget",
           "displayName": "$string:widget_display_name",
           "description": "$string:widget_desc",
           "src": "./ets/widget/pages/WidgetCard.ets",
           "uiSyntax": "arkts",
           "window": {
               "designWidth": 720,
               "autoDesignWidth": true
           },
           "isDynamic": true,
           "isDefault": true,
           "updateEnabled": false,
           "scheduledUpdateTime": "10:30",
           "updateDuration": 1,
           "defaultDimension": "2*2",
           "transparencyEnabled": true,
           "supportDimensions": [
               "2*2"
           ]
       }
     ]
   }
   ```
3. 设置背板透明卡片字体反色。

   在WidgetCard.ets卡片布局文件中，实现默认卡片反色字体颜色设置。

   ```ets
   // entry/src/main/ets/widget/pages/WidgetCard.ets
   const TAG: string = 'WidgetCard';

   @Entry
   @Component
   export struct WidgetCard {
     readonly title: string = '已配置form_config为true三方透明卡片';
     readonly actionType: string = 'router';
     readonly abilityName: string = 'EntryAbility';
     readonly message: string = 'add detail';
     readonly fullWidthPercent: string = '100%';
     readonly fullHeightPercent: string = '100%';

     // 获取反色信息
     @LocalStorageProp('textColor') @Watch('getTextColor') textColor: string = '#00ff00';

     build() {
       Row() {
         Column() {
           Text(this.title)
             .fontSize('20vp')
             .fontWeight(FontWeight.Medium)
             .fontColor(this.textColor)
         }
         .width(this.fullWidthPercent)
       }
       .height(this.fullHeightPercent)
       .backgroundColor(Color.Transparent)
       .onClick(() => {
         postCardAction(this, {
           action: this.actionType,
           abilityName: this.abilityName,
           params: {
             message: this.message
           }
         });
       })
     }

     private getTextColor(): void {
       console.info(TAG, `this.textColor = ${this.textColor}`);
     }
   }
   ```

   在卡片Ability生命周期EntryFormAbility.ets文件中，实现反色字体颜色更新。

   ```ets
   // entry/src/main/ets/entryformability/EntryFormAbility.ets
   import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';

   const TAG: string = 'ServiceEntryFormAbility';

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       console.info(TAG, 'onAddForm', JSON.stringify(want));
       let textColor: string = '#707070';
       let formData: Record<string, string> = {};
       if (want && want.parameters) {
         // 获取反色信息
         let testColorJsonStr = want.parameters[formInfo.FormParam.HOST_BG_INVERSE_COLOR_KEY] as TextColor;
         if (!testColorJsonStr) {
           console.error(TAG, `no host_bg_inverse_color in want parameters`);
         } else {
           textColor = testColorJsonStr.mTextColor;
           formData['textColor'] = textColor;
         }
       }

       return formBindingData.createFormBindingData(formData);
     }

     onCastToNormalForm(formId: string) {}

     onUpdateForm(formId: string, wantParams?: Record<string, Object>) {
       console.info(TAG, 'onUpdateForm', JSON.stringify(wantParams));
       let textColor: string = '#707070';
       if (wantParams) {
         let testColorJsonStr = wantParams[formInfo.FormParam.HOST_BG_INVERSE_COLOR_KEY] as TextColor;
         console.info(TAG, `onUpdate typeof testColorJsonStr = ${JSON.stringify(testColorJsonStr)}`);
         // 获取反色信息
         if (!testColorJsonStr) {
           console.error(TAG, `no host_bg_inverse_color in wantParams parameters`);
           return;
         } else {
           textColor = testColorJsonStr.mTextColor;
         }
       }

       let formMsg: Record<string, string> = {
         'textColor': textColor
       };

       let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(formMsg);
       formProvider.updateForm(formId, formData).then((succ) => {
         console.info(TAG,`succ = ${JSON.stringify(succ)}`);
       }).catch((fail :Error) => {
         console.info(TAG,`err = ${JSON.stringify(fail)}`);
       })

     }

     onFormEvent(formId: string, message: string) {}

     onRemoveForm(formId: string) {}

     onAcquireFormState(want: Want) {
       return formInfo.FormState.READY;
     }
   }

   interface  TextColor {
     mTextColor: string;
     mWallpaperType: number;
   }
   ```
4. 在应用调试或发布时，进行[手动签名](ide-signing-manual.md)后运行。
5. 用户可在卡片中心-卡片管理页面，点击“添加至桌面”，此时在桌面即可看到新添加的背板透明卡片。结果示例如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/2TQNSCFWSLO1RhI5q3u9Jg/zh-cn_image_0000002791725574.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=3565D772A85E453035E592145D8A8CDC8F17B24E7AA9DD66F056DC4E9F6D3866)
