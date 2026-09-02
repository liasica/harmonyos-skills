---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-previewchecker
title: PreviewChecker检测规则
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > PreviewChecker检测规则
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:362203c293f802b9e0f71aebe2822baf01d23093bee5a735707b980a3cbde360
---

DevEco Studio启动预览时将执行PreviewChecker，检测通过后才可进行预览，以确保在使用预览器前识别到已知的不支持预览的场景，若存在不支持预览的场景，将给出优化提示，以便于开发者根据提示的建议进行代码优化。

## @previewer/mandatory-default-value-for-local-initialization

对于所有将被预览到的组件，如果组件的属性支持本地初始化，则都应当设置一个合法的不依赖运行时的默认值，以确保异常调用到该组件时，即使入参不完整，也能正常运行渲染。

**反例**

```ts
@Entry
@Component
struct Index {
  message?: string;
  @BuilderParam myBuilder: () => void;

  build() {
    Row() {
      Column() {
        Text(this.message)
        this.myBuilder()
      }
    }
  }
}
```

**正例**

```ts
@Builder function MyBuilderFunction(): void {}

@Entry
@Component
struct Index {
  message?: string = 'message';
  @Provide messageA: string = 'messageA';
  @StorageLink('varA') varA: number = 2;
  @StorageProp('languageCode') lang: string = 'en';
  @LocalStorageLink('PropA') storageLink1: number = 1;
  @LocalStorageProp('PropB') storageLink2: number = 2;
  @BuilderParam myBuilder: () => void = MyBuilderFunction;

  build() {
    Row() {
      Column() {
        Text(this.message)
        this.myBuilder()
      }
    }
  }
}
```

## @previewer/no-unallowed-decorator-on-root-component

不允许直接预览包含@Consume、@Link、@ObjectLink、@Prop等装饰器的子组件；建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件，并预览此父组件来查看子组件的预览效果。

**反例**

```ts
@Preview
@Component
struct LinkSample {
  @Link message: string;

  build() {
    Row() {
      Text(this.message)
    }
  }
}
```

**正例**

```ts
@Entry
@Component
struct LinkSampleContainer {
  @State message: string = 'Hello World';

  build() {
    Row() {
      LinkSample({message: this.message})
    }
  }
}
 
@Component
struct LinkSample {
  @Link message: string;

  build() {
    Row() {
      Text(this.message)
    }
  }
}
```

## @previewer/paired-use-of-consume-and-provide

如果缺少@Provide定义，@Consume组件在预览时将无法获取有效值。

API 19及以前，@Consume装饰的变量不支持设置默认值，建议被@Consume修饰的组件的祖先组件上应当有对应的@Provide属性，并且该属性应当有合法的不依赖运行时的默认值。

从API 20开始，@Consume装饰的变量支持设置默认值，建议优先对@Consume装饰的变量设置默认值，或者按照API 19及以前版本的方式进行设置。

**反例**

```ts
@Entry
@Component
struct Parent {
  build() {
    Column() {
      Child()
    }
  }
}
 
@Component
struct Child {
  @Consume message: string;
 
  build() {
    Text(this.message)
  }
}
```

**正例**一

```ts
// API 20及以上推荐此方式
@Entry
@Component
struct Parent {
  @Consume message: string = 'hello world';
  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
    }
  }
}
```

**正例二**

```ts
// 所有版本均可使用此方式
@Entry
@Component
struct Parent {
  @Provide message: string = 'hello world';
 
  build() {
    Column() {
      Child()
    }
  }
}
 
@Component
struct Child {
  @Consume message: string;
 
  build() {
    Text(this.message)
  }
}
```

## @previewer/no-page-method-on-preview-component

@Preview通常修饰在组件上，而非@Entry的页面入口。onPageShow、onPageHide、onBackPress仅在@Entry组件上生效。因此禁止在非路由组件上实例化onPageShow等页面级方法。

**反例**

```ts
@Preview
@Component
struct Index {
  @State message: string = 'Hello World';

  onPageShow(): void {}
  onPageHide(): void {}
  onBackPress(): void {}

  build() {
    Column() {
      Text(this.message)
    }
  }
}
```

**正例**

```ts
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  onPageShow(): void {}
  onPageHide(): void {}
  onBackPress(): void {}

  build() {
    Column() {
      Text(this.message)
    }
  }
}
```

## @previewer/no-page-import-unmocked-hsp

由于能力缺失，预览器无法确保HSP是可以正常运行的。界面代码调用HSP可能会在预览运行时无法按预期执行，未正确初始化的接口调用可能会导致运行异常，从而影响界面渲染结果。建议待预览的组件及其依赖的组件避免引用HSP，或为该HSP设置Mock实现，更多关于Mock实现的介绍请参考[预览数据模拟](ide-previewer-mock.md)。

**反例**

```ts
import { add } from 'library'; // 该模块未配置自定义mock。

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Text(this.message)
        .onClick(() => add(1, 2))
    }
  }
}
```

**正例**

```ts
import { add } from 'library'; // 该模块已配置自定义mock，配置方法见下文。

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Text(this.message)
        .onClick(() => add(1, 2))
    }
  }
}
```

自定义mock配置：

```json5
// src/mock/mock-config.json5
{
  "library": {
    "source": "src/mock/myhsp.mock.ets"
  },
}
```

```ts
// src/mock/myhsp.mock.ets
export function add(a: number, b: number): number {
  return a + b;
}
```
