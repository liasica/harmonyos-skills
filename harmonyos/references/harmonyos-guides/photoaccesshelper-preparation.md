---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-preparation
title: 开发准备
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 受限开放能力 > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:37+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:29481a5f4be98aad852ca30c8a52c56d0f19f5b0ec2759694dc3dd34a6c52bbf
---

应用需获取相册管理模块实例，才能访问和修改相册中的媒体数据。相册管理模块涉及用户个人数据信息，应用需向用户申请读写权限，以保证功能的正常运行。使用相册管理模块接口时，如无其他注明，默认在工程代码的pages/index.ets或其他自定义的ets文件中使用。

## 获取相册管理模块实例

应用需要通过上下文[Context](application-context-stage.md)和接口[getPhotoAccessHelper](../harmonyos-references/arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)，获取相册管理模块实例，用于访问和修改相册中的媒体数据信息，如图片和视频。

**开发步骤**

1. 导入photoAccessHelper模块以使用相册管理模块相关接口。
2. 通过getUIContext().getHostContext()获取应用上下文。
3. 获取相册管理模块实例。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { common } from '@kit.AbilityKit';

4. // 此处获取的photoAccessHelper实例为全局对象，后续文档中使用到的地方默认为使用此处获取的对象，如未添加此段代码报未定义的错误请自行添加。
5. // 请在组件内获取context，确保this.getUiContext().getHostContext()返回结果为UIAbilityContext
6. @Entry
7. @Component
8. struct Index {
9. @State outputText: string = '支持的类型为：\n';

11. build() {
12. Row() {
13. Button('example').onClick(async () => {
14. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
16. }).width('100%')
17. }
18. .height('90%')
19. }
20. }
```

## 申请相册管理模块功能相关权限

相册管理模块的读写操作需要相应权限，在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。涉及的权限如下表。

| 权限名 | 说明 | 授权方式 |
| --- | --- | --- |
| ohos.permission.READ\_IMAGEVIDEO | 允许应用读取媒体库的图片和视频媒体文件信息。 | user\_grant |
| ohos.permission.WRITE\_IMAGEVIDEO | 允许应用读写媒体库的图片和视频媒体文件信息。 | user\_grant |
| ohos.permission.MEDIA\_LOCATION | 允许应用访问用户媒体文件中的地理位置信息。 | user\_grant |

以上权限的授权方式均为user\_grant（用户授权），即开发者在[module.json5配置文件](module-configuration-file.md)中配置对应的权限后，需要使用接口[abilityAccessCtrl.requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)去校验当前用户是否已授权。如果已授权，应用可以直接访问和修改目标对象；否则需要弹框向用户申请授权。

**开发步骤**

上述权限ohos.permission.READ\_IMAGEVIDEO和ohos.permission.WRITE\_IMAGEVIDEO为受控权限，通常是不允许三方应用申请的。如果有特殊场景需要使用，请提供相关申请材料到AppGallery Connect申请相应权限证书。申请前请参考[受限开放权限](restricted-permissions.md)，确保应用符合可申请的场景。然后再参考[申请受限权限](declare-permissions-in-acl.md)，完成受限开放权限的申请。

说明

即使用户曾经授予权限，应用在调用受此权限保护的接口前，也应该先检查是否有权限。不能把之前授予的状态持久化，因为用户在动态授予后还可以通过“设置”取消应用的权限。
