---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-14
title: 使用POI关键字搜索返回数据为空排查指导
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 使用POI关键字搜索返回数据为空排查指导
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:2d75535527beb32c4a41760d3a90fae99d673cf11643325663e5606c7585dcc7
---

## 问题现象

使用关键字搜索获取不到结果，POI关键字搜索返回数据为空。

## 背景知识

[POI搜索](../harmonyos-guides/map-site-search.md)提供多种查询POI信息的能力：

* [关键字搜索](../harmonyos-guides/map-site-search.md#关键字搜索)：通过指定的关键字和可选的地理范围，查询诸如旅游景点、企业和学校之类的地点。
* [周边搜索](../harmonyos-guides/map-site-search.md#周边搜索)：基于用户设备位置进行地点查找。
* [自动补全](../harmonyos-guides/map-site-search.md#自动补全)：根据输入的关键字返回预测的输入关键字和地点查询建议。
* [地点详情](../harmonyos-guides/map-site-search.md#地点详情)：查询某个地点更详细的信息。

## 问题定位

1. 首先需要排查下是否[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
2. 开启“地图服务”开放能力后，是否完成[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。
3. 若使用原有的Profile文件，还要确保在申请Profile文件之前已开启“地图服务”，否则开启后需要重新申请Profile文件，并重新配置签名信息。

## 分析结论

开通地图服务后未更新调试证书添加公钥指纹和调试Profile，DevEco Studio未更新手动签名的文件，导致地图服务开通却未生效。

## 修改建议

步骤如下：

1. 在[AGC](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)创建对应的项目并添加相应的应用，同时“开通地图服务”；
2. [申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)，使用添加指纹后的调试证书去[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)；
3. 上架前，需要把发布证书公钥指纹也添加上；
4. 使用调试证书和调试Profile来[配置手动签名](../harmonyos-guides/ide-signing.md#section297715173233)，使用[自动签名](../harmonyos-guides/ide-signing.md#section18815157237)无法使用地图服务；
5. 运行项目查看搜索结果。

配置完成后运行示例代码：

```ts
import { site } from '@kit.MapKit';

@Entry
@Component
struct Index {
  async poiSearch(){
    let params: site.SearchByTextParams = {
      // 指定关键字，xxx需替换具体地址
      query: "xxxxxxxx",
      // 经纬度坐标
      location: {
        latitude: 34.19390192547735,
        longitude: 108.87269875520396
      },
      // 指定地理位置的范围半径
      radius: 10000,
      language: "zh"
    };
    // 返回关键字搜索结果
    const result = await site.searchByText(params);
    console.log("搜索结果：",JSON.stringify(result));
  }
  build() {
    Column() {
      Button('click').onClick(async ()=>{
        await  this.poiSearch();
      })
    }
    .width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

## 常见FAQ

Q：使用POI关键字搜索省份/城市信息为什么只返回一条数据？

A：搜索区划信息时返回最准确的一个，如搜索出关键字相关的地点可以使用自动补全接口：queryAutoComplete。

Q：花瓣地图如何监听点击POI对象？

A：建议使用[on('poiClick')](../harmonyos-references/map-map-mapcomponentcontroller.md#onpoiclick)监听POI点击事件。支持传递多个callback异步回调。
