---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-72
title: 如何获取指定bundleFlags的Ability信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取指定bundleFlags的Ability信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6ed5d2b5d7e1f36fd78ef026076f689bc8a5f3ed7a02b01cb79ba55cc0666af5
---

bundleManager.getBundleInfoForSelf :getBundleInfoForSelf(bundleFlags: number): Promise<BundleInfo>;

根据给定的bundleFlags，异步获取当前应用的BundleInfo，返回结果使用Promise形式。参考示例代码如下：

```
1. // Get appInfo with metadataArray information
2. import { bundleManager } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
7. try {
8. bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
9. hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
10. }).catch((err: BusinessError) => {
11. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
12. });
13. } catch (err) {
14. let message = (err as BusinessError).message;
15. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
16. }
```

[BundleFlags.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/BundleFlags.ets#L21-L36)

**参考链接**

[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)
