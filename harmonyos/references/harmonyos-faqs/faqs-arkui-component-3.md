---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-component-3
title: 嵌套Tabs时渐变导航无法穿透标题栏的解决方法
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 嵌套Tabs时渐变导航无法穿透标题栏的解决方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:0ee9b29c8435cf459f6bd729cf919a623a721ff3322f6d8fc5170069d3b92f07
---

## 问题现象

在HarmonyOS应用开发中，当使用渐变导航并嵌套Tabs组件时，列表上滑后列表项无法穿透标题栏区域显示，导致渐变导航的穿透效果失效。

## 背景知识

在HarmonyOS应用开发中，渐变导航通常通过设置ScrollEffectType.GRADIENT\_BLUR实现列表项滚动时穿透标题栏的视觉效果。Tabs组件常用于实现视图切换，其包含的TabContent组件用于展示具体内容。默认情况下，组件的clip属性为true，会对超出自身边界范围的子组件进行裁剪。更多参考请参见[Tabs组件](../harmonyos-guides/ui-js-building-ui-layout-external-container.md#tabs组件)和[滚动组件通用属性](../harmonyos-guides/har-package.md#导出arkui组件)。

## 问题定位

在实现渐变导航穿透效果时，若在导航容器内嵌套了Tabs及TabContent组件，当内部List组件上滑时，ListItem虽然已经进入标题栏区域，但并未穿透标题栏显示出来。排查发现，由于Tabs和TabContent组件默认开启了clip裁剪功能，超出的内容被直接裁剪掉，导致渐变导航的穿透效果无法正常生效。

## 分析结论

核心原因：Tabs和TabContent组件的clip属性默认会对超出当前组件范围外的子组件区域进行裁剪。

技术原理解析：渐变导航的穿透效果依赖于子组件能够超出父容器边界进行渲染。当嵌套Tabs时，Tabs和TabContent的默认裁剪行为阻止了内部List内容延伸至标题栏区域，从而表现为渐变导航不工作。

## 修改建议

为Tabs和TabContent组件设置clip(false)，关闭超出区域的裁剪功能。

```ts
import { HdsNavigation, HdsNavigationTitleMode, ScrollEffectType, TitleBarStyleOptions } from '@hms.hds.hdsBaseComponent';

@Entry
@Component
struct Index {
  @State index: number = 0

  build() {
    HdsNavigation() {
      Tabs({ index: this.index }) {
        TabContent() {
          FollowListView()
        }
        .clip(false)
        .tabBar(this.TabBuilder(0, '关注'))
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP])

        TabContent() {
          FollowListView()
        }
        .tabBar(this.TabBuilder(1, '粉丝'))
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP])
      }
      .clip(false)
      .tabsStyle()
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP])
    }
    .titleMode(HdsNavigationTitleMode.MINI)
    .titleBar({
      enableComponentSafeArea: true,
      content: {
        title: {
          mainTitle: 'Home'
        }
      },
      style: NavDestinationStyle()
    })
  }

  @Builder
  TabBuilder(index: number, name: string) {
  }
}

@Component
struct FollowListView {
  build() {
    List({ space: 24 }) {
      ForEach([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], (item: number) => {
        ListItem() {
          Text(item + "")
            .padding(16)
            .backgroundColor(Color.Brown)
            .width('100%')
        }
        .height(64)
      }, (item: number) => item + '')
    }
    .width('100%')
    .height('100%')
    .clip(false)
    .cachedCount(3, true)
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP])
  }
}

export function NavDestinationStyle(): TitleBarStyleOptions {
  return {
    scrollEffectOpts: {
      enableScrollEffect: true,
      scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
    },
    scrollEffectStyle: {
      backgroundStyle: {
        backgroundColor: $r('sys.color.ohos_id_color_background_transparent')
      }
    }
  }
}

@Extend(Tabs)
function tabsStyle() {
  .width('100%')
  .height('100%')
  .barHeight(0)
  .barWidth('100%')
  .barOverlap(true)
  .animationDuration(250)
  .barBackgroundBlurStyle(BlurStyle.Regular)
}
```
