---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacementutils
title: TensorPlacementUtils
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorPlacementUtils
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:f32c65c42f2e10bbfc7d54e3bb56eda32b5158255e481aaf6c3e4b48186171ce
---

## 函数功能

提供一组函数，判断TensorPlacement的位置。

## 函数原型

```cpp
class TensorPlacementUtils {
 public:
  // 判断Tensor是否位于Device上的内存（包括HBM和P2p内存）
  static bool IsOnDevice(TensorPlacement placement) {
    return (placement == kOnDeviceHbm) || (placement == kOnDeviceP2p);
  }
  // 判断Tensor是否位于Host上
  static bool IsOnHost(TensorPlacement placement) {
    return (placement == kOnHost) || (placement == kFollowing);
  }
  // 判断Tensor是否位于Host上，且数据紧跟在结构体后面
  static bool IsOnHostFollowing(TensorPlacement placement) {
    return (placement == kFollowing);
  }
  // 判断Tensor是否位于Host上，且数据不紧跟在结构体后面
  static bool IsOnHostNotFollowing(TensorPlacement placement) {
    return (placement == kOnHost);
  }
  // 判断Tensor是否位于Device上的HBM内存
  static bool IsOnDeviceHbm(TensorPlacement placement) {
    return (placement == kOnDeviceHbm);
  }
  // 判断Tensor是否位于Device上的P2p内存
  static bool IsOnDeviceP2p(TensorPlacement placement) {
    return (placement == kOnDeviceP2p);
  }
};
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| placement | 输入 | 需要进行判断的TensorPlacement枚举。 |

## 返回值

* true表示是。
* false表示不是。

## 约束说明

无

## 调用示例

```cpp
TensorData tensor_data;
tensor_data.SetPlacement(TensorPlacement::kOnDeviceHbm);
auto on_device = TensorPlacementUtils::IsOnDevice(tensor_data.GetPlacement()); // on_device为true
```
