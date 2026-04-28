---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-filemanagerservicekit-5051
title: File Manager Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > API变更清单 > File Manager Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:849684dfd047c05ac43ae809baf386b2d27a3f4390eb5f8bb81c1e96748ce51d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace fileManagerService  差异内容：declare namespace fileManagerService | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增API | NA | 类名：fileManagerService；  API声明：function deleteToTrash(uri: string): Promise<string>;  差异内容：function deleteToTrash(uri: string): Promise<string>; | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增API | NA | 类名：fileManagerService；  API声明：function getFileIconSync(fileType: string): string | Resource;  差异内容：function getFileIconSync(fileType: string): string | Resource; | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增API | NA | 类名：fileManagerService；  API声明：function getFileIcon(fileType: string): Promise<string | Resource>;  差异内容：function getFileIcon(fileType: string): Promise<string | Resource>; | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.filemanagement.fileManagerService.d.ts  差异内容：FileManagerServiceKit | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.FileManagerServiceKit.d.ts  差异内容：FileManagerServiceKit | kits/@kit.FileManagerServiceKit.d.ts |
