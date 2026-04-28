---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-multinavigation
title: MultiNavigation
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 导航与切换 > MultiNavigation
category: harmonyos-references
scraped_at: 2026-04-28T08:01:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:911381f9399896d447ef5f279be8297e32c044818a72d572da166d649c86296d
---

MultiNavigation用于在大尺寸设备上分栏显示、进行路由跳转。

说明

该组件从API version 14开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

由于MultiNavigation存在多重栈嵌套，调用本文档明确说明的不支持接口或不在本文档支持接口列表中的接口(例如getParent、setInterception、pushDestination等)，可能会发生无法预期的问题。

MultiNavigation在深层嵌套场景下，可能存在路由动效异常的问题。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { MultiNavigation, MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

不可以包含子组件。

## MultiNavigation

PhonePC/2in1TabletTVWearable

MultiNavigation({navDestination: NavDestinationBuildFunction, multiStack: MultiNavPathStack, onNavigationModeChange?: OnNavigationModeChangeCallback, onHomeShowOnTop?: OnHomeShowOnTopCallback})

创建并初始化MultiNavigation组件。

MultiNavigation组件遵循默认的左起右清栈规则，这意味着从左侧主页点击时，会触发详情页的加载并同时清除右侧所有其他详情页，确保右侧仅展示最新加载的详情页。然而，若在右侧的详情页上再次执行详情页加载操作，系统将不会执行清栈动作。效果可参见[主页跳转详情页效果演示](ohos-arkui-advanced-multinavigation.md#示例)。

**装饰器类型：**@Component

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| multiStack | [MultiNavPathStack](ohos-arkui-advanced-multinavigation.md#multinavpathstack) | 是 | @State | 设置路由栈。 |
| navDestination | [NavDestinationBuildFunction](ohos-arkui-advanced-multinavigation.md#navdestinationbuildfunction) | 是 | @BuilderParam | 设置加载目标页面的路由规则。 |
| onNavigationModeChange | [OnNavigationModeChangeCallback](ohos-arkui-advanced-multinavigation.md#onnavigationmodechangecallback) | 否 | - | 设置MultiNavigation模式变更时的回调。 |
| onHomeShowOnTop | [OnHomeShowOnTopCallback](ohos-arkui-advanced-multinavigation.md#onhomeshowontopcallback) | 否 | - | 设置主页处于栈顶时的回调。 |

## MultiNavPathStack

PhonePC/2in1TabletTVWearable

当前，MultiNavigation的路由栈仅支持由使用方自行创建，不支持通过回调方式获取。请勿使用NavDestination的onReady等类似事件或接口来获取NavPathStack并进行栈操作，因为这可能会导致不可预知的问题。

### constructor

PhonePC/2in1TabletTVWearable

constructor()

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### pushPath

PhonePC/2in1TabletTVWearable

pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void

将指定的NavDestination页面信息入栈。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |
| policy | [SplitPolicy](ohos-arkui-advanced-multinavigation.md#splitpolicy枚举说明) | 否 | 当前入栈页面的策略。默认值：DETAIL\_PAGE |

### pushPath

PhonePC/2in1TabletTVWearable

pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void

将指定的NavDestination页面信息入栈，通过NavigationOptions设置页面栈操作选项。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 页面栈操作选项。仅支持其中的animated字段。 |
| policy | [SplitPolicy](ohos-arkui-advanced-multinavigation.md#splitpolicy枚举说明) | 否 | 当前入栈页面的策略。默认值：DETAIL\_PAGE |

### pushPathByName

PhonePC/2in1TabletTVWearable

pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void

将name指定的NavDestination页面信息入栈，传递的数据为param。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | Object | 是 | NavDestination页面详细参数。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |
| policy | [SplitPolicy](ohos-arkui-advanced-multinavigation.md#splitpolicy枚举说明) | 否 | 当前入栈页面的策略。默认值：DETAIL\_PAGE |

### pushPathByName

PhonePC/2in1TabletTVWearable

pushPathByName(name: string, param: Object, onPop?: base.Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | Object | 是 | NavDestination页面详细参数。 |
| onPop | base.[Callback](js-apis-base.md#callback)<[PopInfo](ts-basic-components-navigation.md#popinfo11)> | 否 | Callback回调，用于页面出栈时触发该回调处理返回结果。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |
| policy | [SplitPolicy](ohos-arkui-advanced-multinavigation.md#splitpolicy枚举说明) | 否 | 当前入栈页面的策略。默认值：DETAIL\_PAGE |

### replacePath

PhonePC/2in1TabletTVWearable

replacePath(info: NavPathInfo, animated?: boolean): void

将当前页面栈栈顶退出，将指定的NavDestination页面信息入栈，新页面的分栏策略继承原栈顶页面的策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

### replacePath

PhonePC/2in1TabletTVWearable

replacePath(info: NavPathInfo, options?: NavigationOptions): void

将当前页面栈栈顶退出，将指定的NavDestination页面信息入栈，新页面的分栏策略继承原栈顶页面的策略，通过NavigationOptions设置页面栈操作选项。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | NavDestination页面的信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 页面栈操作选项。仅支持其中的animated字段。 |

### replacePathByName

PhonePC/2in1TabletTVWearable

replacePathByName(name: string, param: Object, animated?: boolean): void

将当前页面栈栈顶退出，将name指定的页面入栈，新页面的分栏策略继承原栈顶页面的策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| param | Object | 是 | NavDestination页面详细参数。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

### removeByIndexes

PhonePC/2in1TabletTVWearable

removeByIndexes(indexes: Array<number>): number

将页面栈内索引值在indexes中的NavDestination页面删除。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indexes | Array<number> | 是 | 待删除NavDestination页面的索引值数组。  number类型的取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回删除的NavDestination页面数量。 |

### removeByName

PhonePC/2in1TabletTVWearable

removeByName(name: string): number

将页面栈内指定name的NavDestination页面删除。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 待删除NavDestination页面的名字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回删除的NavDestination页面数量。 |

### pop

PhonePC/2in1TabletTVWearable

pop(animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素。

说明

当调用[keepBottomPage](ohos-arkui-advanced-multinavigation.md#keepbottompage)接口并设置为true时，会保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | undefined | 返回栈顶NavDestination页面的信息。 |

### pop

PhonePC/2in1TabletTVWearable

pop(result?: Object, animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

说明

当调用[keepBottomPage](ohos-arkui-advanced-multinavigation.md#keepbottompage)接口并设置为true时，会保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 否 | 页面自定义处理结果。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | undefined | 返回栈顶NavDestination页面的信息。 |

### popToName

PhonePC/2in1TabletTVWearable

popToName(name: string, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。  取值范围：[-1, +∞) |

### popToName

PhonePC/2in1TabletTVWearable

popToName(name: string, result: Object, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| result | Object | 是 | 页面自定义处理结果。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。  取值范围：[-1, +∞) |

### popToIndex

PhonePC/2in1TabletTVWearable

popToIndex(index: number, animated?: boolean): void

回退路由栈到index指定的NavDestination页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。  取值范围：[0, +∞) |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

### popToIndex

PhonePC/2in1TabletTVWearable

popToIndex(index: number, result: Object, animated?: boolean): void

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。  取值范围：[0, +∞) |
| result | Object | 是 | 页面自定义处理结果。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

### moveToTop

PhonePC/2in1TabletTVWearable

moveToTop(name: string, animated?: boolean): number

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

说明

根据找到的第一个名为name的页面的不同，MultiNavigation会进行不同的处理：

1)当找到的是最上层主页或者全屏页，此时不做任何处理；

2)当找到的是最上层主页对应的详情页，则会将对应的详情页移到栈顶；

3)当找到的是非最上层的主页，则会将主页和对应所有详情页移到栈顶，详情页相对栈关系不变；

4)当找到的是非最上层的详情页，则会将主页和对应所有详情页移到栈顶，且将目标详情页移动到对应所有详情页的栈顶；

5)当找到的是非最上层的全屏页，则会将全屏页移动到栈顶。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。 |

### moveIndexToTop

PhonePC/2in1TabletTVWearable

moveIndexToTop(index: number, animated?: boolean): void

将指定index的NavDestination页面移到栈顶。

说明

根据找到的第一个名为name的页面的不同，MultiNavigation会进行不同的处理：

1)当找到的是最上层主页或者全屏页，此时不做任何处理；

2)当找到的是最上层主页对应的详情页，则会将对应的详情页移到栈顶；

3)当找到的是非最上层的主页，则会将主页和对应所有详情页移到栈顶，详情页相对栈关系不变；

4)当找到的是非最上层的详情页，则会将主页和对应所有详情页移到栈顶，且将目标详情页移动到对应所有详情页的栈顶；

5)当找到的是非最上层的全屏页，则会将全屏页移动到栈顶。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。  取值范围：[0, +∞) |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

### clear

PhonePC/2in1TabletTVWearable

clear(animated?: boolean): void

清除栈中所有页面。

说明

当调用[keepBottomPage](ohos-arkui-advanced-multinavigation.md#keepbottompage)接口并设置为true时，会保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true  true：支持转场动画。  false：不支持转场动画。 |

### getAllPathName

PhonePC/2in1TabletTVWearable

getAllPathName(): Array<string>

获取栈中所有NavDestination页面的名称。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回栈中所有NavDestination页面的名称。 |

### getParamByIndex

PhonePC/2in1TabletTVWearable

getParamByIndex(index: number): Object | undefined

获取index指定的NavDestination页面的参数信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | NavDestination页面的位置索引。  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | undefined | Object：返回对应NavDestination页面的参数信息。  undefined: 传入index无效时返回undefined。 |

### getParamByName

PhonePC/2in1TabletTVWearable

getParamByName(name: string): Array<Object>

获取全部名为name的NavDestination页面的参数信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Object> | 返回全部名为name的NavDestination页面的参数信息。 |

### getIndexByName

PhonePC/2in1TabletTVWearable

getIndexByName(name: string): Array<number>

获取全部名为name的NavDestination页面的位置索引。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | NavDestination页面名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回全部名为name的NavDestination页面的位置索引。  number类型的取值范围：[0, +∞) |

### size

PhonePC/2in1TabletTVWearable

size(): number

获取栈大小。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回栈大小。  取值范围：[0, +∞) |

### disableAnimation

PhonePC/2in1TabletTVWearable

disableAnimation(disable: boolean): void

关闭（true）或打开（false）当前MultiNavigation中所有转场动画。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disable | boolean | 是 | 是否关闭转场动画。  默认值：false  true：关闭转场动画。  false：不关闭转场动画。 |

### switchFullScreenState

PhonePC/2in1TabletTVWearable

switchFullScreenState(isFullScreen?: boolean): boolean

切换当前顶栈详情页面的显示模式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFullScreen | boolean | 否 | 是否切换为全屏。默认值为false。true表示全屏模式，false表示分栏模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 切换成功或失败。  true：切换成功。  false：切换失败。 |

### setHomeWidthRange

PhonePC/2in1TabletTVWearable

setHomeWidthRange(minPercent: number, maxPercent: number): void

设置主页宽度可拖动范围。应用不设置的情况下宽度为50%，且不可拖动。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minPercent | number | 是 | 最小主页宽度百分比。  取值范围：[0, 100] |
| maxPercent | number | 是 | 最大主页宽度百分比。  取值范围：[0, 100] |

### keepBottomPage

PhonePC/2in1TabletTVWearable

keepBottomPage(keepBottom: boolean): void

设置在调用pop和clear接口时是否保留栈底页面。

说明

MultiNavigation将主页也当作了NavDestination页面入栈，所以调用pop或clear接口时会将栈底页面也出栈。

应用调用此接口并设置为TRUE时，MultiNavigation会在调用pop和clear接口时保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keepBottom | boolean | 是 | 是否保留栈底页面。  默认值：false  true：保留栈底页面。  false：不保留栈底页面。 |

### setPlaceholderPage

PhonePC/2in1TabletTVWearable

setPlaceholderPage(info: NavPathInfo): void

设置占位页面。

说明

占位页面为特殊页面类型，当应用设置后，在一些大屏设备上会和主页默认形成左右分栏的效果，即左边主页，右边占位页。

当应用可绘制区域小于600VP、折叠屏由展开态切换为折叠态及平板横屏转竖屏等场景时，会自动将占位页出栈，只显示主页；

而当应用可绘制区域大于等于600VP、折叠屏由折叠态切换为展开态及平板竖屏转横屏等场景时，会自动补充占位页，形成分栏。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | 占位页页面信息。 |

## SplitPolicy枚举说明

PhonePC/2in1TabletTVWearable

表示MultiNavigation中页面的类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HOME\_PAGE | 0 | 主页页面类型。全屏模式显示。 |
| DETAIL\_PAGE | 1 | 详情页页面类型。分栏模式显示。 |
| FULL\_PAGE | 2 | 全屏页页面类型。全屏模式显示。 |

## NavDestinationBuildFunction

PhonePC/2in1TabletTVWearable

type NavDestinationBuildFunction = (name: string, param?: object) => void

MultiNavigation用以加载NavDestination的方法。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 路由页面的标识符。 |
| param | object | 否 | 路由跳转创建页面时传递的参数。 |

## OnNavigationModeChangeCallback

PhonePC/2in1TabletTVWearable

type OnNavigationModeChangeCallback = (mode: NavigationMode) => void

当MultiNavigation的mode变化时触发的回调函数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [NavigationMode](ts-basic-components-navigation.md#navigationmode9枚举说明) | 是 | 当回调触发时的NavigationMode。 |

## OnHomeShowOnTopCallback

PhonePC/2in1TabletTVWearable

type OnHomeShowOnTopCallback = (name: string) => void

当主页在栈顶显示时触发的回调函数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 显示在栈顶的页面的标识符。 |

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

本示例演示MultiNavigation的基本功能。

```
1. // pages/Index.ets
2. import { MultiNavigation, MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
3. import { PageDetail1 } from './PageDetail1';
4. import { PageDetail2 } from './PageDetail2';
5. import { PageFull1 } from './PageFull1';
6. import { PageHome1 } from './PageHome1';
7. import { PagePlaceholder } from './PagePlaceholder';

9. @Entry
10. @Component
11. struct Index {
12. @Provide('pageStack') pageStack: MultiNavPathStack = new MultiNavPathStack();

14. @Builder
15. PageMap(name: string, param?: object) {
16. if (name === 'PageHome1') {
17. PageHome1({ param: param });
18. } else if (name === 'PageDetail1') {
19. PageDetail1({ param: param });
20. } else if (name === 'PageDetail2') {
21. PageDetail2({ param: param });
22. } else if (name === 'PageFull1') {
23. PageFull1();
24. } else if (name === 'PagePlaceholder') {
25. PagePlaceholder();
26. }
27. }

29. aboutToAppear(): void {
30. this.pageStack.pushPathByName('PageHome1', 'paramTest', false, SplitPolicy.HOME_PAGE);
31. }

33. build() {
34. Column() {
35. Row() {
36. MultiNavigation({ navDestination: this.PageMap, multiStack: this.pageStack })
37. }
38. .width('100%')
39. }
40. }
41. }
```

```
1. // pages/PageHome1.ets, 对应首页
2. import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Component
6. export struct PageHome1 {
7. @State message: string = 'PageHome1';
8. @Consume('pageStack') pageStack: MultiNavPathStack;
9. controller: TextInputController = new TextInputController();
10. text: string = '';
11. param: Object = new Object();
12. lastBackTime: number = 0;

14. build() {
15. if (this.log()) {
16. NavDestination() {
17. Column() {
18. Column() {
19. Text(this.message)
20. .fontSize(40)
21. .fontWeight(FontWeight.Bold)
22. }
23. .width('100%')
24. .height('8%')
25. Scroll(){
26. Column() {
27. Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule})
28. .width('50%')
29. .height(40)
30. .margin(20)
31. .onClick(() => {
32. if (this.pageStack !== undefined && this.pageStack !== null) {
33. // 跳转至PageHome1页面
34. this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
35. }
36. })
37. Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule})
38. .width('50%')
39. .height(40)
40. .margin(20)
41. .onClick(() => {
42. if (this.pageStack !== undefined && this.pageStack !== null) {
43. // 跳转至PageDetail1页面
44. this.pageStack.pushPathByName('PageDetail1', 'testParam');
45. }
46. })
47. Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule})
48. .width('50%')
49. .height(40)
50. .margin(20)
51. .onClick(() => {
52. if (this.pageStack !== undefined && this.pageStack !== null) {
53. // 跳转至PageFull1页面
54. this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
55. }
56. })
57. TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
58. .placeholderColor(Color.Grey)
59. .placeholderFont({ size: 14, weight: 400 })
60. .caretColor(Color.Blue)
61. .width('50%')
62. .height(40)
63. .margin(20)
64. .type(InputType.Number)
65. .fontSize(14)
66. .fontColor(Color.Black)
67. .onChange((value: string) => {
68. this.text = value;
69. })
70. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule})
71. .width('50%')
72. .height(40)
73. .margin(20)
74. .onClick(() => {
75. if (this.pageStack !== undefined && this.pageStack !== null) {
76. // 返回至指定index页面，删除大于该index的所有页面
77. this.pageStack.popToIndex(Number(this.text));
78. this.controller.caretPosition(1);
79. }
80. })
81. Button('OpenDetailWithName', { stateEffect: true, type: ButtonType.Capsule})
82. .width('50%')
83. .height(40)
84. .margin(20)
85. .onClick(() => {
86. if (this.pageStack !== undefined && this.pageStack !== null) {
87. // 跳转至PageDetail1页面
88. this.pageStack.pushPathByName('PageDetail1', 'testParam', undefined, true);
89. }
90. })
91. Button('pop', { stateEffect: true, type: ButtonType.Capsule})
92. .width('50%')
93. .height(40)
94. .margin(20)
95. .onClick(() => {
96. if (this.pageStack !== undefined && this.pageStack !== null) {
97. this.pageStack.pop();
98. }
99. })
100. Button('moveToTopByName: PageDetail1', { stateEffect: true, type: ButtonType.Capsule})
101. .width('50%')
102. .height(40)
103. .margin(10)
104. .onClick(() => {
105. if (this.pageStack !== undefined && this.pageStack !== null) {
106. // 将PageDetail1页面移动至栈顶
107. let indexFound = this.pageStack.moveToTop('PageDetail1');
108. hilog.info(0x0000, 'demoTest', 'moveToTopByName,indexFound:' + indexFound);
109. }
110. })
111. Button('removeByName HOME', { stateEffect: true, type: ButtonType.Capsule})
112. .width('50%')
113. .height(40)
114. .margin(20)
115. .onClick(() => {
116. if (this.pageStack !== undefined && this.pageStack !== null) {
117. // 删除名称为PageHome1的页面
118. this.pageStack.removeByName('PageHome1');
119. }
120. })
121. Button('removeByIndexes 0135', { stateEffect: true, type: ButtonType.Capsule})
122. .width('50%')
123. .height(40)
124. .margin(20)
125. .onClick(() => {
126. if (this.pageStack !== undefined && this.pageStack !== null) {
127. // 删除栈中index为0，1，3，5的页面
128. this.pageStack.removeByIndexes([0,1,3,5]);
129. }
130. })
131. Button('getAllPathName', { stateEffect: true, type: ButtonType.Capsule})
132. .width('50%')
133. .height(40)
134. .margin(20)
135. .onClick(() => {
136. if (this.pageStack !== undefined && this.pageStack !== null) {
137. let result = this.pageStack.getAllPathName();
138. hilog.info(0x0000, 'demoTest', 'getAllPathName: ' + result.toString());
139. }
140. })
141. Button('getParamByIndex0', { stateEffect: true, type: ButtonType.Capsule})
142. .width('50%')
143. .height(40)
144. .margin(20)
145. .onClick(() => {
146. if (this.pageStack !== undefined && this.pageStack !== null) {
147. // 获取index为0的页面的参数
148. let result = this.pageStack.getParamByIndex(0);
149. hilog.info(0x0000, 'demoTest', 'getParamByIndex: ' + result);
150. }
151. })
152. Button('getParamByNameHomePage', { stateEffect: true, type: ButtonType.Capsule})
153. .width('50%')
154. .height(40)
155. .margin(20)
156. .onClick(() => {
157. if (this.pageStack !== undefined && this.pageStack !== null) {
158. // 获取名称为PageHome1的页面的参数
159. let result = this.pageStack.getParamByName('PageHome1');
160. hilog.info(0x0000, 'demoTest', 'getParamByName: ' + result.toString());
161. }
162. })
163. Button('getIndexByNameHomePage', { stateEffect: true, type: ButtonType.Capsule})
164. .width('50%')
165. .height(40)
166. .margin(20)
167. .onClick(() => {
168. if (this.pageStack !== undefined && this.pageStack !== null) {
169. // 获取名称为PageHome1的页面的Index
170. let result = this.pageStack.getIndexByName('PageHome1');
171. hilog.info(0x0000, 'demoTest', 'getIndexByName: ' + result);
172. }
173. })
174. Button('keepBottomPage True', { stateEffect: true, type: ButtonType.Capsule})
175. .width('50%')
176. .height(40)
177. .margin(10)
178. .onClick(() => {
179. if (this.pageStack !== undefined && this.pageStack !== null) {
180. // 设置栈底页面无法被移除
181. this.pageStack.keepBottomPage(true);
182. }
183. })
184. Button('keepBottomPage False', { stateEffect: true, type: ButtonType.Capsule})
185. .width('50%')
186. .height(40)
187. .margin(10)
188. .onClick(() => {
189. if (this.pageStack !== undefined && this.pageStack !== null) {
190. // 设置栈底页面可以被移除
191. this.pageStack.keepBottomPage(false);
192. }
193. })
194. Button('setPlaceholderPage', { stateEffect: true, type: ButtonType.Capsule})
195. .width('50%')
196. .height(40)
197. .margin(10)
198. .onClick(() => {
199. if (this.pageStack !== undefined && this.pageStack !== null) {
200. this.pageStack.setPlaceholderPage({ name: 'PagePlaceholder' });
201. }
202. })
203. }.backgroundColor(0xFFFFFF).width('100%').padding(10).borderRadius(15)
204. }
205. .width('100%')
206. }
207. .width('100%')
208. .height('92%')
209. }.hideTitleBar(true)
210. }
211. }

213. log(): boolean {
214. hilog.info(0x0000, 'demoTest', 'PageHome1 build called');
215. return true;
216. }
217. }
```

```
1. // pages/PageDetail1.ets：详情页
2. import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Component
6. export struct PageDetail1 {
7. @State message: string = 'PageDetail1';
8. @Consume('pageStack') pageStack: MultiNavPathStack;
9. controller: TextInputController = new TextInputController();
10. text: string = '';
11. param: Object = new Object();

13. build() {
14. if (this.log()) {
15. NavDestination() {
16. Column() {
17. Column() {
18. Text(this.message)
19. .fontSize(40)
20. .fontWeight(FontWeight.Bold)
21. }
22. .height('8%')
23. .width('100%')
24. Scroll(){
25. Column(){
26. Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule})
27. .width('50%')
28. .height(40)
29. .margin(20)
30. .onClick(() => {
31. if (this.pageStack !== undefined && this.pageStack !== null) {
32. // 跳转至PageHome1页面
33. this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
34. }
35. })
36. Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule})
37. .width('50%')
38. .height(40)
39. .margin(20)
40. .onClick(() => {
41. if (this.pageStack !== undefined && this.pageStack !== null) {
42. // 跳转至PageDetail1页面
43. this.pageStack.pushPathByName('PageDetail1', 'testParam');
44. }
45. })
46. Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule})
47. .width('50%')
48. .height(40)
49. .margin(20)
50. .onClick(() => {
51. if (this.pageStack !== undefined && this.pageStack !== null) {
52. // 跳转至PageFull1页面
53. this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
54. }
55. })
56. Button('ReplaceDetail', { stateEffect: true, type: ButtonType.Capsule})
57. .width('50%')
58. .height(40)
59. .margin(20)
60. .onClick(() => {
61. if (this.pageStack !== undefined && this.pageStack !== null) {
62. // 使用PageDetail2替换当前页面
63. this.pageStack.replacePathByName('PageDetail2', 'testParam');
64. }
65. })
66. Button('removeByName PageDetail1', { stateEffect: true, type: ButtonType.Capsule})
67. .width('50%')
68. .height(40)
69. .margin(20)
70. .onClick(() => {
71. if (this.pageStack !== undefined && this.pageStack !== null) {
72. // 删除栈中name为PageDetail1的页面
73. this.pageStack.removeByName('PageDetail1');
74. }
75. })
76. Button('removeByIndexes 0135', { stateEffect: true, type: ButtonType.Capsule})
77. .width('50%')
78. .height(40)
79. .margin(20)
80. .onClick(() => {
81. if (this.pageStack !== undefined && this.pageStack !== null) {
82. // 删除栈中index为0，1，3，5的页面
83. this.pageStack.removeByIndexes([0,1,3,5]);
84. }
85. })
86. Button('switchFullScreenState true', { stateEffect: true, type: ButtonType.Capsule})
87. .width('50%')
88. .height(40)
89. .margin(20)
90. .onClick(() => {
91. if (this.pageStack !== undefined && this.pageStack !== null) {
92. // 将页面设置为全屏
93. this.pageStack.switchFullScreenState(true);
94. }
95. })
96. Button('switchFullScreenState false', { stateEffect: true, type: ButtonType.Capsule})
97. .width('50%')
98. .height(40)
99. .margin(20)
100. .onClick(() => {
101. if (this.pageStack !== undefined && this.pageStack !== null) {
102. // 将页面设置为非全屏
103. this.pageStack.switchFullScreenState(false);
104. }
105. })
106. Button('pop', { stateEffect: true, type: ButtonType.Capsule})
107. .width('50%')
108. .height(40)
109. .margin(20)
110. .onClick(() => {
111. if (this.pageStack !== undefined && this.pageStack !== null) {
112. this.pageStack.pop('123');
113. }
114. })
115. Button('popToHome1', { stateEffect: true, type: ButtonType.Capsule})
116. .width('50%')
117. .height(40)
118. .margin(20)
119. .onClick(() => {
120. if (this.pageStack !== undefined && this.pageStack !== null) {
121. // 返回至指定name的页面，删除大于该页面index的所有其他页面
122. this.pageStack.popToName('PageHome1');
123. }
124. })
125. TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
126. .placeholderColor(Color.Grey)
127. .placeholderFont({ size: 14, weight: 400 })
128. .caretColor(Color.Blue)
129. .type(InputType.Number)
130. .width('50%')
131. .height(40)
132. .margin(20)
133. .fontSize(14)
134. .fontColor(Color.Black)
135. .onChange((value: string) => {
136. this.text = value;
137. })
138. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule})
139. .width('50%')
140. .height(40)
141. .margin(20)
142. .onClick(() => {
143. if (this.pageStack !== undefined && this.pageStack !== null) {
144. // 返回至指定index页面，删除大于该index的所有页面
145. this.pageStack.popToIndex(Number(this.text));
146. this.controller.caretPosition(1);
147. }
148. })
149. Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule})
150. .width('50%')
151. .height(40)
152. .margin(20)
153. .onClick(() => {
154. if (this.pageStack !== undefined && this.pageStack !== null) {
155. // 将指定Index页面移动至栈顶
156. this.pageStack.moveIndexToTop(Number(this.text));
157. this.controller.caretPosition(1);
158. }
159. })
160. Button('clear', { stateEffect: true, type: ButtonType.Capsule})
161. .width('50%')
162. .height(40)
163. .margin(20)
164. .onClick(() => {
165. if (this.pageStack !== undefined && this.pageStack !== null) {
166. // 清空当前路由栈
167. this.pageStack.clear();
168. }
169. })
170. Button('disableAnimation', { stateEffect: true, type: ButtonType.Capsule})
171. .width('50%')
172. .height(40)
173. .margin(20)
174. .onClick(() => {
175. if (this.pageStack !== undefined && this.pageStack !== null) {
176. // 关闭当前栈对应栈操作的动画
177. this.pageStack.disableAnimation(true);
178. }
179. })
180. Button('enableAnimation', { stateEffect: true, type: ButtonType.Capsule})
181. .width('50%')
182. .height(40)
183. .margin(20)
184. .onClick(() => {
185. if (this.pageStack !== undefined && this.pageStack !== null) {
186. // 开启当前栈对应栈操作的动画
187. this.pageStack.disableAnimation(false);
188. }
189. })
190. Button('setHomeWidthRange(20, 80)', { stateEffect: true, type: ButtonType.Capsule})
191. .width('50%')
192. .height(40)
193. .margin(20)
194. .onClick(() => {
195. if (this.pageStack !== undefined && this.pageStack !== null) {
196. this.pageStack.setHomeWidthRange(20, 80);
197. }
198. })
199. Button('setHomeWidthRange(-1, 20)', { stateEffect: true, type: ButtonType.Capsule})
200. .width('50%')
201. .height(40)
202. .margin(20)
203. .onClick(() => {
204. if (this.pageStack !== undefined && this.pageStack !== null) {
205. this.pageStack.setHomeWidthRange(-1, 20);
206. }
207. })
208. Button('setHomeWidthRange(20, 120)', { stateEffect: true, type: ButtonType.Capsule})
209. .width('50%')
210. .height(40)
211. .margin(20)
212. .onClick(() => {
213. if (this.pageStack !== undefined && this.pageStack !== null) {
214. this.pageStack.setHomeWidthRange(20, 120);
215. }
216. })
217. }
218. .width('100%')
219. }
220. .width('100%')
221. .height('92%')
222. }
223. }.hideTitleBar(true)
224. }
225. }

227. log(): boolean {
228. hilog.info(0x0000, 'demoTest', 'PageDetail1 build called');
229. return true;
230. }
231. }
```

```
1. // pages/PageDetail2.ets: 详情页
2. import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Component
6. export struct PageDetail2 {
7. @State message: string = 'PageDetail2';
8. @Consume('pageStack') pageStack: MultiNavPathStack;
9. controller: TextInputController = new TextInputController();
10. text: string = '';
11. param: Object = new Object();

13. build() {
14. if (this.log()) {
15. NavDestination() {
16. Column() {
17. Column() {
18. Text(this.message)
19. .fontSize(40)
20. .fontWeight(FontWeight.Bold)
21. }
22. .width('100%')
23. .height('8%')
24. Scroll(){
25. Column() {
26. Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule})
27. .width('50%')
28. .height(40)
29. .margin(20)
30. .onClick(() => {
31. if (this.pageStack !== undefined && this.pageStack !== null) {
32. // 跳转至PageHome1页面
33. this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
34. }
35. })
36. Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule})
37. .width('50%')
38. .height(40)
39. .margin(20)
40. .onClick(() => {
41. if (this.pageStack !== undefined && this.pageStack !== null) {
42. // 跳转至PageDetail1页面
43. this.pageStack.pushPathByName('PageDetail1', 'testParam');
44. }
45. })
46. Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule})
47. .width('50%')
48. .height(40)
49. .margin(20)
50. .onClick(() => {
51. if (this.pageStack !== undefined && this.pageStack !== null) {
52. // 跳转至PageFull1页面
53. this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
54. }
55. })
56. Button('ReplaceDetail', { stateEffect: true, type: ButtonType.Capsule})
57. .width('50%')
58. .height(40)
59. .margin(20)
60. .onClick(() => {
61. if (this.pageStack !== undefined && this.pageStack !== null) {
62. // 使用PageDetail2替换当前页面
63. this.pageStack.replacePathByName('PageDetail2', 'testParam');
64. }
65. })
66. TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
67. .placeholderColor(Color.Grey)
68. .placeholderFont({ size: 14, weight: 400 })
69. .caretColor(Color.Blue)
70. .type(InputType.Number)
71. .width('50%')
72. .height(40)
73. .margin(20)
74. .fontSize(14)
75. .fontColor(Color.Black)
76. .onChange((value: string) => {
77. this.text = value;
78. })
79. Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule})
80. .width('50%')
81. .height(40)
82. .margin(20)
83. .onClick(() => {
84. if (this.pageStack !== undefined && this.pageStack !== null) {
85. // 将指定index的页面移动至栈顶
86. this.pageStack.moveIndexToTop(Number(this.text));
87. this.controller.caretPosition(1);
88. }
89. })
90. Button('pop', { stateEffect: true, type: ButtonType.Capsule})
91. .width('50%')
92. .height(40)
93. .margin(20)
94. .onClick(() => {
95. if (this.pageStack !== undefined && this.pageStack !== null) {
96. this.pageStack.pop();
97. }
98. })
99. TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
100. .placeholderColor(Color.Grey)
101. .placeholderFont({ size: 14, weight: 400 })
102. .caretColor(Color.Blue)
103. .type(InputType.Number)
104. .width('50%')
105. .height(40)
106. .margin(20)
107. .fontSize(14)
108. .fontColor(Color.Black)
109. .onChange((value: string) => {
110. this.text = value;
111. })
112. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule})
113. .width('50%')
114. .height(40)
115. .margin(20)
116. .onClick(() => {
117. if (this.pageStack !== undefined && this.pageStack !== null) {
118. // 返回至指定index页面，删除大于该index的所有页面
119. this.pageStack.popToIndex(Number(this.text));
120. this.controller.caretPosition(1);
121. }
122. })
123. Button('clear', { stateEffect: true, type: ButtonType.Capsule})
124. .width('50%')
125. .height(40)
126. .margin(20)
127. .onClick(() => {
128. if (this.pageStack !== undefined && this.pageStack !== null) {
129. // 清空当前路由栈
130. this.pageStack.clear();
131. }
132. })
133. Button('disableAnimation', { stateEffect: true, type: ButtonType.Capsule})
134. .width('50%')
135. .height(40)
136. .margin(20)
137. .onClick(() => {
138. if (this.pageStack !== undefined && this.pageStack !== null) {
139. // 关闭当前栈对应栈操作的动画
140. this.pageStack.disableAnimation(true);
141. }
142. })
143. Button('enableAnimation', { stateEffect: true, type: ButtonType.Capsule})
144. .width('50%')
145. .height(40)
146. .margin(20)
147. .onClick(() => {
148. if (this.pageStack !== undefined && this.pageStack !== null) {
149. // 开启当前栈对应栈操作的动画
150. this.pageStack.disableAnimation(false);
151. }
152. })
153. }
154. .width('100%')
155. }
156. .width('100%')
157. .height('92%')
158. }
159. }
160. .hideTitleBar(true)
161. }
162. }

164. log(): boolean {
165. hilog.info(0x0000, 'demoTest', 'PageDetail2 build called');
166. return true;
167. }
168. }
```

```
1. // pages/PageFull1.ets: 不参与分栏的页面，默认全屏展示
2. import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Component
6. export struct PageFull1 {
7. @State message: string = 'PageFull1';
8. @Consume('pageStack') pageStack: MultiNavPathStack;
9. controller: TextInputController = new TextInputController();
10. text: string = '';

12. build() {
13. if (this.log()) {
14. NavDestination() {
15. Column() {
16. Column() {
17. Text(this.message)
18. .fontSize(40)
19. .fontWeight(FontWeight.Bold)
20. }
21. .width('100%')
22. .height('8%')

24. Scroll() {
25. Column() {
26. Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule })
27. .width('50%')
28. .height(40)
29. .margin(20)
30. .onClick(() => {
31. if (this.pageStack !== undefined && this.pageStack !== null) {
32. // 跳转至PageHome1页面
33. this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
34. }
35. })
36. Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule })
37. .width('50%')
38. .height(40)
39. .margin(20)
40. .onClick(() => {
41. if (this.pageStack !== undefined && this.pageStack !== null) {
42. // 跳转至PageDetail1页面
43. this.pageStack.pushPathByName('PageDetail1', 'testParam');
44. }
45. })
46. Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule })
47. .width('50%')
48. .height(40)
49. .margin(20)
50. .onClick(() => {
51. if (this.pageStack !== undefined && this.pageStack !== null) {
52. // 跳转至PageFull1页面
53. this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
54. }
55. })
56. Button('ReplaceFULL', { stateEffect: true, type: ButtonType.Capsule })
57. .width('50%')
58. .height(40)
59. .margin(20)
60. .onClick(() => {
61. if (this.pageStack !== undefined && this.pageStack !== null) {
62. // 使用PageFull1页面替换当前页面
63. this.pageStack.replacePathByName('PageFull1', 'testParam', true);
64. }
65. })
66. Button('removeByName PageFull1', { stateEffect: true, type: ButtonType.Capsule })
67. .width('50%')
68. .height(40)
69. .margin(20)
70. .onClick(() => {
71. if (this.pageStack !== undefined && this.pageStack !== null) {
72. // 删除栈中name为PageFull1的页面
73. this.pageStack.removeByName('PageFull1');
74. }
75. })
76. Button('removeByIndexes 0135', { stateEffect: true, type: ButtonType.Capsule })
77. .width('50%')
78. .height(40)
79. .margin(20)
80. .onClick(() => {
81. if (this.pageStack !== undefined && this.pageStack !== null) {
82. // 删除栈中index为0，1，3，5的页面
83. this.pageStack.removeByIndexes([0, 1, 3, 5]);
84. }
85. })
86. Button('pop', { stateEffect: true, type: ButtonType.Capsule })
87. .width('50%')
88. .height(40)
89. .margin(20)
90. .onClick(() => {
91. if (this.pageStack !== undefined && this.pageStack !== null) {
92. this.pageStack.pop();
93. }
94. })
95. TextInput({ placeholder: 'input your popToIndex ...', controller: this.controller })
96. .placeholderColor(Color.Grey)
97. .placeholderFont({ size: 14, weight: 400 })
98. .caretColor(Color.Blue)
99. .width('50%')
100. .height(40)
101. .margin(20)
102. .type(InputType.Number)
103. .fontSize(14)
104. .fontColor(Color.Black)
105. .onChange((value: string) => {
106. this.text = value;
107. })
108. Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
109. .width('50%')
110. .height(40)
111. .margin(20)
112. .onClick(() => {
113. if (this.pageStack !== undefined && this.pageStack !== null) {
114. this.pageStack.popToIndex(Number(this.text));
115. this.controller.caretPosition(1);
116. }
117. })
118. }
119. .width('100%')
120. }
121. .width('100%')
122. .height('92%')
123. }
124. }
125. .hideTitleBar(true)
126. .onBackPressed(() => {
127. hilog.info(0x0000, 'demoTest', 'PageFull1 onBackPressed: ');
128. return false;
129. })
130. }
131. }

133. log(): boolean {
134. hilog.info(0x0000, 'demoTest', 'PageFull1 build called');
135. return true;
136. }
137. }
```

```
1. // pages/PagePlaceholder.ets: 占位页
2. import { MultiNavPathStack } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Component
6. export struct PagePlaceholder {
7. @State message: string = 'PagePlaceholder';
8. @Consume('pageStack') pageStack: MultiNavPathStack;
9. controller: TextInputController = new TextInputController();
10. text: string = '';
11. lastBackTime: number = 0;

13. build() {
14. if (this.log()) {
15. NavDestination() {
16. Column() {
17. Column() {
18. Text(this.message)
19. .fontSize(50)
20. .fontWeight(FontWeight.Bold)
21. }
22. .width('100%')
23. .height('8%')

25. Stack({alignContent: Alignment.Center}) {
26. Text('Placeholder示例页面')
27. .fontSize(80)
28. .fontWeight(FontWeight.Bold)
29. .fontColor(Color.Red)
30. }
31. .width('100%')
32. .height('92%')
33. }
34. }.hideTitleBar(true)
35. }
36. }

38. log(): boolean {
39. hilog.info(0x0000, 'demoTest', 'PagePlaceholder build called');
40. return true;
41. }
42. }
```

分栏效果演示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/OuGBBm_5QUmwiVqS76P6hA/zh-cn_image_0000002583479675.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=C4930671B7EEB1095405F469D602622228D944CD5A3BCC767A44611B59C1E5D8)

主页跳转详情页效果演示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/b7D01izMQc-lxu1ADFPoAQ/zh-cn_image_0000002552800026.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=254269FF9A01B3B2B697489F0C55C2EAFBA26FF921302E87EDA52484BE532002)

全屏类型页面效果演示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Aw4YcuN4SfyNqKko7sMCkg/zh-cn_image_0000002583439721.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=EAF8AEAD541281C9E1DFC1F82BC7DFFB1D1AE48D4EF58B23AC70C7450967D219)
