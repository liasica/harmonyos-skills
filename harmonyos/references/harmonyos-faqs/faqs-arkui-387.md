---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-387
title: 使用Text嵌套Span或者使用属性字符串渲染文本，部分文本颜色显示异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用Text嵌套Span或者使用属性字符串渲染文本，部分文本颜色显示异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:27f13972f69a215a9ab4093dbdee0c093b682cdb61017ec7760ae046c998caa0
---

**问题现象**

1、使用Text嵌套Span时，文本组合会导致后续文字的颜色无法正常渲染。

```typescript
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text() {
        Span('r')
          .fontColor(Color.Blue)
        Span('f')
          .fontColor(Color.Red)
      }
      .fontSize(50)
    }
    .width('100%')
    .height('100%')
  }
}
```

预期效果应为r显示蓝色、f显示红色，但实际rf都显示为蓝色：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ZU-Q_z2ERxuB7jRze6LuUw/zh-cn_image_0000002624635842.png)

2、使用属性字符串，同段文本设置不同样式后，与预期渲染结果不符。

```typescript
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  textController: TextController = new TextController();

  async onPageShow() {
    let style1: MutableStyledString = new MutableStyledString('');
    style1.appendStyledString(new StyledString('sr', [{
      start: 0,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Blue, fontSize: LengthMetrics.px(150) })
    }]));
    style1.appendStyledString(new StyledString('fff', [{
      start: 0,
      length: 5,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Orange, fontSize: LengthMetrics.px(150) })
    }]));
    this.textController.setStyledString(style1);
  }

  build() {
    Row() {
      Column() {
        Text(undefined, { controller: this.textController })
          .fontSize(30)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

预期结果应该是sr为蓝色，fff为黄色，实际srf结合为蓝色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/H_Qlb6-KRaqPBhYkZVW5Vw/zh-cn_image_0000002624475938.png)

**解决措施**

此问题与[fontFeature](../harmonyos-references/ts-basic-components-text.md#fontfeature12)有关，fontFeature 中的 "liga" 属性默认开启, 导致部分字符发生连接, 两个码点匹配到一个glyph，因此颜色展示异常，可禁用 "liga": "\"liga\" 0"。

系统默认字体支持的liga连字：Th fb ff fb ffb ffh ffi ffk ffl fh fi fk fl rf rt rv rx ry。

在对应的Text组件上添加如下代码，即可取消连字：

```ts
Text()
// ...
  .fontFeature("\"liga\" 0")
```
