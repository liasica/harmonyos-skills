---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-38
title: 如何实现智能手表圆形环绕文字效果
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何实现智能手表圆形环绕文字效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8b320278bd22b58e9ff82a7880b2f204f0b2a10f2efd61c59f926fb3e1f9e7f2
---

## 问题现象

如何实现智能手表中的圆形环绕文字效果？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
* [RichText](../harmonyos-references/ts-basic-components-richtext.md)：富文本组件，解析并显示HTML格式文本，适用于加载与显示一段HTML字符串，且不需要对显示效果进行较多自定义的应用场景。

## 解决方案

* **方案一**：通过translate设置当前坐标系的原点到画布中心位置，设置字体大小计算出圆环上每一个字符所占的弧度，最后利用for循环使用rotate调整角度，在当前坐标轴进行顺时针旋转绘制每个字符。

  ```ts
  @Entry
  @Component
  struct Index {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    // 转换为弧度值
    private getAngle(n: number) {
      return Math.PI / 180 * n;
    }

    private drawCircleText(text: string) {
      const width = this.context.width, height = this.context.height;
      const fontSize = 14;
      const r = width / 2 - fontSize;
      this.context.clearRect(0, 0, width, height); // 清空画布
      this.context.save();
      this.context.font = `${fontSize}vp`;
      this.context.textBaseline = 'top';
      const charRadius = 360 / text.length; // 一个字符所占的弧度
      this.context.translate(width / 2, height / 2);
      for (let i = 0; i < text.length; i++) {
        this.context.fillText(text.charAt(i), 0, -r);
        this.context.rotate(this.getAngle(charRadius));
      }
      this.context.restore();
    }

    build() {
      Row() {
        Column() {
          Canvas(this.context)
            .width(200)
            .height(200)
            .borderColor('green')
            .borderWidth(1)
            .onReady(() => this.drawCircleText('Hello,World!Hello,World!'))
        }
        .width('100%')
      }
      .height('100%')
      .backgroundColor(Color.White)
    }
  }
  ```
* **方案二**：在RichText中通过HTML字符串利用svg标签，通过<path>元素定义形状设置id为圆形，<text>元素设置一个由文字组成的图形，在<textPath>元素内部放置文本，并通过其xlink:href属性值引用<path>元素路径进行绘制。

  ```ts
  interface RichTextProps {
    width: number;
    height: number;
    fontSize: number;
    fontColor: string;
    text: string;
  }

  function getRichTextStr(props: RichTextProps) {
    const width = props.width, height = props.height;
    const fontSize = props.fontSize, fontColor = props.fontColor;
    const str = `<div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;">
            <svg style="overflow: visible; display: inline-block;" viewBox="0 0 100 100" width="${width}" height="${height}">
               <path fill='none' d="M 0,50 a 50,50 0 1, 1 0, 1 z" id="circle"></path>
               <text font-size='${fontSize}'  fill='${fontColor}'>
                 <textPath xlink:href="#circle">
                    ${props.text}
                 </textPath>
               </text>
            </svg>
          </div>`;
    return str;
  };

  @Entry
  @Component
  struct CircleText2 {
    defaultRichTextProps: RichTextProps = {
      width: 600,
      height: 600,
      fontSize: 14,
      fontColor: 'red',
      text: 'Hello,World!Hel!Hello,World!HelHello,World!HelWorld!Hel',
    };

    build() {
      Row() {
        Column() {
          Text('使用RichText实现')
            .width('100%')
            .margin({ bottom: 10, left: 10 })
          RichText(getRichTextStr(this.defaultRichTextProps))
            .borderColor('green')
            .borderWidth(1)
            .width(300)
            .height(300)

        }
        .width('100%')
      }
    }
  }
  ```
