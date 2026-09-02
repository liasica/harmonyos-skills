---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-2
title: 应用内设备信息仅显示品牌，型号信息缺失
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 应用内设备信息仅显示品牌，型号信息缺失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:63850397201f9b5741665e95eca0e6da0998844dbef60dea0d96c1173c22286d
---

## 问题现象

在应用内展示设备信息时，仅显示设备品牌，而未展示具体的设备型号，导致用户无法准确识别当前设备的具体规格或版本。

## 背景知识

[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)：提供终端设备信息查询的模块，当查询字段为brand时，表示查询设备品牌名称。当查询字段为marketName时，表示查询设备的外部产品系列。

## 问题定位

根据deviceInfo模块进行定位，发现应用展示设备信息时查询的字段为deviceInfo.brand，因此展示仅为品牌名，并非查询deviceInfo.marketName（设备的外部产品系列）。

## 分析结论

设备信息展示仅使用deviceInfo.brand字段，导致仅显示品牌名称，未体现具体型号。

## 修改建议

建议应用查询设备信息的查询字段设置为deviceInfo.marketName，展示足够的信息，示例代码：

```screen
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct DeviceInfoPage {
  @State brandInfo: string = '未知';
  @State marketNameInfo: string = '未知';

  aboutToAppear() {
    // 获取设备信息
    this.brandInfo = deviceInfo.brand;
    // 输出结果：the value of the brand is :HUAWEI
    console.info('the value of the device brand is :' + this.brandInfo);

    this.marketNameInfo = deviceInfo.marketName;
    // 输出结果：the value of the marketName is :Mate XX
    console.info('the value of the deviceInfo marketName is :' + this.marketNameInfo);
  }

  build() {
    Column() {
      Text(`品牌：${this.brandInfo}`)
        .fontSize(18)
        .margin(10)
        .fontWeight(FontWeight.Bold)

      Text(`市场型号：${this.marketNameInfo}`)
        .fontSize(18)
        .margin(10)
        .fontWeight(FontWeight.Bold)
    }
    .height('100%')
    .width('100%')
    .padding(20)
    .justifyContent(FlexAlign.Center)
  }
}
```
