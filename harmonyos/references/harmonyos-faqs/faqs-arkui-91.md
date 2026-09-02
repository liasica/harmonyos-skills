---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-91
title: 如何实现文本竖向排列
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现文本竖向排列
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6af79115a64a97697d38e3f8f993845acc1b97e54e2ffe9b932e6b6dd3d9b75f
---

可以通过设置Text组件宽度width与字号一致的方式实现。参考代码如下：

```typescript
@Entry
@Component
struct Index {
  private message: string = 'This document is suitable for beginners in application development. By building a simple application with page jump/return function, quickly understand the main files of the project directory and familiarize yourself with the application development process.';
  build() {
    Column() {
      Text(this.message)
        .fontSize(13)
        .width(13)
    }
  }
}
```
