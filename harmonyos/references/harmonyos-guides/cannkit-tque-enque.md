---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-enque
title: EnQue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQue > EnQue
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:28+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:3ccc828d64a630c05fa18efdd3bed2bdfa42bb007aebc59969d97f6266a31e7f
---

## 功能说明

将Tensor push到队列。

## 函数原型

* 无需指定源和目的位置

  ```cpp
  template <typename T> 
  __aicore__ inline bool EnQue(const LocalTensor<T>& tensor)
  ```
* 需要指定源和目的位置

  通过[TQueBind](cannkit-overview.md)绑定VECIN和VECOUT可实现VECIN和VECOUT内存复用，如下接口用于存在Vector计算的场景下实现复用，在入队时需要指定源和目的位置，不存在Vector计算的场景下可直接调用bool EnQue(LocalTensor<T>& tensor)入队接口。

  ```cpp
  template <TPosition srcUserPos, TPosition dstUserPos, typename T>
  __aicore__ inline bool EnQue(const LocalTensor<T>& tensor)
  ```

## 参数说明

**表1** bool EnQue(LocalTensor<T>& tensor)原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| tensor | 输入 | 指定的Tensor。 |

**表2** template <TPosition srcUserPos, TPosition dstUserPos> bool EnQue(LocalTensor<T>& tensor)原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| srcUserPos | 输入 | 模板参数，开发者指定队列的src position，当前只支持如下通路：GM->VECIN/VECOUT->GM。 |
| dstUserPos | 输入 | 模板参数，开发者指定队列的dst position，当前只支持如下通路：GM->VECIN/VECOUT->GM。 |
| tensor | 输入 | 指定的Tensor。 |

**图1** 将LocalTensor通过EnQue放入A1/B1的Queue中

![](https://media:401788444118544973)

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
// 接口: EnQue Tensor
AscendC::TPipe pipe;
AscendC::TQue<AscendC::TPosition::VECOUT, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue(tensor1);// 将tensor加入VECOUT的Queue中
// 接口：EnQue指定特定的src/dst position，加入相应的队列
// template <TPosition srcUserPos, TPosition dstUserPos> bool EnQue(LocalTensor<T>& tensor)
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::QuePosition::VECIN, AscendC::QuePosition::VECOUT, 1> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue<AscendC::QuePosition::GM, AscendC::QuePosition::VECIN, half>(tensor1);// 将tensor加入VECIN的Queue中，实现内存复用
```
