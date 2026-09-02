---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1113
title: 如何深度观测反序列化和未被@Observed/@ObservedV2装饰的对象
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何深度观测反序列化和未被@Observed/@ObservedV2装饰的对象
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e388a9a4915c828d811a97aeb1af841f7952f3b753ce6faab0419de6eeda0ef7
---

## 问题现象

场景一：JSON字符串使用JSON.parse转换为对象，该对象为嵌套类型的对象，直接修改该对象的属性时，无法刷新页面。

场景二：被@Sendable装饰器装饰的多线程共享数据等未被@Observed/@ObservedV2装饰器装饰的嵌套对象，无法刷新页面。

场景三：collections类型数据无法刷新页面。

## 背景知识

状态管理V2版本可以用[UIUtils.makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)，状态管理V1版本API19以后可以用[UIUtils.makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)实现对未被@Observed/@ObservedV2装饰的对象、系统返回的对象、interface等数据的深度监听。适用情况可参考官网[makeObserved概述](../harmonyos-guides/arkts-new-makeobserved.md#概述)：

1. class的定义在三方包中：开发者无法手动对class中需要观察的属性加上@Trace标签，可以使用makeObserved使得当前对象可以被观察。
2. 当前类的成员属性不能被修改：因为@Trace观察类属性会动态修改类的属性，这个行为在@Sendable装饰的class中是不被允许的，此时可以使用makeObserved（@Sendable装饰的类型不支持makeV1Observed）。
3. interface或者JSON.parse返回的匿名对象：这类场景往往没有明确的class声明，开发者无法使用@Trace标记当前属性可以被观察，此时可以使用makeObserved。

相较于UIUtils.makeObserved的[限制条件](../harmonyos-guides/arkts-new-makeobserved.md#限制条件)，UIUtils.makeV1Observed限制条件可参考官网链接：[makeV1Observed概述与限制条件](../harmonyos-guides/arkts-v1-v2-mixusage.md#makev1observed)。

## 解决方案

| 场景 | 问题现象 | 解决方案 |
| --- | --- | --- |
| 场景一 | JSON字符串使用JSON.parse转换为对象，该对象为嵌套类型的对象，直接修改该对象的属性时，无法刷新页面。 | 1. 方案一：参考[makeObserved的入参为JSON.parse的返回值](../harmonyos-guides/arkts-new-makeobserved.md#makeobserved的入参为jsonparse的返回值)，可以将未使用new创建的对象转化为可深度观测的对象。 2. 方案二：状态管理V1可以使用makeV1Observed方法代替@Observed装饰器，该方案下即使不是通过new创建的也可以进行深度观测。 |
| 场景二 | 被@Sendable装饰器装饰的多线程共享数据等未被@Observed/@ObservedV2装饰器装饰的嵌套对象，无法刷新页面。 | 1. 方案一：参考[makeObserved和@Sendable装饰的class配合使用](../harmonyos-guides/arkts-new-makeobserved.md#makeobserved和sendable装饰的class配合使用)，可以实现在子线程做大数据处理，在UI线程做ViewModel的显示和观察数据的需求。 2. 方案二：将@Sendable数据与深度观测的数据分开管理。 |
| 场景三 | collections类型数据无法刷新页面。 | 详情可参考官方文档：[makeObserved和collections.Array/Set/Map配合使用](../harmonyos-guides/arkts-new-makeobserved.md#makeobserved和collectionsarraysetmap配合使用)。 |

### 场景一

JSON字符串使用JSON.parse转换为对象，该对象为嵌套类型的对象，直接修改该对象的属性时，无法刷新页面。

* 方案一：参考[makeObserved的入参为JSON.parse的返回值](../harmonyos-guides/arkts-new-makeobserved.md#makeobserved的入参为jsonparse的返回值)，可以将未使用new创建的对象转化为可深度观测的对象。
* 方案二：状态管理V1可以使用makeV1Observed方法代替@Observed装饰器，该方案下即使不是通过new创建的也可以进行深度观测。每一层嵌套对象需要单独使用makeV1Observed方法进行转化，并且每一层嵌套对象需要封装在一个子组件中并用@ObjectLink接收。完整示例参考如下：

  ```ts
  import { UIUtils } from '@kit.ArkUI';

  class Father {
    name: string;
    age: number;
    id: string;

    constructor(name: string, age: number, id: string) {
      this.name = name;
      this.age = age;
      this.id = id;
    }
  }

  class Son extends Father {
    father: Father;

    constructor(name: string, age: number, id: string, father: Father) {
      super(name, age, id);
      this.father = father;
    };
  }

  const sonObj: string = `[
    {
      "name": "mick",
      "age": 15,
      "id": "01001",
      "father": {
        "name": "jack",
        "age": 45,
        "id": "01002"
      }
    },
    {
      "name": "stew",
      "age": 17,
      "id": "02001",
      "father": {
        "name": "stan",
        "age": 39,
        "id": "02002"
      }
    }
  ]`;

  @Entry
  @Component
  struct SceneOneOptionTwo {
    @State sonArr: Son[] = JSON.parse(sonObj) as Son[]; // 未通过new的方式构造实例

    aboutToAppear(): void {
      // makeV1Observed不会递归执行，仅会将第一层包装成V1的状态变量，需要手动递归。
      for (let i = 0; i < this.sonArr.length; i++) {
        this.sonArr[i] = UIUtils.makeV1Observed(this.sonArr[i]);
        this.sonArr[i].father = UIUtils.makeV1Observed(this.sonArr[i].father);
      }
    }

    build() {
      Column() {
        ForEach(this.sonArr, (item: Son) => {
          SceneOneOptionTwoSon({ son: item });
          Blank()
            .height(50);
        });
      }
      .height('100%')
      .width('100%');
    }
  }

  @Component
  struct SceneOneOptionTwoSon {
    @ObjectLink son: Son;

    build() {
      Column() {
        Text(`${this.son.name}`)
          .fontSize($r('app.float.page_text_font_size'))
          .onClick(() => {
            this.son.name += '1';
          });
        SceneOneOptionTwoFather({ father: this.son.father });
      };
    }
  }

  @Component
  struct SceneOneOptionTwoFather {
    @ObjectLink father: Father;

    build() {
      Column() {
        Text(`${this.father.name}`)
          .fontSize($r('app.float.page_text_font_size'))
          .onClick(() => {
            this.father.name += '2';
          });
      };
    }
  }
  ```

### 场景二

被@Sendable装饰器装饰的多线程共享数据无法被@Observed/@ObservedV2装饰器装饰，无法刷新页面。

* 方案一：参考[makeObserved和@Sendable装饰的class配合使用](../harmonyos-guides/arkts-new-makeobserved.md#makeobserved和sendable装饰的class配合使用)，可以实现在子线程做大数据处理，在UI线程做ViewModel的显示和观察数据的需求。

  **说明** 

  数据的构建和处理可以在子线程中完成，但有观察能力的数据不能传给子线程，只有在主线程里才可以操作可观察的数据。

  makeObserved的返回值不可直接传给子线程。
* 方案二：将@Sendable数据与深度观测的数据分开管理。以状态管理V2为例，分别创建两个相同属性的类，一个采用@Sendable装饰，用于并发数据传递，另一个采用@ObservedV2装饰，用于UI刷新。完整示例代码如下：

  ```ts
  @Sendable
  export class StockData {
    public name: string;
    public code: string;

    constructor(name: string, code: string) {
      this.name = name;
      this.code = code;
    }
  }

  @ObservedV2
  export class StockViewModel {
    @Trace name: string = '';
    @Trace code: string = '';

    /* 一次性批量更新，避免多次触发 */
    updateFrom(data: StockData) {
      this.name = data.name;
      this.code = data.code;
    }

    /*监听多个字段变化 */
    @Monitor('name', 'code')
    onStockChanged() {
      console.info(`股票变更: ${this.name} ${this.code}`); // 这里可以触发额外业务逻辑，比如重新请求详情接口
    }
  }

  @Entry
  @ComponentV2
  struct SceneTwoOptionTwo {
    @Local view1: StockViewModel = new StockViewModel();

    build() {
      Column() {
        Text(`方案一：${this.view1.name}`);
        Button('Sendable对象更新到ObservedV2对象上')
          .onClick(() => {
            // 直接改即可，响应式照常工作
            this.view1.updateFrom(new StockData('HK', '00700'));
          });
        Button('修改ObservedV2对象刷新UI')
          .onClick(() => {
            this.view1.name += 'HK';
          });
      };
    }
  }
  ```

### 场景三

详情可参考官方文档：[makeObserved和collections.Array/Set/Map配合使用](../harmonyos-guides/arkts-new-makeobserved.md#makeobserved和collectionsarraysetmap配合使用)。

## 常见FAQ

Q：场景一中是否还有其它方案能避免JSON.parse转换的对象无法深度观测的问题？

A：可以使用三方库[class-transformer-arkts](https://ohpm.openharmony.cn/#/cn/detail/class-transformer-arkts)进行转换。

Q：UIUtils.makeObserved将对象变为可观察数据后，可观察多深层的数据改动？

A：UIUtils.makeObserved能递归代理所有层级的属性变化，确保任何深度的数据修改（如：objA.b.c.d=newValue）都能被检测并驱动UI更新。

## 总结

根据以上背景知识与常见场景，makeObserved与makeV1Observed的使用限制与对比如下：

| 场景 | makeObserved | makeV1Observed |
| --- | --- | --- |
| 状态管理版本 | 状态管理V2 | 状态管理V1 |
| 观测深度 | 自动递归代理所有层级的属性变化。 | 代理一层的属性变化，若需要代理所有深度需要手动递归。需要搭配@ObjectLink一起使用。 |
| 支持的数据类型 | JSON.parse返回的Object、Array、Map、Set、Date、collections.Array、collections.Set、collections.Map、@Sendable装饰的类、未被@Observed或@ObservedV2装饰的类等。 | 普通的class、Array、Map、Set、Date等。 |
| 不支持的数据类型 | undefined、null和非Object类型。 | collections类型、@Sendable装饰的class、非object类型、undefined、null以及被@ObservedV2、makeObserved的返回值和V2装饰器装饰的built-in类型的变量（Array、Map、Set和Date）。 |

根据以上的使用限制，makeV1Observed相较于makeObserved存在较大的局限性，同时由于转换后的数据是不同的状态管理版本，使用时需要注意状态管理版本之间的混用规则等问题。
