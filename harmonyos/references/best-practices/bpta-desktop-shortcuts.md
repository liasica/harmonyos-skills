---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-desktop-shortcuts
title: 桌面快捷方式
breadcrumb: 最佳实践 > 应用框架 > 程序包结构 > 桌面快捷方式
category: best-practices
scraped_at: 2026-10-21T07:09:49+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:a94e31bf7546f20cab85d78b1993ef6622902456434b9c51e2f0569b7bff5fb1
---

## 概述

随着应用的功能越来越复杂，用户在使用应用时，找到某个功能的操作步骤也在变得更加繁琐。为了提升用户体验，可以对应用中常用的功能创建对应的桌面快捷方式，以达到快速启动应用、一键直达特定功能等目的。例如相机应用的 “快速拍照”、便签应用的 “新建便签” 和地图应用的“常用地点导航”等功能的快捷方式，用户通过快捷方式可以快速进入特定功能页面，既能大大提高操作效率，同时也增加了用户对应用的依赖性。使用快捷方式，还可以实现个性化定制的需求，创建多个快捷方式，以满足个性化的工作流程和操作偏好。

## 场景介绍

以导航场景为例，当用户使用地图应用导航时，通常是先搜索目的地，然后开始导航。为了提升导航效率和提高操作便捷性，可以给该地图应用添加常去地点的导航快捷方式，如去公司、回家等。添加常去地点（例如公司、家等）的快捷方式后，用户即可通过长按应用图标，打开快捷方式入口，快速开启导航。

快捷方式创建成功后支持以下启动方式：

* 点击快捷方式入口列表中的“回家”项，即可快速打开地图应用，开启从当前位置到家的导航路线选择。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/VkZl3yDqRgGxn2qqnU-_Zw/zh-cn_image_0000002229451729.gif "点击放大")
* 长按快捷方式入口列表中的“回家”项，可将其拖动至桌面，点击桌面对应图标，即可开启从当前位置到家的导航路线选择。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/cQ_OAJGuTuusUM0V003boQ/zh-cn_image_0000002229451733.gif "点击放大")

**说明** 

本文以单[HAP](../harmonyos-guides/hap-package.md)包为场景，讲述了快捷方式的实现步骤。多[HAP](../harmonyos-guides/hap-package.md)包的场景下， 步骤与单[HAP](../harmonyos-guides/hap-package.md)包一致，都是在entry文件夹下进行shortcuts\_config.json的创建和module.json5的配置。

## 实现原理

### 关键技术

