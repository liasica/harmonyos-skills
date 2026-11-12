---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-buildernodenotrelease
title: BuilderNodeNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > BuilderNodeNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d1762280748c265e0adcd24bf5e2c76ef2c7327702e77674d9438b4e83462614
---

通过构造函数创建的BuilderNode对象，使用完毕后，需及时调用dispose()方法释放对实体节点的引用，避免导致内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "BuilderNodeNotRelease",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import { BuilderNode } from '@kit.ArkUI';
@Component
struct TestComponent {
  build() {
    Text('TestComponent')
  }
}
@Builder
function buildComponent() {
  TestComponent()
}

/**
 * 正例：正确释放资源
 */
@Component
export struct TestRelease {
  private builderNode: BuilderNode<[]> | null = null;
  makeNode(uiContext: UIContext): void {
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    this.builderNode.build(new WrappedBuilder(buildComponent));
  }
  aboutToAppear() {
    this.makeNode(this.getUIContext());
  }
  build() {
    Text('Hello TestRelease')
  }
  aboutToDisappear() {
    if (this.builderNode !== null) {
      this.builderNode.dispose();
    }
  }
}
```

## 反例

```ts
import { BuilderNode } from '@kit.ArkUI';
@Component
struct TestComponent {
  build() {
    Text('TestComponent')
  }
}
@Builder
function buildComponent() {
  TestComponent()
}

/**
 * 反例：未释放资源
 */
@Component
export struct TestNotRelease {
  private builderNode: BuilderNode<[]> | null = null;
  makeNode(uiContext: UIContext): void {
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } }); // leak
    this.builderNode.build(new WrappedBuilder(buildComponent));
  }
  aboutToAppear() {
    this.makeNode(this.getUIContext());
  }
  build() {
    Text('Hello TestNotRelease')
  }
  aboutToDisappear() {
    console.log('Do nothing');
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
