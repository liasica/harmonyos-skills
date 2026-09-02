---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-7001
title: Location Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Location Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:029e8e1ef401fa0b311c0c160d257a1fc5f0de84f9d26fa63f172de9c6256300
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：geoLocationManager；  API声明：function isGnssServiceSupported(): boolean;  差异内容：function isGnssServiceSupported(): boolean; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function isGnssFenceServiceSupported(): boolean;  差异内容：function isGnssFenceServiceSupported(): boolean; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function isCachedGnssServiceSupported(): boolean;  差异内容：function isCachedGnssServiceSupported(): boolean; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function findMatchingWlan(wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>;  差异内容：function findMatchingWlan(wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：additionalInfo?: string;  差异内容：additionalInfo?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface MatchingWlanInfo  差异内容：export interface MatchingWlanInfo | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：MatchingWlanInfo；  API声明：index: number;  差异内容：index: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：MatchingWlanInfo；  API声明：ssid: string;  差异内容：ssid: string; | api/@ohos.geoLocationManager.d.ts |
