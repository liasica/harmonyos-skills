---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-font-manager
title: 字体管理错误码
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > 错误码 > 字体管理错误码
category: harmonyos-references
scraped_at: 2026-11-12T09:55:15+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:636c719586b50068496e4d268392fbf628c3b610f255e9e22313876571341fd6
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 31100101 字体文件不存在

**错误信息**

The font does not exist.

**错误描述**

传入的字体文件路径不存在。

**可能原因**

字体文件路径输入错误。

**处理步骤**

检查并确保传入的文件格式为.ttf或.ttc，且路径准确。

## 31100102 字体文件不支持安装

**错误信息**

The font is not supported.

**错误描述**

传入的文件路径，不是字体文件，导致安装失败。

**可能原因**

1. 传入的文件，不是.ttf或.ttc字体文件类型。
2. 文件内容不符合字体文件格式规范。

**处理步骤**

检查并确保传入.ttf或.ttc格式的文件。

## 31100103 字体文件拷贝失败

**错误信息**

Failed to copy the font file.

**错误描述**

安装时，字体文件拷贝失败。

**可能原因**

字体安装时出现拷贝异常。

**处理步骤**

请重试或者重启设备后重试。

## 31100104 字体文件已安装

**错误信息**

The font file is installed.

**错误描述**

传入的字体文件已经安装。

**可能原因**

传入的字体已经安装过，字体名称重复。

**处理步骤**

卸载已有同名字体，重新安装。

## 31100105 已安装字体文件超过最大数量

**错误信息**

Exceeded the maximum number of installed files.

**错误描述**

已安装的字体文件数量超过最大数量。

**可能原因**

安装的字体文件个数超过最大数量限制。

**处理步骤**

请先卸载不需要的字体文件，再重试。

## 31100106 其他错误导致安装失败

**错误信息**

The system ability works abnormally.

**错误描述**

安装字体时出现系统错误，导致安装失败。

**可能原因**

在进行安装时，系统出现异常。

**处理步骤**

请重试或者重启设备后重试。

## 31100107 卸载的字体文件不存在

**错误信息**

The font file does not exist.

**错误描述**

要卸载的字体文件不存在。

**可能原因**

要卸载的字体文件并未安装或者传入的字体文件名称不正确。

**处理步骤**

请检查传入的字体名称是否正确，请更正后重试。

## 31100108 无法删除字体

**错误信息**

Failed to delete the font file.

**错误描述**

卸载字体时删除字体文件失败。

**可能原因**

在进行卸载时，系统出现异常。

**处理步骤**

请重试或者重启设备后重试。

## 31100109 其他错误导致卸载失败

**错误信息**

The system ability works abnormally.

**错误描述**

卸载字体时出现系统错误，导致卸载失败。

**可能原因**

在进行卸载时，系统出现异常。

**处理步骤**

请重试或者重启设备后重试。

## 31100110 系统异常导致接口调用失败

**错误信息**

Call failed due to system error.

**错误描述**

系统服务出现异常，接口调用失败。

**可能原因**

在启动数据迁移任务时，系统出现异常。

**处理步骤**

请重新操作或重启设备后再操作。

## 31100111 迁移任务执行中

**错误信息**

Data migration is in progress.

**错误描述**

数据迁移任务正在执行中，不可重复启动。

**可能原因**

数据迁移任务正在执行中。

**处理步骤**

不可重复启动迁移任务，请等待当前任务执行完毕。

## 31100112 Scope字体未找到

**错误信息**

The scope font is not found.

**错误描述**

卸载或查询字体时，未找到指定字体路径（url）对应的字体记录。

**可能原因**

未安装该字体或字体路径（url）输入错误。

**处理步骤**

请检查应用是否安装此字体，以及检查字体路径（url）是否正确。

## 31100113 字体服务状态监听器已注册

**错误信息**

The font observer is already registered.

**错误描述**

字体服务状态监听器已注册，不可重复注册。

**可能原因**

同一应用重复调用[fontManager.onFontObserver](js-apis-font-manager.md#fontmanageronfontobserver)注册字体服务状态监听器。

**处理步骤**

无需重复注册，如需更新字体服务状态监听器，请先调用[fontManager.offFontObserver](js-apis-font-manager.md#fontmanagerofffontobserver)注销后再重新注册。

## 31100114 超过字体服务状态监听器最大数量

**错误信息**

The maximum number of font observers has been reached.

**错误描述**

同一用户下注册的字体服务状态变化监听器数量超过最大限制（5个）。

**可能原因**

同一用户下已有5个不同应用注册了字体服务状态变化监听器。

**处理步骤**

请等待其他应用注销字体服务状态变化监听器后再重试。

## 31100115 字体服务状态变化监听器未注册

**错误信息**

The font observer is not registered.

**错误描述**

安装应用级字体或注销字体服务状态变化监听器时，该字体服务状态变化监听器未注册。

**可能原因**

1. 调用[fontManager.installScopeFont](js-apis-font-manager.md#fontmanagerinstallscopefont)接口安装应用级字体时，未先调用[fontManager.onFontObserver](js-apis-font-manager.md#fontmanageronfontobserver)接口注册字体服务状态变化监听器。
2. 调用[fontManager.offFontObserver](js-apis-font-manager.md#fontmanagerofffontobserver)接口注销字体服务状态变化监听器时，未注册监听器或监听器已被注销。

**处理步骤**

1. 调用[fontManager.installScopeFont](js-apis-font-manager.md#fontmanagerinstallscopefont)接口安装应用级字体前，需先调用[fontManager.onFontObserver](js-apis-font-manager.md#fontmanageronfontobserver)接口注册字体服务状态变化监听器。
2. 调用[fontManager.offFontObserver](js-apis-font-manager.md#fontmanagerofffontobserver)接口注销字体服务状态变化监听器前，需确保已注册监听器且未被注销。
