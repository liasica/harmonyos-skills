---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/watchface_api
title: watchFace（穿戴表盘能力开放）
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > ArkTS API > watchFace（穿戴表盘能力开放）
category: harmonyos-references
scraped_at: 2026-11-12T09:56:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b47ac182f342357bd4e3ac4ab96f3cbc2519b036759e45d26a8c75a8a290f121
---

本模块提供穿戴设备上表盘的管理能力，应用可调用模块内接口实现如下功能，包括将表盘添加到穿戴设备和为表盘配置生成预览图。

**起始版本**：26.0.1

## 导入模块

```typescript
import { watchFace } from '@kit.WearEngine';
```

## watchFace.isWatchFaceSupport

isWatchFaceSupport(): Promise<boolean>

检查当前设备是否支持使用穿戴表盘的相关接口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回检查结果。true表示支持使用，false表示不支持使用。 |

**示例：**

```typescript
import { watchFace } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

watchFace.isWatchFaceSupport().then((isSupport: boolean) => {
  console.info(`Succeeded in checking watch face support, result is ${isSupport}.`);
}).catch((error: BusinessError) => {
  console.error(`Failed to check watch face support. Code is ${error.code}, message is ${error.message}.`);
})
```

## watchFace.getWatchFaceManager

getWatchFaceManager(context: common.UIAbilityContext): WatchFaceManager

用于获取WatchFaceManager实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-app-ability-common.md#uiabilitycontext) | 是 | 表示Ability的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WatchFaceManager](watchface_api.md#watchfacemanager) | 返回WatchFaceManager实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```typescript
import { watchFace } from '@kit.WearEngine';

let watchFaceManager: watchFace.WatchFaceManager = watchFace.getWatchFaceManager(this.getUIContext().getHostContext());
console.info(`Succeeded in getting watch face manager.`);
```

## WatchFaceManager

表盘管理类，由接口[watchFace.getWatchFaceManager](watchface_api.md#watchfacegetwatchfacemanager)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

### addWatchFace

addWatchFace(config: WatchFaceConfigUnion): Promise<void>

将表盘添加到穿戴设备，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WatchFace

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WatchFaceConfigUnion](watchface_api.md#watchfaceconfigunion) | 是 | 表盘配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```typescript
import { watchFace } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let watchFaceManager: watchFace.WatchFaceManager = watchFace.getWatchFaceManager(this.getUIContext().getHostContext());

// 构造元气样式的表盘配置
let config: watchFace.WatchFaceConfigUnion = {
  defaultStyle: watchFace.Style.VIBRANT,
  isCurrentAppFormsOnly: true
}

// 将表盘添加到穿戴设备
watchFaceManager.addWatchFace(config).then(() => {
  console.info(`Succeeded in adding watch face.`);
}).catch((error: BusinessError) => {
  console.error(`Failed to add watch face. Code is ${error.code}, message is ${error.message}.`);
})
```

### generatePreviews

generatePreviews(configs: WatchFaceConfigUnion[]): Promise<image.PixelMap[]>

根据传入的表盘配置数组，生成对应预览图，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WatchFace

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configs | [WatchFaceConfigUnion](watchface_api.md#watchfaceconfigunion)[] | 是 | 表盘配置数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)[]> | Promise对象，返回预览图。返回的PixelMap对象由调用方管理，使用完毕后应及时调用release()释放资源，避免在内存有限的穿戴设备上造成内存泄漏。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```typescript
import { watchFace } from '@kit.WearEngine';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

let watchFaceManager: watchFace.WatchFaceManager = watchFace.getWatchFaceManager(this.getUIContext().getHostContext());

// 构造多个表盘配置
let configs: watchFace.WatchFaceConfigUnion[] = [
  {
    defaultStyle: watchFace.Style.VIBRANT,
    containers: {
      [watchFace.Position.TOP_LEFT]: {
        options: [watchFace.ContainerOption1x1.STEPS]
      },
      [watchFace.Position.BOTTOM_LEFT]: {
        options: [watchFace.ContainerOption2x2.BATTERY]
      }
    }
  },
  {
    defaultStyle: watchFace.Style.CLASSIC
  }
]

