---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-v1-nested-object-property-change-format-check
title: "@correctness/v1-nested-object-property-change-format-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/v1-nested-object-property-change-format-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f6ae5e26166e47cb35cbbd9c111316b990ce558c171d175acb03216d4105dcba
---

建议不要直接修改普通V1状态变量中嵌套对象的属性，应使用@Observed/@ObjectLink来观察嵌套对象的属性更改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/v1-nested-object-property-change-format-check": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
class Parent {
  parentId: number;
  constructor(parentId: number) {
    this.parentId = parentId;
  }
  getParentId(): number {
    return this.parentId;
  }
  setParentId(parentId: number): void {
    this.parentId = parentId;
  }
}
@Observed
class Child {
  childId: number;
  constructor(childId: number) {
    this.childId = childId;
  }
  getChildId(): number {
    return this.childId;
  }
  setChildId(childId: number): void {
    this.childId = childId;
  }
}
class Cousin extends Parent {
  cousinId: number = 47;
  child: Child;
  constructor(parentId: number, cousinId: number, childId: number) {
    super(parentId);
    this.cousinId = cousinId;
    this.child = new Child(childId);
  }
  getCousinId(): number {
    return this.cousinId;
  }
  setCousinId(cousinId: number): void {
    this.cousinId = cousinId;
  }
  getChild(): number {
    return this.child.getChildId();
  }
  setChild(childId: number): void {
    return this.child.setChildId(childId);
  }
}
@Component
struct ViewChild {
  @ObjectLink child: Child;
  build() {
    Column({ space: 10 }) {
      Text(`childId: ${this.child.getChildId()}`)
      Button('Change childId')
        .onClick(() => {
          this.child.setChildId(this.child.getChildId() + 1);
        })
    }
  }
}
@Entry
@Component
struct MyView {
  @State cousin: Cousin = new Cousin(10, 20, 30);
  build() {
    Column({ space: 10 }) {
      Text(`parentId: ${this.cousin.parentId}`)
      Button('Change Parent.parentId')
        .onClick(() => {
          this.cousin.parentId += 1;
        })
      Text(`cousinId: ${this.cousin.cousinId}`)
      Button('Change Cousin.cousinId')
        .onClick(() => {
          this.cousin.cousinId += 1;
        })
      ViewChild({ child: this.cousin.child }) // Text(`childId: ${this.cousin.child.childId}`)的替代写法
      Button('Change Cousin.Child.childId')
        .onClick(() => {
          this.cousin.child.childId += 1;
        })
    }
  }
}
```

## 反例

```screen
class Parent {
  parentId: number;
  constructor(parentId: number) {
    this.parentId = parentId;
  }
  getParentId(): number {
    return this.parentId;
  }
  setParentId(parentId: number): void {
    this.parentId = parentId;
  }
}
class Child {
  childId: number;
  constructor(childId: number) {
    this.childId = childId;
  }
  getChildId(): number {
    return this.childId;
  }
  setChildId(childId: number): void {
    this.childId = childId;
  }
}
class Cousin extends Parent {
  cousinId: number = 47;
  child: Child;
  constructor(parentId: number, cousinId: number, childId: number) {
    super(parentId);
    this.cousinId = cousinId;
    this.child = new Child(childId);
  }
  getCousinId(): number {
    return this.cousinId;
  }
  setCousinId(cousinId: number): void {
    this.cousinId = cousinId;
  }
  getChild(): number {
    return this.child.getChildId();
  }
  setChild(childId: number): void {
    return this.child.setChildId(childId);
  }
}
@Entry
@Component
struct MyView {
  @State cousin: Cousin = new Cousin(10, 20, 30);
  build() {
    Column({ space: 10 }) {
      Text(`parentId: ${this.cousin.parentId}`)
      Button('Change Parent.parent')
        .onClick(() => {
          this.cousin.parentId += 1;
        })
      Text(`cousinId: ${this.cousin.cousinId}`)
      Button('Change Cousin.cousinId')
        .onClick(() => {
          this.cousin.cousinId += 1;
        })
      Text(`childId: ${this.cousin.child.childId}`)
      Button('Change Cousin.Child.childId')
        .onClick(() => {
          // 点击时上面的Text组件不会刷新
          this.cousin.child.childId += 1;
        })
    }
  }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
