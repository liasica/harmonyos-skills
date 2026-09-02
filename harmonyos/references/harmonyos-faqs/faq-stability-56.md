---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-56
title: 自定义弹框资源未释放导致稳定性测试出现内存泄漏
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 自定义弹框资源未释放导致稳定性测试出现内存泄漏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0c9f15799aaaa8d8f6f853b7a556c142205a4a75a0378f8f9a5e94a1b64909ef
---

## 问题现象

应用设置了全局防截屏，使用DevEco Testing跑稳定性会一直弹禁止截屏弹窗，最终导致内存泄漏。

## 背景知识

[setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)：设置窗口是否为隐私模式。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。设置窗口禁止截屏参考[如何实现防截屏功能](faqs-arkui-3.md)。

## 问题定位

进入应用任意页面，截屏操作会出现一个自定义的防截屏的蒙层和弹窗且不会自动消失，每次截屏操作都会出现蒙层和弹框，稳定性测试过程中需要截图来支撑用户分析定位问题，最终多个蒙层和弹窗一直同时显示。

## 分析结论

根据问题现象分析为弹窗资源没有释放，最终导致内存泄漏。

## 修改建议

1. 当前效果是既设置了HarmonyOS的隐私窗口防截屏，又设置了自定义弹窗提醒，建议参考[HarmonyOS防截屏的示例demo](faqs-arkui-3.md)，只使用HarmonyOS的隐私窗口防截屏。
2. 如果需要弹出自定义的防截屏弹窗，可以设置弹框自动消失时间。实现方案可参考如下示例，用户确认或取消操作后弹框消失，若设定时间内用户无确认或取消操作，到达设定时间后弹框也会自动消失。

```ts
import { ComponentContent, UIContext } from '@kit.ArkUI';

class Params {
  text: string = '';
  closeDialog?: () => void;
  secondsLeft: number = 0;

  constructor(text: string, closeDialog?: () => void, secondsLeft: number = 0) {
    this.text = text;
    this.closeDialog = closeDialog;
    this.secondsLeft = secondsLeft;
  }
}

@Builder
function buildDialog(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(20)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 10 })
    Text(`${params.secondsLeft}秒后自动确认`)
      .fontSize(16)
      .margin({ bottom: 20 })
    Row() {
      Button('确认')
        .onClick(() => {
          if (params.closeDialog) {
            params.closeDialog();
          }
        })
      Button('取消')
        .margin({ left: 20 })
        .onClick(() => {
          if (params.closeDialog) {
            params.closeDialog();
          }
        })
    }
  }.padding(20).backgroundColor('#FFF0F0F0')
}

@Entry
@Component
struct Index {
  private ctx: UIContext = this.getUIContext();
  private closeTimer: number | undefined = undefined;
  private countdownTimer: number | undefined = undefined;
  private secondsLeft: number = 3;
  private contentNode: ComponentContent<Object> | undefined = undefined;

  private closeDialog() {
    if (this.closeTimer !== undefined) {
      clearTimeout(this.closeTimer);
      this.closeTimer = undefined;
    }
    if (this.countdownTimer !== undefined) {
      clearInterval(this.countdownTimer);
      this.countdownTimer = undefined;
    }
    if (this.contentNode !== undefined) {
      this.ctx.getPromptAction().closeCustomDialog(this.contentNode)
        .then(() => {
          if (this.contentNode !== undefined) {
            this.contentNode.dispose();
          }
        });
    }
  }

  build() {
    RelativeContainer() {
      Button('点击弹出自定义弹框')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.secondsLeft = 3;
          this.contentNode = new ComponentContent(this.ctx, wrapBuilder(buildDialog),
            new Params('这是一个自定义弹框', this.closeDialog.bind(this), this.secondsLeft));
          this.ctx.getPromptAction().openCustomDialog(this.contentNode, { alignment: DialogAlignment.Center })
            .then(() => {
              this.countdownTimer = setInterval(() => {
                if (this.secondsLeft > 1) {
                  this.secondsLeft--;
                  // 只更新弹框参数，不重新弹框
                  if (this.contentNode) {
                    this.contentNode.update(new Params('这是一个自定义弹框', this.closeDialog.bind(this),
                      this.secondsLeft));
                  }
                } else {
                  this.closeDialog();
                }
              }, 1000);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 常见FAQ

Q：应用设置了全局防截屏，使用DevEco Testing跑稳定性时候会一直弹截屏弹窗，最终内存溢出，能否去掉DevEco Testing截图功能？

A：稳定性测试服务需要截图来支撑用户分析定位问题，无法去掉截图功能。建议应用开发测试阶段可以关闭防截屏策略使用DevEco Testing工具，上架阶段可以提交正式应用到AG进行测试。
