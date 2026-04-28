---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-71
title: 如何获取App版本号，版本名，屏幕分辨率等信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取App版本号，版本名，屏幕分辨率等信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:47+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:1deea6c1a0668a15a191ef911cac3636472c032a92cf5f19521d6c87acbd4215
---

1. 通过@kit.AbilityKit中的bundleManager模块查询bundleInfo，其中包含App版本号和版本名。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { bundleManager } from '@kit.AbilityKit';

   4. // ...
   5. bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo) => {
   6. let versionName = bundleInfo.versionName; //App version name
   7. let versionNo = bundleInfo.versionCode; //App version code
   8. }).catch((error: BusinessError) => {
   9. console.error('get bundleInfo failed, error is ' + error);
   10. })
   ```

   [GetAppInformationWithBundle.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetAppInformationWithBundle.ets#L21-L30)
2. 在context.config中获取screenDensity，其中包含屏幕分辨率信息。

   ```
   1. import { common } from '@kit.AbilityKit';

   3. // ...
   4. // In the utility class: Save the context to AppStorage in the EntryAbility - onCreate lifecycle, then use AppStorage to retrieve it in the utility class
   5. let context = AppStorage.get('context') as common.UIAbilityContext;

   7. let screenDensity = context.config.screenDensity;
   ```

   [GetAppInformation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetAppInformation.ets#L21-L27)
