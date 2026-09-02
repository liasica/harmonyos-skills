---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-379
title: 如何模拟点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何模拟点击事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:91fc6a8cadeb70577d7df3c64f924156b6f0d13eb8a3c26299b1656dfcfb955d
---

模拟点击事件是指在程序中通过代码模拟触摸操作，模拟用户在界面上的点击行为，常用于自动化测试或绕过UI限制的场景。例如，使用onTouch触发按钮外区域的触摸事件，通过BuilderNode的方法传递touchEvent事件，从而实现模拟点击按钮的[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)手势点击事件。

```ts
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

class Params {
  text: string = 'this is a text';
}

@Builder
function ButtonBuilder(params: Params) {
  Column() {
    Button(`button ` + params.text)
      .backgroundColor(Color.Orange)
      .width('100%')
      .gesture(
        TapGesture()
          .onAction((event: GestureEvent) => {
            console.info('TapGesture');
          })
      )
  }
  .width('100%')
  .height(300)
  .padding({
    left: 16,
    right: 16
  })
  .justifyContent(FlexAlign.Center)
  .backgroundColor(Color.Gray)
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<[Params]> | null = null;
  private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, { text: 'this is a string' });
    return this.rootNode.getFrameNode();
  }

  // Coordinate Conversion Example
  postTouchEvent(event: TouchEvent, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    let node: FrameNode | null = this.rootNode.getFrameNode();
    if (node == null) {
      return false;
    }
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;
    let changedTouchLen = event.changedTouches.length;
    for (let i = 0; i < changedTouchLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        event.changedTouches[i].x = uiContext.vp2px(offsetX + event.changedTouches[i].x);
        event.changedTouches[i].y = uiContext.vp2px(offsetY + event.changedTouches[i].y);
      }
    }
    let result = this.rootNode.postTouchEvent(event);
    console.info('result:' + result);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.nodeController)
        .height(300)
        .width('100%')

      Column()
        .width(500)
        .height(300)
        .backgroundColor('#0A59F7')
        .onTouch((event) => {
          if (event != undefined) {
            let uiContext = this.getUIContext();
            // Dispatch event events to the FrameNode created by the nodeController by touching them with fingers
            this.nodeController.postTouchEvent(event, uiContext);
          }
        })
    }
  }
}
```
