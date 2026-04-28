---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityantivirus
title: SecurityAntivirus_Antivirus
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 结构体 > SecurityAntivirus_Antivirus
category: harmonyos-references
scraped_at: 2026-04-28T08:07:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:242b56042c105e386f0d9d891a7b9fac8c9ab5beda21c8ce8c34c3d797a1c10f
---

## 概述

PC/2in1

定义防病毒应用信息。

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAntivirus](devicesecurity-capi-securityantivirus.md)

**所在头文件：** [security\_antivirus.h](devicesecurity-capi-security-antivirus-8h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| const char \*[bundleName](devicesecurity-capi-structs-securityantivirus.md#bundlename) | 防病毒应用包名 |
| const char \*[metadata](devicesecurity-capi-structs-securityantivirus.md#metadata) | 防病毒应用信息（当前版本号、上次更新时间、病毒防护开关状态、用户ID） |

## 结构体成员变量说明

PC/2in1

### bundleName

PC/2in1

```
1. const char *SecurityAntivirus_Antivirus::bundleName
```

**描述**

防病毒应用包名，包名字段要求请参见[链接](../harmonyos-guides/app-configuration-file.md)。

### metadata

PC/2in1

```
1. const char *SecurityAntivirus_Antivirus::metadata
```

**描述**

防病毒应用信息（包含当前版本号、上次更新时间、病毒防护状态、用户ID的json字符串），其中版本号字段要求请参见[链接](../harmonyos-guides/app-configuration-file.md)，上次更新时间为10位秒级或13位毫秒级时间戳，病毒防护状态仅限on或off，user\_id为用户ID。示例格式如下：

```
1. {
2. "version": "1.0.0.0",
3. "last_update_time": "1751877696",
4. "protection_status": "on/off",
5. "user_id": "100"
6. }
```
