---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-229
title: "使用BuilderParam在父组件调用this的方法报错：Error message: undefined is not callable"
breadcrumb: "FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用BuilderParam在父组件调用this的方法报错：Error message: undefined is not callable"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4a8f3aa90162cfebb9e2922a9530e5e86fc397c1e6028c45a4f88733a84afb05
---

**问题场景**

在子组件Child中使用@BuilderParam参数时，如果在父组件中将父组件的builder函数传递给子组件，并在builder函数中调用父组件的方法，可能会出现Error message: undefined is not callable的错误。

问题代码如下：

```typescript
@Component
struct Child {
  @Builder
  FunABuilder0() {};

  @BuilderParam aBuilder0: () => void = this.FunABuilder0;

  build() {
    Column() {
      this.aBuilder0()
    }
  }
}

@Entry
@Component
struct Parent {
  @Builder
  componentBuilder() {
    Text('Parent builder')
      .onClick(() => {
        this.test1();
      })
  }

  test1(): void {
    console.info('test1');
  }

  build() {
    Column() {
      Child({ aBuilder0: this.componentBuilder })
    }
  }
}
```

**解决方案**

在JavaScript中调用this时，需要注意this的指向。当前代码在子组件中声明builder方法时，this指向的是父组件。而@Builder componentBuilder()通过this.componentBuilder的形式传给子组件@BuilderParam customBuilderParam，此时this指向的是子组件Child的label，即 “Child”。因此，在点击事件响应时，this指向的是Child，而Child中没有test1()方法，从而导致 JavaScript 错误。

为了解决这个问题，需要在父组件中声明子组件时，通过监听函数将 `this` 传递到子组件。应改为：

```typescript
Child({
  aBuilder0: () => {
    this.componentBuilder()
  }
})
```

**参考链接**

[@BuilderParam装饰器：引用@Builder函数](../harmonyos-guides/arkts-builderparam.md)
