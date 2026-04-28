---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-state-variable-usage-in-ui-format-check
title: @performance/state-variable-usage-in-ui-format-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/state-variable-usage-in-ui-format-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:300fbcc76fb2dcac78f796ac9d6fbe8f80510c757ccae195939118e5914c41d7
---

建议删除不使用的UI变量。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/state-variable-usage-in-ui-format-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. class User {
2. private name: string;
3. constructor(name: string) {
4. this.name = name;
5. }
6. }

8. @Entry({ storage: new LocalStorage() })
9. @Component
10. struct Parent {
11. @Prop  prop: number = 1;
12. @State state: string = '1';
13. @State state1: User = new User('name');
14. @StorageLink(`k1`) storageLink: number = 1;
15. @StorageProp(`k1`) storageProp: number = 1;
16. @LocalStorageLink(`k1`) localStorageLink: number = 1;
17. @LocalStorageProp(`k1`) localStorageProp: number = 1;
18. @Provide('k1') provide: string = "hell";
19. build() {
20. Column() {
21. Button() {
22. Text('Insert a new item after item 1').fontSize(30)
23. }

25. Text(`${this.prop}`)
26. Text(`${this.state}`)
27. Text(`${this.state1}`)
28. Text(`${this.storageLink}`)
29. Text(`${this.storageProp}`)
30. Text(`${this.localStorageLink}`)
31. Text(`${this.localStorageProp}`)
32. Text(`${this.provide}`)
33. }
34. .justifyContent(FlexAlign.Center)
35. .width('100%')
36. .height('100%')
37. .backgroundColor(0xF1F3F5)
38. }
39. }
```

## 反例

```
1. class User {
2. private name: string;
3. constructor(name: string) {
4. this.name = name;
5. }
6. }

8. @Entry({ storage: new LocalStorage() })
9. @Component
10. struct Parent {
11. @Prop  prop: number = 1;
12. @State state: string = '1';
13. @State state1: User = new User('name');
14. @StorageLink(`k1`) storageLink: number = 1;
15. @StorageProp(`k1`) storageProp: number = 1;
16. @LocalStorageLink(`k1`) localStorageLink: number = 1;
17. @LocalStorageProp(`k1`) localStorageProp: number = 1;
18. @Provide('k1') provide: string = "hell";
19. build() {
20. Column() {
21. Button() {
22. Text('Insert a new item after item 1').fontSize(30)
23. }

25. Text(`${this.prop}`)
26. Text(`${this.state}`)
27. }
28. .justifyContent(FlexAlign.Center)
29. .width('100%')
30. .height('100%')
31. .backgroundColor(0xF1F3F5)
32. }
33. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
