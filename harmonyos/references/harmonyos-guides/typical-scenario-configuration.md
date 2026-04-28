---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typical-scenario-configuration
title: 创建应用静态快捷方式
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用静态快捷方式
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c33159b068f02adf1ed4b799bfce22cf623de199b9e005f4a7979f9827c99e06
---

随着应用的功能越来越复杂，用户在使用应用时，找到某个功能的操作步骤也变得更加繁琐。为提升用户体验，可以对应用中常用的功能创建对应的桌面快捷方式，以达到快速启动应用、一键直达特定功能等目的。例如相机应用的 “快速拍照”、便签应用的 “新建便签” 和地图应用的常用地点导航等功能的快捷方式，用户通过快捷方式可以快速进入特定功能页面，既能大大提高操作效率，同时也增加了用户对应用的依赖性。使用快捷方式，还可以实现个性化定制的需求，创建多个快捷方式，以满足个性化的工作流程和操作偏好。快捷方式的配置请参考[配置方法](typical-scenario-configuration.md#配置方法)，快捷方式的管理能力请参考[shortcutManager模块](../harmonyos-references/js-apis-shortcutmanager.md)。

## 场景介绍

以导航场景为例，用户使用地图应用导航时，通常先搜索目的地，然后开始导航。为了提升导航效率和操作便捷性，建议在地图应用中添加常去地点的快捷方式，如公司、家等。添加这些快捷方式后，用户长按应用图标，即可打开快捷方式入口，快速启动导航。详情请参见[桌面快捷方式](../best-practices/bpta-desktop-shortcuts.md)。

说明

桌面展示快捷方式的数量有上限要求，最多展示4个。

## 配置方法

下面介绍在工程中配置静态快捷方式的方法。

1. 在entry/src/main/resources/base/element/string.json配置资源文件如下。

   ```
   1. {
   2. "string": [
   3. {
   4. "name": "share",
   5. "value": "分享好友"
   6. },
   7. {
   8. "name": "add",
   9. "value": "添加收藏"
   10. }
   11. ]
   12. }
   ```
2. 配置快捷方式文件。

   在模块的/resources/base/profile/目录下配置[快捷方式的配置文件](module-configuration-file.md#shortcuts标签)，如shortcuts\_config.json。

   ```
   1. {
   2. "shortcuts": [
   3. {
   4. "shortcutId": "id_test1",
   5. "label": "$string:add",
   6. "icon": "$media:add_icon",
   7. "wants": [
   8. {
   9. "bundleName": "com.ohos.hello",
   10. "moduleName": "entry",
   11. "abilityName": "EntryAbility1",
   12. "parameters": {
   13. "testKey": "testValue"
   14. }
   15. }
   16. ]
   17. },
   18. {
   19. "shortcutId": "id_test2",
   20. "label": "$string:share",
   21. "icon": "$media:share_icon",
   22. "wants": [
   23. {
   24. "bundleName": "com.ohos.hello",
   25. "moduleName": "entry",
   26. "abilityName": "EntryAbility",
   27. "parameters": {
   28. "testKey": "testValue"
   29. }
   30. }
   31. ]
   32. }
   33. ]
   34. }
   ```
3. 在应用的module.json5文件中配置metadata，指向快捷方式的配置文件。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. "name": "EntryAbility",
   7. "srcEntry": "./ets/entryability/EntryAbility.ets",
   8. "metadata": [
   9. {
   10. "name": "ohos.ability.shortcuts",  // 配置快捷方式，该值固定为ohos.ability.shortcuts
   11. "resource": "$profile:shortcuts_config"  // 指定shortcuts信息的资源位置
   12. }
   13. ],
   14. // ...
   15. }
   16. ],
   17. // ...
   18. },
   19. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/TypicalScenarioConfiguration/entry/src/main/module.json5#L16-L79)

安装应用后，长按桌面上的应用图标，图标上方会显示开发者配置的快捷方式：“添加收藏”和“分享好友”。点击相应标签，可启动对应的组件。应用配置的静态快捷方式在桌面上的展示效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/1wnVcp4zRwiIZZ6LYWvryQ/zh-cn_image_0000002583437523.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233729Z&HW-CC-Expire=86400&HW-CC-Sign=79B0B59653E337179E721177801B3C16B18FC1531067AE2608E1504B519EE1E2)

## 隐藏快捷方式

可以通过[setShortcutVisibleForSelf](../harmonyos-references/js-apis-shortcutmanager.md#shortcutmanagersetshortcutvisibleforself)接口隐藏或展示快捷方式。
