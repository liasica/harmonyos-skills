---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-2
title: 搜索的地理位置信息不符合用户期望
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 搜索的地理位置信息不符合用户期望
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:924ec5202f17b13292c4acb16dd265c2c0af83a168d89bd10ff7755e7a94f3cf
---

## 问题现象

打开应用进入相关位置搜索界面，输入关键词搜索对应位置信息，返回结果不符合用户实际预期。如在特定的地区搜索，但返回的位置信息不在该地区等现象。

## 背景知识

[Map Kit（地图服务）](../harmonyos-guides/map-introduction.md)：为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化显示地图、位置搜索和路径规划等功能，轻松完成地图构建工作。可以轻松地在HarmonyOS应用/元服务中集成地图相关的功能，全方位提升用户体验（[Map Kit相关API](../harmonyos-references/map-api.md)）。

* [地图交互](../harmonyos-guides/map-interaction.md)：主要分为控件交互、手势交互、事件交互、更改地图位置和地图截图。
* 在地图上绘制：
  1. [标记](../harmonyos-guides/map-marker.md)：标记是指在地图的指定位置添加标记以标识位置、商家、建筑等。
  2. [点注释](../harmonyos-guides/map-annotation.md)：点注释是指在地图的指定位置添加点注释以标识位置、商家、建筑等，并可以通过信息窗口展示详细信息。
* [位置搜索](../harmonyos-guides/map-location-services.md)：site（地点搜索）模块提供地点搜索服务，其中POI搜索提供了关键字搜索、周边搜索、自动补全和地点详情等能力，详情请参考[site](../harmonyos-references/map-site.md)。

| 类型 | 描述 | 参数  （设置关键字、城市、语言等信息） | 描述 |
| --- | --- | --- | --- |
| [searchByText](../harmonyos-references/map-site.md#searchbytext) | 通过指定的关键字和可选的地理范围。 | [SearchByTextParams](../harmonyos-references/map-site.md#searchbytextparams) | 关键字搜索的参数。 |
| [nearbySearch](../harmonyos-references/map-site.md#nearbysearch) | 通过用户传入自己的位置，可以返回周边地点列表。 | [NearbySearchParams](../harmonyos-references/map-site.md#nearbysearchparams) | 周边搜索的参数。 |
| [queryAutoComplete](../harmonyos-references/map-site.md#queryautocomplete) | 根据输入的关键字返回预测的输入关键字和地点查询建议。 | [QueryAutoCompleteParams](../harmonyos-references/map-site.md#queryautocompleteparams) | 自动补全的参数。 |
| [searchById](../harmonyos-references/map-site.md#searchbyid) | 根据地点的唯一主键地点ID获取地点详情。 | [SearchByIdParams](../harmonyos-references/map-site.md#searchbyidparams) | 地点详情的参数。 |

* [ArkTS API错误码](../harmonyos-references/errorcode-map.md)：介绍本模块特有错误码。

## 问题定位

1. 对于位置搜索异常，分析其位置搜索实现原理，主要分为直接请求预设位置数据和[Map Kit（地图服务）](../harmonyos-guides/map-introduction.md)提供的位置搜索。
2. 位置信息由本地数据或云端请求数据获取，根据场景分析是否满足用户需求。
3. 位置搜索能力是[Map Kit（地图服务）](../harmonyos-guides/map-introduction.md)提供，根据实际搜索场景需求，检查POI搜索是否设置正确。
   * 查询诸如旅游景点、企业和学校之类的地点场景，检查SearchByTextParams参数设置。
   * 用户传入自己的位置，返回周边地点列表场景，检查NearbySearchParams参数设置，可以通过提供关键字或指定要搜索的地点的类型来优化搜索结果。
   * 自动补全能力，检查QueryAutoCompleteParams参数设置。根据输入的关键字，将最有可能的搜索词呈现给用户，以减少用户输入信息，提升用户体验。

## 分析结论

位置搜索能力是[Map Kit（地图服务）](../harmonyos-guides/map-introduction.md)提供，其POI搜索相关能力的参数不正确，导致不满足用户实际需求或故障。

## 修改建议

设置合适正确的搜索参数，并满足用户需求。参考[关键词搜索](../harmonyos-guides/map-site-search.md#关键字搜索)，通过指定的关键字和可选的地理范围，查询诸如旅游景点、企业和学校之类的地点。更多详情请参考[位置搜索](../harmonyos-guides/map-location-services.md)。

## 常见FAQ

Q：使用Map Kit（地图服务）搜索附近时报错1002600001。

A：错误码1002600001属于系统内部错误，通常无法通过常规日志直接获取具体原因。建议检查网络环境：

-如果您使用了抓包代理工具（如[Charles](faqs-network-55.md)等），请尝试关闭代理后重新测试。

-确保设备网络连接正常，建议尝试切换Wi-Fi或移动数据。

如果问题持续存在，建议提供抓包日志与复现步骤，以便进一步排查。

Q：地图位置搜索传入经纬度后，返回的搜索地点结果与预期相差很大。

A：位置搜索传入经纬度“latitude”、“longitude”值的类型，必须为number类型，否则会导致搜索结果异常。

Q：位置搜索时，默认搜索范围是[1,50000]米，如果实现全国范围内搜索？

A：使用nearbySearch搜索时，[NearbySearchParams](../harmonyos-references/map-site.md#nearbysearchparams)中location为必选项，只能在指定位置周边进行搜索。如果需要全国范围内搜索，建议使用[searchByText](../harmonyos-references/map-site.md#searchbytext)搜索的方式，不在[SearchByTextParams](../harmonyos-references/map-site.md#searchbytextparams)中填写location参数，同时指定countryCodes为“CN”，即可实现在全国范围内搜索。
