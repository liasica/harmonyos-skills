---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/weather-service-getweather
title: 获取天气数据
breadcrumb: 指南 > 应用服务 > Weather Service Kit（天气服务） > 获取天气数据
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:03+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:51063099f813e8f30fab822647f55ebba1a03cb0f961e96d09424528f6c4b67c
---

通过开发者提供的经纬度数据，获取天气数据，比如：实况数据、预警数据。

## 约束与限制

本kit支持Phone、Tablet、PC/2in1设备，并且从5.1.0(18)版本开始，新增支持Wearable设备，从6.1.0(23)版本开始，新增支持TV设备。

## （可选）获取当前位置经纬度

当开发者需要查询当前位置的天气数据时，需要先[申请权限](../harmonyos-references/js-apis-geolocationmanager.md#申请权限)，并且获取当前位置的经纬度信息。获取当前位置的经纬度信息方法如下：

1. 导入模块。

   ```typescript
   import { geoLocationManager } from '@kit.LocationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation-2)，获取经纬度。

   ```typescript
   return geoLocationManager.getCurrentLocation().then((result) => {
     hilog.info(DOMAIN, TAG, `current location latitude: ${result.latitude}, longitude: ${result.longitude}`);
     // ...
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN, TAG, `getCurrentLocation failed. Code: ${err.code}, message: ${err.message}`);
     // ...
   });
   ```

## 查询天气数据

Weather Service Kit依赖开发者提供的经纬度数据，返回格点天气数据。

1. 导入模块。

   ```typescript
   import { weatherService } from '@kit.WeatherServiceKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建请求对象。

   * location：使用[当前位置](weather-service-getweather.md#可选获取当前位置经纬度)的数据，或者填入查询目的地的经纬度。
   * limitedDatasets：为可选字段，传入一个数组，表示请求有限的数据集，取值范围参考weatherService.[Dataset](../harmonyos-references/weather-service-weatherservice.md#dataset)。

   ```typescript
   let request: weatherService.WeatherRequest = {
     location: {
       latitude: this.latitude,
       longitude: this.longitude
     },
     limitedDatasets: [weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS]
   };
   ```

   **说明** 

   如果limitedDatasets参数不传值，或者传入的数组为空，则默认返回Weather Service Kit支持的所有数据。根据实际需要的天气数据设置limitedDatasets，可以大幅降低接口请求时延。
3. 请求数据。

   ```typescript
   try {
     let weather: weatherService.Weather = await weatherService.getWeather(request);
     if (weather.current) {
       hilog.info(DOMAIN, TAG, `getWeather current temperature: ${weather.current.temperature}`);
     }
     if (weather.alerts?.length) {
       hilog.info(DOMAIN, TAG, `getWeather alert: ${weather.alerts[0].title}`);
     }
     this.weather = weather;
   } catch (err) {
     let error = err as BusinessError;
     this.errorMessage = `获取天气失败: ${error.message}`;
     hilog.error(DOMAIN, TAG, `getWeather failed. Code: ${error.code}, message: ${error.message}`);
   }
   ```

   **说明** 

   getWeather接口的使用依赖当前Ability的Context，如果开发者在无法通过[getHostContext()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)接口获取到Context的环境中请求天气数据，例如使用worker或者taskpool的子线程场景，请使用[weatherService.getWeatherWithContext(context, request)](../harmonyos-references/weather-service-weatherservice.md#weatherservicegetweatherwithcontext)方法并提供Ability的Context信息。
