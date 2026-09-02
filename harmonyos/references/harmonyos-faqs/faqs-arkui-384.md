---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-384
title: 如何解决组件消失动画偏移闪烁
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决组件消失动画偏移闪烁
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7747e1fb7ab91ae01419e7c1c054e15d56705ecbd56a2c7b73c8be18c18f81e4
---

**问题描述**

运行下面demo，点击使色块消失时，会突然出现在左上角闪烁。

```typescript
@Entry
@ComponentV2
struct Index {
  @Local isShow: boolean = true;

  build() {
    Stack() {
      Stack() {
        if (this.isShow) {
          Row()
            .width(100)
            .height(100)
            .backgroundColor(Color.Red)
            .transition(TransitionEffect.OPACITY.animation({ duration: 150 }));
        }
      }
      .backgroundColor(Color.Green)
    }
    .width('100%')
    .height('100%')
    .onClick(() => {
      this.isShow = !this.isShow;
    });
  }
}
```

**解决措施**

原因是当变量置为false时，组件会从视图树中移除，导致内层Stack失去内容后位置重置到左上角，可以固定内层Stack组件的宽高来避免，示例如下：

```typescript
@Entry
@ComponentV2
struct DisappearanceAnimationOffsetFlicker {
  @Local isShow: boolean = true;

  build() {
    Stack() {
      Stack() {
        if (this.isShow) {
          Row()
            .width(100)
            .height(100)
            .backgroundColor(Color.Red)
            .transition(TransitionEffect.OPACITY.animation({ duration: 150 }))
        }
      }
      .width('100%')
      .height('100%')
      .onClick(() => {
        this.isShow = !this.isShow
      })
    }
  }
}
```
