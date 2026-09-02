---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1619
title: 如何使用Canvas绘制树形组织结构
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使用Canvas绘制树形组织结构
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a1ccc3151adc4056110adf34dd2dfe93283486bab7f973d54b186af9f59f8e72
---

## 问题现象

如何使用Canvas绘制树形关系图或组织架构图？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：Canvas组件提供画布，用于自定义绘制图形。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)：使用CanvasRenderingContext2D在Canvas画布组件上进行绘制，绘制对象可以是矩形、文本、图片等。

## 解决方案

1. 定义一个组织类TestOrg，用于展示节点名称和子节点。

   ```ts
   class TestOrg {
     title: string = '';
     children: TestOrg[] = [];
   }
   ```
2. 使用Canvas绘制每个文本框和内部文字方法。

   ```ts
   // 绘制文本框
   drawTextItem(startX: number, startY: number, width: number, height: number, title: string) {
     this.context.beginPath();
     // 画一个外边框
     this.context.rect(startX, startY, width, height);
     this.context.fillStyle = '#0A59F7';
     this.context.strokeStyle = '#0A59F7';
     this.context.stroke();
     this.context.fill();
     // 绘制文字
     this.context.fillStyle = Color.White;
     this.context.font = '16vp sans-serif';
     this.context.textBaseline = 'middle';
     let textWidth = this.context.measureText(title).width;
     this.context.fillText(title, startX + (width - textWidth) / 2, startY + height / 2, textWidth);
   }
   ```
3. 使用Canvas绘制文本框之间起点和终点路径。

   ```ts
   // 绘制路径线条
   drawLine(nodeX: number, nodeY: number, childX: number, childY: number) {
     let nodeWidth = 100;
     let nodeHeight = 50;
     let nodeMargin = 12;
     this.context.beginPath();
     this.context.moveTo(nodeX + (nodeWidth / 2), nodeY + nodeHeight);
     this.context.lineTo(nodeX + (nodeWidth / 2), nodeY + nodeHeight + (nodeMargin / 2));
     this.context.lineTo(childX + (nodeWidth / 2), childY - (nodeMargin / 2));
     this.context.lineTo(childX + (nodeWidth / 2), childY);
     this.context.lineWidth = 2;
     this.context.stroke(); // 将起点和终点连接
   }
   ```
4. 计算子节点的个数。

   ```ts
   // 计算节点数
   getAllCount(city: TestOrg) {
     let count = 0;
     city.children.reduce((pre, cue) => {
       count = pre + (cue.children && cue.children.length > 0 ? this.getAllCount(cue) : 1);
       return count;
     }, 0);
     return count;
   }
   ```
5. 构造树形结构，循环计算子节点个数，递归调用绘制文本框和画线方法。

   ```ts
   render(startX: number, startY: number, node: TestOrg) {
     let nodeWidth = 100;
     let nodeHeight = 50;
     let nodeMargin = 12;
     this.drawTextItem(startX, startY, nodeWidth, nodeHeight, node.title);
     if (node.children && node.children.length > 0) {
       let count = 0;
       count = this.getAllCount(node); // 计算底层节点个数
       let start = startX - (nodeWidth * count + (nodeMargin * (count - 1))) / 2; // 起点
       node.children.forEach((item) => {
         let childrenStartX = 0;
         let childrenStartY = startY + nodeMargin + nodeHeight;
         let nodeLength = 0;
         if (item.children && item.children.length > 0) {
           nodeLength = this.getAllCount(item);
         } else {
           nodeLength = 1;
         }
         childrenStartX = start + (nodeWidth * nodeLength + (nodeMargin * (nodeLength - 1))) / 2;
         start = start + (nodeWidth * nodeLength + (nodeMargin * (nodeLength - 1))) + nodeMargin;
         this.drawLine(startX, startY, childrenStartX, childrenStartY); // 划线
         this.render(childrenStartX, childrenStartY, item); // 画子级
       });
     }
   }
   ```

完整示例参考如下：

```ts
class TestOrg {
  title: string = '';
  children: TestOrg[] = [];
}

@Entry
@Component
struct CanvasExample {

  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  province = new TestOrg();

  aboutToAppear(): void {
    // 创建树形数据
    const street1 = new TestOrg;
    street1.title = '街道1';
    const street2 = new TestOrg;
    street2.title = '街道2';
    const street3 = new TestOrg;
    street3.title = '街道3';
    const region = new TestOrg;
    region.title = '建邺区';
    region.children = [street1, street2];
    const city1 = new TestOrg;
    city1.title = '南京市';
    city1.children = [region];
    const city2 = new TestOrg;
    city2.title = '扬州市';
    this.province.title = '江苏省';
    this.province.children = [city1, city2];
  }

  // 计算节点数
  getAllCount(city: TestOrg) {
    let count = 0;
    city.children.reduce((pre, cue) => {
      count = pre + (cue.children && cue.children.length > 0 ? this.getAllCount(cue) : 1);
      return count;
    }, 0);
    return count;
  }

  // 绘制文本框
  drawTextItem(startX: number, startY: number, width: number, height: number, title: string) {
    this.context.beginPath();
    // 画一个外边框
    this.context.rect(startX, startY, width, height);
    this.context.fillStyle = '#0A59F7';
    this.context.strokeStyle = '#0A59F7';
    this.context.stroke();
    this.context.fill();
    // 绘制文字
    this.context.fillStyle = Color.White;
    this.context.font = '16vp sans-serif';
    this.context.textBaseline = 'middle';
    let textWidth = this.context.measureText(title).width;
    this.context.fillText(title, startX + (width - textWidth) / 2, startY + height / 2, textWidth);
  }

  render(startX: number, startY: number, node: TestOrg) {
    let nodeWidth = 100;
    let nodeHeight = 50;
    let nodeMargin = 12;
    this.drawTextItem(startX, startY, nodeWidth, nodeHeight, node.title);
    if (node.children && node.children.length > 0) {
      let count = 0;
      count = this.getAllCount(node); // 计算底层节点个数
      let start = startX - (nodeWidth * count + (nodeMargin * (count - 1))) / 2; // 起点
      node.children.forEach((item) => {
        let childrenStartX = 0;
        let childrenStartY = startY + nodeMargin + nodeHeight;
        let nodeLength = 0;
        if (item.children && item.children.length > 0) {
          nodeLength = this.getAllCount(item);
        } else {
          nodeLength = 1;
        }
        childrenStartX = start + (nodeWidth * nodeLength + (nodeMargin * (nodeLength - 1))) / 2;
        start = start + (nodeWidth * nodeLength + (nodeMargin * (nodeLength - 1))) + nodeMargin;
        this.drawLine(startX, startY, childrenStartX, childrenStartY); // 划线
        this.render(childrenStartX, childrenStartY, item); // 画子级
      });
    }
  }

  // 绘制路径线条
  drawLine(nodeX: number, nodeY: number, childX: number, childY: number) {
    let nodeWidth = 100;
    let nodeHeight = 50;
    let nodeMargin = 12;
    this.context.beginPath();
    this.context.moveTo(nodeX + (nodeWidth / 2), nodeY + nodeHeight);
    this.context.lineTo(nodeX + (nodeWidth / 2), nodeY + nodeHeight + (nodeMargin / 2));
    this.context.lineTo(childX + (nodeWidth / 2), childY - (nodeMargin / 2));
    this.context.lineTo(childX + (nodeWidth / 2), childY);
    this.context.lineWidth = 2;
    this.context.stroke(); // 将起点和终点连接
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .onReady(() => {
          this.render(130, 200, this.province);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
