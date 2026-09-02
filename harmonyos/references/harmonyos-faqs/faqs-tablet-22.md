---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-22
title: 平板开启强制横屏选择分栏视图，应用横屏后分栏显示异常
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板开启强制横屏选择分栏视图，应用横屏后分栏显示异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f7ffc664519b72dd88d6f5395cf66fc9820f7e9446d5df888b2307cc16e16720
---

## 问题现象

平板开启强制横屏选择分栏视图，应用内页面分栏显示异常。

## 背景知识

* 系统针对平板设备提供了[应用兼容性调试](../best-practices/bpta-pad-guide.md#section11600844887)功能，能够调试应用横屏适配问题。
* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)的[mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性可用来设置导航栏的显示模式，支持单栏（Stack）、分栏（Split）和自适应（Auto）。
* [splitPlaceholder](../harmonyos-references/ts-basic-components-navigation.md#splitplaceholder20)：Navigation双栏模式下，支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件，该属性从API version 20开始支持。

## 问题定位

使用UIView查看页面组件布局，发现当前页面未采用Navigation组件实现路由控制。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/JoxIaeATT9-zjONqmCNVQA/zh-cn_image_0000002658911555.png "点击放大")

## 分析结论

HarmonyOS系统分栏功能为Navigation组件的特性，该应用此处页面未采用Navigation组件做路由控制，故也未适配分栏模式，当使用系统强制横屏功能，打开分栏模式会导致页面显示异常。

## 修改建议

应用代码中采用Navigation组件做路由控制，实现页面间跳转，并根据业务需要合理设置Navigation组件的mode属性，如果需要分栏，该属性参数就配置成NavigationMode.Split，代码样例如下所示。

```screen
import { ComponentContent } from '@kit.ArkUI';

@Builder
function PlaceholderPage() {
  Column() {
    Text("分栏模式占位页")
      .fontSize(22)
      .fontWeight(500)
      .margin({ top: 200 });
  }.width("100%")
  .height("100%");
}

@Entry
@Component
struct NavigationExampleDemo {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  placeholder = new ComponentContent(this.getUIContext(), wrapBuilder(PlaceholderPage));

  @Builder
  NavigationTitle() {
    Column() {
      Text('Title')
        .fontColor('#182431')
        .fontSize(20)
        .lineHeight(30)
        .fontWeight(500);
      Text('subtitle')
        .fontColor('#182431')
        .fontSize(14)
        .lineHeight(19)
        .opacity(0.4)
        .margin({ top: 2, bottom: 20 });
    }.alignItems(HorizontalAlign.Start);
  }

  build() {
    Column() {
      Navigation() {
        TextInput({ placeholder: 'search...' })
          .width('90%')
          .height(40)
          .backgroundColor('#F1F3F5')
          .margin({ top: 8 });

        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('90%')
                .height(72)
                .backgroundColor('#F1F3F5')
                .borderRadius(24)
                .fontSize(16)
                .fontWeight(500)
                .textAlign(TextAlign.Center);
            };
          }, (item: number) => item.toString());
        }
        .height(324)
        .width('100%')
        .margin({ top: 12, left: '10%' });
      }
      .title(this.NavigationTitle)
      .titleMode(NavigationTitleMode.Full)
      .toolbarConfiguration([
        {
          // $r("app.media.startIcon")需要替换为开发者所需的图像资源文件
          value: '首页',
          icon: $r("app.media.startIcon")
        },
        {
          value: '菜单',
          icon: $r("app.media.startIcon")
        },
        {
          value: '我的',
          icon: $r("app.media.startIcon")
        }
      ], { backgroundColor: '#FFFFFF' })
      .mode(NavigationMode.Split)
      .hideTitleBar(false)
      .hideToolBar(false)
      .splitPlaceholder(this.placeholder);
    }.width('100%').height('100%');
  }
}
```
