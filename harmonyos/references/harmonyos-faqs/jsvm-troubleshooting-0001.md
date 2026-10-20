---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/jsvm-troubleshooting-0001
title: NDK与Native开发问题定位
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 故障排查 > NDK与Native开发问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:4977701374c69cf38c273ec79c913e539664e57d1fd2cc620e13a8f088a3dbef
---

## NDK调用Native方法异常闪退

### 问题现象

NDK工程中，调用Native方法报异常。

* 报错信息为符号找不到：

  ```txt
  Symbol not found: xxx, version: nul
  ```
* 报错信息为方法所属的对象未定义：

  ```txt
  TypeError: Cannot read property add of undefined
  ```

  报错信息为系统侧的符号找不到：

  ```txt
  xxx.so: __fd_chk: symbol not found
  ```

  或者：

  ```txt
  xxx: Symbol not found
  ```

  同时应用闪退。

### 定位过程

* 根据缺失的符号，查看对应的SO是否被打包到HAP中正确的路径下，并且该符号在SO中对外可见。
* 查看对应的SO是否存在其他依赖库，依赖库是否正确引入。
* 使用到的SO文件是否是通过HarmonyOS工具链编译的。
* 跨语言调用接口和声明文件是否正确编写。
* 参照版本变更说明，查看SO对应的源码中，有没有版本新增禁止的行为，如申请匿名内存或修改匿名内存。
* 排查SDK版本与工程机版本是否匹配。

### 分析结论

可能导致问题的原因为：

* SO名称或版本不匹配，不是使用HarmonyOS工具链编译的或未打包到正确的lib目录下。
* SO依赖其他SO，依赖的SO没有同步引入。
* 缺少了跨语言调用接口模块和声明文件，接口调用路径不同。
* 使用了被禁止的方法，如申请或修改匿名内存。
* SDK版本与工程版本不匹配。

### 修改建议

* 修改代码，确保未使用被禁止的方法。
* 使用HarmonyOS工具链编译库及其依赖的库，确认需要调用的接口对外可见。
* 将编译的SO放在NDK工程指定路径，参照指导编写跨语言接口模块并在ArkTS侧导入和正确调用。
* 为解决不同版本工程机与SDK之间的兼容性问题，建议工程机版本与IDE/SDK版本配套使用，见[配套关系](../harmonyos-releases/overview-allversion.md)。

## 开启HWAsan监测后应用崩溃如何解决

### 问题现象

未开启HWAsan监测时，应用正常运行，开启HWAsan监测后，应用崩溃闪退。

### 定位过程

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

   ```cpp
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

### 分析结论

* ArkTS的Number类型基于IEEE 754双精度浮点数标准，仅能精确表示53位二进制整数。
* 未开启HWAsan时：系统仅使用40位地址空间，此时地址值在Number的安全范围内（240≈1.1×1012<<2^53），转换后不会丢失高位。
* 开启HWAsan后：地址扩展为完整64位，若高11位（64-53）非零，超出Number的53位精度范围，导致转换时高11位被截断。

### 修改建议

将代码段中的napi\_create\_int64改成napi\_create\_bigint\_int64。JavaScript的BigInt支持任意位数的整数表示，通过napi\_create\_bigint\_int64接口可直接将64位地址转换为BigInt，避免精度丢失。

## ArkTS向C++传递数据异常

### 问题现象

在ArkTS与Native C++通过Node-API接口进行数据传递时，经常会遇到一些数据传递前后不一致甚至报错的问题，如：

ArkTS向C++传递数据问题：

通过napi\_get\_value\_string\_utf8传递长string时，C++获取不到字符串内容。

### 定位过程

C++侧获取不到ArkTS传入的string，可能导致的原因有两种：

* 参数传入的string的内容是否为空；
* string的长度特别长；

可以通过ArkTS侧的源码排查，属于上述哪种情形。

### 分析结论

ArkTS传入的字符串长度超过限制，无法通过napi\_get\_value\_string\_utf8传递，该接口获取字符大小由底层内存决定，Node-API无法设置和更改。

### 修改建议

传输长string时，建议以Buffer传递，通过napi\_get\_buffer\_info来获取从TS层传来的Buffer，再转成string。

## C++向ArkTS传递数据异常

### 问题现象

在ArkTS与Native C++通过Node-API接口进行数据传递时，经常会遇到一些数据传递前后不一致甚至报错的问题，如：

C++向ArkTS传递数据问题：

* 通过napi\_create\_external\_arraybuffer异步传递Buffer，在ArkTS侧获取不到内容。
* 通过napi\_create\_buffer\_copy创建并复制数据到Buffer对象时报错：

  ```txt
  Create failed, current size: 2.969184 MiB, limit size: 2.000000 MiB
  ```
* 通过napi\_create\_typedarray创建并赋值Unicode字符串数据时报错：

  ```txt
  C03F00/ArkCompiler com.examp...lication E RangeError: The newByteLength is out of range.
  ```

### 定位过程

* 异步回调ArkTS收不到数据，通过代码排查是否使用了**external\_arraybuffer**，在External Buffer释放的地方加上日志，通过日志的时间戳检查C++侧数据是否在被取出时已经被释放；
* C++创建和复制数据到Buffer时出错报错，通过检索日志中包含**limit size: 2.000000 MiB**错误信息，判断拷贝的数据超过了2M的限制，在源码中找到Buffer拷贝的数据，确认其大小；
* 通过typedarray传递ArrayBuffer时，检索日志包含**is out of range**，则是数组越界导致，通过代码排查计算**类型大小×length**判断是否超出了数组的大小。

### 分析结论

* external\_arraybuffer不会拷贝内存，而是复用Node-API模块内存块，通过异步回调方式传递数据时，若C++侧数据释放了，ArkTS将获取不到数据；
* napi\_create\_buffer\_copy最大支持2M数据（2097152字节），超出报错；
* Unicode字符占用2字节，napi\_create\_typedarray以类型napi\_int16\_array传递Unicode字符时，2\*length超过数据长度时，出错。

### 修改建议

* 使用External ArrayBuffer复用Node-API内存时，确保在结果回调前内存不释放，或者使用线程安全函数。
* 传递Buffer数据控制数据在2M内，超出时，推荐使用napi\_create\_arraybuffer接口创建的ArrayBuffer对象，该接口没有数据大小限制。
* 创建ArrayBuffer对象时，计算检查数据类型长度，避免数据内存越界。
