---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-componentcontentnotrelease
title: ComponentContentNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > ComponentContentNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f92bb6a2fb5fbc3153c60c9eb49b9f5867b29ab32e3c31105afd859c39f5169f
---

通过构造函数创建的ComponentContent对象，其底层使用了BuilderNode。使用完毕后，需及时调用dispose()释放对实体节点的引用，避免导致内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "ComponentContentNotRelease",
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
import { ComponentContent } from '@kit.ArkUI';
@Builder
function buildText() {
  Text('buildText')
}

/**
 * 正例：正确释放资源
 */
@Component
export struct TestRelease {
  private content: ComponentContent<Object> | null = null;
  aboutToAppear() {
    this.content = new ComponentContent<Object>(this.getUIContext(), wrapBuilder(buildText));
  }
  build() {
    Text('Hello TestRelease')
  }
  aboutToDisappear() {
    this.content?.dispose();
  }
}
```

## 反例

```ts
import { ComponentContent } from '@kit.ArkUI';
@Builder
function buildText() {
  Text('buildText')
}

/**
 * 反例：未释放资源
 */
@Component
export struct TestNotRelease {
  private content: ComponentContent<Object> | null = null;
  aboutToAppear() {
    this.content = new ComponentContent<Object>(this.getUIContext(), wrapBuilder(buildText)); // leak
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
