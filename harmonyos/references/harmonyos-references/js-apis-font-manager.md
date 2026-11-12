---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font-manager
title: "@ohos.fontManager (字体管理)"
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > ArkTS API > @ohos.fontManager (字体管理)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c876f16ecf881b4200949c48acf6b5dbcf49beaac5a3f76521b97eb822b3c94f
---

本模块为应用提供第三方字体的安装、卸载、查询以及字体服务状态监听能力。具体为：

* 安装应用级或会话级字体文件，支持.ttf、.ttc、.otf格式。
* 根据字体路径卸载已安装的字体。
* 查询已安装字体的作用范围。
* 注册字体服务状态变化监听器，当字体服务异常退出时通知应用。

**起始版本：** 26.0.1

## 导入模块

```ts
import { fontManager } from '@kit.LocalizationKit';
```

## FontScope

表示字体作用范围的枚举。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Global.FontManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP | 0 | 应用级字体。字体的生命周期跟随应用的生命周期，应用退出或字体服务异常退出时，安装的字体文件会被自动清理/卸载。需先调用[fontManager.onFontObserver](js-apis-font-manager.md#fontmanageronfontobserver)注册监听后才能安装。 |
| SESSION | 1 | 会话级字体。字体的生命周期不跟随应用的生命周期，设备重启或当前用户退出（多用户场景下）时，安装的字体文件会被自动清理/卸载。 |

## FontClientObserver

字体服务状态变化监听器。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Global.FontManager

### onServiceDied

onServiceDied(): void

字体服务异常退出时的回调函数，应用可在此回调函数中执行资源清理或重新注册等操作。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Global.FontManager

**示例：**

```ts
import { fontManager } from '@kit.LocalizationKit';

const observer: fontManager.FontClientObserver = {
  onServiceDied: () => {
    console.info('font service died');
  }
};
```

## fontManager.installScopeFont

installScopeFont(url: string, scope: FontScope): Promise<void>

安装指定路径下的字体文件为应用级或会话级字体。使用Promise异步回调。

**说明** 

* 当安装应用级字体时，需先调用[fontManager.onFontObserver](js-apis-font-manager.md#fontmanageronfontobserver)接口注册字体服务状态变化监听器。
* 安装成功后，应用可以通过字体名称使用该字体。同一字体路径不可重复安装。
* PC/2in1和Tablet支持安装的字体文件最大数量为800，其他设备支持安装的字体文件个数最大数量为200。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.UPDATE\_SCOPE\_FONT

**系统能力：** SystemCapability.Global.FontManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 待安装的字体文件路径，仅支持.ttf、.ttc和.otf格式的字体文件。 |
| scope | [FontScope](js-apis-font-manager.md#fontscope) | 是 | 字体作用范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[字体管理错误码](errorcode-font-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 31100101 | The font does not exist. |
| 31100102 | The font is not supported. |
| 31100103 | Failed to copy the font file. |
| 31100104 | The font file is installed. |
| 31100105 | Exceeded the maximum number of installed files. |
| 31100110 | Call failed due to system error. |
| 31100115 | The font observer is not registered. |

**示例：**

```ts
import { fontManager } from '@kit.LocalizationKit';

async function installScopeFont() {
  try {
    await fontManager.installScopeFont('fontPath', fontManager.FontScope.APP);
    console.info('installScopeFont suc');
  } catch (error) {
    console.error('installScopeFont err.' + error.code);
  }
}
```

## fontManager.uninstallScopeFont

uninstallScopeFont(url: string): Promise<void>

根据字体路径卸载已安装的应用级或会话级字体。使用Promise异步回调。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.UPDATE\_SCOPE\_FONT

**系统能力：** SystemCapability.Global.FontManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 需要卸载的字体路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[字体管理错误码](errorcode-font-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 31100108 | Failed to delete the font file. |
| 31100110 | Call failed due to system error. |
| 31100112 | The scope font is not found. |

**示例：**

```ts
import { fontManager } from '@kit.LocalizationKit';

async function uninstallScopeFont() {
  try {
    await fontManager.uninstallScopeFont('fontPath');
    console.info('uninstallScopeFont suc');
  } catch (error) {
    console.error('uninstallScopeFont err.' + error.code);
  }
}
```

## fontManager.getFontScope

getFontScope(url: string): Promise<FontScope>

查询指定路径字体的作用范围。使用Promise异步回调。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.UPDATE\_SCOPE\_FONT

**系统能力：** SystemCapability.Global.FontManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 需要查询的字体路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FontScope](js-apis-font-manager.md#fontscope)> | Promise对象，返回字体的作用范围。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[字体管理错误码](errorcode-font-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 31100110 | Call failed due to system error. |
| 31100112 | The scope font is not found. |

**示例：**

```ts
import { fontManager } from '@kit.LocalizationKit';

async function getFontScope() {
  try {
    let scope = await fontManager.getFontScope('fontPath');
    console.info('font scope is ' + scope);
  } catch (error) {
    console.error('getFontScope err.' + error.code);
  }
}
```

## fontManager.onFontObserver

onFontObserver(observer: FontClientObserver): void

注册字体服务状态变化监听器。

**说明** 

* 每个应用仅可注册一个字体服务状态变化监听器，重复注册会报错。
* 同一用户最多允许5个应用同时注册，否则会报错。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.UPDATE\_SCOPE\_FONT

**系统能力：** SystemCapability.Global.FontManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | [FontClientObserver](js-apis-font-manager.md#fontclientobserver) | 是 | 字体服务状态变化监听器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[字体管理错误码](errorcode-font-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 31100110 | Call failed due to system error. |
| 31100113 | The font observer is already registered. |
| 31100114 | The maximum number of font observers has been reached. |

**示例：**

```ts
import { fontManager } from '@kit.LocalizationKit';

const observer: fontManager.FontClientObserver = {
  onServiceDied: () => {
    console.info('font service died, please clean up resources');
  }
};

try {
  fontManager.onFontObserver(observer);
  console.info('onFontObserver suc');
} catch (error) {
  console.error('onFontObserver err.' + error.code);
}
```

## fontManager.offFontObserver

offFontObserver(): void

注销字体服务状态变化监听器。

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.UPDATE\_SCOPE\_FONT

**系统能力：** SystemCapability.Global.FontManager

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[字体管理错误码](errorcode-font-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 31100110 | Call failed due to system error. |
| 31100115 | The font observer is not registered. |

**示例：**

```ts
import { fontManager } from '@kit.LocalizationKit';

try {
  fontManager.offFontObserver();
  console.info('offFontObserver suc');
} catch (error) {
  console.error('offFontObserver err.' + error.code);
}
```
