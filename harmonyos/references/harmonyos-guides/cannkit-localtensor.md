---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-localtensor
title: LocalTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 数据类型定义 > LocalTensor
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:35+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:12858a7dfddf12c2fc3b74fc55663c6178961365ac2c9899294f7eb2e35d6a62
---

## 功能说明

用于存放AI Core中Local Memory（内部存储）的数据，支持QuePosition为VECIN、VECOUT、VECCALC、A1、A2、B1、B2、CO1、CO2。

## 定义原型

```cpp
template <typename T> class LocalTensor : public BaseLocalTensor<T> {
public:
    using PrimType = PrimT<T>;
    __aicore__ inline LocalTensor<T>() {};
#if defined(ASCENDC_CPU_DEBUG) && ASCENDC_CPU_DEBUG == 1
    ~LocalTensor();
    explicit LocalTensor<T>(TBuffAddr& address);
    LocalTensor<T>(const LocalTensor<T>& other);
    LocalTensor<T> operator = (const LocalTensor<T>& other);
    PrimType* GetPhyAddr(const uint32_t offset) const;
    PrimType* GetPhyAddr() const;
    __inout_pipe__(S) PrimType GetValue(const uint32_t offset) const;
    __inout_pipe__(S) PrimType& operator()(const uint32_t offset) const;
    template <typename CAST_T> __aicore__ inline LocalTensor<CAST_T> ReinterpretCast() const;
    template <typename T1> __inout_pipe__(S) void SetValue(const uint32_t index, const T1 value) const;
    LocalTensor operator[](const uint32_t offset) const;
    template <typename T1> void SetAddrWithOffset(LocalTensor<T1> &src, uint32_t offset);
    inline void Print();
    inline void Print(uint32_t len);
    int32_t ToFile(const std::string& fileName) const;
#else
    __aicore__ inline uint64_t GetPhyAddr() const;
    __aicore__ inline uint64_t GetPhyAddr(const uint32_t offset) const;
    __aicore__ inline __inout_pipe__(S) PrimType GetValue(const uint32_t index) const;
    __aicore__ inline __inout_pipe__(S) __ubuf__ PrimType& operator()(const uint32_t offset) const;
    template <typename CAST_T> __aicore__ inline LocalTensor<CAST_T> ReinterpretCast() const;
    template <typename T1> __aicore__ inline __inout_pipe__(S)
        void SetValue(const uint32_t index, const T1 value) const;
    __aicore__ inline LocalTensor operator[](const uint32_t offset) const;
    template <typename T1> 
    [[deprecated("NOTICE: SetAddrWithOffset has been deprecated and will be removed in the next version. "
        "Please do not use it!")]]
    __aicore__ inline void SetAddrWithOffset(LocalTensor<T1> &src, uint32_t offset);
#endif
    __aicore__ inline int32_t GetPosition() const;
    __aicore__ inline void SetSize(const uint32_t size);
    __aicore__ inline uint32_t GetSize() const;
    [[deprecated("NOTICE: GetLength has been deprecated and will be removed in the next version. Please do not use "
                 "it!")]]
    __aicore__ inline uint32_t GetLength() const;
    [[deprecated("NOTICE: SetBufferLen has been deprecated and will be removed in the next version. Please do not use "
                 "it!")]]
    __aicore__ inline void SetBufferLen(uint32_t dataLen);
    __aicore__ inline void SetUserTag(const TTagType tag);
    __aicore__ inline TTagType GetUserTag() const;
    // ...
    __aicore__ inline void SetShapeInfo(const ShapeInfo& shapeInfo);
    __aicore__ inline ShapeInfo GetShapeInfo() const;
    // ...
};
```

## 函数说明

类型T支持基础数据类型，但需要遵循使用此LocalTensor的指令的数据类型支持情况。

**表1** 函数说明

