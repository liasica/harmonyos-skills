---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pdf
title: ArkTS API 错误码
breadcrumb: API参考 > 应用服务 > PDF Kit（PDF服务） > ArkTS API 错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:03:06+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6425c0b3390737e7fecc298c54faf1470eabbd813d700eee93550fc9bc1faa9d
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1011301001 数组大小不匹配

**错误信息**

The arrays of pageIndices and matrices do not match.

**错误描述**

pageIndices和matrices两个数组的长度不一致。

**可能原因**

pageIndices和matrices数组长度不一致。

**处理步骤**

确保[pageIndices](pdf-arkts-pdfservice.md#getpixelmapwithpages)和[matrices](pdf-arkts-pdfservice.md#getpixelmapwithpages)数组长度一致。

## 1011301002 页码值超出范围

**错误信息**

Invalid page number.

**错误描述**

pageIndices中的页码值不在合理范围。

**可能原因**

1. 页码值小于0。
2. 页码值大于等于PDF总页码数。
3. pageIndices的总页码数超过16。

**处理步骤**

确保pageIndices中的页码值大于等于0且小于总页数，总页码数不超过16。

## 1011301003 尺寸超出最大值

**错误信息**

The number of pixels in the bitmap exceeds the upper limit.

**错误描述**

位图中的像素数量超过上限。

**可能原因**

位图尺寸（bitmapWidth × bitmapHeight）对应的像素数超过250M。

**处理步骤**

确保位图尺寸（bitmapWidth × bitmapHeight）对应的像素数不超过250M。

## 1011301004 创建bitmap失败

**错误信息**

Failed to create a bitmap.

**错误描述**

创建bitmap失败。

**可能原因**

系统资源不足。

**处理步骤**

1. 减少渲染页数，将多页批量渲染拆分为单页或少量页面依次渲染。
2. 关闭不用的PDF文档实例、清理图片缓存。
3. 尝试减小bitmapWidth或bitmapHeight的值，减少占用内存。

## 1011301005 bitmap渲染失败

**错误信息**

Failed to render the bitmap.

**错误描述**

bitmap渲染失败。

**可能原因**

PDF文档不完整。

**处理步骤**

1. 使用PDF阅读器打开文件，确认文件能否正常显示。
2. 对比原文件和传输/复制后的文件大小，确保一致。

## 1011301006 PDF文档未加载

**错误信息**

The PDF document is not loaded.

**错误描述**

PDF文档未加载，无法访问指定的PDF文档。

**可能原因**

文档尚未通过初始化流程加载或加载过程中断。

**处理步骤**

调用[loadDocument](pdf-arkts-pdfservice.md#loaddocument)，重新触发加载过程。

## 1011302001 页码值错误

**错误信息**

Invalid page number.

**错误描述**

[loadDocumentFromMemory](pdf-arkts-pdfviewmanage.md#loaddocumentfrommemory)传入的initPageIndex页码值参数不在合理范围。

**可能原因**

1. 页码值小于0。
2. 页码值为Infinity。
3. 页码值为NaN。

**处理步骤**

确保initPageIndex页码值为自然数。

## 1011302002 加载的文档未释放

**错误信息**

The loaded document has not been freed.

**错误描述**

当前有加载的文档没有被释放。

**可能原因**

使用[loadDocumentFromMemory](pdf-arkts-pdfviewmanage.md#loaddocumentfrommemory)接口成功加载文档二进制数据流后，未调用releaseDocument进行文档释放，在同一个controller再次加载文档二进制数据流

**处理步骤**

调用releaseDocument接口释放当前controller加载的文档二进制数据流。

## 1011302003 加载的二进制流为空或超出范围

**错误信息**

The input ArrayBuffer is empty or exceeds the maximum limit.

**错误描述**

当前[loadDocumentFromMemory](pdf-arkts-pdfviewmanage.md#loaddocumentfrommemory)接口加载的二进制数据流为空或超出接口支持的最大大小。

**可能原因**

1. 当前加载的二进制数据流为空。
2. 当前加载的二进制数据流大小超过1GB的最大支持范围。

**处理步骤**

1. 确保传入的二进制数据流为有内容的数据流。
2. 检查传入的二进制数据流大小，确保数据流大小不超过1GB。

## 1011302004 渲染忙碌

**错误信息**

The rendering thread is busy.

**错误描述**

渲染忙碌。

**可能原因**

距离上一次调用本接口的时间过短，小于300ms。

**处理步骤**

等待300ms后再进行下一次调用。

## 1011302005 无效渲染模式

**错误信息**

Unknown rendering mode.

**错误描述**

无效渲染模式。

**可能原因**

[setRenderMode](pdf-arkts-pdfviewmanage.md#setrendermode)传入参数值越界，不在规定范围内。

**处理步骤**

重新设置参数约束，仅允许传入预定义的枚举值。

## 1011302006 加载忙碌

**错误信息**

Another document is being loaded.

**错误描述**

当前有未完成的异步加载任务，无法加载当前文档。

**可能原因**

短时间内并发调用了异步加载接口。

**处理步骤**

检查调用逻辑，避免连续调用异步加载接口。
