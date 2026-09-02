---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-95
title: ArkTS是否支持多继承
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持多继承
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0d3bf9f1b19d7de7261e4d669a99d2fdf55547b2de2ebabeb6692b0e203c9c22
---

接口支持多继承，类仅支持单继承。示例如下：

```ts
class TestClassA {
  address: string = '';
}

class TestClassB {
  name: string = '';
}

// report errors：Classes can only extend a single class.
// class TestClassC extends TestClassA, TestClassB {
// }

interface AreaSize {
  calculateAreaSize(): number;
}

interface Cal {
  Sub(a: number, b: number): number;
}

interface Area extends AreaSize, Cal {
  areaName: string;
  length: number;
  width: number;
}
```