| 函数名称 | 入参说明 | 含义 |
| --- | --- | --- |
| GetValue | offset：偏移量，单位为'element' | 获取LocalTensor中的某个值，返回PrimType类型的数值。  **该接口仅在LocalTensor的TPosition为VECIN、VECCALC、VECOUT时支持。** |
| SetValue | offset：偏移值，单位为'element'  value：设置值，单位为任意类型 | 设置LocalTensor中的某个值。  **该接口仅在LocalTensor的TPosition为VECIN、VECCALC、VECOUT时支持。** |
| operator[] | offset：偏移量 | 获取距原LocalTensor起始地址偏移量为offset的新LocalTensor，注意offset不能超过原有LocalTensor的size大小。 |
| operator() | offset： 下标索引 | 获取本LocalTensor的第offset个变量的引用。用于左值，相当于SetValue接口，用于右值，相当于GetValue接口。 |
| GetSize | 无 | 获取当前LocalTensor size大小。单位为元素。 |
| SetSize | size：元素个数，单位为'element' | 设置当前LocalTensor size大小。单位为元素。当开发者重用local tensor变量且使用长度发生变化的时候，需要使用此接口重新设置Size。 |
| SetUserTag | tag：设置的Tag信息，类型TTagType对应为int32\_t | 为Tensor添加开发者自定义信息，开发者可以根据需要设置对应的Tag。后续可通过GetUserTag获取指定Tensor的Tag信息，并根据Tag信息对Tensor进行相应操作。 |
| GetUserTag | N/A | 获取指定Tensor块的Tag信息，开发者可以根据Tag信息对Tensor进行不同操作。 |
| ReinterpretCast | N/A | 将当前Tensor重解释为开发者指定的新类型，转换后的Tensor与原Tensor地址及内容完全相同，Tensor的大小（字节数）保持不变。 |
| GetPhyAddr | N/A | 返回LocalTensor的地址，如果传入offset，则表示偏移offset个元素。 |
| GetPosition | N/A | 获取QuePosition抽象的逻辑位置，支持QuePosition为VECIN、VECOUT、VECCALC、A1、A2、B1、B2、CO1、CO2。 |
| GetLength | N/A | 获取LocalTensor数据长度，单位为Byte。 |
| SetShapeInfo | shapeInfo：ShapeInfo结构体 | 设置LocalTensor的shapeInfo。 |
| GetShapeInfo | N/A | 获取LocalTensor的shapeInfo。  \*\*说明：\*\*Shape信息没有默认值，只有通过SetShapeInfo设置过Shape信息后，才可以调用该接口获取正确的ShapeInfo。 |
| SetAddrWithOffset | src：基础地址的Tensor，将该Tensor的地址作为基础地址，设置偏移后的Tensor地址  offset：偏移的长度 | 设置带有偏移的Tensor地址。用于快速获取定义一个Tensor，同时指定新Tensor相对于旧Tensor首地址的偏移。偏移的长度为旧Tensor的元素个数。 |
| SetBufferLen | dataLen：buffer长度 | 设置buffer长度。单位为字节。 |
| ToFile | fileName：文件名称 | 只限于CPU调试，将LocalTensor数据Dump到文件中，用于精度调试，文件保存在执行目录。 |
| Print | dataLen：打印元素个数 | 只限于CPU调试，在调试窗口中打印LocalTensor数据用于精度调试，每一行打印一个datablock(32Bytes)的数据。 |

## 注意事项

不要大量使用SetValue对LocalTensor进行赋值，会使性能下降。

## 调用示例

