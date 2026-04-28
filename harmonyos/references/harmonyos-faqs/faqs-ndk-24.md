---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-24
title: 如何在Native侧获取APP版本信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧获取APP版本信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:df094816c6dfb917276e32bd23d69ada2d1974af221ca34f30d264ac4d419e58
---

Native侧目前没有获取APP版本信息的接口。如需获取APP版本信息，可以在ArkTS侧获取，然后传递到Native侧。

通过@kit.AbilityKit模块中的bundleManager查询bundleInfo。bundleInfo包含App版本号和版本名。

ArkTS侧传递数据到Native侧可参考链接：

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. Row() {
11. Column() {
12. Text(this.message)
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. .onClick(() => {
16. bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo)=>{
17. let versionName = bundleInfo.versionName;//Application version name
18. let versionNo = bundleInfo.versionCode;//Application version number
19. }).catch((error : BusinessError)=>{
20. console.error("get bundleInfo failed,error is "+error)})
21. })
22. }
23. .width('100%')
24. }
25. .height('100%')
26. }
27. }
```

[BundInfoPage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/ets/pages/BundInfoPage.ets#L3-L29)

ArkTS侧传递数据到Native侧可参考链接：

[使用Node-API实现跨语言交互开发流程](../harmonyos-guides/use-napi-process.md)

获取模块相关信息参考链接：

[bundleInfo](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#bundleinfo-1)

[@ohos.bundle.bundleManager (应用程序包管理模块)](../harmonyos-references/js-apis-bundlemanager.md)
