---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-navpushpathhelper
title: NavPushPathHelper
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > NavPushPathHelper
category: harmonyos-references
scraped_at: 2026-04-29T13:52:53+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:7e1c6755e488e491523ae904d8b3282cc3380aadbebb6c0bbc51fa4adfc24d57
---

当跳转的目标[NavDestination](ts-basic-components-navdestination.md)在不同的hsp分包，且未被主包依赖，首次运行元服务只会下载安装主包，需要使用NavPushPathHelper先下载安装相应hsp分包，再将指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈。使[Navigation](ts-basic-components-navigation.md)支持动态加载hsp分包后再跳转。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { NavPushPathHelper } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)

## NavPushPathHelper

PhonePC/2in1TabletTVWearable

对Navigation路由栈[NavPathStack](ts-basic-components-navigation.md#navpathstack10)的所有路由跳转接口进行了封装，在NavPushPathHelper中持有一个NavPathStack对象，在封装的跳转接口中，去判断子包是否存在，如果不存在则进行动态下载子包，等结果返回后调用NavPathStack的相应的接口将指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈。使用示例参见[示例](ohos-atomicservice-navpushpathhelper.md#示例)。

### constructor

PhonePC/2in1TabletTVWearable

constructor(navPathStack: NavPathStack)

NavPushPathHelper的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| navPathStack | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 是 | [Navigation](ts-basic-components-navigation.md)路由栈。 |

### pushPath

PhonePC/2in1TabletTVWearable

pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | [NavDestination](ts-basic-components-navdestination.md)页面的信息。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[页面路由错误码](errorcode-router.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 300001 | hsp silent install fail. |

### pushPath

PhonePC/2in1TabletTVWearable

pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，使用Promise异步回调。

具体根据options中指定不同的[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)，有不同的行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | [NavDestination](ts-basic-components-navdestination.md)页面的信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 页面栈操作选项。默认值为{ launchMode: LaunchMode.STANDARD, animated: true }。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[页面路由错误码](errorcode-router.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 300001 | hsp silent install fail. |

### pushPathByName

PhonePC/2in1TabletTVWearable

pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，传递的数据为param，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| name | string | 是 | [NavDestination](ts-basic-components-navdestination.md)页面名称。 |
| param | Object | 是 | [NavDestination](ts-basic-components-navdestination.md)页面详细参数。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[页面路由错误码](errorcode-router.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 300001 | hsp silent install fail. |

### pushPathByName

PhonePC/2in1TabletTVWearable

pushPathByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| name | string | 是 | [NavDestination](ts-basic-components-navdestination.md)页面名称。 |
| param | Object | 是 | [NavDestination](ts-basic-components-navdestination.md)页面详细参数。 |
| onPop | Callback<[PopInfo](ts-basic-components-navigation.md#popinfo11)> | 是 | Callback回调，用于页面出栈时触发该回调处理返回结果。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[页面路由错误码](errorcode-router.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 300001 | hsp silent install fail. |

### pushDestination

PhonePC/2in1TabletTVWearable

pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | [NavDestination](ts-basic-components-navdestination.md)页面的信息。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

### pushDestination

PhonePC/2in1TabletTVWearable

pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将info指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，使用Promise异步回调。

具体根据options中指定不同的[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)，有不同的行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | [NavDestination](ts-basic-components-navdestination.md)页面的信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 页面栈操作选项。默认值为{ launchMode: LaunchMode.STANDARD, animated: true }。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

### pushDestinationByName

PhonePC/2in1TabletTVWearable

pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，传递的数据为param，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| name | string | 是 | [NavDestination](ts-basic-components-navdestination.md)页面名称。 |
| param | Object | 是 | [NavDestination](ts-basic-components-navdestination.md)页面详细参数。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

### pushDestinationByName

PhonePC/2in1TabletTVWearable

pushDestinationByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将name指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，传递的数据为param，并且添加用于页面出栈时处理返回结果的OnPop回调，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| name | string | 是 | [NavDestination](ts-basic-components-navdestination.md)页面名称。 |
| param | Object | 是 | [NavDestination](ts-basic-components-navdestination.md)页面详细参数。 |
| onPop | Callback<[PopInfo](ts-basic-components-navigation.md#popinfo11)> | 是 | Callback回调，用于页面出栈时处理返回结果。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100005 | Builder function not registered. |
| 100006 | NavDestination not found. |
| 300001 | hsp silent install fail. |

### replacePath

PhonePC/2in1TabletTVWearable

replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将info指定的[NavDestination](ts-basic-components-navdestination.md)页面信息入栈，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | 新栈顶页面参数信息 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[页面路由错误码](errorcode-router.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 300001 | hsp silent install fail. |

### replacePath

PhonePC/2in1TabletTVWearable

replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，使用Promise异步回调。

具体根据options中指定不同的[LaunchMode](ts-basic-components-navigation.md#launchmode12枚举说明)，有不同的行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| info | [NavPathInfo](ts-basic-components-navigation.md#navpathinfo10) | 是 | 新栈顶页面参数信息。 |
| options | [NavigationOptions](ts-basic-components-navigation.md#navigationoptions12) | 否 | 页面栈操作选项。默认值为{ launchMode: LaunchMode.STANDARD, animated: true }。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[页面路由错误码](errorcode-router.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 300001 | hsp silent install fail. |

### replacePathByName

PhonePC/2in1TabletTVWearable

replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>

先判断分包是否存在，若不存在，则通过moduleName下载分包，再将当前页面栈栈顶退出，将name指定的页面入栈，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 目标[NavDestination](ts-basic-components-navdestination.md)所在分包的moduleName。 |
| name | string | 是 | [NavDestination](ts-basic-components-navdestination.md)页面名称。 |
| param | Object | 是 | [NavDestination](ts-basic-components-navdestination.md)页面详细参数。 |
| animated | boolean | 否 | 是否支持转场动画。  默认值：true。  true：支持转场动画。  false：不支持转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[页面路由错误码](errorcode-router.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 300001 | hsp silent install fail. |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)

## 示例

PhonePC/2in1TabletTVWearable

主包：

```
1. // Index.ets
2. import { NavPushPathHelper } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. @Entry
5. @Component
6. struct NavigationExample {
7. pageInfo: NavPathStack = new NavPathStack();
8. helper: NavPushPathHelper = new NavPushPathHelper(this.pageInfo);

10. build() {
11. Navigation(this.pageInfo) {
12. Column() {
13. Button('StartTest', { stateEffect: true, type: ButtonType.Capsule })
14. .width('80%')
15. .height(40)
16. .margin(20)
17. .onClick(() => {
18. this.helper.pushPath('hsptest1', { name: 'pageOne' }, false)
19. .catch((error: BusinessError) => {
20. console.error(`[pushPath]failed, error code = ${error.code}, error.message = ${error.message}.`);
21. }).then(() => {
22. console.error(`[pushPath]success.`);
23. }); // 将name指定的NavDestination页面信息入栈。
24. })
25. }
26. }.title('NavIndex')
27. }
28. }
```

分包hsptest1：

```
1. // PageOne.ets
2. import { NavPushPathHelper } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TmpClass {
6. count: number = 10;
7. }

9. class ParamWithOp {
10. operation: number = 1;
11. count: number = 10;
12. }

14. @Builder
15. export function PageOneBuilder(name: string, param: Object) {
16. PageOne();
17. }

19. @Component
20. export struct PageOne {
21. pageInfo: NavPathStack = new NavPathStack();
22. helper: NavPushPathHelper = new NavPushPathHelper(this.pageInfo);
23. @State message: string = 'Hello World';

25. build() {
26. NavDestination() {
27. Column() {
28. Text(this.message)
29. .width('80%')
30. .height(50)
31. .margin(10)

33. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
34. .width('80%')
35. .height(35)
36. .margin(10)
37. .onClick(() => {
38. this.helper.pushPath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
39. this.message = '[pushPath]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
40. }}).catch((error: BusinessError) => {
41. console.error(`[pushPath]failed, error code = ${error.code}, error.message = ${error.message}.`);
42. }).then(() => {
43. console.info(`[pushPath]success.`);
44. });
45. })

47. Button('pushPath with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
48. .width('80%')
49. .height(35)
50. .margin(10)
51. .onClick(() => {
52. this.helper.pushPath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
53. this.message = '[pushPath with NavigationOptions]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
54. }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
55. console.error(`[pushPath with NavigationOptions]failed, error code = ${error.code}, error.message = ${error.message}.`);
56. }).then(() => {
57. console.info(`[pushPath with NavigationOptions]success.`);
58. });
59. })

61. Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
62. .width('80%')
63. .height(35)
64. .margin(10)
65. .onClick(() => {
66. let tmp = new TmpClass();
67. this.helper.pushPathByName('hsptest2', 'pageTwo', tmp, (popInfo) => {
68. this.message = '[pushPathByName]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
69. }).catch((error: BusinessError) => {
70. console.error(`[pushPathByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
71. }).then(() => {
72. console.info(`[pushPathByName]success.`);
73. });
74. })

76. Button('pushPathByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
77. .width('80%')
78. .height(35)
79. .margin(10)
80. .onClick(() => {
81. let tmp = new TmpClass();
82. this.helper.pushPathByName('hsptest2', 'pageTwo', tmp, true)
83. .catch((error: BusinessError) => {
84. console.error(`[pushPathByNameWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
85. }).then(() => {
86. console.info(`[pushPathByNameWithoutOnPop]success.`);
87. });
88. })

90. Button('pushDestination', { stateEffect: true, type: ButtonType.Capsule })
91. .width('80%')
92. .height(35)
93. .margin(10)
94. .onClick(() => {
95. let tmp = new TmpClass()
96. this.helper.pushDestination('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
97. this.message = '[pushDestination]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
98. }}).catch((error: BusinessError) => {
99. console.error(`[pushDestination]failed, error code = ${error.code}, error.message = ${error.message}.`);
100. }).then(() => {
101. console.error(`[pushDestination]success.`);
102. });
103. })

105. Button('pushDestination with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
106. .width('80%')
107. .height(35)
108. .margin(10)
109. .onClick(() => {
110. let tmp = new TmpClass();
111. this.helper.pushDestination('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
112. this.message = '[pushDestination with NavigationOptions]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
113. }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
114. console.error(`[pushDestination with NavigationOptions]failed, error code = ${error.code}, error.message = ${error.message}.`);
115. }).then(() => {
116. console.error(`[pushDestination with NavigationOptions]success.`);
117. });
118. })

120. Button('pushDestinationByName', { stateEffect: true, type: ButtonType.Capsule })
121. .width('80%')
122. .height(35)
123. .margin(10)
124. .onClick(() => {
125. let tmp = new TmpClass()
126. this.helper.pushDestinationByName('hsptest2','pageTwo', tmp, (popInfo) => {
127. this.message = '[pushDestinationByName]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
128. }).catch((error: BusinessError) => {
129. console.error(`[pushDestinationByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
130. }).then(() => {
131. console.error(`[pushDestinationByName]success.`);
132. });
133. })

135. Button('pushDestinationByNameWithoutOnPop', { stateEffect: true, type: ButtonType.Capsule })
136. .width('80%')
137. .height(35)
138. .margin(10)
139. .onClick(() => {
140. let tmp = new TmpClass()
141. this.helper.pushDestinationByName('hsptest2','pageTwo', tmp, true)
142. .catch((error: BusinessError) => {
143. console.error(`[pushDestinationByNameWithoutOnPop]failed, error code = ${error.code}, error.message = ${error.message}.`);
144. }).then(() => {
145. console.error(`[pushDestinationByNameWithoutOnPop]success.`);
146. });
147. })

149. Button('replacePath', { stateEffect: true, type: ButtonType.Capsule })
150. .width('80%')
151. .height(35)
152. .margin(10)
153. .onClick(() => {
154. this.helper.replacePath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
155. this.message = '[replacePath]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
156. }}).catch((error: BusinessError) => {
157. console.error(`[replacePath]failed, error code = ${error.code}, error.message = ${error.message}.`);
158. }).then(() => {
159. console.info(`[replacePath]success.`);
160. });
161. })

163. Button('replacePath with NavigationOptions', { stateEffect: true, type: ButtonType.Capsule })
164. .width('80%')
165. .height(35)
166. .margin(10)
167. .onClick(() => {
168. this.helper.replacePath('hsptest2', { name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
169. this.message = '[replacePath with NavigationOptions]last page is: ' + popInfo.info.name + ', result: ' + JSON.stringify(popInfo.result);
170. }}, {launchMode:0, animated:true}).catch((error: BusinessError) => {
171. console.error(`[replacePath with NavigationOptions]failed, error code = ${error.code}, error.message = ${error.message}.`);
172. }).then(() => {
173. console.info(`[replacePath with NavigationOptions]success.`);
174. });
175. })

177. Button('replacePathByName', { stateEffect: true, type: ButtonType.Capsule })
178. .width('80%')
179. .height(35)
180. .margin(10)
181. .onClick(() => {
182. let tmp = new TmpClass();
183. this.helper.replacePathByName('hsptest2', 'pageTwo', tmp)
184. .catch((error: BusinessError) => {
185. console.error(`[replacePathByName]failed, error code = ${error.code}, error.message = ${error.message}.`);
186. }).then(() => {
187. console.info(`[replacePathByName]success.`);
188. });
189. })

191. }.width('100%').height('100%')
192. }.title('pageOne')
193. .onBackPressed(() => {
194. this.pageInfo.pop({ number: 1 }) // 弹出路由栈栈顶元素。
195. return true;
196. }).onReady((context: NavDestinationContext) => {
197. this.pageInfo = context.pathStack;
198. this.helper = new NavPushPathHelper(this.pageInfo);
199. })
200. }
201. }
```

工程配置文件module.json5中配置 {"routerMap": "$profile:route\_map"}，在route\_map.json文件配置如下：

```
1. {
2. "routerMap": [
3. {
4. "name": "pageOne",
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is pageOne"
9. }
10. }
11. ]
12. }
```

分包hsptest2：

```
1. // PageTwo.ets

