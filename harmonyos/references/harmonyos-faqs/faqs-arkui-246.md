---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-246
title: 如何实现背景跟随文字大小改变
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现背景跟随文字大小改变
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:703778f24b62a63479ba36a42e0a6e7c8c32d49d3f25f0e5a7e553d3e13ec960
---

可以通过文字长度自动调整宽度。参考代码如下：

```typescript
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Row() {
        Text(this.message)
      }
      .backgroundImage($r('app.media.startIcon'))
      .backgroundImageSize({
        width: '100%',
        height: '100%'
      })
      .height(100)
      .border({
        width: 3,
        color: Color.Pink
      })

      TextInput()
        .onChange((value: string) => {
          this.message = value;
        })
    }
  }
}
```
