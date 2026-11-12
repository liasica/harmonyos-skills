---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-no-high-freq-log
title: "@performance/hp-arkui-no-high-freq-log（已下线）"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-high-freq-log（已下线）
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:57+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ae29eee445f69b020c1da2fcc8364f7e3c7b4324fb5eccb1b62b9babc786f1d0
---

建议在正式发布的版本中，注释掉或删除日志打印代码。该规则已于5.0.3.403版本下线。

## 正例

```screen
import hilog from '@ohos.hilog';
@Entry
@Component
struct MyComponent{
  build() {
    Column() {
      Scroll()
        .onScroll(() => {
          //正例
          //hilog.info(1001, 'Index', 'onScroll')
          // do something
        })
    }
  }
}
```

## 反例

```screen
import hilog from '@ohos.hilog';
@Entry
@Component
struct MyComponent{
  build() {
    Column() {
      Scroll()
        .onScroll(() => {
          // 高频操作中不建议写日志
          hilog.info(1001, 'Index', 'onScroll')
          // do something
        })
    }
  }
}
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
