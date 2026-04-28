---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-b065
title: Device Security Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0b8162e585664c9f12187344358046bc524056127c346ab609d9ba7bd3ebb76f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace securityAudit  差异内容： declare namespace securityAudit | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明： interface AuditEvent  差异内容： interface AuditEvent | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent；  API声明：eventId: number;  差异内容：eventId: number; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent；  API声明：version?: string;  差异内容：version?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent；  API声明：timestamp?: string;  差异内容：timestamp?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent；  API声明：content?: string;  差异内容：content?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent；  API声明：userId?: number;  差异内容：userId?: number; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent；  API声明：deviceId?: string;  差异内容：deviceId?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明： interface AuditEventInfo  差异内容： interface AuditEventInfo | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEventInfo；  API声明：eventId: number;  差异内容：eventId: number; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void;  差异内容：function on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit；  API声明：function off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void;  差异内容：function off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void; | api/@hms.security.securityAudit.d.ts |
