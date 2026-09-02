---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1342
title: 列表上拉加载，始终显示加载提示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 列表上拉加载，始终显示加载提示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:07e8e1e7812de10c5a93d0b5b36cfc02f03e444a10804a6b36241bc79e510b9a
---

## 问题现象

列表页中列表尚未滚动至底部边缘，但页面底部一直提示上拉加载更多和加载完成的文字，没有隐藏。

## 背景知识

* [onScrollEdge](../harmonyos-references/ts-container-scroll.md#onscrolledge)：滚动到边缘事件回调，触发该事件的条件包括以下三种场景：滚动组件滚动到边缘时触发、支持键鼠操作等其他触发滚动的输入设置以及通过滚动控制器API接口调用、越界回弹。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：可以控制组件的显示或隐藏。
* [@State装饰器](../harmonyos-guides/arkts-state.md)：被@State装饰的变量称为状态变量，使普通变量具备状态属性。当状态变量改变时，会触发其直接绑定的UI组件渲染更新。

## 问题定位

排查加载提示组件及其父容器的visibility属性是否绑定变量，若未设置visibility属性，则未使用状态变量控制加载提示组件的显隐状态。

## 分析结论

未使用状态变量控制加载提示组件的显隐状态，导致加载提示组件一直显示。

## 修改建议

给Text的父组件设置visibility属性，通过修改绑定的状态变量来控制文字是否显示，可以在列表滚动至底部时显示文字，在加载列表数据完成后延时隐藏文字。示例代码如下：

```screen
@Entry
@Component
struct MessagePage {
  // 是否显示加载文字
  @State isLoading: boolean = true;
  // 提示加载的文字内容
  @State loadingText: string = '上拉加载更多';
  @State listData: string[] = ['列表测试1', '列表测试2', '列表测试3', '列表测试4', '列表测试5'];

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          ForEach(this.listData, (item: string) => {
            Column() {
              Text(item)
            }
            .justifyContent(FlexAlign.Center)
            .width('100%')
            .height('25%')
            .borderRadius(20)
            .backgroundColor('#f1f3f5')
          })
          Column() {
            // 加载提示
            Row() {
              LoadingProgress()
                .enableLoading(this.isLoading)
                .color('#0A59F7')
                .width(24)
              Text(this.loadingText)
            }
          }
          .visibility(this.isLoading ? Visibility.Visible : Visibility.None)
        }
      }
      .width('100%')
      .padding(10)
      .scrollBar(BarState.Off)
      .onScrollEdge((edge: Edge) => {
        if (edge === Edge.Bottom) {
          this.isLoading = true;
          this.loadData();
        }
      })
    }
    .height('100%')
  }

  // 加载更多数据
  loadData() {
    this.loadingText = '加载中';
    setTimeout(() => {
      // 延时添加数据，模拟网络请求获取数据
      for (let i = 0; i < 5; i++) {
        let length = this.listData.length;
        this.listData.push(`列表测试${length + 1}`);
      }
      // 加载完成后
      this.loadingText = '加载完成';
    }, 500);

    // 延时隐藏提示内容
    setTimeout(() => {
      this.isLoading = false;
    }, 1500);
  }
}
```
