---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-233
title: 如何实现页面加载的loading效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现页面加载的loading效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:85c627142f3609c20d1c44b50e251718feb6e3502dcd5bc7664e339eb25f6ebb
---

使用Stack堆叠组件和LoadingProgress加载组件实现页面首次加载时的等待效果。参考代码如下：

```ts
@Entry
@Component
struct PageLoading {
  @State isLoading: boolean = true;

  aboutToAppear(): void {
    // Simulate network request operation, request data from the network 3 seconds later, notify the component, and change the list data
    setTimeout(() => {
      this.isLoading = false;
    }, 3000);
  }

  build() {
    Stack() {
      if (this.isLoading) {
        Column() {
          LoadingProgress()
            .color(Color.White)
            .width(80).height(80)
          Text('Effortlessly loading..')
            .fontSize(16)
            .fontColor(Color.White)
        }
        .width('100%')
        .height('100%')
        .backgroundColor('#40000000')
        .justifyContent(FlexAlign.Center)
      } else {
        Column(){
          Text('主页')
        }
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
  }
}
```
