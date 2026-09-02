---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-24
title: 如何在Native侧获取APP版本信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧获取APP版本信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8f57359a0951477eb69665bb126e1184ba33f3fa2902a9dc0e8be44acf325bab
---

Native侧目前没有获取APP版本信息的接口。如需获取APP版本信息，可以在ArkTS侧获取，然后传递到Native侧。

通过@kit.AbilityKit模块中的bundleManager查询bundleInfo。bundleInfo包含App版本号和版本名。

ArkTS侧传递数据到Native侧可参考链接：

```ts
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo)=>{
              let versionName = bundleInfo.versionName;//Application version name
              let versionNo = bundleInfo.versionCode;//Application version number
            }).catch((error : BusinessError)=>{
              console.error("get bundleInfo failed,error is "+error)})
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

ArkTS侧传递数据到Native侧可参考链接：

[使用Node-API实现跨语言交互开发流程](../harmonyos-guides/use-napi-process.md)

获取模块相关信息参考链接：

[bundleInfo](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#bundleinfo-1)

[@ohos.bundle.bundleManager (应用程序包管理模块)](../harmonyos-references/js-apis-bundlemanager.md)
