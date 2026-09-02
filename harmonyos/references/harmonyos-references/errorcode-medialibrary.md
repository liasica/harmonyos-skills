---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-medialibrary
title: 媒体库错误码
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > 错误码 > 媒体库错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:adc9f63da5c5b337e349d0660b506c1ce1759f68c198170ec187f3be38942987
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 23800301 系统内部错误

**错误信息**

MediaLibrary inner fail.

**错误描述**

媒体库内部错误。

**可能原因**

1. 创建构造函数引用失败（Failed to create reference）。
2. 实例创建失败（Failed to create instance）。
3. 无法获取undefined值（Failed to get undefined value）。
4. 回调信息获取失败（Failed to get callback info）。
5. 无法将原生对象绑定到JS对象（Failed to bind native object to JavaScript object）。
6. 原生对象解包失败（Failed to unwrap native object）。
7. 布尔值创建失败（Failed to create Boolean value）。
8. int32值获取失败（Failed to get int32 value）。
9. 返回数据初始化失败（Failed to initialize data field）。
10. 返回错误信息初始化失败（Failed to initialize error field）。
11. 获取参数类型失败（Failed to get argument type）。
12. 参数类型校验失败（Failed to check argument type）。
13. 创建PhotoAlbumNapi失败（Failed to create PhotoAlbumNapi）。
14. JS对象添加属性失败（Failed to add property）。
15. 无法获取提取选项（Failed to get fetch option）。
16. 无效的相册列（Invalid fetch columns）。
17. 数组类型校验失败（Failed to check array type）。
18. 获取数组长度失败（Failed to get array length）。
19. 获取数组元素失败（Failed to get array element）。

**处理步骤**

清理后台或重启设备。

## 23800151 场景参数校验不通过

**错误信息**

Invalid parameter.

**错误描述**

参数异常。

**可能原因**

1. 必选参数范围不满足要求。
2. 传入的记录已存在。
3. 传入的记录数量超过最大数量。

**处理步骤**

检查参数赋值或者参数长度。

## 23800104 传入参数校验不通过

**错误信息**

Invalid input parameter.

**错误描述**

参数异常。

**可能原因**

参数不在[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)枚举范围之内。

**处理步骤**

检查传入参数是否在PhotoKeys枚举范围之内。

## 23800202 非法场景调用错误

**错误信息**

Invalid call context. Possible causes: 1. The API is called outside the photo browsing scenario. 2. The API is called when isMovingPhotoBadgeShown is already set to true.

**错误描述**

非法场景调用错误。

**可能原因**

1. 在非全图浏览场景下调用该接口。
2. 在已经配置[BaseSelectOptions.isMovingPhotoBadgeShown](arkts-apis-photoaccesshelper-class.md#baseselectoptions)为true的情况下调用该接口。

**处理步骤**

检查接口[setMovingPhotoState](ohos-file-photopickercomponent.md#setmovingphotostate23)的使用场景。
