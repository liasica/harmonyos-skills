---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-problem-of-application
title: 应用程序包常见问题
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用程序包常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:985033a88f262e9d833d7261d0394c8c01e7e9141b4fe7f13fe34a130b9b12a0
---

## 如何获取签名信息中的指纹信息

* 通过调用接口获取。

可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含指纹信息，使用哈希算法SHA-256生成。

```typescript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
  bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
    console.info('testTag', 'getBundleInfoForSelf successfully. fingerprint: ', bundleInfo.signatureInfo.fingerprint);
  }).catch((err: BusinessError) => {
    console.error('testTag', 'getBundleInfoForSelf failed. Cause: ', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('testTag', 'getBundleInfoForSelf failed: %{public}s', message);
}
```

* 通过[bm工具](bm-tool.md)获取指纹信息，使用哈希算法SHA-256生成。

```shell
hdc shell
# 需将com.example.myapplication替换为实际应用的包名
bm dump -n com.example.myapplication | grep fingerprint
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Syfhl5fYQnaUrHu466rskw/zh-cn_image_0000002736312109.png)

* 通过.cer证书文件获取，可以参考[APP备案FAQ](../app/50130.md)中HarmonyOS应用/元服务如何获取公钥和签名信息，指纹信息使用哈希算法SHA-1生成。
* 通过keytool工具获取，详情参考[生成签名证书指纹](../AppGallery-connect-Guides/appgallerykit-preparation-game-0000001055356911.md#section147011294331)，使用哈希算法SHA-256生成。

## 什么是appIdentifier

appIdentifier是[Profile文件](../app/agc-help-release-profile-0000002248341090.md)中的一个字段，为应用的唯一标识，在应用签名时生成，其中：

1. 通过DevEco Studio工具[自动签名](ide-signing.md#section18815157237)生成，此时的appIdentifier字段是随机生成的，在不同的设备上签名、或者重新签名均会导致appIdentifier字段不一致。
2. 采用手动签名，并通过AppGallery Connect平台申请证书，此时申请[调试Profile](../app/agc-help-debug-profile-0000002248181278.md)或者[发布Profile](../app/agc-help-release-profile-0000002248341090.md)中的appIdentifier字段是固定的，该字段来源于AppGallery Connect创建应用时生成的[APP ID](../app/agc-help-create-app-0000002247955506.md#section16423184171915)，由云端统一分配。此时的appIdentifier字段在应用全生命周期中不会发生变化，包括版本升级、证书变更、开发者公私钥变更、应用转移等。

因此，在跨设备调试、跨应用交互调试、或者多用户共同开发且需要共享密钥等要求appIdentifier不变的场景下，推荐使用手动签名，具体场景请参考[使用场景说明](ide-signing.md#section54361623194519)。

## 如何获取应用信息中的appIdentifier

* 可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appIdentifier信息。

```typescript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
  bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
    console.info('testTag', 'getBundleInfoForSelf successfully. appIdentifier:', bundleInfo.signatureInfo.appIdentifier);
  }).catch((err: BusinessError) => {
    console.error('testTag', 'getBundleInfoForSelf failed. Cause:', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('testTag', 'getBundleInfoForSelf failed:', message);
}
```

* 通过[bm工具](bm-tool.md)获取。

```shell
hdc shell
# 需将com.example.myapplication替换为实际应用的包名
bm dump -n com.example.myapplication | grep appIdentifier
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/FhuARZILSbSg2ZLV4NVdtQ/zh-cn_image_0000002706673066.png)

## 什么是appId

appId是应用的唯一标识，由包名、下划线和证书公钥的Base64编码组成。由于appId和签名信息相关，如果签名证书的公钥更换，appId也会跟随变化，所以应用的唯一标识推荐使用[appIdentifier](common-problem-of-application.md#什么是appidentifier)。

## 如何获取应用信息中的appId

* 可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appId信息。

```typescript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
  bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
    console.info('testTag', 'getBundleInfoForSelf successfully. appId:', bundleInfo.signatureInfo.appId);
  }).catch((err: BusinessError) => {
    console.error('testTag', 'getBundleInfoForSelf failed. Cause:', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('testTag', 'getBundleInfoForSelf failed:', message);
}
```

* 通过[bm工具](bm-tool.md)获取。

```shell
hdc shell
# 需将ohos.app.hap.myapplication替换为实际应用的包名
bm dump -n ohos.app.hap.myapplication |grep '"appId":'
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/4bLlUb43RE2GZN5sXEGnjg/zh-cn_image_0000002736432157.png)

## 应用的uid

uid是系统中用于[应用沙箱](access-token-overview.md#应用沙箱)隔离的唯一标识符，它分配给每个应用进程，确保应用在运行时相互隔离（如文件系统，内存空间等）。

uid的生成算法为：uid = userId \* 200000 + (bundleId % 200000)。其中%表示取模运算，计算bundleId除以200000的余数。userId表示应用需要安装的用户编号，可以通过[getOsAccountLocalId](../harmonyos-references/js-apis-osaccount.md#getosaccountlocalid9)接口获取。bundleId表示应用的唯一编号，取值范围为10000到65535的整数，仅系统内部使用，可以通过uid和userId反算获取。

## 如何获取应用的uid

* 通过[bm工具](bm-tool.md)获取。

```shell
hdc shell
# 需将ohos.app.hap.myapplication替换为实际应用的包名
bm dump -n ohos.app.hap.myapplication |grep uid
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/wgB4PqAbRpa-nO3yshT_EA/zh-cn_image_0000002706833002.png)

* 可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，示例代码可以参考[如何获取应用信息中的appId](common-problem-of-application.md#如何获取应用信息中的appid)，取值方式为bundleInfo.appInfo.uid。

## 跨HSP模块调用和跨HAR模块调用的区别

HSP模块和HAR模块被调用时，主要的区别在Module2（HSP/HAR）模块Native调用Module2（HSP/HAR）模块ArkTS中，在调用napi\_load\_module\_with\_info加载模块时的入参不同，其余流程一致。

1. 被调用模块Module2是HAR

   如图所示，编译构建后，HAR模块被打包到各个模块之中，所以其入口模块仍然是HAP模块，napi\_load\_module\_with\_info中第2个参数的模块名称要填HAP模块中oh-package.json5中定义的依赖HAR的名称，而不是HAR模块的实际名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/fh0LxtOjQDWE3gozY9QhpQ/zh-cn_image_0000002736312111.png)
2. 被调用模块Module2是HSP

   当被调用模块Module2是HSP，HSP是独立的模块，其入口模块就是HSP本模块，所以napi\_load\_module\_with\_info第2个参数的模块名就是它自己的模块名。

## 找不到HAR或HSP模块的ArkTS文件

**问题现象**

调用HAR/HSP模块的ArkTS文件时，可能会遇到以下报错：

```ts
Error message:Cannot find module 'staticModule/src/main/ets/utils/Util' imported from 'com.xxxx.crossmodulereference/entry'.
```

**可能原因**

工程级的build-profile.json5中的useNormalizedOHMUrl设置参数为false。

**解决措施**

在调用模块Module1的build-profile.json5里面添加如下配置。

```json5
// ...
  "buildOption": {
    // ...
    "arkOptions" : {
      "runtimeOnly" : {
        "packages": [
          "static_module"
        ]
      }
    }
  },
  // ...
```
