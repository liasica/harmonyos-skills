---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-loadservice
title: 添加元服务卡片至桌面
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 添加元服务卡片至桌面
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:23+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:726ecac79349c6f195c5b21d0f91cfe00681029096a0fa05551aadcd9b2873e0
---

## 场景介绍

为了快速访问和管理元服务卡片信息，用户可以将常用的元服务卡片添加到桌面。应用可通过调用应用市场服务提供的[loadService](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadservice)接口来加载元服务卡片加桌页面，用户点击“添加至桌面”按钮，将元服务卡片添加至桌面。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/_f2iJE-iRk-4XJlO4pzgQg/zh-cn_image_0000002706834788.png)

1. 用户使用元服务卡片加桌功能。
2. 应用调用AppGallery Kit的[loadService](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadservice)接口。
3. AppGallery Kit API获取应用传入的信息，生成展示页面。
4. 展示生成的页面给用户，用户点击“添加至桌面”按钮，将元服务卡片添加至桌面。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/store-productviewmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [loadService](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadservice)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), want: [Want](../harmonyos-references/js-apis-app-ability-want.md), callback?: [ServiceViewCallback](../harmonyos-references/store-productviewmanager.md#serviceviewcallback)): void | 加载元服务加桌页面接口。 |

## 开发步骤

1. 导入productViewManager模块及相关公共模块。

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { productViewManager } from '@kit.AppGalleryKit';
   ```
2. 构造元服务卡片参数。

   ```typescript
   const TAG: string = 'LoadService';

   @Entry
   @Component
   struct LoadServiceView {
       context = this.getUIContext().getHostContext() as common.UIAbilityContext;

       build() {
           Column() {
               Button($r('app.string.load_service'))
                   .id('load_service')
                   .onClick(() => {
                       try {
                           const request: Want = {
                             // 此处填入要加载的元服务的加桌链接
                             uri: 'store://******'
                           };

                           const callback: productViewManager.ServiceViewCallback = {
                               // 接收元服务卡片加桌结果信息
                               onReceive: (data: productViewManager.ServiceViewReceiveData) => {
                                   hilog.info(0, TAG,
                                       `loadService onReceive.result is ${data.result}, msg is ${data.msg}, formInfo is ${JSON.stringify(
                                           data.formInfo)}`);
                               },
                               onError: (error: BusinessError) => {
                                   hilog.error(0, TAG,
                                       `loadService onError.code is ${error.code}, message is ${error.message}`)
                               },
                               // 当元服务卡片加桌页成功打开时回调
                               onAppear: () => {
                                   hilog.info(0, TAG, `loadService onAppear.`);
                               },
                               // 当元服务卡片加桌页关闭时回调
                               onDisappear: () => {
                                   hilog.info(0, TAG, `loadService onDisappear.`);
                               }
                           };

                           // ...
                       } catch (error) {
                           hilog.error(0, TAG,
                               `loadService failed.code is ${(error as BusinessError).code}, message is ${(error as
                                   BusinessError).message}`);
                       }
                   })
                   .width('100%')

           }
           .margin(16)
           .height('100%')
           .justifyContent(FlexAlign.Center)
       }
   }
   ```
3. 调用[productViewManager.loadService](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadservice)方法，将步骤2中构造的参数依次传入接口中。

   ```typescript
   // 调用接口，加载元服务加桌页面
   productViewManager.loadService(this.context, request, callback);
   ```
