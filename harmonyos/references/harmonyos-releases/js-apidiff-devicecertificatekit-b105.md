---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-b105
title: Device Certificate Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9ac84f44ccd23e1270ef0440be5f46f92588f5088f3d92de2c57171a574b2f98
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace certificateManagerDialog  差异内容： declare namespace certificateManagerDialog | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明： export enum CertificateDialogErrorCode  差异内容： export enum CertificateDialogErrorCode | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode；  API声明：ERROR\_GENERIC = 29700001  差异内容：ERROR\_GENERIC = 29700001 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明： export enum CertificateDialogPageType  差异内容： export enum CertificateDialogPageType | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType；  API声明：PAGE\_MAIN = 1  差异内容：PAGE\_MAIN = 1 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType；  API声明：PAGE\_CA\_CERTIFICATE = 2  差异内容：PAGE\_CA\_CERTIFICATE = 2 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType；  API声明：PAGE\_CREDENTIAL = 3  差异内容：PAGE\_CREDENTIAL = 3 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType；  API声明：PAGE\_INSTALL\_CERTIFICATE = 4  差异内容：PAGE\_INSTALL\_CERTIFICATE = 4 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：function openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise<void>;  差异内容：function openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise<void>; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManager；  API声明：function getPrivateCertificates(): Promise<CMResult>;  差异内容：function getPrivateCertificates(): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
