---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-display
title: 屏幕错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > 图形图像 > 屏幕错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0f95c2531d7e44fa5503dda567714e25d2e868dffeb10f35cdd984caa4fa82a0
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1400001 无效的显示设备

PhonePC/2in1TabletTVWearable

**错误信息**

Invalid display or screen.

**错误描述**

当操作无效的显示设备，包括虚拟屏时，会报此错误码。

**可能原因**

1. 虚拟屏未创建。
2. 虚拟屏已销毁。

**处理步骤**

1. 在操作虚拟屏前，检查该虚拟屏是否已经存在，确保已创建该虚拟屏。
2. 在操作虚拟屏前，检查虚拟屏是否已被销毁，确保其未被销毁，再进行相关操作。

## 1400003 系统服务工作异常

PhonePC/2in1TabletTVWearable

**错误信息**

This display manager service works abnormally.

**错误描述**

当系统服务工作异常时，会报此错误码。

**可能原因**

1. 屏幕管理服务没有正常启动。
2. 底层图形图像合成渲染异常。

**处理步骤**

系统服务内部工作异常，请稍候重试，或者重启设备尝试。

## 1400004 参数异常

PhonePC/2in1TabletTVWearable

**错误信息**

Parameter error.

**错误描述**

当传入参数异常时，会报此错误码。

**可能原因**

参数的值超出允许的范围。

**处理步骤**

在对屏幕进行操作前，检查传入参数是否有效，确保参数有效再进行相关操作。
