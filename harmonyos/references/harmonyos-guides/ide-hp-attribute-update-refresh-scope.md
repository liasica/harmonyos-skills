---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-attribute-update-refresh-scope
title: "@performance/hp-arkui-use-attributeUpdater-control-refresh-scope"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-attributeUpdater-control-refresh-scope
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bc8b8d0e6d7499822e9b65482cc66faeae7b308502c187a352d70829669ce7a1
---

建议使用attributeUpdater精准控制组件属性的刷新。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-attributeUpdater-control-refresh-scope": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { AttributeUpdater } from '@ohos.arkui.modifier';
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { FriendMoment } from './data/DataEntry'

export class MyTextUpdater extends AttributeUpdater<TextAttribute> {
  private color: string | number | Resource = "";

  constructor(color: string | number | Resource) {
    super();
    this.color = color
  }

  initializeModifier(instance: TextAttribute): void {
    instance.fontColor(this.color)
  }
}

@Component
export struct UpdaterComponent {
  private momentData: MyDataSource = new MyDataSource();

  build() {
    Column() {
      Text('use MyTextUpdater')
      List({ space: 5 }) {
        LazyForEach(this.momentData, (moment: FriendMoment) => {
          ListItem() {
            OneMomentNoModifier({ color: moment.color })
              .onClick(() => {
                console.log(`my id is ${moment.id}`)
              })
          }
        }, (moment: FriendMoment) => moment.id)
      }.width('100%')
      .height('100%')
      .cachedCount(5)
    }
  }
}

@Reusable
@Component
export struct OneMomentNoModifier {
  color: string | number | Resource = "";
  textUpdater: MyTextUpdater | null = null;

  aboutToAppear(): void {
    this.textUpdater = new MyTextUpdater(this.color);
  }

  aboutToReuse(params: Record<string, Object>): void {
    this.color = params.color as string | number | Resource;
    this.textUpdater?.attribute?.fontColor(this.color);
  }

  build() {
    Column() {
      Text('This is the title')
      Text('This is the internal text')
        .attributeModifier(this.textUpdater)
        .textAlign(TextAlign.Center)
        .fontStyle(FontStyle.Normal)
        .fontSize(13)
        .lineHeight(30)
        .opacity(0.6)
        .margin({ top: 10 })
        .fontWeight(30)
        .clip(false)
        .backgroundBlurStyle(BlurStyle.NONE)
        .foregroundBlurStyle(BlurStyle.NONE)
        .borderWidth(1)
        .borderColor(Color.Pink)
        .borderStyle(BorderStyle.Solid)
        .alignRules({
          'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
          'left': { 'anchor': 'image', 'align': HorizontalAlign.End }
        })
    }
  }
}
```

## 反例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { FriendMoment } from './data/DataEntry'

@Component
export struct UpdaterComponent {
  private momentData: MyDataSource = new MyDataSource();

  build() {
    Column() {
      Text('use nothing')
      List({ space: 5 }) {
        LazyForEach(this.momentData, (moment: FriendMoment) => {
          ListItem() {
            OneMomentNoModifier({ color: moment.color })
              .onClick(() => {
                console.log(`my id is ${moment.id}`)
              })
          }
        }, (moment: FriendMoment) => moment.id)
      }
      .width("100%")
      .height("100%")
      .cachedCount(5)
    }
  }
}

@Reusable
@Component
export struct OneMomentNoModifier {
  @State color: string | number | Resource = "";

  aboutToReuse(params: Record<string, Object>): void {
    this.color = params.color as string | number | Resource;
  }

  build() {
    Column() {
      Text('This is the title')
      Text('This is the internal text')
        .fontColor(this.color)
        .textAlign(TextAlign.Center)
        .fontStyle(FontStyle.Normal)
        .fontSize(13)
        .lineHeight(30)
        .opacity(0.6)
        .margin({ top: 10 })
        .fontWeight(30)
        .clip(false)
        .backgroundBlurStyle(BlurStyle.NONE)
        .foregroundBlurStyle(BlurStyle.NONE)
        .borderWidth(1)
        .borderColor(Color.Pink)
        .borderStyle(BorderStyle.Solid)
        .alignRules({
          'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },
          'left': { 'anchor': 'image', 'align': HorizontalAlign.End }
        })
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
