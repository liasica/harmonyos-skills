---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-163
title: HarmonyOS媒体库相关权限申请及配置
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > HarmonyOS媒体库相关权限申请及配置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:7a1248bd1078de10910893ee720d2993df124b7237c5055d4e5d966bd1cd5de6
---

## 问题现象

媒体开发过程中，媒体库受限开放权限应该如何申请？

## 背景知识

应用在访问数据或者执行操作时，需要评估该行为是否需要应用具备相关的权限。如果确认需要目标权限，则需要在应用安装包中申请目标权限，开发者可以依据下述流程图判断是否可以申请[受限权限](../harmonyos-guides/restricted-permissions.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/2_QJ3DTqR1yyuCUG7k5BeQ/zh-cn_image_0000002628631568.png "点击放大")

## 解决方案

1. 媒体文件相关权限列表：

   | 权限 | 权限内容 | 可申请此权限的特殊场景与功能 |
   | --- | --- | --- |
   | [ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionshort_term_write_imagevideo) | 短时授权，允许应用保存图片、视频到用户公共目录。 | 应用无法使用安全保存控件，例如H5网页应用等。  存在连续多次保存图片/视频的场景，无法使用保存确认弹框，一次保存多个图片/视频。 |
   | [ohos.permission.READ\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionread_imagevideo) | 允许读取用户公共目录的图片或视频文件。 | 应用需要克隆、备份或同步图片/视频类文件。 |
   | [ohos.permission.WRITE\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionwrite_imagevideo) | 允许修改用户公共目录的图片或视频文件。 | 应用需要克隆、备份或同步图片/视频类文件。  应用内包含拍照和录制场景，且应用属于典型的拍照应用。无法使用安全控件或授权弹窗保存图片。 |
   | [ohos.permission.MEDIA\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmedia_location) | 允许应用访问用户媒体文件中的地理位置信息。 | / |
2. 权限申请原因需要具体阐述基于什么应用场景才需要申请相应权限，如果缺失该权限会导致哪些业务场景无法闭环。开发者需要从权限使用的业务场景出发进行原因描述，而非强调功能设计方案，具体申请原因可参考：
   * SHORT\_TERM\_WRITE\_IMAGEVIDEO：需要具体阐述为什么不能使用保存控件和授权弹窗的方式，应用内存在怎样的用户使用场景需要在短时间内保存多张图片，使用弹窗授权方案多次弹窗影响用户体验。
   * ohos.permission.READ\_IMAGEVIDEO：应用存在克隆备份场景，需要在不同设备之间同步媒体文件，无法通过PhotoPicker访问媒体文件。
   * ohos.permission.WRITE\_IMAGEVIDEO：
     + 应用存在克隆备份场景，需要将其他设备/云端的媒体文件数据同步到本地；
     + 应用是拍照类的应用，存在需要在拍照、录制视频之后直接存入图库的场景；
     + 由于使用了不支持安全控件的开源框架，无法使用安全控件，同时应用内存在某些使用场景需要对媒体文件进行修改。
   * MEDIA\_LOCATION：基于某个具体的场景，需要获取到应用图片中的位置信息。

3. 权限审批完成后，在AGC侧申请Profile文件用于后续的应用签名信息配置，在module.json5配置文件的requestPermissions标签中[声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)，权限申请相关配置参数如表：

| 属性 | 含义 | 数据类型 |
| --- | --- | --- |
| name | 使用的权限名称。 | string |
| reason | 申请权限的原因。 | string |
| usedScene | 权限使用的场景，该字段用于应用上架校验。包括abilities和when两个子项。abilities是使用权限的UIAbility或者ExtensionAbility组件的名称；when是权限调用时机。 | 对象 |

4. 在UIAbility中向用户申请授权，调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)拉起弹框请求用户授权。如果用户拒绝授权，将无法再次拉起弹框，需要用户在系统应用“设置”的界面中，手动授予权限。或是调用[requestPermissionOnSetting](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，拉起权限设置弹框，引导用户授权。需要注意的是，在进行权限申请之前，需要先检查当前应用程序是否已经被授予权限。参考[向用户申请授权](../best-practices/bpta-permission-application.md#section1816918297167)。

## 常见FAQ

Q：如果用户已拒绝权限，再次请求权限需要跳转设置页面，那这个跳转路径是什么？

A：跳转系统设置的各级页面Want参数需指定bundleName与abilityName，如需跳转设置相关子页面，除了指定bundleName与abilityName外，通常还需要填写对应uri与parameters，参考[跳转到系统设置](../harmonyos-guides/system-app-startup.md#设置)。

Q：申请受限权限的克隆，备份或同步的场景是哪些？

A：克隆的场景，如换机场景；备份或同步的场景，如云端备份、同步。

## 总结

受限权限需要在应用市场申请权限，权限申请流程繁琐。在开发测试阶段建议使用不需要权限的替代方案，常见情况如保存图片到相册可以使用[安全控件](../harmonyos-guides/photoaccesshelper-savebutton.md#使用安全控件保存媒体库资源)或[弹窗授权](../harmonyos-guides/photoaccesshelper-savebutton.md#使用弹窗授权保存媒体库资源)进行保存，相册管理可以使用[photoAccessHelper](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#photoaccesshelper)进行相册图片选择等。
