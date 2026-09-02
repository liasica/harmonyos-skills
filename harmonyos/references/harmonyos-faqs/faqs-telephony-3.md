---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-telephony-3
title: 调用call.makeCall发生编译告警：The API is not supported on all devices
breadcrumb: FAQ > 系统开发 > 网络 > 蜂窝通信（Telephony） > 调用call.makeCall发生编译告警：The API is not supported on all devices
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:68695e8dbb7d64937f0bf9fce184ac033fbfefeee842af52896e0139006dc32a
---

## 问题现象

调用Telephony Kit（蜂窝通信服务）的[call.makeCall](../harmonyos-references/js-apis-call.md#callmakecall7)方法会有编译告警：

```txt
The API is not supported on all devices. Use the canIUse condition to determine whether the API is supported. <ArkTSCheck>
```

## 背景知识

* SysCap，全称SystemCapability，即系统能力，指操作系统中每一个相对独立的特性，如蓝牙，WIFI，NFC，摄像头等，都是系统能力之一。每个系统能力对应多个API，随着目标设备是否支持该系统能力共同存在或消失。
* [call.makeCall](../harmonyos-references/js-apis-call.md#callmakecall7)使用的系统能力是：SystemCapability.Applications.Contacts。

## 解决方案

当设备不支持具体的系统能力时就会提示The API is not supported on all devices，该提示不会影响在具备系统能力的设备上运行结果。针对该提示，有两种处理方案：

* **方案一**：调用系统API之前可以先判断是否具备系统能力，可以防止运行时报错。

  ```ts
  import { call } from '@kit.TelephonyKit';

  @Entry
  @Component
  struct CallPhoneTest {

    build() {
      Row() {
        Column() {
          Button('Call Phone')
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              let result: boolean = call.hasVoiceCapability();
              if (result) {
                call.makeCall('135****1234', () => {
                });
              }
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```
* **方案二**：在module.json5可以移除未使用的设备类型。

  由于DevEco Studio默认创建的项目会包含phone，tablet，2in1三种设备类型。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Zl-OxdNuR5uAqvvMjsKl0A/zh-cn_image_0000002628773306.png "点击放大")

  tablet和2in1不具备SystemCapability.Applications.Contacts能力。

  所以默认没有修改设备类型时，会提示编译告警。移除下例代码中tablet，2in1后则不会再出现告警：

  ```json
  "deviceTypes": [
    "phone",
    "tablet",
    "2in1",
    "car",
    "wearable",
    "tv"
  ],
  ```

## 常见FAQ

Q：为什么平板没有SIM卡槽，使用canIUse("SystemCapability.Telephony.CallManager")判断系统能力返回为true?

A：由于分布式通信特性，通信相关部件需要在平板上保留，应用开发不能保证都会使用canIUse，为了避免应用因为不调用canIUse，直接使用API导致应用crash，设备需要预置所有的部件，所以当前对于平板设备，不建议使用canIUse机制。

Q：如何实现拉起拨号盘，直接拨打号码和发送短信？

A：目前可以参照[Telephony Kit（蜂窝通信服务）](../harmonyos-guides/telephony-kit.md)实现拨打电话和发送短信。
