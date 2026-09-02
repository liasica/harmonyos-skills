---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1595
title: Tabs切换时进行弹窗拦截
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Tabs切换时进行弹窗拦截
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:79fce1d45d7a24baf5fd4021e7f90f42ba7026262a8082d7321678d7043732c2
---

## 问题现象

在Tabs将要切换时，如何弹出弹窗拦截此次切换，并当在弹窗中执行一些指令后，关闭弹窗，并决定完成或取消此次切换。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/uo5Z3dF6QPajAEXNSgKFBQ/zh-cn_image_0000002658969529.png "点击放大")

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)组件通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。可以使用[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)控制Tabs组件进行页签切换。
* Tab页签点击后触发[onTabBarClick](../harmonyos-references/ts-container-tabs.md#ontabbarclick10)事件，入参为被点击的index索引。

## 解决方案

点击Tabs自带的页签会触发onTabBarClick回调，页面也会立即切换，即使在此回调中设置弹窗也无法达到预期效果。

可以自定义标签栏，在标签栏的点击回调中通过使用[changeIndex](../harmonyos-references/ts-container-tabs.md#changeindex)方法控制跳转。具体示例如下：

```screen
@Entry
@Component
struct TabsDialogDemo {
  private controller: TabsController = new TabsController();
  @State currentIndex: number = 0;
  @State selectIndex: number = -1;
  lastIndex: number = 0;
  private customDialogComponentId: number = 0;
  tabArray: Array<string> = ['部门', '用户'];

  @Builder
  customDialogComponent() {
    Column({ space: 12 }) {
      Text('弹窗').fontSize(24);
      Text('是否跳转').margin({ top: 16, bottom: 16 });
      Row() {
        Button('取消', { buttonStyle: ButtonStyleMode.TEXTUAL }).width('40%').onClick(() => {
          // 关闭自定义对话框
          this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          // 设置当前索引为上一次索引，不进行跳转操作
          this.currentIndex = this.lastIndex;
        });
        Divider().vertical(true).height('20');
        Button('跳转', { buttonStyle: ButtonStyleMode.TEXTUAL }).width('40%').onClick(() => {
          // 关闭自定义对话框
          this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          // 设置当前索引和上次索引
          this.lastIndex = this.currentIndex = this.selectIndex;
          // 调用控制器改变索引
          this.controller.changeIndex(this.currentIndex);
        });
      }.width('80%')
      .justifyContent(FlexAlign.SpaceBetween);
    }.padding(24).justifyContent(FlexAlign.SpaceBetween);
  }

  @Builder
  tabBar(tabName: string, tabIndex: number) {
    Row({ space: 20 }) {
      Text(tabName).fontSize(18)
        .textAlign(TextAlign.Center)
        .width('100')
        .fontColor(tabIndex === this.currentIndex ? '#0A59F7' : Color.Black);
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .width('100')
    .height(60)
    .onClick(() => {
      // 如果当前索引等于标签索引，则不执行任何操作
      if (this.currentIndex === tabIndex) {
        return;
      }
      // 设置上一次索引为当前索引
      this.currentIndex = this.lastIndex;
      // 设置选择的索引为新标签索引
      this.selectIndex = tabIndex;
      // 打开自定义对话框
      this.getUIContext().getPromptAction().openCustomDialog({
        builder: () => {
          this.customDialogComponent();
        },
        width: 328
      }).then((dialogId: number) => {
        this.customDialogComponentId = dialogId;
      });
    });
  }

  build() {
    Column() {
      // 自定义标签栏
      Row() {
        Scroll() {
          Row() {
            ForEach(this.tabArray, (item: string, index: number) => {
              this.tabBar(item, index);
            });
          }.justifyContent(FlexAlign.Center);
        }
        .align(Alignment.Center)
        .scrollable(ScrollDirection.Horizontal)
        .scrollBar(BarState.Off)
        .width('100%');
      }.alignItems(VerticalAlign.Center)
      .width('100%');

      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        TabContent() {
          Text('部门');
        };

        TabContent() {
          Text('用户');
        };
      }
      .vertical(false)
      .barWidth('100%')
      .scrollable(false);
    }
    .height('100%')
    .width('100%');
  }
}
```
