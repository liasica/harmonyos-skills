---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-globaltensor
title: GlobalTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 数据类型定义 > GlobalTensor
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4dc53b7bbf8b3335b8b562835fe3c504fd8339c79f3c0710283ef8e42144dc25
---

## 功能说明

GlobalTensor用来存放Global Memory（外部存储）的全局数据。

## 定义原型

```
1. template <typename T> class GlobalTensor : public BaseGlobalTensor<T> {
2. public:
3. using PrimType = PrimT<T>;
4. __aicore__ inline GlobalTensor<T>() {}
5. __aicore__ inline void SetGlobalBuffer(__gm__ PrimType* buffer, uint64_t bufferSize);  // 传入全局数据的指针，并手动设置一个buffer size，初始化GlobalTensor
6. __aicore__ inline void SetGlobalBuffer(__gm__ PrimType* buffer);  // 传入全局数据的指针，初始化GlobalTensor,可以不传入buffer size,但此时使用GetSize获取的长度是随机值
7. __aicore__ inline const __gm__ PrimType* GetPhyAddr() const;   // 返回全局数据的地址
8. __aicore__ inline __gm__ PrimType* GetPhyAddr(const uint64_t offset) const;  // 返回全局数据(指定偏移offset个元素)的地址
9. __aicore__ inline __inout_pipe__(S) PrimType GetValue(const uint64_t offset) const;  // 获取Tensor的相应偏移位置的值
10. __aicore__ inline __inout_pipe__(S) __gm__ PrimType& operator()(const uint64_t offset) const;   // 返回某个index位置的元素的引用
11. __aicore__ inline void SetValue(const uint64_t offset, PrimType value);  // 设置Tensor相应偏移位置的值。
12. __aicore__ inline uint64_t GetSize() const;  // 返回Tensor中的element个数
13. __aicore__ inline GlobalTensor operator[](const uint64_t offset) const;  // 指定偏移返回一个GlobalTensor，offset单位为element
14. __aicore__ inline void SetShapeInfo(const ShapeInfo& shapeInfo);
15. __aicore__ inline ShapeInfo GetShapeInfo() const;
16. template<CacheRwMode rwMode = CacheRwMode::RW>
17. __aicore__ inline void SetL2CacheHint(CacheMode mode);   // 设置Tensor写入L2 Cache的模式（允许/禁止）
18. // ...
19. };
```

## 函数说明

类型T支持基础数据类型，但需要遵循使用此GlobalTensor的指令的数据类型支持情况。

**表1** 函数说明

| 函数名称 | 入参说明 | 含义 |
| --- | --- | --- |
| GetValue | offset：偏移量，单位为element | 获取GlobalTensor中的某个值，返回T类型的立即数。 |
| SetGlobalBuffer | buffer：主机侧传入的全局数据指针  bufferSize：所包含的类型为T的数据个数，单位为element，需自行保证不会超出实际数据的长度 | 设置GlobalTensor的存储位置：buffer指向外部存储的起始地址，bufferSize为Tensor所占外部存储的大小，如指向的外部存储有连续256个int32\_t，则其bufferSize为256。 |
| GetPhyAddr | - | 返回GlobalTensor的地址，如果传入offset，则表示偏移offset个元素。 |
| GetSize | - | 返回GlobalTensor的element个数。 |
| operator[] | offset：开发者指定的偏移位置 | 根据输入的offset偏移返回新的Tensor，offset的单位为element的个数。 |
| operator() | index: 下标索引 | 获取本GlobalTensor的第index个变量的引用。与[LocalTensor](cannkit-localtensor.md)的operator()类似。 |
| SetShapeInfo | shapeInfo：ShapeInfo结构体 | 设置GlobalTensor的shapeInfo。 |
| GetShapeInfo | 无 | 获取GlobalTensor的shapeInfo。  **说明：** Shape信息没有默认值，只有通过SetShapeInfo设置过Shape信息后，才可以调用该接口获取正确的ShapeInfo。 |

## 调用示例

```
1. void Init(__gm__ uint8_t *src_gm, __gm__ uint8_t *dst_gm)
2. {
3. uint64_t dataSize = 256; //设置input_global的大小为256

5. AscendC::GlobalTensor<int32_t> inputGlobal; // 类型为int32_t
6. inputGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ int32_t *>(src_gm), dataSize); // 设置源操作数在Global Memory上的起始地址为src_gm，所占外部存储的大小为256个int32_t

8. AscendC::LocalTensor<int32_t> inputLocal = inQueueX.AllocTensor<int32_t>();
9. AscendC::DataCopy(inputLocal, inputGlobal, dataSize); // 将Global Memory上的inputGlobal拷贝到Local Memory的inputLocal上
10. // ...
11. }
```
