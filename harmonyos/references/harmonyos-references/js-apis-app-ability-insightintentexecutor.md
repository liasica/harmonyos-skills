---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentexecutor
title: "@ohos.app.ability.InsightIntentExecutor (意图执行基类)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.InsightIntentExecutor (意图执行基类)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:425743e65e439f45e1b8d1cdd9c28925a1a040ca2a72073b089dfe7cca129137
---

本模块提供意图执行基类，开发者通过本模块对接端侧[意图框架](../harmonyos-guides/insight-intent-overview.md)，[通过配置文件开发意图](../harmonyos-guides/insight-intent-config-development.md)实现意图的业务逻辑。

除了可以通过配置文件开发意图，还可以通过装饰器开发意图。对于API version 20及以后的版本，推荐使用[通过装饰器开发意图](../harmonyos-guides/insight-intent-decorator-development.md)。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { InsightIntentExecutor } from '@kit.AbilityKit';
```

## InsightIntentExecutor

表示意图执行基类。

### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [InsightIntentContext](js-apis-app-ability-insightintentcontext.md) | 否 | 否 | 意图执行上下文。 |

### onExecuteInUIAbilityForegroundMode

onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖[UIAbility](js-apis-app-ability-uiability.md)组件前台启动时，会在UIAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 若UIAbility组件冷启动，意图执行时UIAbility组件生命周期触发顺序：[onCreate](js-apis-app-ability-uiability.md#oncreate)、[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)、onExecuteInUIAbilityForegroundMode、[onForeground](js-apis-app-ability-uiability.md#onforeground)。
* 若UIAbility组件热启动，且启动时UIAbility组件处于后台，意图执行时UIAbility组件生命周期触发顺序：[onNewWant](js-apis-app-ability-uiability.md#onnewwant)、onExecuteInUIAbilityForegroundMode、[onForeground](js-apis-app-ability-uiability.md#onforeground)。
* 若UIAbility组件热启动，且启动时UIAbility组件处于前台，意图执行时UIAbility组件生命周期触发顺序：onExecuteInUIAbilityForegroundMode。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |
| pageLoader | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 表示windowStage实例对象，和[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)接口的windowStage实例是同一个，通过调用其loadContent方法加载意图执行的页面，参数为页面路径字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
    pageLoader: window.WindowStage): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // 由开发者定义
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    // 若开发者需要加载意图内容，pages/IntentPage即为意图页面
    pageLoader.loadContent('pages/IntentPage', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Code: ${err.code}, message: ${err.message}`);
      } else {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in loading the content');
      }
    });

    result = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

使用Promise异步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  })
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
  async onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
    pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // 由开发者定义
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = await executeInsightIntent(param);
    return result;
  }
}
```

### onExecuteInUIAbilityBackgroundMode

onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖[UIAbility](js-apis-app-ability-uiability.md)组件后台启动时，会在UIAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 若UIAbility组件冷启动，意图执行时UIAbility组件生命周期触发顺序：[onCreate](js-apis-app-ability-uiability.md#oncreate)、onExecuteInUIAbilityBackgroundMode、[onBackground](js-apis-app-ability-uiability.md#onbackground)。
* 若UIAbility组件热启动，意图执行时UIAbility组件生命周期触发顺序：onExecuteInUIAbilityBackgroundMode。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

使用Promise异步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  })
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
  async onExecuteInUIAbilityBackgroundMode(name: string,
    param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }
    result = await executeInsightIntent(param);
    return result;
  }
}
```

### onExecuteInUIExtensionAbility

onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)启动时，会在UIExtensionAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 意图执行时UIExtensionAbility生命周期触发顺序：[onCreate](js-apis-app-ability-uiextensionability.md#oncreate)、[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)、onExecuteInUIExtensionAbility、[onForeground](js-apis-app-ability-uiextensionability.md#onforeground)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |
| pageLoader | [UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md) | 是 | 表示UIExtensionContentSession实例对象，和[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)接口的UIExtensionContentSession实例是同一个，可用于加载意图执行的页面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
    pageLoader: UIExtensionContentSession): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // 由开发者定义
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    // 若开发者需要加载意图内容，pages/Index即为意图页面
    pageLoader.loadContent('pages/Index');

    result = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

使用Promise异步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  })
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
  async onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
    pageLoader: UIExtensionContentSession): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // 由开发者定义
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = await executeInsightIntent(param);
    return result;
  }
}
```

### onExecuteInServiceExtensionAbility

onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖ServiceExtensionAbility组件启动时，会在ServiceExtensionAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 意图执行时ServiceExtensionAbility生命周期触发顺序：onCreate、onRequest、onExecuteInServiceExtensionAbility。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // 由开发者定义
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

使用Promise异步返回意图执行结果的示例如下：

```ts
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  })
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
  async onExecuteInServiceExtensionAbility(name: string,
    param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // 由开发者定义
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = await executeInsightIntent(param);
    return result;
  }
}
```
