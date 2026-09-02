---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-9
title: 应用无法获取气压信息
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 应用无法获取气压信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:aaf8d0c4073be37979087990dcdf007bee31898ab2f8498e6d90135f0685c74d
---

## 问题现象

应用无法获取当前位置的气压信息，页面上标准大气压一直显示获取中。

## 背景知识

* [SensorId](../harmonyos-references/js-apis-sensor.md#sensorid9)：表示当前支持订阅或取消订阅的传感器类型，比如气压计传感器的名称是BAROMETER，值为8。
* [sensor.getSensorList](../harmonyos-references/js-apis-sensor.md#sensorgetsensorlist9)：获取设备上的所有传感器信息。
* [sensor.getSingleSensor](../harmonyos-references/js-apis-sensor.md#sensorgetsinglesensor9)：获取指定传感器类型的属性信息。
* [BAROMETER](../harmonyos-references/js-apis-sensor.md#sensoronsensoridbarometer9)：订阅气压计传感器数据。

## 问题定位

1. 首先排查是否是网络问题。
   * 使用UIViewer查看页面布局，发现显示气压数据的页面非H5页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/j8OXNX2rSrGrQv3UZ-hb5g/zh-cn_image_0000002628615112.png "点击放大")
   * 查看HiLog日志，搜索"sensorId"、"SubscribeSensor"和包名等关键词，日志如下，发现应用调用了传感器获取相关信息，因此排除设备网络或请求异常导致的问题。

     ```txt
     09-14 13:16:06.834 26904 26904 I C02700/com.hm.example/SensorAgentProxy: in SubscribeSensor, In, sensorId:256
     ```
2. 搜索"not support"、"sensor: 8"等关键词，得到如下日志，"sensor: 8"表示气压计传感器的ID。该日志显示当前设备不支持气压计传感器。

   ```txt
   09-14 13:15:59.770  2943  2943 W C02302/hignss_110x_ohos/HisiLog: sensor: 8 is not support
   ```

## 分析结论

当前设备不支持气压计传感器，导致页面无法显示当前大气压。

## 修改建议

建议在进入相关页面时，检查当前设备是否支持气压计传感器，如果不支持，需要给出相应的提示。具体可以使用sensor.getSensorList或者sensor.getSingleSensor获取设备的传感器信息进行判断，示例代码如下：

```ts
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PressureDemo {
  @State pressure: number | undefined = undefined; // 气压值，单位：帕斯卡
  @State isSupportBarometer: boolean = false; // 设备是否支持气压计传感器

  aboutToAppear(): void {
    // 判断设备是否支持气压计传感器
    try {
      sensor.getSensorList((err: BusinessError, data: Array<sensor.Sensor>) => {
        if (err) {
          console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        for (let i = 0; i < data.length; i++) {
          if (data[i].sensorId === sensor.SensorId.BAROMETER) {
            this.isSupportBarometer = true;
            break;
          }
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
    }
    // 获取大气压
    try {
      sensor.on(sensor.SensorId.BAROMETER, (data: sensor.BarometerResponse) => {
        this.pressure = data.pressure;
      }, { interval: 100000000 });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
    }
  }

  build() {
    Column() {
      if (this.isSupportBarometer) {
        Text('气压值：');
        Text(`${this.pressure}Pa`);
      } else {
        Text('当前设备不支持气压计传感器');
      }
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：Pura 70 Pro为何获取不到海拔和气压？

A：Pura 70 Pro没有气压计，硬件不支持。sensor传感器订阅前可使用[getSingleSensor](../harmonyos-references/js-apis-sensor.md#sensorgetsinglesensor9)接口获取该传感器的信息，获取该传感器信息成功时可正常订阅传感器。或者使用[getSensorList](../harmonyos-references/js-apis-sensor.md#sensorgetsensorlist9)接口获取设备上的所有传感器信息。
