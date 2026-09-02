---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autofillmanager
title: "@ohos.app.ability.autoFillManager (自动填充框架)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.autoFillManager (自动填充框架)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ddf61e369587ec49380bbc7674bbbdf8442c99104a14d8849b5a3bffb9a81064
---

autoFillManager模块为应用提供账号、密码、地址、电话号码等用户信息的自动填充能力。

不同于页面切换时触发的系统自动保存功能，该功能需要由用户手动触发。例如用户在网站上输入了账号密码，并点击“保存”按钮，才能触发相应的自动保存操作。

**说明** 

本模块首批接口从API version 11 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { autoFillManager } from '@kit.AbilityKit';
```

## OnFillSuccessFn

type OnFillSuccessFn = (viewData: ViewData) => void

当填充请求成功时，会触发该回调。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| viewData | [ViewData](js-apis-inner-application-viewdata.md) | 是 | 自动填充的视图数据信息。 |

## OnFillFailureFn

type OnFillFailureFn = (result: FillFailureResult) => void

当填充请求失败时，会触发该回调。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [FillFailureResult](js-apis-inner-application-autofillrequest.md#fillfailureresult) | 是 | 表示自动填充失败结果。 |

## AutoSaveCallback

当保存请求完成时所触发的回调接口。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

### onSuccess

onSuccess(): void

当保存请求成功时，该回调被调用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**示例：**

参见[autoFillManager.requestAutoSave](js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)。

### onFailure

onFailure(): void

当保存请求失败时，该回调被调用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**示例：**

参见[autoFillManager.requestAutoSave](js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)。

## AutoFillCallback

当填充请求完成时所触发的回调接口。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

### onSuccess

onSuccess: OnFillSuccessFn

当填充请求成功时，该回调被调用。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OnFillSuccessFn](js-apis-app-ability-autofillmanager.md#onfillsuccessfn) | 当填充请求成功时，会触发该回调。 |

**示例：**

参见[autoFillManager.requestAutoFill](js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautofill)。

### onFailure

onFailure: OnFillFailureFn

当填充请求失败时，会触发该回调。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OnFillFailureFn](js-apis-app-ability-autofillmanager.md#onfillfailurefn) | 当填充请求失败时，会触发该回调。 |

**示例：**

参见[autoFillManager.requestAutoFill](js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautofill)。

**说明** 

示例中从AppStorage中取得的UiContext为预先在EntryAbility（拉起此页面的Ability）中OnWindowStageCreate生命周期获得，并存储到AppStorage中，具体可参考[requestAutoSave](js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)。

## autoFillManager.requestAutoSave

requestAutoSave(context: UIContext, callback?: AutoSaveCallback): void

请求保存表单数据。使用callback异步回调。

如果当前表单没有提供表单切换的功能，可以通过此接口保存历史表单输入数据，保存请求完成时会触发该回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 将在其中执行保存操作的UI上下文。 |
| callback | [AutoSaveCallback](js-apis-app-ability-autofillmanager.md#autosavecallback) | 否 | 当保存请求完成时所触发的回调接口。 |

**错误码：**

以下错误码的详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: 1. Get instance id failed; 2. Parse instance id failed; 3. The second parameter is not of type callback. |
| 16000050 | Internal error. |

**示例：**

```ts
// EntryAbility.ets
import { UIAbility, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window, UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let localStorageData: Record<string, string | common.UIAbilityContext> = {
      'message': "AutoFill Page",
      'context': this.context,
    };
    let storage = new LocalStorage(localStorageData);
    windowStage.loadContent('pages/Index', storage, (err, data) => {
      if (err && err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      // Obtain the main window.
      windowStage.getMainWindow((err: BusinessError, data: window.Window) => {
        let errCode: number = err?.code;
        if (errCode) {
          console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
          return;
        }
        console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
        // get UIContext instance.
        let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
        PersistentStorage.persistProp("uiContext", uiContext);
      })
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}
```

```ts
// Index.ets
import { autoFillManager } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let uiContext = AppStorage.get<UIContext>('uiContext');
let callback: autoFillManager.AutoSaveCallback = {
  onSuccess: () => {
    console.info(`save request on success.`);
  },
  onFailure: () => {
    console.error(`save request on failure.`);
  }
};

@Entry
@Component
struct Index {
  @State userName: string = "";
  @State password: string = "";
  private uiContext: UIContext = this.getUIContext();
  build() {
    GridRow({ gutter: { y: 20 } }) {
      GridCol({ span: 20 }) {
        TextInput({ placeholder: 'Enter userName', text: this.userName })
          .type(InputType.USER_NAME)
          .width('90%')
          .onChange((value: string) => {
            this.userName = value
          })
      }
      GridCol({ span: 20 }) {
        TextInput({ placeholder: 'Enter password', text: this.password })
          .type(InputType.Password)
          .width('90%')
          .onChange((value: string) => {
            this.password = value
          })
      }
      GridCol({ span: 20 }) {
        Button('requestAutoSave')
          .onClick(() => {
            try {
              // 发起保存请求
              autoFillManager.requestAutoSave(this.uiContext, callback);
            } catch (error) {
              console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
            }
          })
      }
    }
  }
}
```

## autoFillManager.requestAutoSave

requestAutoSave(context: UIContext, request: SaveRequest, callback?: AutoSaveCallback): void

请求保存表单数据。使用callback异步回调。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 将在其中执行保存操作的UI上下文。 |
| request | [SaveRequest](js-apis-inner-application-autofillrequest.md#saverequest) | 是 | 自动保存请求信息。 |
| callback | [AutoSaveCallback](js-apis-app-ability-autofillmanager.md#autosavecallback) | 否 | 当保存请求完成时所触发的回调接口。 |

**错误码：**

以下错误码的详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```ts
// Index.ets
import { autoFillManager } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

// request需按照实际工程配置
let request: autoFillManager.SaveRequest = {
  viewData: {
    bundleName: "com.example.testBundleName",
    pageUrl: "testPageUrl",
    pageNodeInfos: [
      {
        id: 1,
        autoFillType: autoFillManager.AutoFillType.USER_NAME,
        value: "testValue1",
        placeholder: "testPlaceholder1",
        rect: {
          left: 1,
          top: 1,
          width: 1,
          height: 1,
        },
        isFocus: false
      },
      {
        id: 2,
        autoFillType: autoFillManager.AutoFillType.PASSWORD,
        value: "testValue2",
        placeholder: "testPlaceholder2",
        rect: {
          left: 1,
          top: 1,
          width: 1,
          height: 1,
        },
        isFocus: false
      }
    ],
    pageRect: {
      left: 1,
      top: 1,
      width: 1,
      height: 1
    }
  }
}
let callback: autoFillManager.AutoSaveCallback = {
  onSuccess: () => {
    console.info(`save request on success.`);
  },
  onFailure: () => {
    console.error(`save request on failure.`);
  }
};

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  build() {
    GridRow({ gutter: { y: 20 } }) {
      GridCol({ span: 20 }) {
        Button('requestAutoSave')
          .onClick(() => {
            try {
              // 发起保存请求
              autoFillManager.requestAutoSave(this.uiContext, request, callback);
            } catch (error) {
              console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
            }
          })
      }
    }
  }
}
```

## autoFillManager.requestAutoFill

requestAutoFill(context: UIContext, request: FillRequest, callback?: AutoFillCallback): void

请求填充表单数据。使用callback异步回调。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 将在其中执行填充操作的UI上下文。 |
| request | [FillRequest](js-apis-inner-application-autofillrequest.md#fillrequest) | 是 | 自动填充请求信息。 |
| callback | [AutoFillCallback](js-apis-app-ability-autofillmanager.md#autofillcallback) | 否 | 当填充请求完成时所触发的回调接口。 |

**错误码：**

以下错误码的详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```ts
// Index.ets
import { autoFillManager } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

// request需按照实际工程配置
let request: autoFillManager.FillRequest = {
  type: autoFillManager.AutoFillType.USER_NAME,
  viewData: {
    bundleName: "com.example.testBundleName",
    pageUrl: "testPageUrl",
    pageNodeInfos: [
      {
        id: 1,
        autoFillType: autoFillManager.AutoFillType.USER_NAME,
        value: "testValue1",
        placeholder: "testPlaceholder1",
        rect: {
          left: 1,
          top: 1,
          width: 1,
          height: 1,
        },
        isFocus: false
      },
      {
        id: 2,
        autoFillType: autoFillManager.AutoFillType.PASSWORD,
        value: "testValue2",
        placeholder: "testPlaceholder2",
        rect: {
          left: 1,
          top: 1,
          width: 1,
          height: 1,
        },
        isFocus: false
      }
    ],
    pageRect: {
      left: 1,
      top: 1,
      width: 1,
      height: 1
    }
  }
}
let callback: autoFillManager.AutoFillCallback = {
  onSuccess: (viewData: autoFillManager.ViewData) => {
    console.info(`fill request on success, viewData: ${JSON.stringify(viewData)}`);
  },
  onFailure: (result: autoFillManager.FillFailureResult) => {
    console.error(`fill request on failure, result: ${JSON.stringify(result)}`);
  }
};

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  build() {
    GridRow({ gutter: { y: 20 } }) {
      GridCol({ span: 20 }) {
        Button('requestAutoFill')
          .onClick(() => {
            try {
              // 发起填充请求
              autoFillManager.requestAutoFill(this.uiContext, request, callback);
            } catch (error) {
              console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
            }
          })
      }
    }
  }
}
```

## ViewData

type ViewData = \_ViewData.default

自动填充的视图数据信息。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_ViewData](js-apis-inner-application-viewdata.md#viewdata-1).default | 表示自动填充的视图数据信息。 |

## PageNodeInfo

type PageNodeInfo = \_PageNodeInfo.default

自动填充的页面节点信息。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_PageNodeInfo](js-apis-inner-application-pagenodeinfo.md#pagenodeinfo-1).default | 表示自动填充的页面节点信息。 |

## FillRequest

type FillRequest = \_AutoFillRequest.FillRequest

自动填充的请求信息。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AutoFillRequest.FillRequest](js-apis-inner-application-autofillrequest.md#fillrequest) | 表示自动填充的请求信息。 |

## SaveRequest

type SaveRequest = \_AutoFillRequest.SaveRequest

自动保存的请求信息。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AutoFillRequest.SaveRequest](js-apis-inner-application-autofillrequest.md#saverequest) | 表示自动保存的请求信息。 |

## AutoFillRect

type AutoFillRect = \_AutoFillRect.default

用于自动填充的矩形区域。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_AutoFillRect](js-apis-inner-application-autofillrect.md#autofillrect-1).default | 表示用于自动填充的矩形区域。 |

## FillFailureResult

type FillFailureResult = \_FillFailureResult

自动填充失败结果。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [\_FillFailureResult](js-apis-inner-application-autofillrequest.md#fillfailureresult) | 表示自动填充失败结果。 |
