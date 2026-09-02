---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-146
title: ArkTS是否支持调用js文件中的方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持调用js文件中的方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:9591ea2521d156aba65480e458b3a78aa0c596b9aaf94183afd5edcc105b0087
---

**问题描述**

ArkTS是否支持调用js文件中的方法，如果支持，能否提供一下ArkTS与js交互的代码样例?

**解决措施**

ets文件调用js文件和正常ts/ets模块一样，import然后调用就行。

```ts
import {jsFunc} from './JsLib';
@Entry
@Component
struct Index {

  build() {
    Column({ space: 20 }) {
      Text("Import Js Demo")
      Button("Call Js")
        .onClick(() => {
          jsFunc(); // Call jsFunc from js file
        })
    }
    .width("100%")
    .height("100%")
    .padding(10)
  }
}
```

JsLib.js文件中的demo如下：

```json
export function jsFunc(){
    console.info("this is a js function");
}
```
