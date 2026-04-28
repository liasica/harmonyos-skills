---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisespacekit-6001
title: Enterprise Space Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Enterprise Space Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:cedd6ff9663db5fcd8c72e17838baec6854b5568260476d7f5de6064b980ffc7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace fileTransfer  差异内容：declare namespace fileTransfer | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：fileTransfer；  API声明：interface AuditInfo  差异内容：interface AuditInfo | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：AuditInfo；  API声明：auditId: string;  差异内容：auditId: string; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：AuditInfo；  API声明：userId: string;  差异内容：userId: string; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：AuditInfo；  API声明：userName: string;  差异内容：userName: string; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：AuditInfo；  API声明：time: number;  差异内容：time: number; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：AuditInfo；  API声明：comments: string;  差异内容：comments: string; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：AuditInfo；  API声明：status: string;  差异内容：status: string; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：fileTransfer；  API声明：function getAuditInfo(transactionNum: string): AuditInfo;  差异内容：function getAuditInfo(transactionNum: string): AuditInfo; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增API | NA | 类名：fileTransfer；  API声明：function setAuditInfo(transactionNum: string, info: AuditInfo): number;  差异内容：function setAuditInfo(transactionNum: string, info: AuditInfo): number; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.enterpriseSpaceService.fileTransfer.d.ts  差异内容：EnterpriseSpaceKit | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.EnterpriseSpaceKit.d.ts  差异内容：EnterpriseSpaceKit | kits/@kit.EnterpriseSpaceKit.d.ts |
