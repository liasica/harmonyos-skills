---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-watch-monitor
title: 状态变量变化监听
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态变量变化监听
category: harmonyos-references
scraped_at: 2026-04-28T08:02:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc14eb74a7df8ed16c75dec99723b3e5a2415362a67cbb117d48b55aaf3ef9ad
---

状态变量监听模块提供了对状态变量变化的感知能力。

本文档仅为API参考说明。实际功能使用与限制见各接口对应的开发指南。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## Watch

PhonePC/2in1TabletTVWearable

Watch: (value: string) => PropertyDecorator

@Watch装饰器用于状态管理V1中对状态变量变化的监听。@Watch的详细使用方式见[@Watch装饰器：状态变量更改通知](../harmonyos-guides/arkts-watch.md)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 用于监听的回调函数名，内容由开发者指定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器，开发者无需关注该返回值。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. @State @Watch('onChange') num: number = 0; // @Watch入参为函数名

6. onChange() {
7. console.info(`num change to ${this.num}`);
8. }

10. build() {
11. Column() {
12. Text(`num is: ${this.num}`)
13. .onClick(() => {
14. this.num++; // 会触发onChange函数回调
15. })
16. }
17. }
18. }
```

## Monitor12+

PhonePC/2in1TabletTVWearable

Monitor: MonitorDecorator

@Monitor装饰器用于状态管理V2中对状态变量变化的监听。@Monitor相关内容的详细使用方式见[@Monitor装饰器：状态变量修改异步监听](../harmonyos-guides/arkts-new-monitor.md)。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## MonitorDecorator12+

PhonePC/2in1TabletTVWearable

type MonitorDecorator = (value: string, ...args: string[]) => MethodDecorator

@Monitor装饰器的实际类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 用于监听的变量名路径，内容由开发者指定。当开发者仅传入一个字符串时，入参为该类型。 |
| ...args | string[] | 否 | 用于监听的变量名路径数组，内容由开发者指定。当开发者传入多个字符串时，入参为该类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MethodDecorator | 方法装饰器，开发者无需关注该返回值。 |

**示例：**

```
1. @ObservedV2
2. class Info {
3. @Trace name: string = 'Tom';
4. @Trace age: number = 25;
5. @Trace height: number = 175;

7. // 监听一个变量
8. @Monitor('name')
9. onNameChange() {
10. console.info(`name change to ${this.name}`);
11. }

13. // 监听多个变量
14. @Monitor('age','height')
15. onRecordChange(monitor: IMonitor) {
16. monitor.dirty.forEach((path: string) => {
17. console.info(`${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
18. })
19. }
20. }

22. @Entry
23. @ComponentV2
24. struct Index {
25. @Local info: Info = new Info();

27. build() {
28. Column() {
29. Text(`info.name: ${this.info.name}`)
30. .onClick(() => {
31. this.info.name = 'Bob'; // 输出日志：name change to Bob
32. })
33. Text(`info.age: ${this.info.age}, info.height: ${this.info.height}`)
34. .onClick(() => {
35. this.info.age++; // 输出日志：age change from 25 to 26
36. this.info.height++; // 输出日志：height change from 175 to 176
37. })
38. }
39. }
40. }
```

## IMonitor12+

PhonePC/2in1TabletTVWearable

当监听的变量变化时，状态管理框架侧将回调开发者注册的函数，并传入变化信息。变化信息的类型即为IMonitor类型。

### 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dirty12+ | Array<string> | 否 | 否 | 变化路径的数组。 |

### value12+

PhonePC/2in1TabletTVWearable

value<T>(path?: string): IMonitorValue<T> | undefined

获取指定path的变化信息。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 否 | 可选，被监听的变量路径名。未指定时默认使用变化路径数组dirty中的第一个路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IMonitorValue<T>](ts-state-management-watch-monitor.md#imonitorvaluet12) | undefined | @Monitor监听变量的路径以及变化前后值信息。  T为监听变量的类型。  当监听的路径不存在时，返回undefined。  当未指定路径时，默认返回变化路径数组dirty中第一个路径对应的信息。 |

**示例：**

```
1. @ObservedV2
2. class Info {
3. @Trace name: string = 'Tom';
4. @Trace age: number = 25;
5. @Trace height: number = 175;

7. // 监听一个变量
8. @Monitor('name')
9. onNameChange(monitor: IMonitor) {
10. // 未指定value的入参时，默认使用dirty中的第一个路径作为入参
11. console.info(`path: ${monitor.value()?.path} change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
12. }

14. // 监听多个变量
15. @Monitor('age','height')
16. onRecordChange(monitor: IMonitor) {
17. // 指定value的入参时，将返回入参路径path对应的变量变化值信息
18. monitor.dirty.forEach((path: string) => {
19. console.info(`path: ${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
20. })
21. }
22. }

24. @Entry
25. @ComponentV2
26. struct Index {
27. @Local info: Info = new Info();

29. build() {
30. Column() {
31. Text(`info.name: ${this.info.name}`)
32. .onClick(() => {
33. this.info.name = 'Bob'; // 输出日志：path: name change from Tom to Bob
34. })
35. Text(`info.age: ${this.info.age}, info.height: ${this.info.height}`)
36. .onClick(() => {
37. this.info.age++; // 输出日志：path: age change from 25 to 26
38. this.info.height++; // 输出日志：path: height change from 175 to 176
39. })
40. }
41. }
42. }
```

## IMonitorValue<T>12+

PhonePC/2in1TabletTVWearable

@Monitor监听变量变化的具体信息，通过IMonitor的value接口获取。T为变量类型。

### 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| before12+ | T | 否 | 否 | 变量变化前的值。 |
| now12+ | T | 否 | 否 | 变量当前的值。 |
| path12+ | string | 否 | 否 | 变量的路径。 |

**示例：**

```
1. @ObservedV2
2. class Info {
3. @Trace name: string = 'Tom';
4. @Monitor('name')
5. onNameChange(monitor: IMonitor) {
6. // value的返回值为IMonitorValue类型，可以通过该返回值获取变量变化的信息
7. console.info(`path: ${monitor.value()?.path} change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
8. }
9. }
10. @Entry
11. @ComponentV2
12. struct Index {
13. @Local info: Info = new Info();
14. build() {
15. Column() {
16. Text(`info.name: ${this.info.name}`)
17. .onClick(() => {
18. this.info.name = 'Bob'; // 输出日志：path: name change from Tom to Bob
19. })
20. }
21. }
22. }
```

## SyncMonitor23+

PhonePC/2in1TabletTVWearable

SyncMonitor: MonitorDecorator

@SyncMonitor装饰器用于状态管理V2中对状态变量变化的监听。@SyncMonitor相关内容的详细使用方式见[@SyncMonitor装饰器：状态变量修改同步监听](../harmonyos-guides/arkts-new-syncmonitor.md)。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| SyncMonitor | [MonitorDecorator](ts-state-management-watch-monitor.md#monitordecorator12) | 属性装饰器，监听状态变量的修改。 |

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](errorcode-statemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 130001 | The path is invalid. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @ObservedV2
4. class Info {
5. @Trace name: string = 'Tom';
6. @Trace age: number = 25;
7. @Trace height: number = 175;

9. // 监听一个变量
10. @SyncMonitor('name')
11. onNameChange() {
12. hilog.info(0xFF00, 'testTag', '%{public}s', `name change to ${this.name}`);
13. }

15. // 监听多个变量
16. @SyncMonitor('age','height')
17. onRecordChange(monitor: IMonitor) {
18. monitor.dirty.forEach((path: string) => {
19. hilog.info(0xFF00, 'testTag', '%{public}s',
20. `${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
21. })
22. }
23. }

25. @Entry
26. @ComponentV2
27. struct Index {
28. @Local info: Info = new Info();

30. build() {
31. Column() {
32. Text(`info.name: ${this.info.name}`)
33. .onClick(() => {
34. this.info.name = 'Bob'; // 输出日志：name change to Bob
35. })
36. Text(`info.age: ${this.info.age}, info.height: ${this.info.height}`)
37. .onClick(() => {
38. this.info.age++; // 输出日志：age change from 25 to 26
39. this.info.height++; // 输出日志：height change from 175 to 176
40. })
41. }
42. }
43. }
```
