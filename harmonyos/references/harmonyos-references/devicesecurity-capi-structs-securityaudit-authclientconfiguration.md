---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-authclientconfiguration
title: SecurityAudit_AuthClientConfiguration
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 结构体 > SecurityAudit_AuthClientConfiguration
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d328f561b5f827d20b43cee96f5492bce1bdc34263edbb2891140889b24ac632
---

## 概述

该结构体定义了创建阻断类客户端时可配置的默认阻断策略。

**起始版本：** 26.0.0

**相关模块：** [SecurityAudit](devicesecurity-capi-securityaudit.md)

**所在头文件：** [security\_audit.h](devicesecurity-capi-security-audit-8h.md)

## 汇总

### 成员变量

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| timeoutAuthResult | [SecurityAudit\_AuthResult](devicesecurity-capi-securityaudit.md#securityaudit_authresult) | 设置阻断事件响应超时时的默认阻断结果。  - SECURITY\_AUDIT\_AUTH\_RESULT\_ALLOW：超时放行  - SECURITY\_AUDIT\_AUTH\_RESULT\_DENY：超时阻断 |
