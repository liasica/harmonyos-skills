---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-wearengine-6111
title: Wear Engine Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Wear Engine Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:702676c1faaf8a16254dcfb36162722d4ad2d2c5b126ee201f01a76bd9877fb4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：wearEngine；  API声明：enum EntryType  差异内容：enum EntryType | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：EntryType；  API声明：DISTRIBUTED\_SERVICE = 'DistributedService'  差异内容：DISTRIBUTED\_SERVICE = 'DistributedService' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：EntryType；  API声明：SERVICE = 'Service'  差异内容：SERVICE = 'Service' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：EntryType；  API声明：UI = 'UI'  差异内容：UI = 'UI' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pFile；  API声明：progress?: number;  差异内容：progress?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine；  API声明：interface StartConfig  差异内容：interface StartConfig | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：StartConfig；  API声明：entryType: EntryType;  差异内容：entryType: EntryType; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：StartConfig；  API声明：entryName?: string;  差异内容：entryName?: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient；  API声明：registerFileReceiverWithProgress(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>;  差异内容：registerFileReceiverWithProgress(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorItem；  API声明：SPORT\_STATUS = 'sportStatus'  差异内容：SPORT\_STATUS = 'sportStatus' | api/@hms.health.wearEngine.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：P2pClient；  API声明：startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise<P2pResult>;  差异内容：startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise<P2pResult>; | 类名：P2pClient；  API声明：startRemoteApp(deviceRandomId: string, remoteApp: AppInfo, startConfig: StartConfig): Promise<P2pResult>;  差异内容：startRemoteApp(deviceRandomId: string, remoteApp: AppInfo, startConfig: StartConfig): Promise<P2pResult>; | api/@hms.health.wearEngine.d.ts |
