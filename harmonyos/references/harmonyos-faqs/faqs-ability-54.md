---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-54
title: 如何实现通过调用其他已安装的应用来打开特定文件
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何实现通过调用其他已安装的应用来打开特定文件
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8bd97871a46cc24c480d3c48d0baf7855319d6020e84f86b569e83d38ff13816
---

开发者可以通过使用隐式Want机制来调用其他应用打开文件。通过设置合适的携带的数据（uri）、MIME type类型（type）、处理Want的方式（flag）等字段，以便系统能够识别并弹出一个选择框，让用户选择合适的应用来打开文件，若仅匹配到一个应用，则会直接拉起该应用。

效果示意如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/abfVz1ESRdm1NBmVsRscSA/zh-cn_image_0000002194158992.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061501Z&HW-CC-Expire=86400&HW-CC-Sign=1F91EB2A9954A20FB50DCA05E6331FD6033A35B5D3C02BE86C35E76CF46686FD "点击放大")

**调用方**

1. 导入所需模块。

   ```
   1. import common from '@ohos.app.ability.common';
   2. import Want from '@ohos.app.ability.Want';
   3. import wantConstant from '@ohos.app.ability.wantConstant';
   4. import { BusinessError } from '@ohos.base';
   ```

   [StartAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/StartAbility.ets#L21-L24)
2. 构造请求数据。

   ```
   1. // Construct request data Want, taking opening a Word file as an example
   2. let wantInfo: Want = {
   3. uri: 'file://.../test.docx', // Indicate the URI path of the file to be opened, usually used in conjunction with type
   4. type: 'application/msword', // Indicate the type of file to be opened
   5. flags: wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION, // Authorization to perform write operations on URI
   6. }
   ```

   [StartAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/StartAbility.ets#L28-L33)
3. 调用接口启动。

   ```
   1. // Call the startAbility interface to open files
   2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. context.startAbility(wantInfo).then(() => {
   4. // ...
   5. }).catch((err: BusinessError) => {
   6. // ...
   7. })
   ```

   [StartAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/StartAbility.ets#L42-L48)

**目标方**

在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中注册文件打开能力。

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. // ...
7. "skills": [
8. {
9. "actions": [
10. "ohos.want.action.viewData" // Declaration of Data Processing Capability
11. ],
12. "uris": [
13. {
14. // Allow opening Word files in URI that start with the file://protocol to identify the local file
15. "scheme": "file",
16. "type": "application/msword", // Indicates supported file types for opening
17. "linkFeature": "FileOpen" // The function of this URI is to open files
18. }
19. // ...
20. ]
21. // ...
22. }
23. ]
24. }
25. ]
26. }
27. }
```

[module\_startability.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/module_startability.json5#L6-L32)

目标方应用在应用市场上架时会进行审核。

**参考链接**

[隐式Want匹配原理](../harmonyos-guides/explicit-implicit-want-mappings.md#隐式want匹配原理)
