---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-loadproduct
title: 展示应用详情页面
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场推荐 > 展示应用详情页面
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:03+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:3e00d834efb0427314122cd830e9846f8cdc1879fddaf23470917dc5ffe68d98
---

## 场景介绍

通过应用内调用[loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)接口或者在网页嵌入跳转链接的方式，用户可直接进入应用详情页，简化应用下载流程，增加应用的下载量和用户活跃度。

**说明** 

应用内打开应用市场App，通过应用市场下载推荐应用，推荐使用loadProduct方式；Web页面打开应用市场App，推荐使用[App Linking](appgallery-productview-loadproduct.md#app-linking方式)链接方式。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/N4QC061sTDiOBFfLoOHRSQ/zh-cn_image_0000002712245034.png)

1. 用户使用打开应用详情页功能。
2. 应用调用AppGallery Kit的[loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)接口。
3. AppGallery Kit API获取应用传入的信息，生成展示页面。
4. 展示生成的页面给用户使用。

## 约束与限制

* 应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/store-productviewmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), want: [Want](../harmonyos-references/js-apis-app-ability-want.md), callback?: [ProductViewCallback](../harmonyos-references/store-productviewmanager.md#productviewcallback)): void | 加载应用详情页面接口。 |

## 开发步骤

### loadProduct接口调用

1. 导入productViewManager模块及相关公共模块。

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { productViewManager } from '@kit.AppGalleryKit';
   ```
2. 构造应用详情页参数。

   ```typescript
   const TAG: string = 'LoadProduct';

   @Entry
   @Component
   struct LoadProductView {
       build() {
           Column() {
               Button($r('app.string.load_product'))
                   .id('load_product')
                   .onClick(() => {
                       try {
                           const exposureData: productViewManager.SKExposure = {
                               adTechId: '20****e8',
                               campaignId: '123456',
                               destinationId: '10******',
                               mmpIds: ['2f****5', '2f7***5'],
                               serviceTag: '123***2',
                               nonce: '123***2',
                               timestamp: 1705536488,
                               signature: 'MEQCIEQlmZ****zKBSE8QnhLTIHZZZ****ZpRqRxHss65Ko****JgJKjdrWdkL****juEx2RmFS7da****ZRVZ8RyMyUXg=='
                           };
                           const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext
                           const wantParam: Want = {
                               parameters: {
                                   // 必填，此处填入要加载的应用包名，例如： bundleName: 'com.huawei.hmsapp.books'
                                   bundleName: 'com.huawei.hmsapp.appgallery',
                                   // 可选，向应用归因服务传递登记归因来源数据
                                   skExposure: exposureData
                               }
                           };
                           const callback: productViewManager.ProductViewCallback = {
                               onError: (error: BusinessError) => {
                                 hilog.error(0, 'TAG',
                                   `loadProduct onError.code is ${error.code}, message is ${error.message}`)
                               },
                               // 当应用详情页成功打开时回调
                               onAppear: () => {
                                   hilog.info(0, 'TAG', `loadProduct onAppear.`);
                               },
                               // 当应用详情页关闭时回调
                               onDisappear: () => {
                                   hilog.info(0, 'TAG', `loadProduct onDisappear.`);
                               }
                           }
                           // ...
                       } catch (error) {
                           hilog.error(0, TAG,
                               `loadProduct failed. code is ${(error as BusinessError).code}, message is ${(error as
                                   BusinessError).message}`);
                       }
                   })
                   .width('100%')
                   .margin(16)
               // ...
           }
           .margin(16)
           .height('100%')
           .justifyContent(FlexAlign.Center)
       }
   }
   ```
3. 调用[loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)方法，将步骤2中构造的参数依次传入接口中。

   ```typescript
   // 调用接口，加载元服务加桌页面
   productViewManager.loadProduct(uiContext, wantParam, callback);
   ```

### Deep Linking方式

1. 构造拼接bundleName的Deep Linking链接，其中bundleName为需要打开的应用包名，其格式为：

   ```typescript
   // bundleName为需要打开应用详情的应用包名
   uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName,
   ```
2. 在应用中调用[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-2)方法，拉起应用市场应用详情页：

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   // ...

   @Entry
   @Component
   struct LoadProductView {
       build() {
           Column() {
               // ...
               Button('deepLink')
                   .onClick(() => {
                       const context: common.UIAbilityContext =
                           this.getUIContext().getHostContext() as common.UIAbilityContext;
                       // 按实际需求获取应用的bundleName，例如bundleName: 'com.**.hmsapp.books'
                       const bundleName = 'xxxx';
                       let want: Want = {
                           action: 'ohos.want.action.appdetail', // 隐式指定action为ohos.want.action.appdetail
                           // bundleName为需要打开应用详情的应用包名
                           uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName,
                       };
                       context.startAbility(want).then(() => {
                           hilog.info(0x0001, 'TAG', 'Succeeded in starting Ability successfully.')
                       }).catch((error: BusinessError) => {
                           hilog.error(0x0001, 'TAG',
                               `Failed to startAbility.Code: ${error.code}, message is ${error.message}`);
                       });
                   })
                   .width('100%')
                   .margin(16)
               // ...
           }
           .margin(16)
           .height('100%')
           .justifyContent(FlexAlign.Center)
       }
   }
   ```
3. 在网页中打开Deep Linking链接拉起应用市场应用详情页：

   ```typescript
    <html lang="en">
      <head>
        <meta charset="UTF-8">
      </head>
      <body>
        <div>
          <button type="button" onclick="openDeepLink()">拉起应用详情页</button>
        </div>
      </body>
    </html>
    <script>
      function openDeepLink() {
        window.open('store://appgallery.huawei.com/app/detail?id=com.xxxx.xxxx')
      }
    </script>
   ```

### App Linking方式

1. 构造拼接bundleName的App Linking链接，其中bundleName为需要打开的应用包名，其格式为：

   ```typescript
   // 需要替换成真实的跳转链接
   let link: string = '***://appgallery.huawei.com/app/detail?id=' + bundleName;
   ```
2. 在应用中调用[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口拉起App Linking链接：

   ```typescript
   import { common, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   // ...

   @Entry
   @Component
   struct LoadProductView {
       build() {
           Column() {
               // ...
               Button('appLink')
                   .onClick(() => {
                       let context: common.UIAbilityContext =
                           this.getUIContext().getHostContext() as common.UIAbilityContext;
                       // 需要拼接不同的应用包名，用以打开不同的应用详情页,例如：bundleName: 'com.**.hmsapp.books'
                       let bundleName: string = 'com.**.hmsapp.books';
                       // 需要替换成真实的跳转链接
                       let link: string = '***://appgallery.huawei.com/app/detail?id=' + bundleName;
                       // 以App Linking优先的方式在应用市场打开指定包名的应用详情页
                       context.openLink(link, { appLinkingOnly: false })
                           .then(() => {
                               hilog.info(0x0001, 'TAG', 'openlink success.');
                           })
                           .catch((error: BusinessError) => {
                               hilog.error(0x0001, 'TAG',
                                   `openlink failed. Code: ${error.code}, message is ${error.message}`);
                           });
                   })
                   .width('100%')
                   .margin(16)
           }
           .margin(16)
           .height('100%')
           .justifyContent(FlexAlign.Center)
       }
   }
   ```
3. 在网页中打开App Linking链接：

   ```typescript
     <html lang="en">
       <head>
         <meta charset="UTF-8">
         <title>跳转示例</title>
       </head>
       <body>
         <a href='https://appgallery.huawei.com/app/detail?id=bundleName'>AppLinking跳转示例</a>
       </body>
     </html>
   ```
