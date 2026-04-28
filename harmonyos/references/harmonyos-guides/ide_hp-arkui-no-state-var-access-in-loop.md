---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-state-var-access-in-loop
title: @performance/hp-arkui-no-state-var-access-in-loop
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-state-var-access-in-loop
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:05+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9de67f5fd42d34991d8768b0fe574b13af276d0b8639c49a1b7567349197fd5b
---

避免在for、while等循环逻辑中频繁读取状态变量。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-no-state-var-access-in-loop": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import hilog from '@ohos.hilog'

3. @Entry
4. @Component
5. struct MyComponent{
6. @State message: string = '';
7. build() {
8. Column() {
9. Button('点击打印日志')
10. .onClick(() => {
11. this.message = 'click';
12. let logMessage: string = this.message;
13. for (let i = 0; i < 10; i++) {
14. hilog.info(0x0000, 'TAG', '%{public}s', logMessage);
15. }
16. })
17. .width('90%')
18. .backgroundColor(Color.Blue)
19. .fontColor(Color.White)
20. .margin({
21. top: 10
22. })
23. }
24. .justifyContent(FlexAlign.Start)
25. .alignItems(HorizontalAlign.Center)
26. .margin({
27. top: 15
28. })
29. }
30. }
```

## 反例

```
1. import hilog from '@ohos.hilog'
2. @Entry
3. @Component
4. struct MyComponent{
5. @State message: string = '';
6. build() {
7. Column() {
8. Button('点击打印日志')
9. .onClick(() => {
10. this.message = 'click';
11. for (let i = 0; i < 10; i++) {
12. hilog.info(0x0000, 'TAG', '%{public}s', this.message);
13. }
14. })
15. .width('90%')
16. .backgroundColor(Color.Blue)
17. .fontColor(Color.White)
18. .margin({
19. top: 10
20. })
21. }
22. .justifyContent(FlexAlign.Start)
23. .alignItems(HorizontalAlign.Center)
24. .margin({
25. top: 15
26. })
27. }
28. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
