---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/weather-service-weatherservice
title: weatherService（天气数据服务）
breadcrumb: API参考 > 应用服务 > Weather Service Kit（天气服务） > ArkTS API > weatherService（天气数据服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:21976ff51519932ea39773d6e09d33c4fcb9214925661e4952848ef5c841497b
---

本模块提供天气数据服务。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { weatherService } from '@kit.WeatherServiceKit';
```

## weatherService.getWeather

PhonePC/2in1TabletTVWearable

getWeather(request: WeatherRequest): Promise<Weather>

天气数据获取接口，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [WeatherRequest](weather-service-weatherservice.md#weatherrequest) | 是 | 天气数据请求体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Weather](weather-service-weatherservice.md#weather)> | Promise对象，返回天气数据对象。 |

**错误码：**

以下错误码的详细介绍请参见天气服务[ArkTS API错误码](weather-service-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1011900001 | Capability is not configured. |
| 1011900002 | The requested longitude and latitude grid point lacks data. |
| 1011900003 | Network error. |
| 1011900004 | System error. |

**示例：**

```
1. // 引入
2. import { weatherService } from '@kit.WeatherServiceKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function getWeatherData() {
6. // 初始化参数
7. let request: weatherService.WeatherRequest = {
8. location: {
9. latitude: 22.62,
10. longitude: 114.07
11. },
12. // 只请求需要的数据，不设置的话默认请求全量数据
13. limitedDatasets: [weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS]
14. }

16. // 请求及错误处理
17. try {
18. let weather = await weatherService.getWeather(request);
19. if (weather.current) {
20. console.info('getWeather current temperature: ' + weather.current.temperature);
21. }
22. if (weather.alerts?.length) {
23. console.info('getWeather alert: ' + weather.alerts[0].title);
24. }
25. } catch (err) {
26. err = err as BusinessError;
27. console.error(`getWeather failed. Code: ${err.code}, message: ${err.message}`);
28. }
29. }
```

## weatherService.getWeatherWithContext

PhonePC/2in1TabletTVWearable

getWeatherWithContext(context: common.Context, request: WeatherRequest): Promise<Weather>

根据调用方提供的上下文信息获取天气数据，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 上下文，目前只支持[UIAbility](js-apis-app-ability-uiability.md)或[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)的上下文环境。 |
| request | [WeatherRequest](weather-service-weatherservice.md#weatherrequest) | 是 | 天气数据请求体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Weather](weather-service-weatherservice.md#weather)> | Promise对象，返回天气数据对象。 |

**错误码：**

以下错误码的详细介绍请参见天气服务[ArkTS API错误码](weather-service-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1011900001 | Capability is not configured. |
| 1011900002 | The requested longitude and latitude grid point lacks data. |
| 1011900003 | Network error. |
| 1011900004 | System error. |

**示例：**

```
1. // 引入
2. import { UIAbility } from '@kit.AbilityKit';
3. import { weatherService } from '@kit.WeatherServiceKit';
4. import { common } from '@kit.AbilityKit';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import { taskpool } from '@kit.ArkTS';

8. @Concurrent
9. async function getWeatherData(context: common.Context) {
10. let request: weatherService.WeatherRequest = {
11. location: {
12. latitude: 22.62,
13. longitude: 114.07
14. },
15. // 只请求需要的数据，不设置的话默认请求全量数据
16. limitedDatasets: [weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS]
17. }

19. // 请求及错误处理
20. try {
21. let weather = await weatherService.getWeatherWithContext(context, request);
22. if (weather.current) {
23. console.info('getWeatherWithContext current temperature: ' + weather.current.temperature);
24. }
25. if (weather.alerts?.length) {
26. console.info('getWeatherWithContext alert: ' + weather.alerts[0].title);
27. }
28. } catch (err) {
29. err = err as BusinessError;
30. console.error(`getWeatherWithContext failed. Code: ${err.code}, message: ${err.message}`);
31. }
32. }

34. function executeGetWeather(context: common.Context) {
35. taskpool.execute(getWeatherData, context);
36. }

