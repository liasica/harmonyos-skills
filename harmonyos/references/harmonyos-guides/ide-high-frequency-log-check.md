---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-high-frequency-log-check
title: "@performance/high-frequency-log-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/high-frequency-log-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c09f2d35acbdf3dc3df64b7f3c6ffb4f8f658e163adbb6d5d44cec9553e9db5e
---

不建议在高频函数中使用Hilog。高频函数包括：onTouch、onItemDragMove、onDragMove、onMouse、onVisibleAreaChange、onAreaChange、onScroll（已废弃）、onWillScroll。

高耗时函数处建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/high-frequency-log-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// Test.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Scroll()
        .onWillScroll(() => {
          const TAG = 'onWillScroll';
        })
    }
  }
}
```

## 反例

```screen
// Test.ets
import hilog from '@ohos.hilog';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Scroll()
        .onWillScroll(() => {
          // Avoid printing logs
          hilog.info(1001, 'Index', 'onWillScroll');
        })
    }
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
