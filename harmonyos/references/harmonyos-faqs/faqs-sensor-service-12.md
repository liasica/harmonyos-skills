---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-12
title: 平板上指南针方位指向异常
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 平板上指南针方位指向异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:b38ba94683e512306697965e01f0a7067067a6ed8ca63c0be14816341252dc5a
---

## 问题现象

平板设备上具有方位指示功能的应用，指向方位和实际的方位不一致。

## 背景知识

* [MAGNETIC\_FIELD](../harmonyos-references/js-apis-sensor.md#sensoronsensoridmagnetic_field9)：通过订阅该字段获取地磁传感器数据，以此计算方位。
* [on('rotationChange')](../harmonyos-references/arkts-apis-window-window.md#onrotationchange19)：开启窗口旋转变化的监听。

## 问题定位

1. 在手机端打开该应用，与系统自带的指南针应用对比，两者指示方位一致。
2. 在平板端默认横屏状态下，打开该应用，指示方位与系统指南针应用存在固定90度的偏差，指示方位不正确，问题复现。
3. 关闭系统旋转锁定，将平板切换成竖屏状态，该应用与系统指南针应用指示方位一致，指向正确。

## 分析结论

应用/元服务获取传感器数据无异常，由于没有适配横屏，导致该问题。

## 修改建议

* 方式一：适配横屏，检测屏幕横屏状态时，将计算的方位旋转90度。

  以[指南针](../architecture-guides/compass_effect-0000002317882746.md)示例代码为基础，修改CompassPage.ets，通过点击“旋转屏幕”模拟屏幕横竖屏。

  ```screen
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { CompassView } from '../component/CompassView';
  import { CompassController } from '../controller/CompassController';

  @Entry
  @Component
  struct CompassPage {
    context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    windowClass = (this.context as common.UIAbilityContext).windowStage.getMainWindowSync();
    @State angle: number = 0;
    @State angleShow: ResourceStr = $r('app.string.N', 0);
    private orientation: boolean = false;
    private controller: CompassController = new CompassController();

    aboutToAppear(): void {
      this.windowClass.on('rotationChange', (info: window.RotationChangeInfo) => {
        if (info.type === window.RotationChangeType.WINDOW_DID_ROTATE && (info.orientation & 0x01)) {
          this.orientation = true;
        } else {
          this.orientation = false;
        }
      });

      this.controller.setAngleUpdateListener((angle: number) => {
        this.angle = angle + (this.orientation ? 90 : 0);
        this.angleShow = this.controller.scalAngle(this.angle);
      });

      this.controller.getAngle();
    }

    aboutToDisappear(): void {
      this.windowClass.off('rotationChange');
    }

    build() {
      Column() {
        Row() {
          Text(this.angleShow)
            .fontSize(45)
            .layoutWeight(1)
            .textAlign(TextAlign.End);
          Row() {
            Text($r('app.string.degree', this.angle))
              .fontSize(45)
              .textAlign(TextAlign.Start);
            Text('旋转屏幕')
              .fontStyle(FontStyle.Italic)
              .onClick(() => {
                let orientation = this.windowClass.getPreferredOrientation() !== window.Orientation.LANDSCAPE ?
                  window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT;
                this.windowClass.setPreferredOrientation(orientation);
              });
          }
            .layoutWeight(1);
        }.margin({ top: 32 })
        .width('100%');

        CompassView({
          angle: this.angle,
        }).width(200).height(200)
          .margin({ top: 56 });

      }.backgroundColor('#F1F3F5')
      .height('100%')
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```
* 方式二：固定该应用/元服务的屏幕状态为竖屏。

  以[指南针](../architecture-guides/compass_effect-0000002317882746.md)示例代码为基础，修改CompassPage.ets，固定竖屏显示。

  ```screen
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { CompassView } from '../component/CompassView';
  import { CompassController } from '../controller/CompassController';

  @Entry
  @Component
  struct CompassPage {
    context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    windowClass = (this.context as common.UIAbilityContext).windowStage.getMainWindowSync();
    @State angle: number = 0;
    @State angleShow: ResourceStr = $r('app.string.N', 0);
    private controller: CompassController = new CompassController();

    aboutToAppear(): void {
      this.windowClass.setPreferredOrientation(window.Orientation.PORTRAIT);
      this.controller.setAngleUpdateListener((angle: number) => {
        this.angle = angle;
        this.angleShow = this.controller.scalAngle(this.angle);
      });

      this.controller.getAngle();
    }

    build() {
      Column() {
        Row() {
          Text(this.angleShow)
            .fontSize(45)
            .layoutWeight(1)
            .textAlign(TextAlign.End);

          Text($r('app.string.degree', this.angle))
            .fontSize(45)
            .layoutWeight(1)
            .textAlign(TextAlign.Start);

        }.margin({ top: 32 })
        .width('100%');

        CompassView({
          angle: this.angle,
        }).width(270).height(270)
          .margin({ top: 56 });

      }.backgroundColor('#F1F3F5')
      .height('100%')
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```
