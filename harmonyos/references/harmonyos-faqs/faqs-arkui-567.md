---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-567
title: 如何解决Scroll组件嵌套Web组件滑动冲突问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Scroll组件嵌套Web组件滑动冲突问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d31e796f7b24e9e67cf636cf0552d7352c8e628c377c930968dda14ff5071362
---

## 问题现象

当Scroll组件嵌套Web组件滑动时，滑动冲突，如何处理？

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [ArkWeb](../harmonyos-guides/web-component-overview.md)：ArkWeb（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。
* [触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)可以设置不同的触摸测试响应模式，影响组件的触摸测试收集结果，最终影响后续的触屏事件分发。

## 解决方案

Web组件和Scroll组件在同一页面时，会存在Web获取焦点，导致Scroll无法上下滑动。

解决思路是可以通过设置边界调节来屏蔽其中一个的滑动响应来实现避免冲突的效果。

* **方案一**：屏蔽Web响应。

  可以在Scroll的onWillScroll事件中增加判断，在Scroll滑动到底部之前屏蔽所有Web响应，不过需要注意的是，如果Web本身也需要滑动的话，该方法不太适用，这种场景下可以使用方案二来处理冲突。

  ```screen
  .onWillScroll(() => {
    if (this.scroller.isAtEnd()) {
      this.webEnable = true;
      console.info(`webEnable: ${this.webEnable}`);
    } else {
      this.webEnable = false;
      console.info(`webEnable: ${this.webEnable}`);
    }
  });
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/XXyYpdT4Q4ebLDoe5b1Aeg/zh-cn_image_0000002658911361.png "点击放大")
* **方案二**：触摸事件传递。

  可以使用触摸测试控制来规避此种情况，请给显示在上层的节点设置hitTestBehavior为HitTestMode.Transparent。详情见[参考文档](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)。

  ```screen
  .hitTestBehavior(HitTestMode.Transparent); // 自身和子节点均响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2Sq-MCe2RNSWGVKI62BiOg/zh-cn_image_0000002628392144.png "点击放大")
* **方案三**：调整嵌套滚动模式。

  在嵌套滚动组件时，可以通过设置“nestedScroll”属性来控制滚动顺序。

  ```screen
  .nestedScroll({
    scrollForward: NestedScrollMode.PARENT_FIRST, // 向前滚动父容器优先
    scrollBackward: NestedScrollMode.SELF_FIRST // 向后滚动子组件优先
  });
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Vdr1_x9jSoeu1DbzDH5sgQ/zh-cn_image_0000002658791425.png "点击放大")

完整示例代码如下：

ArkTS页面代码：

```screen
import { webview } from '@kit.ArkWeb';

@Component
struct Solution1 {
  private scroller: Scroller = new Scroller();
  private webController: webview.WebviewController = new webview.WebviewController();
  @State webEnable: boolean = false;

  build() {
    Scroll(this.scroller) {
      Column({ space: 20 }) {
        Web({
          // 开发者需根据需求替换src
          src: $rawfile('ScrollWeb.html'),
          controller: this.webController
        })
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
          .fileAccess(true)
          .geolocationAccess(false)
          .width('100%')
          .height('100%')
          .enabled(this.webEnable);
        Row()
          .height(150);
      };
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .width('100%')
    .height('100%')
    .backgroundColor('#F1F3F5')
    .onWillScroll(() => {
      if (this.scroller.isAtEnd()) {
        this.webEnable = true;
        console.info(`webEnable: ${this.webEnable}`);
      } else {
        this.webEnable = false;
        console.info(`webEnable: ${this.webEnable}`);
      }
    });
  }
}

@Component
struct Solution2 {
  private scroller: Scroller = new Scroller();
  private webController: webview.WebviewController = new webview.WebviewController();

