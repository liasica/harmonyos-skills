---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1052
title: HitTestMode的不同应用场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > HitTestMode的不同应用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7b77c3e3272ad0e15b31de8690d89fc5477f1fbc30dcfa0471969590c1503ae3
---

## 问题现象

hitTestBehavior属性通过HitTestMode的不同枚举值设置不同的触摸测试响应模式，影响触摸测试收集结果及后续事件分发。如何根据实际应用场景合理使用HitTestMode，以确保触摸事件能够准确、预期地被响应和分发？

| 场景 | 场景说明 |
| --- | --- |
| 场景一：控制onTouch事件的传递 | 触摸测试响应直接影响到onTouch事件能否在父子和兄弟组件间的透传，Z轴上存在重叠效果的组件通常需要根据实际需求来设置不同的HitTestMode。 |
| 场景二：控制触摸行为的传递 | HitTestMode控制的是触摸行为的传递，因此它不仅影响onTouch事件的触发，也影响由触摸行为产生的一系列交互结果，例如滚动组件能否被滑动，长按、拖拽等手势能否被识别等。 |
| 场景三：触摸发生后再决定HitTestMode | 需要在触摸发生后再根据触摸点信息动态修改HitTestMode的值。例如，实现一个组件内部特定区域可以透传，剩余区域不能透传；实现一个组件处于上半屏时可以透传，处于下半屏时不能透传。 |

## 背景知识

* [触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)：在ArkUI开发框架中，处理触屏事件和鼠标事件时，会在事件触发前进行按压点与组件响应热区的触摸测试，以收集需响应事件的组件。基于测试结果，框架会分发相应的事件。hitTestBehavior设置组件的触摸测试类型。如果组件不设置hitTestBehavior，其默认触摸测试类型为HitTestMode.Default。
* [事件响应链](../harmonyos-guides/arkts-interaction-basic-principles.md#事件响应链)：ArkUI事件响应链通过触摸测试进行收集，遵循右子树（按组件布局的先后层级）优先的后序遍历。
* [HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9)：定义触摸测试的响应逻辑及节点阻塞规则。
* [onTouchIntercept](../harmonyos-references/ts-universal-attributes-on-touch-intercept.md)：为组件提供自定义的事件拦截能力，开发者可根据事件在控件上按下时的位置，输入源等事件信息决定控件上的HitTestMode属性。

## 解决方案

* **场景一**：一个含有子组件的全屏蒙层，希望点击蒙层内的组件时事件不穿透，点击蒙层空白区域时事件穿透。

  实现思路：给全屏蒙层设置hitTestBehavior(HitTestMode.None)使点击时事件可以传递蒙层下方组件，同时给蒙层的子组件设置hitTestBehavior(HitTestMode.BLOCK\_HIERARCHY)阻止事件传递到蒙层下方组件。

  ```ts
  @Entry
  @Component
  struct BlockHierarchy {
    build() {
      Stack() {
        Column()
        .onTouch(() => {
          console.info('蒙层下方组件被点击');
        })
        .height('100%')
        .width('100%');

        Column() {
          Button('蒙层内按钮')
            .hitTestBehavior(HitTestMode.BLOCK_HIERARCHY)
            .onTouch(() => {
              console.info('蒙层内子组件被点击');
            });
        }
        .justifyContent(FlexAlign.Center)
        .hitTestBehavior(HitTestMode.None)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .backgroundColor('rgba(0, 0, 0, 0.3)')
        .height('100%')
        .width('100%');
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .height('100%')
      .width('100%');
    }
  }
  ```
* **场景二**：Scroll中存在一个子组件，希望触摸该子组件时不会滑动Scroll，触摸其余区域时可以滑动Scroll。

  实现思路：给该子组件设置hitTestBehavior(HitTestMode.Block)，阻塞其父组件Scroll的触摸测试。

  ```ts
  @Entry
  @Component
  struct Block {
    build() {
      Scroll() {
        Column({ space: 16 }) {
          Column()
            .height(400)
            .width('100%')
          Column()
            .height(56)
            .width('100%')
            .backgroundColor('#F1F3F5')
            .hitTestBehavior(HitTestMode.Block)
          Column()
            .height(400)
            .width('100%')
        };
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/P3byQJ3OQXK_pxUBBCyCnQ/zh-cn_image_0000002628565458.png "点击放大")
* **场景三**：一个容器组件（灰色矩形包裹区域），希望点击内部的深灰色矩形区域时，手势不会透传到TextArea上；点击空白区域时，手势会透传到TextArea上。

  实现思路：如果希望只有点击空白区域才透传，可以在onTouchIntercept方法中判断触摸位置是否处于深灰色矩形区域内，如果是，则修改HitTestMode为Default，不进行透传。否则修改HitTestMode为Transparent，进行透传。

  ```ts
  import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

  class Params {
    columnX: number = 0;
    columnY: number = 0;
    columnWidth: number = 0;
    columnHeight: number = 0;
  }

  @Builder
  function buttonBuilder(params: Params) {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {
      Column()
        .onAreaChange((oldValue: Area, newValue: Area) => {
          console.info(`oldValue:${oldValue}`);
          params.columnX = Number(newValue.globalPosition.x);
          params.columnY = Number(newValue.globalPosition.y);
          params.columnWidth = Number(newValue.width);
          params.columnHeight = Number(newValue.height);
        })
        .height(50)
        .width(100)
        .hitTestBehavior(HitTestMode.Block)
        .borderRadius(8)
        .backgroundColor('#C7C7CC');
    }
    .backgroundColor('#E5E5EA')
    .height(100)
    .width(200);
  }

  class MyNodeController extends NodeController {
    private rootNode: BuilderNode<[Params]> | null = null;
    private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);
    params: Params = new Params();

    makeNode(uiContext: UIContext): FrameNode | null {
      if (this.rootNode === null) {
        this.rootNode = new BuilderNode(uiContext);
        this.rootNode.build(this.wrapBuilder, this.params);
      }
      return this.rootNode.getFrameNode();
    }
  }

  @Entry
  @Component
  struct HitTestModeDemo {
    private baseNode: MyNodeController = new MyNodeController();

    isPolygon(event: TouchEvent) {
      console.info(`${event}`);
      return true;
    }

    build() {
      Stack() {
        Column() {
          TextArea({ placeholder: 'input your word...' })
            .width(200)
            .height(200)
            .backgroundColor('#F1F3F5');
        };

        NodeContainer(this.baseNode)
          .onTouchIntercept((event: TouchEvent) => {
            // 判断触摸点是否在深灰色矩形Column中
            if (this.isPolygon(event) && 0 <= (Number(event.touches[0].displayX) - this.baseNode.params.columnX) &&
              (Number(event.touches[0].displayX) - this.baseNode.params.columnX) <=
              this.baseNode.params.columnWidth &&
              0 <= (Number(event.touches[0].displayY) - this.baseNode.params.columnY) &&
              (Number(event.touches[0].displayY) - this.baseNode.params.columnY) <=
              this.baseNode.params.columnHeight) {
              return HitTestMode.Default;
            }
            return HitTestMode.Transparent;
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/uIo9XqCOSPChdglRojkygg/zh-cn_image_0000002658924767.png "点击放大")
