---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-communicates-with-mainthread
title: TaskPool任务与宿主线程通信
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > TaskPool任务与宿主线程通信
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f5c40ac23e609c23171d398c079f13d223bc81236bb569da9158f13b7d4f5882
---

如果Task不仅需要返回最终执行结果，还需定时通知宿主线程状态和数据变化，或分段返回大量数据（如从数据库读取大量数据），可按以下方式实现。

下面以多个图片加载任务结果实时返回为例说明。

在需要执行的Task中，添加sendData()接口将消息发送给宿主线程。在宿主线程通过onReceiveData()接口接收消息。这样宿主线程就可以通过notice()接口接收到Task发送的数据。

```typescript
export class IconItemSource {
  image: string | Resource = '';
  text: string | Resource = '';

  constructor(image: string | Resource = '', text: string | Resource = '') {
    this.image = image;
    this.text = text;
  }
}
```

```typescript
import { taskpool } from '@kit.ArkTS';
import { IconItemSource } from './IconItemSource';
// 实现接收Task消息的方法
function notice(data: number): void {
  console.info('子线程已加载数据，共加载图片: ', data);
}

// 通过Task的sendData方法，即时通知宿主线程信息
@Concurrent
export function loadPictureSendData(count: number): IconItemSource[] {
  let iconItemSourceList: IconItemSource[] = [];
  // 遍历添加6*count个IconItem的数据
  for (let index = 0; index < count; index++) {
    const numStart: number = index * 6;
    // 此处循环使用6张图片资源
    iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 1}`));
    iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 2}`));
    iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 3}`));
    iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 4}`));
    iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 5}`));
    iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 6}`));

    taskpool.Task.sendData(iconItemSourceList.length);
  }
  return iconItemSourceList;
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let iconItemSourceList: IconItemSource[];
            let loadPictureTask: taskpool.Task = new taskpool.Task(loadPictureSendData, 30);
            // 设置notice方法接收Task发送的消息
            loadPictureTask.onReceiveData(notice);
            taskpool.execute(loadPictureTask).then((res: object) => {
              iconItemSourceList = res as IconItemSource[];
              this.message = 'success';
            }).catch((e: BusinessError) => {
              this.message = 'failed';
              console.error(`taskpool: execute: Code: ${e.code}, message: ${e.message}`);
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
