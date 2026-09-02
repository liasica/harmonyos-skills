---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-72
title: 如何获取指定bundleFlags的Ability信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取指定bundleFlags的Ability信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eb10445189a75888c5fbd58fe9d233b30f9ede7a6a4182c161ee745b25c2556f
---

bundleManager.getBundleInfoForSelf :getBundleInfoForSelf(bundleFlags: number): Promise<BundleInfo>;

根据给定的bundleFlags，异步获取当前应用的BundleInfo，返回结果使用Promise形式。参考示例代码如下：

```typescript
// Get appInfo with metadataArray information
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
}
```

**参考链接**

[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)
