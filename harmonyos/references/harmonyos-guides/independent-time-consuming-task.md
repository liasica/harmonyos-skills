---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/independent-time-consuming-task
title: 使用TaskPool执行独立的耗时任务
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > 使用TaskPool执行独立的耗时任务
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2b93b326f2720df058571c5d22109f47532b2e6b54b275eca1552d89d6749a88
---

对于独立运行的耗时任务，任务完成后将结果返回给宿主线程。可采用以下方式实现。

下面通过图片加载来说明。

1. 实现子线程需要执行的任务。

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
   import { IconItemSource } from './IconItemSource';

   // 在Task中执行的方法，需要添加@Concurrent注解，否则无法正常调用。
   @Concurrent
   export function loadPicture(count: number): IconItemSource[] {
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
     }
     return iconItemSourceList;
   }
   ```
2. 使用TaskPool的execute方法执行任务，加载图片。

   ```typescript
   import { taskpool } from '@kit.ArkTS';
   import { IconItemSource } from './IconItemSource';
   import { loadPicture } from './IndependentTask';

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
               let iconItemSourceList: IconItemSource[] = [];
               // 创建Task
               let loadPictureTask: taskpool.Task = new taskpool.Task(loadPicture, 30);
               // 执行Task，并返回结果
               taskpool.execute(loadPictureTask).then((res: object) => {
                 // loadPicture方法的执行结果
                 iconItemSourceList = res as IconItemSource[];
                 this.message = 'success';
               }).catch(() => {
                 console.error(`Failed to execute taskpool.`);
                 this.message = 'fail';
               })
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
