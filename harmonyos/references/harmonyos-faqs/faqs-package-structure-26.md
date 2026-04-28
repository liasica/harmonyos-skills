---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-26
title: 如何获取当前HAP的BundleName
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何获取当前HAP的BundleName
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0fc0a43808da494ae0347db11057d11d4f8b6a6fa301d177cf074e236547e4c1
---

使用bundleManager模块的getBundleInfoForSelf接口获取所有信息。

GET\_BUNDLE\_INFO\_DEFAULT：接口默认参数，返回结果的name字段对应BundleName。

GET\_BUNDLE\_INFO\_WITH\_APPLICATION：除基本字段外，还能够获取ApplicationInfo字段，ApplicationInfo的name字段对应BundleName。

下面代码以GET\_BUNDLE\_INFO\_DEFAULT为例：

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;
5. try {
6. bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
7. hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
10. });
11. } catch (err) {
12. let message = (err as BusinessError).message;
13. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
14. }
```

[GetBundleName.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/ets/pages/GetBundleName.ets#L21-L34)
