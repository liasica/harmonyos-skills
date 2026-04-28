---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-nested-post-frame-callback-check
title: @performance/nested-post-frame-callback-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/nested-post-frame-callback-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:11920bb63f0f6955f29fe47d8a499c0e3b06aff780023cdc5ec8bec88fc59e2e
---

postFrameCallback会请求vsync，循环嵌套调用postFrameCallback会导致一直请求vsync，从而引起无效渲染问题。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/nested-post-frame-callback-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import {FrameCallback } from '@kit.ArkUI';
2. class MyFrameCallback extends FrameCallback {
3. private tag: string;
4. constructor(tag: string) {
5. super();
6. this.tag = tag;
7. }
8. onFrame(frameTimeNanos: number) {
9. console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
10. }
11. }
12. @Entry
13. @Component
14. struct Index {
15. build() {
16. Row() {
17. Button('Invoke postFrameCallback')
18. .onClick(() => {
19. this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
20. })
21. }
22. }
23. }
```

## 反例

```
1. import { FrameCallback, UIContext } from '@kit.ArkUI';
2. class MyFrameCallback extends FrameCallback {
3. private tag: string;
4. constructor(tag: string) {
5. super();
6. this.tag = tag;
7. const uiContext = new UIContext();
8. uiContext.postFrameCallback(new MyFrameCallback1("normTask1"));
9. }
10. onFrame(frameTimeNanos: number) {
11. new UIContext().postFrameCallback(new MyFrameCallback1("normTask1"));
12. console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
13. }
14. }
15. class MyFrameCallback1 extends FrameCallback {
16. private tag: string;
17. constructor(tag: string) {
18. super();
19. this.tag = tag;
20. }
21. onFrame(frameTimeNanos: number) {
22. console.info('MyFrameCallback1 ' + this.tag + ' ' + frameTimeNanos.toString());
23. }
24. }
25. @Entry
26. @Component
27. struct Index {
28. build() {
29. Row() {
30. Button('Nested postFrameCallback')
31. .onClick(() => {
32. this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
33. })
34. }
35. }
36. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
