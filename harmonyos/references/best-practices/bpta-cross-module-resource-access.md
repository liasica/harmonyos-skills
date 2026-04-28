---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-module-resource-access
title: 跨模块资源访问
breadcrumb: 最佳实践 > 应用框架 > 程序包结构 > 跨模块资源访问
category: best-practices
scraped_at: 2026-04-28T08:20:07+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:2da628e3446964afbe7a21dfe499361a6e5d17f73e329f3aa4d3824860f64f59
---

## 概述

随着应用复杂度的增加，将应用划分为多个独立的模块有助于提高代码的可维护性和可扩展性。特别是在大型项目中，不同团队负责不同的模块（如HAR/HSP模块），当某些资源（如图标、颜色、字符串等）被多个模块复用时，可以将其集中管理在某个模块中给其他模块使用，从而减少重复定义，便于资源管理，提升开发效率。

在HarmonyOS中应用模块化设计一般使用HAR和HSP来共享资源，本文将介绍如何实现跨模块访问HAR和HSP里面的资源。

## 跨模块访问HAR资源

跨模块（HAP、HSP或HAR）访问HAR资源和访问模块自身资源一样，可以使用下面两种方法访问资源：

1. **方法一：通过'$r'或'$rawfile'语法访问资源。**

   此方法适合简单的、静态的资源引用场景，比如在UI组件中直接引用。通过$('app.type.name')或$rawfile('name')访问资源，其中，app为resources目录中定义的资源；type为资源类型或资源的存放位置；name为资源名，开发者定义资源时确定。

   ```
   1. Text($r('app.string.string_in_har2'))
   2. Image($r('app.media.image_in_har2'))
   ```

   [Har1Page.ets](https://gitcode.com/harmonyos_samples/CrossModuleResourceAccess/blob/master/har1/src/main/ets/components/Har1Page.ets#L28-L34)
2. **方法二：通过resourceManager访问资源。**

   此方法提供的API更为丰富，适用于构建更加复杂的应用逻辑，比如图像效果处理。通过本应用上下文获取ResourceManager后，调用不同[资源管理接口](../harmonyos-references/js-apis-resource-manager.md)访问不同资源。例如：resourceManager.getStringSync('string\_in\_har1').id可获取字符串资源，推荐使用资源id作为入参的方式使用，这种方式性能更好，具体可以参考：避免使用耗时接口中关于[ResourceManager](bpta-time-optimization-of-the-main-thread.md#section193673511440)的介绍。

   ```
   1. let stringInHar1 = this.context.resourceManager.getStringSync($r('app.string.access_resource_har1').id);
   2. let imgArrayInHar1 = this.context.resourceManager.getMediaContentSync($r('app.media.image_in_har1').id);
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/CrossModuleResourceAccess/blob/master/entry/src/main/ets/pages/Index.ets#L35-L36)

说明

1. 在编译构建HAP时，DevEco Studio会从HAP模块及依赖的模块中收集资源文件，如果不同模块下的资源文件出现重名冲突时，DevEco Studio会按照以下优先级进行覆盖（优先级由高到低）：

* AppScope里面的资源。
* HAP包自身模块。
* 依赖的HAR模块，如果依赖的多个HAR之间有资源冲突，会按照工程oh-package.json5中dependencies下的依赖顺序进行覆盖，依赖顺序在前的优先级较高。

2. 对于HAR开启混淆、中间码HAR、字节码HAR、跨HAP/HSP包，这四种场景推荐使用getStringByName()等方法通过名称获取资源。

## 跨模块访问HSP资源

跨模块（HAP、HSP或HAR）访问HSP资源一般有以下三种方法，下面详细介绍这三种方法的使用场景和优缺点。

1. **方法一：通过"$r"或"$rawfile"语法访问资源。**

   **使用场景**

   适合简单的、静态的资源引用场景，比如在UI组件中直接引用。

   **优点**

   使用简单，易于理解。

   **缺点**

   不能直接获取到值，不方便对数据进行处理。

   **实现方式**

   使用$r或$rawfile语法，并指定HSP模块名称（HSP模块module.json5中module的name属性），资源访问格式如下：

   * 使用$r('[hsp].media.name')访问resources资源目录下media文件夹中的资源。
   * 使用$rawfile('[hsp].name')访问rawfile资源目录下的资源。

   其中，[hsp]是HSP模块名，type是资源类型，而name是资源名称。下面示例代码中加载的资源来自名为“hsp1”的HSP模块：

   ```
   1. Text($r('app.string.access_resource_hsp1'))
   2. Text($r('[hsp1].string.string_in_hsp1'))
   3. Image($r('[hsp1].media.image_in_hsp1'))
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/CrossModuleResourceAccess/blob/master/entry/src/main/ets/pages/Index.ets#L90-L103)
2. **方法二：通过createModuleContext访问资源。**

   **使用场景**

   根据业务逻辑需要对资源文件数据进行处理，比如图片编解码、字符串拼接处理，适合少量数据的使用。

   **优点**

   使用相对简单，不需要添加依赖。

   **缺点**

   因为需要开发者手动写资源的名称，且使用方无法感知HSP内部的资源名称变化，当引用的数据量比较多的时候，建议使用第三种方法访问资源。

   **实现方式**

   通过[createModuleContext(context, moduleName)](../harmonyos-references/js-apis-app-ability-application.md#applicationcreatemodulecontext)接口创建同应用中不同module的上下文，获取resourceManager对象后，调用不同[资源管理接口](../harmonyos-references/js-apis-resource-manager.md)访问不同资源。

   ```
   1. import { application, common } from '@kit.AbilityKit';
   2. application.createModuleContext(this.context, 'hsp1').then(data => {
   3. let stringInHsp1 = data.resourceManager.getStringByNameSync('string_in_hsp1');
   4. let imgArrayInHsp2 = data.resourceManager.getMediaByNameSync('image_in_hsp1');
   5. // ...
   6. })
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/CrossModuleResourceAccess/blob/master/entry/src/main/ets/pages/Index.ets#L17-L49)
3. **方法三：HSP导出资源给使用方使用。**

   **使用场景**

   根据业务逻辑需要对资源文件数据进行处理，比如图片编解码、字符串拼接处理。

   **优点**

   * HSP开发者可以控制自己需要导出的资源，不需要对外暴露的资源可以不用导出。
   * 使用方无须感知HSP内部的资源名称。当HSP内部的资源名称发生变化时，也不需要使用方跟着修改。

   **缺点**

   需要封装管理类，开发稍显复杂。

   **实现方式**

   跨包访问HSP内资源时，推荐实现一个资源管理类，以封装对外导出的资源，其具体实现如下。

1. 在HSP中对外提供的资源封装为一个资源管理类：

   ```
   1. export class ResManager {
   2. static getPic(): Resource {
   3. return $r('app.media.image_in_hsp1');
   4. }

   6. static getDesc(): Resource {
   7. return $r('app.string.string_in_hsp1');
   8. }
   9. }
   ```

   [ResManager.ets](https://gitcode.com/harmonyos_samples/CrossModuleResourceAccess/blob/master/hsp1/src/main/ets/common/ResManager.ets#L17-L25)
2. 对外暴露的接口，需要在HSP入口文件index.ets中声明：

   ```
   1. export { ResManager } from './src/main/ets/common/ResManager';
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/CrossModuleResourceAccess/blob/master/hsp1/Index.ets#L19-L19)
3. 使用方使用import导入ResManager，访问HSP导出的资源，如下所示：

   ```
   1. import { ResManager } from 'hsp1';

   3. @Entry
   4. @Component
   5. struct GetHspResource {
   6. build() {
   7. Column() {
   8. Text(ResManager.getDesc())
   9. .fontSize(50)
   10. .fontWeight(FontWeight.Bold)
   11. Image(ResManager.getPic())
   12. .height(100)
   13. }
   14. .width('100%')
   15. .height('100%')
   16. }
   17. }
   ```

   [GetHspResource.ets](https://gitcode.com/harmonyos_samples/CrossModuleResourceAccess/blob/master/entry/src/main/ets/pages/GetHspResource.ets#L17-L33)

## 示例代码

* [实现跨模块访问HAR/HSP资源文件功能](https://gitcode.com/harmonyos_samples/CrossModuleResourceAccess)