3. class resultClass {
4. constructor(count: number) {
5. this.count = count;
6. }
7. count: number = 10
8. }

10. @Builder
11. export function PageTwoBuilder() {
12. PageTwo()
13. }

15. @Component
16. export struct PageTwo {
17. pathStack: NavPathStack = new NavPathStack()

19. build() {
20. NavDestination() {
21. Column() {
22. Button('pop', { stateEffect: true, type: ButtonType.Capsule })
23. .width('80%')
24. .height(40)
25. .margin(20)
26. .onClick(() => {
27. this.pathStack.pop(new resultClass(1)); // 回退到上一个页面，将处理结果传入push的onPop回调中。
28. })
29. }.width('100%').height('100%')
30. }.title('pageTwo')
31. .onBackPressed(() => {
32. this.pathStack.pop(new resultClass(0)); // 回退到上一个页面，将处理结果传入push的onPop回调。
33. return true;
34. }).onReady((context: NavDestinationContext) => {
35. this.pathStack = context.pathStack
36. })
37. }
38. }
```

工程配置文件module.json5中配置 {"routerMap": "$profile:route\_map"}，在route\_map.json文件配置如下：

```
1. {
2. "routerMap": [
3. {
4. "name": "pageTwo",
5. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
6. "buildFunction": "PageTwoBuilder",
7. "data": {
8. "description": "this is pageTwo"
9. }
10. }
11. ]
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/cPGe58WtSeCE83nwtQVuxA/zh-cn_image_0000002558606954.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055252Z&HW-CC-Expire=86400&HW-CC-Sign=A03DBF4082C7976CC9DFC9A0F445E29A994D6CD1028DAD3D553A84A355E7C896)
