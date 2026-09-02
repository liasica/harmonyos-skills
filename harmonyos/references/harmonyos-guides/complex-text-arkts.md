---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-arkts
title: 复杂文本绘制与显示（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 复杂文本绘制与显示（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e449b6374e57938fcef5dbee8bbb0d8fa4b36e03710c4e017af0bedcb0b599bb
---

在进行文本绘制时，可以通过选择合适的字体、大小和颜色完成简单文本的绘制与显示；此外，还支持通过设置其他丰富的样式、语言、段落等进行复杂文本的绘制。

复杂文本绘制主要包含以下几个场景：

* 多语言文本绘制与显示
* 多行文本绘制与显示
* 多样式文本绘制与显示

## 多语言文本绘制与显示

多语言支持是全球化应用的基础。多语言文本绘制需要支持不同语言的字符集及其独特的显示需求，例如右到左语言（如阿拉伯语）或竖排文本（如中文）。开发者需要理解不同语言的渲染特性，确保文本的正确显示。

在多语言文本使用的场景下，主要通过指定[TextStyle](../harmonyos-references/js-apis-graphics-text.md#textstyle)文本样式中的**locale**字段来实现，可直接通过locale字段的值优先匹配对应字体，跳过遍历列表匹配字体的过程，从而降低匹配时间和内存使用。

### 开发步骤

1. 通过context获取到Canvas画布对象。

   ```typescript
   // 绘制代码逻辑写在这里
   let canvas = context.canvas;
   ```
2. 初始化文本样式。

   ```typescript
   let myTextStyle: text.TextStyle = {
     color: {
       alpha: 255,
       red: 255,
       green: 0,
       blue: 0
     },
     fontSize: 50,
     // 设置语言偏好为简体中文
     locale: 'zh-Hans'
   };
   ```
3. 初始化段落样式。

   ```typescript
   let myParagraphStyle: text.ParagraphStyle = {
     textStyle: myTextStyle,
   };
   ```
4. 初始化段落对象，并添加文本。

   ```typescript
   let fontCollection = text.FontCollection.getGlobalInstance();
   let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   // 更新文本样式
   paragraphBuilder.pushStyle(myTextStyle);
   // 添加文本
   paragraphBuilder.addText('你好，世界');
   ```
5. 排版段落并进行文本绘制。

   ```typescript
   // 生成段落
   let paragraph = paragraphBuilder.build();
   // 布局
   paragraph.layoutSync(1250);
   // 绘制文本
   paragraph.paint(canvas, 10, 0);
   ```

### 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/tB09LCx-SCCXS837X4ixyw/zh-cn_image_0000002706674734.png)

## 多行文本绘制与显示

多行文本相对于单行文本比较复杂，一般针对多行文本，需要进行文本排版、断词策略设置、文本对齐方式、最大行数限制等，主要通过设置段落样式实现。

### 实现说明

**段落样式**（[ParagraphStyle](../harmonyos-references/js-apis-graphics-text.md#paragraphstyle)）是对多行文本中每段内容的样式设置，包括断词策略、文本对齐方式、最大行数限制等。开发者可以通过对不同段落进行样式化，以提高文本的可读性和美观性。

### 开发步骤

1. 通过context获取到Canvas画布对象。

   ```typescript
   // 绘制代码逻辑写在这里
   let canvas = context.canvas;
   ```
2. 初始化文本样式。

   ```typescript
   let myTextStyle: text.TextStyle = {
     color: {
       alpha: 255,
       red: 255,
       green: 0,
       blue: 0
     },
     fontSize: 50,
     // 当wordBreak为text.WordBreak.BREAK_HYPHEN时，需要为段落设置语言偏好，段落会在不同语言偏好下呈现不同的文本断词效果
     locale: 'en-gb'
   };
   ```
3. 初始化段落样式。

   ```typescript
   let myParagraphStyle: text.ParagraphStyle = {
     textStyle: myTextStyle,
     // 文本对齐方式
     align: text.TextAlign.LEFT,
     // 最大行数
     maxLines: 3,
     // 断词策略
     wordBreak: text.WordBreak.BREAK_WORD
   };
   ```
4. 初始化段落对象，并添加文本。

   ```typescript
   let fontCollection = text.FontCollection.getGlobalInstance();
   let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   // 更新文本样式
   paragraphBuilder.pushStyle(myTextStyle);
   // 添加文本
   paragraphBuilder.addText('Hello World Hello World Hello World Hello World Hello World Hello World ' +
     'Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World ' +
     'Hello World Hello World Hello World Hello World Hello World ');
   ```
5. 排版段落并进行文本绘制。

   ```typescript
   // 生成段落
   let paragraph = paragraphBuilder.build();
   // 布局
   paragraph.layoutSync(1250);
   // 绘制文本
   paragraph.paint(canvas, 10, 0);
   ```

### 效果展示

| 段落样式设置（断词策略、文本对齐方式、最大行数限制） | 效果示意 |
| --- | --- |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为3，断词策略为text.WordBreak.BREAK\_WORD。 |  |
| 文本对齐方式为text.TextAlign.RIGHT，最大行数为3，断词策略为text.WordBreak.BREAK\_WORD。 |  |
| 文本对齐方式为text.TextAlign.JUSTIFY，最大行数为10，断词策略为text.WordBreak.BREAK\_WORD。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为3，断词策略为text.WordBreak.BREAK\_ALL。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_ALL。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_HYPHEN，  不设置语言偏好。段落无连字符“-”断词效果。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_HYPHEN，  语言偏好为en-gb（英式英语）。段落产生连字符“-”断词效果，并根据语言偏好呈现英式语言环境断词效果。 |  |
| 文本对齐方式为text.TextAlign.LEFT，最大行数为10，断词策略为text.WordBreak.BREAK\_HYPHEN，  语言偏好为en-us（美式英语）。段落产生连字符“-”断词效果，并根据语言偏好呈现美式语言环境断词效果。 |  |

## 多样式文本绘制与显示

除基本文字、排版属性之外，针对应用中不同文本的设计，开发者可能需要设置使用不同的绘制样式或能力，以凸显对应文本的独特表现或风格，此时可以结合使用多种绘制样式进行文本的渲染。

当前支持的多样式绘制及各绘制样式侧重效果如下：

* **装饰线样式绘制：** 主要通过不同的线条样式对文本进行装饰，可以使文本更加突出，富有表现力。
* **字体特性绘制：** 主要通过字体的变化，包括粗细、斜体等特性来改变文本的外观，增强文本的可读性和美观性。
* **可变字体绘制：** 对应提供文本在不同的显示环境和设备上灵活调整的能力，可满足更为精细的视觉效果。
* **文本阴影绘制：** 主要通过在文本周围添加阴影效果，以提升文本的层次感和立体感，从而使文本更具吸引力。
* **占位符绘制：** 可以在不确定文本内容时保持文本布局的稳定性，使得文本显示更为流畅和自然。
* **自动间距绘制：** 可以在一些字符混排切换的地方自动添加额外间距，提升阅读体验。
* **垂直对齐：** 调整文本在垂直方向排版位置，提升排版质量。
* **上下标：** 可以将任意字符处理成上标或下标，更精准表达文本含义。
* **高对比度文字绘制：** 主要通过将深色文字变黑、浅色文字变白，增强文本的对比效果。
* **行高调整：** 调整行高可改变文本行的垂直间距，使行间距更松散或更紧凑，显著改善文本垂直截断问题，提高可读性。
* **行间距调整：** 通过调整行间距的方式可以实现行高调整一样的效果，优化阅读体验。
* **省略号样式设置：** 在文本内容超出显示区域时，可以使用省略号截断文本，支持头部、中部、尾部以及多行省略模式。
* **文字换行方式设置：** 文本排版时支持不同的断行策略，可根据场景选择合适的换行方式。
* **行首标点压缩：** 在排版中，通过开启行首标点压缩功能，将行首标点符号进行挤压处理，避免标点占用行首空间，提升排版紧凑度。

### 装饰线

装饰线（[Decoration](../harmonyos-references/js-apis-graphics-text.md#decoration)）是指在文本上方、下方或中间添加的装饰性线条，当前支持上划线、下划线、删除线。

可以通过添加文本装饰线，提升文本的视觉效果和可读性。

使用装饰线需要初始化装饰线样式对象，并添加到文本样式中，从而在文本绘制时生效。

具体使用效果可参见下文[示例一](complex-text-arkts.md#示例一装饰线字体特征)。

### 字体特征

**字体特征**（[FontFeature](../harmonyos-references/js-apis-graphics-text.md#fontfeature)）绘制专注于在文本渲染过程中对字体特性（如粗体、斜体、字体变体等）的处理，允许字体在不同的排版场景下表现出不同的效果，可用于增强文本的表现力，使其更符合设计和阅读需求。

常见的**FontFeature**包含有liga、frac、case等，需要对应的ttf文件支持才能正常使能。

具体使用效果可参见下文[示例一](complex-text-arkts.md#示例一装饰线字体特征)。

### 可变字体

**可变字体**（[FontVariation](../harmonyos-references/js-apis-graphics-text.md#fontvariation)）是一种在一个字体文件中包含多个字形变体的字体格式，允许在一个字体文件内灵活地调整字体的各种属性（如字重、字宽、斜体等）。

与传统字体文件（每种变体需要一个独立的文件）不同，可变字体在一个字体文件中包含多个变体轴，可通过使用可变字体实现文本渲染绘制时的平滑过渡。

具体使用效果可参见下文[示例二](complex-text-arkts.md#示例二可变字体文本阴影占位符)。

### 文本阴影

**文本阴影**（[TextShadow](../harmonyos-references/js-apis-graphics-text.md#textshadow)）为文本提供了深度感，使得文本在背景上更具立体感。通常用于提升文本的视觉吸引力或增强可读性，尤其是在色彩对比度较低的场景下。

其中，TextShadow有三个属性，分别为阴影颜色color、阴影基于当前文本的偏移位置point、阴影半径blurRadius。

使用阴影效果需要在文本样式中设置对应的阴影效果数组，从而在文本绘制时生效。

具体使用效果可参见下文[示例二](complex-text-arkts.md#示例二可变字体文本阴影占位符)。

### 占位符

占位符绘制用于处理文本中占位符符号的渲染。

占位符也是用来实现图文混排的关键，是指在实际图像或内容注册之前，用来预先提供或替代某个位置的视觉元素。

具体使用效果可参见下文[示例二](complex-text-arkts.md#示例二可变字体文本阴影占位符)。

### 自动间距

使能自动间距，则会在文本排版时自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。例如，在中英文混排场景中，使能自动间距即可在中英文切换的地方自动添加额外间距，提升阅读体验。

关键示例如下：

```ts
let myParagraphStyle: text.ParagraphStyle = {
  autoSpace: true
};
```

### 垂直对齐

垂直对齐用于调整文本在一行中垂直方向的排版位置。开启行高缩放或行内存在不同字号文本混排时使能垂直对齐，可以让文本实现顶部对齐、居中对齐、底部对齐或基线对齐（默认）。关键代码如下：

```ts
let myParagraphStyle: text.ParagraphStyle = {
  verticalAlign: text.TextVerticalAlign.CENTER
};
```

具体使用效果可参见下文[示例三](complex-text-arkts.md#示例三垂直对齐)。

### 上下标

使能上下标，能将文本作为上标或下标参与排版。一般用于数学公式、化学式等场景。关键代码如下：

```ts
let superScriptStyle: text.TextStyle = {
    badgeType: text.TextBadgeType.TEXT_SUPERSCRIPT
};
```

具体使用效果可参见下文[示例四](complex-text-arkts.md#示例四上下标文本)。

### 高对比度

高对比度可将深色文字变黑、浅色文字变白。开发者可选择开启或关闭应用的高对比度文字渲染，或遵循系统设置中的高对比度文字配置。

高对比度模式有3种，具体参考[TextHighContrast](../harmonyos-references/js-apis-graphics-text.md#texthighcontrast20)。

具体使用效果可参见下文[示例五](complex-text-arkts.md#示例五高对比度)。

### 行高调整

当前行高调整方式包括两种：设置行高上限/下限和使用行高缩放系数。

**行高调整（方式一）**

从API version 21开始，支持通过设置行高上限和下限调整行高，关键代码如下：

```ts
let myTextStyle: text.TextStyle = {
    // 设置行高上限
    lineHeightMaximum: 65,
    // 设置行高下限
    lineHeightMinimum: 65
};
```

使用效果参考下文[示例六](complex-text-arkts.md#示例六行高调整方式一)。

**行高调整（方式二）**

通过设置行高缩放系数调整行高，关键代码如下：

```ts
let myTextStyle: text.TextStyle = {
    // 开启行高缩放开关
    heightOnly: true,
    // 设置行高缩放系数
    heightScale: 1.5,
    // 设置行高缩放风格
    lineHeightStyle: text.LineHeightStyle.FONT_HEIGHT
};
```

使用效果参考下文[示例七](complex-text-arkts.md#示例七行高调整方式二)。

### 行间距调整

从API version 21开始，支持设置行间距改善文本行之间的距离，提高阅读体验，关键代码如下：

```ts
let myParagraphStyle: text.ParagraphStyle = {
  // 设置行间距
  lineSpacing: 100,
  // 关闭段落上升部和下降部
  textHeightBehavior: text.TextHeightBehavior.DISABLE_ALL,
};
```

具体使用效果可参见下文[示例八](complex-text-arkts.md#示例八行间距调整)。

### 省略号样式设置

从API version 22开始，支持设置省略号样式，在文本内容超出显示区域时截断文本。从API version 24开始，支持多行省略模式。

通过[ParagraphStyle](../harmonyos-references/js-apis-graphics-text.md#paragraphstyle)中的textStyle属性设置省略号模式，可选的省略号模式可见[EllipsisMode](../harmonyos-references/js-apis-graphics-text.md#ellipsismode)。

需要注意，省略号相关属性需要在ParagraphStyle的textStyle中设置才生效，通过pushStyle设置的省略号属性不会生效。

具体使用效果可参见下文[示例九](complex-text-arkts.md#示例九省略号样式)。

### 文字换行方式设置

从API version 22开始，支持在文本排版时设置断行策略，断行策略决定了文本如何在行尾进行换行处理。

通过设置[ParagraphStyle](../harmonyos-references/js-apis-graphics-text.md#paragraphstyle)中的breakStrategy属性可以控制断行策略，可选的断行策略可见[BreakStrategy](../harmonyos-references/js-apis-graphics-text.md#breakstrategy)。

具体使用效果可参见下文[示例十](complex-text-arkts.md#示例十文字换行方式)。

### 行首标点压缩

从API version 23开始，在文本排版中支持行首标点压缩功能。通过启用行首标点压缩功能，可以将行首标点符号进行挤压处理，提升排版紧凑度。

通过设置[ParagraphStyle](../harmonyos-references/js-apis-graphics-text.md#paragraphstyle)中的compressHeadPunctuation属性设置是否启用行首标点压缩。

具体使用效果可参见下文[示例十一](complex-text-arkts.md#示例十一行首标点压缩)。

### 示例一（装饰线、字体特征）

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext } from '@kit.ArkUI'
import { UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    // 初始化装饰线对象
    let decorations: text.Decoration =
      {
        // 装饰线类型，支持上划线、下划线、删除线
        textDecoration: text.TextDecorationType.UNDERLINE,
        // 装饰线颜色
        color: {
          alpha: 255,
          red: 255,
          green: 0,
          blue: 0
        },
        // 装饰线样式，支持波浪，虚线，直线等
        decorationStyle:text.TextDecorationStyle.SOLID,
        // 装饰线粗细缩放比例
        decorationThicknessScale: 1
      };

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 200,
      // 设置装饰线
      decoration: decorations,
      // 开启字体特征
      fontFeatures: [{name: 'frac', value: 1}]
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 更新文本样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('1/2 1/3 1/4 ');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(1250);
    // 绘制文本
    paragraph.paint(canvas, 0, 0);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode();
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Image(this.src)
          .width('0%').height('0%')
          .onComplete(
            () => {
              performTask();
            })
      }
      .width('100%')
    }
  }
}
```

具体示意效果如下所示：

| 样式设置（装饰线样式、字体特征） | 示意效果 |
| --- | --- |
| 不开启装饰线和字体特征 |  |
| 开启装饰线和字体特征 |  |

### 示例二（可变字体、文本阴影、占位符）

这里以可变字体、文本阴影、占位符三个特性为例，呈现多样式文本的绘制与显示。

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext } from '@kit.ArkUI'
import { UIContext } from '@kit.ArkUI'
import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 120,
      // 可变字体
      fontVariations: [{axis: 'wght', value: 555}],
      // 文本阴影
      textShadows: [{color: { alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00 }, point: {x:10,y:10}, blurRadius: 10}],
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 初始化占位符对象
    let myPlaceholderSpan: text.PlaceholderSpan = {
      // 宽度
      width: 300,
      // 高度
      height: 300,
      // 基线对齐策略
      align: text.PlaceholderAlignment.BOTTOM_OF_ROW_BOX,
      // 使用的文本基线类型
      baseline: text.TextBaseline.ALPHABETIC,
      // 相比基线的偏移量。只有对齐策略是OFFSET_AT_BASELINE时生效
      baselineOffset: 100
    };
    // 添加占位符
    paragraphBuilder.addPlaceholder(myPlaceholderSpan);

    // 更新文本样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('Hello Test');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(1250);
    // 绘制文本
    paragraph.paint(canvas, 0, 0);

    // 获取全部占位符的数组
    let placeholderRects = paragraph.getRectsForPlaceholders();
    // 获取第一个占位符的左边界
    let left = placeholderRects[0].rect.left;
    // 获取第一个占位符的上边界
    let top = placeholderRects[0].rect.top;
    // 获取第一个占位符的右边界
    let right = placeholderRects[0].rect.right;
    // 获取第一个占位符的下边界
    let bottom = placeholderRects[0].rect.bottom;
    let pen: drawing.Pen =  new drawing.Pen();
    let penColor : common2D.Color = { alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00 };
    pen.setColor(penColor);
    canvas.attachPen(pen);
    // 使用draw方法绘制占位符矩形框
    canvas.drawRect(left,top,right,bottom);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode();
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600,
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Image(this.src)
          .width('0%').height('0%')
          .onComplete(
            () => {
              performTask();
            })
      }
      .width('100%')
    }
  }
}
```

具体示意效果如下所示：

| 样式设置（可变字体、文本阴影、占位符） | 示意效果 |
| --- | --- |
| 不开启可变字体和文本阴影，不使用占位符 |  |
| 开启可变字体和文本阴影，使用占位符 |  |

### 示例三（垂直对齐）

这里以垂直对齐-居中对齐特性为例，呈现文本垂直方向排版的特性。

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 30,
      // 开启行高缩放
      heightOnly: true,
      // 行高缩放系数为字号的2倍
      heightScale: 2
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      // 设置垂直对齐-居中对齐模式
      verticalAlign: text.TextVerticalAlign.CENTER,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 设置待排版文本要应用的样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('VerticalAlignment-center');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(1000);
    // 绘制文本
    paragraph.paint(canvas, 0, 0);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode();
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for vertical alignment')
          .onAppear(() => {
            performTask();
          })
      }
      .width('100%')
    }
  }
}
```

具体示意效果如下所示：

| 样式设置（垂直对齐） | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| 基线对齐（默认） |  |
| 顶部对齐 |  |
| 居中对齐 |  |
| 底部对齐 |  |

### 示例四（上下标文本）

这里以下标样式为例，呈现上下标文本排版特性。

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 30,
    };

    let subScriptStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 30,
      // 设置下标样式
      badgeType: text.TextBadgeType.TEXT_SUBSCRIPT
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 设置待排版文本要应用的样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('The chemical formula for water: H');
    paragraphBuilder.pushStyle(subScriptStyle);
    paragraphBuilder.addText('2');
    paragraphBuilder.pushStyle(myTextStyle);
    paragraphBuilder.addText('o');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(1000);
    // 绘制文本
    paragraph.paint(canvas, 0, 0);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode();
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for superscript and subscript')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}
```

具体示意效果如下所示：

| 样式设置（上下标） | 示意效果 |
| --- | --- |
| 上标文本 |  |
| 下标文本 |  |

### 示例五（高对比度）

这里以高对比度为例，呈现高对比度文字的绘制与显示。

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext, UIContext} from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    // 开启APP的文字渲染高对比度配置
    text.setTextHighContrast(text.TextHighContrast.TEXT_APP_ENABLE_HIGH_CONTRAST);

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 111,
        green: 255,
        blue: 255
      },
      fontSize: 100,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 更新文本样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('Hello World');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(1250);
    // 绘制文本
    paragraph.paint(canvas, 10, 800);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode();
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      };
      renderNode.pivot = { x: 0.2, y: 0.8 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test high contrast')
          .onAppear(() => {
            performTask();
          })
      }
      .width('100%')
    }
  }
}
```

具体示意效果如下所示：

| 高对比度设置 | 示意效果 |
| --- | --- |
| 不开启高对比度 |  |
| 开启高对比度 |  |

### 示例六（行高调整方式一）

这里以行高上限与行高下限设置相同值为例，呈现固定行高时的绘制表现。

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
      // 设置行高上限
      lineHeightMaximum: 65,
      // 设置行高下限
      lineHeightMinimum: 65,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 设置待排版文本要应用的样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('Hello World!');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(1000);
    // 绘制文本
    paragraph.paint(canvas, 0, 0);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode()
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
}
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext)
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode()
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon')
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for line height limit')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}
```

具体效果如下所示：

| 行高上限值 | 行高下限值 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- | --- |
| 65 | 65 |  |
| 200 | 200 |  |

### 示例七（行高调整方式二）

这里以行高缩放且行高缩放样式FontHeight为例，呈现行高调整后文字的绘制与显示。

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
      // 开启行高缩放开关
      heightOnly: true,
      // 设置行高缩放系数
      heightScale: 1.5,
      // 设置行高缩放风格
      lineHeightStyle: text.LineHeightStyle.FONT_HEIGHT,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 设置待排版文本要应用的样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('Hello World!');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(1000);
    // 绘制文本
    paragraph.paint(canvas, 0, 0);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode();
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
}
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext)
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      };
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode()
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon')
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for line height limit')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}
```

具体效果如下所示：

| 行高缩放样式 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| FontSize |  |
| FontHeight |  |

### 示例八（行间距调整）

这里以关闭段落上升部下降部并设置行间距为例，呈现行间距增加后的文本绘制与显示。

```typescript
import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// 创建一个MyRenderNode类，并绘制文本。
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      // 设置行间距
      lineSpacing: 100,
      // 关闭段落上升部和下降部
      textHeightBehavior: text.TextHeightBehavior.DISABLE_ALL,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // 设置待排版文本要应用的样式
    paragraphBuilder.pushStyle(myTextStyle);
    // 添加文本
    paragraphBuilder.addText('Hello World!');

    // 生成段落
    let paragraph = paragraphBuilder.build();
    // 布局
    paragraph.layoutSync(200);
    // 绘制文本
    paragraph.paint(canvas, 0, 0);
  }
}

// 创建一个MyRenderNode对象
const textNode = new MyRenderNode();
// 定义newNode的像素格式
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
}
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon')
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for lineSpacing and height behavior')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}
```

具体效果如下所示：

| 上升部下降部开关 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| DISABLE\_ALL |  |
| ALL |  |

### 示例九（省略号样式）

以下示例展示了开启尾部省略号模式的文本截断效果。

```typescript
// 设置文本样式，包含省略号字符串和省略号模式
let myTextStyle: text.TextStyle = {
  color: {
    alpha: 255,
    red: 0,
    green: 0,
    blue: 0
  },
  fontSize: 40,
  // 设置省略号字符串
  ellipsis: '...',
  // 设置省略号模式为尾部省略
  ellipsisMode: text.EllipsisMode.END
};
// 设置段落样式，包含最大行数
let myParagraphStyle: text.ParagraphStyle = {
  textStyle: myTextStyle,
  // 设置最大显示行数为2
  maxLines: 2
};
```

具体效果如下所示：

| 省略号模式 | 示意效果 |
| --- | --- |
| 不开启省略号 |  |
| 开启头部省略号 |  |
| 开启中部省略号 |  |
| 开启尾部省略号 |  |
| 开启多行头部省略号 |  |
| 开启多行中部省略号 |  |

### 示例十（文字换行方式）

以下示例展示了BALANCED断行策略对文本排版的影响。

```typescript
// 设置断行策略为均衡策略（BALANCED）
let myParagraphStyle: text.ParagraphStyle = {
  textStyle: myTextStyle,
  // 设置断行策略为均衡策略，各行宽度尽量均衡
  breakStrategy: text.BreakStrategy.BALANCED
};
```

具体效果如下所示：

| 断行策略 | 示意效果 |
| --- | --- |
| GREEDY |  |
| BALANCED |  |
| HIGH\_QUALITY |  |

### 示例十一（行首标点压缩）

以下示例展示了开启行首标点压缩的排版对比效果。

```typescript
// 开启行首标点压缩
let myParagraphStyle: text.ParagraphStyle = {
  textStyle: myTextStyle,
  compressHeadPunctuation: true
};
```

具体效果如下所示：

| 标点压缩设置 | 示意效果 |
| --- | --- |
| 未开启标点压缩 |  |
| 开启标点压缩 |  |
