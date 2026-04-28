---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/medialibrary-request-photouris-permission
title: 设备升级继承媒体文件访问权限
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 设备升级继承媒体文件访问权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ff2b86d153de2fd59a5a5c049e88367ad3fa129074e3a09e0110d0474e997216
---

应用在HarmonyOS 3.1 Release API 9及更低版本运行时，有图片/视频访问权限，并在应用内记录对应的图片/视频文件路径或uri，在进入应用特定界面时，可实时访问图片/视频显示内容。

但在设备从HarmonyOS 3.1 Release API 9及更低版本升级至HarmonyOS 5.0.2及以上版本时，图片、视频等媒体文件的访问方式发生变化，应用无法使用原来的文件路径或uri访问媒体文件，且新版本上应用默认没有权限直接访问图片/视频。在新版本上，应用需要向用户发起请求，用户同意后，可继承原有的媒体文件访问权限。

本指南将帮助开发者了解如何在升级后，继承媒体文件的访问权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/2BhSz8gMRUusLnOk1t85cw/zh-cn_image_0000002552798960.png?HW-CC-KV=V1&HW-CC-Date=20260427T234636Z&HW-CC-Expire=86400&HW-CC-Sign=5F11F4B1E6DF1BE3CB6FA50327076210C35464FD4DE724C9B40F3C9B6DB45490)

应用在启动或是进入对应的业务界面之后，从应用数据中获取在HarmonyOS 3.1/4.0版本的应用上已有权限且需要继承权限的媒体文件uri，调用Scenario Fusion Kit的接口[convertFileUris](../harmonyos-references/scenario-fusion-fileuriresult.md#convertfileuris)，获取转换后的HarmonyOS 5.0可访问的uri。再调用Media Library Kit的接口[requestPhotoUrisReadPermission()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#requestphotourisreadpermission14)，输入需要继承访问权限的媒体文件uri，拉起授权界面。在授权界面，根据应用输入的uri，将显示对应图片/视频缩略图。用户可以勾选对应的图片/视频，并同意授权，此时应用将获取该图片/视频的访问权限。

在用户界面的效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/nJQgS6p3SLmS-hPBp1yllA/zh-cn_image_0000002583438655.png?HW-CC-KV=V1&HW-CC-Date=20260427T234636Z&HW-CC-Expire=86400&HW-CC-Sign=6DD4542209EABAF6269E6377DBB26EA00C849BE30E3C1CCC04451FE571638586)

## 开发步骤

此处仅展示如何调用Media Library Kit的接口[requestPhotoUrisReadPermission()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#requestphotourisreadpermission14)，输入需要继承访问权限的媒体文件uri，拉起授权界面。

调用Scenario Fusion Kit的接口[convertFileUris](../harmonyos-references/scenario-fusion-fileuriresult.md#convertfileuris)，获取转换后的HarmonyOS 5.0可访问的uri，请参考[公共目录文件URI继承](code-precautions.md#公共目录文件uri继承)。

1. 导入相关接口模块文件。

   ```
   1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 初始化输入的uri列表。

   ```
   1. // 用于初始化时接口类实例
   2. // 请在组件内获取context，确保this.getUiContext().getHostContext()返回结果为UIAbilityContext
   3. import { common } from '@kit.AbilityKit';
   4. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   5. let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
   ```
3. 初始化输入的uri列表并赋值。

   ```
   1. private uris: Array<string> = new Array<string>();
   2. // 自行对其赋值，输入需要授权的uri信息
   3. this.uris = [];
   ```
4. 调用接口拉起授权界面。

   ```
   1. try {
   2. phAccessHelper.requestPhotoUrisReadPermission(this.uris).then((result: Array<string>) => {
   3. console.info("requestPhotoUrisReadPermission, result = " + JSON.stringify(result));
   4. if (result) {
   5. // 授权成功返回授权后新的uri列表
   6. } else {
   7. // 授权失败后的处理
   8. }
   9. })
   10. } catch(error) {
   11. console.error("requestPhotoUrisReadPermission error: " + JSON.stringify(error));
   12. }
   ```

## 完整示例

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';
3. @Entry
4. @Component
5. struct Index{
6. private uris: Array<string> = new Array<string>();

8. build() {
9. Row() {
10. Column() {
11. Button("拉起授权界面").width('100%').height('10%').margin({top: 150})
12. .onClick(()=>{
13. // 自行对其赋值，输入需要授权的uri信息
14. this.uris = [];
15. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
17. try {
18. phAccessHelper.requestPhotoUrisReadPermission(this.uris).then((result: Array<string>) => {
19. console.info("requestPhotoUrisReadPermission, result = " + JSON.stringify(result));
20. if (result) {
21. // 授权成功返回授权后新的uri列表
22. } else {
23. // 授权失败后的处理
24. }
25. })
26. } catch(error) {
27. console.error("requestPhotoUrisReadPermission error: " + JSON.stringify(error));
28. }
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```
