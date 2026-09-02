---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-associations-state-var-check
title: "@performance/multiple-associations-state-var-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/multiple-associations-state-var-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e07650582af16b566dc2ddf2c2ac9933b00df045275c493b2e5ac14d3bd42347
---

多个组件关联同一数据时，建议在组件中使用@Watch装饰器添加更新条件，避免不必要的组件更新。

[通用丢帧场景](../best-practices/bpta-status-management.md#section117631443131915)下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/multiple-associations-state-var-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Observed
class UIStyle {
  fontSize: number = 0;
  fontColor: string = '';
  isChecked: boolean = false;
}
@Entry
@Component
struct MultipleAssociationsStateVarNoReport0 {
  @State uiStyle: UIStyle = new UIStyle();
  private listData: string[] = [];
  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.listData.push(`ListItemComponent ${i}`);
    }
  }
  build() {
    Row() {
      Column() {
        CompA({item: '1', index: 1, subStyle: this.uiStyle})
        CompB({item: '2', index: 2, subStyle: this.uiStyle})
        CompC({item: '3', index: 3, subStyle: this.uiStyle})
        Text('change state var')
          .onClick(()=>{
            this.uiStyle.fontSize = 20;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
@Component
struct CompA {
  @Prop item: string;
  @Prop index: number;
  @Link @Watch('onStyleChange') subStyle: UIStyle;
  @State fontSize: number = 0;
  isRender(): number {
    console.info(`CompA ${this.index} Text is rendered`);
    return this.fontSize;
  }
  onStyleChange() {
    this.fontSize = this.subStyle.fontSize;
  }
  build() {
    Column() {
      Text(this.item)
        .fontSize(this.isRender())
      Text('abc')
    }
  }
}
@Component
struct CompB {
  @Prop item: string;
  @Prop index: number;
  @Link @Watch('onStyleChange') subStyle: UIStyle;
  @State fontColor: string = '#00ffff';
  isRender(): number {
    console.info(`CompB ${this.index} Text is rendered`);
    return 10;
  }
  onStyleChange() {
    this.fontColor = this.subStyle.fontColor;
  }
  build() {
    Column() {
      Text(this.item)
        .fontSize(this.isRender())
        .fontColor(this.fontColor)
      Text('abc')
    }
  }
}
@Component
struct CompC {
  @Prop item: string;
  @Prop index: number;
  @Link @Watch('onStyleChange') subStyle: UIStyle;
  @State isChecked: boolean = false;
  isRender(): number {
    console.info(`CompC ${this.index} Text is rendered`);
    return 50;
  }
  onStyleChange() {
    this.isChecked = this.subStyle.isChecked;
  }
  build() {
    Column() {
      if (this.isChecked) {
        Text('checked')
      } else {
        Text('unchecked')
      }
    }
  }
}
```

## 反例

```screen
@Observed
class UIStyle {
  fontSize: number = 0;
  fontColor: string = '';
  isChecked: boolean = false;
}
@Entry
@Component
struct MultipleAssociationsStateVarReport0 {
  @State uiStyle: UIStyle = new UIStyle();
  private listData: string[] = [];
  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.listData.push(`ListItemComponent ${i}`);
    }
  }
  build() {
    Row() {
      Column() {
        CompA({item: '1', index: 1, subStyle: this.uiStyle})
        CompB({item: '2', index: 2, subStyle: this.uiStyle})
        CompC({item: '3', index: 3, subStyle: this.uiStyle})
        Text('change state var')
          .onClick(()=>{
            this.uiStyle.fontSize = 20;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
@Component
struct CompA {
  @Prop item: string;
  @Prop index: number;
  @Link subStyle: UIStyle;
  private sizeFont: number = 50;
  isRender(): number {
    console.info(`CompA ${this.index} Text is rendered`);
    return this.sizeFont;
  }
  build() {
    Column() {
      Text(this.item)
        .fontSize(this.isRender())
      Text('abc')
    }
  }
}
@Component
struct CompB {
  @Prop item: string;
  @Prop index: number;
  @Link subStyle: UIStyle;
  private sizeFont: number = 50;
  isRender(): number {
    console.info(`CompB ${this.index} Text is rendered`);
    return this.sizeFont;
  }
  build() {
    Column() {
      Text(this.item)
        .fontSize(this.isRender())
        .fontColor(this.subStyle.fontColor)
      Text('abc')
    }
  }
}
@Component
struct CompC {
  @Prop item: string;
  @Prop index: number;
  @Link subStyle: UIStyle;
  private sizeFont: number = 50;
  isRender(): number {
    console.info(`CompC ${this.index} Text is rendered`);
    return this.sizeFont;
  }
  build() {
    Column() {
      if (this.subStyle.isChecked) {
        Text('checked')
      } else {
        Text('unchecked')
      }
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
