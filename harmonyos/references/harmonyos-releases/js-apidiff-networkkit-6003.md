---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-6003
title: Network Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:20+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:191339e72cd94e09a30d961dda6cbabdab28de32e45567981696b7a16e90fca0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：LocalSocketServer；  API声明：close(): Promise<void>;  差异内容：close(): Promise<void>; | api/@ohos.net.socket.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：TCPSocketServer；  API声明：close(): Promise<void>;  差异内容：close(): Promise<void>; | api/@ohos.net.socket.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：TLSSocketServer；  API声明：close(): Promise<void>;  差异内容：close(): Promise<void>; | api/@ohos.net.socket.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RouteInfo；  API声明：isExcludedRoute?: boolean;  差异内容：isExcludedRoute?: boolean; | api/@ohos.net.connection.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HttpRequestOptions；  API声明：caData?: string;  差异内容：caData?: string; | api/@ohos.net.http.d.ts |
