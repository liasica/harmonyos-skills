---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-52
title: 如何查询应用包的名称、供应商、版本号、版本文本、安装时间、更新时间描述信息
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何查询应用包的名称、供应商、版本号、版本文本、安装时间、更新时间描述信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:91e64fdfa4a63d50c2259eae1281c7d8cc38b68f59f7ffc47905d7f314aa29ec
---

首先，通过 bundleManager.getBundleInfoForSelf() 接口获取应用包的名称、供应商、版本号、版本文本、安装时间和更新时间。具体可参考示例代码：

```typescript
import { bundleManager } from '@kit.AbilityKit';

// Apply to obtain BundleInfo and applicationInfo
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;

try {
  bundleManager.getBundleInfoForSelf(bundleFlags, (err, data) => {
    // Get the bundle name of the application itself
    const bundleName = data.name;
    // Get the version number of the application（versionCode）
    const versionCode = data.versionCode;
    // Get the version name of the application（versionName）
    const versionName = data.versionName;

    if (err) {
      console.error(`getBundleInfoForSelf failed: ${err.message}`);
    } else {
      console.info(`get bundleName successfully: ${bundleName}`);
      console.info(`get versionCode successfully: ${versionCode}`);
      console.info(`get versionName successfully: ${versionName}`);
      console.info(`getBundleInfoForSelf successfully: ${JSON.stringify(data)}`);
    }
  });
} catch (err) {
  console.error(`getBundleInfoForSelf failed: ${JSON.stringify(err)}`);
}
```

**参考链接**

[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself-1)
