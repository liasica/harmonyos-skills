---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-42
title: 点击跳转三方支付时应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 点击跳转三方支付时应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:272fbea1bee36f0ed19db3441aa44334c4fab9c9e6a21d87fa76a8b0ccd3e051
---

## 问题现象

用户在收银台页面选择支付方式后，点击“确认支付”时应用出现闪退，直接退到桌面。

## 背景知识

[拉起指定应用](../harmonyos-guides/app-startup-overview.md)：通过应用链接跳转的方式拉起指定应用。

## 问题定位

从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是Error，自定义错误类型，故障信息为BusinessError 17700056: The scheme of the specified link is not in the querySchemes.，该错误表明是应用没有正确配置目标应用的scheme，导致跳转时查询不到目标应用的URL scheme。

```shell
Reason:Error
Error name:Error
Error message:BusinessError 17700056: The scheme of the specified link is not in the querySchemes.
Error code:
Stacktrace:
Cannot get SourceMap info, dump raw stack:
    at isApplicationExist (entry|entry|1.0.0|src/main/ets/domain/system/SystemUtils.ts:101:1)
    at anonymous (entry|@hzw/ohos-dsbridge|1.6.0|src/main/ets/entity/BaseBridge.ts:140:1)
    at (entry/src/main/ets/pages/Index.ets:38:7)
```

## 分析结论

应用没有正确配置目标应用的scheme，点击跳转时查询不到目标应用的URL scheme，又没有做异常处理，导致应用出现闪退。

## 修改建议

在拉起三方应用之前，可以先调用[canOpenLink](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercanopenlink12)判断应用是否存在，如果存在再拉起。相关示例参考文档[（可选）使用canOpenLink判断应用是否可访问](../harmonyos-guides/canopenlink.md)中的操作步骤。
