---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-672
title: 如何解决软键盘弹出后顶部控件无法固定的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决软键盘弹出后顶部控件无法固定的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:06755bedf55f0d26c12ce25c2df0902c8d5e272fcba2a4eb5006639c3d2f1ed3
---

## 问题现象

页面分为三个部分，顶部固定标题，中间是列表，底部是输入框。用户点击底部输入框时，页面弹出软键盘，顶部固定标题没有固定住，固定标题随着列表往上移动。

问题现象预览：左侧图是没弹出软键盘的场景，右侧图是弹出软键盘的场景。

| 没弹出软键盘的场景 | 弹出软键盘的场景 |
| --- | --- |
|  |  |

问题代码示例参考如下：

```screen
@Entry
@Component
struct Index {
  private list: string[] = [];
  private scroller = new Scroller();

  aboutToAppear(): void {
    for (let i = 0; i < 200; i++) {
      this.list.push(`选项${i}`);
    }
  }

  build() {
    Column() {
      Text('我是固定标题')
        .fontColor(Color.White)
        .backgroundColor('#0A59F7');
      List({ scroller: this.scroller, initialIndex: this.list.length - 1 }) {
        ForEach(this.list, (item: string) => {
          ListItem() {
            Text(item).padding(10);
          };
        });
      }.layoutWeight(1);

      TextInput().margin({ left: 16, right: 16, bottom: 16 });
    }.height('100%').width('100%');
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Ef3kYmV9SDK2RvttvELNKA/zh-cn_image_0000002628394680.png "点击放大")

## 背景知识

* 在移动设备上，由于输入法通常固定在屏幕下半段，应用可通过[setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)方法设置键盘抬起时页面的避让模式。
* [KeyboardAvoidMode](../harmonyos-references/arkts-apis-uicontext-e.md#keyboardavoidmode11)配置键盘避让页面的避让模式，其中KeyboardAvoidMode.RESIZE表示压缩模式。

## 问题定位

用户触发软键盘抬起后，顶部导航栏不固定需要从组件使用的正确性和软键盘的使用正确性方面进行检查。

1. 查看列表内容的滚动和文本输入框组件是否使用正确。
2. 查看键盘抬起后是否正确配置键盘避让模式。

## 分析结论

根据定位思路，进行如下操作：

1. 排查组件使用是否正确：首先需要排查组件是否使用正确。列表的实现需要使用[List](../harmonyos-references/ts-container-list.md)组件实现。列表的内容滚动需要使用[ListOptions](../harmonyos-references/ts-container-list.md#listoptions18对象说明)参数。文本输入框[TextInput](../harmonyos-guides/arkts-common-components-text-input.md)用于响应用户的输入操作。
2. 配置键盘避让模式：排查基础组件正确使用后，本示例未正确配置键盘避让模式，从而导致软键盘抬起后顶部控件无法固定。

## 修改建议

可以通过setKeyboardAvoidMode设置软键盘抬起时页面避让模式为压缩模式，并设置List组件的布局权重layoutWeight为1，在键盘抬起时List组件会被压缩，顶部文字不会向上移动。

```screen
import { KeyboardAvoidMode } from '@kit.ArkUI';

@Entry
@Component
struct KeyboardAvoidPage {
  private list: string[] = [];
  private scroller = new Scroller();

  aboutToAppear(): void {
    for (let i = 0; i < 200; i++) {
      this.list.push(`选项${i}`);
    }
    this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE); // 设置键盘避让模式
  }

  build() {
    Column() {
      Text('我是固定标题')
        .fontColor(Color.White)
        .backgroundColor('#0A59F7');
      List({ scroller: this.scroller, initialIndex: this.list.length - 1 }) {
        ForEach(this.list, (item: string) => {
          ListItem() {
            Text(item)
              .padding(16);
          };
        });
      }.layoutWeight(1);

      TextInput().margin({ left: 16, right: 16, bottom: 16 });
    }.height('100%').width('100%');
  }
}
```
