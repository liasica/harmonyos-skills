---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1242
title: Navigation在分栏模式下页面有大量留白
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation在分栏模式下页面有大量留白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:21d83f6f775e117e219c431c5e195240f78246376355bb17130d416477741b86
---

## 问题现象

当用户在平板设备上或折叠屏展开态打开应用时，应用的页面呈现出左侧为导航栏，而右侧为大面积空白的现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/NWLfyhC-TquS_qdC0XzXDw/zh-cn_image_0000002658834707.png "点击放大")

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
* [mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)：Navigation组件的分栏模式由mode属性控制，包括单栏（Stack）、分栏（Split）和自适应（Auto）三个属性。该属性默认为Auto模式，在该模式下会自动监听屏幕属性，当为折叠屏或平板时，默认分栏显示，在折叠状态或普通手机时可为单栏显示。
* [splitPlaceholder](../harmonyos-references/ts-basic-components-navigation.md#splitplaceholder20)：Navigation双栏模式下，支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件。

## 问题定位

* 建议检查代码中是否使用splitPlaceholder设置分栏模式下，右侧默认占位页面。
* 建议检查代码中，是否在Navigation页面启动时，使用pushPath给右侧内容区域推送默认页面路由。

## 分析结论

应用在分栏模式下，未使用splitPlaceholder设置右侧默认占位页，也没有使用pushPath给右侧内容区域推送默认页面路由，导致刚进应用时，右侧显示空白。

## 修改建议

API20后推荐使用splitPlaceholder接口，可以使用splitPlaceholder设置右侧页面显示默认占位页。

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
