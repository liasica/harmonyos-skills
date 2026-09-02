---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-30
title: 如何在Entry模块中访问Library模块中的数据
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何在Entry模块中访问Library模块中的数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:30d247d43487cadb4027805ee6a100ec4ba1a5e39be89da542c4858d5314ed16
---

## 问题现象

在项目开发中采用了Entry模块结合多个Library模块的设计方式，这种情况下，Library模块中的数据Entry模块如何访问到？

## 背景知识

* 模块（Module）是应用的基本功能单元，包含了源代码、资源文件、第三方库及配置文件。一个应用通常会包含一个或多个模块，因此，可以在工程中[创建模块](../harmonyos-guides/ide-add-new-module.md#section165216251331)。
* [模块（Module）类型](../harmonyos-guides/application-package-overview.md#module类型)：模块按照使用场景可以分为Ability类型的Module和Library类型的Module。前者用于实现应用的功能和特性，后者用于实现代码和资源的共享。

## 解决方案

通过在Library模块中定义静态变量和导出函数的方法，实现模块之间的数据传递。详细步骤如下：

1. 创建共享模块：新建工程时选择API 10及以上的Stage模型，工程创建完成后，新建'Static Library'模块。模块创建方法可参考在工程中[添加Module](../harmonyos-guides/ide-har.md#section643521083015)。

   此案例中通过添加模块方式，创建名为'library'的模块。

2. 在Library模块中定义函数、常量类；

   ```ts
   // ets/constants/SharedLibraryConstants.ets
   export class SharedLibraryConstants {
     static readonly ENGLISH: string = 'Hello';
     static readonly CHINESE: string = '你好';
   }

   export function add(a: number, b: number) {
     return a + b;
   }

   export function sub(a: number, b: number) {
     return a - b;
   }
   ```
3. 在library模块下找到Index.ets，导出第二步中定义的常量类和函数；

   ```ts
   export { SharedLibraryConstants, add, sub } from './src/main/ets/constants/SharedLibraryConstants';
   ```
4. 在Entry模块添加library的依赖：

   Entry的oh-package.json5中增加对library的依赖关系，点击右上角的同步。

   ```json
   "dependencies": {
     "library": "file:../library"
   }
   ```

   注：这边的'library'是library模块下oh-package.json5中name的名称。
5. 在Entry模块src/main/ets/pages/Index.ets中导入library模块中定义的函数、常量类，并使用。

   ```ts
   import { add, sub, SharedLibraryConstants } from 'library';

   @Entry
   @Component
   struct Index {
     content: string = '10和5，两个数的计算结果： ';
     systemContent: string = '语言：';
     @State result: string = '';
     @State systemResult: string = '';

     build() {
       Column() {
         Text(this.content + this.result)
           .fontSize(20)
           .fontWeight(FontWeight.Bold)
           .margin(10);

         Button('加法')
           .onClick(() => {
             this.result = add(10, 5).toString();
           })
           .margin(10);

         Button('减法')
           .onClick(() => {
             this.result = sub(10, 5).toString();
           })
           .margin(10);

         Text(this.systemContent + this.systemResult)
           .fontSize(20)
           .fontWeight(FontWeight.Bold)
           .margin(10);

         Button('英文')
           .onClick(() => {
             this.systemResult = SharedLibraryConstants.ENGLISH;
           })
           .margin(10);

         Button('中文')
           .onClick(() => {
             this.systemResult = SharedLibraryConstants.CHINESE;
           })
           .margin(10);
       }
       .width('100%');
     }
   }
   ```
6. 实现效果，通过上述步骤成功在Entry模块拿到library的数据。如图所示：当点击'加法'时，调用library中定义的加法函数，计算结果为'15'。当点击'减法'时，调用library中定义的减法函数，计算结果为'5'。点击'英文'、'中文'时，分别调用library中定义的SharedLibraryConstants类中的'Hello'、'你好'。

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/PMtCjc3JSQSDXsbqX4bvkQ/zh-cn_image_0000002658927281.png "点击放大")

## 总结

此类问题涉及整个工程中如何进行数据管理、数据传递，在开发时需明确工程中各个模块的作用，以及它们的依赖关系，并在oh-package.json5中做好依赖定义，工程逻辑结构较清晰且模块间的依赖关系明朗，有利于开发及后期维护。
