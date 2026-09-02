---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-30
title: 如何获取UI组件的显示或隐藏状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何获取UI组件的显示或隐藏状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:864ef86f4b1ac5f6d48db3633bc5a8ddc4cfdf72ae304acdd8f8cf0c45bd2b9f
---

* 方法1：使用if条件渲染，通过变量控制组件的显隐。使用@Watch监听变量，可以判断组件的显示状态。
* 方法2：组件显示或隐藏时，生命周期方法 aboutToAppear() 和 aboutToDisappear() 会触发，可以感知组件的显示状态。

具体可参考示例代码：

```ts
@Component
struct ComponentA {
  aboutToAppear(): void {
    // Perception components are visible and hidden
    console.log('Component A display');
  }

  aboutToDisappear(): void {
    // Perception components are visible and hidden
    console.log('Component A hidden');
  }

  build() {
    Column() {
      Text('Component A').fontSize(16).fontColor(Color.Black);
    }
    .width(100)
    .height(50)
  }
}

@Entry
@Component
struct ComponentB {
  @State @Watch('onCompAShowStatusChange') isShowA: boolean = false;
  onCompAShowStatusChange() {
    // Perception components are visible and hidden
    console.log('Monitor component A：' + `${this.isShowA ? 'display' : 'hide'}`);
  }

  build() {
    Column() {
      Button('Switch between visible and hidden').type(ButtonType.Normal).width(100).height(50).onClick(() => {
        this.isShowA = !this.isShowA;
      })
      if (this.isShowA) {
        ComponentA();
      }
    }
  }
}
```

**参考链接**

[@Watch装饰器：状态变量更改通知](../harmonyos-guides/arkts-watch.md)、[if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)
