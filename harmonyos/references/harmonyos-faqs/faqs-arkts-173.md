---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-173
title: ArkTS如何解析GeoJSON
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS如何解析GeoJSON
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:69bd415b58b6261061994afd1dadc0d4b086298927a0cffb3545d1b0262593ce
---

## 问题现象

GeoJSON为一个类型不固定结构，属性参数都是可变的。如何实现对GeoJSON的解析。

## 背景知识

GeoJSON：是一种对各种地理数据结构进行编码的格式，基于JavaScript对象表示法（JavaScript Object Notation，简称JSON）的地理空间信息数据交换格式。

## 解决方案

首先通过JSON.parse将GeoJSON从字符串解析出来，直接解析会报错所以需要解析为一个Record<string, string>对象。再通过递归遍历的方式对Record对象进行遍历，达到解析GeoJSON对象的目的。

```ts
import { JSON } from '@kit.ArkTS';

function geoJsonAnalysisHandler(geoJsonData: object) {
  Object.keys(geoJsonData).forEach(key => {
    if (key == 'coordinates') {
      console.info(JSON.stringify(Array.from(geoJsonData['coordinates'] as string)));
    } else if ((typeof geoJsonData[key]) === 'object') {
      console.info(key, ':');
      geoJsonAnalysisHandler(geoJsonData[key]);
    } else {
      console.info(key, geoJsonData[key]);
    }
  });
}

@Entry
@Component
struct GeoJsonAnalysis {
  public geoJsonString: string = `
  { "type": "FeatureCollection",
    "features": [
      { "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
        "properties": {"prop0": "value0"}
      },
      { "type": "Feature",
        "geometry": {
          "type": "LineString",
          "coordinates": [
            [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
          ]
        },
        "properties": {
          "prop0": "value0",
          "prop1": 0.0
        }
      },
      { "type": "Feature",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
              [100.0, 1.0], [100.0, 0.0] ]
          ]
        },
        "properties": {
          "prop0": "value0",
          "prop1": {"this": "that"}
        }
      }
    ]
  }`;

  build() {
    Column() {
      Button('点击测试')
        .onClick(() => {
          let geoJsonData = JSON.parse(this.geoJsonString) as Record<string, string>;
          geoJsonAnalysisHandler(geoJsonData);
        });
    }
    .align(Alignment.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
