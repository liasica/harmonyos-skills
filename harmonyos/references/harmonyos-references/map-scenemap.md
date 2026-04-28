---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-scenemap
title: sceneMap（场景化控件）
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > sceneMap（场景化控件）
category: harmonyos-references
scraped_at: 2026-04-28T08:17:26+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3c0e67afff92dbb0d99aeb3275ea003c9dbfa4b8846800975fdca5b4a9c90157
---

本模块提供地图场景化控件功能，包括地点详情展示控件、地点选取控件和区划选择控件。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { sceneMap } from '@kit.MapKit';
```

## queryLocation

PhonePC/2in1TabletWearable

queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise<void>

根据提供的参数拉起地点详情展示控件。使用Promise异步回调。

说明

* 此函数必须在ArkUI页面上下文中调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)或[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)所对应的context。 |
| options | [LocationQueryOptions](map-scenemap.md#locationqueryoptions) | 是 | 查询地点详情参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. let queryLocationOptions: sceneMap.LocationQueryOptions = { siteId: "922207154068557824" };
5. sceneMap.queryLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, queryLocationOptions)
6. .then(() => {
7. console.info("QueryLocation", "Succeeded in querying location.");
8. })
9. .catch((err: BusinessError) => {
10. console.error("QueryLocation", `Failed to query Location, code: ${err.code}, message: ${err.message}`);
11. });
```

## chooseLocation

PhonePC/2in1TabletWearable

chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise<LocationChoosingResult>

根据提供的参数拉起地点选取控件。使用Promise异步回调。

说明

* 此函数必须在ArkUI页面上下文中调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)或[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)所对应的context。 |
| options | [LocationChoosingOptions](map-scenemap.md#locationchoosingoptions) | 是 | 地点选取参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LocationChoosingResult](map-scenemap.md#locationchoosingresult)> | Promise对象，返回[LocationChoosingResult](map-scenemap.md#locationchoosingresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
5. location: { latitude: 39.92194051376904, longitude: 116.3971836796932 },
6. searchEnabled: true,
7. showNearbyPoi: true
8. };
9. sceneMap.chooseLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, locationChoosingOptions)
10. .then((data) => {
11. console.info("ChooseLocation", "Succeeded in choosing location.");
12. })
13. .catch((err: BusinessError) => {
14. console.error("ChooseLocation", `Failed to choose Location, code: ${err.code}, message: ${err.message}`);
15. });
```

## selectDistrict

PhonePC/2in1TabletWearable

selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>

根据提供的参数调出区划选择页面。使用Promise异步回调。

说明

* 此函数必须在ArkUI页面上下文中调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)或[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)所对应的context。 |
| options | [DistrictSelectOptions](map-scenemap.md#districtselectoptions) | 是 | 区划选择页面初始选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DistrictSelectResult](map-scenemap.md#districtselectresult)> | Promise对象，返回[DistrictSelectResult](map-scenemap.md#districtselectresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002600012 | The country code is not supported. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let districtSelectOptions: sceneMap.DistrictSelectOptions = {
4. countryCode: "CN"
5. };
6. sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
7. console.info("SelectDistrict", "Succeeded in selecting district.");
8. }).catch((err: BusinessError) => {
9. console.error("SelectDistrict", `Failed to select district, code: ${err.code}, message: ${err.message}`);
10. });
```

## LocationQueryOptions

PhonePC/2in1TabletWearable

