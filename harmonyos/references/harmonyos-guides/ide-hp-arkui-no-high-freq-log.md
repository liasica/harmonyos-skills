---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-no-high-freq-log
title: "@performance/hp-arkui-no-high-freq-log（已下线）"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-high-freq-log（已下线）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a464b13d8fcbccd2425ee6dc955796904d2900a12a024366151e6fbd40a0905e
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
