---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1403
title: 实现bindContextMenu弹出式菜单点击后保持开启
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现bindContextMenu弹出式菜单点击后保持开启
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:326ae9418589309c96871791d0a4f9b8a2eec4d0022aa648c1e5786f3df8e0a7
---

## 问题现象

使用[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)为组件绑定长按触发的弹出式菜单。

菜单采用自定义组件方式，存在一个【更多】按钮用于展现更多选项，但在点击按钮时菜单会自动关闭。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/7qKn4ffpQx2SiOg5RtYb2g/zh-cn_image_0000002628603238.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/yrUAxyPWTyqiwPgXqLx8sg/zh-cn_image_0000002658842503.gif "点击放大")

## 背景知识

* [bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)一般用于给组件绑定自定义菜单，触发方式为长按或者右键点击。
* 弹出菜单时，点击菜单或非菜单区域均会触发菜单关闭。
* 默认情况下父子组件之间触摸事件能够同时触发，[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)可以更改该默认配置，触摸测试控制类型：

| 触摸测试类型 | 描述 |
| --- | --- |
| Default | 自身及子节点响应触摸测试，但阻塞兄弟节点的触摸测试，不影响祖先节点的触摸测试。 |
| Block | 自身响应触摸测试，阻塞子节点和兄弟节点的触摸测试，同时阻塞祖先节点的触摸测试。 |
| Transparent | 自身和子节点都响应触摸测试，不会阻塞兄弟节点的触摸测试，不会影响祖先节点的触摸测试。 |
| None | 自身不响应触摸测试，不会阻塞子节点和兄弟节点的触摸测试，不会影响祖先节点的触摸测试。 |

## 解决方案

对于需要点击后保持菜单开启状态的组件例如【更多】按钮，可设置触摸测试控制为HitTestMode.Block。

用户点击该组件时将阻塞父组件即菜单获得该触摸事件，实现点击后菜单展开并且保持开启状态。

```ts
Button('更多')
  .onClick(() => {
    this.showMore = true;
  })
  .hitTestBehavior(HitTestMode.Block);
```

完整示例参考如下：

```ts
@Entry
@Component
struct bindContextMenuTest {
  build() {
    RelativeContainer() {
      Text('长按打开菜单')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .bindContextMenu(myMenuBuilder(), ResponseType.LongPress)
        .borderWidth(1);
    }
    .height('100%')
    .width('100%');
  }
}

@ComponentV2
struct MyMenu {
  @Local showMore: boolean = false;

  build() {
    Column() {
      Text('action 1');
      Text('action 2');
      Text('action 3');
      Button('更多')
        .onClick(() => {
          this.showMore = true;
        })
        .hitTestBehavior(HitTestMode.Block);
      if (this.showMore) {
        Text('action 4');
        Text('action 5');
        Text('action 6');
        Text('action 7');
      }
    }
    .width('100');
  }
}

@Builder
function myMenuBuilder() {
  MyMenu();
}
```
