---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-78
title: 如何在ArkTS中实现自定义装饰器能力
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在ArkTS中实现自定义装饰器能力
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3ba4ad05e148ab6660cdaba76e346b68f13624635df9a0d5799e71cb0dc25117
---

ArkTS支持TS5.0之前（如TS4.x及以下版本）的TS装饰器语法。关于装饰器的定义和运行时行为，可以参考[TS官方文档](https://www.typescriptlang.org/docs/handbook/decorators.html)。

注意，如果在.ets文件中定义装饰器，则需要同时满足[从TypeScript到ArkTS的适配规则](../harmonyos-guides/typescript-to-arkts-migration-guide.md)，比如不能使用any等。

参考代码如下：

```ts
function MyDescriptor(target: Object, key: string, descriptor: PropertyDescriptor) {
  const originalMethod: Function = descriptor.value
  descriptor.value = (...args: Object[]) => {
    // Get the name, input parameters, and return value of the decorated method
    console.log(`Calling ${target.constructor?.name} method ${key} with argument: ${args}`)
    const result: Object = originalMethod(...args)
    console.log(`Method ${key} returned: ${result}`)
    return result
  }
  return descriptor
}

@Entry
@Component
export struct MyDescriptorCom {
  @State message: string = 'Hello World';

  @MyDescriptor
  demoFunc(str: string) {
    return str
  }

  aboutToAppear(): void {
    this.demoFunc('DemoTest')
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**说明** 

由于ArkTS当前运行时限制，当前版本暂不支持同时应用多个自定义装饰器。
