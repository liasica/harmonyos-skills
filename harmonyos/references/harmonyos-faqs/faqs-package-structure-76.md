---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-76
title: 跨HAP包页面跳转方案
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 跨HAP包页面跳转方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0a62c25a81d95eb0c5bd31a1c015b5bce7518e9bfb52568821b916a6707b78fc
---

## 问题现象

在多HAP场景中，开发者需要实现跨HAP模块的页面跳转。Navigation路由操作不支持从一个HAP跳转到另一个HAP的页面，会抛出跳转失败的错误。

## 背景知识

[多HAP场景](../harmonyos-guides/hap-package.md#开发)是指在HarmonyOS中使用多个应用包（一个entry包和多个feature包）来实现复杂应用的开发方式。这种开发模式允许将复杂应用拆分成多个模块，每个模块可以独立开发、测试和更新，提高了开发效率和维护性。

区别于[HAR](../harmonyos-guides/har-package.md)和[HSP](../harmonyos-guides/in-app-hsp.md)，每个HAP模块具有各自的UIAbility组件。多HAP应用运行时，同一进程中的UIAbility组件被启动时，才加载对应HAP的资源和代码。[Router](../harmonyos-references/js-apis-router.md)和[Navigation](../harmonyos-references/ts-basic-components-navigation.md)可以实现HAP至HAR/HSP页面的跳转，无法跳转其它HAP页面。可以通过UIAbility中的[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法拉起其它HAP包中的页面。

## 解决方案

1. 在项目中创建targetHap：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/3zXsLf2NQ3W1Qc0APqA8hQ/zh-cn_image_0000002628628222.png "点击放大")
2. 在entry模块中使用startAbility拉起targetHap模块的实例，需要配置bundleName和Ability名称，并在被拉起的HAP中配置期望打开的页面即可。发起侧示例代码如下：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   const BUNDLE_NAME: string = 'com.example.jumphap'; // 在应用app.json5文件中"bundleName"节点获得
   const ABILITY_NAME: string = 'TargetHapAbility'; // 在HAP包的对应Ability文件中获得

   @Entry
   @Component
   struct Index {
     private context?: common.UIAbilityContext; // 创建context实例

     aboutToAppear(): void {
       this.context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取当前页面关联的UIAbilityContext
     }

     jumpHap() {
       if (this.context) {
         // 启动Ability，拉起HAP模块的UIAbility实例
         this.context.startAbility({
           bundleName: BUNDLE_NAME,
           abilityName: ABILITY_NAME
         }).then(() => {
           console.info('start ability success');
         }).catch((error: BusinessError) => {
           console.error(`start ability failed, error: ${error}`);
         });
       }
     }

     build() {
       RelativeContainer() {
         Button('startAbility跳转HAP')
           .fontSize(25)
           .width(350)
           .height(50)
           .margin({ top: 400 })
           .alignRules({
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             this.jumpHap(); // 点击跳转
           });
       };
     }
   }
   ```
3. 进入“Run”>“Edit Configurations”>“Run/Debug Configuration”，勾选主模块的Deploy Multi Hap/Hsp选框下的Deploy Multi Hap/Hsp Packages和All Modules选项，即可运行验证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/RnYEKFvpRBev40imTl02Dg/zh-cn_image_0000002658867501.png "点击放大")
4. 若是有多模块页面跳转的需求，建议还是使用静态库HAR或动态库HSP，尽量避免涉及多HAP之间的页面跳转。

## 常见FAQ

Q：feature类型的HAP包支持导出组件或者接口给其他模块使用吗？

A：feature类型的HAP包不支持导出接口或组件给其他模块使用。该类型的HAP包用于实现动态特性扩展的核心模块设计，可参考案例：[示例代码](../harmonyos-guides/hap-package.md#示例代码)。如果需要共享资源，需要使用HSP(动态共享包)或者HAR(静态共享包)。可参考多HAP场景的[使用场景](../harmonyos-guides/hap-package.md#使用场景)。
