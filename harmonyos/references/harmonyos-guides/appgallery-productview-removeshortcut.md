---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-removeshortcut
title: 删除应用内快捷方式
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 应用内快捷方式 > 删除应用内快捷方式
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:18+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:25fff0001a741cdb90c492b4f8604b85cdfde1f9051921b4ff42c73a4b633525
---

**说明** 

6.1.1(24)版本开始，新增删除桌面快捷方式接口，支持用户删除桌面快捷方式。

## 场景介绍

当应用的桌面快捷方式功能发生变化或者用户希望删除不再使用的桌面快捷方式时，用户可以通过调用[removePinShortcut](../harmonyos-references/store-productviewmanager.md#productviewmanagerremovepinshortcut)接口删除当前应用的桌面快捷方式。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/WRGS_MbnSGGgrhk5F_yA0w/zh-cn_image_0000002793037852.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFAE0E36E1C56A5301D4CF7599FFF89EF5F94E1E340EAC5F44E2F7A1DFB50A99)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/eD67fK8aRRudTvMugHPEtw/zh-cn_image_0000002821837785.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D32D0DAC21B6D55439EDA70D47EE1CCC2FF3E927F872A8FA4328A68FC975395)
2. 在项目列表中找到您的项目，并点击选择需申请静默删除桌面快捷方式能力的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/pWQqK4UpTyaLgtpJqEOySQ/zh-cn_image_0000002792877882.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=F595494E42231C40188AD7710222F1994FE6415A4ED63FF51F212784857C08B3)
3. 在“开放能力管理”页面，点击静默删除桌面快捷方式对应的“申请”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/DR9_PRTUQEGfvX1zp20Cxg/zh-cn_image_0000002821837789.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=45AACDFBE57493E693CAC424528D3530155B385E8B23F48B02C3FA30831DABE4)
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，包括应用介绍、使用场景，不超过256个字符。上传附件：必填，提供应用的使用场景录屏，录屏中需要体现应用自己的弹框以及在弹框中显示提示用户删除桌面快捷方式，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/fw-C1tfpQlqIQtPcme8zMA/zh-cn_image_0000002821757791.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=95B9A8833E0CADD4BCCFFC87C7CE498465925BB0F5A78FAFA3BBA1825D88CB2B)
5. 返回“开放能力管理”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/f0yHuLQOQBiMGI9DYnu7Tw/zh-cn_image_0000002793037854.png?HW-CC-KV=V1&HW-CC-Date=20261121T011051Z&HW-CC-Expire=31536000000&HW-CC-Sign=06EC85B26A49485DCBE74CB65DE06C5E962868A0600A226525F42CCD6D2D2D1E)
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
