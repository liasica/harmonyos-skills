---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-138
title: ArkTS如何定义callback函数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS如何定义callback函数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e12f4a5dc9aada9441bf8d76ee49d3232f79338524b42ccd6f080f85a18434e7
---

定义一个callback函数的样例，参考代码如下：

1. 定义回调函数

   ```
   1. // Define 2 parameters on the page, return empty callback function
   2. myCallback: (a: number,b: string) => void = () => {}
   ```

   [DefineCallback.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DefineCallback.ets#L23-L24)
2. 在使用时进行初始化赋值

   ```
   1. aboutToAppear() {
   2. // Initialization of callback function
   3. this.myCallback = (a,b) => {
   4. console.info(`handle myCallback a=${a},b=${b}`)
   5. }
   6. }
   ```

   [DefineCallback.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DefineCallback.ets#L27-L32)
