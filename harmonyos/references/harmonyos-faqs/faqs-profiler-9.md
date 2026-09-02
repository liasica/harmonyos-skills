---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-9
title: 应用体检在MacOS X86_64的系统上无法进行检测
breadcrumb: FAQ > DevEco Studio > 性能分析 > 应用体检在MacOS X86_64的系统上无法进行检测
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:15cb9c797497a910fae0d39e39ef2ad71ba51f0660e4364173f3ba8ffe69d113
---

**问题现象**

MacOS X86\_64上无法使用应用体检，加载FFmpeg 7.1-1.5.11库异常或者有DevEco Studio Crash问题。

```text
java.lang.UnsatisfiedLinkError: no jniavutil in java.library.path: /Users/username/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:.
at java.base/java.lang.ClassLoader.loadLibrary(ClassLoader.java:2458)
at java.base/java.lang.Runtime.loadLibrary0(Runtime.java:916)
at java.base/java.lang.System.loadLibrary(System.java:2063)
at org.bytedeco.javacpp.Loader.loadLibrary(Loader.java:1832)
at org.bytedeco.javacpp.Loader.load(Loader.java:1423)
at org.bytedeco.javacpp.Loader.load(Loader.java:1234)
at org.bytedeco.javacpp.Loader.load(Loader.java:1210)
at org.bytedeco.ffmpeg.global.avutil.<clinit>(avutil.java:14)
at java.base/java.lang.Class.forName0(Native Method)
at java.base/java.lang.Class.forName(Class.java:534)
at java.base/java.lang.Class.forName(Class.java:513)
at org.bytedeco.javacpp.Loader.load(Loader.java:1289)
at org.bytedeco.javacpp.Loader.load(Loader.java:1234)
at org.bytedeco.javacpp.Loader.load(Loader.java:1210)
at org.bytedeco.ffmpeg.global.avcodec.<clinit>(avcodec.java:18)
......more
at java.base/java.security.ProtectionDomain$JavaSecurityAccessImpl.doIntersectionPrivilege(ProtectionDomain.java:87)
at java.desktop/java.awt.EventQueue.dispatchEvent(EventQueue.java:750)
at com.intellij.ide.IdeEventQueue.defaultDispatchEvent(IdeEventQueue.kt:675)
at com.intellij.ide.IdeEventQueue._dispatchEvent(IdeEventQueue.kt:573)
at com.intellij.ide.IdeEventQueue.dispatchEvent$lambda$18$lambda$17$lambda$16$lambda$15(IdeEventQueue.kt:355)
at com.intellij.openapi.progress.impl.CoreProgressManager.computePrioritized(CoreProgressManager.java:857)
at com.intellij.ide.IdeEventQueue.dispatchEvent$lambda$18$lambda$17$lambda$16(IdeEventQueue.kt:354)
at com.intellij.ide.IdeEventQueueKt.performActivity$lambda$2$lambda$1(IdeEventQueue.kt:1045)
at com.intellij.openapi.application.WriteIntentReadAction.lambda$run$0(WriteIntentReadAction.java:24)
at com.intellij.openapi.application.impl.AnyThreadWriteThreadingSupport.runWriteIntentReadAction(AnyThreadWriteThreadingSupport.kt:128)
at com.intellij.openapi.application.impl.ApplicationImpl.runWriteIntentReadAction(ApplicationImpl.java:917)
at com.intellij.openapi.application.WriteIntentReadAction.compute(WriteIntentReadAction.java:55)
at com.intellij.openapi.application.WriteIntentReadAction.run(WriteIntentReadAction.java:23)
at com.intellij.ide.IdeEventQueueKt.performActivity$lambda$2(IdeEventQueue.kt:1045)
at com.intellij.ide.IdeEventQueueKt.performActivity$lambda$3(IdeEventQueue.kt:1054)
at com.intellij.openapi.application.TransactionGuardImpl.performActivity(TransactionGuardImpl.java:109)
at com.intellij.ide.IdeEventQueueKt.performActivity(IdeEventQueue.kt:1054)
at com.intellij.ide.IdeEventQueue.dispatchEvent$lambda$18(IdeEventQueue.kt:349)
at com.intellij.ide.IdeEventQueue.dispatchEvent(IdeEventQueue.kt:395)
at java.desktop/java.awt.EventDispatchThread.pumpOneEventForFilters(EventDispatchThread.java:207)
at java.desktop/java.awt.EventDispatchThread.pumpEventsForFilter(EventDispatchThread.java:128)
at java.desktop/java.awt.EventDispatchThread.pumpEventsForHierarchy(EventDispatchThread.java:117)
at java.desktop/java.awt.EventDispatchThread.pumpEvents(EventDispatchThread.java:113)
at java.desktop/java.awt.EventDispatchThread.pumpEvents(EventDispatchThread.java:105)
at java.desktop/java.awt.EventDispatchThread.run(EventDispatchThread.java:92)
Caused by: java.lang.UnsatisfiedLinkError: /Users/username/.javacpp/cache/ffmpeg-7.1-1.5.11-macosx-x86_64.jar/org/bytedeco/ffmpeg/macosx-x86_64/libjniavutil.dylib: dlopen(/Users/username/.javacpp/cache/ffmpeg-7.1-1.5.11-macosx-x86_64.jar/org/bytedeco/ffmpeg/macosx-x86_64/libjniavutil.dylib, 1): Symbol not found: _CVBufferCopyAttachments
  Referenced from: /Users/username/.javacpp/cache/ffmpeg-7.1-1.5.11-macosx-x86_64.jar/org/bytedeco/ffmpeg/macosx-x86_64/./libavutil.59.dylib (which was built for Mac OS X 12.0)
  Expected in: /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo

at java.base/jdk.internal.loader.NativeLibraries.load(Native Method)
at java.base/jdk.internal.loader.NativeLibraries$NativeLibraryImpl.open(NativeLibraries.java:331)
at java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:197)
at java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:139)
at java.base/java.lang.ClassLoader.loadLibrary(ClassLoader.java:2418)
at java.base/java.lang.Runtime.load0(Runtime.java:852)
at java.base/java.lang.System.load(System.java:2025)
at org.bytedeco.javacpp.Loader.loadLibrary(Loader.java:1779)
```

**可能原因**

FFmpeg 7.1-1.5.11与MacOS X86\_64系统低版本有兼容性问题。

**解决措施**

需要升级最新版本的MacOSX86\_64系统。
