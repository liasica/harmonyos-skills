---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/medialibrary-asset-judgment-faq
title: 如何正确判断媒体资源类型
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > Media Library Kit常见问题 > 如何正确判断媒体资源类型
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6d22ab80c8363a5ee9b82b01b74222ea03ccf234042ff2a9e5fdbb0a52353cfc
---

[Media Library Kit](photoaccesshelper-overview.md)（媒体文件管理服务）提供了媒体资源的管理能力，开发者可以访问和管理相册中的媒体信息。针对不同的媒体资源类型，系统会提供相应的判断方式，本文档提供了相关示例方法以便开发者使用。

## 使用mimeType字段来判断资源类型

开发者可以通过判断mimeType的字符串前缀来区分媒体类型，具体判断方式如下：

* 当mimeType以'image/'开头时，表示该媒体文件为图片。
* 当mimeType以'video/'开头时，表示该媒体文件为视频。

**示例：**

```typescript
function getMediaTypeByMimeType(mimeType: string): string {
  if (mimeType.startsWith('video/')) {
    return 'video';
  } else if (mimeType.startsWith('image/')) {
    return 'image';
  }
  return 'unknown';
}
```

## 通过URI判断连拍图资源

未重命名连拍照片的URI中包含特定标识，开发者可以通过检查URI中的关键字来判断是否为连拍图资源。

* 当URI同时包含burst和cover时，表示该资源为连拍封面。
* 当URI仅包含burst时，表示该资源为连拍照片（非封面）。
* 当URI中不包含burst关键字时，表示该资源为非连拍图。

**示例：**

```typescript
function getBurstTypeByUri(uri: string): string {
  const hasBurst = uri.includes('burst');
  const hasCover = uri.includes('cover');
        
  if (hasBurst && hasCover) {
    return '连拍封面';
  } else if (hasBurst) {
    return '连拍照片';
  }
  return '非连拍图';
}
```
