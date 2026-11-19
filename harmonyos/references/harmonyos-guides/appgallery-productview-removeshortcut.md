---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-removeshortcut
title: 删除应用内快捷方式
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 应用内快捷方式 > 删除应用内快捷方式
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:52+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:780ac9bdd054efefbf843305c716dd98fa4909aee12eebde36a324d4676144db
---

**说明** 

6.1.1(24)版本开始，新增删除桌面快捷方式接口，支持用户删除桌面快捷方式。

## 场景介绍

当应用的桌面快捷方式功能发生变化或者用户希望删除不再使用的桌面快捷方式时，用户可以通过调用[removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)接口删除当前应用的桌面快捷方式。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Gl6-3ctbSiqlqJy_pnAr7Q/zh-cn_image_0000002820526181.png?HW-CC-KV=V1&HW-CC-Date=20261119T014758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D57E3FBAE9BC1B90BAC2140E1E53B4C9730D173C68C86BB0A83A4A0E6265A617)

1. 用户需要删除桌面快捷方式。
2. 应用调用[removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)接口删除快捷方式。
3. AppGallery Kit向应用弹出快捷方式删除确认框。
4. 用户确认是否删除快捷方式。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。从6.0.2(22)版本开始，新增支持TV设备；并且从API版本26.0.1开始，新增支持Car设备。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/store-productviewmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), shortcutId: string): Promise<void> | 删除桌面快捷方式。 |

## 开发准备

### （可选）静默删除桌面快捷方式开放能力申请

当应用已有自己的删除确认弹框并在弹框中提示用户删除桌面快捷方式时，开发者可以申请静默删除权限，实现在不显示系统确认弹框的情况下完成删除操作。

1. 登录AppGallery Connect，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/_icBO4eASsemFVvzJySpLw/zh-cn_image_0000002791726198.png?HW-CC-KV=V1&HW-CC-Date=20261119T014758Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDB1CFB190BA7779BBCDFEDB62A79231040AAAB7F26D4A125F516C416A6227C8)
2. 在项目列表中找到您的项目，并点击选择需申请静默删除桌面快捷方式能力的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/rr7vrqaUT32y4BHasDJCqw/zh-cn_image_0000002820406181.png?HW-CC-KV=V1&HW-CC-Date=20261119T014758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1910F8A4780644C6BB4DD2AD6C17E4EA87C66ACAC5DF32EE84F38A586EDA60CA)
3. 在“开放能力管理”页面，点击静默删除桌面快捷方式对应的“申请”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Mm-LeQ95QxCvVsxajo24rA/zh-cn_image_0000002791726202.png?HW-CC-KV=V1&HW-CC-Date=20261119T014758Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7B74FAB17ACE811BFB881A3C3C52A4693C9428FEE899BA4BDC1EF1C4C8962C3)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，包括应用介绍、使用场景，不超过256个字符。上传附件：必填，提供应用的使用场景录屏，录屏中需要体现应用自己的弹框以及在弹框中显示提示用户删除桌面快捷方式，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/99VN7HqeQLumm0_Slb1csQ/zh-cn_image_0000002791566230.png?HW-CC-KV=V1&HW-CC-Date=20261119T014758Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEC06DD337EDF293F56F83852A0C358F1EFE8A3486C3CB68C174DC5411912CC8)
5. 返回“开放能力管理”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_UOzT55PRzWxN_leUYYaog/zh-cn_image_0000002820526183.png?HW-CC-KV=V1&HW-CC-Date=20261119T014758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D507AD097FF546D40992B641CF316E240B9EA82D8FE30B8244343804B56BEB6F)
6. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。
7. 能力申请通过后，勾选删除桌面快捷方式的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。

## 开发步骤

1. 导入productViewManager模块及相关公共模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { productViewManager } from '@kit.AppGalleryKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)方法删除桌面快捷方式。

   ```typescript
   const REMOVE_TAG: string = 'removePinShortcut';

   @Entry
   @Component
   @Preview
   struct Index {
       scroller: Scroller = new Scroller();
       tid: string = '';

       build() {
           Scroll(this.scroller) {
               Column() {
                   // ...
                   Button('removePinShortcut')
                       .width('100%')
                       .onClick(() => {
                           try {
                               const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
                               const shortcutId = 'xxx'; // 通过checkPinShortcutPermitted接口获取
                               productViewManager.removePinShortcut(uiContext, shortcutId)
                                   .then(() => {
                                       hilog.info(0x0001, REMOVE_TAG, `removePinShortcut success.`);
                                   }).catch((error: BusinessError) => {
                                   hilog.error(0x0001, REMOVE_TAG,
                                       `removePinShortcut error. code is ${error.code}, message is ${error.message}`);
                                   // ...
                               })
                           } catch (err) {
                               hilog.error(0x0001, REMOVE_TAG,
                                   `removePinShortcut failed, code is ${err.code}, message is ${err.message}`);
                               // ...
                           }
                       }).margin({ top: 4 })
               }.padding({ left: 4, right: 4 })
           }
       }
   }
   ```
