---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-binding
title: 绑定手势方法
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 添加手势响应 > 绑定手势方法
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0f87c70442ac64aa19b0f8f250f776ecccc0bd857fa59c76bc4c905fec760fad
---

通过给各个组件绑定不同的手势事件，并设计事件的响应方式，当手势识别成功时，ArkUI框架将通过事件回调通知组件手势识别的结果。

说明

gesture、priorityGesture和parallelGesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。

## gesture（常规手势绑定方法）

```
1. .gesture(gesture: GestureType, mask?: GestureMask)
```

gesture为通用的一种手势绑定方法，可以将手势绑定到对应的组件上。

例如，可以将点击手势TapGesture通过gesture方法将手势绑定到Text组件上。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RegularBinding {
5. build() {
6. Column() {
7. Text('Gesture').fontSize(28)
8. // 采用gesture手势绑定方法绑定TapGesture
9. .gesture(
10. TapGesture()
11. .onAction(() => {
12. console.info('TapGesture is onAction');
13. }))
14. }
15. .height(200)
16. .width(250)
17. }
18. }
```

[Gesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureBinding/entry/src/main/ets/pages/Gesture.ets#L18-L37)

## priorityGesture（带优先级的手势绑定方法）

```
1. .priorityGesture(gesture: GestureType, mask?: GestureMask)
```

priorityGesture是带优先级的手势绑定方法，可以在组件上绑定优先识别的手势。

在默认情况下，当父组件和子组件均使用gesture绑定相同类型手势时，子组件优先识别通过gesture绑定的手势。当父组件使用priorityGesture绑定与子组件同类型的手势时，父组件优先识别通过priorityGesture绑定的手势。

对于绑定了长按手势的组件，可以设置触发长按的最短时间[duration](../harmonyos-references/ts-gesturehandler.md#longpressgesturehandleroptions)。触发长按时，系统将优先响应触发长按时间最短的组件，忽略priorityGesture设置。

例如，当父组件Column和子组件Text同时绑定TapGesture手势时，父组件以带优先级手势priorityGesture的形式进行绑定时，优先响应父组件绑定的TapGesture。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PriorityBinding {
5. build() {
6. Column() {
7. Text('Gesture').fontSize(28)
8. .gesture(
9. TapGesture()
10. .onAction(() => {
11. hilog.info(DOMAIN, TAG,'Text TapGesture is onAction');
12. }))
13. }
14. .height(200)
15. .width(250)
16. // 设置为priorityGesture时，点击文本区域会忽略Text组件的TapGesture手势事件，优先响应父组件Column的TapGesture手势事件
17. .priorityGesture(
18. TapGesture()
19. .onAction(() => {
20. hilog.info(DOMAIN, TAG,'Column TapGesture is onAction');
21. }), GestureMask.IgnoreInternal)
22. }
23. }
```

[PriorityGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureBinding/entry/src/main/ets/pages/PriorityGesture.ets#L18-L42)

## parallelGesture（并行手势绑定方法）

```
1. .parallelGesture(gesture: GestureType, mask?: GestureMask)
```

parallelGesture是并行的手势绑定方法，可以在父子组件上绑定可以同时响应的相同手势。

在默认情况下，手势事件为非冒泡事件，当父子组件绑定相同的手势时，父子组件绑定的手势事件会发生竞争，最多只有一个组件的手势事件能够获得响应。而当父组件绑定了并行手势parallelGesture时，父子组件相同的手势事件都可以触发，实现类似冒泡效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ParallelBinding {
5. build() {
6. Column() {
7. Text('Gesture').fontSize(28)
8. .gesture(
9. TapGesture()
10. .onAction(() => {
11. hilog.info(DOMAIN, TAG,'Text TapGesture is onAction');
12. }))
13. }
14. .height(200)
15. .width(250)
16. // 设置为parallelGesture时，点击文本区域会同时响应父组件Column和子组件Text的TapGesture手势事件
17. .parallelGesture(
18. TapGesture()
19. .onAction(() => {
20. hilog.info(DOMAIN, TAG,'Column TapGesture is onAction');
21. }), GestureMask.Normal)
22. }
23. }
```

[ParallelGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureBinding/entry/src/main/ets/pages/ParallelGesture.ets#L19-L43)
