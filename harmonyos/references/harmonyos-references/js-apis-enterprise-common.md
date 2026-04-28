---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-common
title: @ohos.enterprise.common（Enterprise公共模块）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.common（Enterprise公共模块）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bb13d3169d76c722215d56ef66d8bfd001984f07981393d23d47cdfb44969586
---

本模块提供MDM Kit中常用公共能力的纯类型定义，包含枚举类型和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1Tablet

```
1. import { common } from '@kit.MDMKit';
```

## ManagedPolicy

PhonePC/2in1Tablet

企业设备管控策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认，无管控策略。 |
| DISALLOW | 1 | 禁用。 |
| FORCE\_OPEN | 2 | 强制开启。 |

## ApplicationInstance

PhonePC/2in1Tablet

应用的实例数据。

该接口目前在[addUserNonStopApps](js-apis-enterprise-applicationmanager.md#applicationmanageraddusernonstopapps22)、[removeUserNonStopApps](js-apis-enterprise-applicationmanager.md#applicationmanagerremoveusernonstopapps22)、[addFreezeExemptedApps](js-apis-enterprise-applicationmanager.md#applicationmanageraddfreezeexemptedapps22)、[removeFreezeExemptedApps](js-apis-enterprise-applicationmanager.md#applicationmanagerremovefreezeexemptedapps22)接口中作为入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appIdentifier | string | 否 | 否 | 应用[唯一标识符](js-apis-bundlemanager-bundleinfo.md#signatureinfo)，可以通过接口[bundleManager.getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14-2)获取bundleInfo.signatureInfo.appIdentifier。 |
| accountId | number | 否 | 否 | 用户ID。取值范围：大于等于0的整数。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)接口获取。 |
| appIndex | number | 否 | 否 | 应用分身索引。取值范围：大于等于0的整数。  appIndex可以通过[getAppCloneIdentity](js-apis-bundlemanager.md#bundlemanagergetappcloneidentity14)接口获取。 |

## InstallationResult

PhonePC/2in1Tablet

应用安装结果。

该对象目前在[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](js-apis-enterpriseadminextensionability.md#onmarketappinstallresult22)作为回调入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | [Result](js-apis-enterprise-common.md#result) | 否 | 否 | 应用安装结果码。 |
| message | string | 否 | 否 | 应用安装结果消息。 |

## Result

PhonePC/2in1Tablet

应用安装结果码。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 应用安装成功。 |
| FAIL | -1 | 应用安装失败。 |

## EnterpriseAdminExtensionContext23+

PhonePC/2in1Tablet

type EnterpriseAdminExtensionContext = \_EnterpriseAdminExtensionContext.default

EnterpriseAdminExtensionContext是[EnterpriseAdminExtensionAbility](js-apis-enterpriseadminextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**系统能力**: SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_EnterpriseAdminExtensionContext.default](s-apis-application-enterpriseadminextensioncontext.md) | EnterpriseAdminExtensionAbility组件的上下文。 |
