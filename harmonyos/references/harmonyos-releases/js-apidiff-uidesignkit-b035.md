---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-b035
title: UI Design Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:34+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:605b852d32dbb89b306bac1a00061bd9859c752be44c5d2e45842733fa22f25a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：hdsDrawable；  API声明：function getHdsLayeredIconAsync(bundleName: string, layeredDrawableDescriptor: LayeredDrawableDescriptor, size: number, hasBorder?: boolean): Promise<image.PixelMap>;  差异内容：function getHdsLayeredIconAsync(bundleName: string, layeredDrawableDescriptor: LayeredDrawableDescriptor, size: number, hasBorder?: boolean): Promise<image.PixelMap>; | api/@hms.hds.hdsDrawable.d.ts |
| 新增API | NA | 类名：hdsDrawable；  API声明：function getHdsIconAsync(bundleName: string, pixelMap: image.PixelMap, size: number, mask: image.PixelMap, hasBorder?: boolean): Promise<image.PixelMap>;  差异内容：function getHdsIconAsync(bundleName: string, pixelMap: image.PixelMap, size: number, mask: image.PixelMap, hasBorder?: boolean): Promise<image.PixelMap>; | api/@hms.hds.hdsDrawable.d.ts |
