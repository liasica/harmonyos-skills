---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-667
title: Scroll嵌套RichEditor时滚动冲突问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Scroll嵌套RichEditor时滚动冲突问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:09+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:afca953a2bedd0e5e8602f026f1b20b2710b7dd2918b508574708b6b401cf573
---

## 问题现象

RichEditor设置固定高度，文本过多会出现滚动条，导致和父组件Scroll产生滚动冲突，导致不能滑动到最底部，怎么避免这种情况？

问题代码示例参考如下：

```ts
@Entry
@Component
struct Problem {
  controller: RichEditorController = new RichEditorController();
  scroller: Scroller = new Scroller();

  build() {
    Column() {
      Scroll(this.scroller) {
        RichEditor({ controller: this.controller })
          .borderWidth(1)
          .borderColor(Color.Gray)
          .height(120)
          .width(200);
      }
      .height(100)
      .scrollBar(BarState.On);
    }
    .height('100%')
    .width('100%');
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/QhbDHX8hTACk99J1JsX8RQ/zh-cn_image_0000002658913883.gif "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)为可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件。

## 解决方案

* **方案一**：设置父组件Scroll的高度大于等于子组件RichEditor的高度，此时只会出现子组件RichEditor的滚动条，RichEditor组件大小固定，否则只要子组件高度大于父组件高度，则父组件Scroll就会出现滚动条。

  ```ts
  @Entry
  @Component
  struct OptionOne {
    controller: RichEditorController = new RichEditorController();
    scroller: Scroller = new Scroller();

    build() {
      Column() {
        Scroll(this.scroller) {
          RichEditor({ controller: this.controller })
            .borderWidth(1)
            .borderColor(Color.Gray)
            .height(100)
            .width(200);
        }
        .height(100)
        .scrollBar(BarState.Off); // 关掉Scroll组件的滚动条
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/oI2GCl-vTduSjkHIFaGemw/zh-cn_image_0000002658793941.gif "点击放大")

* **方案二**：去掉子组件RichEditor的高度。此时RichEditor组件大小随着文本变化，超过父组件Scroll的高度后，只会出现父组件Scroll的滚动条，此时关掉Scroll组件的滚动条后就没有滚动条。

  ```ts
  @Entry
  @Component
  struct OptionTwo {
    controller: RichEditorController = new RichEditorController();
    scroller: Scroller = new Scroller();

    build() {
      Column() {
        Scroll(this.scroller) {
          RichEditor({ controller: this.controller })
            .borderWidth(1)
            .borderColor(Color.Gray)
            .width(200);
        }
        .height(100)
        .scrollBar(BarState.Off); // 关掉Scroll组件的滚动条
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/YnBJa1srR7q2Btqsr1VDIQ/zh-cn_image_0000002628394676.gif "点击放大")

* **方案三**：去掉父组件Scroll的高度，此时只会出现子组件RichEditor的滚动条，RichEditor组件大小固定。

  ```ts
  @Entry
  @Component
  struct OptionThree {
    controller: RichEditorController = new RichEditorController();
    scroller: Scroller = new Scroller();

    build() {
      Column() {
        Scroll(this.scroller) {
          RichEditor({ controller: this.controller })
            .borderWidth(1)
            .borderColor(Color.Gray)
            .height(100)
            .width(200);
        }
        .scrollBar(BarState.Off); // 关掉Scroll组件的滚动条
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/U98gHPE1SK6sH3HJ0xGR5w/zh-cn_image_0000002628554562.gif "点击放大")

## 总结

上述三种解决方案都通过关掉Scroll组件的滚动条实现，这样不仅可以规避滚动冲突问题，还可以确定是哪个组件在进行滚动，方案一与方案三都是RichEditor在进行滚动，出现了RichEditor组件的滚动条，而方案二是Scroll组件进行滚动，此时可以对滚动条进行隐藏，由于RichEditor目前没有去掉滚动条的属性或者方法，所以方案二可以作为RichEditor组件去掉滚动条的问题的替代方案。

## 常见FAQ

Q：可以通过滚动组件通用接口[nestedScroll](../harmonyos-references/ts-container-scrollable-common.md#nestedscroll11)来处理嵌套滚动模式，实现与父组件的滚动联动吗？

A：此场景下不可以，因为此时的子组件为RichEditor，而滚动组件通用属性和事件目前只支持List、Grid、Scroll和WaterFlow组件。
