---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-riskcontrolengine
title: RiskControlEngine（星盾机密风控引擎）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > ArkTS API错误码 > RiskControlEngine（星盾机密风控引擎）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf3f6d4f7944bff8899ff84ffa47f13ceab1b07931e70d1fecb43654ca17e21f
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1010800004 校验capability失败

**错误信息**

Verify capability fail.

**错误描述**

应用未开通星盾机密风控引擎服务。

**可能原因**

应用未开通星盾机密风控引擎服务。

**处理步骤**

1. 参考[开通Device Security服务](../harmonyos-guides/devicesecurity-deviceverify-activateservice.md)在AppGallery Connect开通“星盾机密风控引擎”。
2. 重新[申请Profile](../app/agc-help-profile-0000002270709473.md)，将新申请到的Profile作为工程的签名文件后重试。

## 1010800005 调用次数超过并行阈值

**错误信息**

The number of calls exceeds the parallel threshold.

**错误描述**

接口被同时调用的数量超出最大阈值。

**可能原因**

1. 开发者应用并发调用该接口或者其他应用同时调用该接口，调用数量超出最大阈值。
2. 每个设备上最多支持5个并发调用。

**处理步骤**

建议延迟重试，比如延迟1秒。

## 1010800006 API调用频率超过阈值

**错误信息**

The invoking frequency exceeds the threshold.

**错误描述**

接口被在单位时间内调用次数超出最大阈值。

**可能原因**

应用调用该接口的次数太多。

**处理步骤**

控制应用调用次数，此时不应重试，需在下一个统计周期再调用该接口。

## 1010800007 操作超时

**错误信息**

Operation timeout.

**错误描述**

接口执行超时。

**可能原因**

系统高负载。

**处理步骤**

请重新发起请求。

## 1010800009 导入风险因子数据失败

**错误信息**

Failed to import risk factor data.

**错误描述**

导入风险因子数据失败。

**可能原因**

导入因子没有配置 、导入因子数据与配置的数据类型不匹配，或者导入因子数据缓存重复。

**处理步骤**

请根据因子配置，检查因子数据取值是否错误或更换nonce值重试。

## 1010800010 风控评分计算失败

**错误信息**

Risk score calculation failed.

**错误描述**

风控评分计算失败。

**可能原因**

风险策略配置或风险因子获取异常。

**处理步骤**

请检查风险策略配置是否正确。
