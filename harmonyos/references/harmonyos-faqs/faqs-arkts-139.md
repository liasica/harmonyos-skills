---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-139
title: 对象中函数的this如何指向外层
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 对象中函数的this如何指向外层
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:71c0f80f92fff1d748e330875d2f496d7c84893ef9d8bdf193c33ce6f099ac4c
---

通过箭头函数实现。参考代码如下：

```ts
interface T {
  start: () => number
}
@Component
struct PointingOuterLayer {
  @State num: number = 1
  obj: T = {
    start: () => {
      return this.num
    }
  }
```
