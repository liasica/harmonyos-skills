---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-node-memory-leak-check
title: "@performance/custom-node-memory-leak-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/custom-node-memory-leak-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e8dd2d3ccfe7a875834701785569572437cd0aedeca37be76c17a2d99a66e56c
---

建议在Component中新建自定义节点时主动释放节点，避免因未释放节点导致的内存泄漏。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/custom-node-memory-leak-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { BuilderNode } from '@kit.ArkUI';

@Entry
@Component
struct BuilderNodeDisposeExample {
  private builder: BuilderNode<[]> | null = null
  build() {
    Column({ space: 20 }) {
      Button('open dialog')
        .onClick(() => {
          const uiContext = this.getUIContext()
          this.builder = new BuilderNode(uiContext) // 创建 BuilderNode
        })

      Button('close dialog')
        .onClick(() => {
          if (this.builder) {
            this.builder.dispose() // 释放构建出的节点
            this.builder = null
          }
        })
    }
    .width('100%')
    .height('100%')
    .padding(20)
    .backgroundColor(Color.Grey)
  }
}
```

## 反例

```screen
import { BuilderNode } from '@kit.ArkUI';

@Entry
@Component
struct LeakyBuilderExample {
  private builder: BuilderNode<[]> | null = null
  build() {
    Column({ space: 20 }) {
      Button('create dialog')
        .onClick(() => {
          const context = this.getUIContext();

          // 没有释放旧 builder，直接创建新 builder
          this.builder = new BuilderNode(context)

        })
    }
    .width('100%')
    .height('100%')
    .padding(20)
    .backgroundColor(Color.Grey)
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