38. export default class EntryAbility extends UIAbility {
39. onCreate(): void {
40. executeGetWeather(this.context);
41. }
42. }
```

## WeatherRequest

PhonePC/2in1TabletTVWearable

天气数据请求类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| location | [Location](weather-service-weatherservice.md#location) | 否 | 否 | 位置信息。 |
| limitedDatasets | [Dataset](weather-service-weatherservice.md#dataset)[] | 否 | 是 | 接口只返回列表中指定的数据类型，若未设置或数组为空，默认返回全量数据。 |

## Location

PhonePC/2in1TabletTVWearable

位置信息。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度。  取值范围：[-90, 90]。  在6.1.0(23)之前，精度支持小数点后两位，从6.1.0(23)开始，中国境内(香港特别行政区、澳门特别行政区、中国台湾除外)精度支持小数点后五位，其他地区仍为两位。 |
| longitude | number | 否 | 否 | 经度。  取值范围：[-180, 180]。  在6.1.0(23)之前，精度支持小数点后两位，从6.1.0(23)开始，中国境内(香港特别行政区、澳门特别行政区、中国台湾除外)精度支持小数点后五位，其他地区仍为两位。 |

## Weather

PhonePC/2in1TabletTVWearable

天气数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| current | [CurrentWeather](weather-service-weatherservice.md#currentweather) | 否 | 是 | 实况天气，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).CURRENT，该字段不返回。 |
| daily | [Forecast](weather-service-weatherservice.md#forecastt)<[DailyWeather](weather-service-weatherservice.md#dailyweather)> | 否 | 是 | 多日预报，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).DAILY，该字段不返回。 |
| hourly | [Forecast](weather-service-weatherservice.md#forecastt)<[HourlyWeather](weather-service-weatherservice.md#hourlyweather)> | 否 | 是 | 逐小时预报，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).HOURLY，该字段不返回。 |
| minute | [Forecast](weather-service-weatherservice.md#forecastt)<[MinuteWeather](weather-service-weatherservice.md#minuteweather)> | 否 | 是 | 分钟级降水预报，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).MINUTE，或者该区域短期无降水，该字段不返回。 |
| alerts | [WeatherAlert](weather-service-weatherservice.md#weatheralert)[] | 否 | 是 | 天气预警，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).ALERTS，或者该区域当前无预警，该字段不返回。 |
| indices | [WeatherIndex](weather-service-weatherservice.md#weatherindex)[] | 否 | 是 | 天气指数，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).INDICES，该字段不返回。 |
| tides | [Tide](weather-service-weatherservice.md#tide)[] | 否 | 是 | 潮汐，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).TIDES，或者该区域无潮汐站点，该字段不返回。 |
| city | [City](weather-service-weatherservice.md#city) | 否 | 是 | 请求经纬度对应的城市信息，若设置了limitedDatasets且数组中不包含[Dataset](weather-service-weatherservice.md#dataset).CITY，该字段不返回。  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。  **起始版本：** 6.1.0(23)  **模型约束：** 此接口仅可在Stage模型下使用。 |
| metadata | [WeatherMetadata](weather-service-weatherservice.md#weathermetadata) | 否 | 否 | 天气数据元数据。 |
| attributions | [WeatherAttribution](weather-service-weatherservice.md#weatherattribution)[] | 否 | 否 | 天气数据的归因。 |

## CurrentWeather

PhonePC/2in1TabletTVWearable

实况天气数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| temperature | number | 否 | 否 | 温度。  单位：℃。 |
| apparentTemperature | number | 否 | 否 | 体感温度。  单位：℃。 |
| humidity | number | 否 | 否 | 相对湿度。  例如湿度为30%，本字段返回30。 |
| pressure | number | 否 | 否 | 地面气压。  单位：hPa。 |
| pressureTrend | [PressureTrend](weather-service-weatherservice.md#pressuretrend) | 否 | 否 | 气压趋势。 |
| wind | [Wind](weather-service-weatherservice.md#wind) | 否 | 否 | 风力风向。 |
| cloudCover | number | 否 | 否 | 云量。  例如云量为30%，本字段返回30。 |
| condition | [WeatherCondition](weather-service-weatherservice.md#weathercondition) | 否 | 否 | 天气现象。 |
| uvIndex | [UVIndex](weather-service-weatherservice.md#uvindex) | 否 | 否 | 紫外线指数。 |
| aqi | [WeatherAqi](weather-service-weatherservice.md#weatheraqi) | 否 | 是 | 空气质量。 |
| visibility | number | 否 | 否 | 能见度。  单位：km。 |
| updateTime | Date | 否 | 否 | 数据更新时间，UTC时间格式。 |
| expirationTime | Date | 否 | 否 | 数据失效时间，UTC时间格式。 |
| summary | string | 否 | 是 | 实况天气一句话描述。 |
| alertTitle | string | 否 | 是 | 预警标题。  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。  **起始版本：** 6.1.0(23)  **模型约束：** 此接口仅可在Stage模型下使用。 |

## Forecast<T>

PhonePC/2in1TabletTVWearable

预报类天气集合。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| forecast | T[] | 否 | 否 | 预报数据集合。 |
| updateTime | Date | 否 | 否 | 数据更新时间，UTC时间格式。 |
| expirationTime | Date | 否 | 否 | 数据失效时间，UTC时间格式。 |
| summary | string | 否 | 是 | 预报数据一句话描述，只有分钟级降水预报会返回该字段。 |

## DailyWeather

PhonePC/2in1TabletTVWearable

多日天气数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| date | Date | 否 | 否 | 日期，精确到天，UTC时间格式。 |
| highTemperature | number | 否 | 否 | 高温。  单位：℃。 |
| lowTemperature | number | 否 | 否 | 低温。  单位：℃。 |
| highApparentTemperature | number | 否 | 否 | 体感温度高温。  单位：℃。 |
| lowApparentTemperature | number | 否 | 否 | 体感温度低温。  单位：℃。 |
| uvIndex | [UVIndex](weather-service-weatherservice.md#uvindex) | 否 | 否 | 紫外线指数。 |
| aqi | [WeatherAqi](weather-service-weatherservice.md#weatheraqi) | 否 | 是 | 空气质量。 |
| visibility | number | 否 | 否 | 能见度。  单位：km。 |
| moon | [MoonEvents](weather-service-weatherservice.md#moonevents) | 否 | 否 | 月出/月落时间，月相等信息。 |
| sun | [SunEvents](weather-service-weatherservice.md#sunevents) | 否 | 否 | 日出/日落时间。 |
| daytimeForecast | [DayPartForecast](weather-service-weatherservice.md#daypartforecast) | 否 | 否 | 白天天气数据。 |
| overnightForecast | [DayPartForecast](weather-service-weatherservice.md#daypartforecast) | 否 | 否 | 夜晚天气数据。 |
| pressure | number | 否 | 否 | 地面气压。  单位：hPa。 |

## HourlyWeather

PhonePC/2in1TabletTVWearable

小时天气数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| date | Date | 否 | 否 | 日期， 精确到小时，UTC时间格式。 |
| temperature | number | 否 | 否 | 温度。  单位：℃。 |
| apparentTemperature | number | 否 | 否 | 体感温度。  单位：℃。 |
| humidity | number | 否 | 否 | 相对湿度。  例如湿度为30%，本字段返回30。 |
| wind | [Wind](weather-service-weatherservice.md#wind) | 否 | 否 | 风力风向。 |
| cloudCover | number | 否 | 否 | 云量。  例如云量为30%，本字段返回30。 |
| condition | [WeatherCondition](weather-service-weatherservice.md#weathercondition) | 否 | 否 | 天气现象。 |
| uvIndex | [UVIndex](weather-service-weatherservice.md#uvindex) | 否 | 否 | 紫外线等级。 |
| aqi | [WeatherAqi](weather-service-weatherservice.md#weatheraqi) | 否 | 是 | 空气质量。 |
| visibility | number | 否 | 否 | 能见度。  单位：km。 |
| precipitationProbability | number | 否 | 否 | 降水概率。 |
| precipitationAmount | number | 否 | 否 | 降水量。  单位：mm。 |

## MinuteWeather

PhonePC/2in1TabletTVWearable

分钟级降水数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| date | Date | 否 | 否 | 日期， 精确到分钟，UTC时间格式。 |
| precipitation | [Precipitation](weather-service-weatherservice.md#precipitation) | 否 | 否 | 降水类型。 |
| precipitationIntensity | number | 否 | 否 | 降水密度。  取值范围：[0, 1]。 |

## WeatherAlert

PhonePC/2in1TabletTVWearable

天气预警信息类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| updateTime | Date | 否 | 否 | 数据更新时间，UTC时间格式。 |
| expirationTime | Date | 否 | 否 | 数据失效时间，UTC时间格式。 |
| id | string | 否 | 否 | 预警id。 |
| title | string | 否 | 否 | 预警标题。 |
| region | string | 否 | 是 | 预警区域。 |
| level | [AlertLevel](weather-service-weatherservice.md#alertlevel) | 否 | 否 | 预警等级。 |
| levelDescription | string | 否 | 否 | 预警等级描述。 |
| type | [AlertType](weather-service-weatherservice.md#alerttype) | 否 | 否 | 预警类型。 |
| typeDescription | string | 否 | 否 | 预警类型描述。 |
| content | string | 否 | 否 | 预警正文。 |
| guide | string | 否 | 是 | 预警防御指南。 |
| detailsUrl | string | 否 | 是 | 预警详情链接。 |
| source | string | 否 | 否 | 预警来源。 |
| icon | [resourceManager.Resource](js-apis-resource-manager.md#resource9) | 否 | 是 | 预警图标。 |

## WeatherIndex

PhonePC/2in1TabletTVWearable

天气指数数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| updateTime | Date | 否 | 否 | 数据更新时间，UTC时间格式。 |
| expirationTime | Date | 否 | 否 | 数据失效时间，UTC时间格式。 |
| type | [WeatherIndexType](weather-service-weatherservice.md#weatherindextype) | 否 | 否 | 指数类型。 |
| name | string | 否 | 否 | 指数名称。 |
| dailyItems | [DailyIndex](weather-service-weatherservice.md#dailyindex)[] | 否 | 否 | 每天的指数详情。 |

## Tide

PhonePC/2in1TabletTVWearable

潮汐数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| updateTime | Date | 否 | 否 | 数据更新时间，UTC时间格式。 |
| expirationTime | Date | 否 | 否 | 数据失效时间，UTC时间格式。 |
| stationId | string | 否 | 否 | 潮汐站点id。 |
| stationName | string | 否 | 否 | 潮汐站点名称。 |
| hourlyTides | [HourlyTide](weather-service-weatherservice.md#hourlytide)[] | 否 | 否 | 小时潮汐数据。 |

## City

PhonePC/2in1TabletTVWearable

城市信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| countryCode | string | 否 | 否 | 国家编码，ISO 3166-1 标准中的两位国家编码。 |
| level | number | 否 | 否 | 行政区划等级。  0：国家  1：省份  2：地级市  3：县区 |
| localizedName | string | 否 | 否 | 本地化语言城市名称。 |
| chineseName | string | 否 | 是 | 中文城市名称。 |
| englishName | string | 否 | 是 | 英文城市名称。 |
| timezone | string | 否 | 是 | 时区。 |
| administrativeAreas | [AdministrativeArea](weather-service-weatherservice.md#administrativearea)[] | 否 | 是 | 行政区域列表。 |

## WeatherMetadata

PhonePC/2in1TabletTVWearable

天气元数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestTime | Date | 否 | 否 | 接口请求时间，UTC时间格式。 |
| version | string | 否 | 否 | 天气服务版本。 |
| timeZone | string | 否 | 是 | 接口请求目的地的时区。 |

## WeatherAttribution

PhonePC/2in1TabletTVWearable

天气数据归因类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceName | string | 否 | 否 | 数据供应商名称。 |
| legalPageUrl | string | 否 | 否 | 归因页面链接。 |

## Wind

PhonePC/2in1TabletTVWearable

风力风向数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | [CompassDirection](weather-service-weatherservice.md#compassdirection) | 否 | 否 | 风向。 |
| speed | number | 否 | 否 | 风速。  单位：km/h。 |
| level | number | 否 | 否 | 风力级别。 |
| gustDirection | [CompassDirection](weather-service-weatherservice.md#compassdirection) | 否 | 是 | 阵风风向。 |
| gustSpeed | number | 否 | 是 | 阵风风速。  单位：km/h。 |
| gustLevel | number | 否 | 是 | 阵风风力级别。 |

## WeatherCondition

PhonePC/2in1TabletTVWearable

天气现象数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ConditionType](weather-service-weatherservice.md#conditiontype) | 否 | 否 | 天气现象类型。 |
| icon | [resourceManager.Resource](js-apis-resource-manager.md#resource9) | 否 | 否 | 天气现象图标。 |
| description | string | 否 | 否 | 天气现象描述。 |

## UVIndex

PhonePC/2in1TabletTVWearable

紫外线指数数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| category | [ExposureCategory](weather-service-weatherservice.md#exposurecategory) | 否 | 否 | 紫外线暴露类别。 |
| value | number | 否 | 否 | 紫外线等级。 |
| description | string | 否 | 否 | 紫外线等级描述。 |

## WeatherAqi

PhonePC/2in1TabletTVWearable

空气质量数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| no2 | number | 否 | 是 | 二氧化氮浓度。  单位：μg/m3。 |
| o3 | number | 否 | 是 | 臭氧浓度。  单位：μg/m3。 |
| pm10 | number | 否 | 是 | PM10浓度。  单位：μg/m3。 |
| pm25 | number | 否 | 是 | PM2.5浓度。  单位：μg/m3。 |
| so2 | number | 否 | 是 | 二氧化硫浓度。  单位：μg/m3。 |
| co | number | 否 | 是 | 一氧化碳浓度。  单位：μg/m3。 |
| aqiValue | number | 否 | 否 | 空气质量数值。 |
| aqiCategory | [AqiCategory](weather-service-weatherservice.md#aqicategory) | 否 | 否 | 空气质量类别。 |
| aqiDescription | string | 否 | 否 | 空气质量类别描述。 |

## MoonEvents

PhonePC/2in1TabletTVWearable

月出/月落时间，月相等信息类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moonrise | Date | 否 | 否 | 月出时间，UTC时间格式。 |
| moonset | Date | 否 | 否 | 月落时间，UTC时间格式。 |
| phase | [MoonPhase](weather-service-weatherservice.md#moonphase) | 否 | 否 | 月相。 |
| illuminatedFraction | number | 否 | 是 | 月面照亮比例。  例如比例为30%，本字段返回30。 |
| age | number | 否 | 是 | 月龄。 |

## MoonPhase

PhonePC/2in1TabletTVWearable

月相信息类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [MoonPhaseType](weather-service-weatherservice.md#moonphasetype) | 否 | 否 | 月相类型。 |
| description | string | 否 | 否 | 月相描述。 |
| icon | [resourceManager.Resource](js-apis-resource-manager.md#resource9) | 否 | 否 | 月相图标。 |

## SunEvents

PhonePC/2in1TabletTVWearable

日出/日落信息类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sunrise | Date | 否 | 否 | 日出时间，UTC时间格式。 |
| sunset | Date | 否 | 否 | 日落时间，UTC时间格式。 |

## DayPartForecast

PhonePC/2in1TabletTVWearable

全天部分时段天气信息类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wind | [Wind](weather-service-weatherservice.md#wind) | 否 | 否 | 风力风向。 |
| humidity | number | 否 | 否 | 相对湿度。  例如湿度为30%，本字段返回30。 |
| cloudCover | number | 否 | 否 | 云量。  例如云量为30%，本字段返回30。 |
| condition | [WeatherCondition](weather-service-weatherservice.md#weathercondition) | 否 | 否 | 天气现象。 |
| precipitationProbability | number | 否 | 否 | 降水概率。 |
| precipitationAmount | number | 否 | 否 | 降水量。  单位：mm。 |
| rainfallProbability | number | 否 | 是 | 降雨概率。 |
| rainfallAmount | number | 否 | 是 | 降雨量。  单位：mm。 |
| snowfallProbability | number | 否 | 是 | 降雪概率。 |
| snowfallAmount | number | 否 | 是 | 降雪量。  单位：mm。 |

## DailyIndex

PhonePC/2in1TabletTVWearable

每天天气指数数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| date | Date | 否 | 否 | 日期，精确到天，UTC时间格式。 |
| level | number | 否 | 否 | 指数级别。 |
| levelDescription | string | 否 | 否 | 指数级别描述。 |
| content | string | 否 | 否 | 指数内容。 |

## HourlyTide

PhonePC/2in1TabletTVWearable

小时潮汐数据类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| date | Date | 否 | 否 | 日期，精确到小时，UTC时间格式。 |
| category | [TideCategory](weather-service-weatherservice.md#tidecategory) | 否 | 是 | 潮汐类型。 |
| height | number | 否 | 否 | 潮汐高度。  单位：cm。 |

## AdministrativeArea

PhonePC/2in1TabletTVWearable

行政区域信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| level | number | 否 | 否 | 行政区划等级。  0：国家  1：省份  2：地级市  3：县区 |
| localizedName | string | 否 | 否 | 本地化语言名称。 |
| chineseName | string | 否 | 是 | 中文名称。 |
| englishName | string | 否 | 是 | 英文名称。 |

## Dataset

PhonePC/2in1TabletTVWearable

数据集枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CURRENT | 0 | 实况天气。 |
| DAILY | 1 | 多日预报。 |
| HOURLY | 2 | 逐小时预报。 |
| MINUTE | 3 | 分钟级降水预报。 |
| ALERTS | 4 | 天气预警。 |
| INDICES | 5 | 天气指数。 |
| TIDES | 6 | 潮汐。 |
| CITY | 7 | 城市信息。  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。  **起始版本：** 6.1.0(23)  **模型约束：** 此接口仅可在Stage模型下使用。 |

## PressureTrend

PhonePC/2in1TabletTVWearable

气压趋势枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义。 |
| FALLING | 1 | 下降。 |
| RISING | 2 | 上升。 |
| STEADY | 3 | 稳定。 |

## ConditionType

PhonePC/2in1TabletTVWearable

天气现象类型枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义 |
| SUNNY | 1 | 晴 |
| MOSTLY\_SUNNY | 2 | 多云 |
| PARTLY\_SUNNY | 3 | 多云 |
| INTERMITTENT\_CLOUDS | 4 | 多云 |
| HAZY\_SUNSHINE | 5 | 霾 |
| MOSTLY\_CLOUDY | 6 | 多云 |
| CLOUDY | 7 | 多云 |
| OVERCAST | 8 | 阴 |
| FOG | 11 | 雾 |
| SHOWERS | 12 | 阵雨 |
| MOSTLY\_CLOUDY\_WITH\_SHOWERS | 13 | 阵雨 |
| PARTLY\_SUNNY\_WITH\_SHOWERS | 14 | 阵雨 |
| T\_STORMS | 15 | 雷阵雨 |
| MOSTLY\_CLOUDY\_WITH\_T\_STORMS | 16 | 雷阵雨 |
| PARTLY\_SUNNY\_WITH\_T\_STORMS | 17 | 雷阵雨 |
| RAIN | 18 | 雨 |
| FLURRIES | 19 | 阵雪 |
| MOSTLY\_CLOUDY\_WITH\_FLURRIES | 20 | 阵雪 |
| PARTLY\_SUNNY\_WITH\_FLURRIES | 21 | 阵雪 |
| SNOW | 22 | 雪 |
| MOSTLY\_CLOUDY\_WITH\_SNOW | 23 | 雪 |
| ICE | 24 | 雪 |
| SLEET | 25 | 雨夹雪 |
| FREEZING\_RAIN | 26 | 雨 |
| RAIN\_AND\_SNOW | 29 | 雨夹雪 |
| HOT | 30 | 炎热 |
| COLD | 31 | 寒冷 |
| WINDY | 32 | 有风 |
| CLEAR | 33 | 晴 |
| MOSTLY\_CLEAR | 34 | 多云 |
| PARTLY\_CLOUDY | 35 | 多云 |
| INTERMITTENT\_CLOUDS\_NIGHT | 36 | 多云 |
| HAZY\_MOONLIGHT | 37 | 霾 |
| MOSTLY\_CLOUDY\_NIGHT | 38 | 多云 |
| PARTLY\_CLOUDY\_WITH\_SHOWERS | 39 | 阵雨 |
| MOSTLY\_CLOUDY\_WITH\_SHOWERS\_NIGHT | 40 | 阵雨 |
| PARTLY\_CLOUDY\_WITH\_T\_STORMS | 41 | 雷阵雨 |
| MOSTLY\_CLOUDY\_WITH\_T\_STORMS\_NIGHT | 42 | 雷阵雨 |
| MOSTLY\_CLOUDY\_WITH\_FLURRIES\_NIGHT | 43 | 阵雪 |
| MOSTLY\_CLOUDY\_WITH\_SNOW\_NIGHT | 44 | 雪 |
| THUNDERSHOWER\_WITH\_HAIL | 45 | 冰雹 |
| LIGHT\_RAIN | 46 | 小雨 |
| MODERATE\_RAIN | 47 | 中雨 |
| HEAVY\_RAIN | 48 | 大雨 |
| STORM | 49 | 暴雨 |
| HEAVY\_STORM | 50 | 暴雨 |
| SEVERE\_STORM | 51 | 特大暴雨 |
| LIGHT\_SNOW | 52 | 阵雪 |
| MODERATE\_SNOW | 53 | 中雪 |
| HEAVY\_SNOW | 54 | 大雪 |
| SNOWSTORM | 55 | 暴雪 |
| DUST\_STORM | 56 | 沙尘暴 |
| LIGHT\_TO\_MODERATE\_RAIN | 57 | 中雨 |
| MODERATE\_TO\_HEAVY\_RAIN | 58 | 大雨 |
| HEAVY\_RAIN\_TO\_STORM | 59 | 暴雨 |
| STORM\_TO\_HEAVY\_STORM | 60 | 暴雨 |
| HEAVY\_TO\_SEVERE\_STORM | 61 | 特大暴雨 |
| LIGHT\_TO\_MODERATE\_SNOW | 62 | 中雪 |
| MODERATE\_TO\_HEAVY\_SNOW | 63 | 大雪 |
| HEAVY\_SNOW\_TO\_SNOWSTORM | 64 | 暴雪 |
| DUST | 65 | 浮尘 |
| SAND | 66 | 扬沙 |
| SANDSTORM | 67 | 强沙尘暴 |
| DENSE\_FOGGY | 68 | 雾 |
| MODERATE\_FOGGY | 69 | 雾 |
| MODERATE\_HAZE | 70 | 霾 |
| HEAVY\_HAZE | 71 | 霾 |
| SEVERE\_HAZE | 72 | 霾 |
| HEAVY\_FOGGY | 73 | 雾 |
| SEVERE\_FOGGY | 74 | 雾 |
| OVERCAST\_NIGHT | 75 | 阴 |
| BLOWING\_SNOW | 76 | 阵雪 |

## CompassDirection

PhonePC/2in1TabletTVWearable

指针方向枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义。 |
| NORTH | 1 | 北。 |
| NORTH\_EAST | 2 | 东北。 |
| EAST | 3 | 东。 |
| SOUTH\_EAST | 4 | 东南。 |
| SOUTH | 5 | 南。 |
| SOUTH\_WEST | 6 | 西南。 |
| WEST | 7 | 西。 |
| NORTH\_WEST | 8 | 西北。 |

## ExposureCategory

PhonePC/2in1TabletTVWearable

紫外线暴露程度枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义。 |
| VERY\_LOW | 1 | 最弱。 |
| LOW | 2 | 弱。 |
| MODERATE | 3 | 中等。 |
| HIGH | 4 | 强。 |
| VERY\_HIGH | 5 | 很强。 |

## MoonPhaseType

PhonePC/2in1TabletTVWearable

月相类别枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义。 |
| NEW | 1 | 新月。 |
| WAXING\_CRESCENT | 2 | 娥眉月。 |
| FIRST\_QUARTER | 3 | 上弦月。 |
| WAXING\_GIBBOUS | 4 | 盈凸月。 |
| FULL | 5 | 满月。 |
| WANING\_GIBBOUS | 6 | 亏凸月。 |
| LAST\_QUARTER | 7 | 下弦月。 |
| WANING\_CRESCENT | 8 | 残月。 |

## Precipitation

PhonePC/2in1TabletTVWearable

降水类型枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无降水。 |
| HAIL | 1 | 冰雹。 |
| RAIN | 2 | 雨。 |
| SLEET | 3 | 雨夹雪。 |
| SNOW | 4 | 雪。 |

## AlertLevel

PhonePC/2in1TabletTVWearable

预警级别枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLUE | 1 | 蓝色预警。 |
| YELLOW | 2 | 黄色预警。 |
| ORANGE | 3 | 橙色预警。 |
| RED | 4 | 红色预警。 |
| OTHER | 5 | 其他。 |
| WHITE | 6 | 白色预警。 |
| BLACK | 7 | 黑色预警。 |

## AlertType

PhonePC/2in1TabletTVWearable

预警类型枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPHOON | 1 | 台风。 |
| RAIN\_STORM | 2 | 暴雨 |
| SNOW\_STORM | 3 | 暴雪。 |
| COLD\_WAVE | 4 | 寒潮。 |
| GALE | 5 | 大风。 |
| SAND\_STORM | 6 | 沙尘暴。 |
| HEAT\_WAVE | 7 | 高温。 |
| DROUGHT | 8 | 干旱。 |
| LIGHTNING | 9 | 雷电。 |
| HAIL | 10 | 冰雹。 |
| FROST | 11 | 霜冻。 |
| HEAVY\_FOG | 12 | 大雾。 |
| HAZE | 13 | 霾。 |
| ROAD\_ICING | 14 | 道路结冰。 |
| OTHER | 15 | 其他。 |
| THUNDER\_AND\_GALE | 17 | 雷电大风。 |
| FOREST\_FIRE\_RISK | 18 | 森林火险。 |
| COLD | 19 | 寒冷。 |
| DUST\_HAZE | 20 | 灰霾。 |
| COOLING | 21 | 降温。 |
| ROAD\_ICE\_AND\_SNOW | 22 | 道路冰雪。 |
| DRY\_HOT\_WIND | 23 | 干热风。 |
| HAZE\_VERY\_UNHEALTHY | 24 | 空气重污染。 |
| FROZEN | 25 | 冰冻。 |
| HEAVY\_FOG\_AT\_SEA | 26 | 海上大雾。 |
| THUNDERSTORM\_AND\_GALE | 27 | 雷暴大风。 |
| CONTINUOUS\_LOW\_TEMPERATURE | 28 | 持续低温。 |
| THICK\_DUST | 29 | 浓浮尘。 |
| TORNADO | 30 | 龙卷风。 |
| LOW\_TEMPERATURE\_FREEZE\_INJURY | 31 | 低温冻害。 |
| GALE\_AT\_SEA | 32 | 海上大风。 |
| LOW\_TEMPERATURE\_FREEZING\_RAIN\_AND\_SNOW | 33 | 低温雨雪冰冻。 |
| SEVERE\_CONVECTION | 34 | 强对流。 |
| OZONE | 35 | 臭氧。 |
| HEAVY\_SNOW | 36 | 大雪。 |
| HEAVY\_RAINFALL | 37 | 强降雨。 |
| STRONG\_COOLING | 38 | 强降温。 |
| SNOW\_DISASTER | 39 | 雪灾。 |
| FOREST\_GRASSLAND\_FIRE\_RISK | 40 | 森林（草原）火险。 |
| THUNDERSTORM | 41 | 雷暴。 |
| SEVERE\_COLD | 42 | 严寒。 |
| SAND\_DUST | 43 | 沙尘。 |
| THUNDERSTORM\_AND\_GALE\_AT\_SEA | 44 | 海上雷雨大风。 |
| LIGHTNING\_AT\_SEA | 45 | 海上雷电。 |
| TYPHOON\_AT\_SEA | 46 | 海上台风。 |
| LOW\_TEMPERATURE | 47 | 低温。 |
| GEOLOGICAL\_HAZARD | 48 | 地质灾害。 |
| GEOLOGICAL\_HAZARD\_AND\_METEOROLOGICAL\_RISK | 49 | 地质灾害气象风险。 |
| FLUSH\_FLOOD | 50 | 山洪。 |
| GRASSLAND\_FIRE\_RISK | 51 | 草原火险。 |
| THUNDER\_RAIN\_AND\_GALE | 52 | 雷雨大风。 |

## AqiCategory

PhonePC/2in1TabletTVWearable

空气质量类别枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义。 |
| EXCELLENT | 1 | 优质。 |
| GOOD | 2 | 良。 |
| SLIGHT | 3 | 轻度污染。 |
| MODERATE | 4 | 中度污染。 |
| HEAVY | 5 | 重度污染。 |
| SEVERE | 6 | 严重污染。 |

## WeatherIndexType

PhonePC/2in1TabletTVWearable

天气指数类型枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义。 |
| DRESSING | 1 | 穿衣指数。 |
| MOTION | 2 | 运动指数。 |
| COLD | 3 | 感冒指数。 |
| CAR\_WASHING | 4 | 洗车指数。 |
| TOURISM | 5 | 旅游指数。 |
| SUN\_PROTECTION | 7 | 防晒指数。 |
| FISHING | 8 | 钓鱼指数。 |
| MORNING\_EXERCISE | 10 | 晨练指数。 |
| ALLERGY | 24 | 过敏指数。 |
| SKIING | 31 | 滑雪指数。 |
| STARGAZING | 34 | 观星指数。 |

## TideCategory

PhonePC/2in1TabletTVWearable

潮汐类别枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Weather.Core

**设备行为差异：** 对于5.0.5(17)及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中可正常使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED | 0 | 未定义。 |
| HIGH | 1 | 潮高。 |
| LOW | 2 | 潮低。 |
