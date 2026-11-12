---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/shared-arraybuffer-object
title: SharedArrayBuffer对象
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > SharedArrayBuffer对象
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f41e8872ccf18328662fe2d1fb18117c8362724574192c437f2777f25b8c3950
---

SharedArrayBuffer内部包含一块Native内存，其JS对象壳被分配在虚拟机本地堆（LocalHeap）。支持跨并发实例间共享Native内存，但是对共享Native内存的访问及修改需要采用Atomics类，防止数据竞争。SharedArrayBuffer可用于多个并发实例间的状态或数据共享。通信过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/_Cj7dgRySiqbjy7o6tUynQ/zh-cn_image_0000002815557879.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=8855D924C252AF2D5FB68C7198B31A33530C2AA6465F66A89AEA7F5D3FCFA49F)

## 使用示例

使用TaskPool传递Int32Array对象，实现如下：

```typescript
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function transferAtomics(arg1: Int32Array) {
  console.info('wait begin::');
  // 使用Atomics进行操作
  let res = Atomics.wait(arg1, 0, 0, 3000);
  return res;
}

@Entry
@Component
struct CSharedArrayBuffer {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          // 定义可共享对象
          let sab: SharedArrayBuffer = new SharedArrayBuffer(20);
          let int32 = new Int32Array(sab);
          let task: taskpool.Task = new taskpool.Task(transferAtomics, int32);
          taskpool.execute(task).then((res) => {
            this.message = 'success';
            console.info(`this res is: ${res}`);
          }).catch((e: BusinessError) => {
            this.message = 'fail';
            console.error(`taskpool: execute task: code: ${e.code}, message: ${e.message}`);
          });
          setTimeout(() => {
            Atomics.notify(int32, 0, 1);
          }, 1000);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
