---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-60
title: 如何实现子组件数据传递给父组件且父组件修改数据不影响子组件
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何实现子组件数据传递给父组件且父组件修改数据不影响子组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3ae4f17f4a388807ca4df130652d0686dcf97a0bac36f3aa1073a425044ff93
---

## 问题现象

父子组件均设置状态变量（如selectedData: string[]），如何实现在子组件数据变化时，数据传递给父组件，在父组件对数据进行修改处理时，修改后的数据不会传递给子组件。

## 背景知识

[Emitter模块](../harmonyos-references/js-apis-emitter.md)提供了在同一进程不同线程间或同一线程内发送和处理事件的能力，可以通过[emitter.emit](../harmonyos-references/js-apis-emitter.md#emitteremit)接口发送指定事件。

## 解决方案

可以使用Emitter模块的emit接口，EventData定义事件携带的数据，将子组件的数据发送给父组件，父组件调用emitter.on函数接收事件携带的数据，实现父子组件之间实现数据通信，且在父组件处理数据时不会影响子组件的数据。

1. 子组件修改数据，定义事件携带数据并发送事件。

   ```screen
   // 修改子组件数据
   this.selectedData.push(data);
   let eventDataMap = new Map<string, Object>();
   eventDataMap.set("content", data);
   // 定义事件携带的数据
   let eventData: emitter.EventData = {
     data: {
       eventDataMap
     }
   };
   // 设置事件优先级
   let options: emitter.Options = {
     priority: emitter.EventPriority.HIGH
   };
   // 发送eventId为EmitterTest事件
   emitter.emit("EmitterTest", options, eventData);
   ```
2. 父组件接收事件，执行回调函数，获取子组件数据。

   ```ts
   // 收到eventId为EmitterTest的事件后执行回调函数
   emitter.on('EmitterTest', (eventData: emitter.EventData) => {
     let eventDataMap = eventData.data?.eventDataMap as Map<string, Object>;
     this.selectedData.push(eventDataMap.get('content') as string);
     console.info(`EmitterTest callback, eventData: ${eventDataMap.get('content')}`);
   });
   ```
3. 父组件按照业务需要修改数据，如删除数据。

   ```ts
   // 删除数据内第一个元素
   this.selectedData.splice(0, 1);
   ```

完整示例代码如下：

```ts
import { emitter } from '@kit.BasicServicesKit';

// 定义子组件
@Component
struct ChildComponent {
  @State selectedData: string[] = [];

  build() {
    Column() {
      Text('修改子组件数据')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          let data = new Date().toString();
          // 修改子组件数据
          this.selectedData.push(data);
          let eventDataMap = new Map<string, Object>();
          eventDataMap.set("content", data);
          // 定义事件携带的数据
          let eventData: emitter.EventData = {
            data: {
              eventDataMap
            }
          };
          // 设置事件优先级
          let options: emitter.Options = {
            priority: emitter.EventPriority.HIGH
          };
          // 发送eventId为EmitterTest事件
          emitter.emit("EmitterTest", options, eventData);
        });
      ForEach(this.selectedData, (item: string) => {
        Text(item);
      });
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}

@Entry
@Component
struct ParentComponent {
  @State selectedData: string[] = [];

  aboutToAppear(): void {
    // 收到eventId为EmitterTest的事件后执行回调函数
    emitter.on('EmitterTest', (eventData: emitter.EventData) => {
      let eventDataMap = eventData.data?.eventDataMap as Map<string, Object>;
      this.selectedData.push(eventDataMap.get('content') as string);
      console.info(`EmitterTest callback, eventData: ${eventDataMap.get('content')}`);
    });
  }

  build() {
    Column({ space: 10 }) {
      Column() {
        ForEach(this.selectedData, (item: string) => {
          Text(item);
        });
        Text('删除父组件数据')
          .onClick(() => {
            // 删除数据内第一个元素
            this.selectedData.splice(0, 1);
          });
      }
      .justifyContent(FlexAlign.End)
      .width('100%')
      .height('50%');

      Text('---------------分割线--------------')
        .width('100%')
        .textAlign(TextAlign.Center);

      ChildComponent()
        .layoutWeight(1);
    }
    .height('100%')
    .width('100%');
  }
}
```
