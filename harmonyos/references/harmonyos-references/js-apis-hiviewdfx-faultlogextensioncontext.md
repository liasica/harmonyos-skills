---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext
title: "@ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)"
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7009e9fdfc889cc337ed32dddf83e71ddca657bbec08d645458e7f5bc144086b
---

FaultLogExtensionContext是[FaultLogExtensionAbility](js-apis-hiviewdfx-faultlogextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

FaultLogExtensionContext模块提供访问[FaultLogExtensionAbility](js-apis-hiviewdfx-faultlogextensionability.md)的资源的能力，对于扩展的ExtensionAbility，可直接将ExtensionContext作为上下文环境，或者定义一个继承自ExtensionContext的类型作为上下文环境。

**说明** 

* 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 使用说明

通过FaultLogExtensionAbility子类实例来获取。

```ts
import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onFaultReportReady() {
        let context = this.context; // 获取FaultLogExtensionContext
        console.info('cache dir is ' + context.cacheDir); // 访问context中的成员
    }
}
```

## FaultLogExtensionContext

FaultLogExtensionContext是[FaultLogExtensionAbility](js-apis-hiviewdfx-faultlogextensionability.md)的上下文环境。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger
