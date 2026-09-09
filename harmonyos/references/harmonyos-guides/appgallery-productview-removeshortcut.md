---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-removeshortcut
title: 删除应用内快捷方式
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 应用内快捷方式 > 删除应用内快捷方式
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:11+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:f581c4781e59192a57e23ecf774d332d562db62ff3684590535d225fcbff7b99
---

**说明** 

6.1.1(24)版本开始，新增删除桌面快捷方式接口，支持用户删除桌面快捷方式。

## 场景介绍

当应用的桌面快捷方式功能发生变化或者用户希望删除不再使用的桌面快捷方式时，用户可以通过调用[removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)接口删除当前应用的桌面快捷方式。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/as2WpreHS6GLJ8yoVeEcHQ/zh-cn_image_0000002747211515.png)

1. 用户需要删除桌面快捷方式。
2. 应用调用[removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)接口删除快捷方式。
3. AppGallery Kit向应用弹出快捷方式删除确认框。
4. 用户确认是否删除快捷方式。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/store-productviewmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), shortcutId: string): Promise<void> | 删除桌面快捷方式。 |

## 开发准备

### （可选）静默删除桌面快捷方式开放能力申请

当应用已有自己的删除确认弹框并在弹框中提示用户删除桌面快捷方式时，开发者可以申请静默删除权限，实现在不显示系统确认弹框的情况下完成删除操作。

1. 登录AppGallery Connect，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/siv1MJLWQBOwUh1uNmpr0w/zh-cn_image_0000002717611644.png)
2. 在项目列表中找到您的项目，并点击选择需申请静默删除桌面快捷方式能力的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/k2_ojJ3ZTXqPVSOnIZfIjw/zh-cn_image_0000002717771580.png)
3. 在“开放能力管理”页面，点击静默删除桌面快捷方式对应的“申请”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/tneoJ2r0TI6SWUP6mjRJcg/zh-cn_image_0000002717611648.png)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，包括应用介绍、使用场景，不超过256个字符。上传附件：必填，提供应用的使用场景录屏，录屏中需要体现应用自己的弹框以及在弹框中显示提示用户删除桌面快捷方式，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/5MgzwoyPSnmTKtM2s3Ol0A/zh-cn_image_0000002747291599.png)
5. 返回“开放能力管理”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/0_xaKnF6ToWWIlEeb3p9sQ/zh-cn_image_0000002747211517.png)
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
