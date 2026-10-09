---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-high-frequency-log-check
title: "@performance/high-frequency-log-check"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/high-frequency-log-check
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d948b7a3b48b19e230fb73fab4ab05d3a3da46d848631928a39fd11e978d20cc
---

不建议在高频函数中使用Hilog。高频函数包括：onTouch、onItemDragMove、onDragMove、onMouse、onVisibleAreaChange、onAreaChange、onScroll（已废弃）、onWillScroll。

高耗时函数处建议优先修改。

## 规则配置

```json
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

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
