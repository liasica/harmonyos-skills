---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-23
title: 应用指南针在平板上有90度偏差
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 应用指南针在平板上有90度偏差
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:faf208e95c481d3e6214b5daf61350cb002ef70e36c736b9c5672da69b09da45
---

## 问题现象

应用中指南针在手机上正常使用，在平板上使用时偏差90度。

手机上现象：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Orh0XS3ZSieQ0Zv2byyaIA/zh-cn_image_0000002628392334.png "点击放大")

平板上现象：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Eh5Qn9xlRWaWWXRn_biV6Q/zh-cn_image_0000002658791621.png "点击放大")

## 背景知识

[传感器](../harmonyos-guides/sensor-overview.md)：系统传感器是应用访问底层硬件传感器的一种设备抽象概念。开发者根据传感器提供的Sensor接口，可以查询设备上的传感器，订阅传感器数据，并根据传感器数据定制相应的算法开发各类应用，比如指南针、运动健康、游戏等。

## 问题定位

查看日志关键字rotation，如果rotation为90或270，说明指南针传感器旋转了90度。

```screen
[invalidDomain][] SetCurrentRotation(4710): currentRotation: 270
[] UpdateViewportConfig(1185): [rotation,deviceRotation,transformHint,virtualPixelRatio]:[0,0,0,2.000000]
```

## 分析结论

平板设备默认横屏显示，而手机多采用竖屏，两者在传感器坐标系与屏幕坐标系不一致，应用未正确适配会导致方向发生偏差。

## 修改建议

处理方向传感器数据时增加设备方向补偿：

```screen
import { sensor } from '@kit.SensorServiceKit';
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct CompassPage {
  @State angle: number = 0; // 当前设备方向角度
  @State angleAll: number = 0; // 最终显示角度

  // 在页面生命周期中注册/注销监听
  onPageShow() {
    this.registerOrientationSensor();
  }

  onPageHide() {
    sensor.off(sensor.SensorId.ORIENTATION);
  }

  private registerOrientationSensor() {
    try {
      sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
        this.angle = Math.round(data.alpha); // 获取0-359度方位角
        if (deviceInfo.deviceType === 'tablet') {
          this.angleAll = -this.angle - 90;
        } else if (deviceInfo.deviceType === 'phone') {
          this.angleAll = -this.angle;
        }
      }, { interval: 100000000 }); // 100ms更新间隔
    } catch (err) {
      console.error(`Sensor error: ${err.code}, ${err.message}`);
    }
  }

  build() {
    Column() {
      // 指南针背景（需替换为实际资源路径）
      Image($r('app.media.compass_bg'))
        .width(300)
        .height(300)
        .rotate({ angle: this.angleAll });

      // 方向角度显示
      Text(`${Math.abs(this.angle)}°`)
        .fontSize(30)
        .margin(20);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
