---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-overview
title: Media Library Kit 简介
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > Media Library Kit 简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:34+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2363fb9f2dc82196c2301f315cc4ccc7b158d0b229c9b669a215079716c6c204
---

Media Library Kit（媒体文件管理服务）提供了管理相册和媒体文件的能力，包括图片和视频，帮助应用快速构建图片和视频的展示与播放功能。

## 能力范围

通过Media Library Kit，开发者可以管理相册和媒体文件，包括创建相册、访问和修改相册中的媒体信息。

面向**所有应用**开放如下能力：

* 选择/保存媒体库资源
  + [使用Picker选择媒体库资源](photoaccesshelper-photoviewpicker.md)
  + [保存媒体库资源](photoaccesshelper-savebutton.md)
* 管理动态照片
  + [访问和管理动态照片资源](photoaccesshelper-movingphoto.md)
  + [使用MovingPhotoView播放动态照片](movingphotoview-guidelines.md)
* 使用Picker组件
  + [使用PhotoPicker组件访问图片/视频](component-guidelines-photoviewpicker.md)
  + [使用AlbumPicker组件访问相册列表](component-guidelines-albumpicker.md)
  + [使用RecentPhoto组件获取最近一张图片](component-guidelines-recentphoto.md)
  + [使用PhotoPicker推荐图片](smart-photopicker.md)
  + [使用PickerController将编辑后的图片替换原图](medialibrary-pickercontroller.md)

面向**三方应用受限**开放如下能力：

注意

受限开放的能力需要[申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)。这部分权限为受控开放，通常是不允许三方应用申请的。如果有特殊场景需要使用，请提供相关申请材料到AppGallery Connect申请相应权限证书。

* [媒体资源使用指导](photoaccesshelper-resource-guidelines.md)，包括：
  + 获取指定媒体资源。
  + 获取图片和视频缩略图。
  + 重命名媒体资源。
* [用户相册资源使用指导](photoaccesshelper-useralbum-guidelines.md)，包括：
  + 获取用户相册。
  + 重命名用户相册。
  + 添加图片和视频到用户相册中。
  + 获取用户相册中的图片和视频。
  + 从用户相册中移除图片和视频。
* [系统相册资源使用指导](photoaccesshelper-systemalbum-guidelines.md)，包括：
  + 收藏夹。
  + 视频相册。
* [媒体资源变更通知相关指导](photoaccesshelper-notify-guidelines.md)，包括：
  + 注册对指定URI的监听。
  + 取消指定URI的监听。

## 亮点/特征

* 对象化API设计，简洁高效，接入便捷。
* 端云一体化访问管理。
* 安全精准强管控，picker和保存控件自动授权。
* 智能格式转化，框架层统一完成转化。

## 框架原理

媒体库接收用户对媒体资产的获取与变更请求，进行请求合法性检查和权限校验，通过后与数据库进行交互，并返回请求结果。
