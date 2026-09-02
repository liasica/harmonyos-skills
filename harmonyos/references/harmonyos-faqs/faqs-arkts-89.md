---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-89
title: 如何将JSON对象转换成HashMap
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将JSON对象转换成HashMap
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2936e913380f7b9edb0031422ef89fe00bfb781bb3b2ad12f761468a7ed42a16
---

可以参考如下示例代码：

```ts
import { HashMap } from '@kit.ArkTS';

let str: string = '{\"common_params\": {' +
  '\"city_id\": 1,' +
  '\"nav_id_list\": \"\",' +
  '\"show_hook_card\": 2,' +
  '\"use_one_stop_structure\": 1,' +
  '\"version_tag\": \"homepageonestop\"' +
  '}' +
  '}';

let jsonObj: Object = JSON.parse(str);
let commObj = (jsonObj as Record<string, Object>);
let commRecord = (commObj['common_params'] as Record<string, Object>);
let keyStr = Object.keys(commRecord);

for (let index: number = 0; index < keyStr.length; index++) {
  commRecord[keyStr[index].toString()].toString();
}

let hashMapData: HashMap<string, Object> = new HashMap();
hashMapData.set('common_params', commRecord);

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('JSON to HashMap')
          .onClick(() => {
            // common_params: {"city_id":1,"nav_id_list":"","show_hook_card":2,"use_one_stop_structure":1,"version_tag":"homepageonestop"}
            console.log('common_params:', JSON.stringify(hashMapData.get('common_params')));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
