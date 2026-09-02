---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-29
title: 引用三方库图片资源报错
breadcrumb: FAQ > DevEco Studio > 工程管理 > 引用三方库图片资源报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:995213d5ca8e17c7f7fdfce81683cbef43eb07c794e7b47f1d5d28414232567c
---

## 问题现象

导入一个三方库，库里有资源文件。单独的三方库能正常运行，但是被导入工程后，引用资源文件失败。

**预期效果**：导入三方库后，能成功使用三方库中的资源文件。

**实际效果**：导入三方库后，使用库中资源文件报错。

本文将以导入@ohos/zxing中的scan\_back图片为例。

**问题代码如下：**

1. 工程内终端上安装@ohos/zxing。

   ```txt
   ohpm install @ohos/zxing
   ```
2. 检查工程级oh-package.json5文件，确定三方库已安装成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/RveTeB2YQlSGXieKgPP1mg/zh-cn_image_0000002628408062.png "点击放大")
3. 在工程中使用@ohos/zxing的scan\_back图片资源，发现资源报未知资源错误。

   ```ts
   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         Image($r('app.media.scan_back')).width(100).height(100).backgroundColor(Color.Black);
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Hzn5zHoCTUS2Chgdw90xyQ/zh-cn_image_0000002628567958.png "点击放大")

## 背景知识

* [添加依赖项](../harmonyos-guides/ide-hvigor-dependencies.md)：应用/服务支持通过包管理工具ohpm来安装、共享、分发代码，管理项目的依赖关系。
* [三方库的使用](../harmonyos-guides/cta-third-party.md)：常用的三方库可以分为UI、动画、网络、图片、多媒体、数据存储、安全、工具等；使用方式请见链接。

## 解决方案

对于不同资源，有不同的导入方式，当前资源为三方库资源，因此得从三方库的导入方式来排查问题：

* **模块内引用**：模块只会查找自己模块内的资源，因此导入三方库的位置应该放入模块的oh-package.json5文件中，不需要放在工程级oh-package.json5文件中。
* **工程内引用**：在工程级别目录下导入三方库，若需要对应模块能使用该库，则需在三方库中暴露对应资源，再在模块中import使用。

所以只需在entry模块的oh-package.json文件中引用@ohos/zxing，即可在entry模块使用$r显示三方库的图片资源。
