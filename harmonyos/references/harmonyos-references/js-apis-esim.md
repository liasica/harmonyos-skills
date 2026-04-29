---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-esim
title: @ohos.telephony.esim (eSIM卡管理)
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.esim (eSIM卡管理)
category: harmonyos-references
scraped_at: 2026-04-29T13:59:59+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a587b6a6152fce09a02300e673302a632f3f5b8ccebd4e0b9cfdf771f5373868
---

eSIM卡管理模块提供了eSIM卡管理的基础能力，包括获取指定卡槽是否支持eSIM功能，如果支持则允许用户添加单个配置文件。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhoneWearable

```
1. import { eSIM } from '@kit.TelephonyKit';
```

## eSIM.isSupported

PhoneWearable

isSupported(slotId: number): boolean

获取指定卡槽是否支持eSIM功能。

**系统能力**：SystemCapability.Telephony.CoreService.Esim

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定卡槽是否支持eSIM功能，如果支持返回true，不支持返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 3120001 | Service connection failed. |
| 3120002 | System internal error. |

**示例：**

```
1. import { eSIM } from '@kit.TelephonyKit';

3. let isSupported: boolean = eSIM.isSupported(1);
4. console.info(`the esim is Supported:` + isSupported);
```

## eSIM.addProfile

PhoneWearable

addProfile(profile: DownloadableProfile): Promise<boolean>

通过该接口拉起下载界面，允许用户添加单个配置文件。使用Promise异步回调。

**需要权限**：ohos.permission.SET\_TELEPHONY\_ESIM\_STATE\_OPEN

**系统能力**：SystemCapability.Telephony.CoreService.Esim

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | [DownloadableProfile](js-apis-esim.md#downloadableprofile) | 是 | 可下载的配置文件信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回最终用户添加单个配置文件的结果。返回true为成功，false为失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 3120001 | Service connection failed. |
| 3120002 | System internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { eSIM } from '@kit.TelephonyKit';

4. let profile: eSIM.DownloadableProfile = {
5. activationCode:'1',
6. confirmationCode:'1',
7. carrierName:'test',
8. accessRules:[{
9. certificateHashHexStr:'test',
10. packageName:'com.example.testcoreservice',
11. accessType:0
12. }]
13. };

15. eSIM.addProfile(profile).then(() => {
16. console.info(`addProfile invoking succeeded.`);
17. }).catch((err: BusinessError<void>) => {
18. console.error(`addProfile, promise: err->${JSON.stringify(err)}`);
19. });
```

## DownloadableProfile

PhoneWearable

可下载的配置文件。

**系统能力**：SystemCapability.Telephony.CoreService.Esim

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| activationCode | string | 否 | 否 | 激活码。对于不基于激活码的配置文件，可能为空。 |
| confirmationCode | string | 否 | 是 | 确认码。 |
| carrierName | string | 否 | 是 | 订阅名称。 |
| accessRules | Array<[AccessRule](js-apis-esim.md#accessrule20)> | 否 | 是 | 访问规则数组。 |

## AccessRule20+

PhoneWearable

访问规则。

**系统能力**：SystemCapability.Telephony.CoreService.Esim

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certificateHashHexStr | string | 否 | 否 | 证书哈希的十六进制字符串。 |
| packageName | string | 否 | 否 | 规则适用的程序包名称。 |
| accessType | number | 否 | 否 | 规则的类型。 |
