---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-34
title: 应用上架检测出未使用的权限
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用上架检测出未使用的权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:983891249c998aa25cda4adafbc3f8fe161353bda43dd8d828d2e6eddc0b1d44
---

## 问题现象

场景一：

代码中没有用到通讯录受限权限([ohos.permission.READ\_CONTACTS](../harmonyos-guides/restricted-permissions.md#ohospermissionread_contacts),[ohos.permission.WRITE\_CONTACTS](../harmonyos-guides/restricted-permissions.md#ohospermissionwrite_contacts))，但是上传app包时提示软件包内存在这个权限。

场景二：

应用上架的时候，应用市场反馈：

“app.hap的permission为用户授权权限但未配置reason和usedScene:ohos.permission.APP\_TRACKING\_CONSENT”。

对于未使用到的SDK权限，需要从app包中去除冗余。

## 背景知识

* 应用存在收集用户的个人信息或权限的行为（通讯录），但未在应用内的隐私政策/在AppGallery Connect上提交的隐私政策网址中进行说明。不符合华为应用市场《审核指南》第7.11项。
* [removePermissions](../harmonyos-guides/ide-hvigor-build-profile-app.md#section99591415322)：removePermissions是一个对象数组，用于编译HAP/HSP模块时，指定需要删除的依赖包中的冗余权限，模块本身的权限不会被删除。

## 问题定位

1. 排查app包内的[module.json5](../harmonyos-guides/module-configuration-file.md)文件，看是否误填了未使用的权限。如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/-yYya0NrQ2a8ku_OefFzAA/zh-cn_image_0000002628394608.png "点击放大")
2. 排查引用的三方库是否使用了此权限。比如在项目工程目录oh\_modules下，依次在引用三方库的module.json5文件中查看“requestPermissions”字段，以此排查应用申请权限属于哪个三方库。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/auvoMM59Q-W6K8n1Yl4rwg/zh-cn_image_0000002628554496.png "点击放大")
3. 验证权限是否与功能场景匹配，避免声明未使用的敏感权限（如通讯录、位置等）。
4. 排查是否使用了已废弃权限，例如[ohos.permission.WRITE\_MEDIA](../harmonyos-guides/permissions-for-all-user.md#ohospermissionwrite_media)权限。需要根据文档说明使用替换方案。

## 分析结论

项目中有三方库使用该权限。

## 修改建议

1. 使用removePermissions删除三方库中未使用权限。

   IDE使用API15 beta2以上版本：[下载链接](https://developer.huawei.com/consumer/cn/download/)。

   build-profile.json5新增[removePermissions](../harmonyos-guides/ide-hvigor-build-profile-app.md#section99591415322)字段，在编译时将删除指定的依赖包中的冗余权限，而模块本身的权限不会被删除，仅对hap/hsp模块生效。
2. 查看三方库最新版本是否更新移除了该权限，如果去掉，可以更新到最新版。

## 常见FAQ

Q：在UniApp工程应该如何去配置removePermissions字段呢？

A：在harmony-configs文件夹下放一个自定义的build-profile.json5文件，在build-profile.json5文件添加removePermissions字段即可。
