---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-monitor-invisible-area-in-image-animation
title: @performance/monitor-invisible-area-in-image-animation
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/monitor-invisible-area-in-image-animation
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:14+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:84fc0adf5a25879d1220c72301fa50db3aeb3cf625ba8ee9e22974f8c46e9d39
---

使用ImageAnimation实现帧动画时，建议显式调用monitorInvisibleArea接口。在动画组件不可见时，会停止动画播放，减少无效的冗余动画带来的负载恶化。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/monitor-invisible-area-in-image-animation": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct ImageAnimatorTest {
4. @State message: string = 'hello world';
5. build() {
6. Column() {
7. ImageAnimator()
8. .images([])
9. .borderRadius(10)
10. .monitorInvisibleArea(true)
11. test1()
12. }
13. .width('100%')
14. }
15. }
16. @Builder
17. function test1() {
18. ImageAnimator()
19. .monitorInvisibleArea(true)
20. }
```

## 反例

```
1. @Entry
2. @Component
3. struct ImageAnimatorTest {
4. @State message: string = 'hello world';
5. build() {
6. Column() {
7. ImageAnimator()
8. .images([])
9. .borderRadius(10)
10. test1()
11. }
12. .width('100%')
13. }
14. }
15. @Builder
16. function test1() {
17. ImageAnimator()
18. .images([])
19. .borderRadius(10)
20. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
