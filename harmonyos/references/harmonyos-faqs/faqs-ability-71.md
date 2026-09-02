---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-71
title: 如何获取App版本号，版本名，屏幕分辨率等信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取App版本号，版本名，屏幕分辨率等信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a06216a7a525cd6a202b14eb2e585ed47138d514b2b30c44110623ecd30c95f6
---

1. 通过@kit.AbilityKit中的bundleManager模块查询bundleInfo，其中包含App版本号和版本名。

   ```screen
   import { BusinessError } from '@kit.BasicServicesKit';
   import { bundleManager } from '@kit.AbilityKit';

   // ...
   bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo) => {
     let versionName = bundleInfo.versionName; // App version name
     let versionNo = bundleInfo.versionCode; // App version code
   }).catch((error: BusinessError) => {
     console.error('get bundleInfo failed, error is ' + error);
   })
   ```
2. 在context.config中获取screenDensity，其中包含屏幕分辨率信息。

   ```screen
   import { common } from '@kit.AbilityKit';

   // ...
   // In the utility class: Save the context to AppStorage in the EntryAbility - onCreate lifecycle, then use AppStorage to retrieve it in the utility class
   let context = AppStorage.get('context') as common.UIAbilityContext;

   let screenDensity = context.config.screenDensity;
   ```
