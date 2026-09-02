---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-172
title: 如何获取应用签名信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取应用签名信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fa1ff03d49d6c73b9eecbd6fccb61542f23433d7aae9b93b8146b5a498cd850d
---

## 问题现象

如何在应用程序当中获取应用签名信息？包括应用的appId、应用包的指纹信息、应用的唯一标识appIdentifier、应用的证书公钥。

## 背景知识

[bundleManager.getBundleInfoForSelf：](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)根据给定的bundleFlags获取当前应用的BundleInfo，当bundleFlags指定为GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO时，获取的则是应用签名信息。

## 解决方案

bundleManager.getBundleInfoForSelf接口返回值：

* appId: appId是应用的唯一标识，由包名、下划线和证书公钥的Base64编码组成。
* fingerprint：应用包的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。
* appIdentifier：appIdentifier是Profile文件中的一个字段，为应用的唯一标识，在应用签名时生成。
* certificate：应用的证书公钥。

代码参考如下：

```ts
import { bundleManager } from '@kit.AbilityKit';

@Entry
@Component
struct Index {

  build() {
    RelativeContainer() {
      Text('查询应用签名信息')
        .fontSize(25)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
          try {
            bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
              console.info(`应用的appId：${bundleInfo.signatureInfo.appId}`);
              console.info(`应用包的指纹信息：${bundleInfo.signatureInfo.fingerprint}`);
              console.info(`应用的唯一标识：${bundleInfo.signatureInfo.appIdentifier}`);
              console.info(`应用的证书公钥：${bundleInfo.signatureInfo.certificate}`);
            }).catch((err: BusinessError) => {
              console.error(`code:${err.code}; meesage:${err.message}`);
            });
          } catch (err) {
            let error = err as BusinessError;
            console.error(`code:${error.code}; meesage:${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 常见FAQ

Q：签名过期后使用同一个CSR重新申请的证书与原证书是否一致呢？

A：CSR公钥相同则新申请的签名证书同原证书可以认为是一致的。

Q：调试证书和发布证书获取的appIdentifier是否一致。

A：一致。

Q：appId和appIdentifier有什么区别？

A：appId是应用的唯一标识，由包名、下划线和证书公钥的Base64编码组成。由于appId和签名信息相关，如果签名证书的公钥更换，appId也会跟随变化。

appIdentifier是Profile文件中的一个字段，为应用的唯一标识，为云端统一分配的随机字符串。该ID在应用全生命周期中不会发生变化，包括版本升级、证书变更、开发者公私钥变更、应用转移等。但如果使用的IDE自动签名，那么appIdentifier为随机分配。
