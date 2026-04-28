---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacementutils
title: TensorPlacementUtils
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorPlacementUtils
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2127ff78dc39167d97b098559b182825a3c2295fc56fda6aac45045883505897
---

## 函数功能

提供一组函数，判断TensorPlacement的位置。

## 函数原型

```
1. class TensorPlacementUtils {
2. public:
3. // 判断Tensor是否位于Device上的内存（包括HBM和P2p内存）
4. static bool IsOnDevice(TensorPlacement placement) {
5. return (placement == kOnDeviceHbm) || (placement == kOnDeviceP2p);
6. }
7. // 判断Tensor是否位于Host上
8. static bool IsOnHost(TensorPlacement placement) {
9. return (placement == kOnHost) || (placement == kFollowing);
10. }
11. // 判断Tensor是否位于Host上，且数据紧跟在结构体后面
12. static bool IsOnHostFollowing(TensorPlacement placement) {
13. return (placement == kFollowing);
14. }
15. // 判断Tensor是否位于Host上，且数据不紧跟在结构体后面
16. static bool IsOnHostNotFollowing(TensorPlacement placement) {
17. return (placement == kOnHost);
18. }
19. // 判断Tensor是否位于Device上的HBM内存
20. static bool IsOnDeviceHbm(TensorPlacement placement) {
21. return (placement == kOnDeviceHbm);
22. }
23. // 判断Tensor是否位于Device上的P2p内存
24. static bool IsOnDeviceP2p(TensorPlacement placement) {
25. return (placement == kOnDeviceP2p);
26. }
27. };
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

```
1. TensorData tensor_data;
2. tensor_data.SetPlacement(TensorPlacement::kOnDeviceHbm);
3. auto on_device = TensorPlacementUtils::IsOnDevice(tensor_data.GetPlacement()); // on_device is true
```
