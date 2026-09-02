---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-car
title: ArkTS API错误码
breadcrumb: API参考 > 系统 > 硬件 > Car Kit（车服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:11+08:00
doc_updated_at: 2026-06-13
content_hash: sha256:2c53af5565e4e1278cb597c6315aa83ca21f2e46d9e9d2ec01be0b500aa1d915
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1003810001 参数值无效

**错误信息**

Invalid parameter value.

**错误描述**

无效的参数值。

**可能原因**

1. 设置导航状态时目的地名称长度或途经点名称长度超出1024字节。
2. 设置导航元数据时当前道路名或下一次进入的道路名的长度超出1024字节。
3. 参数值超出范围，比如设置导航状态时经纬度值不在有效范围（纬度值的数值范围是[-90, 90]，经度值的有效范围是[-180, 180]）内。

**处理步骤**

在设置导航状态、导航元数据时请确保参数传递正确。

## 1003810002 所有参数总大小超出限制

**错误信息**

The total size of all parameters exceeds the limit.

**错误描述**

所有参数总大小超出了限制。

**可能原因**

1. 设置导航状态时添加的途经点太多。
2. 设置导航元数据时当传入路口放大图时参数总大小可能会超出限制（200Kbytes）。

**处理步骤**

1. 设置导航状态时检查添加途经点的数量，确保途经点的数量不超出20个。
2. 设置导航元数据时如果要传入路口放大图，并且图片较大时，建议对图片做压缩处理。
