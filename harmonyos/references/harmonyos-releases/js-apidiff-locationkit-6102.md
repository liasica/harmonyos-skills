---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-6102
title: Location Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta2引入的变更 > Location Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f881b51c32d8accf5a139389f7c9654c7515ccc5205f603abafae103611507f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：GeolocationResponse；  API声明：longitude: number;  差异内容：NA | 类名：GeolocationResponse；  API声明：longitude: number;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GeolocationResponse；  API声明：latitude: number;  差异内容：NA | 类名：GeolocationResponse；  API声明：latitude: number;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GeolocationResponse；  API声明：altitude: number;  差异内容：NA | 类名：GeolocationResponse；  API声明：altitude: number;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GeolocationResponse；  API声明：accuracy: number;  差异内容：NA | 类名：GeolocationResponse；  API声明：accuracy: number;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GeolocationResponse；  API声明：time: number;  差异内容：NA | 类名：GeolocationResponse；  API声明：time: number;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationOption；  API声明：timeout?: number;  差异内容：NA | 类名：GetLocationOption；  API声明：timeout?: number;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationOption；  API声明：coordType?: string;  差异内容：NA | 类名：GetLocationOption；  API声明：coordType?: string;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationOption；  API声明：success?: (data: GeolocationResponse) => void;  差异内容：NA | 类名：GetLocationOption；  API声明：success?: (data: GeolocationResponse) => void;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationOption；  API声明：fail?: (data: string, code: number) => void;  差异内容：NA | 类名：GetLocationOption；  API声明：fail?: (data: string, code: number) => void;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationOption；  API声明：complete?: () => void;  差异内容：NA | 类名：GetLocationOption；  API声明：complete?: () => void;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationTypeResponse；  API声明：types: Array<string>;  差异内容：NA | 类名：GetLocationTypeResponse；  API声明：types: Array<string>;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationTypeOption；  API声明：success?: (data: GetLocationTypeResponse) => void;  差异内容：NA | 类名：GetLocationTypeOption；  API声明：success?: (data: GetLocationTypeResponse) => void;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationTypeOption；  API声明：fail?: (data: string, code: number) => void;  差异内容：NA | 类名：GetLocationTypeOption；  API声明：fail?: (data: string, code: number) => void;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：GetLocationTypeOption；  API声明：complete?: () => void;  差异内容：NA | 类名：GetLocationTypeOption；  API声明：complete?: () => void;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：SubscribeLocationOption；  API声明：coordType?: string;  差异内容：NA | 类名：SubscribeLocationOption；  API声明：coordType?: string;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：SubscribeLocationOption；  API声明：success: (data: GeolocationResponse) => void;  差异内容：NA | 类名：SubscribeLocationOption；  API声明：success: (data: GeolocationResponse) => void;  差异内容：9 | api/@system.geolocation.d.ts |
| API废弃版本变更 | 类名：SubscribeLocationOption；  API声明：fail?: (data: string, code: number) => void;  差异内容：NA | 类名：SubscribeLocationOption；  API声明：fail?: (data: string, code: number) => void;  差异内容：9 | api/@system.geolocation.d.ts |
