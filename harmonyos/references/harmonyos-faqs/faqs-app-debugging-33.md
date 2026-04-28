---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-33
title: 如何解决Network单元测试用例crash问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何解决Network单元测试用例crash问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5c59990478d2c0593d063651cfd78f98ffd40c1592b4f5444695bd56ca128a5d
---

**问题描述**

组件依赖已更新到最新。network源码编译时出现如下报错：

```
1. Fingerprint:8c83cd8bd1e043ceecdb478f0ca56f241b09616da77300b1a834d50620c6cdd9Module name:msc_cpp_testTimestamp:2024-03-22 15:35:05.292Pid:59626Uid:0Process name:/data/local/tmp/msc_cpp_test/msc_cpp_testReason:Signal:SIGABRT(SI_TKILL)@0x000000000000e8ea from:59626:0Fault thread Info:Tid:59626, Name:msc_cpp_test#00 pc 0000000000185ca8 /system/lib/ld-musl-aarch64.so.1(raise+188)(bad62e733958f8d89d07480a2491abc9)#01 pc 00000000001381a8 /system/lib/ld-musl-aarch64.so.1(abort+20)(bad62e733958f8d89d07480a2491abc9)#02 pc 000000000005bef4 /system/lib64/libclang_rt.asan.so(d3894082b99f633c446cd1895b6190bd6a0bad31)#03 pc 000000000005a48c /system/lib64/libclang_rt.asan.so(d3894082b99f633c446cd1895b6190bd6a0bad31)#04 pc 00000000000d64e8 /system/lib64/libclang_rt.asan.so(d3894082b99f633c446cd1895b6190bd6a0bad31)#05 pc 00000000000d88ac /system/lib64/libclang_rt.asan.so(d3894082b99f633c446cd1895b6190bd6a0bad31)#06 pc 00000000000d2624 /system/lib64/libclang_rt.asan.so(__asan_memmove+468)(d3894082b99f633c446cd1895b6190bd6a0bad31)#07 pc 000000000064a264 /data/local/tmp/msc_cpp_test/libnetwork.so(std::__n1::pair<int const*, int*> std::__n1::__copy_impl[abi:v15004]<int const, int, void>(int const*, int const*, int*)+376)(f3db319579d1a289ab34f7fab2eb24eb1da4921e)./llvm-addr2line -Cfpie libnetwork.so 000000000064a264mt_network::WebSocket::Impl::Impl() at /Users/xxx/workspace/workspace/123460300/22012/s/network/src/main/cpp/websocket/websocket.cpp:114#08 pc 0000000000649ab0 /data/local/tmp/msc_cpp_test/libnetwork.so(std::__n1::pair<int const*, int*> std::__n1::__copy[abi:v15004]<int const*, int const*, int*, 0>(int const*, int const*, int*)+600)(f3db319579d1a289ab34f7fab2eb24eb1da4921e)./llvm-addr2line -Cfpie libnetwork.so 0000000000649ab0unsigned long std::__n1::allocator_traits<std::__n1::allocator<std::__n1::__shared_ptr_emplace<mt_network::WebSocket::Impl, std::__n1::allocator<mt_network::WebSocket::Impl>>>>::max_size[abi:v15004]<std::__n1::allocator<std::__n1::__shared_ptr_emplace<mt_network::WebSocket::Impl, std::__n1::allocator<mt_network::WebSocket::Impl>>>, void>(std::__n1::allocator<std::__n1::__shared_ptr_emplace<mt_network::WebSocket::Impl, std::__n1::allocator<mt_network::WebSocket::Impl>>> const&) at /Users/xxx/.meat/sdk/default/base/native/llvm/bin/…/include/libcxx-ohos/include/c++/v1/__memory/allocator_traits.h:326#09 pc 0000000000649720 /data/local/tmp/msc_cpp_test/libnetwork.so(int* std::__n1::copy[abi:v15004]<int const*, int*>(int const*, int const*, int*)+296)(f3db319579d1a289ab34f7fab2eb24eb1da4921e)./llvm-addr2line -Cfpie libnetwork.so 0000000000649720std::__n1::__allocation_guard<std::__n1::allocator<std::__n1::__shared_ptr_emplace<mt_network::WebSocket::Impl, std::__n1::allocator<mt_network::WebSocket::Impl>>>>::__release_ptrabi:v15004 at /Users/xxx/.meat/sdk/default/base/native/llvm/bin/…/include/libcxx-ohos/include/c++/v1/__memory/allocation_guard.h:6
```

**解决方案**

网络单元测试用例崩溃的原因是 `container\_overflow`。该检测项存在较多误报，目前通过环境变量关闭。测试用例未设置 ASAN 对应的环境变量，因此触发了该检测，导致误报。解决方法是在运行测试用例时设置 ASAN 环境变量。在执行的 Linux 脚本中添加以下两条命令：

```
1. sh
2. export ASAN_OPTIONS=detect_container_overflows=0
```
