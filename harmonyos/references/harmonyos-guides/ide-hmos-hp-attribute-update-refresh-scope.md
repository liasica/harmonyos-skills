---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hp-attribute-update-refresh-scope
title: "@performance/hp-arkui-use-attributeUpdater-control-refresh-scope"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-attributeUpdater-control-refresh-scope
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b9b440084145a889fd8549bbbaa63b8d2a1055925f658ef342c4d8a5b5776fc0
---

建议使用attributeUpdater精准控制组件属性的刷新。

通用丢帧场景下，建议优先修改。

## 规则配置

```json
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

```ts
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

```ts
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

```json
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
