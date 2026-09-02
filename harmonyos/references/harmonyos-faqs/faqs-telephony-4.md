---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-telephony-4
title: 如何检测设备SIM卡是否已变更
breadcrumb: FAQ > 系统开发 > 网络 > 蜂窝通信（Telephony） > 如何检测设备SIM卡是否已变更
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:59c7b14dff56c7d883aef9696697fb3391cbf10aab3e7ff45caf1dc4b4b5d276
---

## 问题现象

企业应用需要监听获取SIM卡标识，首次接入使用企业应用需要进行记录，以后认证使用企业应用都需要检测SIM卡是否做过变更，如何实现检测SIM卡是否已变更的功能？

## 背景知识

* [SIM卡管理模块](../harmonyos-references/js-apis-sim.md#simgetsimoperatornumeric)提供了SIM卡管理的基础能力，包括获取指定卡槽SIM卡的ISO国家码、归属PLMN号、服务提供商名称、SIM卡状态、卡类型、是否插卡、是否激活等。
* SIM卡管理模块中的[getSimOperatorNumeric](../harmonyos-references/js-apis-sim.md#simgetsimoperatornumeric)接口可以获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。

## 解决方案

可以在首次接入使用应用时，将获取的PLMN信息存储在一个文件或系统设置中，后续再次使用应用时，则重新获取PLMN信息，与首次存储的PLMN信息进行匹配，进而判断SIM卡是否做过变更。

样例代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

@Entry
@Component
struct Index {
  // 先获取首次存储PLMN号
  plmn: string = 'xxxxxxxxxxx';

  getSimOperatorNumeric() {
    // 获取SIM卡PLMN号
    sim.getSimOperatorNumeric(0, (err: BusinessError, data: string) => {
      console.info(`err: ${err.code} ,PLMN号: ${data}`);
      if (data === this.plmn) {
        // SIM卡未变更
      } else {
        // SIM卡已变更
      }
    });
  }

  build() {
    Column() {
      Button('getSimOperatorNumeric').onClick(() => {
        this.getSimOperatorNumeric();
      });
    }.height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```
