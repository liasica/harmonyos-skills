---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-15
title: 获取未成年模式开启状态失败
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 获取未成年模式开启状态失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:22925c4749aacec8900ba31b076d410d635614b3c73a5eede7284510b35171b3
---

## 问题现象

在系统未成年模式已经开启的情况下，应用内显示未成年模式未开启，并未获取正确的状态。

## 背景知识

[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)：该方法为同步方法，调用该方法获取未成年人模式的开启状态，以及年龄段信息。应用可跟随未成年人模式开启状态，进行开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。

## 问题定位

根据代码关键词getMinorsProtectionInfoSync进行定位，发现应用并未调用getMinorsProtectionInfoSync()接口来获取未成年人模式的开启状态。

## 分析结论

应用并未调用getMinorsProtectionInfoSync()接口，导致查询未成年模式状态失败，与系统不同步。

## 修改建议

建议应用调用getMinorsProtectionInfoSync()接口进行查询，代码样例：

```ts
import { minorsProtection } from '@kit.AccountKit';

@Entry
@Component
struct minorsProtection1 {
  @State minorsProtectionMode: boolean = false;
  @State status: string = '';

  build() {
    Column() {
      Row() {
        Text('当前未成年模式开启状态：' + this.status)
          .fontSize(20)
          .margin(20)
      }
      .width('90%')

      Row() {
        Button('点击查询')
          .onClick(() => {
            this.minorsProtectionMode = minorsProtection.getMinorsProtectionInfoSync().minorsProtectionMode;
            this.status = this.minorsProtectionMode + '';
          })
      }
      .width('90%')
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
