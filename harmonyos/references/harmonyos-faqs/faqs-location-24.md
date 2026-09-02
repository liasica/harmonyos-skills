---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-24
title: 如何监听/获取“位置”配置的开关状态
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何监听/获取“位置”配置的开关状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:248ee655fd2874170b308b5a8c542d6d061a73a2aeb17781883b62ec0870e38e
---

## 问题现象

应用使用位置服务时，需要判断用户是否开启了“位置”配置，进一步实现相关业务，如何监听和获取“位置”配置的开关状态？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/I7oW5lmnQYGzannB2cVB9Q/zh-cn_image_0000002628554432.png "点击放大")

## 背景知识

* [geoLocationManager.on('locationEnabledChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationenabledchange)：订阅位置服务状态变化。
* [geoLocationManager.isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)：判断位置服务是否已经开启。

## 解决方案

* 监听“位置”配置的开关状态。

  通过geoLocationManager.on('locationEnabledChange')接口订阅“位置”配置的开关状态，在“设置-隐私和安全-位置-访问我的位置”或者手机右上角下拉的“位置”配置发生变化时，可以实时监听到变化并返回开关状态。
* 获取“位置”配置的开关状态。

  通过geoLocationManager.isLocationEnabled接口查询当前“位置”配置的开关状态。

完整示例参考如下：

```ts
import { geoLocationManager } from '@kit.LocationKit';

@Entry
@Component
struct CheckLocationEnable {
  @State getLocationEnableState: string = '未知';
  @State monitorEnableState: string = '未知';

  async aboutToAppear() {
    let locationEnabledChange = (state: boolean): void => {
      if (state) {
        this.monitorEnableState = '开';
      } else {
        this.monitorEnableState = '关';
      }
      console.info('locationEnabledChange: ' + JSON.stringify(state));
    };
    try {
      geoLocationManager.on('locationEnabledChange', locationEnabledChange);
    } catch (err) {
      console.error('errCode:' + err.code + ', message:' + err.message);
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('获取当前位置开关状态')
        .onClick(() => {
          try {
            let locationEnabled = geoLocationManager.isLocationEnabled();
            if (locationEnabled) {
              this.getLocationEnableState = '开';
            } else {
              this.getLocationEnableState = '关';
            }
          } catch (err) {
            console.error('errCode:' + err.code + ', message:' + err.message);
          }
        });
      Text(`获取的位置开关状态为: ${this.getLocationEnableState}`);
      Text(`监听的位置开关状态为: ${this.monitorEnableState}`);
    }
    .height('100%')
    .width('100%')
    .padding(20);
  }
}
```
