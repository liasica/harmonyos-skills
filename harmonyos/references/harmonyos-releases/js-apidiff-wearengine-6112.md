---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-wearengine-6112
title: Wear Engine
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > Wear Engine
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:93940e8ba06503ece2f320c6d1f71705bd38eaaf09ecd70b7c359ab002c49d4f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：MonitorClient；  API声明：queryStatus(deviceRandomId: string, item: MonitorItem): Promise<MonitorData>;  差异内容：NA | 类名：MonitorClient；  API声明：queryStatus(deviceRandomId: string, item: MonitorItem): Promise<MonitorData>;  差异内容：801 | api/@hms.health.wearEngine.d.ts |
| 新增错误码 | 类名：MonitorClient；  API声明：subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>;  差异内容：NA | 类名：MonitorClient；  API声明：subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>;  差异内容：801 | api/@hms.health.wearEngine.d.ts |
| 新增错误码 | 类名：MonitorClient；  API声明：unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>;  差异内容：NA | 类名：MonitorClient；  API声明：unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>;  差异内容：801 | api/@hms.health.wearEngine.d.ts |
