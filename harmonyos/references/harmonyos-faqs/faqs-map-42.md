---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-42
title: 通过地图应用实现导航常见问题
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 通过地图应用实现导航常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:11f2e881c3edfcd3d1169d50d95ceebd117bd7103b21bd02cf5cfe62b5cd9933
---

## 问题现象

HarmonyOS当前支持应用通过接口拉起华为地图应用进行地点搜索、地点详情查看、路线规划和导航等功能。功能开发过程中可能会遇到以下问题：

1. 使用petalMaps（拉起地图应用），是否需要[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)？
2. 拉起地图应用时，是否可以仅传递目的地点名称进行导航？
3. 拉起地图应用进行导航时，传递的坐标是什么坐标系？
4. 是否可以在应用内实现导航？
5. 拉起地图应用进行路线规划和导航时，需要传递目的地坐标，如何获取目的地的坐标？
6. [打开地图应用查看地点详情](../harmonyos-guides/map-petalmaps.md#打开地图应用查看地点详情)时，只传入坐标为什么不展示地点详情。

## 背景知识

应用可通过两种方式拉起华为地图应用：

* 通过startAbilityByType接口配合对应的Want参数，可以拉起华为地图应用和其他已安装的导航类应用，参考[拉起导航类应用（startAbilityByType）](../harmonyos-guides/start-navigation-apps.md)。
* 通过[petalMaps（拉起地图应用）](../harmonyos-references/map-petal-maps.md)接口，拉起华为地图应用，实现导航等功能，参考[通过地图应用实现导航等能力](../harmonyos-guides/map-petalmaps.md)。

## 解决方案

本方案主要针对以上通过petalMaps（拉起地图应用）接口拉起华为地图应用开发过程中遇到的问题进行回答。

1. 使用petalMaps（拉起地图应用）接口无需开通地图服务。
2. 通过[openMapRoutePlan](../harmonyos-references/map-petal-maps.md#openmaprouteplan)接口[打开地图应用规划路线](../harmonyos-guides/map-petalmaps.md#打开地图应用规划路线)时，必须要传入目的地坐标。如果需要通过地点名称进行导航，可以通过[打开地图应用进行地点搜索](../harmonyos-guides/map-petalmaps.md#打开地图应用进行地点搜索)传入目的地名称，跳转地图应用后，在弹出的地点搜索列表中选择目的地，进行导航。
3. 通过openMapRoutePlan接口打开地图应用规划路线时，需要传入坐标为GCJ02坐标系，如果坐标数据源是其他坐标系时，需要进行转换。例如WGS84坐标参考[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md)进行转换。
4. 当前Map Kit可以实现[出行路线规划](../harmonyos-guides/map-navi-routes.md)能力，但不直接提供导航能力，建议使用打开地图应用规划路线方式跳转地图应用选择路线进行导航。
5. 获取目的地坐标的几种场景：
   * 目的地为Map Kit中的Marker时，可以通过Marker的[getPosition](../harmonyos-references/map-map-marker.md#getposition)接口，获取Marker所在位置的坐标。
   * 目的地为明确的地点或地址时，可以通过[正地理编码](../harmonyos-guides/map-site-geocode.md#正地理编码)获取地址所在坐标。
6. [打开地图应用查看地点详情](../harmonyos-guides/map-petalmaps.md#打开地图应用查看地点详情)时，需要传递所查看目标地点的Aoi ID，才会展示对应地点的真实详情。获取坐标对应的Aoi ID，请参见[reverseGeocode](../harmonyos-references/map-site.md#reversegeocode)，在查询结果的aois数组中，获取的第一个Aoi的siteId值，即为所查看目标地点的Aoi ID。
