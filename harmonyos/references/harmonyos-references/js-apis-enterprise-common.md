---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-common
title: "@ohos.enterprise.common (Enterprise公共模块)"
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.common (Enterprise公共模块)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:04+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f36c78fc1d10d99de69d2ee8cf5807c0e7db0b5241186c5317aa821c6fa088ae
---

本模块提供MDM Kit中常用公共能力的纯类型定义，包含枚举类型和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

**使用场景**：

在企业设备管理应用开发中，当需要配置设备管控策略、管理应用实例、处理应用安装结果、监听策略变更等场景时，会使用本模块定义的类型。这些类型为MDM Kit中各子模块的接口提供统一的参数和返回值标准。

**收益**：

通过标准化的类型定义，可以简化企业设备管理应用的开发流程，提高代码的可维护性和类型安全性，降低类型相关的运行时错误。

**说明** 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { common } from '@kit.MDMKit';
```

## ManagedPolicy

企业设备管控策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认，无管控策略。 |
| DISALLOW | 1 | 禁用。 |
| FORCE\_OPEN | 2 | 强制开启。 |

## ApplicationInstance

应用的实例数据。

该接口目前在[addUserNonStopApps](js-apis-enterprise-applicationmanager.md#applicationmanageraddusernonstopapps22)、[removeUserNonStopApps](js-apis-enterprise-applicationmanager.md#applicationmanagerremoveusernonstopapps22)、[addFreezeExemptedApps](js-apis-enterprise-applicationmanager.md#applicationmanageraddfreezeexemptedapps22)、[removeFreezeExemptedApps](js-apis-enterprise-applicationmanager.md#applicationmanagerremovefreezeexemptedapps22)接口中作为入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appIdentifier | string | 否 | 否 | 应用[唯一标识符](js-apis-bundlemanager-bundleinfo.md#signatureinfo)，可以通过接口[bundleManager.getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14-2)获取bundleInfo.signatureInfo.appIdentifier。 |
| accountId | number | 否 | 否 | 用户ID。取值范围：大于等于0的整数。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)接口获取。 |
| appIndex | number | 否 | 否 | 应用分身索引。取值范围：大于等于0的整数。  appIndex可以通过[getAppCloneIdentity](js-apis-bundlemanager.md#bundlemanagergetappcloneidentity14)接口获取。 |

## InstallationResult

应用安装结果。

该对象目前在[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](js-apis-enterpriseadminextensionability.md#onmarketappinstallresult22)作为回调入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | [Result](js-apis-enterprise-common.md#result) | 否 | 否 | 应用安装结果码。SUCCESS表示应用安装成功，应用可正常使用；FAIL表示应用安装失败，应用不可用。 |
| message | string | 否 | 否 | 应用安装结果消息。 |

## Result

应用安装结果码。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 应用安装成功。 |
| FAIL | -1 | 应用安装失败。 |

## EnterpriseAdminExtensionContext23+

type EnterpriseAdminExtensionContext = \_EnterpriseAdminExtensionContext.default

EnterpriseAdminExtensionContext是[EnterpriseAdminExtensionAbility](js-apis-enterpriseadminextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**系统能力**: SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| \_EnterpriseAdminExtensionContext.default | EnterpriseAdminExtensionAbility组件的上下文[EnterpriseAdminExtensionContext](js-apis-application-enterpriseadminextensioncontext.md)。 |

## StartupScene24+

开机向导完成场景。端侧系统在首次切换子用户完成（仅限PC）、OTA升级完成、首次开机完成开机向导时会通过[onStartupGuideCompleted](js-apis-enterpriseadminextensionability.md#onstartupguidecompleted24)回调接口通知设备管理应用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_SETUP | 0 | 子用户被首次切换并完成其开机向导场景（仅限PC）。后续再次切换该子用户不会触发回调。 |
| OTA | 1 | OTA升级完成场景。 |
| DEVICE\_PROVISION | 2 | 首次开机完成开机向导场景。 |

## PolicyChangedEvent

策略变更事件。

该接口目前在[onAdminPolicyChanged](js-apis-enterpriseadminextensionability.md#onadminpolicychanged)接口中作为回调入参使用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用包名。 |
| functionName | string | 否 | 否 | 接口名称。例如调用[setPasswordPolicy](js-apis-enterprise-securitymanager.md#securitymanagersetpasswordpolicy)接口时，该字段返回值为setPasswordPolicy。 |
| parameters | string | 否 | 否 | 调用接口时传入的参数值（不包含admin参数），JSON格式字符串。例如调用[setPasswordPolicy](js-apis-enterprise-securitymanager.md#securitymanagersetpasswordpolicy)接口，该字段返回值为{"policy":{"complexityRegex":"^(?=.\*[a-zA-Z])(?=.\*\\d).{8},$","validityPeriod":1808309786000,"additionalDescription":"至少8个字符，且包含数字和字母。"}}。 |
| time | number | 否 | 否 | 调用接口的时间戳，单位：ms。 |

## DiskType

外置存储设备磁盘类型的枚举。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SD\_CARD | 1 | SD卡类型。 |
| USB\_FLASH | 2 | U盘类型。 |
| CD\_DVD\_BD | 3 | 光盘类型。 |

## ExternalStorageDeviceInfo

外置存储设备信息。该接口目前在[usbManager.getExternalStorageDeviceInfos](js-apis-enterprise-usbmanager.md#usbmanagergetexternalstoragedeviceinfos)接口中作为返回值使用，在[EnterpriseAdminExtensionAbility.onUnmountExternalStorageDevice](js-apis-enterpriseadminextensionability.md#onunmountexternalstoragedevice)接口中作为回调入参使用。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [DiskType](js-apis-enterprise-common.md#disktype) | 否 | 否 | 磁盘类型。 |
| devicePath | string | 否 | 否 | 挂载路径。 |
| volumeId | string | 否 | 否 | 卷ID。 |
| mountStatus | boolean | 否 | 否 | 挂载状态。返回true表示已挂载；返回false表示未挂载。 |
| vendorId | number | 否 | 否 | 厂商ID。 |
| productId | number | 否 | 否 | 产品ID。 |
| serial | string | 否 | 否 | 序列号。 |

## QueryPolicy

获取策略。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELF | 0 | 当前Admin设置的策略。 |
| ALL | 1 | 全部Admin设置的策略。 |

## ManagedFeature

管控特性。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL\_HOTA\_DOMAIN | 0 | 本机HOTA（Huawei Over-the-Air）域名。 |
| USER\_EXTEND\_CREDENTIAL | 1 | 扩展身份认证凭据。 |
| DEVICE\_SECURITY\_LEVEL | 2 | 设备安全等级。 |
| PRINTER\_IP\_ADDRESS\_POLICY | 3 | 打印机IP地址策略。 |
| OPTICAL\_DISC\_DRIVE\_BURN | 4 | 光驱刻录。 |
| EXACT\_TIMER | 5 | 精确定时器。 |
| EXEMPTION\_RESOURCE | 6 | 资源豁免。 |
| X\_KEY | 7 | X键。 |
| SYSTEM\_ROLLBACK | 8 | 系统回退。 |
| SUPER\_PRIVACY | 9 | 超级隐私模式。 |

## common.isFeatureSupported

isFeatureSupported(feature: ManagedFeature): boolean

查询是否支持某个管控特性。适用于企业设备管理应用在调用与设备形态相关的管控接口前，先确认当前设备是否支持对应特性，再进行差异化的业务处理，避免在不支持的设备上调用相关接口。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| feature | [ManagedFeature](js-apis-enterprise-common.md#managedfeature) | 是 | 管控特性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示支持该特性，false表示不支持该特性。 |

**示例：**

```ts
import { common, systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let domain: string = "https://www.hotaExample.com";
// 调用接口前，先使用本接口查询设备是否支持本机HOTA域名特性
let isSupported: boolean = common.isFeatureSupported(common.ManagedFeature.LOCAL_HOTA_DOMAIN);
if (isSupported) {
  try {
    systemManager.setLocalHotaDomain(wantTemp, domain);
    console.info('Succeeded in setting local HOTA domain.');
  } catch (err) {
    console.error(`Failed to set local HOTA domain. Code is ${err.code}, message is ${err.message}`);
  }
} else {
  console.info('The local HOTA domain feature is not supported.');
}
```
