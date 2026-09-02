---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-env-property
title: "@CustomEnv：自定义环境变量"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 响应式环境变量 > @CustomEnv：自定义环境变量
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9fa2a74672acbe3590b2bb108e849885a20c5b5e8fe0439a5428638c1b10b188
---

用于获取自定义环境变量。

开发者指南见：[@CustomEnv开发者指南](../harmonyos-guides/arkts-custom-env-property.md)。

**起始版本：** 26.0.0

## @CustomEnv

CustomEnv<T>(key: CustomEnvKey<T>): PropertyDecorator

@CustomEnv装饰器用于获取自定义环境变量，通过[CustomEnvKey.create()](ts-custom-env-property.md#createt)创建自定义环境变量Key，作为参数传入@CustomEnv装饰器。

@CustomEnv装饰的变量会读取该Key对应的环境变量值；若该环境变量未设置，则使用本地声明的默认值。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | CustomEnvKey<T> | 是 | 自定义环境变量Key，用于标识要获取的自定义环境变量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器，开发者无需关注该返回值。 |

**示例：**

```typescript
const custom = CustomEnvKey.create<string>();

@Entry
@Component
struct Index {
  // @CustomEnv装饰的变量设置本地默认值
  @CustomEnv(custom) customVarName: string = 'hello world';

  build() {
    Column() {
      Text(`${this.customVarName}`)
    }
  }
}
```

## CustomEnvKey<S>

自定义环境变量的Key的类型。

### 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | S | 否 | 是 | 自定义环境变量Key的类型。 |

### create<T>

static create<T>(): CustomEnvKey<T>

创建一个自定义环境变量Key，作为@CustomEnv装饰器的参数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CustomEnvKey<T>](ts-custom-env-property.md#customenvkeys) | 自定义环境变量Key，用于标识要获取的自定义环境变量。 |

**示例：**

```typescript
const customKey = CustomEnvKey.create<string>();
```

### constructor

protected constructor()

用于创建该类的实例对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
