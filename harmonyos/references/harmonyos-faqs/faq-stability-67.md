---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-67
title: 句柄泄漏(FD_LEAK)问题排查与解决
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 句柄泄漏(FD_LEAK)问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-07-24
content_hash: sha256:e9dfcaaf891c73c2bcca522679bbf98b16b845b38b99e13ed64385fb8de2921f
---

## 问题现象

应用在运行过程中突然崩溃或功能异常（如网络请求一直失败、文件无法写入）。

查看HiLog日志，搜索PROCESS\_KILL.\*包名出现Reason为ResourceLeak:Fd Leak错误信息。

另外，在ArkTS层创建PixelMap对象给Image组件使用时，当Image组件销毁时，若未及时释放PixelMap所占用的fd，也会导致fd资源泄漏。

ArkTS最小运行代码示例（模拟泄漏场景）：

```ts
import { fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State leakCount: number = 0;

  // 模拟泄漏：只打开不关闭
  triggerLeak() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let path = context.filesDir + '/test_leak.txt';
    // 创建一个文件用于测试
    try {
      let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
      fs.closeSync(file);
    } catch (e) {
      console.error('File operation failed:' + JSON.stringify(e));
    }

    // 循环打开文件，模拟泄漏
    for (let i = 0; i < 500; i++) {
      try {
        // 错误：这里打开了文件句柄，但是没有保存引用，也没有调用close
        let file = fs.openSync(path, fs.OpenMode.READ_WRITE);
        this.leakCount++;
        console.info(`Open fd success: ${file.fd}`);
      } catch (e) {
        console.error(`Open failed: ${JSON.stringify(e)}`);
      }
    }
  }

  build() {
    Column() {
      Text('当前模拟泄漏次数: ' + this.leakCount)
        .fontSize(20)
        .margin(20)

      Button('点击触发fd泄漏')
        .fontSize(20)
        .onClick(() => {
          this.triggerLeak();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 背景知识

* **句柄（File Descriptor）**：进程打开文件、创建Socket网络连接、创建线程（pipe/anon\_inode）等操作都会申请文件句柄。
* **句柄限制**：系统对单个进程持有的句柄数量有限制。当泄漏数量达到阈值（每隔60s遍历一次进程，获取进程fd句柄总数，超过阈值5000个时抓取详细句柄信息，同步上报泄漏），再次申请资源会失败，导致应用崩溃或被系统判定为资源泄漏而强行终止。
* **泄漏日志**：系统检测到泄漏时，会生成[pid]\_fd\_leak.txt或RESOURCE\_OVERLIMIT...日志文件，记录泄漏时的快照信息。

## 问题定位

1. **第一步：获取并分析泄漏日志**。

   日志路径通常位于/data/log/reliability/resource\_leak/或通过导出故障日志获取。打开日志文件（如1380\_fd\_leak.txt），按以下顺序分析：

   1. 确认泄漏规模：

      查看日志头部信息，关注leaked fd nums字段。

      ```text
      time: 2024/06/27 11:55:28
      pid: 1380
      process: com.example.myapp
      leaked fd nums: 5111  <-- 当前持有的句柄总数，远超正常值
      ```
   2. 确定泄漏的主要类型：

      查看Leaked fd Top 10区域：

      * **情况A（普通文件泄漏）**：如果类型为REG或具体文件名很少，需结合下一步分析。
      * **情况B（特殊资源泄漏）**：如果Top 1是Ashmem（共享内存）、socket（网络）、pipe（管道）、dmabuf（显存）等，说明是特定系统资源未释放。

        ```text
        Leaked fd Top 10:
        4796    Ashmem    <-- 绝大多数泄漏是共享内存
        259     socket
        // ...
        ```
   3. 定位具体文件路径（针对文件句柄）：

      查看Dir Type Top 10区域，这里会按路径聚类。

      如下所示，可以明确看到是RDB数据库文件发生了泄漏：

      ```text
      Dir Type Top 10:
      6175 /data/storage/el2/database/rdb  <-- 明确指向数据库文件
      5    /dev/urandom
      ```
2. **第二步：分析调用栈（核心步骤）**

   在日志下方的LOGGER\_MEMCHECK\_FD\_STACK\_INFO区域，系统记录了句柄申请的调用栈（需开启开发者模式或Log版本）。

   -num：表示该堆栈产生的句柄数量（未释放的）。

   -bt：调用栈的程序计数器（PC）地址。

   ```text
   ==============================Sorted by num==============================
   num 8272 bt [/system/lib64/libfdleak_tracker.so+0x1fb58] ... [/data/storage/el1/bundle/libs/arm64/libentry.so+0x148940]
   ```
3. **第三步：反解堆栈定位代码**

   使用SDK提供的addr2line工具，将bt中的地址还原为代码行号。

   假设泄漏发生在libentry.so的0x148940处：

   ```shell
   # 命令行示例
   addr2line -C -f -e /path/to/libentry.so 0x148940
   ```

   输出结果将直接指向代码中执行open、socket或napi\_create\_dataview（对应Ashmem）的具体行数。

## 分析结论

导致句柄泄漏的常见原因有：

1. **未关闭资源**：在循环或高频调用的函数中打开了文件/Socket，但在函数结束或异常返回（Exception/Early return）时未调用close。
2. **重复初始化**：对象（如RDB Store、AVPlayer）被重复创建，旧对象未释放。
3. **IPC通信异常**：Ashmem或Binder通信频繁创建且未正确回收。
4. **PixelMap未释放**：创建PixelMap对象给Image组件使用时，HarmonyOS不会自动回收PixelMap的底层资源，开发者必须主动调用Release()方法释放。若Image组件销毁时未释放，会导致fd泄漏。

## 修改建议

1. **成对释放资源**：确保所有open都有对应的close。在C++中使用RAII（智能指针或类封装）管理资源；在ArkTS中使用try-finally块确保文件关闭。
2. **异常处理**：检查代码中的异常分支（if error return），确保在返回前已释放申请的fd。
3. **释放PixelMap资源**：PixelMap是前端持有的，Image组件不负责释放。即使不涉及手动打开文件操作，PixelMap的Release()调用仍然不可省略。在组件的aboutToDisappear中主动调用pixelMap.release()并置空引用，是解决此场景下fd泄漏的核心手段。
