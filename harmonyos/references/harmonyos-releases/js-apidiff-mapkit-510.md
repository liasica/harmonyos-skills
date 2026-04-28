---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-510
title: Map Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Map Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:11+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d8493c1073fcff1f1e18f7c06b4c81597806fc2e083797a84f161f0ae080e23c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：petalMaps；  API声明：function openMapHomePage(context: common.Context): Promise<void>;  差异内容：NA | 类名：petalMaps；  API声明：function openMapHomePage(context: common.Context): Promise<void>;  差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps；  API声明：function openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>;  差异内容：NA | 类名：petalMaps；  API声明：function openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>;  差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps；  API声明：function openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>;  差异内容：NA | 类名：petalMaps；  API声明：function openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>;  差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps；  API声明：function openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>;  差异内容：NA | 类名：petalMaps；  API声明：function openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>;  差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps；  API声明：function openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>;  差异内容：NA | 类名：petalMaps；  API声明：function openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>;  差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：sceneMap；  API声明：function queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise<void>;  差异内容：NA | 类名：sceneMap；  API声明：function queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise<void>;  差异内容：801 | api/@hms.core.map.sceneMap.d.ts |
| 新增错误码 | 类名：sceneMap；  API声明：function chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise<LocationChoosingResult>;  差异内容：NA | 类名：sceneMap；  API声明：function chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise<LocationChoosingResult>;  差异内容：801 | api/@hms.core.map.sceneMap.d.ts |
| 新增错误码 | 类名：sceneMap；  API声明：function selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>;  差异内容：NA | 类名：sceneMap；  API声明：function selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>;  差异内容：801 | api/@hms.core.map.sceneMap.d.ts |
| 属性变更 | 类名：MarkerOptions；  API声明：annotations?: Array<Text>;  差异内容：Array<Text> | 类名：MarkerOptions；  API声明：annotations?: Text[];  差异内容：Text[] | api/@hms.core.map.mapCommon.d.ts |
