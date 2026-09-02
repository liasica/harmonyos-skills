---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-99
title: 如何通过AOP统计方法执行时间
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何通过AOP统计方法执行时间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a86736b1444b3144925d14efa08ed870a081f2cbd3930a2fad0055e0a7ea702c
---

为了统计执行时间，可以使用addBefore记录开始时间，使用addAfter记录结束时间。

示例如下：

```ts
import { util } from '@kit.ArkTS';
import { systemDateTime } from '@kit.BasicServicesKit';

class Utils {
  Add(len: number): number {
    let num = 0;
    for (let index = 1; index <= len; index++) {
      num += index;
    }
    return num;
  }
}

let startTime = 0; // Initialization start time
let endTime = 0; // Initialization end time

util.Aspect.addBefore(Utils, 'Add', false, () => {
  startTime = systemDateTime.getTime(true); // Return the start time in nanoseconds
})

util.Aspect.addAfter(Utils, 'Add', false, () => {
  endTime = systemDateTime.getTime(true); // Return the end time in nanoseconds
})

let utilsObj = new Utils();
utilsObj.Add(1000);

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('get execution time')
          .onClick(() => {
            console.log('startTime:', startTime);
            console.log('endTime:', endTime);
            console.log('endTime - startTime = ', endTime - startTime);
          })
      }
      .width('100%')
    }.height('100%')
  }
}
```
