---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-mock
title: 预览数据模拟
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 预览数据模拟
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e3ec20b4328e305fae9ab6bf734dca921f9489aa3358b5f2b08f28c7b2b9f9b7
---

**说明** 

仅API 11及以上版本的Stage模型工程支持。

在预览场景中，由于代码的运行环境与真机设备上的运行环境不同，调用部分接口时无法获取到有效的返回值（例如获取电池电量信息等，在预览场景下batteryInfo.voltage返回的是一个固定的值0），这样开发者就无法在预览时查看到不同返回值带来的界面变化。因此，Hamock提供了预览场景的模拟功能，在不改变业务运行逻辑的同时，开发者可以模拟UI组件上的属性或方法，或模拟import的模块接口。

## 使用前提

使用Hamock在预览场景模拟，需要在工程或模块的oh-package.json5中添加该依赖，然后重新同步工程。

```json5
"devDependencies": {
    "@ohos/hamock": "1.0.0"
}
```

## UI组件上的Mock

Hamock提供了@MockSetup用于修饰Mock方法，仅支持声明式范式的组件。当开发者预览该组件时，预览运行时将在组件初始化时执行被@MockSetup修饰的方法。因此，开发者可以在这个被修饰的方法内重定义组件的方法或重赋值组件的属性，其将在预览时生效。

**说明** 

@MockSetup修饰的方法仅在预览场景会自动触发，并先于组件的aboutToAppear执行。

### UI组件的方法

1. 在ArkTS页面代码中引入Hamock。

   ```ts
   import { MockKit, when, MockSetup } from '@ohos/hamock';
   ```
2. 在目标组件中定义一个方法，并用@MockSetup修饰该方法。在这个方法中，使用MockKit模拟目标方法。

   ```ts
   import { MockKit, when, MockSetup } from '@ohos/hamock';

   @Entry
   @Component
   struct Index {
    ...
    @MockSetup
    randomName() {
     let mocker: MockKit = new MockKit();
     let mockfunc: Object = mocker.mockFunc(this, this.method1);
     // mock 指定的方法在指定入参的返回值
     when(mockfunc)('test').afterReturn(1);
    }
    ...
    // 业务场景调用方法
    const result = this.method1('test'); // in previewer, result = 1
   }
   ```

### UI组件的属性

1. 在ArkTS页面代码中引入Hamock。

   ```ts
   import { MockSetup } from '@ohos/hamock';
   ```
2. 在目标组件中定义一个方法，并用@MockSetup修饰该方法。在这个方法中，对于需要Mock的属性，可以重新赋值。

   ```ts
   import { MockSetup } from '@ohos/hamock';

   @Component
   struct Person {
    @Prop species: string;
    // 在@MockSetup片段中，定义对象属性
    @MockSetup
    randomName() {
     this.species = 'primates'
    }
    ...
    // 业务场景调用属性（如果从初始化到调用期间，该属性无变化）
    const result = this.species // in previewer, result = primates
   }
   ```

**说明** 

* ArkUI部分类型属性不支持Mock，如readonly、@ObjectLink。
* 被@Link/@Consume/@Prop/@BuilderParam装饰器修饰的变量，ArkUI语法要求父容器需要有对应属性的定义，因此更推荐开发者通过定义一个预览场景父容器（并通过父容器传递合适的数据）来预览这一类的组件。

## 模块的Mock

模块的Mock支持对系统模块、依赖模块及本地模块的Mock，通过新建ArkTS文件定义Mock实现代码，并在mock-config.json5配置文件中定义目标模块与Mock实现代码文件的映射关系。目标模块与Mock实现代码文件为一对一的关系，即对于同一目标模块，仅支持一份Mock实现代码，预览运行时，所有页面import目标模块都将指向这一份Mock实现代码。

### 系统模块/依赖的模块

1. 在src/mock目录下新建一个ArkTS文件，在这个文件内定义目标模块的Mock实现。

   ```ts
   // src/mock/MeasureText.mock.ets
   import MeasureText from '@ohos.measure'

   // 类的mock使用继承(extends)的方式实现
   class MockMeasureText extends MeasureText {
     // 定义mock实现
     static measureText(): number {
       console.log('Return value of the mock measureText function')
       return 100;
     }
   };

   export default MockMeasureText;
   ```

   **说明** 

   用户在对类定义Mock的实现时，建议使用继承(extends)的方式实现。若不使用继承，需要保证代码中使用到依赖模块的所有方法都重新定义Mock实现。
2. 在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的替换关系。该替换关系会在预览场景下生效。

   ```json5
   {
     "@ohos.measure": { // 待替换的moduleName
       "source": "src/mock/MeasureText.mock.ets" // Mock代码的路径，相对于模块根目录
     },
    ...
   }
   ```
3. 在原调用处中添加Hilog日志，方便在预览时，在Log中打印获取返回值，从而验证Mock是否生效。

   ```ts
   hilog.debug(DomainNumber, logTag, 'Mock %{public}s', `${MeasureText.measureText({textContent: 'Hello World'})}`)
   ```

### 本地模块

1. 在src/mock目录下新建一个ArkTS文件，在这个文件内定义目标模块的Mock实现。

   ```ts
   // src/mock/module/utils/CommonUtils.mock.ets
   // 导入本地模块
   import LibDefaultExport from '../../../main/ets/utils/CommonUtils'; // get origin default export
   import { methodA, ObjectB } from '../../../main/ets/utils/CommonUtils'; // get origin export on demand

   class DefaultExportMock extends LibDefaultExport {
     // 定义mock实现
     public static getName(): String {
       return "Mocked Name";
     }
   };

   // Mock methodA方法
   export const methodAMock = (): string => {
     return "methodA Mocked"
   }
   export {
     methodAMock as methodA,
     ObjectB,
   }

   export default DefaultExportMock;
   ```

   其中CommonUtils.ets文件示例如下：

   ```ts
   export default class CommonUtils {
     public static getName(): String {
       return "origin name";
     }

     public static getTitle(): String {
       return "origin title";
     }
   }

   export const methodA = (): string => {
     return "methodA"
   }

   export const ObjectB: Object = new Object();
   ```

   **说明** 

   本地模块的Mock仅支持src/main/ets目录下的ArkTS或TS文件。
2. 在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的替换关系。该替换关系会在预览场景下生效。

   ```json5
   {
    "utils/CommonUtils.ets": { // 本地模块只支持ets/xxx的相对路径，并需明确文件后缀
     "source": "src/mock/module/utils/CommonUtils.mock.ets"
    },
    ...
   }
   ```
3. 在原调用处中添加Hilog日志，方便在预览时，在Log中打印获取返回值，从而验证Mock是否生效。

   ```ts
   hilog.debug(DomainNumber, logTag, 'Mock %{public}s', CommonUtils.getName());
   ```