使用[shortcuts](../harmonyos-guides/module-configuration-file.md#shortcuts标签)来配置应用的快捷方式，其配置值为数组，包含四个子标签shortcutId、label、icon、wants。

* shortcutId：标识快捷方式的ID，取值为长度不超过63字节的字符串。
* label：标识快捷方式的标签信息，即快捷方式对外显示的文字描述信息。取值为长度不超过255字节的字符串，可以是描述性内容，也可以是标识label的资源索引。
* icon：标识快捷方式的图标，取值为资源文件的索引。快捷方式图标规范详见[快捷方式图标规范](../doccenter-ux-design/shortcat-0000002550987962.md#section1989093019508)，若使用Svg格式的图标资源，相关规格需满足如下限制：

  | 规格类型 | 限制 |
  | --- | --- |
  | 构建时DOM深度，渲染时节点和内部引用的统一递归路径 | 256 |
  | XML元素和文本节点总数 | 100,000 |
  | XML DOM arena中受计费分配的累计字节数 | 64 MiB |
  | 整个文档所有 `<style>` 文本回调的累计字节数 | 1 MiB |
  | 单个 `<text>` 子树的UTF-8文本长度 | 1 MiB |
  | CSS style map中不同selector key的数量 | 10,000 |
  | 单条CSS规则的声明数 | 1,000 |
  | 整个DOM中所有 `class` 属性实际展开的属性总数 | 1,000,000 |
  | 单个通用list属性值的字节数 | 1,000,000 |
  | 单个polyline/polygon解析出的点数 | 100,000 |
  | 单个path解析出的非move verb数 | 100,000 |
  | mask/filter/opacity累计设备像素消耗 | 500,000,000 |
  | 单个 `<feMerge>` 的输入数 | 10 |
* [wants](../harmonyos-guides/module-configuration-file.md#wants标签)：标识快捷方式内定义的目标[wants](../harmonyos-guides/module-configuration-file.md#wants标签)信息集合，[wants](../harmonyos-guides/module-configuration-file.md#wants标签)中可配置如下参数：

  | 属性名称 | 含义 |
  | --- | --- |
  | bundleName | 表示快捷方式的目标包名。 |
  | moduleName | 表示快捷方式的目标模块名。 |
  | abilityName | 表示快捷方式的目标组件名。 |
  | parameters | 表示拉起快捷方式时的自定义数据，仅支持配置字符串类型的数据。其中键值均最大支持1024长度的字符串。 |

[shortcuts](../harmonyos-guides/module-configuration-file.md#shortcuts标签)配置完成后，还需要在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中配置[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)字段来指定应用的快捷方式配置文件，从而完成快捷方式的基本配置。

**说明** 

通过在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中配置[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)字段的快捷方式是一种在系统中创建的可以快速访问应用程序或特定功能的链接，与[卡片](../harmonyos-guides/formkit-overview.md)的区别在于：快捷方式只允许跳转至某个具体的UIAbility，无法直接跳转至非入口页面。

### 实现流程

给地图应用添加常用地点的导航快捷方式需要进行如下步骤：

1. 创建页面并配置页面的路由信息。首先需要创建对应的快捷方式页面，且页面组件需要用@Entry装饰。然后在resources/base/profile下的main\_pages.json文件中添加对应快捷方式页面的路由信息。

   ```json
   {
     "src": [
       "pages/Index",
       "pages/GoHouse",
       "pages/GoCompany"
     ]
   }
   ```
2. 在/resources/base/profile/目录下创建名为shortcuts\_config.json的文件，并在文件中定义应用快捷方式的相关配置。其中shortcutId表示快捷方式的ID、label表示快捷方式对外显示的文字描述信息、icon表示快捷方式的图标、[wants](../harmonyos-guides/module-configuration-file.md#wants标签)中则是快捷方式内定义的目标wants信息集合。通过wants中的parameters参数来指定拉起快捷方式时的自定义数据。

   ```json
   {
     "shortcuts": [
       {
         "shortcutId": "id_company",
         "label": "$string:Go_to_the_Company",
         "icon": "$media:company",
         "wants": [
           {
             "bundleName": "com.example.desktopshortcuts",
             "moduleName": "entry",
             "abilityName": "EntryAbility",
             "parameters": {
               "shortCutKey": "CompanyPage"
             }
           }
         ]
       },
       {
         "shortcutId": "id_house",
         "label": "$string:Go_to_House",
         "icon": "$media:house",
         "wants": [
           {
             "bundleName": "com.example.desktopshortcuts",
             "moduleName": "entry",
             "abilityName": "EntryAbility",
             "parameters": {
               "shortCutKey": "HousePage"
             }
           }
         ]
       }
     ]
   }
   ```
3. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的[abilities](../harmonyos-guides/module-configuration-file.md#abilities标签)标签下的[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)中设置resource属性值为$profile:shortcuts\_config，指定应用的快捷方式配置文件，即使用shortcuts\_config.json文件中的shortcuts配置。

   ```json
   {
     "module": {
       // ...
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           // ...
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ],
           "metadata": [
             {
               "name": "ohos.ability.shortcuts",
               "resource": "$profile:shortcuts_config"
             }
           ]
         }
       ],
       // ...
     }
   }
   ```
4. 定义跳转到指定页面的方法。在步骤2中，通过parameters参数来指定了拉起快捷方式时的自定义数据 ，如"shortCutKey": "HousePage"。此时，可以通过获取want中的parameters里的shortCutKey来判断用户使用了哪种快捷方式，从而进行对应的页面跳转。如用户使用了“回家”的快捷方式进行导航，则获取到的shortCutKey的值为HousePage。

   ```screen
   export function goToSpecifyPage(context: UIContext, want?: Want) {
     let shortCutKey = want?.parameters?.shortCutKey;

     if (shortCutKey && shortCutKey === 'CompanyPage') {
       context.getRouter().pushUrl({
         url: 'pages/GoCompany'
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Failed to push url. Code is ${err.code}, message is ${err.message}`);
       });
     }
     if (shortCutKey && shortCutKey === 'HousePage') {
       context.getRouter().pushUrl({
         url: 'pages/GoHouse'
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Failed to push url. Code is ${err.code}, message is ${err.message}`);
       });
     }
   }
   ```
5. 最后，需要在Index.ets文件中定义newWantChange()方法，并在该方法中调用步骤4的goToSpecifyPage()方法，并将want作为参数传入。其中，want需要在EntryAbility.ets文件中的[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中通过AppStorage存入，然后在newWantChange()方法中获取。

   ```screen
   newWantChange(): void {
     if (this.isNewWant && AppStorage.has('want')) {
       let want: Want | undefined = AppStorage.get('want');
       if (want?.parameters?.shortCutKey) {
         this.isNewWant = false;
         goToSpecifyPage(this.getUIContext(), want);
       }
     }
   }
   ```

## 示例代码

* [通过module.json5文件配置应用快捷打开方式入口](https://gitcode.com/harmonyos_samples/DesktopShortcut)
