---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-b123sp18
title: Device Certificate Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:50+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:17a038793b7624caa6667b30047eedb98a226c150b75c83366ae6b8ec7bf3e96
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：CertificateDialogErrorCode；  API声明：ERROR\_OPERATION\_CANCELED = 29700002  差异内容：ERROR\_OPERATION\_CANCELED = 29700002 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode；  API声明：ERROR\_OPERATION\_FAILED = 29700003  差异内容：ERROR\_OPERATION\_FAILED = 29700003 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode；  API声明：ERROR\_DEVICE\_NOT\_SUPPORTED = 29700004  差异内容：ERROR\_DEVICE\_NOT\_SUPPORTED = 29700004 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明： export enum CertificateType  差异内容： export enum CertificateType | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateType；  API声明：CA\_CERT = 1  差异内容：CA\_CERT = 1 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明： export enum CertificateScope  差异内容： export enum CertificateScope | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateScope；  API声明：CURRENT\_USER = 1  差异内容：CURRENT\_USER = 1 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog；  API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>;  差异内容：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>; | api/@ohos.security.certManagerDialog.d.ts |
