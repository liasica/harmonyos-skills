---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-391
title: 如何实现弹窗动画和遮罩动画分开设置
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现弹窗动画和遮罩动画分开设置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ff283ee3e82eec7dced0f336d7d2c60c7359987988196be341ec4db37466d89c
---

**问题现象**

目前由于弹窗和遮罩是一起的，如果给弹窗增加由上往下的动画，遮罩也会同时执行相同的动画效果。

**解决措施**

可以单独给dialog里的自定义组件添加.transition属性设置该组件的出现方式，在消失前，通过让组件提前进入隐藏状态触发.transition动画，然后再关闭弹窗实现退场效果：

```typescript
import { ComponentContent } from '@kit.ArkUI';

export interface SimpleDialogParams {
  title: string
  desc: string
  visible?: Visibility
}

@Builder
function SimpleDialogBuilder(params: SimpleDialogParams) {
  SimpleDialogUI({ params })
}

@Component
struct SimpleDialogUI {
  @Prop params: SimpleDialogParams | null = null;
  @State yOffset: number | string = '100%';
  @Prop visible: Visibility = Visibility.Visible;

  build() {
    Column() {
      Text(this.params?.title)
        .fontSize(18)
        .fontWeight(FontWeight.Bold)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .margin({ bottom: 16 })
        .width('100%')
      Text(this.params?.desc)
        .fontSize(14)
        .lineHeight(22)
        .fontColor(Color.Gray)
        .margin({ bottom: 16 })
        .width('100%')
    }
    .borderRadius({ topLeft: 16, topRight: 16 })
    .backgroundColor(Color.White)
    .width('100%')
    .alignItems(HorizontalAlign.Start)
    .visibility(this.params?.visible)
    .padding(20)
    .transition(TransitionEffect.translate({ y: '100%' }).animation({ duration: 200 }))
  }
}

@Entry
@Component
struct SetDialogAnimationAndMaskAnimationSeparately {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          const param =
            { title: '标题标题标题', desc: '描述描述描述描述描述描述描述描述描述描述描述描述' } as SimpleDialogParams;
          const contentNode = new ComponentContent(this.getUIContext(), new WrappedBuilder(SimpleDialogBuilder), param);
          this.getUIContext().getPromptAction().openCustomDialog(contentNode, {
            autoCancel: true,
            maskColor: 'cc000000',
            maskRect: {
              x: 0,
              y: '-100%',
              width: '100%',
              height: '200%'
            },
            alignment: DialogAlignment.Bottom,
            transition: TransitionEffect.opacity(0).animation({ duration: 200 }),
            onWillDismiss: res => {
              contentNode.update({
                title: '标题标题标题',
                desc: '描述描述描述描述描述描述描述描述描述描述描述描述',
                visible: Visibility.Hidden
              });
              res.dismiss();
            }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
