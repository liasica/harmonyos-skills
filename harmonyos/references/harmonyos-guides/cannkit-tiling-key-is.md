---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tiling-key-is
title: TILING_KEY_IS
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > Kernel Tiling > TILING_KEY_IS
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:31+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:676f3632dd14b306adc010e617b1cada8791820c026c6bac6430cbce5effae08
---

## 函数功能

在核函数中判断本次执行时的tiling\_key是否等于某个key，从而标识tiling\_key==key的一条kernel分支。

## 函数原型

```
1. TILING_KEY_IS(key)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| key | 输入 | 此参数是非负整数，表示某个核函数的分支。 |

## 约束说明

* key必须是非负整数。
* TILING\_KEY\_IS运用于if和else if分支，不支持else分支，即用TILING\_KEY\_IS函数来表征N个分支，必须用N个TILING\_KEY\_IS(key)来分别表示。
* 暂不支持kernel直调工程。

## 调用示例

```
1. extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *workspace, __gm__ uint8_t *tiling)
2. {
3. GET_TILING_DATA(tilingData, tiling);
4. if (workspace == nullptr) {
5. return;
6. }
7. KernelAdd op;
8. op.Init(x, y, z, tilingData.blockDim, tilingData.totalLength, tilingData.tileNum);
9. // 当TilingKey为1时，执行Process1；为2时，执行Process2；为3时，执行Process3
10. if (TILING_KEY_IS(1)) {
11. op.Process1();
12. } else if (TILING_KEY_IS(2)) {
13. op.Process2();
14. } else if (TILING_KEY_IS(3)) {
15. op.Process3();
16. }
17. // 其他代码逻辑
18. // ...
19. // 此处示例当TilingKey为3时，会执行ProcessOther
20. if (TILING_KEY_IS(3)) {
21. op.ProcessOther();
22. }
23. }
24. // 配套的host侧tiling函数示例：
25. ge::graphStatus TilingFunc(gert::TilingContext* context)
26. {
27. // 其他代码逻辑
28. // ...
29. if (context->GetInputShape(0) > 10) {
30. context->SetTilingKey(1);
31. } else if (some condition) {
32. context->SetTilingKey(2);
33. } else if (some condition) {
34. context->SetTilingKey(3);
35. }
36. }
```
