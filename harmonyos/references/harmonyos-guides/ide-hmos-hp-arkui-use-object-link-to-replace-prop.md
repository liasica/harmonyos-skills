---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hp-arkui-use-object-link-to-replace-prop
title: "@performance/hp-arkui-use-object-link-to-replace-prop"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-object-link-to-replace-prop
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:587808c16ef077ee2fe4b36dd98290598f01ed05dc269b1e7d13ef0ef3d8917f
---

建议使用@ObjectLink代替@Prop减少不必要的深拷贝。

通用丢帧场景下，建议优先修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-object-link-to-replace-prop": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
@Observed
class ClassA {
  public c: number = 0;
  constructor(c: number) {
    this.c = c;
  }
}
@Component
struct PropChild {
  // @ObjectLink 装饰状态变量不会深拷贝
  // 当修饰为ObjectLink时 ClassA必须同时被Observed修饰
  @ObjectLink testNum: ClassA;
  build() {
    Text(`PropChild testNum ${this.testNum.c}`)
  }
}
@Entry
@Component
struct Parent {
  @State testNum: ClassA[] = [new ClassA(1)];
  build() {
    Column() {
      Text(`Parent testNum ${this.testNum[0].c}`)
        .onClick(() => {
          this.testNum[0].c += 1;
        })
      // 当子组件不需要发生本地改变时，优先使用@ObjectLink，因为@Prop是会深拷贝数据，具有拷贝的性能开销，所以这个时候@ObjectLink是比@Link和@Prop更优的选择
      PropChild({ testNum: this.testNum[0] })
    }
  }}
```

## 反例

```ts
@Observed
class ClassA {
  public c: number = 0;
  constructor(c: number) {
    this.c = c;
  }
}
@Component
struct PropChild {
  // @Prop 装饰状态变量会深拷贝
  @Prop testNum: ClassA;
  build() {
    Text(`PropChild testNum ${this.testNum.c}`)
  }
}
@Entry
@Component
struct Parent {
  @State testNum: ClassA[] = [new ClassA(1)];
  build() {
    Column() {
      Text(`Parent testNum ${this.testNum[0].c}`)
        .onClick(() => {
          this.testNum[0].c += 1;
        })
      // PropChild没有改变@Prop testNum: ClassA的值，所以这时最优的选择是使用@ObjectLink
      PropChild({ testNum: this.testNum[0] })
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