查询地点详情的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| siteId | string | 否 | 是 | 地点详情页的地点ID，异常值返回401错误码。  siteId可通过[MapEventManager](map-map-mapeventmanager.md)中[on](map-map-mapeventmanager.md#onpoiclick)(type: 'poiClick', callback: Callback<[mapCommon.Poi](map-common.md#poi)>)方法获取。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| language | string | 否 | 是 | 语言，请参见[地图Picker支持语言](../harmonyos-guides/map-language.md#地图picker支持语言)，如果未设置，默认使用系统语言。异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 地图中心点坐标。如果没有siteId，使用location查询地点详情。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| name | string | 否 | 是 | 地点的名称。如果没有siteId，使用name作为location的名称标注。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| address | string | 否 | 是 | 地点的地址。如果没有siteId，使用address作为location的地址标注。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| showBusiness | boolean | 否 | 是 | 是否显示商业信息（如打车），默认值为true。  - true：显示  - false：不显示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  版本4.1.0(11)~5.1.1(19)为预留字段，从版本6.0.0(20)开始使用。 |
| themeColor | [CustomColors](js-apis-arkui-theme.md#customcolors) | 否 | 是 | 自定义主题颜色对象，默认为brand（品牌色）。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| cancelCallback | Callback<void> | 否 | 是 | 回调函数。无返回结果的回调函数。地点详情控件关闭事件回调。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| transitionDuration | number | 否 | 是 | 转场动效时间，默认值：-1，单位：ms，取值范围[0, Number.MAX\_VALUE)，异常值将按照默认值-1处理，保持[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)(0.5, 1, 328, 36)（初始速度为0.5，质量为1，刚度为1，阻尼为1）。2in1设备当前不显示转场动效，该配置不生效。  **起始版本：** 6.0.2(22)  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。 |

说明

以下两组参数，至少传入其中一组，如果都传入，以siteId为主。

* siteId
* location、name

**示例：**

```
1. let queryLocationOptions: sceneMap.LocationQueryOptions = { siteId: "922207154068557824" };
```

## LocationChoosingOptions

PhonePC/2in1TabletWearable

地点选取的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 地图中心点坐标。  如果参数未传，使用设备当前位置作为中心点；如果未获取到设备当前位置，默认以故宫博物院为中心点。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| language | string | 否 | 是 | 语言，请参见[地图Picker支持语言](../harmonyos-guides/map-language.md#地图picker支持语言)，如果未设置，默认使用系统语言。异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| poiTypes | Array<string> | 否 | 是 | 指定需要展示的POI类别。取值范围参见[HwLocationType](map-poi.md#hwlocationtype)。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| searchEnabled | boolean | 否 | 是 | 是否展示搜索控件，默认值为false，异常值按默认值处理。  - true：展示  - false：不展示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| showNearbyPoi | boolean | 否 | 是 | 是否展示附近POI，默认值为false，异常值按默认值处理。  - true：展示  - false：不展示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| snapshotEnabled | boolean | 否 | 是 | 是否返回映射快照，默认值为false。  - true：返回  - false：不返回  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| themeColor | [CustomColors](js-apis-arkui-theme.md#customcolors) | 否 | 是 | 自定义主题颜色对象，默认为brand（品牌色）。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| cancelCallback | Callback<void> | 否 | 是 | 回调函数。无返回结果的回调函数。地点选取控件关闭事件回调。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| transitionDuration | number | 否 | 是 | 转场动效时间，默认值：-1，单位：ms，取值范围[0, Number.MAX\_VALUE)，异常值将按照默认值-1处理，保持[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)(0.5, 1, 328, 36)（初始速度为0.5，质量为1，刚度为1，阻尼为1）。2in1设备当前不显示转场动效，该配置不生效。  **起始版本：** 6.0.2(22)  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。 |

**示例：**

```
1. let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
2. location: { latitude: 39.9, longitude: 116.4 }
3. };
```

## LocationChoosingResult

PhonePC/2in1TabletWearable

地点选取的返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| siteId | string | 否 | 是 | 选点的地点ID。如果选点非POI，则不返回。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 选点的坐标点。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| name | string | 否 | 是 | 选点的POI名称。如果选点非POI，则返回的name值为"标记点"。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| address | string | 否 | 否 | 选点地址。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| addressComponent | [site.AddressComponent](map-site.md#addresscomponent) | 否 | 是 | 选点地址的详细信息。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| zoom | number | 否 | 否 | 选点地址的缩放层级，取值范围：[2, 20]，超出按边界值处理。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| snapshot | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 地图快照。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

## DistrictSelectOptions

PhonePC/2in1TabletWearable

区划选择页面初始选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| countryCode | string | 否 | 是 | 查询指定国家或地区的行政区划，国家或地区码必须符合ISO 3166-1 alpha-2规则。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| language | string | 否 | 是 | 设置页面语言，请参见[地图Picker支持语言](../harmonyos-guides/map-language.md#地图picker支持语言)，如果未设置，默认使用系统语言。异常值按默认值处理。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| address | string | 否 | 是 | 指定地址查询。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| themeColor | [CustomColors](js-apis-arkui-theme.md#customcolors) | 否 | 是 | 自定义主题颜色对象，默认为brand（品牌色）。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| subWindowEnabled | boolean | 否 | 是 | 是否在子窗口中显示区划选择，默认值为false。  - true：在子窗口中显示  - false：不在子窗口中显示  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| cancelCallback | Callback<void> | 否 | 是 | 回调函数。无返回结果的回调函数。区划选择控件关闭事件回调。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| transitionDuration | number | 否 | 是 | 转场动效时间，默认值：-1，单位：ms，取值范围[0, Number.MAX\_VALUE)，异常值将按照默认值-1处理，保持[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)(0.5, 1, 328, 36)（初始速度为0.5，质量为1，刚度为1，阻尼为1）。当subWindowEnabled为true时该配置不生效。  **起始版本：** 6.0.2(22)  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。 |

**示例：**

```
1. let districtSelectOptions: sceneMap.DistrictSelectOptions = {
2. countryCode: "CN",
3. language:"zh",
4. address: "河南"
5. };
```

## DistrictSelectResult

PhonePC/2in1TabletWearable

区划选择请求的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| districts | Array<[District](map-scenemap.md#district)> | 否 | 否 | 所选行政区划的级别信息。 |
| addressDescription | string | 否 | 是 | 返回所选行政区划的地址信息。 |

## District

PhonePC/2in1TabletWearable

行政区划信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| siteId | string | 否 | 是 | 区划的地点ID。 |
| name | string | 否 | 是 | 区划的名称。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 区划的坐标点 |
| adminLevel | string | 否 | 是 | 区划级别，分国家、省份、城市、区/县和街道五个区划级别。  **说明：**  国家：COUNTRY  省份：ADMINISTRATIVE\_AREA\_LEVEL\_1  城市：ADMINISTRATIVE\_AREA\_LEVEL\_2  区/县：ADMINISTRATIVE\_AREA\_LEVEL\_3  街道：ADMINISTRATIVE\_AREA\_LEVEL\_4 |
| adminCode | string | 否 | 是 | [行政区划码](map-citycode.md)。  **说明：**  接口返回的行政区划码覆盖中国大陆及港澳地区，包括省份、城市、区/县、乡镇/街道等层级，文档附录中仅提供部分城市行政区划码示例。 |
| cityCode | string | 否 | 是 | [城市码](map-citycode.md)。 |
| countryCode | string | 否 | 是 | 国家/地区码。 |
