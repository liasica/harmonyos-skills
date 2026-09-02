---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-22
title: 卡片中引用HAR包中组件的实现方式及白屏问题解决
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 卡片中引用HAR包中组件的实现方式及白屏问题解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:970fe777b6fb5cb4c832e8730c287c2427ee016f3c89727096c2809d3c8b244f
---

## 问题现象

为了提高自定义组件复用率，项目采用HAR包定义公共UI组件，如何在卡片页面中引用？

## 背景知识

* [Form Kit（卡片开发服务）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* [HAR（Harmony Archive）](../harmonyos-guides/har-package.md)是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。

## 解决方案

在项目中引用HAR，本文介绍采用从本地文件夹安装以及从本地压缩包安装两种方式。

* **场景一：从本地文件夹安装。**
  1. 参考[创建ArkTS卡片](../harmonyos-guides/arkts-ui-widget-creation.md)，在工程中创建动态卡片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/E14DYbz6ROKgTJpxaVnzUg/zh-cn_image_0000002681833717.png)
  2. 参考[构建HAR](../harmonyos-guides/ide-hvigor-build-har.md#section3761328124112)，在工程中创建名称为localFolderPack的HAR包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Yj0QVX5cQ6641FuA7a0Olw/zh-cn_image_0000002681673901.png)
  3. 在localFolderPack的HAR包中自定义MainPage组件，并导出。

     ```ts
     @Component
     export struct MainPage {
       @State message: string = 'Hello World';

       build() {
         Row() {
           Column() {
             Text(this.message)
               .fontSize($r('app.float.page_text_font_size'))
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                 this.message = 'Welcome';
               });
           }
           .width('100%');
         }
         .height('100%');
       }
     }
     ```
  4. 在主项目中配置对HAR的依赖，参考[引用及管理共享包-引用本地模块源码](../harmonyos-guides/ide-har-import.md)。导入后oh-package.json5中会添加"localfolderpack": "file:../localFolderPack"。
  5. 在项目卡片页面WidgetCard.ets，引入HAR包并使用组件。

     ```ts
     import { MainPage } from 'localfolderpack';

     @Entry
     @Component
     struct WidgetCard {
       build() {
         Row() {
           MainPage();
         }
         .width('100%')
         .height('100%')
         .backgroundColor($r('sys.color.comp_background_primary'));
       }
     }
     ```
* **场景二：从本地压缩包安装。**
  1. 参考[创建ArkTS卡片](../harmonyos-guides/arkts-ui-widget-creation.md)，在工程中创建动态卡片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/Ui2-Zyz6TrKVwgmyM2_m-g/zh-cn_image_0000002681834069.png)
  2. 参考[构建HAR](../harmonyos-guides/ide-hvigor-build-har.md#section3761328124112)，在工程中创建名称为localZipPack的HAR包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/cc2xkuytSlyBeBNaqOweqw/zh-cn_image_0000002651794458.png)
  3. 在localZipPack的HAR包中自定义MainPage组件，并导出。

     ```ts
     @Component
     export struct MainPage {
       isShow: boolean = true;

       build() {
         Column() {
           if (this.isShow) {
             Row() {
               Text('localZipPack hello')
                 .fontSize(20);
             };
           } else {
             Row() {
               Text('localZipPack hi')
                 .fontSize(20);
             };
           }
         }
         .padding(16)
         .width('100%')
         .height('100%');
       }
     }
     ```
  4. 参考[编译HAR模块](../harmonyos-guides/ide-har.md#section7892044183814)，进行编译，获取build/default/outputs/default/localZipPack.har。
  5. 在主项目中配置对HAR的依赖，参考[引用及管理共享包-引用本地HAR/HSP包](../harmonyos-guides/ide-har-import.md)。导入后oh-package.json5中会添加"localzippack": "file:../localZipPack.har"。
  6. 在项目卡片页面WidgetCard.ets，引入HAR包并使用组件。注意：从本地压缩包安装HAR包，编译器未能将HAR包自定义组件所使用的系统组件自动导入，需要手动将所使用的组件重新配置。本案例在MainPage组件中使用了Column、Row、Text、if组件，所以完整写法如下：

     ```ts
     import { MainPage } from 'localzippack';

     @Entry
     @Component
     struct WidgetCard {
       build() {
         Row() {
           MainPage({ isShow: false });
         };
       }

       @Builder
       MainPageImport() {
         Column();
         Text();
         Row();
         if (true) {
         }
       }
     }
     ```

## 常见FAQ

Q：采用HAR包封装公共组件，将HAR包引入在卡片中复用时可能出现白屏，该如何解决？

A：采用源码编译的方式直接从本地文件夹安装HAR包不会出现问题，使用\*.har压缩包安装引入出现该问题原因是二进制文件没有参与编译，导致打包的component\_collection.json文件里不包含二进制文件内的组件信息。

Q：锁屏卡片添加SDK暴露的Component组件出现白屏，SDK组件若是普通Text文本就可以加载成功，若是复杂组件组合就会出现白屏，该如何解决？

A：该问题已在6.1.1 Release（6.1.1.290）版本上修复，请升级版本验证。
