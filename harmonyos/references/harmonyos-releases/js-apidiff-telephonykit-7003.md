---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-7003
title: Telephony Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d4f8cd60f2d9a1551deb807b4f15a60a827d5d6061e2d20f7187a6c04713c175
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：data；  API声明：function getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void;  差异内容：ohos.permission.GET\_NETWORK\_INFO | 类名：data；  API声明：function getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void;  差异内容：ohos.permission.GET\_NETWORK\_INFO [since 22] | api/@ohos.telephony.data.d.ts |
| 权限变更 | 类名：data；  API声明：function getCellularDataFlowType(): Promise<DataFlowType>;  差异内容：ohos.permission.GET\_NETWORK\_INFO | 类名：data；  API声明：function getCellularDataFlowType(): Promise<DataFlowType>;  差异内容：ohos.permission.GET\_NETWORK\_INFO [since 22] | api/@ohos.telephony.data.d.ts |
| 权限变更 | 类名：data；  API声明：function getCellularDataState(callback: AsyncCallback<DataConnectState>): void;  差异内容：ohos.permission.GET\_NETWORK\_INFO | 类名：data；  API声明：function getCellularDataState(callback: AsyncCallback<DataConnectState>): void;  差异内容：ohos.permission.GET\_NETWORK\_INFO [since 22] | api/@ohos.telephony.data.d.ts |
| 权限变更 | 类名：data；  API声明：function getCellularDataState(): Promise<DataConnectState>;  差异内容：ohos.permission.GET\_NETWORK\_INFO | 类名：data；  API声明：function getCellularDataState(): Promise<DataConnectState>;  差异内容：ohos.permission.GET\_NETWORK\_INFO [since 22] | api/@ohos.telephony.data.d.ts |
