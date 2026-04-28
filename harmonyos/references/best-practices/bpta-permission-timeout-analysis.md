---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-permission-timeout-analysis
title: 分析任务执行超时问题
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析任务执行超时问题
category: best-practices
scraped_at: 2026-04-28T08:22:23+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:df9a8a6d6e8c95b53a7109960bab70ce6ccc5c5cd866c767ba6798f94f19ec32
---

在应用开发过程中，开发者希望某段业务逻辑能在预期时间内完成执行。如果该业务逻辑的执行时间超过了预期，即被视为任务超时。

任务超时检测包括主线程超时检测和任务执行超时检测，这两种检测均可通过HiCollie实现，以自定义时长对选定的业务逻辑进行主动监控。对于主线程超时，也可以选择使用默认时长进行检测。详情请参阅：[HiCollie使用指导](../harmonyos-guides/hicollie.md)。

任务执行超时检测的原理、日志获取方式及规格，请参阅：[任务超时检测](../harmonyos-guides/apptask-timeout-guidelines.md)。

## 分析思路

1. 主线程超时

   [主线程超时检测](../harmonyos-guides/apptask-timeout-guidelines.md#主线程超时检测)实际利用多次采样堆栈，并聚类的原理来提供最终堆栈。分析此类问题时，开发者只需关注与业务逻辑相关的堆栈（命中次数最高者），并进行优化即可。
2. 任务执行超时

   由于任务执行超时分析方法与应用冻屏分析方法一致，可参考[应用冻屏（AppFreeze）问题排查方法](bpta-stability-app-freeze-way.md)。

## 分析步骤

1. 示例：主线程超时采样堆栈，数字表示采样命中次数

   ```
   1. 9 #00 pc 0000757c /system/bin/appspawn(55679d09bcdea35bb1e0d4e1d9a3e58f)
   2. 9 #01 pc 000731c0 /system/lib/ld-musl-aarch64.so.1(add9e521e4eaf5cb009d4260f3b69ccd)
   3. 9 #02 pc 000090a9 /system/bin/appspawn(main+396)(55679d09bcdea35bb1e0d4e1d9a3e58f)
   4. 9 #03 pc 0000ab5d /system/bin/appspawn(AppSpawnRun+100)(55679d09bcdea35bb1e0d4e1d9a3e58f)
   5. 9 #04 pc 0000e7f1 /system/lib/chipset-pub-sdk/libbegetutil.z.so(RunLoop_+200)(52ace27d827ad482439bf32cc75bb17b)
   6. ......
   7. 9 #21 pc 00107aec /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+628)(add9e521e4eaf5cb009d4260f3b69ccd)
   8. 1 #00 pc 00032e67 /system/lib/platformsdk/libmmi-util.z.so(OHOS::MMI::UDSSocket::OnReadPackets(OHOS::MMI::CircleStreamBuffer&, std::__h::function<void (OHOS::MMI::NetPacket&)>)+158)(99e56bc765f9208f7b7ba8b268886a59)
   9. 1 #01 pc 0000312e5 /system/lib/platformsdk/libmmi-client.z.so(OHOS::MMI::ClientMsgHandler::OnMsgHandler(OHOS::MMI::UDSClient const&, OHOS::MMI::NetPacket&)+340)(66ac85e964777ae89f0c26c339093cd1)
   10. 1 #02 pc 0003016b /system/lib/platformsdk/libmmi-client.z.so(OHOS::MMI::ClientMsgHandler::OnPointerEvent(OHOS::MMI::UDSClient const&, OHOS::MMI::NetPacket&)+1222)(66ac85e964777ae89f0c26c339093cd1)
   11. 1 #03 pc 0003b96b /system/lib/platformsdk/libmmi-client.z.so(OHOS::MMI::InputManagerImpl::OnPointerEvent(std::__h::shared_ptr<OHOS::MMI::PointerEvent>)+1370)(66ac85e964777ae89f0c26c339093cd1)
   12. 1 #04 pc 00095903 /system/lib/platformsdk/libwm.z.so(OHOS::Rosen::InputEventListener::OnInputEvent(std::__h::shared_ptr<OHOS::MMI::PointerEvent>) const+478)(9c40c5f416d6f830435126998fbcad42)
   13. ......
   14. 1 #21 pc 003f5c55 /system/lib/platformsdk/libark_jsruntime.so(4e6a2651ec80a7f639233f414d6486fe)
   15. 1 #22 at anonymous (/entry/build/default/cache/default/default@CompileArkTS/esmodule/debug/entry/src/main/ets/pages/Index.js:67:17)
   16. 1 #23 at wait2 (/entry/build/default/cache/default/default@CompileArkTS/esmodule/debug/entry/src/main/ets/pages/Index.js:16:12)
   17. ......
   ```

   如上述示例所示，通过订阅相关事件获取日志信息后，按照#xx前的数字排查，排除系统侧堆栈之后，查找与业务逻辑相关的堆栈，数字越高表示采样栈命中次数越高，需要优化的可能性越大。如上述案例所示，需要分析#22业务执行耗时逻辑是否合理。
2. 任务执行超时分析步骤同[应用冻屏（AppFreeze）定位步骤与思路](bpta-stability-app-freeze-way.md#section1950514261110)。
