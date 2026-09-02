---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-10
title: 使用POI关键字搜索结果跟花瓣地图搜索不一致
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 使用POI关键字搜索结果跟花瓣地图搜索不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:d3e9250f46692e13a29b58f46cf12078a69c2c8a16cadccdae3009d49afe6015
---

## 问题现象

调用[searchByText](../harmonyos-references/map-site.md#searchbytext)进行地点搜索的时候，返回的数据跟用花瓣地图返回的结果差异较大。如何能返回跟花瓣地图相同的结果。

## 解决方案

本解决方案需要开通[地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)，并在项目中进行相应配置。

[SearchByTextParams](../harmonyos-references/map-site.md#searchbytextparams)：SearchByTextParams定义了搜索关键字的参数。

花瓣地图APP搜索会默认获取当前的经纬度参数并传值到SearchByTextParams。所以调用API进行地点搜索的时候，需要通过网页地图，或者其他方法[获取到当前的经纬度信息](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)，并传值到SearchByTextParams。就可以获取跟花瓣地图搜索相同的值。

```ts
import { site } from '@kit.MapKit';

@Entry
@Component
struct Index {
  async poiSearch() {
    let params: site.SearchByTextParams = {
      query: '牛肉',
      location: {
        latitude: 1.000,
        longitude: 2.000
      },

      radius: 10000,
      language: 'zh'
    };
    try {
      const result = (await site.searchByText(params)).totalCount;
      console.info('搜索结果：', JSON.stringify(result));
    } catch (error) {
      console.error(`Failed to code ${error.code},message is ${error.message}`);
    }
  }

  build() {
    Column() {
      Button('click').onClick(async () => {
        await this.poiSearch();
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
