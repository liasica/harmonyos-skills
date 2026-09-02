---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-50
title: 如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8dc58e0e12446b0777f6234b3de89e6073fa74957c48d83fd2345e6bc4e9b56f
---

使用@Watch回调来监测状态变量的变化。如果回调函数执行，说明在下一次VSync信号发送时，使用该状态变量的UI会刷新绘制。

参考代码如下：

```ts
@Component
struct TotalView {
  @Prop @Watch('onCountUpdated') count: number = 0;
  @State total: number = 0;
  // @Watch callback
  onCountUpdated(propName: string): void {
    this.total += this.count;
  }

  build() {
    Text(`Total: ${this.total}`)
  }
}

@Entry
@Component
struct CountModifier {
  @State count: number = 0;

  build() {
    Column() {
      Button('add to basket')
        .onClick(() => {
          this.count++;
        })
      TotalView({ count: this.count })
    }
  }
}
```

**参考链接**

[watch和自定义组件更新](../harmonyos-guides/arkts-watch.md#watch和自定义组件更新)
