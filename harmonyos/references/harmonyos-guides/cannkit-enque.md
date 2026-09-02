---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-enque
title: EnQue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQueBind > EnQue
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:5b9d768f5094c9cbb21ed4dd5db1228ca38ac09b2ff16e90ab63e5818f22f021
---

## 功能说明

将Tensor push到队列。

## 函数原型

```cpp
template <typename T> 
__aicore__ inline bool EnQue(const LocalTensor<T>& tensor)
```

## 参数说明

**表1** bool EnQue(LocalTensor<T>& tensor)原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| tensor | 输入 | 指定的Tensor。 |

**图1** 将LocalTensor通过EnQue放入A1/B1的Queue中

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/lUSsnEkbRbGTQ4QLavYp5Q/zh-cn_image_0000002736434497.png)

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

无

## 返回值

* true：表示Tensor加入Queue成功。
* false：表示Queue已满，入队失败。

## 调用示例

```cpp
// 接口：EnQue Tensor
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue(tensor1);// 将tensor加入VECOUT的Queue中
```
