---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-desktop-shortcuts
title: 桌面快捷方式
breadcrumb: 最佳实践 > 应用框架 > 程序包结构 > 桌面快捷方式
category: best-practices
scraped_at: 2026-04-29T14:10:47+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:bd6188ef7d3d3e7944ff8715e5a68e96343ec9ecda623e283a365ea892789daf
---

## 概述

随着应用的功能越来越复杂，用户在使用应用时，找到某个功能的操作步骤也在变得更加繁琐。为了提升用户体验，可以对应用中常用的功能创建对应的桌面快捷方式，以达到快速启动应用、一键直达特定功能等目的。例如相机应用的 “快速拍照”、便签应用的 “新建便签” 和地图应用的“常用地点导航”等功能的快捷方式，用户通过快捷方式可以快速进入特定功能页面，既能大大提高操作效率，同时也增加了用户对应用的依赖性。使用快捷方式，还可以实现个性化定制的需求，创建多个快捷方式，以满足个性化的工作流程和操作偏好。

## 场景介绍

以导航场景为例，当用户使用地图应用导航时，通常是先搜索目的地，然后开始导航。为了提升导航效率和提高操作便捷性，可以给该地图应用添加常去地点的导航快捷方式，如去公司、回家等。添加常去地点（例如公司、家等）的快捷方式后，用户即可通过长按应用图标，打开快捷方式入口，快速开启导航。

快捷方式创建成功后支持以下启动方式：

* 点击快捷方式入口列表中的“回家”项，即可快速打开地图应用，开启从当前位置到家的导航路线选择。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/mzTjD9rbQWad90yKhtFWtw/zh-cn_image_0000002229451729.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061046Z&HW-CC-Expire=86400&HW-CC-Sign=FAF03072FE56650B865092C443E31E90A4963A1A088E249C6492561B2B1D2830 "点击放大")
* 长按快捷方式入口列表中的“回家”项，可将其拖动至桌面，点击桌面对应图标，即可开启从当前位置到家的导航路线选择。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/YoyXxc-qTe6zFJaDJPmzbg/zh-cn_image_0000002229451733.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061046Z&HW-CC-Expire=86400&HW-CC-Sign=907819BBF3EA219C6184B4B8B717922392D5EDAF67D9332FBCF6F47AED0054AF "点击放大")

说明

本文以单[HAP](../harmonyos-guides/hap-package.md)包为场景，讲述了快捷方式的实现步骤。多[HAP](../harmonyos-guides/hap-package.md)包的场景下， 步骤与单[HAP](../harmonyos-guides/hap-package.md)包一致，都是在entry文件夹下进行shortcuts\_config.json的创建和module.json5的配置。

## 实现原理

### 关键技术

