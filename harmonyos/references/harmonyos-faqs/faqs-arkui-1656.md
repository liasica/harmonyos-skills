---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1656
title: 进入直播间时弹幕列表自动显示最新内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 进入直播间时弹幕列表自动显示最新内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:da7343eddcf43b76a534e72dc3fbf54ac392d8ab55e899f72680b400e7e245d1
---

## 问题现象

用户进入直播间后，竖向弹幕列表的默认焦点将置于消息流最底端，确保首先展示最新的弹幕内容。

## 背景知识

* 组件生命周期函数[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)的触发时机是在build函数之前，此时组件未开始渲染；组件挂载显示后触发[onAppear回调](../harmonyos-references/ts-universal-events-show-hide.md#onappear)，该回调可能发生在组件布局渲染后。
* [scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)滚动到容器边缘，不区分滚动轴方向。

## 解决方案

aboutToAppear生命周期于build前触发，适用于数据初始化；而onAppear在组件渲染并挂载显示后执行。为实现弹幕列表初始化后直接显示底部内容，可在List组件的onAppear回调中，通过Scroller控制器的scrollEdge(Edge.Bottom)方法实现自动滚动。

示例代码如下：

```ts
@Entry
@Component
struct BulletScreen {
  @State list: number[] = [];
  scroller: Scroller = new Scroller();

  aboutToAppear(): void {
    // 加载弹幕
    let list: number[] = [];
    for (let i = 0; i < 10; i++) {
      list.push(i);
    }
    this.list = list;
  }

  build() {
    Column() {
      // 弹幕数据加载完毕再初始化List组件
      if (this.list.length > 0) {
        List({ scroller: this.scroller }) {
          ForEach(this.list, (item: number) => {
            ListItem() {
              Text(`我是弹幕${item + 1}`)
                .fontSize(20);
            }
            .width('100%')
            .height(120)
            .borderRadius(30)
            .margin({ top: 16 })
            .backgroundColor('rgba(242, 243, 245, 1)');
          });
        }
        // 在组件挂载显示的onAppear回调中，执行滚动竖直方向下边缘。
        .onAppear(() => {
          this.scroller.scrollEdge(Edge.Bottom);
        })
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
      }
    }
    .width('100%')
    .height('100%')
    .padding({ left: 16, right: 16 })
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```

## 常见FAQ

Q：在自定义组件的生命周期函数aboutToAppear()上，如果给生命周期函数加上async关键字修饰，里面的代码会变成异步执行吗？

A：[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)方法，加上async关键字后不会阻塞组件的build()函数执行，里面的代码也会异步执行，但不能保证调用的时序。
