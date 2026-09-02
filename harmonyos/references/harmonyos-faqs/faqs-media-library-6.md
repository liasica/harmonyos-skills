---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-6
title: 编辑富文本文件时，无法显示插入的视频文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 编辑富文本文件时，无法显示插入的视频文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b889f90e44eca3ffcb987146178f53c841a82564a7e6b819ca747f2f9d58c6c
---

## 问题现象

用户在应用中编辑一个富文本格式的文件时，插入一个视频文件。但是，在选择了一个视频文件后，当前编辑界面无法显示插入的视频文件。界面上，显示load file failed，或者视频预览界面为空白。

## 背景知识

* [Media Library Kit 简介](../harmonyos-guides/photoaccesshelper-overview.md)：Media Library Kit（媒体文件管理服务）提供了管理相册和媒体文件的能力，包括照片和视频，帮助应用快速构建图片和视频的展示与播放功能。
* [媒体资源使用指导](../harmonyos-guides/photoaccesshelper-resource-guidelines.md)：应用可以通过photoAccessHelper的接口，对媒体资源（图片、视频）进行相关操作。
* [用户相册资源使用指导](../harmonyos-guides/photoaccesshelper-useralbum-guidelines.md)：photoAccessHelper提供用户相册相关的接口，支持创建和删除相册，以及添加和删除相册中的图片和视频资源。
* [视频相册](../harmonyos-guides/photoaccesshelper-systemalbum-guidelines.md#视频相册)：视频相册属于系统相册，用户文件中属于视频类型的媒体文件会自动加入到视频相册中。

## 问题定位

1. 确认应用是否有读取用户相册、视频相册的权限。如果确认应用有读取图片/视频的权限，则转步骤2，检查应用读取视频的文件路径地址信息。方法，检查module.json5配置文件的requestPermissions标签中声明权限。

   | 属性 | 含义 | 数据类型 | 取值范围 |
   | --- | --- | --- | --- |
   | name | 需要使用的权限名称。 | 字符串 | 必填，需为系统已定义的权限，取值范围请参考[应用权限列表](../harmonyos-guides/app-permissions.md)。 |
   | reason | 申请权限的原因。 | 字符串 | 可选填写，该字段用于应用上架校验，当申请的权限为user\_grant权限时必填，并且需要进行多语种适配。 使用string类资源引用。格式为$string: \*\*\*。可参考[权限使用理由的文案内容规范](../harmonyos-guides/declare-permissions.md#权限使用理由的文案内容规范)。 |
   | usedScene | 权限使用的场景，该字段用于应用上架校验。包括abilities和when两个子项。abilities：使用权限的UIAbility或者ExtensionAbility组件的名称。 when：调用时机。 | 对象 | usedScene必填。 abilities：可选填写，可以配置为多个UIAbility或者ExtensionAbility名称的字符串数组。when：可选填写，但如果配置此字段，只能填入固定值inuse（使用时）、always（始终），不能为空。当申请的权限为user\_grant权限时建议填写。 |

   如果不是使用Picker，则需以下权限：

   | 权限名 | 说明 | 授权方式 |
   | --- | --- | --- |
   | ohos.permission.READ\_IMAGEVIDEO | 允许应用读取媒体库的图片和视频媒体文件信息。 | user\_grant |
   | ohos.permission.WRITE\_IMAGEVIDEO | 允许应用读写媒体库的图片和视频媒体文件信息。 | user\_grant |
2. 确认应用读取的文件路径地址，可以通过Hilog日志文件查看。例如，如下日志中：

   ```txt
   06-10 16:35:02.444 [picker] result: {"resultCode":0."uris": ["file://media/Photo/7/VID_1748483794_002/SVID_20250529_095454_1.mp4"],"isOrigin":false}
   ```

   ```txt
   06-10 16:35:02.445 [GetRealPath:156] GetRealPath uri is ,<private>
   ```

   ```txt
   06-10 16:35:02.444 [picker] selectresult: {"data":{"photoUris":["file://media/Photo/7/VID_1748483794_002/SVID_20250529_095454_1.mp4"],"isOriginalPhoto":false}
   ```

   通过日志，可以确认在读取文件地址的时候获取的路径出错。

## 分析结论

| 步骤 | 分析步骤 | 分析结论 |
| --- | --- | --- |
| 步骤1 | 检查应用使用相册的权限 | 如果无权限，则确认为权限问题。如果有权限，则转下一步。 |
| 步骤2 | 检查获取文件的路径 | 获取文件路径异常，确认获取文件地址出错。 |

## 修改建议

* 建议[使用Picker选择媒体库资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md)，此接口本身无需申请权限，目前适用于界面UIAbility，使用窗口组件触发。
* [使用PhotoPicker组件访问图片/视频](../harmonyos-guides/component-guidelines-photoviewpicker.md)，当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。
* [申请相册管理模块功能相关权限](../harmonyos-guides/photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)：应用需要先获取相册管理模块实例，才能访问和修改相册中的媒体数据信息。相册管理模块的读写操作需要相应权限，在申请权限前，请保证符合权限使用的基本原则。
* [在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)，应用需要在module.json5配置文件的requestPermissions标签中声明权限。
* [指定媒体文件名获取图片或视频资源](../harmonyos-guides/photoaccesshelper-resource-guidelines.md#指定媒体文件名获取图片或视频资源)。
* [获取用户相册中的图片和视频](../harmonyos-guides/photoaccesshelper-useralbum-guidelines.md#获取用户相册中的图片和视频)，先获取用户相册对象，然后调用Album.getAssets接口获取用户相册中的图片资源。
* [获取视频相册中的视频](../harmonyos-guides/photoaccesshelper-systemalbum-guidelines.md#获取视频相册中的视频)：先获取视频相册对象。然后调用Album.getAssets接口获取视频相册对象中的视频资源。
