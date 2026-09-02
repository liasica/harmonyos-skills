---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-getshortcut
title: 查询应用内快捷方式
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 应用内快捷方式 > 查询应用内快捷方式
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:7855d8b93fedb5b6734dd54d3383e92704d36dac550c3d97959e03ae826b15a5
---

**说明** 

6.1.1(24)版本开始，新增查询桌面快捷方式接口，支持用户查询桌面快捷方式。

## 场景介绍

查询应用内快捷方式用于获取当前应用已固定在桌面上的所有快捷方式列表。用户可以在应用内查看已添加到桌面的快捷方式列表，快速找到特定的快捷方式。也可通过定期查看和管理这些快捷方式，确保桌面的整洁和高效。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/7beEMFOaQO-wrgHQz_AvSg/zh-cn_image_0000002706674854.png)

1. 用户需要查询当前应用的快捷方式。
2. 应用调用[getPinShortcutInfos](../harmonyos-references/store-productviewmanager.md#productviewmanagergetpinshortcutinfos)接口获取快捷方式信息。
3. AppGallery Kit返回查询结果信息给应用。
4. 应用将查询结果返回给用户。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/store-productviewmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [getPinShortcutInfos](../harmonyos-references/store-productviewmanager.md#productviewmanagergetpinshortcutinfos)(): Promise<[PinShortcutInfo](../harmonyos-references/store-productviewmanager.md#pinshortcutinfo)[]> | 查询桌面快捷方式列表。 |

## 开发步骤

1. 导入productViewManager模块及相关公共模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { productViewManager } from '@kit.AppGalleryKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[getPinShortcutInfos](../harmonyos-references/store-productviewmanager.md#productviewmanagergetpinshortcutinfos)方法查询当前应用所有桌面快捷方式列表信息。

   ```typescript
   const GET_TAG: string = 'getPinShortcutInfos';
   // ...

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

                   Button('GetPinShortcutInfos')
                       .width('100%')
                       .onClick(() => {
                           try {
                               // 通过getPinShortcutInfos接口获取桌面快捷方式列表信息
                               productViewManager.getPinShortcutInfos()
                                   .then((result: productViewManager.PinShortcutInfo[]) => {
                                       hilog.info(0x0001, GET_TAG, `getPinShortcutInfos success.`);
                                       this.getUIContext().getPromptAction().showToast({
                                           message: `getPinShortcutInfos result: ${JSON.stringify(result)}`,
                                           duration: 2000
                                       });
                                   }).catch((error: BusinessError) => {
                                   hilog.error(0x0001, GET_TAG,
                                       `getPinShortcutInfos error. code is ${error.code}, message is ${error.message}`);
                                   this.getUIContext().getPromptAction().showToast({
                                       message: JSON.stringify(error),
                                       duration: 2000
                                   });
                               })
                           } catch (err) {
                               hilog.error(0x0001, GET_TAG,
                                   `getPinShortcutInfos failed, code is ${err.code}, message is ${err.message}`);
                               this.getUIContext().getPromptAction().showToast({
                                   message: JSON.stringify(err),
                                   duration: 2000
                               });
                           }
                   }).margin({ top: 4 })
                   // ...
               }.padding({ left: 4, right: 4 })
           }
       }
   }
   ```
