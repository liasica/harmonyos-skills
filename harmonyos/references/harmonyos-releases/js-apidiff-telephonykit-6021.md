---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-6021
title: Telephony Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:49+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a6307b53f99400f9a699a8854f16460f0594ec1442ed037bb7422a3fb42546e5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：data；  API声明：function getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void;  差异内容：NA | 类名：data；  API声明：function getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void;  差异内容：201 | api/@ohos.telephony.data.d.ts |
| 新增错误码 | 类名：data；  API声明：function getCellularDataFlowType(): Promise<DataFlowType>;  差异内容：NA | 类名：data；  API声明：function getCellularDataFlowType(): Promise<DataFlowType>;  差异内容：201 | api/@ohos.telephony.data.d.ts |
| 新增错误码 | 类名：data；  API声明：function getCellularDataState(callback: AsyncCallback<DataConnectState>): void;  差异内容：NA | 类名：data；  API声明：function getCellularDataState(callback: AsyncCallback<DataConnectState>): void;  差异内容：201 | api/@ohos.telephony.data.d.ts |
| 新增错误码 | 类名：data；  API声明：function getCellularDataState(): Promise<DataConnectState>;  差异内容：NA | 类名：data；  API声明：function getCellularDataState(): Promise<DataConnectState>;  差异内容：201 | api/@ohos.telephony.data.d.ts |
| 权限变更 | 类名：data；  API声明：function getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void;  差异内容：NA | 类名：data；  API声明：function getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void;  差异内容：ohos.permission.GET\_NETWORK\_INFO | api/@ohos.telephony.data.d.ts |
| 权限变更 | 类名：data；  API声明：function getCellularDataFlowType(): Promise<DataFlowType>;  差异内容：NA | 类名：data；  API声明：function getCellularDataFlowType(): Promise<DataFlowType>;  差异内容：ohos.permission.GET\_NETWORK\_INFO | api/@ohos.telephony.data.d.ts |
| 权限变更 | 类名：data；  API声明：function getCellularDataState(callback: AsyncCallback<DataConnectState>): void;  差异内容：NA | 类名：data；  API声明：function getCellularDataState(callback: AsyncCallback<DataConnectState>): void;  差异内容：ohos.permission.GET\_NETWORK\_INFO | api/@ohos.telephony.data.d.ts |
| 权限变更 | 类名：data；  API声明：function getCellularDataState(): Promise<DataConnectState>;  差异内容：NA | 类名：data；  API声明：function getCellularDataState(): Promise<DataConnectState>;  差异内容：ohos.permission.GET\_NETWORK\_INFO | api/@ohos.telephony.data.d.ts |