  build() {
    Scroll(this.scroller) {
      Column({ space: 20 }) {
        Web({
          // 开发者需根据需求替换src
          src: $rawfile('ScrollWeb.html'),
          controller: this.webController
        })
          .fileAccess(true)
          .geolocationAccess(false)
          .width('100%')
          .height('100%')
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
        Row()
          .height(150);
      };
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .backgroundColor('#F1F3F5')
    .hitTestBehavior(HitTestMode.Transparent); // 自身和子节点均响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。
  }
}

@Component
struct Solution3 {
  private scroller: Scroller = new Scroller();
  private webController: webview.WebviewController = new webview.WebviewController();

  build() {
    Scroll(this.scroller) {
      Column({ space: 20 }) {
        Web({
          // 开发者需根据需求替换src
          src: $rawfile('ScrollWeb.html'),
          controller: this.webController
        })
          .fileAccess(true)
          .geolocationAccess(false)
          .width('100%')
          .height('100%')
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
          .nestedScroll({
            scrollForward: NestedScrollMode.PARENT_FIRST, // 向前滚动父容器优先
            scrollBackward: NestedScrollMode.SELF_FIRST // 向后滚动子组件优先
          });
        Row()
          .height(150);
      };
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F1F3F5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}

@Entry
@Component
struct TabsExample {
  fontColor: string = '#182431';
  selectedFontColor: string = '#007DFF';
  @State currentIndex: number = 0;
  @State selectedIndex: number = 0;
  private controller: TabsController = new TabsController();

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 });
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.selectedIndex === index ? 1 : 0);
    }.width('100%');
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        TabContent() {
          Solution1().expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
        }
        .tabBar(this.tabBuilder(0, '方案1'))
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);

        TabContent() {
          Solution2().expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
        }
        .tabBar(this.tabBuilder(1, '方案2'))
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);

        TabContent() {
          Solution3().expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
        }
        .tabBar(this.tabBuilder(2, '方案3'))
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
      }
      //.vertical(false)
      //.barMode(BarMode.Fixed)
      .barWidth(360)
      .barHeight(56)
      .animationDuration(400)
      .onChange((index: number) => {
        // currentIndex控制TabContent显示页签
        this.currentIndex = index;
        this.selectedIndex = index;
      })
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        if (index === targetIndex) {
          return;
        }
        console.info(`event currentOffset ${event.currentOffset}`);
        // selectedIndex控制自定义TabBar内Image和Text颜色切换
        this.selectedIndex = targetIndex;
      })
      .width('100%')
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```

html页面代码：

```screen
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .lightgray {
          background-color: #D1D1D6;
        }
        .midgray {
          background-color: #C7C7CC;
        }
        .lightgray, .midgray {
         font-size:16px;
         height:200px;
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
        }
    </style>
</head>
<body>
<div class="lightgray" >webArea</div>
<div class="midgray">webArea</div>
<div class="lightgray">webArea</div>
<div class="midgray">webArea</div>
<div class="lightgray">webArea</div>
<div class="midgray">webArea</div>
<div class="lightgray">webArea</div>
</body>
</html>
```

## 总结

当两个可响应滑动的组件（如Web和Scroll）共存时，可能出现焦点抢占导致某一组件无法滑动的问题。

通过控制组件的交互响应优先级，避免冲突，主要有三类方案：

1. 动态启用/禁用组件响应：

   根据外部条件（如滚动位置）切换组件的交互状态，在需要某一组件响应时，禁用另一组件。

   例：Scroll未滑到底部时禁用Web的交互，滑到底部后再启用Web。
2. 控制触摸事件传递：

   通过设置组件的触摸测试行为（如hitTestBehavior），自身和子节点均响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。

   例：给Scroll设置hitTestBehavior属性为HitTestMode.Transparent，使自身和子节点均可响应。
3. 自定义滚动优先级：

   为嵌套的滚动组件配置滚动顺序规则（如nestedScroll），明确父/子组件的滚动优先级，按规则依次响应。

   例：向前滚动时父组件优先，向后滚动时子组件优先。
