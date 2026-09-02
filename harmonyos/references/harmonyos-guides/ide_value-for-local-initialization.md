---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_value-for-local-initialization
title: "@previewer/mandatory-default-value-for-local-initialization"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 预览规则@previewer > @previewer/mandatory-default-value-for-local-initialization
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a4da1f884806557175281452095394a73eb877dba94b5626c69d079fdd7ef759
---

如果组件的属性支持本地初始化，需要设置一个合法的不依赖运行时的默认值。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@previewer/mandatory-default-value-for-local-initialization": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Builder
function MyBuilderFunction(): void {
}

@Entry
@Component
struct Index {
  messageA?: string;
  message: string = 'Hello World';
  @Provide messageB: string = 'messageB';
  @StorageLink('varA') varA: number = 2;
  @StorageProp('languageCode') lang: string = 'en';
  @LocalStorageLink('PropA') storageLink1: number = 1;
  @LocalStorageProp('PropB') storageLink2: number = 2;
  @BuilderParam myBuilder: () => void = MyBuilderFunction;

  build() {
    Row() {
      Column() {
        Text(this.message)
        this.myBuilder()
      }
    }
  }
}
```

## 反例

```screen
@Entry
@Component
struct Index {
  @BuilderParam myBuilder: () => void;

  build() {
    Row() {
      Column() {
        Text('Hello World')
        this.myBuilder()
      }
    }
  }
}
```

## 规则集

```screen
plugin:@previewer/recommended
plugin:@previewer/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
