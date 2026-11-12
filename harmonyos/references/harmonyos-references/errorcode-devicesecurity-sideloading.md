---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-sideloading
title: Sideloading（侧载安全管控）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > ArkTS API错误码 > Sideloading（侧载安全管控）
category: harmonyos-references
scraped_at: 2026-11-12T09:55:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4b7382e93a5f9e7aebd1de31b40a18f9cedf692de3eb36a8ceb5e7953930ddf7
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1006205000 内部错误

**错误信息**

Internal error. Possible causes: 1.System is busy or resources are insufficient; 2.Abnormal system environment. Please try again later, you can check the logs for more information.

**错误描述**

侧载安全管控内部错误。

**可能原因**

1. 系统繁忙或资源不足。
2. 系统环境异常。

**处理步骤**

请稍后重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

## 1006205001 参数无效

**错误信息**

Invalid parameter.

**错误描述**

非法参数。

**可能原因**

1. 必填参数为null或undefined。
2. 确保沿用应用原有的上下文。

**处理步骤**

请检查传入的context参数，确保沿用应用原有的context。

## 1006205002 侧载安全管控不支持

**错误信息**

Sideloading is not supported.

**错误描述**

当前设备或系统不支持侧载安全管控能力。

**可能原因**

1. 该设备类型不支持接入侧载功能。
2. Tablet类型设备处于平板模式下。

**处理步骤**

请确认当前设备或系统版本是否支持侧载安全管控能力。
