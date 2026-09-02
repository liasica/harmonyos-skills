---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1046
title: 如何实现Canvas画布移动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Canvas画布移动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:39116da6e6e54af81a6b35b390a55b976b276b951aaf1b3d2c7faf54b2340c51
---

## 问题现象

通过Canvas实现自定义的绘图效果，怎么移动Canvas画布？

## 背景知识

* Canvas提供绘制基本图形的能力，用于在屏幕上绘制图形和处理图形，参考：[画布的获取与绘制结果的显示（ArkTS）](../harmonyos-guides/canvas-get-result-draw-arkts.md)。
* [NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)：用于实现自定义节点的创建、显示、更新等操作的管理，并负责将自定义节点挂载到[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)上。

## 解决方案

Canvas画布平移操作通过translate(x, y)方法实现，将画布原点从默认的左上角(0,0)平移到新坐标(x, y)，绘制操作再基于新坐标执行。

1. 添加自定义RenderNode，重写自定义RenderNode的draw()函数，获取Canvas进行自定义的绘制操作，使用translate()接口实现画布平移。
2. 添加自定义NodeController，并将自定义NodeController进行显示。

完整示例参考如下：

```ts
import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

// 自定义RenderNode
export class MyRenderNode extends RenderNode {
  private currentX: number = 0;
  private currentY: number = 0;

  setOffset(x: number, y: number) {
    this.currentX = x;
    this.currentY = y;
    this.invalidate();
  }

  async draw(context: DrawContext) {
    // 创建画布canvas对象
    const canvas = context.canvas;

    // 使用translate()接口实现画布平移
    canvas.translate(this.currentX, this.currentY);

    // 自定义绘制相关操作
    const brush = new drawing.Brush();
    const pen = new drawing.Pen();
    pen.setColor({
      alpha: 255,
      red: 0,
      green: 0,
      blue: 255
    });
    pen.setStrokeWidth(2);
    brush.setColor({
      alpha: 255,
      red: 0,
      green: 0,
      blue: 255
    });
    canvas.attachBrush(brush);
    canvas.attachPen(pen);

    const font = new drawing.Font();
    font.setSize(100);
    const textBlob = drawing.TextBlob.makeFromString('Hello world', font);
    canvas.drawTextBlob(textBlob, 100, 720);
  }
}

// 自定义NodeController
export class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  myRenderNode = new MyRenderNode();

  updateOffset(x: number, y: number) {
    this.myRenderNode.setOffset(x, y);
  }

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      this.myRenderNode.backgroundColor = 0xffffffff;
      this.myRenderNode.frame = {
        x: 0,
        y: 0,
        width: 4800,
        height: 4800
      };
      this.myRenderNode.pivot = { x: 0.2, y: 0.8 };
      this.myRenderNode.scale = { x: 1, y: 1 };
      try {
        renderNode.appendChild(this.myRenderNode);
      } catch (error) {
        console.error(`appendChild error. Code is ${error.code}, message is ${error.message}.`);
      }
      renderNode.clipToFrame = false;
    }
    return this.rootNode;
  }
}

@Entry
@Component
struct RenderTest {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  private controller: MyNodeController = new MyNodeController();

  build() {
    Column() {
      Column() {
        // 将自定义NodeController进行显示
        NodeContainer(this.controller)
          .width('100%')
          .height('95%');
      };

      Row({ space: 5 }) {
        Button('向左')
          .onClick(() => {
            this.offsetX -= 100;
            this.controller.updateOffset(this.offsetX, this.offsetY);
          });
        Button('向右')
          .onClick(() => {
            this.offsetX += 100;
            this.controller.updateOffset(this.offsetX, this.offsetY);
          });
        Button('向上')
          .onClick(() => {
            this.offsetY -= 100;
            this.controller.updateOffset(this.offsetX, this.offsetY);
          });
        Button('向下')
          .onClick(() => {
            this.offsetY += 100;
            this.controller.updateOffset(this.offsetX, this.offsetY);
          });
        Button('复位')
          .onClick(() => {
            this.offsetX = 0;
            this.offsetY = 0;
            this.controller.updateOffset(this.offsetX, this.offsetY);
          });
      }
      .width('100%')
      .justifyContent(FlexAlign.Center) // 设置当前Row容器内子元素在主轴上居中对齐
      .alignItems(VerticalAlign.Center) // 设置当前Row容器内子元素在交叉轴（垂直方向）上的对齐方式为底部对齐
      .layoutWeight(1); // 设置当前Row在父容器Column中的布局权重为1
    };
  }
}
```

运行效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/-jKghDTiThSoEPp2By7hKA/zh-cn_image_0000002628405550.png "点击放大")
