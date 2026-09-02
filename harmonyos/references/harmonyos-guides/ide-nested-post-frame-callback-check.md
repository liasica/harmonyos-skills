---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-nested-post-frame-callback-check
title: "@performance/nested-post-frame-callback-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/nested-post-frame-callback-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3c0199b52405f93d570546a0f85633eb1c2e21f1c4e4c718d747ba9a477ab56b
---

postFrameCallback会请求vsync，循环嵌套调用postFrameCallback会导致一直请求vsync，从而引起无效渲染问题。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/nested-post-frame-callback-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import {FrameCallback } from '@kit.ArkUI';
class MyFrameCallback extends FrameCallback {
  private tag: string;
  constructor(tag: string) {
    super();
    this.tag = tag;
  }
  onFrame(frameTimeNanos: number) {
    console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
  }
}
@Entry
@Component
struct Index {
  build() {
    Row() {
      Button('Invoke postFrameCallback')
        .onClick(() => {
          this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
        })
    }
  }
}
```

## 反例

```screen
import { FrameCallback, UIContext } from '@kit.ArkUI';
class MyFrameCallback extends FrameCallback {
  private tag: string;
  constructor(tag: string) {
    super();
    this.tag = tag;
    const uiContext = new UIContext();
    uiContext.postFrameCallback(new MyFrameCallback1("normTask1"));
  }
  onFrame(frameTimeNanos: number) {
    new UIContext().postFrameCallback(new MyFrameCallback1("normTask1"));
    console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
  }
}
class MyFrameCallback1 extends FrameCallback {
  private tag: string;
  constructor(tag: string) {
    super();
    this.tag = tag;
  }
  onFrame(frameTimeNanos: number) {
    console.info('MyFrameCallback1 ' + this.tag + ' ' + frameTimeNanos.toString());
  }
}
@Entry
@Component
struct Index {
  build() {
    Row() {
      Button('Nested postFrameCallback')
        .onClick(() => {
          this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
        })
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
