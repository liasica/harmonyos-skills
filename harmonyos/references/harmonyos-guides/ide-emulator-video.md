---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-video
title: 获取模拟器实时画面数据
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 获取模拟器实时画面数据
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:839d9e8fa65f90e504e3cee031d8df7ca9606ce34bb29b1a36b51b5828aa4de1
---

从26.0.1版本开始，模拟器支持通过共享内存对外输出画面帧数据，为远程服务器开发、自动化测试、画面采集与转码等场景提供实时画面获取能力。使用-streamOutput启动参数，模拟器会将主屏幕画面帧实时写入命名共享内存，供外部进程读取。开发者无需连接显示器或额外采集工具，即可通过本地脚本直接获取模拟器实时画面数据。

在使用本文提供的能力之前，开发者需要具备图像开发的基础知识。

## 使用约束

* 支持Linux、macOS，暂不支持Windows。
* 如电脑环境存在多个用户，仅同用户进程可访问模拟器共享内存。

## 开发指导

1. 启动模拟器，开启共享内存写入能力。

   启动模拟器时附加-streamOutput参数，即可打开共享内存写入能力。

   ```bash
   # 基本用法
   Emulator -start <instanceName> -streamOutput
   # 自定义hdc端口（多实例场景）
   Emulator -start <instanceName> -streamOutput -hdcPort 10001
   ```
2. 确定共享内存名称。

   共享内存命名格式：emu-shm-frame-<模拟器端口号>

   其中模拟器端口号为-hdcPort指定的端口，如不指定时为默认端口号，可通过hdc命令查询。

   ```bash
   # 查询已连接设备
   hdc list targets
   # 查询指定端口号对应的模拟器名称
   hdc -t <模拟器端口号> shell "param get | grep hvd"
   ```

   示例：

   ```bash
   $ hdc list targets
   127.0.0.1:5555
   $ hdc -t 127.0.0.1:5555 shell "param get | grep hvd"
       ohos.qemu.hvd.name = Mate 90 RS
   ```
3. 本地实现读取逻辑。

   从共享内存段读取画面帧数据，共享内存数据结构如下。

   ```
   // 共享内存Header结构
   struct FrameHeader {
       uint32_t magic;         // 内存标识：固定取0x52464D48（ASCII "RMFH"），等于该值才表示属于模拟器共享内存，用于防止误访问非法内存段
       uint32_t ready;         // 就绪标志：0表示模拟器正在写入，1表示本帧已写入完毕
       uint64_t frame_index;   // 帧序号：模拟器每写入一帧单调递增
       uint64_t timestamp;     // 时间戳：本帧写入时刻，Unix微秒（microseconds）
       uint32_t width;         // 画面宽度（像素）
       uint32_t height;        // 画面高度（像素）
       uint32_t format;        // 像素格式：当前固定为0，表示RGBA8888
       uint32_t encode;        // 编码方式：当前固定为0，表示原始未编码（raw）数据
       uint32_t payload_size;  // 像素数据长度（字节）：等于width × height × 4（RGBA每像素4字节）
   };

   // 共享内存整体结构：Header之后紧跟像素数据
   struct Frame {
       FrameHeader hdr;
       // payload并非共享内存中实际存储的指针字段，而是表示FrameHeader之后紧跟的像素数据区域，读取时通过hdr + 1偏移访问
       char *payload;          // 画面帧像素数据
   };
   ```
4. 对获取到的画面帧做后续处理（显示/转码/发送等，自行实现）。

## 示例代码

以下为本地读取共享内存画面帧的示例代码：

```
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <cstdint>
#include <cstdio>

// 数据结构，也可从共享内存中单独读取如width、height
#pragma pack(push, 1)
struct FrameHeader {
    uint32_t magic;
    uint32_t ready;
    uint64_t frame_index;
    uint64_t timestamp;
    uint32_t width;
    uint32_t height;
    uint32_t format;
    uint32_t encode;
    uint32_t payload_size;
};
#pragma pack(pop)

// 标准读取流程（Reader读流程）：
// 校验magic：确认magic == 0x52464D48，防止访问非法内存段；
// 轮询就绪：检查ready字段，确认模拟器是否写入完毕，如跳过可能导致读取的数据异常；
// 帧去重：确认frame_index与上次已消费的帧号不同，避免重复处理同一帧；
// 防越界校验：确认payload_size == width × height × 4，且不超过共享内存段大小范围；
// 读取像素：从共享内存读取width × height × 4字节的RGBA像素数据；
// 记录进度：将本次frame_index记为"已消费帧号"，供下一轮去重。

int main()
{
    // 共享内存名称，读取入口，需要修改为实际的名称
    const char *name = "/emu-shm-frame-5555";
    int fd = shm_open(name, O_RDONLY, 0600);
    if (fd < 0) {
        perror("shm_open");
        return 1;
    }

    struct stat st;
    fstat(fd, &st);  // 段大小动态，用fstat查询
    size_t mapSize = st.st_size;
    void *mapped = mmap(nullptr, mapSize, PROT_READ, MAP_SHARED, fd, 0);
    if (mapped == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    FrameHeader *hdr = static_cast<FrameHeader *>(mapped);
    // 跳过FrameHeader，指向像素数据起始位置
    uint8_t *payload = reinterpret_cast<uint8_t *>(hdr + 1);
    uint64_t lastIndex = 0;

    while (true) {
        // ① 校验模拟器内存标识（magic）
        if (hdr->magic != 0x52464D48) {
            usleep(1000);
            continue;
        }
        // ② 查询模拟器是否写入完毕（轮询就绪）
        if (hdr->ready != 1) {
            usleep(1000);
            continue;
        }
        // ③ 检查是否是已读帧（去重）
        if (hdr->frame_index == lastIndex) {
            usleep(1000);
            continue;
        }
        // ④ 防越界校验
        if (hdr->payload_size != (uint64_t)hdr->width * hdr->height * 4 ||
            hdr->payload_size > mapSize - sizeof(FrameHeader)) {
            usleep(1000);
            continue;
        }

        lastIndex = hdr->frame_index;  // ⑤ 记录已消费帧号
        // ⑥ 处理像素：payload指向width*height*4字节RGBA数据
        printf("frame %llu: %ux%u, payload %u bytes\n",
               (unsigned long long)hdr->frame_index, hdr->width, hdr->height,
               hdr->payload_size);

        // 通过脚本获取共享内存画面帧后，可自行实现开发所需工作，例如：画面显示、视频转码、网络发送等
        // ... 你的处理逻辑（转码/显示/发送）...
        // payload即为读取到的实时画面数据
    }

    munmap(mapped, mapSize);
    close(fd);
    return 0;
}
```
