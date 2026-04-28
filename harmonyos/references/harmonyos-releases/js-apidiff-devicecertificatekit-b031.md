---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-b031
title: Device Certificate Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Device Certificate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:2ae90b3dc814b400a38f2bc2b4ccd2319ad293745dfc4902a4dc057a751731c9
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：X509Cert；  API声明：getSubjectName(): DataBlob;  差异内容：19020001,19020002,19030001 | 类名：X509Cert；  API声明：getSubjectName(encodingType?: EncodingType): DataBlob;  差异内容：19020001,19020002,19030001,401 | api/@ohos.security.cert.d.ts |
| 函数变更 | 类名：X509Cert；  API声明：getSubjectName(): DataBlob;  差异内容：NA | 类名：X509Cert；  API声明：getSubjectName(encodingType?: EncodingType): DataBlob;  差异内容：encodingType?: EncodingType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert；  API声明： enum EncodingType  差异内容： enum EncodingType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：EncodingType；  API声明：ENCODING\_UTF8 = 0  差异内容：ENCODING\_UTF8 = 0 | api/@ohos.security.cert.d.ts |
