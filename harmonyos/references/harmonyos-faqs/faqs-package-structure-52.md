---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-52
title: 如何查询应用包的名称、供应商、版本号、版本文本、安装时间、更新时间等信息
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何查询应用包的名称、供应商、版本号、版本文本、安装时间、更新时间等信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:36+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c33eda7bf575abe958bfd7e5b04fcf677f5deb51a1fba5820b98f43465e32b86
---

首先，通过 bundleManager.getBundleInfoForSelf() 接口获取应用包的名称、供应商、版本号、版本文本、安装时间和更新时间。具体可参考示例代码：

```
1. import { bundleManager } from '@kit.AbilityKit';

3. // Apply to obtain BundleInfo and applicationInfo
4. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;

6. try {
7. bundleManager.getBundleInfoForSelf(bundleFlags, (err, data) => {
8. // Get the bundle name of the application itself
9. const bundleName = data.name;
10. // Get the version number of the application（versionCode）
11. const versionCode = data.versionCode;
12. // Get the version name of the application（versionName）
13. const versionName = data.versionName;

15. if (err) {
16. console.error(`getBundleInfoForSelf failed: ${err.message}`);
17. } else {
18. console.info(`get bundleName successfully: ${bundleName}`);
19. console.info(`get versionCode successfully: ${versionCode}`);
20. console.info(`get versionName successfully: ${versionName}`);
21. console.info(`getBundleInfoForSelf successfully: ${JSON.stringify(data)}`);
22. }
23. });
24. } catch (err) {
25. console.error(`getBundleInfoForSelf failed: ${JSON.stringify(err)}`);
26. }
```

[GetBundleInfo.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/ets/pages/GetBundleInfo.ets#L21-L46)

**参考链接**

[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself-1)
