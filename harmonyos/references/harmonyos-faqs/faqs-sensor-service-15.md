---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-15
title: 罗盘指南针方向与实际不符
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 罗盘指南针方向与实际不符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5948a81e3fc3f7586b587aabb0f110f74d4a99fc492884b93ab8a97d75260a9d
---

## 问题现象

应用运行时，指南针文本指示方向与图形显示方向不一致。例如指南针文本描述为北偏东61°，但是指南针图片显示的方向是北偏西61°，导致用户方位判断出现偏差。

## 背景知识

* [指南针](../architecture-guides/compass_effect-0000002317882746.md)：是一种常见的工具类应用，用于检测设备的物理方向。
* [OrientationResponse](../harmonyos-references/js-apis-sensor.md#orientationresponse)：方向传感器数据，继承于Response。
* [RotationVectorResponse](../harmonyos-references/js-apis-sensor.md#rotationvectorresponse)：旋转矢量传感器数据，继承于Response。

## 问题定位

1. 全局搜索关键词sensor，排查传感器监听与角度获取的方法是否正确。有以下两种方式获取角度：
   * 方式一：通过监听方向传感器获取角度（推荐）。

     ```ts
     // 监听方向传感器
     sensor.on(
       sensor.SensorId.ORIENTATION,
       this.angleChange,
       {
         interval: Constants.SENSOR_INTERVAL
       });

     // 获取角度
     public angleChange = (data: sensor.OrientationResponse) => {
       this.angle = Math.round(data.alpha);
     }
     ```
   * 方式二：通过监听旋转矢量传感器获取角度。

     ```ts
     // 监听旋转矢量传感器
     sensor.on(
       sensor.SensorId.ROTATION_VECTOR,
       this.angleChange2,
       {
         interval: Constants.SENSOR_INTERVAL
       });

     public angleChange2 = (data: sensor.RotationVectorResponse) => {
       this.rotation[0] = data.x;
       this.rotation[1] = data.y;
       this.rotation[2] = data.z;
       this.rotation[3] = data.w;
     }

     // 获取角度
     sensor.getRotationMatrix(this.rotation,(err,data)=>{
       sensor.getOrientation(data, (err,data)=>{
         this.angle2 = data[0] * 180 / 3.1415926;
       });
     });
     ```
2. 全局搜索关键词rotate，排查指南针背景旋转方向是否正确。如下所示，设置angle:this.angle会导致指南针背景的旋转方向与实际方向相反。

   ```ts
   Image($r('app.media.compass_background'))
     .rotate({
       angle: this.angle
     });
   ```

## 分析结论

1. 未正确监听方向传感器，或未从传感器数据中正确提取角度值。
2. 指南针背景旋转方向设置错误，导致视觉效果与实际方向不一致。

## 修改建议

1. 调用sensor.on方法监听方向传感器sensor.SensorId.ORIENTATION，获取转动角度sensor.OrientationResponse.alpha。
2. 修正指南针背景旋转方向。

   参考代码如下，代码中的资源文件需进行替换：

   ```ts
   import { common } from '@kit.AbilityKit';
   import { sensor } from '@kit.SensorServiceKit';

   @Entry
   @Component
   struct CompassPage {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     @State angle: number = 0;
     @State angleText: string = '';
     @State angleShow: number = 0;
     public angleChange = (data: sensor.OrientationResponse) => {
       this.angle = data.alpha;
       if (this.angle > 359 || this.angle < 1) {
         this.angleText = '北';
         this.angleShow = 0;
       } else if (this.angle >= 1 && this.angle <= 89) {
         this.angleText = '北偏东';
         this.angleShow = this.angle;
       } else if (this.angle > 89 && this.angle < 91) {
         this.angleText = '东';
         this.angleShow = 0;
       } else if (this.angle >= 91 && this.angle <= 179) {
         this.angleText = '南偏东';
         this.angleShow = 180 - this.angle;
       } else if (this.angle > 179 && this.angle < 181) {
         this.angleText = '南';
         this.angleShow = 0;
       } else if (this.angle >= 181 && this.angle <= 269) {
         this.angleText = '南偏西';
         this.angleShow = this.angle - 180;
       } else if (this.angle > 269 && this.angle < 271) {
         this.angleText = '西';
         this.angleShow = 0;
       } else if (this.angle >= 271 && this.angle <= 359) {
         this.angleText = '北偏西';
         this.angleShow = 360 - this.angle;
       }
     };

     aboutToAppear(): void {
       sensor.on(
         sensor.SensorId.ORIENTATION,
         this.angleChange,
         {
           interval: 10000000
         });
     }

     build() {
       Column() {
         Row() {
           Text(this.angleText + Math.floor(this.angleShow) + '°')
             .fontSize(45)
             .fontWeight(FontWeight.Regular)
             .layoutWeight(1)
             .textAlign(TextAlign.Center);
         }
         .margin({ top: 32 })
         .width('100%');

         CompassView({
           angle: this.angle,
         })
           .width(290)
           .height(290)
           .margin({ top: 56 });
       }
       .justifyContent(FlexAlign.Center)
       .backgroundColor('#F1F3F5')
       .height('100%')
       .width('100%')
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
     }
   }

   @Component
   export struct CompassView {
     @Prop angle: number;

     build() {
       Stack() {
         Stack() {
           Image($r('app.media.compass_background')).width(290).height(290);
           Image($r('app.media.circle_secondary')).width(290).height(290);
           Image($r('app.media.circle_first')).width(290).height(290);
           Image($r('app.media.compass_arrow')).width(240).height(240);
         }
         .width(290).height(290)
         .rotate({
           x: 0,
           y: 0,
           z: 1,
           angle: -this.angle
         });

         Line()
           .width(3)
           .height(26)
           .backgroundColor('#254FF7')
           .borderRadius('50%')
           .margin({ bottom: 280 });
       }.scale({ x: 1, y: 1 });
     }
   }
   ```
