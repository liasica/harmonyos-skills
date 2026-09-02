---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-split-line
title: 设置页签栏的分割线
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签栏的分割线
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c5895230f26741e42f46c5aab31077d0459c1160a2efa6580cd2ab98530367d1
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置页签栏的分割线。

[HdsTabs (底部页签)](../harmonyos-references/ui-design-hdstabs.md)容器组件扩展支持页签栏分割线常隐、常显和渐进显隐。当应用开发者需要分割线一直显示、一直隐藏或者内容区超过页签栏8vp后分割线完全消失时，可以通过设置HdsTabs组件的分割线的模式，同时也支持自定义分割线样式。

| 常显 | 常隐 | 跟手 |
| --- | --- | --- |
|  |  |  |

## 约束条件

1. 将页签栏置于容器的底部且支持模糊，即barPosition设置为BarPosition.End，vertical设置为false和barOverlap设置为true。
2. 分割线模式设置为跟手滑动模式时，跟手滑动效果仅限支持滚动的通用接口的组件，其他类型组件由开发者自己实现。
3. 跟手滑动效果依赖HdsTabs控制器绑定需要设置的list滑动控制器。

## 开发步骤

1. 导入相关模块。

   ```typescript
   // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   import { HdsTabs, HdsTabsController, DividerMode, HdsTabsAttribute } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置的Button可以切换分割线展示效果，分别是常显、常隐和跟手滑动效果。

   ```typescript
    @Entry
    @Component
    struct Index {
      private controller: HdsTabsController = new HdsTabsController();
      private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8];
      @State mode: DividerMode = DividerMode.FOLLOW_SCROLL;
      listScroller0: ListScroller = new ListScroller();
      listScroller1: ListScroller = new ListScroller();
    
      aboutToAppear(): void {
        this.controller.bindScroller(0, this.listScroller0);
        this.controller.bindScroller(1, this.listScroller1);
      }
    
      aboutToDisappear(): void {
        this.controller.unbindScroller(this.listScroller0);
        this.controller.unbindScroller(this.listScroller1);
      }
    
      build() {
        Column() {
          Column() {
            Row() {
              Text('Split Line:')
                .width('20%')
              Button('Visible')
                .onClick(() => {
                  this.mode = DividerMode.VISIBLE;
                })
              Button('None')
                .onClick(() => {
                  this.mode = DividerMode.NONE;
                })
              Button('Follow Scroll')
                .onClick(() => {
                  this.mode = DividerMode.FOLLOW_SCROLL;
                })
            }
          }
          .justifyContent(FlexAlign.Center)
          .width('100%')
          .height('10%')
    
          HdsTabs({ controller: this.controller }) {
            TabContent() {
              this.ContentBuilder(this.listScroller0)
            }
            .tabBar({ icon: $r('app.media.startIcon'), text: 'Tab 1' })
    
            TabContent() {
              this.ContentBuilder(this.listScroller1)
            }
            .tabBar({ icon: $r('app.media.startIcon'), text: 'Tab 2' })
          }
          .barOverlap(true)
          .barPosition(BarPosition.End)
          .vertical(false)
          .divider({
            mode: this.mode,
            style: {
              color: Color.Black,
              strokeWidth: 1,
              startMargin: 0,
              endMargin: 0
            }
          })
          .width('100%')
          .height('90%')
        }
      }
    
      @Builder
      ContentBuilder(listScroller: Scroller) {
        List({ scroller: listScroller }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text("item" + item)
                .height(96)
                .width('100%')
                .backgroundColor(item % 2 === 0 ? Color.Pink : Color.Yellow)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)
        }
        .width('100%')
        .height('100%')
      }
    }
   ```
