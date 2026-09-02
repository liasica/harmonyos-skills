---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-723
title: 如何解决Refresh每次下拉重复触发刷新回调的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Refresh每次下拉重复触发刷新回调的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:39b7fb502b4ee218f7cbf17c8989b87be7149a7c2a666b0b7397d4c2fea56413
---

## 问题现象

Refresh组件在反复滑动时，会重复触发刷新回调，无法控制刷新状态，问题图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ZO4IywDySHKkBqI7zIEROw/zh-cn_image_0000002658914537.png "点击放大")

由图可见，Refresh的刷新不断重复触发，如何解决Refresh每次下拉重复触发刷新回调的问题？

## 背景知识

[Refresh](../harmonyos-references/ts-container-refresh.md)是可以进行页面下拉操作并显示刷新动效的容器组件，其[onRefreshing](../harmonyos-references/ts-container-refresh.md#onrefreshing)回调会在进入刷新状态时触发。

## 解决方案

通过给onRefreshing刷新回调增加限制条件来限制其触发频率，具体实现如下：

1. 使用@State装饰器定义多个状态变量，如arr、refreshing、refreshOffset等。

   ```ts
   @State arr: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
   @State refreshing: boolean = false;
   @State refreshOffset: number = 0;
   @State refreshState: RefreshStatus = RefreshStatus.Inactive;
   @State canLoad: boolean = false;
   @State isLoading: boolean = false;
   @State isRefresh: boolean = true;
   ```
2. 在onScrollFrameBegin回调中，监听用户下拉操作，当下拉距离超过阈值且没有正在加载时，设置canLoad为true，允许加载更多数据。

   ```ts
   .onScrollFrameBegin((offset: number) => {
     if (offset > 5 && !this.isLoading) {
       this.canLoad = true;
     }
     return { offsetRemain: offset };
   })
   ```
3. 在onRefreshing回调中，处理刷新状态的逻辑，当触发刷新时，设置refreshing为true，并在6秒后恢复为false。

   ```ts
   .onRefreshing(() => {
     if (this.refreshing) {
       this.isRefresh = false;
     }
     console.info(`SystemRefreshPage`, `refreshing:${this.refreshing}`);
     setTimeout(() => {
       this.refreshing = false;
       this.isRefresh = true;
     }, 6000);
   });
   ```

完整代码示例如下：

```ts
@Entry
@Component
struct RefreshRepeatProblem {
  @State arr: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  @State refreshing: boolean = false;
  @State refreshOffset: number = 0;
  @State refreshState: RefreshStatus = RefreshStatus.Inactive;
  @State canLoad: boolean = false;
  @State isLoading: boolean = false;
  @State isRefresh: boolean = true;

  build() {
    Refresh({ refreshing: $$this.refreshing }) {
      List() {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(80)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .backgroundColor('#F1F3F5')
              .borderRadius(15);
          }.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM]).margin({ top: 7, bottom: 7, left: 20 });
        }, (item: string) => item);
      }.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
      .width('92%')
      .margin({right:20})
      .onScrollIndex((end: number) => {
        if (this.canLoad && end >= this.arr.length - 1) {
          this.canLoad = false;
          this.isLoading = true;
          setTimeout(() => {
            for (let i = 0; i < 10; i++) {
              this.arr.push(this.arr.length);
              this.isLoading = false;
            }
          }, 6000);
        }
      })
      .onScrollFrameBegin((offset: number) => {
        if (offset > 5 && !this.isLoading) {
          this.canLoad = true;
        }
        return { offsetRemain: offset };
      })
      .scrollBar(BarState.Off)
      .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true });
    }.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    .width('100%')
    .height('100%')
    .backgroundColor('#ffffffff')
    .pullToRefresh(this.isRefresh)
    .onOffsetChange((offset: number) => {
      this.refreshOffset = offset;
    })
    .onStateChange((state: RefreshStatus) => {
      this.refreshState = state;
    })
    .onRefreshing(() => {
      if (this.refreshing) {
        this.isRefresh = false;
      }
      console.info(`SystemRefreshPage`, `refreshing:${this.refreshing}`);
      setTimeout(() => {
        this.refreshing = false;
        this.isRefresh = true;
      }, 6000);
    });
  }
}
```

修正效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/WDAAYU2HQJyl04-XJTp9Bg/zh-cn_image_0000002628395312.png "点击放大")

由图可见，Refresh组件的刷新状态不会在短时间内频繁触发。
