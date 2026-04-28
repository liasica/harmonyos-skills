---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-scenemanager
title: sceneManager （生态查询服务）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > sceneManager （生态查询服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62cd695e543077e2e459bb54b9a55c2c73d3d4ac35b45d8144679f45d31218c4
---

对场景值进行管理，提供查询自身场景值，获取广告验签版本功能。

说明

调用接口需捕获异常。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { sceneManager } from '@kit.AppGalleryKit';
```

## sceneManager.getSelfSceneCode

PhonePC/2in1TabletTV

getSelfSceneCode(): string

查询自身场景值。调用此接口需捕获异常。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.EcologicalRuleManager.SceneManager

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 自身场景值。 |

**示例：**

```
1. import { sceneManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const selfSceneCode: string = sceneManager.getSelfSceneCode();
6. hilog.info(0, 'TAG', "Succeeded in getting SelfSceneCode res = " + selfSceneCode);
7. } catch (err) {
8. hilog.error(0, 'TAG', `get self sceneCode failed.code is ${err.code}, message is ${err.message}`);
9. }
```

## sceneManager.getAdsVerificationVersion

PhonePC/2in1TabletTV

getAdsVerificationVersion(): number

获取广告验签版本。调用此接口需捕获异常。

**系统能力：** SystemCapability.BundleManager.EcologicalRuleManager.SceneManager

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 广告验签版本。当前返回值为1。  广告场景中开发者需要在want参数中携带以下参数：ohos.market.param.signature、ohos.market.param.ad\_networkid、ohos.market.param.timestamp、ohos.market.param.verify\_version、ohos.market.param.ad\_nonce，验签时会根据want中这些字段值使用公钥进行验签。 |

**示例：**

```
1. import { sceneManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const version: number = sceneManager.getAdsVerificationVersion();
6. hilog.info(0, 'TAG', "Succeeded in getting AdsVerificationVersion res = " + version);
7. } catch (err) {
8. hilog.error(0, 'TAG', `get ads verification version failed.code is ${err.code}, message is ${err.message}`);
9. }
```
