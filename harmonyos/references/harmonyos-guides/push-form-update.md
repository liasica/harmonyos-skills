---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-form-update
title: 推送卡片刷新消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送卡片刷新消息
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:00+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:8ac89a885205f60092f1240f9e5669c2bd43ff44abbc28b734a6b51b932a3aa1
---

## 场景介绍

如今衣食住行娱乐影音应用占据了大多数人的手机，一部手机可以满足日常大多需求，但对需要经常查看或进行简单操作的应用来说，总需要用户点开应用体验较繁琐。针对此种场景，HarmonyOS提供了[Form Kit（卡片开发服务）](form-kit.md)，您可以将应用的重要信息或操作前置到卡片，以达到服务直达、减少体验层级的目的。

面对需要实时更新信息的应用卡片，Push Kit向开发者提供了卡片刷新服务。应用通过集成Push Kit后获取Push Token，基于Push Kit的系统级通道，便可以在合适场景向用户即时推送卡片内容，从而提升用户的感知度和活跃度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/kb3CZDr1QjGu9nryEgwgLQ/zh-cn_image_0000002706835146.png)

## 约束与限制

推送卡片刷新消息支持Phone、Tablet、PC/2in1设备。并且从6.1.0(23)版本开始，新增支持Wearable、TV设备。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据使用场景和流量进行管控，不合理的使用场景系统会进行频控。

应用每张卡片独占刷新上限限制，单张服务卡片刷新消息数量按[华为应用市场应用分类示例](../app/classify-1.md)划分，具体频控规则请参考[ArkTS卡片Push刷新](arkts-ui-widget-update-by-push.md)。

**说明** 

不论是测试消息还是正式消息，卡片刷新消息单次发送仅能携带一个Token。

## 开发步骤

### 开发卡片

推送卡片刷新消息前，您需先完成本地卡片的开发。

1. 参见[创建一个ArkTS卡片](arkts-ui-widget-creation.md)，完成本地服务卡片的创建。
2. 在项目模块级别下的**src/main/resources/base/profile/form\_config.json**中配置dataProxyEnabled字段为**true**，开启卡片代理刷新功能。

   ```json
   {
     "forms": [
       {
         "name": "widget",
         "src": "./ets/widget/pages/WidgetCard.ets",
         "uiSyntax": "arkts",
         "window": {
           "designWidth": 720,
           "autoDesignWidth": true
         },
         "colorMode": "auto",
         "isDefault": true,
         "updateEnabled": true,
         "updateDuration": 1,
         "scheduledUpdateTime": "10:30",
         "defaultDimension": "2*2",
         "supportDimensions": ["2*2"],
         "dataProxyEnabled": true
       }
     ]
   }
   ```
3. 在卡片生命周期管理文件（下以EntryFormAbility为例）的[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)()回调中获取**formId**，定义需要在卡片页面文件（下以WidgetCard为例）中和通过Push Kit要刷新的字段，如下以**textKey**和**imageKey**为例。

   ```typescript
   import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';
   // ...

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want): formBindingData.FormBindingData {
       // 获取formId
       const formId = want.parameters![formInfo.FormParam.IDENTITY_KEY] as string;
       // ...
       // 定义需要在WidgetCard中刷新的字段
       class CreateFormData {
         public formId: string = '';
         public textKey: string = '';
         public imageKey: string = '';
       }

       const obj: CreateFormData = {
         formId: formId,
         textKey: '默认文本',
         imageKey: ''
       }
       const bindingData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);

       // 定义需要通过Push Kit代理刷新的字段，每个key均需要在上面bindingData中定义
       const textKey: formBindingData.ProxyData = {
         key: 'textKey',
         subscriberId: formId
       };
       const imageKey: formBindingData.ProxyData = {
         key: 'imageKey',
         subscriberId: formId
       };
       bindingData.proxies = [textKey, imageKey];
       return bindingData;
     }

     // ...
   }
   ```
