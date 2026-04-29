---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-problem-of-application
title: 应用程序包常见问题
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用程序包常见问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:35+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1cc2d2acd02b0a906fcd52407212f63e0269aa7928666d211cf5a706d377e31c
---

## 如何获取签名信息中的指纹信息

* 通过调用接口获取。

可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含指纹信息，使用哈希算法SHA-256生成。

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
5. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
6. try {
7. bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
8. console.info('testTag', 'getBundleInfoForSelf successfully. fingerprint: ', bundleInfo.signatureInfo.fingerprint);
9. }).catch((err: BusinessError) => {
10. console.error('testTag', 'getBundleInfoForSelf failed. Cause: ', err.message);
11. });
12. } catch (err) {
13. let message = (err as BusinessError).message;
14. console.error('testTag', 'getBundleInfoForSelf failed: %{public}s', message);
15. }
```

[GetFingerprint.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/CommonProblemOfApplication/entry/src/main/ets/pages/GetFingerprint.ets#L16-L32)

* 通过[bm工具](bm-tool.md)获取指纹信息，使用哈希算法SHA-256生成。

```
1. hdc shell
2. # 需将com.example.myapplication替换为实际应用的包名
3. bm dump -n com.example.myapplication | grep fingerprint
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/56coLL5CRbiskAAyrGZV0A/zh-cn_image_0000002558604316.png?HW-CC-KV=V1&HW-CC-Date=20260429T052534Z&HW-CC-Expire=86400&HW-CC-Sign=68AF60D0628DBA3F41873E77DA6A03567D47BCB0D12E05F8ACDE89AFF3BB57A7)

* 通过.cer证书文件获取，可以参考[APP备案FAQ](../app/50130.md)中HarmonyOS应用/元服务如何获取公钥和签名信息，指纹信息使用哈希算法SHA-1生成。
* 通过keytool工具获取，详情参考[生成签名证书指纹](../AppGallery-connect-Guides/appgallerykit-preparation-game-0000001055356911.md#section147011294331)，使用哈希算法SHA-256生成。

## 什么是appIdentifier

appIdentifier是[Profile文件](../app/agc-help-release-profile-0000002248341090.md)中的一个字段，为应用的唯一标识，在应用签名时生成，其中：

1. 通过DevEco Studio工具[自动签名](ide-signing.md#section18815157237)生成，此时的appIdentifier字段是随机生成的，在不同的设备上签名、或者重新签名均会导致appIdentifier字段不一致。
2. 采用手动签名，并通过AppGallery Connect平台申请证书，此时申请[调试Profile](../app/agc-help-debug-profile-0000002248181278.md)或者[发布Profile](../app/agc-help-release-profile-0000002248341090.md)中的appIdentifier字段是固定的，该字段来源于AppGallery Connect创建应用时生成的[APP ID](../app/agc-help-create-app-0000002247955506.md#section16423184171915)，由云端统一分配。此时的appIdentifier字段在应用全生命周期中不会发生变化，包括版本升级、证书变更、开发者公私钥变更、应用转移等。

因此，在跨设备调试、跨应用交互调试、或者多用户共同开发且需要共享密钥等要求appIdentifier不变的场景下，推荐使用手动签名，具体场景请参考[使用场景说明](ide-signing.md#section54361623194519)。

## 如何获取应用信息中的appIdentifier

* 可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appIdentifier信息。

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
5. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
6. try {
7. bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
8. console.info('testTag', 'getBundleInfoForSelf successfully. appIdentifier:', bundleInfo.signatureInfo.appIdentifier);
9. }).catch((err: BusinessError) => {
10. console.error('testTag', 'getBundleInfoForSelf failed. Cause:', err.message);
11. });
12. } catch (err) {
13. let message = (err as BusinessError).message;
14. console.error('testTag', 'getBundleInfoForSelf failed:', message);
15. }
```

[GetAppIdentifier.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/CommonProblemOfApplication/entry/src/main/ets/pages/GetAppIdentifier.ets#L16-L32)

* 通过[bm工具](bm-tool.md)获取。

```
1. hdc shell
2. # 需将com.example.myapplication替换为实际应用的包名
3. bm dump -n com.example.myapplication | grep appIdentifier
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VoQPPlYWRuSNBdW0ist8ow/zh-cn_image_0000002589323841.png?HW-CC-KV=V1&HW-CC-Date=20260429T052534Z&HW-CC-Expire=86400&HW-CC-Sign=B7FEFDF3EA298509DFF72482B92F56C63EA6E92100C99C4070429D1AD2B92CCA)

## 什么是appId

appId是应用的唯一标识，由包名、下划线和证书公钥的Base64编码组成。由于appId和签名信息相关，如果签名证书的公钥更换，appId也会跟随变化，所以应用的唯一标识推荐使用[appIdentifier](common-problem-of-application.md#什么是appidentifier)。

## 如何获取应用信息中的appId

* 可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appId信息。

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
5. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
6. try {
7. bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
8. console.info('testTag', 'getBundleInfoForSelf successfully. appId:', bundleInfo.signatureInfo.appId);
9. }).catch((err: BusinessError) => {
10. console.error('testTag', 'getBundleInfoForSelf failed. Cause:', err.message);
11. });
12. } catch (err) {
13. let message = (err as BusinessError).message;
14. console.error('testTag', 'getBundleInfoForSelf failed:', message);
15. }
```

[GetAppId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/CommonProblemOfApplication/entry/src/main/ets/pages/GetAppId.ets#L16-L32)

* 通过[bm工具](bm-tool.md)获取。

```
1. hdc shell
2. # 需将ohos.app.hap.myapplication替换为实际应用的包名
3. bm dump -n ohos.app.hap.myapplication |grep '"appId":'
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/RHNx3TsQQj6zCdY_bVUU_w/zh-cn_image_0000002589243779.png?HW-CC-KV=V1&HW-CC-Date=20260429T052534Z&HW-CC-Expire=86400&HW-CC-Sign=C9FA6CB54336B6EC61AC590980202E3E52C3023C1A647E718DC79A3B304BDD90)

## 应用的uid

uid是系统中用于[应用沙箱](access-token-overview.md#应用沙箱)隔离的唯一标识符，它分配给每个应用进程，确保应用在运行时相互隔离（如文件系统，内存空间等）。

uid的生成算法为：uid = userId \* 200000 + (bundleId % 200000)。其中%表示取模运算，计算bundleId除以200000的余数。userId表示应用需要安装的用户编号，可以通过[getOsAccountLocalId接口](../harmonyos-references/js-apis-osaccount.md#getosaccountlocalid9)获取。bundleId表示应用的唯一编号，取值范围为10000到65535的整数，仅系统内部使用，可以通过uid和userId反算获取，暂无其他获取途径。
