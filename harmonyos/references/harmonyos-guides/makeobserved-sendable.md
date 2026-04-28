---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/makeobserved-sendable
title: ArkUI数据更新场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > ArkUI数据更新场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d32079de797c845124daae3617e1b5528647eb4b85d1fb73d611483a2500aeb
---

当需要网络下载或者本地生成的数据需要发送到UI线程进行展示时，由于ArkUI的标注和[@Sendable装饰器](arkts-sendable.md#sendable装饰器)不能同时修饰变量和对象，因此需要使用[makeObserved](arkts-new-makeobserved.md)在ArkUI中导入可观测的Sendable共享数据。

本示例说明以下场景：

* makeObserved在传入@Sendable类型的数据后有观测能力，且其变化可以触发UI更新。
* 从子线程获取数据，整体替换UI线程的可观测数据。
* 从子线程获取的数据重新执行makeObserved，变为可观测数据。
* 将数据从UI主线程传递回子线程时，只传递不可观测的数据。makeObserved的返回值不能直接传给子线程。

```
1. @Sendable
2. export class SendableData {
3. public name: string = 'Tom';
4. public age: number = 20;
5. public gender: number = 1;
6. public likes: number = 1;
7. public follow: boolean = false;
8. }
```

```
1. import { taskpool } from '@kit.ArkTS';
2. import { SendableData } from './SendableData';
3. import { UIUtils } from '@kit.ArkUI';

5. @Concurrent
6. function threadGetData(param: string): SendableData {
7. // 在子线程处理数据
8. let ret = new SendableData();
9. console.info(`Concurrent threadGetData, param ${param}`);
10. ret.name = param + '-o';
11. ret.age = Math.floor(Math.random() * 40);
12. ret.likes = Math.floor(Math.random() * 100);
13. return ret;
14. }

16. @Entry
17. @ComponentV2
18. struct Index {
19. // 通过makeObserved给普通对象或是Sendable对象添加可观测能力
20. @Local send: SendableData = UIUtils.makeObserved(new SendableData());

22. build() {
23. Column() {
24. Text(this.send.name)
25. Button('change name').onClick(() => {
26. // 可以观察到属性的改变
27. this.send.name += '0';
28. })
29. .id('change name')
30. Button('task').onClick(() => {
31. // 将待执行的函数放入taskpool内部任务队列等待，等待分发到工作线程执行。
32. // 因为数据的构建和处理可以在子线程中完成，但有观测能力的数据不能传给子线程，只有在UI主线程里才可以操作可观测的数据。
33. // 所以这里只是将`this.send`的属性`name`传给子线程操作。
34. taskpool.execute(threadGetData, this.send.name).then(val => {
35. // 和@Local一起使用，可以观察this.send的变化
36. this.send = UIUtils.makeObserved(val as SendableData);
37. })
38. })
39. .id('task')
40. }
41. }
42. }
```
