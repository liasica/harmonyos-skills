---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-531
title: 侧滑无法从首页退出应用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 侧滑无法从首页退出应用
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ddbaa9a3d4f4eeb779dcc9f1df9c701d553be70b0d3c6905d13a1088c58e656
---

## 问题现象

进入应用后，首页（进入应用的第一个页面）侧滑无法退出应用。

## 背景知识

[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：属于自定义组件的生命周期回调函数之一，当用户点击返回按钮或侧滑返回时触发，仅@Entry装饰的自定义组件生效。返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。

## 场景一：侧滑无法返回且onBackPress返回为true

### 问题定位

在日志中全局搜索关键字router user onBackPress return true、onBackPress called，如果出现onBackPress返回为true的类似日志，则说明用户重写了onBackPress的方法，相关日志内容如下：

```screen
[] HandleBackEvent(3205)	called
[(-1:100000:singleton)] [com.example.app][entry][100000] OnBackPressed called
[(100000:100000:scope)	router user onBackPress return true
[(100000:100000:scope)	router	consumed backpressed event
```

### 分析结论

侧滑无法返回且onBackPress返回为true。应用侧开发者重写了onBackPress方法且将返回值设置为true，但侧滑退出应用的代码逻辑错误，导致在首页使用侧滑手势退出时执行异常。

## 场景二：报错出现“禁止手势返回”或其他拦截提示信息

### 问题定位

如果故障位置应用日志报错出现了其他如“禁止手势返回”等拦截提示信息，则为设置了侧滑返回拦截。这是代码逻辑问题，误对侧滑返回操作进行拦截。

```screen
I[] HandleBackEvent(3943): cautea 
I[(-1:100000:singleton)] [com.example.app][entry][100000]: OnBackPressed called
I[(-2:100000:singleton)] Fail to find subwindow in subwindowMap_, instanceId is 100000.
I[(100000:100000:scope)]	router user onBackPress return true
I[(100000:100000:scope)]	router consumed backpressed event
I[CONSOLE:1021]"禁止手势返回", source: https://链接地址 (1021)
```

### 分析结论

报错出现“禁止手势返回”或其他拦截提示信息。开发者设置了侧滑手势的返回拦截。

## 修改建议

### 场景一

删除onBackPress方法处修改的代码逻辑，或return false即可。

### 场景二

排查对应代码逻辑，解除首页退出限制。以下是两种设置侧滑手势的返回拦截方式。

* 方案一：使用了UIContext.getPromptAction().onWillDismiss拦截返回操作。通过PromptAction提供的onWillDismiss回调，在弹窗即将关闭时进行拦截，当关闭原因是侧滑手势时，不执行关闭弹窗。
* 方案二：使用了Navigation自定义弹窗+onBackPressed拦截返回。通过NavDestination的onBackPressed回调，实现返回和关闭命令前的逻辑判断，拦截了侧滑手势返回操作，即当侧滑手势发生时不执行返回和退出命令。

```screen
import { PromptAction } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 获取当前UI上下文
  private uiContext: UIContext = this.getUIContext();
  // 弹窗实例
  private promptAction: PromptAction = this.uiContext.getPromptAction();
  // 保存弹窗ID
  private dialogId: number = 0;

  // 弹窗构建器
  @Builder
  buildDialogContent() {
    Column() {
      Row() {
        Text('提示')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
      .height(56)
      .justifyContent(FlexAlign.Center)

      Text('您确定要关闭吗？')
        .fontSize(14)

      Button('确认')
        .fontSize(16)
        .fontColor('#0A59F7')
        .backgroundColor(Color.White)
        .onClick(() => {
          this.promptAction.closeCustomDialog(this.dialogId);
        })
        .width('100%')
        .margin({ top: 8, bottom: 16 })
    }
  }

  build() {
    NavDestination() {
      Column() {
        Row() {
          Button('打开弹窗')
            .fontSize(16)
            .width('100%')
            .borderRadius(20)
            .margin({ bottom: 16 })
            .backgroundColor('#0A59F7')
            .onClick(() => {
              this.promptAction.openCustomDialog({
                builder: () => this.buildDialogContent(),
                alignment: DialogAlignment.Center,
                maskColor: 'rgba(0, 0, 0, 0.2)',
                // 根据关闭原因决定是否关闭弹窗
                onWillDismiss: (reason: DismissDialogAction) => {
                  hilog.info(0xFF00, 'DialogCloseReason', `关闭原因: ${reason.reason}`);
                  if (reason.reason === DismissReason.PRESS_BACK || reason.reason === DismissReason.SLIDE) {
                    // 阻止关闭
                    return false;
                  }
                  return true;
                }
              }).then((id: number) => {
                this.dialogId = id;
              });
            })
        }
        .width('100%')
        .alignItems(VerticalAlign.Center)
      }
      .width('100%')
      .height('100%')
      .padding({ left: 16, right: 16 })
      .justifyContent(FlexAlign.End)
    }
  }
}

@Component
export struct Index1 {
  // 页面栈
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Stack({ alignContent: Alignment.Center }) {
          Column() {
            Row() {
              Text('提示')
                .fontSize(20)
                .fontWeight(FontWeight.Bold)
            }
            .width('100%')
            .height(56)
            .justifyContent(FlexAlign.Center)

            Text('您确定要关闭吗？')
              .fontSize(14)

            Button('确认')
              .fontSize(16)
              .fontColor('#0A59F7')
              .backgroundColor(Color.White)
              .onClick(() => {
                this.pageInfos.pop();
              })
              .width('100%')
              .margin({ top: 8, bottom: 16 })
          }
          .padding({ left: 24, right: 24 })
          .justifyContent(FlexAlign.Center)
          .alignItems(HorizontalAlign.Center)
          .backgroundColor(Color.White)
          .borderRadius(32)
          .margin({ left: 16, right: 16 })
        }
        .height('100%')
        .width('100%')

        // 设置弹窗样式
        .backgroundColor('rgba(0, 0, 0, 0.2)')
      }
    }
    .hideTitleBar(true)
    .mode(NavDestinationMode.DIALOG)
    .onBackPressed(() => {
      // 重写返回逻辑，自定义返回规则
      // todo
      // 返回为true后触发重写的返回逻辑
      return true;
    })
  }
}
```
