---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-b065
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:474fa725cf3a2f7649dd11baf2e4e2cdd334a42fa3b0d7e6ec224932a2f5ae25
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：wifiManager；  API声明：function getLinkedInfo(): Promise<WifiLinkedInfo>;  差异内容：201,202,2501000,2501001,801 | 类名：wifiManager；  API声明：function getLinkedInfo(): Promise<WifiLinkedInfo>;  差异内容：201,2501000,2501001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：201,202,2501000,2501001,801 | 类名：wifiManager；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：201,2501000,2501001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function isConnected(): boolean;  差异内容：201,202,2501000,801 | 类名：wifiManager；  API声明：function isConnected(): boolean;  差异内容：201,2501000,801 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： enum WifiCategory  差异内容： enum WifiCategory | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory；  API声明：DEFAULT = 1  差异内容：DEFAULT = 1 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory；  API声明：WIFI6 = 2  差异内容：WIFI6 = 2 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory；  API声明：WIFI6\_PLUS = 3  差异内容：WIFI6\_PLUS = 3 | api/@ohos.wifiManager.d.ts |
