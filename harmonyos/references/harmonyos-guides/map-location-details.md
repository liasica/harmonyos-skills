---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-details
title: 地点详情展示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 地点详情展示
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a55db667a37d61d75209a4b21f0cfccdfb5117cb61e789eaadd958c88889d7b5
---

## 场景介绍

本章节介绍如何集成地点详情展示控件。该控件提供便捷的地点详情展示功能以及导航和打车服务入口，开发者无需自行开发地图页面，即可实现用户点击“路线”按钮启动导航，或点击“打车”按钮发起打车。

**图1** 地点详情

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/zOZqx8f2TyCrHImjN0sjPg/zh-cn_image_0000002589245357.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053916Z&HW-CC-Expire=86400&HW-CC-Sign=CC0052AF69093B8D5957FFBA70D9BF01F47FCD0462E66F6F711B3957ED71634D "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 仅支持手机、平板和2in1设备。

## 接口说明

地点详情控件功能主要由[sceneMap](../harmonyos-references/map-scenemap.md)命名空间下的[queryLocation](../harmonyos-references/map-scenemap.md#querylocation)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-scenemap.md)。

| 接口名 | 描述 |
| --- | --- |
| [LocationQueryOptions](../harmonyos-references/map-scenemap.md#locationqueryoptions) | 查询地点详情的参数。 |
| [queryLocation](../harmonyos-references/map-scenemap.md#querylocation)(context: common.[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), options: [LocationQueryOptions](../harmonyos-references/map-scenemap.md#locationqueryoptions)): Promise<void> | 查询地点详情。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { sceneMap } from '@kit.MapKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   ```
2. 创建查询地点详情参数，调用[queryLocation](../harmonyos-references/map-scenemap.md#querylocation)方法拉起地点详情页。

   ```
   1. // 方式一：传入siteId
   2. let queryLocationOptions: sceneMap.LocationQueryOptions = {
   3. siteId: "922207154068557824"
   4. };
   5. // 拉起地点详情页
   6. sceneMap.queryLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, queryLocationOptions)
   7. .then(() => {
   8. console.info("QueryLocation", "Succeeded in querying location.");
   9. })
   10. .catch((err: BusinessError) => {
   11. console.error("QueryLocation", `Failed to query Location, code: ${err.code}, message: ${err.message}`);
   12. });

   14. // 方式二：传入location和name
   15. let queryLocationOptions: sceneMap.LocationQueryOptions = {
   16. location: {
   17. latitude: 39.9175,
   18. longitude: 116.3972
   19. },
   20. name: '故宫博物院'
   21. };
   22. // 拉起地点详情页
   23. sceneMap.queryLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, queryLocationOptions)
   24. .then(() => {
   25. console.info("QueryLocation", "Succeeded in querying location.");
   26. })
   27. .catch((err: BusinessError) => {
   28. console.error("QueryLocation", `Failed to query Location, code: ${err.code}, message: ${err.message}`);
   29. });
   ```
