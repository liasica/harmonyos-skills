---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisefoundationkit-26011
title: Enterprise Foundation Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Enterprise Foundation Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:96109cf0bb9b263fdc4819d22cf3e49b89f609bdb166483ba5731da679cbc048
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace enterpriseDeployRestore  差异内容：declare namespace enterpriseDeployRestore | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：enum DirectoryIdentifier  差异内容：enum DirectoryIdentifier | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：DirectoryIdentifier；  API声明：DOCUMENTS = 0  差异内容：DOCUMENTS = 0 | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：DirectoryIdentifier；  API声明：DOWNLOAD = 1  差异内容：DOWNLOAD = 1 | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：interface RestoreUserDataOptions  差异内容：interface RestoreUserDataOptions | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：RestoreUserDataOptions；  API声明：excludeDirIdentifiers?: DirectoryIdentifier[];  差异内容：excludeDirIdentifiers?: DirectoryIdentifier[]; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：interface BundleInfo  差异内容：interface BundleInfo | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：versionCode: number;  差异内容：versionCode: number; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：versionName: string;  差异内容：versionName: string; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：interface BackupRestoreProgressInfo  差异内容：interface BackupRestoreProgressInfo | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：BackupRestoreProgressInfo；  API声明：progress: number;  差异内容：progress: number; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：type BackupRestoreProgressCallback = (progressInfo: BackupRestoreProgressInfo) => void;  差异内容：type BackupRestoreProgressCallback = (progressInfo: BackupRestoreProgressInfo) => void; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function getUserBackupDataSize(): Promise<number>;  差异内容：function getUserBackupDataSize(): Promise<number>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function backupUserData(dest: string, progressCallback: BackupRestoreProgressCallback): Promise<void>;  差异内容：function backupUserData(dest: string, progressCallback: BackupRestoreProgressCallback): Promise<void>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function restoreUserData(src: string, progressCallback: BackupRestoreProgressCallback, options?: RestoreUserDataOptions): Promise<void>;  差异内容：function restoreUserData(src: string, progressCallback: BackupRestoreProgressCallback, options?: RestoreUserDataOptions): Promise<void>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function getAllowedBackupAndRestoreBundleList(): Promise<BundleInfo[]>;  差异内容：function getAllowedBackupAndRestoreBundleList(): Promise<BundleInfo[]>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function getBundlesBackupDataSize(bundleList: string[]): Promise<number>;  差异内容：function getBundlesBackupDataSize(bundleList: string[]): Promise<number>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function backupBundles(bundleList: string[], dest: string, progressCallback: BackupRestoreProgressCallback): Promise<void>;  差异内容：function backupBundles(bundleList: string[], dest: string, progressCallback: BackupRestoreProgressCallback): Promise<void>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function restoreBundles(bundleList: string[], src: string, progressCallback: BackupRestoreProgressCallback): Promise<void>;  差异内容：function restoreBundles(bundleList: string[], src: string, progressCallback: BackupRestoreProgressCallback): Promise<void>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增API | NA | 类名：enterpriseDeployRestore；  API声明：function cancelBackupRestore(): Promise<void>;  差异内容：function cancelBackupRestore(): Promise<void>; | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.pcService.enterpriseDeployRestore.d.ts  差异内容：EnterpriseFoundationKit | api/@hms.pcService.enterpriseDeployRestore.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.EnterpriseFoundationKit.d.ts  差异内容：EnterpriseFoundationKit | kits/@kit.EnterpriseFoundationKit.d.ts |
