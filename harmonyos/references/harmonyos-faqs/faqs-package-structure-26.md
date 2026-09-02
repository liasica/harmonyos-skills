---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-26
title: 如何获取当前HAP的BundleName
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何获取当前HAP的BundleName
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e846a77ef46d22df7d515de75466be1f6b2f183808ae1e8e7a8f8e88b0f4f931
---

使用bundleManager模块的getBundleInfoForSelf接口获取所有信息。

GET\_BUNDLE\_INFO\_DEFAULT：接口默认参数，返回结果的name字段对应BundleName。

GET\_BUNDLE\_INFO\_WITH\_APPLICATION：除基本字段外，还能够获取ApplicationInfo字段，ApplicationInfo的name字段对应BundleName。

下面代码以GET\_BUNDLE\_INFO\_DEFAULT为例：

```typescript
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;
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
