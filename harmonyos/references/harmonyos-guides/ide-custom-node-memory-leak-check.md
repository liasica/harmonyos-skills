---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-custom-node-memory-leak-check
title: @performance/custom-node-memory-leak-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/custom-node-memory-leak-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55b476babce07fe8f25d198f2153f8f0b92c01b40e9aba851e2313c649711d66
---

建议在Component中新建自定义节点时主动释放节点，避免因未释放节点导致的内存泄露。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/custom-node-memory-leak-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { BuilderNode } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct BuilderNodeDisposeExample {
6. private builder: BuilderNode<[]> | null = null
7. build() {
8. Column({ space: 20 }) {
9. Button('open dialog')
10. .onClick(() => {
11. const uiContext = this.getUIContext()
12. this.builder = new BuilderNode(uiContext) // 创建 BuilderNode
13. })

15. Button('close dialog')
16. .onClick(() => {
17. if (this.builder) {
18. this.builder.dispose() // 释放构建出的节点
19. this.builder = null
20. }
21. })
22. }
23. .width('100%')
24. .height('100%')
25. .padding(20)
26. .backgroundColor(Color.Grey)
27. }
28. }
```

## 反例

```
1. import { BuilderNode } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct LeakyBuilderExample {
6. private builder: BuilderNode<[]> | null = null
7. build() {
8. Column({ space: 20 }) {
9. Button('create dialog')
10. .onClick(() => {
11. const context = this.getUIContext();

13. // 没有释放旧 builder，直接创建新 builder
14. this.builder = new BuilderNode(context)

16. })
17. }
18. .width('100%')
19. .height('100%')
20. .padding(20)
21. .backgroundColor(Color.Grey)
22. }
23. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
