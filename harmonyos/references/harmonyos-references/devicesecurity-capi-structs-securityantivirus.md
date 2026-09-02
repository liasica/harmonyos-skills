---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityantivirus
title: SecurityAntivirus_Antivirus
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 结构体 > SecurityAntivirus_Antivirus
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:28fcf32dc482106cc74f92806364b6937133eff0abfd638830fdc347cf314c70
---

## 概述

定义防病毒应用信息。

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAntivirus](devicesecurity-capi-securityantivirus.md)

**所在头文件：** [security\_antivirus.h](devicesecurity-capi-security-antivirus-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \*[bundleName](devicesecurity-capi-structs-securityantivirus.md#bundlename) | 防病毒应用包名 |
| const char \*[metadata](devicesecurity-capi-structs-securityantivirus.md#metadata) | 防病毒应用信息（当前版本号、上次更新时间、病毒防护开关状态、用户ID） |

## 结构体成员变量说明

### bundleName

```c
const char *SecurityAntivirus_Antivirus::bundleName
```

**描述**

防病毒应用包名，包名字段要求请参见[链接](../harmonyos-guides/app-configuration-file.md)。

### metadata

```c
const char *SecurityAntivirus_Antivirus::metadata
```

**描述**

防病毒应用信息（包含当前版本号、上次更新时间、病毒防护状态、用户ID的json字符串），其中版本号字段要求请参见[链接](../harmonyos-guides/app-configuration-file.md)，上次更新时间为10位秒级或13位毫秒级时间戳，病毒防护状态仅限on或off，user\_id为用户ID。示例格式如下：

```json
{
"version": "1.0.0.0",
"last_update_time": "1751877696",
"protection_status": "on/off",
"user_id": "100"
}
```
