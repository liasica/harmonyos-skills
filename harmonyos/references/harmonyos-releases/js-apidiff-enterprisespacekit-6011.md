---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisespacekit-6011
title: Enterprise Space Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Enterprise Space Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:59+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b2b629ffe05f8e5d5a667c71733b08932e294ca0d61ce1e183a82c8fb1a8a987
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：spaceManager；  API声明：interface ProcessConfigInfo  差异内容：interface ProcessConfigInfo | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：ProcessConfigInfo；  API声明：processName: string;  差异内容：processName: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：ProcessConfigInfo；  API声明：disallowPaths: string[];  差异内容：disallowPaths: string[]; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：enum UserDataEnum  差异内容：enum UserDataEnum | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：UserDataEnum；  API声明：ENTERPRISE = 0  差异内容：ENTERPRISE = 0 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：UserDataEnum；  API声明：PERSONAL = 1  差异内容：PERSONAL = 1 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise<void>;  差异内容：function setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise<void>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise<boolean>;  差异内容：function getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise<boolean>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>;  差异内容：function getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise<void>;  差异内容：function addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise<void>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string): Promise<void>;  差异内容：function deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string): Promise<void>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
