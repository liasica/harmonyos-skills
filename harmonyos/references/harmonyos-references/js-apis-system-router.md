---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-router
title: @system.router (页面路由)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @system.router (页面路由)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bab0fdd5fd29f285f7b07032445f128e4ca10d53f01ac7ec78495b9c5ae000b9
---

通过不同的uri访问不同的页面。

说明

* 从API version 8 开始，该接口不再维护，推荐使用新接口[@ohos.router](js-apis-router.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearableLite Wearable

```
1. import router from '@system.router';
```

## router.push

PhonePC/2in1TabletTVWearable

push(options: RouterOptions): void

跳转到应用内的指定页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-system-router.md#routeroptions) | 是 | 页面路由参数，详细请参考RouterOptions。 |

**示例：**

```
1. // 在当前页面中
2. import router from '@system.router';
3. class A{
4. pushPage() {
5. router.push({
6. uri: 'pages/routerpage2/routerpage2',
7. params: {
8. data1: 'message',
9. data2: {
10. data3: [123, 456, 789]
11. }
12. }
13. });
14. }
15. }
16. export default new A()
```

```
1. // 在routerpage2页面中
2. class B{
3. data:Record<string,string> = {'data1': 'default'}
4. data2:Record<string,number[]> = {'data3': [1, 2, 3]}
5. onInit() {
6. console.info('showData1:' + this.data.data1);
7. console.info('showData3:' + this.data2.data3);
8. }
9. }
10. export default new B()
```

说明

页面路由栈支持的最大Page数量为32。

## router.replace

PhonePC/2in1TabletTVWearableLite Wearable

replace(options: RouterOptions): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-system-router.md#routeroptions) | 是 | 页面路由参数，详细请参考RouterOptions。 |

**示例：**

```
1. // 在当前页面中
2. import router from '@system.router';
3. class C{
4. replacePage() {
5. router.replace({
6. uri: 'pages/detail/detail',
7. params: {
8. data1: 'message'
9. }
10. });
11. }
12. }
13. export default new C()
```

```
1. // 在detail页面中
2. class Area {
3. data:Record<string,string> = {'data1': 'default'}
4. onInit() {
5. console.info(`showData1: ${JSON.stringify(this.data)}`);
6. }
7. }
8. export default new Area()
```

## router.back

PhonePC/2in1TabletTVWearable

back(options?: BackRouterOptions): void

返回上一页面或指定的页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [BackRouterOptions](js-apis-system-router.md#backrouteroptions) | 否 | 详细请参考BackRouterOptions。 |

**示例：**

```
1. // index页面
2. import router from '@system.router';
3. class D{
4. indexPushPage() {
5. router.push({
6. uri: 'pages/detail/detail'
7. });
8. }
9. }
10. export default new D()
```

```
1. // detail页面
2. import router from '@system.router';
3. class E{
4. detailPushPage() {
5. router.push({
6. uri: 'pages/mall/mall'
7. });
8. }
9. }
10. export default new E()
```

```
1. // mall页面通过back，将返回detail页面
2. import router from '@system.router';
3. class F{
4. mallBackPage() {
5. router.back();
6. }
7. }
8. export default new F()
```

```
1. // detail页面通过back，将返回index页面
2. import router from '@system.router';
3. class G{
4. defaultBack() {
5. router.back();
6. }
7. }
8. export default new G()
```

```
1. // 通过back，返回到detail页面
2. import router from '@system.router';
3. class H{
4. backToDetail() {
5. router.back({uri:'pages/detail/detail'});
6. }
7. }
8. export default new H()
```

说明

示例中的uri字段是页面路由，由配置文件中的pages列表指定。

## router.getParams7+

PhonePC/2in1TabletTVWearable

getParams(): ParamsInterface

获取当前页面的参数信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ParamsInterface](js-apis-system-router.md#paramsinterface) | 详细请参见ParamsInterface。 |

## router.clear

PhonePC/2in1TabletTVWearable

clear(): void

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import router from '@system.router';
2. class I{
3. clearPage() {
4. router.clear();
5. }
6. }
7. export default new I()
```

## router.getLength

PhonePC/2in1TabletTVWearable

getLength(): string

获取当前在页面栈内的页面数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 页面数量，页面栈支持最大数值是32。 |

**示例：**

```
1. import router from '@system.router';
2. class J{
3. getLength() {
4. let size = router.getLength();
5. console.info('pages stack size = ' + size);
6. }
7. }
8. export default new J()
```

## router.getState

PhonePC/2in1TabletTVWearable

getState(): RouterState

获取当前页面的状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 参数类型 | 说明 |
| --- | --- |
| [RouterState](js-apis-system-router.md#routerstate) | 详细请参见RouterState。 |

**示例：**

```
1. import router from '@system.router';
2. class K{
3. getState() {
4. let page = router.getState();
5. console.info('current index = ' + page.index);
6. console.info('current name = ' + page.name);
7. console.info('current path = ' + page.path);
8. }
9. }
10. export default new K()
```

## router.enableAlertBeforeBackPage6+

PhonePC/2in1TabletTVWearable

enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void

开启页面返回询问对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EnableAlertBeforeBackPageOptions](js-apis-system-router.md#enablealertbeforebackpageoptions6) | 是 | 详细请参见EnableAlertBeforeBackPageOptions。 |

**示例：**

```
1. import router from '@system.router';
2. class L{
3. enableAlertBeforeBackPage() {
4. router.enableAlertBeforeBackPage({
5. message: 'Message Info',
6. success: ()=> {
7. console.info('success');
8. },
9. cancel: ()=> {
10. console.info('cancel');
11. }
12. });
13. }
14. }
15. export default new L()
```

## router.disableAlertBeforeBackPage6+

PhonePC/2in1TabletTVWearable

disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void

禁用页面返回询问对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DisableAlertBeforeBackPageOptions](js-apis-system-router.md#disablealertbeforebackpageoptions6) | 否 | 详细请参见DisableAlertBeforeBackPageOptions。 |

**示例：**

```
1. import router from '@system.router';
2. class Z{
3. disableAlertBeforeBackPage() {
4. router.disableAlertBeforeBackPage({
5. success: ()=> {
6. console.info('success');
7. },
8. cancel: ()=> {
9. console.info('cancel');
10. }
11. });
12. }
13. }
14. export default new Z()
```

## RouterOptions

PhonePC/2in1TabletTVWearableLite Wearable

定义路由器的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 目标页面的uri，可以是以下的两种格式：  1. 页面的绝对路径，由config.json文件中的页面列表提供。例如：  - pages/index/index  - pages/detail/detail  2. 特定路径。如果URI为斜杠（/），则显示主页。 |
| params | Object | 否 | 表示路由跳转时要同时传递到目标页面的数据。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。 |

## BackRouterOptions

PhonePC/2in1TabletTVWearableLite Wearable

定义路由器返回的选项。

**系统能力：** 以下各项对应的系统能力有所不同，详见下表。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri7+ | string | 否 | 返回到指定uri的界面，如果页面栈上没有uri页面，则不响应该情况。如果uri未设置，则返回上一页。  **系统能力：** SystemCapability.ArkUI.ArkUI.Full |
| params7+ | object | 否 | 跳转时要同时传递到目标页面的数据。  **系统能力：** SystemCapability.ArkUI.ArkUI.Lite |

## RouterState

PhonePC/2in1TabletTVWearable

定义路由器的状态。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。 |
| name | string | 是 | 表示当前页面的名称，即对应文件名。 |
| path | string | 是 | 表示当前页面的路径。 |

## EnableAlertBeforeBackPageOptions6+

PhonePC/2in1TabletTVWearable

定义EnableAlertBeforeBackPage选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 询问对话框内容。 |
| success | (errMsg: string) => void | 否 | 用户选择对话框确认按钮时触发，errMsg表示返回信息。 |
| cancel | (errMsg: string) => void | 否 | 用户选择对话框取消按钮时触发，errMsg表示返回信息。 |
| complete | () => void | 否 | 当对话框关闭时触发该回调。 |

## DisableAlertBeforeBackPageOptions6+

PhonePC/2in1TabletTVWearable

定义DisableAlertBeforeBackPage参数选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (errMsg: string) => void | 否 | 关闭询问对话框能力成功时触发，errMsg表示返回信息。 |
| cancel | (errMsg: string) => void | 否 | 关闭询问对话框能力失败时触发，errMsg表示返回信息。 |
| complete | () => void | 否 | 当对话框关闭时触发该回调。 |

## ParamsInterface

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 参数类型 | 说明 |
| --- | --- | --- |
| [key: string] | object | 路由参数列表。 |
