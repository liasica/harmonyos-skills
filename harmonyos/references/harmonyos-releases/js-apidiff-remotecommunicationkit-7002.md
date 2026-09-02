---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-remotecommunicationkit-7002
title: Remote Communication Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Remote Communication Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7e57d1f7dedf1b4f32ec7957b5b3ac0dd590797524401315b0e8959e7e41c9ea
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：TracingConfiguration；  API声明：plaintextInException?: boolean;  差异内容：plaintextInException?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type CertificateDecompress = 'zlib' | 'brotli';  差异内容：export type CertificateDecompress = 'zlib' | 'brotli'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type SecurityLayerType = 'ssl-tls' | 'tlcp';  差异内容：export type SecurityLayerType = 'ssl-tls' | 'tlcp'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：SecurityConfiguration；  API声明：certificateEnc?: ClientCertificate;  差异内容：certificateEnc?: ClientCertificate; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：SecurityConfiguration；  API声明：securityLayerType?: SecurityLayerType;  差异内容：securityLayerType?: SecurityLayerType; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：SecurityConfiguration；  API声明：certificateDecompress?: CertificateDecompress | CertificateDecompress[];  差异内容：certificateDecompress?: CertificateDecompress | CertificateDecompress[]; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type SessionPathPreference = 'auto' | 'cellular-if-could' | 'mptcp';  差异内容：export type SessionPathPreference = 'auto' | 'cellular-if-could' | 'mptcp'; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：SessionConfiguration；  API声明：sessionPathPreference?: SessionPathPreference;  差异内容：sessionPathPreference?: SessionPathPreference; | api/@hms.collaboration.rcp.d.ts |
