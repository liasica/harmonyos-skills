---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-antivirus-8h
title: security_antivirus.h
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 头文件 > security_antivirus.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4aef63c91529996767469897f522500c7d82b065738d3d75f63b299b30b9ee74
---

## 概述

PC/2in1

文件中定义了与病毒防护服务管理相关的函数。

**引用文件：** <DeviceSecurityKit/security\_antivirus.h>

**库：** libsecurityantivirus\_ndk.z.so

**系统能力：** SystemCapability.Security.SecurityAntivirus

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAntivirus](devicesecurity-capi-securityantivirus.md)

## 汇总

PC/2in1

### 结构体

PC/2in1

| 名称 | 描述 |
| --- | --- |
| struct [SecurityAntivirus\_Antivirus](devicesecurity-capi-structs-securityantivirus.md) | 定义病毒防护服务应用信息，包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID。 |

### 枚举

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [SecurityAntivirus\_ErrCode](devicesecurity-capi-securityantivirus.md#securityantivirus_errcode){  SECURITY\_ANTIVIRUS\_SUCCESS = 0,  SECURITY\_ANTIVIRUS\_PERMISSION\_NOT\_GRANTED = 201,  SECURITY\_ANTIVIRUS\_PARAM\_INVALID = 1019900001,  SECURITY\_ANTIVIRUS\_NO\_REGISTER = 1019900002,  SECURITY\_ANTIVIRUS\_INNER\_ERROR = 1019900003  } | 定义病毒防护服务管理错误码。 |

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_RegisterAntivirus](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_registerantivirus)(const char\* bundleName) | 三方EDR应用向HarmonyOS安全防护服务注册。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_UnregisterAntivirus](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_unregisterantivirus)(const char\* bundleName) | 三方EDR应用从HarmonyOS安全防护服务注销。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_UpdateAntivirus](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_updateantivirus)(const [SecurityAntivirus\_Antivirus](devicesecurity-capi-structs-securityantivirus.md)\* antivirus) | 三方EDR应用向HarmonyOS安全防护服务更新信息，包含包名、当前版本号、上次更新时间、病毒防护开关状态、用户ID。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_QueryAntivirus](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_queryantivirus)([SecurityAntivirus\_Antivirus](devicesecurity-capi-structs-securityantivirus.md)\*\* list, uint32\_t\* length) | 零信任应用向HarmonyOS安全防护服务查询当前所有三方EDR注册信息。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_querypreinstalledantivirus)([SecurityAntivirus\_Antivirus](devicesecurity-capi-structs-securityantivirus.md)\*\* list, uint32\_t\* length) | MDM应用向HarmonyOS安全防护服务查询所有用户的防病毒功能状态。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_enablepreinstalledantivirus)(void) | MDM应用启用HarmonyOS安全防护服务所有用户的防病毒功能。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_disablepreinstalledantivirus)(void) | MDM应用禁用HarmonyOS安全防护服务所有用户的防病毒功能。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_enablepreinstalledantivirusbyaccount)(int32\_t accountId) | MDM应用启用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。 |
| SecurityAntivirus\_ErrCode [HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount](devicesecurity-capi-securityantivirus.md#hms_securityantivirus_disablepreinstalledantivirusbyaccount)(int32\_t accountId) | MDM应用禁用HarmonyOS安全防护服务中用户ID为accountId的防病毒功能。 |
