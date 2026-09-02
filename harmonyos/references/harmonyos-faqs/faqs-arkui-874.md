---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-874
title: 下拉刷新列表，部分数据无变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 下拉刷新列表，部分数据无变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:62769aea014788da51820c37a8763455637add9234847c364e4dec6b8a093f23
---

## 问题现象

列表每次下拉刷新，只刷新了前两条内容，第三条内容无变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/IBfcJK8USmW7CX6yKILxtQ/zh-cn_image_0000002628398916.png "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [Refresh](../harmonyos-references/ts-container-refresh.md)可以进行页面下拉操作并显示刷新动效的容器组件。

## 问题定位

列表下拉刷新后，前两条成功刷新，则获取后端信息逻辑正确，需排查如下两点：

* 步骤一：前端刷新后获取信息逻辑是否正常获取所有所需信息。

  若使用Refresh组件，需要排查[onStateChange](../harmonyos-references/ts-container-refresh.md#onstatechange)和[onRefreshing](../harmonyos-references/ts-container-refresh.md#onrefreshing)的刷新回调，若使用自定义组件需排查自定义刷新回调，查看获取的数据是否正常。
* 步骤二：数据是否正常刷新到List的数据源。

  若数据获取正常，查看第三条数据内容是否有所变化，以及是否将数据刷入数据源，并进行更新。

数据更新错误示例代码：

代码遍历了获取到的数据源，但存在更新不完全，以及新数据过多，数组越界问题。

```typescript
.onRefreshing(() => {
  let listData: String[] = []
  // 模拟数据获取
  setTimeout(() =>{
    listData = ['1-1', '1-2']
  }, 1000)
  setTimeout(() => {
    this.isRefreshing = false;
    listData.forEach((data, index) => {
      this.arr[index] = data
    })
  }, 2000)
})
```

## 分析结论

* 步骤一中数据获取不正常：只获取了两条数据，获取数据时传参问题；第三条数据无变化，后端数据源第三条数据处理错误。
* 步骤二中数据刷新不正常：正确获取数据仅两条，未将页面上第三条数据删除；正确获取数据三条，未将第三条数据刷新。

## 修改建议

* 传参问题：正确传输所需参数，获取所有所需数据。
* 数据源问题：后端处理数据，确保数据正确。
* 数据有限：仅两条数据，确保数据更新后，删除原有的第三条数据。
* 数据未刷新：复用一二条刷新方法，刷新数据即可。

示例代码：

```typescript
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

  build() {
    Column() {
      Row({ space: 35 }) {
        Button('开始刷新').onClick(() => {
          this.isRefreshing = true;
        });
        Button('停止刷新').onClick(() => {
          this.isRefreshing = false;
        });
      }.padding({ top: 10, bottom: 20 });

      Refresh({ refreshing: $$this.isRefreshing }) {
        List({ space: 10 }) {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('100%')
                .height(80)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF);
            };
          }, (item: string) => item);
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .padding(16)
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off);
      }
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onOffsetChange((value: number) => {
        console.info('Refresh onOffsetChange offset:' + value);
      })
      .onRefreshing(() => {
        // 防止数据获取失败后页面无数据
        let listData: String[] = this.arr;
        // 模拟数据获取
        setTimeout(() => {
          listData = ['1-1', '1-2'];
        }, 1000);
        // 刷新
        setTimeout(() => {
          this.isRefreshing = false;
          this.arr = listData;
        }, 2000);
      })
      .backgroundColor('#F1F3F5')
      .padding({ bottom: 50 })
      .refreshOffset(64)
      .pullToRefresh(true);
    };
  }
}
```