4. 卡片页面文件（**下以src/main/ets/widget/pages/WidgetCard.ets为例**）中，创建[LocalStorage](arkts-localstorage.md)变量并与[@Entry](arkts-create-custom-components.md#entry)装饰器绑定，使用[@LocalStorageProp](arkts-localstorage.md#localstorageprop)装饰器创建key-value的变量。

   本文创建了formId、text和image三个变量，对应的key为**formId**、**textKey**和**imageKey**，需要注意的是卡片页面布局中image对应的组件是Image图片组件，图片组件传递的变量必须以**memory://** 开头。

   ```typescript
   // 定义页面级的UI状态存储LocalStorage
   const storage = new LocalStorage();

   // 绑定
   @Entry(storage)
   @Component
   struct WidgetCard {
     @LocalStorageProp('formId') formId: string = '';
     @LocalStorageProp('textKey') text: string = '';
     @LocalStorageProp('imageKey') image: string = '';

     build() {
       Flex({ direction: FlexDirection.Column }) {
         Row() {
           Text() {
             // Span是Text组件的子组件，用于显示行内文本
             Span('formID:')
             Span(this.formId)
           }
           .fontSize(10)
         }

         Row() {
           Text() {
             Span('文本:')
             Span(this.text)
           }
           .fontSize(10)
         }

         Row() {
           if (this.image) {
             Image('memory://' + this.image).height(80)
           }
         }
       }
       .padding(10)
       .onClick(() => {
         postCardAction(this, {
           action: 'router',
           abilityName: 'MainAbility', // 请配置为应用实际的abilityName
         });
       })
     }
   }
   ```

### 推送卡片刷新消息

1. 参见指导[获取Push Token](push-get-token.md)。
2. （可选）建议您将**formId**、**pushToken**等信息上报到应用服务端，用于向应用发送卡片刷新消息。

   ```typescript
   // 以下为伪代码
   import { Want } from '@kit.AbilityKit';
   import { pushService } from '@kit.PushKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { formInfo } from '@kit.FormKit';

   const DOMAIN = 0x0000;

   async function saveFormInfo(want: Want): Promise<void> {
     try {
       const formId = want.parameters![formInfo.FormParam.IDENTITY_KEY] as string;
       const moduleName = want.moduleName;
       const abilityName = want.abilityName;
       const formName = want.parameters![formInfo.FormParam.NAME_KEY] as string;
       const pushToken: string = await pushService.getToken();

       // 将formId, moduleName, abilityName, formName, pushToken 上报到应用服务端
     } catch (err) {
       let e: BusinessError = err as BusinessError;
       hilog.error(DOMAIN, 'testTag', 'Failed to save form info: %{public}d %{public}s', e.code, e.message);
     }
   }
   ```
3. 应用服务端调用REST API推送卡片刷新消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)，请求示例如下：

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 1

   // Request Body
   {
       "payload": {
       "moduleName": "entry",
       "abilityName": "EntryFormAbility",
       "formName": "widget",
       "formId": 423434262,
       "version": 123456,
       "formData": {
         "textKey": "刷新文本内容"
       },
       "images": [
         {
           "keyName": "imageKey",
           "url": "https://***.png",
           "require": 1
         }
       ]
     },
     "target": {
       "token": [
         "MAMzLg**********lPW"
       ]
     },
     "pushOptions": {
        "testMessage": true
     }
   }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：1表示服务卡片刷新场景。
   * moduleName：项目模块级别下的 **src/main/module.json5** 中的 **module **标签下的**name**值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/DTEMFr3gTIaEz-xSdLapZA/zh-cn_image_0000002736314253.png)
   * abilityName：项目模块级别下的**src/main/module.json5**中的**extensionAbilities**标签下的服务卡片的ability名称。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/sa6bo2RlSWespLJ3g1hvTg/zh-cn_image_0000002706675210.png)
   * formName：项目模块级别下的**src/main/resources/base/profile/form\_config.json**中**forms**标签下服务卡片的名称。下图以卡片配置文件form\_config为例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CXy1x6d0Sre4kWOVzyPneA/zh-cn_image_0000002736434299.png)
   * version：当前卡片刷新消息的版本号，新的卡片刷新消息的版本号需**大于**当前卡片刷新消息版本号，否则会刷新失败。详情参见[version](../harmonyos-references/push-scenariozed-api-request-param.md#formupdatepayload-卡片刷新消息)。
   * formId：服务卡片的实例ID，当卡片的[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)()方法被调用时（卡片使用方添加卡片至桌面）进行获取。最大值为**231-1**。
   * formData：填写待刷新服务卡片的业务数据，该数据来源于项目模块级别下的**src/main/ets/widget/pages/WidgetCard.ets**文件下的声明式范式组件名称。下图以卡片页面文件WidgetCard为例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ZczjgmtUTFm2k0-DYOoRLQ/zh-cn_image_0000002706835148.png)
   * images：待刷新服务卡片业务数据中的图片数据，其中keyName为您服务卡片中图片控件的key值，url为图片的地址，下图以卡片页面文件**WidgetCard**为例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/UUlV6cbJTomv33L7jrZxQg/zh-cn_image_0000002736314255.png)

     **说明** 

     Push Kit禁止推送包含敏感信息的图片。

     支持图片的格式为PNG、JPG、JPEG、WEBP，图片文件最大为512KB，若超过则图片不展示。
   * require：图片刷新策略控制，0表示如果图片下载失败，仅刷新文字；1表示如果图片下载失败，则不进行刷新操作。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送仅能发送一个Token。详情请参见[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
