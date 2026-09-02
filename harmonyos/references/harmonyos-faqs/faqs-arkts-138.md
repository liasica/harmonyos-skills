---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-138
title: ArkTS如何定义callback函数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS如何定义callback函数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:82994214e569a3e2fbbb9b580d91e2277a89c863b1f70e81421a471ee779291b
---

定义一个callback函数的样例，参考代码如下：

1. 定义回调函数

   ```ts
   // Define 2 parameters on the page, return empty callback function
   myCallback: (a: number,b: string) => void = () => {}
   ```
2. 在使用时进行初始化赋值

   ```ts
   aboutToAppear() {
     // Initialization of callback function
     this.myCallback = (a,b) => {
       console.info(`handle myCallback a=${a},b=${b}`)
     }
   }
   ```
