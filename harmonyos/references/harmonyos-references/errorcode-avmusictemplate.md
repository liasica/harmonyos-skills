---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avmusictemplate
title: 音频模板错误码
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > 错误码 > 音频模板错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:12:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a0d40754ea478cf39d221142b9fd83aa81c2b71b1972a5b0ab4e349b567f0a0
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 35000001 音频模板创建失败

**错误信息**

Failed to create the AVMusicTemplate.

**错误描述**

音频模板创建失败。

**可能原因**

媒体增强服务连接失败。

**处理步骤**

可以尝试重启设备。

## 35000002 音频模板控制器创建失败

**错误信息**

Failed to create the AVMusicTemplate controller.

**错误描述**

音频模板控制器创建失败。

**可能原因**

创建controller的参数sessionId不合法。

**处理步骤**

检查sessionId是否为空或者是否有创建过该sessionId对应的AVMusicTemplate的应用。

## 35000003 模板监听未注册

**错误信息**

Template listener not registered.

**错误描述**

模板监听未注册。

**可能原因**

模板监听注册失败。

**处理步骤**

1. 检查应用是否正常创建AVMusicTemplate实例。
2. 检查应用内其他核心功能是否出现了异常。

## 35000004 未注册模板控制器回调

**错误信息**

Controller callback not registered.

**错误描述**

未注册模板控制器回调。

**可能原因**

controller callback 注册失败。

**处理步骤**

1. 检查应用是否正常创建AVMusicTemplateController实例。
2. 检查应用内其他核心功能是否出现了异常。

## 35000005 音频模板不存在

**错误信息**

AVMusicTemplate does not exist.

**错误描述**

音频模板不存在。

**可能原因**

音频模板还未创建。

**处理步骤**

1. 检查应用是否正常创建AVMusicTemplate实例。
2. 检查应用内其他核心功能是否出现了异常。

## 35000006 模板控制器不存在

**错误信息**

AVMusicTemplateController does not exist.

**错误描述**

模板控制器不存在。

**可能原因**

AVMusicTemplateController不存在。

**处理步骤**

1. 检查应用是否正常创建AVMusicTemplateController实例。
2. 检查应用内其他核心功能是否出现了异常。

## 35000007 模板控制器已经存在

**错误信息**

AVMusicTemplateController already exists.

**错误描述**

模板控制器已经存在。

**可能原因**

AVMusicTemplateController已存在，不需要重复创建。

**处理步骤**

在一个应用进程内，一个sessionId对应一个AVMusicTemplateController，不需要重复创建。

## 35000008 音频模板管理服务不存在

**错误信息**

AVMusicTemplate Manager services do not exist.

**错误描述**

音频模板管理服务不存在。

**可能原因**

媒体增强服务启动失败。

**处理步骤**

可以尝试重启设备。

## 35000009 音频模板管理服务异常

**错误信息**

AVMusicTemplate Manager services exception.

**错误描述**

音频模板管理服务异常。

**可能原因**

媒体增强服务通信出现异常。

**处理步骤**

1. 检查应用内其他核心功能是否出现了异常。
2. 尝试重启设备。

## 350000010 数据超过了允许的最大传输容量

**错误信息**

The data exceeds the maximum allowable transmission capacity.

**错误描述**

数据超过了允许的最大传输容量。

**可能原因**

传输的数据超过允许传输的1MB容量限制。

**处理步骤**

针对超过1MB的数据采用分批传输。

## 350000011 数据写入错误，数据无效

**错误信息**

The data write error, data is invalid.

**错误描述**

写数据失败，数据不可用。

**可能原因**

数据写入失败。

**处理步骤**

检查待传输的数据是否存在不合法的属性或者值。

## 350000012 音频模板错误

**错误信息**

AVMusicTemplate error.

**错误描述**

音频模板错误。

**可能原因**

媒体增强服务的音频内容配置错误。

**处理步骤**

1. 检查应用是否正确配置了API接入参数并能够成功调用。
2. 检查应用内其他核心功能是否出现了异常。
