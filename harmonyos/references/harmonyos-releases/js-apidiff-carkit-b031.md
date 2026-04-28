---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-carkit-b031
title: Car Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Car Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:37+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:81a99ddc5b6be590f97bc88a415bd52747cd30ca5ff1b548192ef79fbf8bf23b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：SystemNavigationListener；  API声明：onQueryNavigationInfo(query: QueryType, args: {  [key: string]: object;  }): Promise<ResultData>;  差异内容：args: {  [key: string]: object;  } | 类名：SystemNavigationListener；  API声明：onQueryNavigationInfo(query: QueryType, args: Record<string, Object>): Promise<ResultData>;  差异内容：args: Record<string, Object> | api/@hms.carService.navigationInfoMgr.d.ts |
| 函数变更 | 类名：SystemNavigationListener；  API声明：onReceiveNavigationCmd(command: CommandType, args: {  [key: string]: object;  }): Promise<ResultData>;  差异内容：args: {  [key: string]: object;  } | 类名：SystemNavigationListener；  API声明：onReceiveNavigationCmd(command: CommandType, args: Record<string, Object>): Promise<ResultData>;  差异内容：args: Record<string, Object> | api/@hms.carService.navigationInfoMgr.d.ts |
