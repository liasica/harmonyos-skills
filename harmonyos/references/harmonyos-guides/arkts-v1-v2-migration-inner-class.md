---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-class
title: 数据对象状态变量迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > 数据对象状态变量迁移
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4300009b1459eb5a02e5291e7fac8eb28fb064875127d000d0dce3cd05637b57
---

本文档主要介绍数据对象内的状态变量的迁移场景，包含以下场景：

| V1装饰器名 | V2装饰器名 |
| --- | --- |
| [@ObjectLink](arkts-observed-and-objectlink.md)/[@Observed](arkts-observed-and-objectlink.md) /[@Track](arkts-track.md) | [@ObservedV2](arkts-new-observedv2-and-trace.md)/[@Trace](arkts-new-observedv2-and-trace.md) |

## 各装饰器迁移示例

### @ObjectLink/@Observed/@Track -> @ObservedV2/@Trace

**迁移规则**

在V1中，@Observed与@ObjectLink装饰器用于观察类对象及其嵌套属性的变化，但V1只能观察对象的第一层属性。嵌套对象的属性需要通过自定义组件和@ObjectLink观察。此外，V1中提供了@Track装饰器实现对属性级别变化的精确控制。

在V2中，结合使用@ObservedV2和@Trace，可以高效实现类对象及其嵌套属性的深度观察，省去对自定义组件的依赖，简化开发流程。同时，@Trace装饰器具备精确更新能力，替代V1中的@Track，实现更高效的UI刷新控制。根据不同场景，有以下迁移策略：

* 嵌套对象的属性观察：V1中需要通过自定义组件和@ObjectLink观察嵌套属性，V2中则可以使用@ObservedV2和@Trace直接观察嵌套对象，简化了代码结构。
* 类属性的精确更新：V1中的@Track可以用V2中的@Trace取代，@Trace可以同时观察和精确更新属性变化，使代码更简洁高效。

**示例**

**嵌套对象属性观察方法**

在V1中，无法直接观察嵌套对象的属性变化，只能观察到第一层属性的变化。必须通过创建自定义组件并使用@ObjectLink来实现对嵌套属性的观察。V2中使用@ObservedV2和@Trace，可以直接对嵌套对象的属性进行深度观察，减少复杂度。

V1实现：

```typescript
@Observed
class Address {
  public city: string;

  constructor(city: string) {
    this.city = city;
  }
}

@Observed
class User {
  public name: string;
  public address: Address;

  constructor(name: string, address: Address) {
    this.name = name;
    this.address = address;
  }
}

@Component
struct AddressView {
  // 子组件中@ObjectLink装饰的address从父组件初始化，接收被@Observed装饰的Address实例
  @ObjectLink address: Address;

  build() {
    Column() {
      Text(`City: ${this.address.city}`)
      Button('city +a')
        .onClick(() => {
          this.address.city += 'a';
        })
    }
  }
}

@Entry
@Component
struct UserProfile {
  @State user: User = new User('Alice', new Address('New York'));

  build() {
    Column() {
      Text(`Name: ${this.user.name}`)
      // 无法直接观察嵌套对象的属性变化，例如this.user.address.city
      // 只能观察到对象第一层属性变化，所以需要将嵌套的对象Address抽取到自定义组件AddressView
      AddressView({ address: this.user.address })
    }
  }
}
```

V2迁移策略：使用@ObservedV2和@Trace。

```typescript
@ObservedV2
class Address {
  @Trace public city: string;

  constructor(city: string) {
    this.city = city;
  }
}

@ObservedV2
class User {
  @Trace public name: string;
  @Trace public address: Address;

  constructor(name: string, address: Address) {
    this.name = name;
    this.address = address;
  }
}

@Entry
@ComponentV2
struct UserProfile {
  @Local user: User = new User('Alice', new Address('New York'));

  build() {
    Column() {
      Text(`Name: ${this.user.name}`)
      // 通过@ObservedV2和@Trace可以直接观察嵌套属性
      Text(`City: ${this.user.address.city}`)
      Button('city +a')
        .onClick(() => {
          this.user.address.city += 'a';
        })
    }
  }
}
```

**类属性变化观测**

在V1中，@Observed用于观察类实例及其属性的变化，@Track用于类对象的属性级的观察。在V2中，@Trace实现了观察和更新属性级别变化的能力，搭配@ObservedV2实现高效的UI更新。

V1实现：

```typescript
@Observed
class User {
  @Track public name: string;
  @Track public age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

@Entry
@Component
struct UserProfile {
  @State user: User = new User('Alice', 30);

  build() {
    Column() {
      Text(`Name: ${this.user.name}`)
      Text(`Age: ${this.user.age}`)
      // 点击Button更新user.age，触发UI刷新
      Button('increase age')
        .onClick(() => {
          this.user.age++;
        })
    }
  }
}
```

V2迁移策略：使用@ObservedV2和@Trace。

```typescript
// V2使用@ObservedV2代替V1的@Observed
@ObservedV2
class User {
  // V2使用@Trace代替V1的@Track
  @Trace public name: string;
  @Trace public age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

@Entry
@ComponentV2
struct UserProfile {
  @Local user: User = new User('Alice', 30);

  build() {
    Column() {
      Text(`Name: ${this.user.name}`)
      Text(`Age: ${this.user.age}`)
      Button('Increase age')
        .onClick(() => {
          this.user.age++;
        })
    }
  }
}
```
