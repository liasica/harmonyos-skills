---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext
title: @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8f82d227f2ad67839bd4c156521e3893f2915282cc42789e28e8c870946d065f
---

FaultLogExtensionContext是[FaultLogExtensionAbility](js-apis-hiviewdfx-faultlogextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

FaultLogExtensionContext模块提供访问[FaultLogExtensionAbility](js-apis-hiviewdfx-faultlogextensionability.md)的资源的能力，对于扩展的ExtensionAbility，可直接将ExtensionContext作为上下文环境，或者定义一个继承自ExtensionContext的类型作为上下文环境。

说明

* 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 使用说明

PhonePC/2in1TabletTVWearable

通过FaultLogExtensionAbility子类实例来获取。

```
1. import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';

3. export default class MyFaultLogExtension extends FaultLogExtensionAbility {
4. onFaultReportReady() {
5. let context = this.context; // 获取FaultLogExtensionContext
6. console.info('cache dir is ' + context.cacheDir); // 访问context中的成员
7. }
8. }
```

## FaultLogExtensionContext

PhonePC/2in1TabletTVWearable

FaultLogExtensionContext是[FaultLogExtensionAbility](js-apis-hiviewdfx-faultlogextensionability.md)的上下文环境。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger
