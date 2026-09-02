---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-139
title: 如何获取实时网络速度
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何获取实时网络速度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:74b5332fc1d0e6efe427c4d1ce96c773294322ea76941b93f0737112ddef8285
---

## 问题现象

如何获取实时的网速，并且动态地显示出来？

## 背景知识

[netQuality（网络质量）](../harmonyos-references/networkboost-netquality.md)：提供网络质量实时评估、网络场景识别以及弱信号预测等能力，以便应用针对弱网等环境下实现网络自适应，包括缓存、码率、帧率、分辨率等策略的调整。应用也可以通过网络质量中的应用传输体验反馈接口，触发系统进行网络加速。

## 解决方案

1. 通过[on('netQosChange')](../harmonyos-references/networkboost-netquality.md#netqualityonnetqoschange)订阅网络质量信息，并通过返回的NetworkQos数组获取实时网速。
2. 在不需要的时候要取消网络质量信息的订阅。

完整实例代码如下：

```ts
import { netQuality } from '@kit.NetworkBoostKit';
import { Decimal } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  network: number | undefined = 0;
  @State networkSpeed: string = '';

  networkSpeedMonitor() {
    try {
      netQuality.on('netQosChange', (info: Array<netQuality.NetworkQos>) => {
        if (info.length > 0) {
          info.forEach((networkQos) => {
            if (networkQos.linkDownRate / 1000000 / 8 <= 1024) {
              this.network = Number(new Decimal(networkQos.linkDownRate / 1000000 / 8 * 1024).toDecimalPlaces(2));
              this.networkSpeed = String(this.network) + 'KB/s';
            } else {
              this.network = Number(new Decimal(networkQos.linkDownRate / 1000000 / 8).toDecimalPlaces(1));
              this.networkSpeed = String(this.network) + 'MB/s';
            }
          });
        }
      });
    } catch (err) {
      hilog.info(0x0000, 'networkSpeed',
        `errorCode:${(err as BusinessError).code},errorMessage:${(err as BusinessError).message}`);
    }
  }

  networkSpeedMonitorOff() {
    try {
      netQuality.off('netQosChange');
      hilog.info(0x0000, 'networkSpeed', 'networkSpeedMonitorOff success');
    } catch (err) {
      hilog.info(0x0000, 'networkSpeed',
        `monitor off err,errCode:${(err as BusinessError).code},errMessage:${(err as BusinessError).message}`);
    }
  }

  aboutToAppear(): void {
    this.networkSpeedMonitor();
  }

  aboutToDisappear(): void {
    this.networkSpeedMonitorOff();
  }

  build() {
    Column() {
      Text(this.networkSpeed)
        .fontSize(18)
        .margin({ top: 80 });
    }
    .size({ height: '100%', width: '100%' });
  }
}
```

## 常见FAQ

Q：如何根据网络质量回调信息[NetworkQos](../harmonyos-references/networkboost-netquality.md#networkqos)的rttMs属性判断网络好坏？

A：网络质量回调信息中的rttMs为RTT时延，表示统计时间间隔内，[PathType](../harmonyos-references/networkboost-netquality.md#pathtype)对应数据路径上，所有的TCP上下行数据包的平均往返时延，单位为ms，取值范围是任意正数。通常情况下，rttMs≤100ms表示优秀的网络体验，rttMs≥500ms表示极差的网络体验。

Q：在监听netQosChange时，无网络情况下为什么没有回调？

A：无网络情况下，调用[on('netQosChange')](../harmonyos-references/networkboost-netquality.md#netqualityonnetqoschange)监听接口无回调是正常现象。此监听接口需在设备联网的场景才会触发回调。

Q：在监听netSceneChange时，为什么会无任何回调？

A：[on('netSceneChange')](../harmonyos-references/networkboost-netquality.md#netqualityonnetscenechange)监听接口的回调触发条件为：网络在[PathType](../harmonyos-references/networkboost-netquality.md#pathtype)枚举值标注的场景下切换。

Q：on('netQosChange')监听接口回调的是一组数据，怎么判断是否弱网比较好？

A：应用可根据自身业务特点，选择网络质量评估信息中一种或多种自定义门限来判决为弱网。参考文档：[弱网感知判决](../harmonyos-guides/networkboost-weaksignaljudge.md)。
