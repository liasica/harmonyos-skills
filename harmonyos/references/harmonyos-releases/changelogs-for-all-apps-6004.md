---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-6004
title: OS平台API行为的变更
breadcrumb: 版本说明 > 更多版本 > 6.0.0(20) > OS平台能力 > OS平台行为变更说明 > 6.0.0(20) Beta5引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:39+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:f1bb54f7f80814391fb8d59b31a45d277e2d3f6e5cfefa03cba7abcc45ad83f6
---

## ArkTS

### 禁止在编译产物为JS的HAR包中使用注解

**变更原因**

应用开发中，在[release模式下构建](../harmonyos-guides/ide-hvigor-build-har.md#section19788284410)源码HAR，并同时[开启混淆](../harmonyos-guides/source-obfuscation.md)时，由于编译产物为JS文件，而在JS中没有注解的实现机制，因此会在编译过程中被移除，导致无法通过注解实现AOP插桩。

为避免因此引起的功能异常，禁止在JS HAR(编译产物中存在JS的HAR包)中使用注解。

**变更影响**

此变更涉及应用适配。

变更前：构建JS HAR时，若代码中存在注解，编译不会报错。

如下代码在JS形态的HAR包中编译时不会报错。

```ts
// test.ets
@interface ClassAuthor {
  authorName: string
}

@ClassAuthor({authorName: "Bob"})
class MyClass {
  /* body */
}
```

变更后：构建JS HAR时，若代码中存在注解，编译会报错。

**起始API Level**

不涉及

**变更的接口/组件**

不涉及

**适配指导**

删除JS HAR中的注解声明和调用，或者重新编译成其他形态的HAR包，例如[字节码HAR](../harmonyos-guides/ide-hvigor-build-har.md#section16598338112415)。
