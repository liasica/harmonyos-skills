---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-146
title: ArkTS是否支持调用js文件中的方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持调用js文件中的方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:19+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:dce9c88aaefbf12054ae531a4b99daf61b1724607a446936226ba0bbc85e6631
---

**问题描述**

ArkTS是否支持调用js文件中的方法，如果支持，能否提供一下ArkTS与js交互的代码样例?

**解决措施**

ets文件调用js文件和正常ts/ets模块一样，import然后调用就行。

```
1. import {jsFunc} from './JsLib';
2. @Entry
3. @Component
4. struct Index {

6. build() {
7. Column({ space: 20 }) {
8. Text("Import Js Demo")
9. Button("Call Js")
10. .onClick(() => {
11. jsFunc(); // Call jsFunc from js file
12. })
13. }
14. .width("100%")
15. .height("100%")
16. .padding(10)
17. }
18. }
```

[ImportJs.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImportJs.ets#L21-L38)

JsLib.js文件中的demo如下：

```
1. export function jsFunc(){
2. console.info("this is a js function");
3. }
```

[JsLib.js](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/JsLib.js#L20-L22)
