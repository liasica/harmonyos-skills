---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-state-variable-usage-in-ui-format-check
title: "@performance/state-variable-usage-in-ui-format-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/state-variable-usage-in-ui-format-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1c47d42507c2e76803240058487818fdd944e9bcad61057c46931f0ae6174f4c
---

建议删除不使用的UI变量。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/state-variable-usage-in-ui-format-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
class User {
  private name: string;
  constructor(name: string) {
    this.name = name;
  }
}

@Entry({ storage: new LocalStorage() })
@Component
struct Parent {
  @Prop  prop: number = 1;
  @State state: string = '1';
  @State state1: User = new User('name');
  @StorageLink(`k1`) storageLink: number = 1;
  @StorageProp(`k1`) storageProp: number = 1;
  @LocalStorageLink(`k1`) localStorageLink: number = 1;
  @LocalStorageProp(`k1`) localStorageProp: number = 1;
  @Provide('k1') provide: string = "hell";
  build() {
    Column() {
      Button() {
        Text('Insert a new item after item 1').fontSize(30)
      }

      Text(`${this.prop}`)
      Text(`${this.state}`)
      Text(`${this.state1}`)
      Text(`${this.storageLink}`)
      Text(`${this.storageProp}`)
      Text(`${this.localStorageLink}`)
      Text(`${this.localStorageProp}`)
      Text(`${this.provide}`)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}
```

## 反例

```screen
class User {
  private name: string;
  constructor(name: string) {
    this.name = name;
  }
}

@Entry({ storage: new LocalStorage() })
@Component
struct Parent {
  @Prop  prop: number = 1;
  @State state: string = '1';
  @State state1: User = new User('name');
  @StorageLink(`k1`) storageLink: number = 1;
  @StorageProp(`k1`) storageProp: number = 1;
  @LocalStorageLink(`k1`) localStorageLink: number = 1;
  @LocalStorageProp(`k1`) localStorageProp: number = 1;
  @Provide('k1') provide: string = "hell";
  build() {
    Column() {
      Button() {
        Text('Insert a new item after item 1').fontSize(30)
      }

      Text(`${this.prop}`)
      Text(`${this.state}`)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
