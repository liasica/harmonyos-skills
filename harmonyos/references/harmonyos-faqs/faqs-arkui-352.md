---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-352
title: 如何避免Badge在数量显示切换时的Image闪烁问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何避免Badge在数量显示切换时的Image闪烁问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:359dac23fc446c8c51f196b4a0eda7817acdf3e3e41fc5ef4b54c6f19e1885ac
---

通过@State装饰器修饰变量，动态设置badgeSize以控制Badge状态，当值设为0时Badge自动隐藏。

```ts
@Entry
@Component
struct BadgeDemo {
  @State message: string = 'Hello World';
  @State badgeSize: number = 15;

  build() {
    Row() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // change the Badge size
          this.badgeSize = this.badgeSize === 0 ? 15 : 0;
        })
      Badge({
        value: '1',
        position: {
          x: 40,
          y: 0
        },
        style: {
          badgeSize: this.badgeSize,
          badgeColor: Color.Red
        }
      }) {
        Image($r('app.media.startIcon'))
          .width(50)
          .height(50)
      }
    }
    .height('100%')
  }
}
```