使用[shortcuts](../harmonyos-guides/module-configuration-file.md#shortcuts标签)来配置应用的快捷方式，其配置值为数组，包含四个子标签shortcutId、label、icon、wants。

* shortcutId：标识快捷方式的ID，取值为长度不超过63字节的字符串。
* label：标识快捷方式的标签信息，即快捷方式对外显示的文字描述信息。取值为长度不超过255字节的字符串，可以是描述性内容，也可以是标识label的资源索引。
* icon：标识快捷方式的图标，取值为资源文件的索引。
* [wants](../harmonyos-guides/module-configuration-file.md#wants标签)：标识快捷方式内定义的目标[wants](../harmonyos-guides/module-configuration-file.md#wants标签)信息集合，[wants](../harmonyos-guides/module-configuration-file.md#wants标签)中可配置如下参数：

  | 属性名称 | 含义 |
  | --- | --- |
  | bundleName | 表示快捷方式的目标包名。 |
  | moduleName | 表示快捷方式的目标模块名。 |
  | abilityName | 表示快捷方式的目标组件名。 |
  | parameters | 表示拉起快捷方式时的自定义数据，仅支持配置字符串类型的数据。其中键值均最大支持1024长度的字符串。 |

[shortcuts](../harmonyos-guides/module-configuration-file.md#shortcuts标签)配置完成后，还需要在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中配置[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)字段来指定应用的快捷方式配置文件，从而完成快捷方式的基本配置。

说明

通过在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中配置[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)字段的快捷方式是一种在系统中创建的可以快速访问应用程序或特定功能的链接，与[卡片](../harmonyos-guides/formkit-overview.md)的区别在于：快捷方式只允许跳转至某个具体的UIAbility，无法直接跳转至非入口页面。

### 实现流程

给地图应用添加常用地点的导航快捷方式需要进行如下步骤：

1. 创建页面并配置页面的路由信息。首先需要创建对应的快捷方式页面，且页面组件需要用@Entry装饰。然后在resources/base/profile下的main\_pages.json文件中添加对应快捷方式页面的路由信息。

   ```
   1. {
   2. "src": [
   3. "pages/Index",
   4. "pages/GoHouse",
   5. "pages/GoCompany"
   6. ]
   7. }
   ```
2. 在/resources/base/profile/目录下创建名为shortcuts\_config.json的文件，并在文件中定义应用快捷方式的相关配置。其中shortcutId表示快捷方式的ID、label表示快捷方式对外显示的文字描述信息、icon表示快捷方式的图标、[wants](../harmonyos-guides/module-configuration-file.md#wants标签)中则是快捷方式内定义的目标wants信息集合。通过wants中的parameters参数来指定拉起快捷方式时的自定义数据。

   ```
   1. {
   2. "shortcuts": [
   3. {
   4. "shortcutId": "id_company",
   5. "label": "$string:Go_to_the_Company",
   6. "icon": "$media:company",
   7. "wants": [
   8. {
   9. "bundleName": "com.example.desktopshortcuts",
   10. "moduleName": "entry",
   11. "abilityName": "EntryAbility",
   12. "parameters": {
   13. "shortCutKey": "CompanyPage"
   14. }
   15. }
   16. ]
   17. },
   18. {
   19. "shortcutId": "id_house",
   20. "label": "$string:Go_to_House",
   21. "icon": "$media:house",
   22. "wants": [
   23. {
   24. "bundleName": "com.example.desktopshortcuts",
   25. "moduleName": "entry",
   26. "abilityName": "EntryAbility",
   27. "parameters": {
   28. "shortCutKey": "HousePage"
   29. }
   30. }
   31. ]
   32. }
   33. ]
   34. }
   ```
3. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的[abilities](../harmonyos-guides/module-configuration-file.md#abilities标签)标签下的[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)中设置resource属性值为$profile:shortcuts\_config，指定应用的快捷方式配置文件，即使用shortcuts\_config.json文件中的shortcuts配置。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. "name": "EntryAbility",
   7. "srcEntry": "./ets/entryability/EntryAbility.ets",
   8. // ...
   9. "skills": [
   10. {
   11. "entities": [
   12. "entity.system.home"
   13. ],
   14. "actions": [
   15. "ohos.want.action.home"
   16. ]
   17. }
   18. ],
   19. "metadata": [
   20. {
   21. "name": "ohos.ability.shortcuts",
   22. "resource": "$profile:shortcuts_config"
   23. }
   24. ]
   25. }
   26. ],
   27. // ...
   28. }
   29. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/DesktopShortcut/blob/master/entry/src/main/module.json5#L6-L67)
4. 定义跳转到指定页面的方法。在步骤2中，通过parameters参数来指定了拉起快捷方式时的自定义数据 ，如"shortCutKey": "HousePage"。此时，可以通过获取want中的parameters里的shortCutKey来判断用户使用了哪种快捷方式，从而进行对应的页面跳转。如用户使用了“回家”的快捷方式进行导航，则获取到的shortCutKey的值为HousePage。

   ```
   1. export function goToSpecifyPage(context: UIContext, want?: Want) {
   2. let shortCutKey = want?.parameters?.shortCutKey;

   4. if (shortCutKey && shortCutKey === 'CompanyPage') {
   5. context.getRouter().pushUrl({
   6. url: 'pages/GoCompany'
   7. }).catch((err: BusinessError) => {
   8. hilog.error(0x0000, 'testTag', `Failed to push url. Code is ${err.code}, message is ${err.message}`);
   9. });
   10. }
   11. if (shortCutKey && shortCutKey === 'HousePage') {
   12. context.getRouter().pushUrl({
   13. url: 'pages/GoHouse'
   14. }).catch((err: BusinessError) => {
   15. hilog.error(0x0000, 'testTag', `Failed to push url. Code is ${err.code}, message is ${err.message}`);
   16. });
   17. }
   18. }
   ```

   [CommonFunction.ets](https://gitcode.com/HarmonyOS_Samples/DesktopShortcut/blob/master/entry/src/main/ets/util/CommonFunction.ets#L22-L39)
5. 最后，需要在Index.ets文件中定义newWantChange()方法，并在该方法中调用步骤4的goToSpecifyPage()方法，并将want作为参数传入。其中，want需要在EntryAbility.ets文件中的[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中通过AppStorage存入，然后在newWantChange()方法中获取。

   ```
   1. newWantChange(): void {
   2. if (this.isNewWant && AppStorage.has('want')) {
   3. let want: Want | undefined = AppStorage.get('want');
   4. if (want?.parameters?.shortCutKey) {
   5. this.isNewWant = false;
   6. goToSpecifyPage(this.getUIContext(), want);
   7. }
   8. }
   9. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/DesktopShortcut/blob/master/entry/src/main/ets/pages/Index.ets#L77-L86)

## 示例代码

* [通过module.json5文件配置应用快捷打开方式入口](https://gitcode.com/harmonyos_samples/DesktopShortcut)
