---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-142
title: 如何判断应用程序是否安装
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何判断应用程序是否安装
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4afa0abb762af9f10fb321de2310cff402f295f84b293fa8c356960dea10aee6
---

## 问题现象

在实际开发中，如何判断设备上是否已安装了目标应用？

## 背景知识

[canOpenLink](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercanopenlink12)：根据给定的链接判断目标应用是否可访问，链接中的scheme需要在[module.json配置文件标签](../harmonyos-guides/module-configuration-file.md#配置文件标签)里的querySchemes字段下配置。

## 解决方案

以判断华为地图是否安装为例：（需要知道目标应用的querySchemes、应用链接url）

1. 在应用中配置querySchemes：

   ```json
   "querySchemes": [
     // 华为地图
     'maps'
   ]
   ```
2. 判断应用地图是否安装：

   ```ts
   import { bundleManager } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     @State result:boolean = false;

     build() {
       Column({ space: 16 }) {
         Button('目标应用安装测试').onClick(() => {
           this.isMapInstalled();
         });

         Text(this.result ? '已安装' : '未安装');
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
     }

     isMapInstalled() {
       try {
         this.result = bundleManager.canOpenLink('maps://navigation');
       } catch (err) {
         let message = (err as BusinessError).message;
         console.error(`canOpenLink failed: ${message}`);
       }
       console.info(`canOpenLink result: ${this.result}`);
     }
   }
   ```

## 常见FAQ

Q：能否根据bundleName （包名）判断应用是否安装？

A：当前无法直接通过bundleName （包名）判断应用是否安装，可以尝试使用startAbility拉起应用，[错误码是16000001时，指定的ability不存在](../harmonyos-references/errorcode-ability.md#section16000001-指定的ability名称不存在)。

Q：canOpenLink判断App Linking方式目标应用是否安装，卸载目标应用后还是返回true，是什么原因？

A：[canOpenLink](../harmonyos-guides/canopenlink.md#使用场景)接口不支持判断以App Linking方式跳转的目标应用是否可访问。使用App Linking应用链接进行跳转时，系统会根据接口传入的uri信息（HTTPS链接）将用户引导至目标应用中的特定内容，无论应用是否已安装，用户都可以访问到链接对应的内容，所以不能作为判断应用是否安装的条件。
