---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-binding
title: 绑定手势方法
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 添加手势响应 > 绑定手势方法
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a2969583a0eb13bb768287100edc32fb0e34e309ca1256f7edc600bcd43bece3
---

通过给各个组件绑定不同的手势事件，并设计事件的响应方式，当手势识别成功时，ArkUI框架将通过事件回调通知组件手势识别的结果。

**说明** 

gesture、priorityGesture和parallelGesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。

## gesture（常规手势绑定方法）

```ts
.gesture(gesture: GestureType, mask?: GestureMask)
```

gesture为通用的一种手势绑定方法，可以将手势绑定到对应的组件上。

例如，可以将点击手势TapGesture通过gesture方法将手势绑定到Text组件上。

```typescript
// xxx.ets
@Entry
@Component
struct RegularBinding {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
      // 采用gesture手势绑定方法绑定TapGesture
        .gesture(
          TapGesture()
            .onAction(() => {
              console.info('TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
  }
}
```

## priorityGesture（带优先级的手势绑定方法）

```ts
.priorityGesture(gesture: GestureType, mask?: GestureMask)
```

priorityGesture是带优先级的手势绑定方法，可以在组件上绑定优先识别的手势。

在默认情况下，当父组件和子组件均使用gesture绑定相同类型手势时，子组件优先识别通过gesture绑定的手势。当父组件使用priorityGesture绑定与子组件同类型的手势时，父组件优先识别通过priorityGesture绑定的手势。

对于绑定了长按手势的组件，可以设置触发长按的最短时间[duration](../harmonyos-references/ts-gesturehandler.md#longpressgesturehandleroptions)。触发长按时，系统将优先响应触发长按时间最短的组件，忽略priorityGesture设置。

例如，当父组件Column和子组件Text同时绑定TapGesture手势时，父组件以带优先级手势priorityGesture的形式进行绑定时，优先响应父组件绑定的TapGesture。

```typescript
// xxx.ets
@Entry
@Component
struct PriorityBinding {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        .gesture(
          TapGesture()
            .onAction(() => {
              hilog.info(DOMAIN, TAG,'Text TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
    // 设置为priorityGesture时，点击文本区域会忽略Text组件的TapGesture手势事件，优先响应父组件Column的TapGesture手势事件
    .priorityGesture(
      TapGesture()
        .onAction(() => {
          hilog.info(DOMAIN, TAG,'Column TapGesture is onAction');
        }), GestureMask.IgnoreInternal)
  }
}
```

## parallelGesture（并行手势绑定方法）

```ts
.parallelGesture(gesture: GestureType, mask?: GestureMask)
```

parallelGesture是并行的手势绑定方法，可以在父子组件上绑定可以同时响应的相同手势。

在默认情况下，手势事件为非冒泡事件，当父子组件绑定相同的手势时，父子组件绑定的手势事件会发生竞争，最多只有一个组件的手势事件能够获得响应。而当父组件绑定了并行手势parallelGesture时，父子组件相同的手势事件都可以触发，实现类似冒泡效果。

```typescript
// xxx.ets
@Entry
@Component
struct ParallelBinding {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        .gesture(
          TapGesture()
            .onAction(() => {
              hilog.info(DOMAIN, TAG,'Text TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
    // 设置为parallelGesture时，点击文本区域会同时响应父组件Column和子组件Text的TapGesture手势事件
    .parallelGesture(
      TapGesture()
        .onAction(() => {
          hilog.info(DOMAIN, TAG,'Column TapGesture is onAction');
        }), GestureMask.Normal)
  }
}
```