```cpp
// srcLen = 256, num = 100, M = 50
// 示例1
for (int32_t i = 0; i < srcLen; ++i) {
    inputLocal.SetValue(i, num); // 对inputLocal中第i个位置进行赋值为num
}
// 示例1结果如下：
// 数据(inputLocal): [100 100 100  ... 100]
 
// 示例2
for (int32_t i = 0; i < srcLen; ++i) {
    auto element = inputLocal.GetValue(i); // 获取inputLocal中第i个位置的数值
}
// 示例2结果如下：
// element为100
 
// 示例3
for (int32_t i = 0; i < srcLen; ++i) {
    inputLocal(i) = num; // 对inputLocal中第i个位置进行赋值为num
}
// 示例3结果如下：
// 数据(inputLocal): [100 100 100  ... 100]
 
// 示例4
for (int32_t i = 0; i < srcLen; ++i) {
    auto element = inputLocal(i); // 获取inputLocal中第i个位置的数值
}
// 示例4结果如下：
// element 为100
 
// 示例5
auto size = inputLocal.GetSize(); // 获取inputLocal的长度，size大小为inputLocal有多少个element
// 示例5结果如下：
// size大小为srcLen，256。
 
// 示例6
// operator[]使用方法，inputLocal[16]为从起始地址开始偏移量为16的新tensor
AscendC::Add(outputLocal[16], inputLocal[16], inputLocal2[16], M);
// 示例6结果如下：
// 输入数据(inputLocal): [100 100 100 ... 100]
// 输入数据(inputLocal2): [1 2 3 ... 66]
// 输出数据(outputLocal): [... 117 118 119 ... 166]
 
// 示例7
AscendC::TTagType tag = 10;
inputLocal.SetUserTag(tag); // 对LocalTensor设置tag信息。
 
// 示例8
AscendC::LocalTensor<half> tensor1 = que1.DeQue<half>();
AscendC::TTagType tag1 = tensor1.GetUserTag();
AscendC::LocalTensor<half> tensor2 = que2.DeQue<half>();
AscendC::TTagType tag2 = tensor2.GetUserTag();
AscendC::LocalTensor<half> tensor3 = que3.AllocTensor<half>();
/* 使用Tag控制条件语句执行 */
if ((tag1 <= 10) && (tag2 >= 9)) {
    AscendC::Add(tensor3, tensor1, tensor2, TILE_LENGTH); // 当tag1小于等于10，tag2大于等于9的时候，才能进行相加操作。
}
// 示例9
// input_local为int32_t 类型，包含16个元素(64字节)
for (int32_t i = 0; i < 16; ++i) {
    inputLocal.SetValue(i, i); // 对inputLocal中第i个位置进行赋值为i
}
 
// 调用ReinterpretCast将input_local重解释为int16_t类型
AscendC::LocalTensor<int16_t> interpreTensor = inputLocal.ReinterpretCast<int16_t>();
// 示例9结果如下，二者数据完全一致，在物理内存上也是同一地址，仅根据不同类型进行了重解释
// inputLocal:0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
// interpreTensor:0 0 1 0 2 0 3 0 4 0 5 0 6 0 7 0 8 0 9 0 10 0 11 0 12 0 13 0 14 0 15 0
 
// 示例10
// 调用GetPhyAddr()返回LocalTensor地址，CPU上返回的是指针类型(T*)，NPU上返回的是物理存储的地址(uint64_t)
#ifdef ASCEND_CPU_DEBUG
float *inputLocalCpuPtr = inputLocal.GetPhyAddr();
uint64_t realAddr = (uint64_t)inputLocalCpuPtr - (uint64_t)(GetTPipePtr()->GetBaseAddr(static_cast<int8_t>(AscendC::QuePosition::VECCALC)));
#else
uint64_t realAddr = inputLocal.GetPhyAddr();
#endif
 
// 示例11
AscendC::QuePosition srcPos = (AscendC::QuePosition)inputLocal.GetPosition();
if (srcPos == AscendC::QuePosition::VECCALC) {
    // 处理逻辑1
} else if (srcPos == AscendC::QuePosition::A1) {
    // 处理逻辑2
} else {
    // 处理逻辑3
}
 
// 示例12
// 获取localTensor的长度(单位为Byte)，数据类型为int32_t，所以是16*sizeof(int32_t)
uint32_t len = inputLocal.GetLength();
// inputLocal:0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
// len: 64
 
// 示例13 设置Tensor的ShapeInfo信息
AscendC::LocalTensor<float> maxUb = softmaxMaxBuf.template Get<float>();
uint32_t shapeArray[] = {16, 1024};
maxUb.SetShapeInfo(AscendC::ShapeInfo(2, shapeArray, AscendC::DataFormat::ND));
 
// 示例14 获取Tensor的ShapeInfo信息
AscendC::ShapeInfo maxShapeInfo = maxUb.GetShapeInfo();
uint32_t orgShape0 = maxShapeInfo.originalShape[0];
uint32_t orgShape1 = maxShapeInfo.originalShape[1];
uint32_t orgShape2 = maxShapeInfo.originalShape[2];
uint32_t orgShape3 = maxShapeInfo.originalShape[3];
uint32_t shape2 = maxShapeInfo.shape[2];
 
// 示例15 SetAddrWithOffset，用于快速获取定义一个Tensor，同时指定新Tensor相对于旧Tensor首地址的偏移
// 需要注意，偏移的长度为旧Tensor的元素个数
AscendC::LocalTensor<float> tmpBuffer1 = tempBmm2Queue.AllocTensor<float>();
AscendC::LocalTensor<half> tmpHalfBuffer;
tmpHalfBuffer.SetAddrWithOffset(tmpBuffer1, calcSize * 2);
 
// 示例16 SetBufferLen 如下示例将申请的Tensor长度修改为1024(单位为字节)
AscendC::LocalTensor<float> tmpBuffer2 = tempBmm2Queue.AllocTensor<float>();
tmpBuffer2.SetBufferLen(1024);
 
// 示例17 SetSize 如下示例将申请的Tensor长度修改为256(单位为元素)
AscendC::LocalTensor<float> tmpBuffer3 = tempBmm2Queue.AllocTensor<float>();
tmpBuffer3.SetSize(256);
 
#ifdef ASCEND_CPU_DEBUG
// 示例18 只限于CPU调试，将LocalTensor数据Dump到文件中，用于精度调试，文件保存在执行目录
AscendC::LocalTensor<float> tmpTensor = softmaxMaxBuf.template Get<float>();
tmpTensor.ToFile("tmpTensor.bin");
 
// 示例19 只限于CPU调试，在调试窗口中打印LocalTensor数据用于精度调试，每一行打印一个datablock(32Bytes)的数据
AscendC::LocalTensor<int32_t> inputLocal = softmaxMaxBuf.template Get<int32_t>();
for (int32_t i = 0; i < 16; ++i) {
    inputLocal.SetValue(i, i); // 对input_local中第i个位置进行赋值为i
}
inputLocal.Print();
// 0000: 0 1 2 3 4 5 6 7 8
// 0008: 9 10 11 12 13 14 15
#endif
```
