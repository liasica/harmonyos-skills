---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/layered-image
title: 配置应用图标和名称
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 配置应用图标和名称
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:34+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3f058eee612e6142f3d4b178b1bd9a3159d3fc0fc5e68a60fb65314745196ed3
---

本页面提供应用图标和名称的配置指导。应用图标分为单层图标和分层图标。单层图标包含一个图片，分层图标包含前景图和背景图。图标规范详见[图标资源规范](../design-guides/application-icon-0000001953444009.md#section634668113212)，图标和名称配置约束详见[图标和名称配置](application-component-configuration-stage.md#应用图标和名称配置)。

## 使用场景

* 用于在设备桌面上展示当前应用。例如：桌面或者最近任务列表中显示应用。
* 用于在应用界面内展示当前应用。例如：在设置应用中展示应用列表。
* 用于在通知栏中展示发出通知消息的应用。

效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/9kC2iqaHQRmw_Q2Y923cdA/zh-cn_image_0000002589243777.png?HW-CC-KV=V1&HW-CC-Date=20260429T052533Z&HW-CC-Expire=86400&HW-CC-Sign=FB1EB3C694FBD433852C2378A1F7819F79ED3770C10F19C22AAF8B820C3F4B46)

## 配置优先级和生成策略

* HAP中包含UIAbility

  1. 入口UIAbility：skills标签中entities中包含"entity.system.home"、并且actions中包含"ohos.want.action.home"。
  2. 在module.json5配置了多个入口UIAbility：

     + 如果module.json5中mainElement配置的为入口UIAbility，则返回mainElement对应的入口UIAbility配置的icon和label。
     + 如果module.json5中mainElement未配置或者配置的不为入口UIAbility，则返回module.json5中配置的第一个入口UIAbility对应的icon和label。
  3. 在module.json5配置文件中，出现以下任一情况时，系统将返回app.json5中的icon或label：

     + mainElement配置的为入口UIAbility，但是入口UIAbility未设置icon或label。
     + mainElement未配置或者配置的不为入口UIAbility，且module.json5配置文件中第一个入口UIAbility未设置icon或label。

  多HAP包的工程中，如果entry类型存在，以entry类型的HAP中module.json5配置文件为准。如果没有entry类型，此时用所有hap的moduleName以ASCII字典序排序，最终以排序为最后一个的feature包的module.json5配置文件为准。
* HAP中不包含UIAbility，系统将返回app.json5中的icon和label。

说明

在编译构建时，AppScope目录下的资源文件会合入到模块下相同路径的资源目录中，如果两个目录下存在重名文件，编译打包后AppScope目录下的资源文件会覆盖模块下的资源。

例如，app.json5和module.json5中配置的分层图标的资源文件名称一致、图标不一致，AppScope目录下的资源文件会覆盖模块中的文件，最后的效果是app.json5中的配置图标生效。

如果应用配置中未设置入口UIAbility，点击桌面图标将直接进入应用详情页（设置->应用和元服务下，点击任意应用即可进入该应用的应用详情页）。其他情况下，点击桌面图标将直接进入应用页面。应用未配置入口UIAbility包含2种场景：

1. 应用没有配置任何UIAbility。
2. 所有UIAbility中skills标签下的entities未配置或配置内容不包括 "entity.system.home"，并且actions未配置或配置内容不包括 "ohos.want.action.home"。

## 配置单层图标和应用名称

