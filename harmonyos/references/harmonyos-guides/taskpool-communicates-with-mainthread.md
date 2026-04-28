---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-communicates-with-mainthread
title: TaskPool任务与宿主线程通信
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > TaskPool任务与宿主线程通信
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:387be5aa5c2b0109a250119f1ca3d432c7604c33555f84076973e36cae96f41b
---

如果Task不仅需要返回最终执行结果，还需定时通知宿主线程状态和数据变化，或分段返回大量数据（如从数据库读取大量数据），可按以下方式实现。

下面以多个图片加载任务结果实时返回为例说明。

1. 实现接收Task消息的方法。

   ```
   1. import { taskpool } from '@kit.ArkTS';
   2. import { IconItemSource } from './IconItemSource';

   4. function notice(data: number): void {
   5. console.info('子线程任务已执行完，共加载图片: ', data);
   6. }
   ```
2. 在需要执行的Task中，添加sendData()接口将消息发送给宿主线程。在宿主线程通过onReceiveData()接口接收消息。这样宿主线程就可以通过notice()接口接收到Task发送的数据。

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
   1. import { taskpool } from '@kit.ArkTS';
   2. import { IconItemSource } from './IconItemSource';

   4. function notice(data: number): void {
   5. console.info('子线程任务已执行完，共加载图片: ', data);
   6. }

   8. // 通过Task的sendData方法，即时通知宿主线程信息
   9. @Concurrent
   10. export function loadPictureSendData(count: number): IconItemSource[] {
   11. let iconItemSourceList: IconItemSource[] = [];
   12. // 遍历添加6*count个IconItem的数据
   13. for (let index = 0; index < count; index++) {
   14. const numStart: number = index * 6;
   15. // 此处循环使用6张图片资源
   16. iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 1}`));
   17. iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 2}`));
   18. iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 3}`));
   19. iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 4}`));
   20. iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 5}`));
   21. iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 6}`));

   23. taskpool.Task.sendData(iconItemSourceList.length);
   24. }
   25. return iconItemSourceList;
   26. }

   28. @Entry
   29. @Component
   30. struct Index {
   31. @State message: string = 'Hello World';

   33. build() {
   34. Row() {
   35. Column() {
   36. Text(this.message)
   37. .fontSize(50)
   38. .fontWeight(FontWeight.Bold)
   39. .onClick(() => {
   40. let iconItemSourceList: IconItemSource[];
   41. let lodePictureTask: taskpool.Task = new taskpool.Task(loadPictureSendData, 30);
   42. // 设置notice方法接收Task发送的消息
   43. lodePictureTask.onReceiveData(notice);
   44. taskpool.execute(lodePictureTask).then((res: object) => {
   45. iconItemSourceList = res as IconItemSource[];
   46. })
   47. this.message = 'success';
   48. })
   49. }
   50. .width('100%')
   51. }
   52. .height('100%')
   53. }
   54. }
   ```
