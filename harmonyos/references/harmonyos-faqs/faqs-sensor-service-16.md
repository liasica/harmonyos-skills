---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-16
title: 如何确认硬件是否具备某个传感器
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 如何确认硬件是否具备某个传感器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:33da9f2572746e1d64f31d3a862758408dafcdb1e6fe3a2b6f01a9f506fd27dd
---

## 问题现象

当不确定开发设备是否具备某个传感器的情况下，直接进行开发调试可能会导致以下情况：

* 执行sensor.on()，sensor.off()会崩溃报错：The parameter invalid.；
* 某些传感器不具备但可以执行，导致获取传感器结果异常，结果可能为传感器型号（固定值），这种情况下会导致排查困难。

## 背景知识

[传感器类型](../harmonyos-guides/sensor-overview.md#传感器类型)：列举了目前支持的传感器类型。

[SensorId](../harmonyos-references/js-apis-sensor.md#sensorid9)：传感器类型对应的id值。

## 解决方案

* **开发前查询**

  开发前确认软件目标设备是否具备该传感器，来进行功能规划：

  1. 连接设备，在IDE终端使用hdc shell命令；
  2. 输入指令：hidumper -s 3601 -a -l可查看设备具备的所有传感器，根据设备具备的传感器进行开发。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/C5V6-LxrSxWTvtgpHQ3pjA/zh-cn_image_0000002658974323.png "点击放大")
* **使用前查询**

  同一套代码可能涉及多种设备，开发中获取运行设备支持的传感器类型列表，根据SensorId判断是否具备某个传感器进行针对性开发：

  ```ts
  query() {
    // 获取传感器列表
    try {
      sensor.getSensorList((err: BusinessError, data: Array<sensor.Sensor>) => {
        if (err) {
          console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        this.sensorList = data;
        this.sensorListStr = [];
        for (let i = 0; i < data.length; i++) {
          this.sensorListStr.push(data[i].sensorId + ' ' + data[i].sensorName);
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
    }
  }
  ```
* **使用try catch保证不崩溃**

  下面以重力传感器为例：

  ```ts
  onDegree() {
    try {
      sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
        this.degree = [];
        this.degree.push(data.x.toString());
        this.degree.push(data.y.toString());
        this.degree.push(data.z.toString());
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      this.degree.push(e.code.toString());
      this.degree.push(e.message);
      console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
    }
  }

  disDegree() {
    try {
      sensor.off(sensor.SensorId.GRAVITY);
      this.degree = [];
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      this.degree.push(e.code.toString());
      this.degree.push(e.message);
      console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
    }
  }
  ```
* 完整示例代码如下：

  ```ts
  import { sensor } from '@kit.SensorServiceKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Index {
    sensorList: Array<sensor.Sensor> = [];
    @State sensorListStr: Array<string> = [];
    @State degree: Array<string> = [];

    query() {
      // 获取传感器列表
      try {
        sensor.getSensorList((err: BusinessError, data: Array<sensor.Sensor>) => {
          if (err) {
            console.error(`Failed to get sensorList. Code: ${err.code}, message: ${err.message}`);
            return;
          }
          this.sensorList = data;
          this.sensorListStr = [];
          for (let i = 0; i < data.length; i++) {
            this.sensorListStr.push(data[i].sensorId + ' ' + data[i].sensorName);
          }
        });
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
      }
    }

    onDegree() {
      try {
        sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
          this.degree = [];
          this.degree.push(data.x.toString());
          this.degree.push(data.y.toString());
          this.degree.push(data.z.toString());
        });
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        this.degree.push(e.code.toString());
        this.degree.push(e.message);
        console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
      }
    }

    disDegree() {
      try {
        sensor.off(sensor.SensorId.GRAVITY);
        this.degree = [];
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        this.degree.push(e.code.toString());
        this.degree.push(e.message);
        console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
      }
    }

    build() {
      Column({ space: 16 }) {
        Button('查询支持的传感器列表')
          .onClick(() => {
            this.query();
          });
        Button('启动重力传感器')
          .onClick(() => {
            this.onDegree();
          });
        Button('关闭重力传感器')
          .onClick(() => {
            this.disDegree();
          });
        Text('重力传感器数据：');
        Text(`${this.degree.join('\n')}`);
        Text('传感器列表如下：\n ');
        Text(`${this.sensorListStr.join('\n')}`);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

## 总结

涉及传感器接口时：建议加try catch避免代码崩溃。