* **方式一：配置app.json5**

  该配置仅当module.json5配置文件中无UIAbility、或者存在UIAbility但abilities标签中未设置icon和label（可手动删除icon和label配置）时生效。

  ```
  1. {
  2. "app": {
  3. // ...
  4. "icon": "$media:app_icon",
  5. "label": "$string:app_name" // 需要在AppScope/resources/base/element/string.json配置name为app_name的资源，已存在可以忽略
  6. }
  7. }
  ```

  [app.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/LayeredImage1/AppScope/app.json5#L16-L29)
* **方式二：配置module.json5**

  除了需要配置icon与label字段，还需要在skills标签下面的entities中添加"entity.system.home"、actions中添加"ohos.want.action.home"。

  ```
  1. {
  2. "module": {
  3. // ...
  4. "abilities": [
  5. {
  6. // ...
  7. "icon": "$media:icon",
  8. // 需要在entry/src/main/resources/base/element/string.json配置name为EntryAbility_label的资源，已存在可以忽略
  9. "label": "$string:EntryAbility_label",
  10. "skills": [
  11. {
  12. "entities": [
  13. "entity.system.home"
  14. ],
  15. "actions": [
  16. "ohos.want.action.home"
  17. ]
  18. }
  19. ]
  20. }
  21. ],
  22. // ...
  23. }
  24. }
  ```

  [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/LayeredImage1/entry/src/main/module.json5#L16-L74)

## 配置分层图标和应用名称

* **方式一：配置app.json5**

  该配置仅当module.json5配置文件中无UIAbility、或者存在UIAbility但abilities标签中未设置icon和label（可手动删除icon和label配置）时生效。

  1. 将前景资源和背景资源文件放在“AppScope\resources\base\media”文件夹下。

     本例中，前景资源文件名为“foreground.png”，背景资源文件名为“background.png”。
  2. 在“AppScope\resources\base\media”文件夹下app\_layered\_image.json分层图标资源文件中，配置分层图标的前景资源与背景资源信息。

     ```
     1. {
     2. "layered-image":
     3. {
     4. "background" : "$media:background",
     5. "foreground" : "$media:foreground"
     6. }
     7. }
     ```
  3. 在[app.json5配置文件](app-configuration-file.md)中引用分层图标资源文件。示例如下：

     ```
     1. {
     2. "app": {
     3. // ...
     4. "icon": "$media:layered_image",
     5. "label": "$string:app_name" // 需要在AppScope/resources/base/element/string.json配置name为app_name的资源，已存在可以忽略
     6. }
     7. }
     ```

     [app.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/LayeredImage2/AppScope/app.json5#L16-L29)
* **方式二：配置module.json5**

  1. 将前景资源和背景资源文件放在“entry\src\main\resources\base\media”文件夹下。

     本例中采用的前景资源和背景资源的文件名分别为“foreground.png”和“background.png”。
  2. 在“entry\src\main\resources\base\media”文件夹下layered\_image.json分层图标资源文件中，配置分层图标的前景资源与背景资源信息。

     ```
     1. {
     2. "layered-image":
     3. {
     4. "background" : "$media:background",
     5. "foreground" : "$media:foreground"
     6. }
     7. }
     ```
  3. 如果需要在桌面显示UIAbility图标，除了需要配置icon与label字段，还需要在skills标签下面的entities中添加"entity.system.home"、actions中添加"ohos.want.action.home"。

     ```
     1. {
     2. "module": {
     3. // ...
     4. "abilities": [
     5. {
     6. // ...
     7. // icon配置为分层图标资源文件的索引
     8. "icon": "$media:layered_image",
     9. // 需要在entry/src/main/resources/base/element/string.json配置name为EntryAbility_label的资源，已存在可以忽略
     10. "label": "$string:EntryAbility_label",
     11. "skills": [
     12. {
     13. "entities": [
     14. "entity.system.home"
     15. ],
     16. "actions": [
     17. "ohos.want.action.home"
     18. ]
     19. }
     20. ]
     21. }
     22. ],
     23. // ...
     24. }
     25. }
     ```

     [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/LayeredImage2/entry/src/main/module.json5#L16-L75)

说明

DevEco Studio NEXT Beta1(5.0.3.814) 及之后的版本，创建应用时默认模板中包含分层图标的资源文件，不同版本生成的资源文件名称可能不同，文件名称支持手动修改。如果分层图标资源文件不存在则需要手动创建，文件名称需要符合资源命名规范，由数字、字母、点和下划线组成。
