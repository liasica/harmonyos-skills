---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-32
title: 地图POI搜索中adminCode是否可以仅返回区划代码
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 地图POI搜索中adminCode是否可以仅返回区划代码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:39460fd2f6fa5f56366bc9f87394fc9ff6770626a4edd10c8aec5bfd54c8ed39
---

## 问题现象

使用地图服务的[POI搜索](../harmonyos-guides/map-site-search.md)时，关键字搜索（[searchByText](../harmonyos-references/map-site.md#searchbytext)）和周边搜索（[nearbySearch](../harmonyos-references/map-site.md#nearbysearch)）的搜索结果中，当前返回的adminCode是9位数代码，是否可以仅返回区划代码？

```json
"sites": [
  {
    "siteId": "2031343823139177856",
    "name": "松山湖风景区",
    "formatAddress": "广东省东莞市松山湖至诚路12号",
    "addressComponent": {
      "countryName": "中国",
      "countryCode": "CN",
      "adminLevel1": "广东省",
      "adminLevel2": "东莞市",
      "adminLevel3": "松山湖",
      "adminCode": "441900401"
    }
  }
]
```

## 解决方案

关键字搜索（searchByText）和周边搜索（nearbySearch）的搜索结果中，[AddressComponent](../harmonyos-references/map-site.md#addresscomponent)描述详细的地址信息。其中adminCode表示行政区划代码。

在部分城市和地区搜索时，返回的行政区划代码adminCode超过了标准的6位区划代码，但adminCode的前6位仍是标准的6位区划代码。

如果需要查询位置的标准6位区划代码，需在返回结果中获取adminCode值后，自行截取前6位，如：广东省东莞市：441900。标准6位区划代码请参见[城市码及区划代码表](../harmonyos-references/map-citycode.md)。