// 为表盘配置生成预览图
watchFaceManager.generatePreviews(configs).then((previews: image.PixelMap[]) => {
  console.info(`Succeeded in generating previews, number is ${previews.length}.`);
  previews.forEach((preview: image.PixelMap) => {
    // 使用完毕后释放PixelMap资源，避免内存泄漏
    preview.release();
  })
}).catch((error: BusinessError) => {
  console.error(`Failed to generate previews. Code is ${error.code}, message is ${error.message}.`);
})
```

## WatchFaceConfigUnion

type WatchFaceConfigUnion = VibrantWatchFaceConfig | ClassicWatchFaceConfig

表盘样式的联合类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 类型 | 说明 |
| --- | --- |
| [VibrantWatchFaceConfig](watchface_api.md#vibrantwatchfaceconfig) | 元气样式的表盘配置。 |
| [ClassicWatchFaceConfig](watchface_api.md#classicwatchfaceconfig) | 经典样式的表盘配置。 |

## VibrantWatchFaceConfig

元气样式的表盘配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultStyle | [Style.VIBRANT](watchface_api.md#style) | 否 | 否 | 表盘的默认样式。 |
| containers | [VibrantContainersConfig](watchface_api.md#vibrantcontainersconfig) | 否 | 是 | 元气样式的容器配置。未填写时使用系统默认配置。 |
| isCurrentAppFormsOnly | boolean | 否 | 是 | 是否只展示当前三方应用的2\*2控件。true表示只展示当前三方应用的2\*2卡片，false表示点击进入自定义之后会带上其他卡片。 |

## ClassicWatchFaceConfig

经典样式的表盘配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultStyle | [Style.CLASSIC](watchface_api.md#style) | 否 | 否 | 表盘的默认样式。 |
| containers | [ClassicContainersConfig](watchface_api.md#classiccontainersconfig) | 否 | 是 | 经典样式的容器配置。未填写时使用系统默认配置。 |
| isCurrentAppFormsOnly | boolean | 否 | 是 | 是否只展示当前三方应用的2\*2控件。true表示只展示当前三方应用的2\*2卡片，false表示点击进入自定义之后会带上其他卡片。 |

## Style

表盘样式的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIBRANT | 2 | 元气样式。 |
| CLASSIC | 3 | 经典样式。 |

## Position

表盘容器位置的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP\_LEFT | 'top\_left' | 左上位置。 |
| TOP\_CENTER | 'top\_center' | 中上位置。 |
| TOP\_RIGHT | 'top\_right' | 右上位置。 |
| MIDDLE\_LEFT | 'middle\_left' | 左中位置。 |
| MIDDLE\_CENTER | 'middle\_center' | 中间位置。 |
| MIDDLE\_RIGHT | 'middle\_right' | 右中位置。 |
| BOTTOM\_LEFT | 'bottom\_left' | 左下位置。 |
| BOTTOM\_CENTER | 'bottom\_center' | 中下位置。 |
| BOTTOM\_RIGHT | 'bottom\_right' | 右下位置。 |

## VibrantContainersConfig

元气样式的控件容器配置类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| Position.TOP\_LEFT | [ContainerConfig1x1](watchface_api.md#containerconfig1x1) | 否 | 是 | 左上位置的容器配置。未提供时使用系统默认配置。 |
| Position.BOTTOM\_LEFT | [ContainerConfig2x2](watchface_api.md#containerconfig2x2) | 否 | 是 | 左下位置的容器配置。未提供时使用系统默认配置。 |
| Position.MIDDLE\_RIGHT | [ContainerConfig1x1](watchface_api.md#containerconfig1x1) | 否 | 是 | 右中位置的容器配置。未提供时使用系统默认配置。 |
| Position.BOTTOM\_RIGHT | [ContainerConfig1x1](watchface_api.md#containerconfig1x1) | 否 | 是 | 右下位置的容器配置。未提供时使用系统默认配置。 |

## ClassicContainersConfig

经典样式的控件容器配置类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| Position.BOTTOM\_LEFT | [ContainerConfig2x2](watchface_api.md#containerconfig2x2) | 否 | 是 | 左下位置的容器配置。未提供时使用系统默认配置。 |
| Position.MIDDLE\_RIGHT | [ContainerConfig1x1](watchface_api.md#containerconfig1x1) | 否 | 是 | 右中位置的容器配置。未提供时使用系统默认配置。 |
| Position.BOTTOM\_RIGHT | [ContainerConfig1x1](watchface_api.md#containerconfig1x1) | 否 | 是 | 右下位置的容器配置。未提供时使用系统默认配置。 |

## ContainerConfig1x1

1x1控件容器配置类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultOptions | [ContainerOption1x1](watchface_api.md#containeroption1x1) | 否 | 是 | 默认的控件容器选项。如果未指定，则取options中的第一个选项。 |
| options | [ContainerOption1x1](watchface_api.md#containeroption1x1)[] | 否 | 是 | 控件容器的可选组合。 |

## ContainerConfig2x2

2x2控件容器配置类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultForm | [FormInfo](watchface_api.md#forminfo) | 否 | 是 | 可将指定卡片作为控件容器的默认选项。如果未指定，则取defaultOptions的值。 |
| defaultOptions | [ContainerOption2x2](watchface_api.md#containeroption2x2) | 否 | 是 | 默认的控件容器选项。如果未指定，则取options中的第一个选项。 |
| options | [ContainerOption2x2](watchface_api.md#containeroption2x2)[] | 否 | 是 | 控件容器的可选组合。 |

**说明** 

defaultForm和defaultOptions互斥，如果同时提供，defaultForm优先。

## FormInfo

卡片信息类，具体请参考[Form Kit介绍](../harmonyos-guides/formkit-overview.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 否 | 否 | 卡片所属的模块。 |
| abilityName | string | 否 | 否 | 卡片跳转的Ability。 |
| name | string | 否 | 否 | 卡片的名称。 |

## ContainerOption1x1

1x1控件容器可用的选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WORKOUT | 7 | 显示锻炼图标，点击可跳转至对应的APP页面。 |
| WORKOUT\_RECORDS | 8 | 显示锻炼记录，点击可跳转至对应的数据页面。 |
| VO2MAX | 9 | 显示最大摄氧量（VO2 max）数据，点击可跳转至对应的数据页面。 |
| ACTIVITY\_RECORDS | 10 | 显示活动记录进度，点击可跳转至对应的数据页面。 |
| MOVEMENT | 11 | 显示活动数据，点击可跳转至对应的数据页面。 |
| EXERCISE | 12 | 显示运动数据，点击可跳转至对应的数据页面。 |
| STAND | 13 | 显示站立时间数据，点击可跳转至对应的数据页面。 |
| STEPS | 14 | 显示步数数据，点击可跳转至对应的数据页面。 |
| EMOTIONS | 15 | 显示情绪数据，点击可跳转至对应的数据页面。 |
| STRESS\_VALUE | 16 | 显示压力值数据，点击可跳转至对应的数据页面。 |
| HEART\_RATE\_VALUE | 17 | 显示心率值数据，点击可跳转至对应的数据页面。 |
| SPO2 | 18 | 显示血氧饱和度（SpO2）数据，点击可跳转至对应的数据页面。 |
| SLEEP\_DURATION | 19 | 显示睡眠时长数据，点击可跳转至对应的数据页面。 |
| WECHAT | 20 | 显示微信图标，点击跳转到微信。 |
| ALIPAY | 21 | 显示支付宝图标，点击跳转到支付宝。 |
| TEMP | 22 | 显示温度数据，点击可跳转至对应的数据页面。 |
| AQI | 23 | 显示空气质量指数（AQI）数据，点击可跳转至对应的数据页面。 |
| UV\_INDEX | 24 | 显示紫外线（UV）数据，点击可跳转至对应的数据页面。 |
| SUNRISE\_SUNSET | 25 | 显示日出/日落时间，日出/日落数据，点击可跳转至对应的数据页面。 |
| MOONRISE\_MOONSET | 26 | 显示月出/月落时间，月出/月落数据，点击可跳转至对应的数据页面。 |
| MOON\_PHASE | 27 | 显示月相数据，点击可跳转至对应的数据页面。 |
| ALTITUDE | 28 | 显示海拔数据，点击可跳转至对应的数据页面。 |
| AIR\_PRESSURE | 29 | 显示气压数据，点击可跳转至对应的数据页面。 |
| DATE | 30 | 显示日期数据，点击可跳转至对应的数据页面。 |
| LUNAR\_DATE | 32 | 显示农历日期数据，点击可跳转至对应的数据页面。 |
| WORLD\_CLOCK | 33 | 显示世界时钟数据，点击可跳转至对应的数据页面。 |
| STOPWATCH | 34 | 显示秒表图标，点击可跳转至对应的APP页面。 |
| TIMER | 35 | 显示计时器图标，点击可跳转至对应的APP页面。 |
| ALARM | 36 | 显示闹钟图标，点击可跳转至对应的APP页面。 |
| COMPASS | 37 | 显示指南针图标，点击可跳转至对应的APP页面。 |
| BATTERY | 38 | 显示电量数据，点击可跳转至对应的数据页面。 |
| WECHAT\_PAY | 76 | 显示微信支付图标，点击跳转到微信支付页面。 |

## ContainerOption2x2

2x2控件容器可用的选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WatchFace

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WORKOUT | 59 | 显示锻炼数据，点击可跳转至对应的数据页面。 |
| RECOVERY | 60 | 显示恢复进度数据，点击可跳转至对应的数据页面。 |
| ACTIVITY\_RECORDS | 61 | 显示活动记录进度，点击可跳转至对应的数据页面。 |
| ACTIVITY\_DATA | 62 | 显示活动数据，点击可跳转至对应的数据页面。 |
| EMOTIONS | 63 | 显示情绪数据，点击可跳转至对应的数据页面。 |
| STRESS\_LEVEL | 64 | 显示压力值数据，点击可跳转至对应的数据页面。 |
| HEART\_RATE\_VALUE | 65 | 显示心率值数据，点击可跳转至对应的数据页面。 |
| SPO2 | 66 | 显示血氧饱和度（SpO2）数据，点击可跳转至对应的数据页面。 |
| RECENT\_SLEEP | 67 | 显示最近睡眠数据，点击可跳转至对应的数据页面。 |
| MEDIA\_PLAYER | 68 | 显示媒体播放器数据，点击可跳转至对应的数据页面。 |
| TODAY\_WEATHER | 69 | 显示今日天气数据，点击可跳转至对应的数据页面。 |
| MOON\_PHASE | 70 | 显示月相数据，点击可跳转至对应的数据页面。 |
| WEATHER\_COMBO | 71 | 显示天气组合数据，点击可跳转至对应的数据页面。 |
| UPCOMING\_EVENTS | 72 | 显示近期日程数据，点击可跳转至对应的数据页面。 |
| BATTERY | 73 | 显示电量数据，点击可跳转至对应的数据页面。 |
| CUTE\_PET\_MYSTERY\_BOX | 74 | 显示随机可爱萌宠动画。 |
| EMOTIONAL\_PET | 75 | 基于情绪显示萌宠，点击可跳转至对应的数据页面。 |
