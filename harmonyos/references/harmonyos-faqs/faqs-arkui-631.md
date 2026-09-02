---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-631
title: RichEditor组件设置禁止编辑
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor组件设置禁止编辑
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d8ddf6baee6b2de489b17dc6bd82622961f8207091d51b1c91583e2cf5743f6b
---

## 问题现象

如何实现RichEditor组件禁止编辑态？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/3fNtKn6_TYGEpI1eOsILBw/zh-cn_image_0000002658913491.png "点击放大")

## 背景知识

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件。[customKeyboard](../harmonyos-references/ts-basic-components-richeditor.md#customkeyboard)属性可设置自定义键盘。

## 解决方案

* **方案一**：

  RichEditor没有禁止文本编辑的属性，可使用customKeyboard属性绑定一个空白的自定义键盘来代替系统键盘，实现禁止编辑的功能。

  ```ts
  @Entry
  @Component
  struct RichEditorDemo {
    controller: RichEditorController = new RichEditorController();

    @Builder
    TestBoard() {
    }

    build() {
      Column() {
        RichEditor({ controller: this.controller })
          .onReady(() => {
            this.controller.addTextSpan('测试文字测试文字测试文字测试文字测试文字测试文字');
          })
          .customKeyboard(this.TestBoard())
          .width('100%')
          .border({ width: 1, radius: 5 })
          .key('RichEditor')
          .caretColor(Color.Transparent)
          .margin({ top: 50 })
      }
      .width('100%')
    }
  }
  ```
* **方案二**：设置属性hitTestBehavior(HitTestMode.None)，RichEditor组件不响应点击事件。

## 常见FAQ

Q：RichEditor菜单怎么禁止剪切和粘贴？

A：可以通过修改editMenuOptions属性绑定的菜单，去除剪切和粘贴选项。

```ts
@Entry
@Component
struct Faq {
  controller: RichEditorController = new RichEditorController();
  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .editMenuOptions({
          onCreateMenu: (menuItems: Array<TextMenuItem>) => {
            let menus = menuItems.filter((item: TextMenuItem) => {
              return !item.id.equals(TextMenuItemId.PASTE) && !item.id.equals(TextMenuItemId.of('OH_DEFAULT_PASTE'))
                && !item.id.equals(TextMenuItemId.CUT) && !item.id.equals(TextMenuItemId.of('OH_DEFAULT_CUT'));
            });
            return menus;
          },
          onMenuItemClick: (menuItem: TextMenuItem) => {
            if (menuItem.id.equals(TextMenuItemId.PASTE) || menuItem.id.equals(TextMenuItemId.of('OH_DEFAULT_PASTE')) ||
            menuItem.id.equals(TextMenuItemId.CUT) || menuItem.id.equals(TextMenuItemId.of('OH_DEFAULT_CUT'))) {
              return true;
            };
            return false;
          }
        })
        .width('100%')
        .border({ width: 1, radius: 5 })
        .key('RichEditor')
        .caretColor(Color.Transparent)
        .margin({ top: 50 })
    }
    .width('100%')
  }
}
```
