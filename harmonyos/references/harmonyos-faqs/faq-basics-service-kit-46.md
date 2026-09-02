---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-46
title: 应用内电量与系统电量显示不一致
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 应用内电量与系统电量显示不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:e7cc147d9c051080f5cce7c54ddfb7a3dacb26e07b5e38b88a832bae8d62ee21
---

## 问题现象

应用右下角显示的电量与系统电量存在较大差异。例如，当手机系统显示电量为95%时，应用内部却显示约为30%。

## 背景知识

* 关于应用中显示电量，需要用到[@ohos.batteryInfo](../harmonyos-references/js-apis-battery-info.md)模块来实时获取电量，并在页面中展示出来。

  batteryInfo主要属性如下：

  | 名称 | 类型 | 可读 | 可写 | 说明 |
  | --- | --- | --- | --- | --- |
  | batterySOC | number | 是 | 否 | 表示当前设备剩余电池电量百分比。元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
  | chargingStatus | BatteryChargeState | 是 | 否 | 表示当前设备电池的充电状态。元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
  | healthStatus | BatteryHealthState | 是 | 否 | 表示当前设备电池的健康状态。 |
  | pluggedType | BatteryPluggedType | 是 | 否 | 表示当前设备连接的充电器类型。 |
  | voltage | number | 是 | 否 | 表示当前设备电池的电压，单位微伏。 |
  | technology | string | 是 | 否 | 表示当前设备电池的技术型号。 |
  | batteryTemperature | number | 是 | 否 | 表示当前设备电池的温度，单位0.1摄氏度。 |
  | isBatteryPresent | boolean | 是 | 否 | 表示当前设备是否支持电池或者电池是否在位。 |
  | batteryCapacityLevel | BatteryCapacityLevel | 是 | 否 | 表示当前设备电池电量的等级。 |
  | nowCurrent | number | 是 | 否 | 表示当前设备电池的电流，单位毫安。 |

* [COMMON\_EVENT\_BATTERY\_CHANGED](../harmonyos-references/commoneventmanager-definitions.md#common_event_battery_changed)：表示电池充电状态、电平和其他信息发生变化的公共事件的动作。当电池电量、电池电压、电池温度、电池健康状态、设备连接的充电器类型、充电器最大电流、充电器最大电压、电池充电状态、充电次数、电池的总容量、电池剩余容量、电池的技术型号、当前电池的电流、电池的充电类型变化时，将会触发事件通知服务发布该系统公共事件。

## 问题定位

1. 通过全局搜索batteryInfo或batterySOC等关键词，确认哪些页面或组件使用了@ohos.batteryInfo模块来获取设备电量信息。
2. 检查是否有使用setInterval或setTimeOut周期性获取电量信息。
3. 是否在每次获取电量后修改应用内电量数据。需要在getBatteryInfo()调用后，将batterySOC的值传递给页面组件进行渲染。

## 分析结论

应用内部电量显示仅在页面初始化时获取一次，未随系统电量变化而动态更新，导致显示结果与实际系统电量不一致。

## 修改建议

为了使应用内部电量显示与系统电量保持一致，建议应用通过动态订阅系统的公共事件来监听电量信息的变化。

具体实现可参考以下代码：

```ts
import { batteryInfo, BusinessError, commonEventManager } from '@kit.BasicServicesKit';

@Entry
@Component
struct ScanLoopPage2 {
  @State batterySOC: string = '';
  // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
  private subscriber: commonEventManager.CommonEventSubscriber | null = null;
  // 订阅者信息
  private subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    events: ['usual.event.BATTERY_CHANGED']
  };

  private sub() {
    // 创建订阅者回调
    commonEventManager.createSubscriber(this.subscribeInfo,
      (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
        if (err) {
          console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
          return;
        }
        console.info('Succeeded in creating subscriber.');
        this.subscriber = data;
        // 订阅公共事件回调
        commonEventManager.subscribe(this.subscriber,
          (err: BusinessError) => {
            if (err) {
              console.error(`Failed to subscribe common event. Code is ${err.code}, message is ${err.message}`);
              return;
            }
            this.batterySOC = `电量${batteryInfo.batterySOC}%`;
            console.info('监听到一次电池状态变化');
          });
      });
  }

  private unSub() {
    if (this.subscriber !== null) {
      commonEventManager.unsubscribe(this.subscriber, (err: BusinessError) => {
        if (err) {
          console.error(`Failed to unsubscribe. code is ${err.code}, message is ${err.message}`);
        } else {
          console.info(`Succeeded in unsubscribing.`);
          this.subscriber = null;
        }
      });
    }
  }

  aboutToAppear(): void {
    // 在合适的生命周期中开始订阅公共事件
    this.batterySOC = `电量${batteryInfo.batterySOC}%`;
    console.info(`当前电量：${batteryInfo.batterySOC}%`);
    this.sub();
  }

  aboutToDisappear(): void {
    // 在相应的生命周期回调中取消订阅，防止内存泄漏
    this.unSub();
  }

  build() {
    Column({ space: 20 }) {
      // 显示当前电量状态
      Text(this.batterySOC)
        .fontSize(18)
        .fontWeight(FontWeight.Bold)
        .textAlign(TextAlign.Center)
        .margin({ top: 20 });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#f0f0f0');
  }
}
```
