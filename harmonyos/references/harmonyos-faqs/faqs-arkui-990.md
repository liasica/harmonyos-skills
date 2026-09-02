---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-990
title: openCustomDialog蒙层如何添加模糊效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > openCustomDialog蒙层如何添加模糊效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:77b3a3c8a7fa9e50f3081f22ee1a387a97a5b2479868aca6cf77d5ecadc6129f
---

## 问题现象

如何为自定义弹窗蒙层添加模糊效果，并且不影响点击蒙层关闭弹窗。

## 背景知识

* 推荐使用UIContext中获取到的PromptAction对象提供的[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口在相对应用复杂的场景来实现自定义弹出框，相较于[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)优势点在于页面解耦，支持[update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)动态刷新。
* [backdropBlur](../harmonyos-references/ts-universal-attributes-background.md#backdropblur)为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。

## 解决方案

自定义弹窗暂无内置属性支持设置蒙层背景模糊效果。给openCustomDialog蒙层添加模糊效果，可以在弹窗内容容器外包裹一层空column容器作为蒙层，设置backdropBlur属性，达到为蒙层添加模糊效果的目的，并通过监听onClick事件来关闭弹窗。为防止点击弹窗本身关闭弹窗，可以为弹窗内容容器设置空的onClick事件。

示例代码如下：该示例弹窗蒙层及弹窗开启关闭加了动画效果，仅供参考。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent, promptAction, UIContext, window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

export class PromptActionDialogClass {
  static context: UIContext;
  static contentNode: ComponentContent<Object>;
  static options: promptAction.BaseDialogOptions;

  static setContext(context: UIContext) {
    PromptActionDialogClass.context = context;
  }

  static setContentNode(node: ComponentContent<Object>) {
    PromptActionDialogClass.contentNode = node;
  }

  static setOptions(options: promptAction.BaseDialogOptions) {
    PromptActionDialogClass.options = options;
  }

  static openDialog() {
    if (PromptActionDialogClass.contentNode !== null) {
      PromptActionDialogClass.context.getPromptAction()
        .openCustomDialog(PromptActionDialogClass.contentNode, PromptActionDialogClass.options)
        .then(() => {
          console.info('OpenCustomDialog complete.');
        })
        .catch((error: BusinessError) => {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
        });
    }
  }

  static closeDialog() {
    if (PromptActionDialogClass.contentNode !== null) {
      PromptActionDialogClass.context.getPromptAction()
        .closeCustomDialog(PromptActionDialogClass.contentNode)
        .then(() => {
          console.info('CloseCustomDialog complete.');
        })
        .catch((error: BusinessError) => {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(`CloseCustomDialog args error code is ${code}, message is ${message}`);
        });
    }
  }

  static updateDialog(options: promptAction.BaseDialogOptions) {
    if (PromptActionDialogClass.contentNode !== null) {
      PromptActionDialogClass.context.getPromptAction()
        .updateCustomDialog(PromptActionDialogClass.contentNode, options)
        .then(() => {
          console.info('UpdateCustomDialog complete.');
        })
        .catch((error: BusinessError) => {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(`UpdateCustomDialog args error code is ${code}, message is ${message}`);
        });
    }
  }
}

class Params {
  topHeight: number;
  flag: boolean;

  constructor(topHeight: number, flag: boolean) {
    this.topHeight = topHeight;
    this.flag = flag;
  }
}

@Builder
function buildText(params: Params) {
  Stack() {
    if (params.flag) {
      // 蒙层
      Column()
        .width('100%')
        .height('100%')
        .backdropBlur(30)
        .borderRadius(15)
        .transition(TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Ease })) // 蒙层动画
        .onClick(() => {
          // 弹窗关闭的时候置为false标识弹窗即将关闭
          PromptActionDialogClass.contentNode.update(new Params(params.topHeight, false));
          // 延迟2s关闭动画
          setTimeout(() => {
            PromptActionDialogClass.closeDialog();
          }, 2000);
        });

      // 实际弹窗内容
      Column() {
        Text('这是自定义弹窗')
          .fontSize(30)
          .height(100);
        Button('点我关闭弹窗')
          .onClick(() => {
            PromptActionDialogClass.contentNode.update(new Params(params.topHeight, false));
            // 延迟2s关闭动画
            setTimeout(() => {
              PromptActionDialogClass.closeDialog();
            }, 2000);
          })
          .margin(20);
      }
      .padding(15)
      .backgroundColor(Color.Gray)
      .borderRadius(15)
      // 弹窗动画
      .transition(TransitionEffect.move(TransitionEdge.START).animation({ duration: 1000 }))
      // 加入空的点击事件弹窗就不会关闭
      .onClick(() => {
      });
    }
  }
  .width('100%')
  .height('100%')
  // 此处margin需要替换为顶部安全区高度topHeight，因蒙层会侵入安全区，所以做假蒙层也要侵入安全区
  .margin({ top: -params.topHeight })
  .padding({ top: params.topHeight });
}

@Entry
@Component
struct CustomDialogMaskPage {
  private ctx: UIContext = this.getUIContext();
  private windowClass: window.Window = (this.getUIContext().getHostContext() as common.UIAbilityContext)
    .windowStage.getMainWindowSync();
  private topHeight: number = this.ctx.px2vp(
    this.windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
  private contentNode: ComponentContent<Object> =
    new ComponentContent(this.ctx, wrapBuilder(buildText), new Params(this.topHeight, true));

  aboutToAppear(): void {
    PromptActionDialogClass.setContext(this.ctx);
    PromptActionDialogClass.setContentNode(this.contentNode);
    PromptActionDialogClass.setOptions({
      alignment: DialogAlignment.Top,
      offset: { dx: 0, dy: this.topHeight },
      isModal: false,
    });
  }

  build() {
    Row() {
      Column({ space: 30 }) {
        Button('open dialog and update options')
          .margin({ top: 50 })
          .onClick(() => {
            // 弹窗开启的时候设置为true标识弹窗打开
            this.contentNode.update(new Params(this.topHeight, true));
            PromptActionDialogClass.openDialog();
          });
      }
      .width('100%')
      .height('100%');
    }
    .height('100%');
  }
}
```
