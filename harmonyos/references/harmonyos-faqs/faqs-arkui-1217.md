---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1217
title: List组件滑动时如何控制滑动幅度和滑动范围
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List组件滑动时如何控制滑动幅度和滑动范围
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6342e80b22eafab02aa63f46f222f7b6997afcc3e08905979f8bd39b5a03f72f
---

## 问题现象

List组件，如何控制滑动的幅度和范围。

## 背景知识

* [onScrollFrameBegin](../harmonyos-references/ts-container-list.md#onscrollframebegin9)：列表开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，列表将按照返回值的实际滑动量进行滑动。
* [onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)：有子组件划入或划出List显示区域时触发。计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。
* [onDidScroll](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)：滚动组件滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

## 解决方案

* onScrollFrameBegin的入参offset表示即将发生的滑动量，单位vp。返回参数offsetRemain表示实际滑动量。通过offset的大小来判断即将发生的滑动幅度是否超过预期值，通过控制返回的offsetRemain大小来限制实际的滑动量。

  核心代码如下：

  ```ts
  .onScrollFrameBegin((offset: number) => {
    if (offset > 1) {
      offset = 1;
    }
    if (offset < -1) {
      offset = -1;
    }
    return { offsetRemain: offset };
  })
  ```

  控制offsetRemain，滑动速度很缓慢，效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/qxNjTFdoR_GJvIPBQKDkPg/zh-cn_image_0000002658832837.png "点击放大")
* onScrollIndex的入参firstIndex超过预期值时，表示已经滑动出了预期范围，用this.scroller.scrollToIndex()把滑动强制拉回到预期值。

  核心代码如下：

  ```ts
  .onScrollIndex((firstIndex: number) => {
    if (firstIndex > 10) {
      this.scroller.scrollToIndex(10);
    }
  })
  ```

  下滑超过10之后继续滑动，会强制跳回10，效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/FoaBAMl8QzaSrdbr8TLkjg/zh-cn_image_0000002628593596.png "点击放大")

全量代码如下：

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct ScrollerPage {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
  scroller: Scroller = new Scroller();

  // 沉浸式窗口
  onPageShow(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      win.setWindowLayoutFullScreen(true);
    });
  }

  onPageHide(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      win.setWindowLayoutFullScreen(false);
    });
  }

  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scroller }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xDCDCDC);
          };
        }, (item: string) => item);
      }
      // 排列方向
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .friction(0.6)
      .edgeEffect(EdgeEffect.None)
      .onScrollFrameBegin((offset: number) => {
        if (offset > 1) {
          offset = 1;
        }
        if (offset < -1) {
          offset = -1;
        }
        return { offsetRemain: offset };
      })
      // 根据List显示组件的索引值判断是否滑动到顶部
      .onScrollIndex((firstIndex: number) => {
        if (firstIndex > 10) {
          this.scroller.scrollToIndex(10);
        }
      })
      .width('90%');
    }
    .width('100%')
    .height('100%');
  }
}
```
