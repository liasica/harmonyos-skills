---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1297
title: 如何让每个Tab页签的数据只请求一次
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何让每个Tab页签的数据只请求一次
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:546d3f870fb63ac80b50b0e7bf6f0a1b8338ac13d8879bb6c6804e9866ce7606
---

## 问题现象

当前实现逻辑：进入页面时自动请求第一个页签的数据，每当该页签显示时都会触发数据请求。现在需要实现当该页签第二次及之后显示时，避免重新发起数据请求。请问应如何实现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/0u4kIgSpQoSsZfJpDw91aw/zh-cn_image_0000002658837247.gif "点击放大")

## 背景知识

TabContent在切换过程中会触发[onSelected](../harmonyos-references/ts-container-tabs.md#onselected18)回调，返回当前显示的页签索引。点击、滑动页签操作、修改状态变量等操作均会触发该回调。

## 解决方案

通过创建状态变量tabContentArr记录该页签是否已被显示过，来判断TabContent页签的数据是否需要再次请求。

```screen
@Entry
@ComponentV2
struct TabContentLoading {
  // 记录页签是否显示过，true已显示，false未显示，默认显示第一个页签
  @Local tabContentArr: boolean[] = [true, false, false, false];
  tabContents: string[] = ['首页', '推荐', '发现', '我的'];

  build() {
    Row() {
      Column() {
        Tabs({ barPosition: BarPosition.Start }) {
          ForEach(this.tabContents, (item: string, index) => {
            TabContent() {
              if (this.tabContentArr[index]) {
                TabChild({ textName: index })
              } else {
                LoadingProgress().width(50)
              }
            }.tabBar(item)
          }, (item: string) => `${item}`)
        }
        .onSelected((index) => {
          if (this.tabContentArr[index]) {
            return;
          }
          // 模拟请求
          setTimeout(() => {
            this.tabContentArr[index] = true; // 显示过设置为true
          }, 500);
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}

@ComponentV2
struct TabChild {
  @Require @Param textName: number;

  build() {
    Column() {
      Text(this.textName + '')
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```
