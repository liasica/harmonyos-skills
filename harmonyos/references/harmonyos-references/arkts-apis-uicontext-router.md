---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router
title: Class (Router)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (Router)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99b07f82350814e0b8d95bd7f44bd20a97558b594078c0edbcd4abb1a8cc8491
---

提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。Router还支持命名路由跳转、页面栈管理、参数传递、返回确认对话框等能力，适用于需要统一管理页面导航流程、处理页面间数据传递的场景，与UIContext集成使用可实现灵活的路由控制。

Router基于页面栈机制管理页面导航，页面栈支持的最大容量为32个页面。当调用pushUrl时，目标页面会被压入栈顶；调用replaceUrl时，当前页面会被弹出栈并销毁，目标页面压入栈顶；调用back时，栈顶页面会被弹出。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 本模块接口仅可在Stage模型下使用。
* 以下API需先使用UIContext中的[getRouter()](arkts-apis-uicontext-uicontext.md#getrouter)方法获取到Router对象，再通过该对象调用对应方法。
* Router提供了以下两种路由方式：

  + **普通路由**（[pushUrl](arkts-apis-uicontext-router.md#pushurl)/[replaceUrl](arkts-apis-uicontext-router.md#replaceurl)）：通过url路径标识目标页面，适用于简单的页面跳转场景。
  + **命名路由**（[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute)/[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute)）：通过name标识目标页面，在跳转之前需要将目标跳转页面通过import将页面进行加载，适用于跨包跳转场景。

  建议在页面路径可能变化或需要统一管理路由的场景下使用命名路由，其他场景使用普通路由。根据是否需要返回上一页来选择使用哪个方法。

## pushUrl

pushUrl(options: router.RouterOptions): Promise<void>

跳转到应用内的指定页面，使用Promise异步回调。

**说明** 

pushUrl()会在页面栈顶部添加新页面，页面栈深度+1（上限32页，超限报错误码100003），后续可调用back()返回到上一页面或调用replaceUrl()替换当前页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息，包含url（目标页面路径）和params（传递的参数）等字段。  **说明：**  页面栈最大支持32个页面，建议跳转前通过[getStackSize](arkts-apis-uicontext-router.md#getstacksize23)（从API version 23开始支持）检查当前栈大小，避免超出限制导致跳转失败（错误码100003）。API version 23之前可使用[getLength](arkts-apis-uicontext-router.md#getlengthdeprecated)检查。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义传递参数的内部类
class InnerParams {
  array: number[];

  constructor(tuple: number[]) {
    this.array = tuple;
  }
}

// 定义路由参数类
class RouterParams {
  data: InnerParams;

  constructor(tuple: number[]) {
    this.data = new InnerParams(tuple);
  }
}

@Entry
@Component
struct Index {
  async routePage() {
    let options: router.RouterOptions = {
      url: 'pages/second',  // 跳转目标页面路径
      params: new RouterParams([12, 45, 78])  // 传递的页面参数
    }
    this.getUIContext()
      .getRouter()
      .pushUrl(options)
      .then(() => {
        console.info('pushUrl success');
      })
      .catch((err: ESObject) => {
        console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('First Page')
      Button('Next page')
        .type(ButtonType.Capsule)
        .margin({ top: 20 })
        .onClick(() => {
          this.routePage()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```ts
// 在second页面中接收传递过来的参数
class InnerParams {
  array: number[];

  constructor(tuple: number[]) {
    this.array = tuple;
  }
}

class RouterParams {
  data: InnerParams;

  constructor(tuple: number[]) {
    this.data = new InnerParams(tuple);
  }
}

@Entry
@Component
struct Second {
  @State data: object = (this.getUIContext().getRouter().getParams() as RouterParams).data;
  @State secondData: string = '';

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('Second Page')
      Button('Back')
        .fontSize(30)
        .onClick(() => {
          try {
            // 开启返回询问对话框
            this.getUIContext().getRouter().showAlertBeforeBackPage({ message: 'Are you sure to return?' })
          } catch (error) {
            // TODO: Implement error handling.
          }
          this.getUIContext().getRouter().back()
        })
        .margin({ top: 20 })
      Button(`The value on the first page：${this.secondData}`)
        .margin({ top: 20 })
        .onClick(()=> {
          this.secondData = (this.data['array'][1]).toString();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## pushUrl

pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 页面跳转结果回调函数。  当页面跳转成功时，error为undefined。当页面跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    // 调用pushUrl接口进行页面跳转
    this.getUIContext().getRouter().pushUrl({
      url: 'pages/routerpage2',  // 跳转目标页面路径
      params: {  // 传递的页面参数
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushUrl success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## pushUrl

pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>

跳转到应用内的指定页面，使用Promise异步回调。与[pushUrl](arkts-apis-uicontext-router.md#pushurl)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义路由模式类
class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;  // 标准路由模式
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushUrl({
        url: 'pages/routerpage2',
        params: {  // 传递的页面参数
          data1: 'message',
          data2: {
            data3: [123, 456, 789]
          }
        }
      }, rtm.Standard)  // 使用标准路由模式
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## pushUrl

pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。使用callback异步回调。与[pushUrl](arkts-apis-uicontext-router.md#pushurl-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |
| callback | AsyncCallback<void> | 是 | 页面跳转结果回调函数。  当页面跳转成功时，error为undefined。当页面跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushUrl({
      url: 'pages/routerpage2',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, rtm.Standard, (err) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushUrl success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceUrl

replaceUrl(options: router.RouterOptions): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。

**说明** 

replaceUrl()会替换页面栈栈顶页面，页面栈深度维持不变。与pushUrl()的核心差异：pushUrl()入栈新页面、栈深度 + 1，replaceUrl()不改变栈深度。被替换的页面会直接销毁，无法通过back()回退访问。适用场景：登录成功跳转首页（避免回退至登录页）、页面重定向、临时中转页面跳转等。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    // 调用replaceUrl接口进行页面替换
    this.getUIContext().getRouter().replaceUrl({
        url: 'pages/detail',  // 替换的目标页面路径
        params: {  // 传递的页面参数
          data1: 'message'
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`replaceUrl failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceUrl

replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 页面替换结果回调函数。  当页面替换成功时，error为undefined。当页面替换失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceUrl({
      url: 'pages/detail',
      params: {  // 传递的页面参数
        data1: 'message'
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceUrl success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceUrl

replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。与[replaceUrl](arkts-apis-uicontext-router.md#replaceurl)相比，新增了mode参数，即支持设置替换页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 替换页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceUrl({
        url: 'pages/detail',
        params: {
          data1: 'message'
        }
      }, rtm.Standard)
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`replaceUrl failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceUrl

replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。使用callback异步回调。与[replaceUrl](arkts-apis-uicontext-router.md#replaceurl-1)相比，新增了mode参数，即支持设置替换页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 替换页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |
| callback | AsyncCallback<void> | 是 | 页面替换结果回调函数。  当页面替换成功时，error为undefined。当页面替换失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceUrl({
      url: 'pages/detail',
      params: {
        data1: 'message'
      }
    }, rtm.Standard, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceUrl success');
    });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions): Promise<void>

跳转到指定的命名路由页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息，包含name（命名路由名称）和params（传递的参数）等字段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    // 调用pushNamedRoute接口跳转到命名路由页面
    this.getUIContext().getRouter().pushNamedRoute({
        name: 'myPage',  // 命名路由名称
        params: {  // 传递的页面参数
          data1: 'message',
          data2: {
            data3: [123, 456, 789]
          }
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushNamedRoute failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 页面跳转结果回调函数。  当页面跳转成功时，error为undefined。当页面跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushNamedRoute({
      name: 'myPage',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>

跳转到指定的命名路由页面，使用Promise异步回调。与[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp{
  Standard:router.RouterMode = router.RouterMode.Standard;
}
let rtm:RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushNamedRoute({
      name: 'myPage',
      params: {  // 传递的页面参数
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
          }
        }
      }, rtm.Standard)
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushNamedRoute failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。使用callback异步回调。与[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |
| callback | AsyncCallback<void> | 是 | 页面跳转结果回调函数。  当页面跳转成功时，error为undefined。当页面跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushNamedRoute({
      name: 'myPage',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, rtm.Standard, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。适用于大型应用中使用命名路由管理页面、路由路径可能变化时避免硬编码URL、模块化开发中各模块独立管理自己的命名路由等场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | if the number of parameters is less than 1 or the type of the url parameter is not string. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    // 调用replaceNamedRoute接口替换命名路由页面
    this.getUIContext().getRouter().replaceNamedRoute({
        name: 'myPage',
        params: {  // 传递的页面参数
          data1: 'message'
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`replaceNamedRoute failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 页面替换结果回调函数。  当页面替换成功时，error为undefined。当页面替换失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceNamedRoute({
      name: 'myPage',
      params: {  // 传递的页面参数
        data1: 'message'
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。与[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute)相比，新增了mode参数，即支持设置替换页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 替换页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceNamedRoute({
        name: 'myPage',
        params: {
          data1: 'message'
        }
      }, rtm.Standard)
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`replaceNamedRoute failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。使用callback异步回调。与[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute-1)相比，新增了mode参数，即支持设置替换页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 替换页面使用的模式，可选Standard（标准模式）或Single（单例模式）。建议根据页面栈管理需求选择：Standard模式适用于常规页面跳转；Single模式可避免相同页面重复入栈，适合登录页、主页等单例场景。 |
| callback | AsyncCallback<void> | 是 | 页面替换结果回调函数。  当页面替换成功时，error为undefined。当页面替换失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | if the number of parameters is less than 1 or the type of the url parameter is not string. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceNamedRoute({
      name: 'myPage',
      params: {
        data1: 'message'
      }
    }, rtm.Standard, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## back

back(options?: router.RouterOptions ): void

返回上一页面或指定的页面。

**说明** 

如果之前调用了showAlertBeforeBackPage()开启了返回询问对话框，则调用back()时会弹出确认对话框：用户选择"取消"则back()不执行，选择"确认"则继续执行；可通过hideAlertBeforeBackPage()关闭返回询问对话框。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 否 | 返回页面描述信息。当需要返回到指定的页面时传入此参数（通过url指定目标页面）；当只需返回上一页时可以不传入此参数。url指定返回的目标页面：若页面栈中存在该url，则返回至index最大的同名页面；若不存在则不响应操作。若url未设置，则返回上一页（页面不会重新构建，出栈后会被回收）。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
router.back({url:'pages/detail'});
```

## back12+

back(index: number, params?: Object): void

返回指定的页面。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 返回目标页面的索引值，从0开始计数（注意：与[getStateByIndex](arkts-apis-uicontext-router.md#getstatebyindex12)的index参数不同，后者从1开始计数）。  取值范围：[0, +∞)。如果index超出页面栈范围或不存在对应页面，则不响应用户操作。 |
| params | Object | 否 | 页面返回时携带的参数。不传入时不携带参数。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
router.back(1);
```

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
router.back(1, {info:'来自Home页'}); // 携带参数返回
```

## clear

clear(): void

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

**说明** 

调用 clear()方法会清空全部历史页面栈，最终仅保留当前页面，页面栈深度变为1。此时栈内无历史记录，back()回退接口将失效；但pushUrl()、replaceUrl()等跳转方法仍可正常使用，支持新增页面或替换当前页面。该操作具备不可逆特性，执行完成后用户无法回访任何历史页面，建议仅在退出登录、切换账号等业务场景下使用，调用前务必持久化存储关键页面状态数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
router.clear();
```

## getLength(deprecated)

getLength(): string

获取当前在页面栈内的页面数量。

**说明** 

从API version 10开始支持，从 API version 23开始废弃，建议使用[getStackSize](arkts-apis-uicontext-router.md#getstacksize23)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 页面数量，页面栈支持最大数值是32。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
let size = router.getLength();
console.info('pages stack size = ' + size);
```

## getStackSize23+

getStackSize(): number

获取当前页面栈内的页面数量。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 页面数量，页面栈支持最大数值是32。 |

**示例：**

```ts
@Entry
@Component
struct Index {

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('stack size')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        console.info(`get stack size: ${this.getUIContext().getRouter().getStackSize()}`)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## getState

getState(): router.RouterState

获取当前页面的状态信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| router.[RouterState](js-apis-router.md#routerstate) | 页面状态信息。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
let page = router.getState();
if (page != undefined) {
  console.info('current index = ' + page.index);
  console.info('current name = ' + page.name);
  console.info('current path = ' + page.path);
}
```

## getStateByIndex12+

getStateByIndex(index: number): router.RouterState | undefined

通过索引值获取对应页面的状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 表示要获取的页面索引，从1开始计数（注意：与[back](arkts-apis-uicontext-router.md#back12)的index参数不同，后者从0开始计数）。  取值范围：[1, +∞)。索引不存在时返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| router.[RouterState](js-apis-router.md#routerstate) | undefined | 返回页面状态信息。索引不存在时返回undefined。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info('params = ' + options.params);
}
```

## getStateByUrl12+

getStateByUrl(url: string): Array<router.RouterState>

通过url获取匹配指定url的页面的状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 表示要获取对应页面信息的url，需使用应用内页面路径格式。如果页面栈中没有对应url的页面，返回空数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<router.[RouterState](js-apis-router.md#routerstate)> | 页面状态信息。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
let options:Array<router.RouterState> = router.getStateByUrl('pages/index');
for (let i: number = 0; i < options.length; i++) {
  console.info('index = ' + options[i].index);
  console.info('name = ' + options[i].name);
  console.info('path = ' + options[i].path);
  console.info('params = ' + options[i].params);
}
```

## showAlertBeforeBackPage

showAlertBeforeBackPage(options: router.EnableAlertOptions): void

开启页面返回询问对话框。调用此方法后，当用户触发返回操作（如点击返回键、调用back方法）时，系统会先弹出确认对话框询问用户是否返回；用户确认后才会执行返回操作，取消则留在当前页面。适用于表单填写页面（防止用户误触返回导致内容丢失）、重要操作确认页面（如支付、提交订单等）、内容编辑页面（用户可能有未保存的修改时）等场景。与hideAlertBeforeBackPage()方法成对使用：调用本方法开启对话框后，建议在适当时机调用hideAlertBeforeBackPage()关闭对话框。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.EnableAlertOptions](js-apis-router.md#enablealertoptions) | 是 | 文本弹窗信息描述，包含message（弹窗提示内容）等参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
try {
  router.showAlertBeforeBackPage({
    message: 'Message Info'
  });
} catch(error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(`showAlertBeforeBackPage failed, code is ${code}, message is ${message}`);
}
```

## hideAlertBeforeBackPage

hideAlertBeforeBackPage(): void

禁用页面返回询问对话框。适用于用户已完成保存操作可以安全返回、页面状态切换后不再需要返回确认、需要动态控制返回行为等场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
router.hideAlertBeforeBackPage();
```

## getParams

getParams(): Object

获取发起跳转的页面往当前页传入的参数。参数在页面跳转时通过RouterOptions或NamedRouterOptions的params字段传递。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 发起跳转的页面往当前页传入的参数。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```ts
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
router.getParams();
```
