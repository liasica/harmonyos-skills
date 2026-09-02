---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-7003
title: Network Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d2e4bfe00a01854268bded8423e884ff49c5dc1d5c65155926c2dda2a9d70a5d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：NetConnection；  API声明：unregister(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NetConnection；  API声明：unregister(callback: AsyncCallback<void>): void;  差异内容：201 | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.GET\_NETWORK\_STATS | 类名：statistics；  API声明：function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.GET\_NETWORK\_STATS [since 26.0.0] | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidRxBytes(uid: number): Promise<number>;  差异内容：ohos.permission.GET\_NETWORK\_STATS | 类名：statistics；  API声明：function getUidRxBytes(uid: number): Promise<number>;  差异内容：ohos.permission.GET\_NETWORK\_STATS [since 26.0.0] | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidTxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.GET\_NETWORK\_STATS | 类名：statistics；  API声明：function getUidTxBytes(uid: number, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.GET\_NETWORK\_STATS [since 26.0.0] | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics；  API声明：function getUidTxBytes(uid: number): Promise<number>;  差异内容：ohos.permission.GET\_NETWORK\_STATS | 类名：statistics；  API声明：function getUidTxBytes(uid: number): Promise<number>;  差异内容：ohos.permission.GET\_NETWORK\_STATS [since 26.0.0] | api/@ohos.net.statistics.d.ts |
| 新增kit | 类名：global；  API声明：api@system.fetch.d.ts  差异内容：NA | 类名：global；  API声明：api@system.fetch.d.ts  差异内容：NetworkKit | api/@system.fetch.d.ts |
| 新增kit | 类名：global；  API声明：api@system.network.d.ts  差异内容：NA | 类名：global；  API声明：api@system.network.d.ts  差异内容：NetworkKit | api/@system.network.d.ts |
