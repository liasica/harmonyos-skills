---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1414
title: 如何实现文本的动态播报
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现文本的动态播报
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4c024578985af041ea76ee052a6daa4cfdfd73cd7fcf72ae4364ee6fa42d39d5
---

## 问题现象

如何实现一个动态文字效果，将每个字符逐步从黑色变为橙色，类似于逐字播报的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/mWXOx4jPRS-h4oZSSgCaeA/zh-cn_image_0000002658842535.gif "点击放大")

## 背景知识

* [UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)提供[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效，支持属性动画、布局类宽高变化等场景。
* [ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)接口基于数组循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。

## 解决方案

1. 用双重ForEach实现逐字符动态分割。
2. 根据字符的总索引位置与当前value的比例，决定显示字符颜色。
3. 使用animateTo动画实现进度平滑过渡实现动态播报效果。

完整示例参考如下：

```screen
@Entry
@Component
struct Page {
  message: string = '问君西游何时还？畏途巉岩不可攀。但见悲鸟号古木，雄飞雌从绕林间。';
  @State value: number = 0;

  build() {
    Column() {
      // 使用getLines方法将message分割成多行字符串
      ForEach(this.getLines(this.message), (line: string, lineIndex: number) => {
        Row() {
          // 为每行中的每个字符生成Text组件
          ForEach(line.split(''), (char: string, charIndex: number) => {
            Text(char)
              .fontSize(30)
              .fontColor(this.getCharColor(lineIndex, charIndex))
              .fontWeight(FontWeight.Bold);
          });
        }
        .padding(30)
        .backgroundColor('#ffdedcdc');
      });
      Button('开始')
        .margin({ top: 30 })
        .backgroundColor('#0A59f7')
        .onClick(() => {
          let timeout = setInterval(() => {
            this.incrementValue();
            if (this.value >= 1) {
              clearInterval(timeout);
            }
            console.info("计时器：", this.value);
          }, 200);
        });
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }

  // 增加value并触发动画
  incrementValue() {
    this.getUIContext().animateTo({ duration: 500 }, () => {
      this.value = Math.min(this.value + 0.01, 1);
    });
  }

  // 将消息分割成行的方法
  getLines(message: string): string[] {
    const charsPerLine = this.getCharsPerLine();
    const lines: string[] = [];
    for (let i = 0; i < message.length; i += charsPerLine) {
      lines.push(message.substring(i, i + charsPerLine));
    }
    return lines;
  }

  // 获取每行字符数的方法
  getCharsPerLine(): number {
    return 8; // 根据需要调整每行字符数
  }

  // 根据字符的位置计算颜色
  getCharColor(lineIndex: number, charIndex: number): string {
    const totalIndex = lineIndex * this.getCharsPerLine() + charIndex;
    const ratio = totalIndex / this.message.length;
    if (ratio <= this.value) {
      return '#0A59f7'; // 渐变的起始颜色（蓝色）
    } else {
      return '#ff0a0a0a'; // 渐变的结束颜色（黑色）
    }
  }
}
```
