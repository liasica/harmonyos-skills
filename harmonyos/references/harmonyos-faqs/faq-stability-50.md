---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-50
title: 开启HWAsan监测后应用崩溃如何解决
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 开启HWAsan监测后应用崩溃如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e36834ef982466ae078a2a435a50e8e57e2df47df97be63eb82bfb0bc20f741b
---

## 问题现象

未开启HWAsan监测时，应用正常运行，开启HWAsan监测后，应用崩溃闪退。

## 背景知识

HWAsan是Hardware-Assisted Address Sanitizer的简称，它是Clang LLVM提供的一套内存错误检测系统，用来检测C/C++中常见的内存访问错误，相比之前的Asan（Address Sanitizer），HWAsan在性能、内存上有不小提升，依赖于编译器的Address Tagging特性，该特性允许应用程序自定义数据存储到虚拟地址的最高8位，当CPU操作该虚拟地址时会自动忽略它。详见：[使用HWAsan检测内存错误](../best-practices/bpta-stability-hwasan-detection.md)。

## 问题定位

1. 查看asan日志。

   ```txt
   Device info:HUAWEI Mate 60 Pro
   Build info:ALN-AL00 5.0.0.150(SP8C00E150R4P30log)
   Fingerprint:xxx
   Module name:com.xxx
   Version:1.0.0
   Pid:33555
   Uid:20020131
   Reason:heap-buffer-overflow
   ==appspawn==33555==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000200eb5c20 at pc 0x005af67eda80
   WRITE of size 8 at 0x000200eb5c20 tags: 5a/ba (ptr/mem) in thread T0
       #0 0x5af67eda80  (/data/storage/el1/bundle/libs/arm64/libxxx.so+0x2da80) (BuildId: f8bf8a86************************697ffb3)
       #1 0x5af67dd2f0  (/data/storage/el1/bundle/libs/arm64/libxxx.so+0x1d2f0) (BuildId: f8bf8a86************************697ffb3)
       #2 0x5ad8dfe9e4  (/system/lib64/platformsdk/libace_napi.z.so+0x3e9e4) (BuildId: 85e70f1f************************2f4922c)

   [0x000200eb5c00,0x000200eb5c40) is a small allocated heap chunk; size: 64 offset: 32

   Cause: heap-buffer-overflow
   0x000200eb5c20 is located 32 bytes to the left of 40-byte region [0x000200eb5c40,0x000200eb5c68)
   allocated here:
       #0 0x5ad41e2614  (/system/lib64/libclang_rt.hwasan.so+0x22614) (BuildId: 92356864************************d1ed78d7)
       #1 0x5af67dcdd4  (/data/storage/el1/bundle/libs/arm64/libxxx.so+0x1cdd4) (BuildId: f8bf8a86************************697ffb3)
       #2 0x5ad8dfe9e4  (/system/lib64/platformsdk/libace_napi.z.so+0x3e9e4) (BuildId: 85e70f1f************************2f4922c)
       #3 0x5af0104b2c  (/system/lib64/module/arkcompiler/stub.an+0x404b2c)
       #4 0x5aefd0bbf4  (/system/lib64/module/arkcompiler/stub.an+0xbbf4)
       #5 0x26bfd64954  ([anon:ArkTS Heapnon movable space]+0x64954)
   ```
2. 点击asan日志中的链接即可跳转至引起内存错误的代码处。

   ```
   static napi_value TcpInitCmdSocket(napi_env env, napi_callback_info info) 
   {
       logi(TAG, "%s:", __func__ );
       TcpCmdContext *context = (TcpCmdContext *)malloc(sizeof(TcpCmdContext));
       memset(context, 0, sizeof(TcpCmdContext));
       context->env = env;

       napi_value value;
       int64_t addr = (int64_t)context;
       napi_create_int64(env, addr, &value);
       return value;
   }

   void tcp_cmd_create(TcpCmdContext *ctx, char *ip, int port) 
   {
       logi(TAG, "%s", __func__);
       tcp_cmd_t *client = (tcp_cmd_t*)calloc(1, sizeof(tcp_cmd_t));
       ctx->client = client; // HWAsan检测跳转代码行
       client->port = port;

       return ;  
   }
   ```

   定位到ctx->client = client，排查上下文代码发现调用了napi\_create\_int64，在HWAsan的运行环境中，napi\_create\_int64创建指针给JS调用，后续使用ctx的地址发生偏移导致运行崩溃。

## 分析结论

* ArkTS的Number类型基于IEEE 754双精度浮点数标准，仅能精确表示53位二进制整数。
* 未开启HWAsan时：系统仅使用40位地址空间，此时地址值在Number的安全范围内（2^40≈1.1×10^12<<2^53），转换后不会丢失高位。
* 开启HWAsan后：地址扩展为完整64位，若高11位（64-53）非零，超出Number的53位精度范围，导致转换时高11位被截断。

## 修改建议

将代码段中的napi\_create\_int64改成napi\_create\_bigint\_int64。JavaScript的BigInt支持任意位数的整数表示，通过napi\_create\_bigint\_int64接口可直接将64位地址转换为BigInt，避免精度丢失。

## 总结

Number类型的精度限制与64位地址的冲突，根据地址位数是否超出Number安全范围，选择对应接口。
