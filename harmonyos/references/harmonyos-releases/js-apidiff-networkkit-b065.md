---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-b065
title: Network Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:69db074389a0b8145cb388a5e3c9678e89e87211561438e8a876e141864e2a60
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：networkSecurity；  API声明：export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>;  差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305023,2305024,2305027,401 | 类名：networkSecurity；  API声明：export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>;  差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305018,2305023,2305024,2305027,2305069,401 | api/@ohos.net.networkSecurity.d.ts |
| 错误码变更 | 类名：networkSecurity；  API声明：export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number;  差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305023,2305024,2305027,401 | 类名：networkSecurity；  API声明：export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number;  差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305018,2305023,2305024,2305027,2305069,401 | api/@ohos.net.networkSecurity.d.ts |
| 错误码变更 | 类名：WebSocket；  API声明：connect(url: string, callback: AsyncCallback<boolean>): void;  差异内容：201,401 | 类名：WebSocket；  API声明：connect(url: string, callback: AsyncCallback<boolean>): void;  差异内容：201,2302001,2302002,2302003,2302999,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket；  API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void;  差异内容：201,401 | 类名：WebSocket；  API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void;  差异内容：201,2302001,2302002,2302003,2302999,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket；  API声明：connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>;  差异内容：201,401 | 类名：WebSocket；  API声明：connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>;  差异内容：201,2302001,2302002,2302003,2302999,401 | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：NetCap；  API声明：NET\_CAPABILITY\_CHECKING\_CONNECTIVITY = 31  差异内容：NET\_CAPABILITY\_CHECKING\_CONNECTIVITY = 31 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetBearType；  API声明：BEARER\_BLUETOOTH = 2  差异内容：BEARER\_BLUETOOTH = 2 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TLSSecureOptions；  API声明：isBidirectionalAuthentication?: boolean;  差异内容：isBidirectionalAuthentication?: boolean; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSConnectOptions；  API声明：skipRemoteValidation?: boolean;  差异内容：skipRemoteValidation?: boolean; | api/@ohos.net.socket.d.ts |
