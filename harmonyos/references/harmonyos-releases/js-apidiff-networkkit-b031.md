---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-b031
title: Network Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c9ff6e8cf2f1fbf796d17e3419ae53b889626c3c7b88ab062873804233ffa106
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：certificatePinning?: CertificatePinning | CertificatePinning[];  差异内容：certificatePinning?: CertificatePinning | CertificatePinning[]; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http；  API声明： interface CertificatePinning  差异内容： interface CertificatePinning | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：CertificatePinning；  API声明：publicKeyHash: string;  差异内容：publicKeyHash: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：CertificatePinning；  API声明：hashAlgorithm: 'SHA-256';  差异内容：hashAlgorithm: 'SHA-256'; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：UDPSocket；  API声明：getLocalAddress(): Promise<NetAddress>;  差异内容：getLocalAddress(): Promise<NetAddress>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket；  API声明：getLocalAddress(): Promise<string>;  差异内容：getLocalAddress(): Promise<string>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection；  API声明：getLocalAddress(): Promise<string>;  差异内容：getLocalAddress(): Promise<string>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer；  API声明：getLocalAddress(): Promise<string>;  差异内容：getLocalAddress(): Promise<string>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocket；  API声明：getLocalAddress(): Promise<NetAddress>;  差异内容：getLocalAddress(): Promise<NetAddress>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocket；  API声明：getLocalAddress(): Promise<NetAddress>;  差异内容：getLocalAddress(): Promise<NetAddress>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection；  API声明：getLocalAddress(): Promise<NetAddress>;  差异内容：getLocalAddress(): Promise<NetAddress>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer；  API声明：getLocalAddress(): Promise<NetAddress>;  差异内容：getLocalAddress(): Promise<NetAddress>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection；  API声明：getLocalAddress(): Promise<NetAddress>;  差异内容：getLocalAddress(): Promise<NetAddress>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer；  API声明：getLocalAddress(): Promise<NetAddress>;  差异内容：getLocalAddress(): Promise<NetAddress>; | api/@ohos.net.socket.d.ts |
