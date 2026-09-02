---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1468
title: OverlayManager实现页面顶部固定公告
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > OverlayManager实现页面顶部固定公告
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7e1b73280715216ef5dd44fe1c34122080b1601f1b0c2bd3f5ef62abd6c841e0
---

## 问题现象

在开发过程中，常需在当前组件上叠加显示遮罩文本或自定义内容（如提示标签、水印、操作浮层等）。虽然Stack组件可通过层级嵌套实现此类效果，但过度使用嵌套结构会导致组件树层级过深，增加渲染开销，影响页面性能。

相比之下，使用[浮层（OverlayManager）](../harmonyos-guides/arkts-create-overlaymanager.md)可在不增加组件层级的前提下，将浮层内容直接挂载至目标组件之上，有效减少一层Stack节点的嵌套。该方案在实现视觉效果的同时，显著优化了渲染性能与结构简洁性。

## 背景知识

[浮层（OverlayManager）](../harmonyos-guides/arkts-create-overlaymanager.md)用于在页面（Page）之上展示自定义的UI内容，位于[Dialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#tipsdialog)、[Popup](../harmonyos-references/ohos-arkui-advanced-popup.md)、[Menu](../harmonyos-references/ts-basic-components-menu.md)、[BindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)、[BindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)和[Toast](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opentoast18)等组件之下，展示范围为当前窗口的安全区内，适用于常驻悬浮等场景。

可以通过使用UIContext中的[getOverlayManager](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getoverlaymanager12)方法获取当前UI上下文关联的[OverlayManager](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md)对象，再通过该对象调用对应方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Jm8HERZsRoCvADBtKzei4Q/zh-cn_image_0000002658964567.png "点击放大")

## 解决方案

使用OverlayManager传入[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md#componentcontent-1)添加浮层实现在页面顶部固定公告，示例代码如下：

1. 自定义Params类，实现公告效果时text与offset为必需。

   ```ts
   export class Params {
     text: string = '';
     offset: Position;
     overlayContent: ComponentContent<Params>[];
     overlayNode: OverlayManager;

     constructor(text: string, overlayContent: ComponentContent<Params>[],
       overlayNode: OverlayManager, offset: Position) {
       this.text = text;
       this.offset = offset;
       this.overlayContent = overlayContent;
       this.overlayNode = overlayNode;
     }
   }
   ```
2. 自定义公告组件，此处可自定义固定公告样式，以及设置点击后跳转至详情页并隐藏ComponentContent。

   ```ts
   @Builder
   export function OverlayNode(params: Params) {
     Row({ space: 5 }) {
       Text(params.text)
         .fontWeight(400)
         .lineHeight(16)
         .fontSize(14)
         .maxLines(1)
         .textOverflow({ overflow: TextOverflow.Ellipsis })
         .layoutWeight(1);
       Text('查看详情')
         .fontSize(12)
         .fontColor('#0A59F7');
       Text('>')
         .fontSize(12)
         .fontColor('#0A59F7');
     }
     .alignItems(VerticalAlign.Center)
     .justifyContent(FlexAlign.SpaceBetween)
     .onClick(() => {
       let componentContent = params.overlayContent[0];
       params.overlayNode.hideComponentContent(componentContent);
     })
     .position({
       x: params.offset.x,
       y: params.offset.y
     })
     .expandSafeArea([SafeAreaType.KEYBOARD])
     .width('100%')
     .padding({
       top: 16,
       bottom: 16,
       left: 16,
       right: 16
     })
     .backgroundColor('#f1f3f5')
     .hitTestBehavior(HitTestMode.Transparent); // 配置浮层不阻塞交互
   }
   ```
3. 在aboutToAppear()中初始化ComponentContent，并添加浮层节点。

   ```ts
   aboutToAppear(): void {
     let componentContent = new ComponentContent(
       this.uiContext, wrapBuilder<[Params]>(OverlayNode), this.params
     );
     this.overlayNode.addComponentContent(componentContent, 0);
     this.overlayContent.push(componentContent);
   }
   ```
4. 在aboutToDisappear()中销毁ComponentContent。

   ```ts
   aboutToDisappear(): void {
     let componentContent = this.overlayContent.pop();
     this.overlayNode.removeComponentContent(componentContent);
   }
   ```

完整示例参考如下：

```ts
import { ComponentContent, OverlayManager } from '@kit.ArkUI';

export class Params {
  text: string = '';
  offset: Position;
  overlayContent: ComponentContent<Params>[];
  overlayNode: OverlayManager;

  constructor(text: string, overlayContent: ComponentContent<Params>[],
    overlayNode: OverlayManager, offset: Position) {
    this.text = text;
    this.offset = offset;
    this.overlayContent = overlayContent;
    this.overlayNode = overlayNode;
  }
}

@Builder
export function OverlayNode(params: Params) {
  Row({ space: 5 }) {
    Text(params.text)
      .fontWeight(400)
      .lineHeight(16)
      .fontSize(14)
      .maxLines(1)
      .textOverflow({ overflow: TextOverflow.Ellipsis })
      .layoutWeight(1);
    Text('查看详情')
      .fontSize(12)
      .fontColor('#0A59F7');
    Text('>')
      .fontSize(12)
      .fontColor('#0A59F7');
  }
  .alignItems(VerticalAlign.Center)
  .justifyContent(FlexAlign.SpaceBetween)
  .onClick(() => {
    let componentContent = params.overlayContent[0];
    params.overlayNode.hideComponentContent(componentContent);
  })
  .position({
    x: params.offset.x,
    y: params.offset.y
  })
  .expandSafeArea([SafeAreaType.KEYBOARD])
  .width('100%')
  .padding({
    top: 16,
    bottom: 16,
    left: 16,
    right: 16
  })
  .backgroundColor('#f1f3f5')
  .hitTestBehavior(HitTestMode.Transparent); // 配置浮层不阻塞交互
}
@Entry
@Component
struct MainPage {
  text: string = '下周一下午15:00开例会，主要过一下本周的项目进度和接下来的项目安排。';
  componentOffset: Position = { x: 0, y: 1 };
  private uiContext: UIContext = this.getUIContext();
  private overlayNode: OverlayManager = this.uiContext.getOverlayManager();
  private overlayContent: ComponentContent<Params>[] = [];
  @Provide params: Params =
    new Params(this.text, this.overlayContent, this.overlayNode, this.componentOffset);
  aboutToAppear(): void {
    let componentContent = new ComponentContent(
      this.uiContext, wrapBuilder<[Params]>(OverlayNode), this.params
    );
    this.overlayNode.addComponentContent(componentContent, 0);
    this.overlayContent.push(componentContent);
  }
  aboutToDisappear(): void {
    let componentContent = this.overlayContent.pop();
    this.overlayNode.removeComponentContent(componentContent);
  }
  build() {
    Column() {
    }
    .backgroundColor('#ffffff');
  }
}
```

## 总结

想要实现固定公告、悬浮层可以使用overlay属性。使用OverlayManager实现文本浮层比[Stack](../harmonyos-references/ts-container-stack.md#子组件)组件嵌套方式少了一层Stack节点。使用[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)设置浮层时，浮层中的内容会在页面刷新时销毁并重新创建，存在一定的性能损耗，页面频繁刷新的场景推荐使用ComponentContent方式设置浮层。
