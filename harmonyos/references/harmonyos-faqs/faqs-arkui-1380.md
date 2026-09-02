---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1380
title: 如何实现Refresh组件下滑动展开和收起List某个ListItem的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Refresh组件下滑动展开和收起List某个ListItem的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dc594025629fce81f0d15db6a74d2a8593974932dc3e144f7517ee2ef11f8c8a
---

## 问题现象

如何实现在Refresh组件下，通过滑动操作展开和收起List组件的第一个ListItem，实现下拉刷新的效果。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/bBdO_zFhSf6RMuiBqXVSZA/zh-cn_image_0000002628762558.png "点击放大")

## 背景知识

[Refresh组件](../harmonyos-references/ts-container-refresh.md)可以通过下拉一定距离，实现页面的刷新，下拉的响应灵敏度可以通过[pullDownRatio属性](../harmonyos-references/ts-container-refresh.md#pulldownratio12)调整；而滑动[List组件](../harmonyos-references/ts-container-list.md)，会在组件滚动前触发[onWillScroll事件回调](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)，执行回调操作。

## 解决方案

在onWillScroll事件回调中判断当前List组件滚动的偏移量和移动状态，当满足预定条件时，修改第一个ListItem的高度，实现ListItem的展开和收起；同时为了避免手势冲突，当此ListItem未展开时，设置Refresh的pullDownRatio属性参数为0，即不跟随手势下拉。

示例代码如下：

```typescript
@Entry
@Component
struct ScalingComponent {
  @State isRefreshing: boolean = false;
  @State itemList: string[] = [];
  @State isExpand: boolean = false;
  private minHeight = 30;
  private maxHeight = 200;
  private scroller: ListScroller = new ListScroller();
  aboutToAppear(): void {
    for (let i = 1; i < 11; i++) {
      this.itemList.push(`Item Text ${i}`);
    };
  };

  build() {
    Refresh({ refreshing: $$this.isRefreshing }) {
      List({ space: 5, scroller: this.scroller }) {
        // 可展开收起的ListItem
        ListItem() {
          Text('Scaling component');
        }
        .height(this.isExpand ? this.maxHeight : this.minHeight) // 通过状态变量的变化改变组件高度
        .width('100%')
        .align(Alignment.Top);

        ForEach(this.itemList, (item: string) => {
          ListItem() {
            Text(item)
              .fontColor('#000');
          }
          .height(100)
          .width('100%')
          .borderRadius(16)
          .backgroundColor('#f1f3f5');
        });
      } .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])

      .padding({left:16,right:16})
      .height('100%')
      .width('100%')
      .onWillScroll((offset, state, source) => {
        // 当List处于开始边缘时，手势向下拉，回调结果为偏移量offset=0，滚动状态state=1，此时展开ListItem；其他情况收起ListItem
        console.info(`source: ${source}`);
        if (offset === 0 && state === 1) {
          this.isExpand = true;
        } else {
          this.isExpand = false;
        };
      });
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    .height('100%')
    .width('100%')

    // 当ListItem未展开时，Refresh组件不随手势下拉
    .pullDownRatio(this.isExpand ? undefined : 0)
    .onRefreshing(() => {
      setTimeout(() => {
        this.isRefreshing = false;
      }, 2000);
    });
  };
};
```
