---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm
title: 模块描述
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > ArkTS API > @ohos.multimedia.drm (数字版权保护) > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T08:12:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:693fb8e850d14152a5974b83f4fe2c0c72c050df2cd71955553bb8bf238bb009
---

DRM（Digital Rights Management）框架组件支持音视频媒体业务数字版权管理功能的开发。开发者可以调用系统提供的DRM插件，完成以下功能：

* DRM证书管理：生成证书请求、设置证书响应，实现对证书Provision（下载）功能。
* DRM媒体密钥管理：生成媒体密钥请求、设置媒体密钥响应、管理离线媒体密钥功能。
* DRM节目授权：支持DRM插件根据媒体密钥权限对DRM节目授权。
* DRM节目解密：支持媒体播放功能的解密调用，实现对DRM节目的解密。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```
1. import { drm } from '@kit.DrmKit';
```
