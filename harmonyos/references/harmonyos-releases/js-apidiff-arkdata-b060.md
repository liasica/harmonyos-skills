---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-b060
title: ArkData
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta5引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:25+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7290f2e6d7d7cb7ff8e94c0d49bf3ff83ffddcbc8d7a5866c98693be5756fbd5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function insertData(options: Options, data: UnifiedData): Promise<string>;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function insertData(options: Options, data: UnifiedData): Promise<string>;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function updateData(options: Options, data: UnifiedData): Promise<void>;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function updateData(options: Options, data: UnifiedData): Promise<void>;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function queryData(options: Options): Promise<Array<UnifiedData>>;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function queryData(options: Options): Promise<Array<UnifiedData>>;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel；  API声明：function deleteData(options: Options): Promise<Array<UnifiedData>>;  差异内容：201,401 | 类名：unifiedDataChannel；  API声明：function deleteData(options: Options): Promise<Array<UnifiedData>>;  差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 权限变更 | 类名：relationalStore；  API声明： enum SubscribeType  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：relationalStore；  API声明： enum SubscribeType  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_REMOTE = 0  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_REMOTE = 0  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：relationalStore；  API声明： enum DistributedType  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：relationalStore；  API声明： enum DistributedType  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DistributedType；  API声明：DISTRIBUTED\_DEVICE  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：DistributedType；  API声明：DISTRIBUTED\_DEVICE  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
