---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-961
title: 自定义弹窗动态高度与滚动实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义弹窗动态高度与滚动实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3df3be3f2466634fb92873ddcb3182a5a49c9a064d141e6b8546cf5f37367c16
---

## 问题现象

当弹窗内容高度不确定时，需实现以下效果：

* 动态高度：弹窗高度根据内容自动调整。
* 最大高度限制：超过设定高度（如100vp）时，内容区域支持滚动。
* 滚动体验：内容超出后显示滚动条，确保用户可完整查看内容。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/XeWWOF6eSw6iwiVkW3YGKA/zh-cn_image_0000002628401674.png "点击放大")

## 背景知识

* [自定义弹窗（CustomDialog）](../harmonyos-references/ts-methods-custom-dialog-box.md)：通过[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)或[PromptAction](../harmonyos-references/js-apis-promptaction.md)控制弹窗，支持完全自定义UI布局。
* 滚动容器（[Scroll](../harmonyos-references/ts-container-scroll.md)）：Scroll组件提供垂直/水平滚动能力，结合[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)可限制最大尺寸。
* 约束布局：[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)方法动态控制组件尺寸，确保布局自适应。

## 解决方案

1. 弹窗外层包裹滚动容器。
   * 使用Scroll作为根容器，设置滚动方向为垂直（ScrollDirection.Vertical）。
   * 通过.scrollBar(BarState.On)启用滚动条，提升交互可视性。
2. 动态高度与最大高度限制。
   * 不固定高度：弹窗内部组件（如Column/Row）不设置固定高度。
   * 约束最大高度：用constraintSize限制Scroll组件的最大高度。
3. 滚动行为优化。

   禁用边缘效果：设置[edgeEffect](../harmonyos-references/ts-container-scroll.md#edgeeffect)属性的值为None避免滚动到边缘时有滑动效果。
4. 弹窗控制逻辑。
   * 通过PromptAction打开/关闭弹窗，绑定自定义组件ID实现精准控制。
   * 处理物理返回键/点击外部关闭：重写[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中的onWillDismiss方法拦截DismissReason.PRESS\_BACK和DismissReason.TOUCH\_OUTSIDE。

完整代码：

```ts
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct customDialogScroll {
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  private customDialogComponentId: number = 0; // 弹窗ID，用于关闭时定位
  scroller: Scroller = new Scroller(); // 滚动控制器

  // 自定义弹窗UI
  @Builder
  customDialogComponent() {
    Column() {
      Text('弹窗标题')
        .fontSize(30)
        .padding({ top: 10, bottom: 10 });
      Scroll(this.scroller) {
        Column() {
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
        }
        .padding({left:15,right:15})
        .backgroundColor('rgba(246, 244, 244, 1.00)')
        .width('100%'); // 模拟动态内容
      }
      .scrollable(ScrollDirection.Vertical) // 启用垂直滚动
      .scrollBar(BarState.On)
      .constraintSize({ maxHeight: 100 }) // ✅核心：限制最大高度
      .edgeEffect(EdgeEffect.None); // 禁用边缘效果
      Flex({direction:FlexDirection.Row,justifyContent:FlexAlign.SpaceEvenly,alignItems:ItemAlign.Center}){
        Button('取消')
          .fontColor('#0a59f7')
          .backgroundColor(Color.White)
          .backgroundColor('rgba(246, 244, 244, 1.00)')
          .onClick(() => this.closeDialog());
        Row()
          .width(1)
          .height(15)
          .backgroundColor(Color.Gray)
          .opacity(0.5)
        Button('确认')
          .fontColor('#0a59f7')
          .backgroundColor('rgba(246, 244, 244, 1.00)')
          .onClick(() => this.closeDialog());
      }

      .margin({ top: 8, bottom: 8 });
    }.backgroundColor('rgba(246, 244, 244, 1.00)');

  }

  // 关闭弹窗方法
  private closeDialog() {
    this.promptAction.closeCustomDialog(this.customDialogComponentId);
  }

  build() {
    Row() {
      Column() {
        Button('打开弹窗')
          .onClick(() => {
            this.promptAction.openCustomDialog({
              builder: () => this.customDialogComponent(), // 绑定UI构建器
              onWillDismiss: (action: DismissDialogAction) => {
                // 处理物理返回键/点击外部关闭
                if (action.reason === DismissReason.PRESS_BACK ||
                  action.reason === DismissReason.TOUCH_OUTSIDE) {
                  action.dismiss(); // 执行关闭
                }
              }
            }).then((dialogId: number) => {
              this.customDialogComponentId = dialogId; // 保存弹窗ID
            });
          });
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center);
    };
  }
}
```
