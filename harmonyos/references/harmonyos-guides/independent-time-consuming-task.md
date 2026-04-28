---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/independent-time-consuming-task
title: 使用TaskPool执行独立的耗时任务
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > 使用TaskPool执行独立的耗时任务
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7821266307a666f3720e70c878a7f3dac66a0413d9785602bfdefbc4e2320abf
---

对于独立运行的耗时任务，任务完成后将结果返回给宿主线程。可采用以下方式实现。

下面通过图片加载来说明。

1. 实现子线程需要执行的任务。

   ```
   1. export class IconItemSource {
   2. image: string | Resource = '';
   3. text: string | Resource = '';

   5. constructor(image: string | Resource = '', text: string | Resource = '') {
   6. this.image = image;
   7. this.text = text;
   8. }
   9. }
   ```

   ```
   1. import { IconItemSource } from './IconItemSource';

   3. // 在Task中执行的方法，需要添加@Concurrent注解，否则无法正常调用。
   4. @Concurrent
   5. export function loadPicture(count: number): IconItemSource[] {
   6. let iconItemSourceList: IconItemSource[] = [];
   7. // 遍历添加6*count个IconItem的数据
   8. for (let index = 0; index < count; index++) {
   9. const numStart: number = index * 6;
   10. // 此处循环使用6张图片资源
   11. iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 1}`));
   12. iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 2}`));
   13. iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 3}`));
   14. iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 4}`));
   15. iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 5}`));
   16. iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 6}`));
   17. }
   18. return iconItemSourceList;
   19. }
   ```
2. 使用TaskPool的execute方法执行任务，加载图片。

   ```
   1. import { taskpool } from '@kit.ArkTS';
   2. import { IconItemSource } from './IconItemSource';
   3. import { loadPicture } from './IndependentTask';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'Hello World';

   10. build() {
   11. Row() {
   12. Column() {
   13. Text(this.message)
   14. .fontSize(50)
   15. .fontWeight(FontWeight.Bold)
   16. .onClick(() => {
   17. let iconItemSourceList: IconItemSource[] = [];
   18. // 创建Task
   19. let lodePictureTask: taskpool.Task = new taskpool.Task(loadPicture, 30);
   20. // 执行Task，并返回结果
   21. taskpool.execute(lodePictureTask).then((res: object) => {
   22. // loadPicture方法的执行结果
   23. iconItemSourceList = res as IconItemSource[];
   24. })
   25. this.message = 'success';
   26. })
   27. }
   28. .width('100%')
   29. }
   30. .height('100%')
   31. }
   32. }
   ```
